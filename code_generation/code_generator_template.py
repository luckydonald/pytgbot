# -*- coding: utf-8 -*-
import os

from collections import Mapping
from itertools import chain
from typing import List, Optional, Tuple, Union, Callable, Set

from jinja2 import  Environment, FileSystemLoader
from jinja2.exceptions import TemplateSyntaxError
from luckydonaldUtils.exceptions import assert_type_or_raise

from luckydonaldUtils.logger import logging
from luckydonaldUtils.decorators import cached
from luckydonaldUtils.imports.relative import relimport

try:
    from code_generator import safe_var_translations, get_type_path, convert_to_underscore
    from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT
    from code_generator_settings import MESSAGE_CLASS_OVERRIDES, TYPE_STRING_OVERRIDES
except ImportError:
    from .code_generator import safe_var_translations, get_type_path, convert_to_underscore
    from .code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT
    from .code_generator_settings import MESSAGE_CLASS_OVERRIDES, TYPE_STRING_OVERRIDES
# end if

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


try:
    from luckydonaldUtils.imports.representation import path_to_import_text, split_path
    logger.warning('Please remove the old code now that this feature is in luckydonaldUtils.')
except ImportError:
    # define those functions manually until I get around to push an update to luckydonaldUtils.

    def split_path(path):
        """
        Splits the text and build a nice import statement from it.
        Note: only well defined import paths are supported. Not something invalid like '..foo.bar..'.

        :param path: The path to split.
        :type  path: str

        :return: The import text, like `from x import y` or `import z`
        :rtype: tuple(str)|Tuple[str, str]
        """
        last_dot_position = path.rfind('.')
        if last_dot_position == -1:
            # no dot found.
            import_path = ''
            import_name = path
        else:
            import_path = path[:last_dot_position + 1]
            import_name = path[last_dot_position + 1:]

            # handle 'foo.bar.Baz' not resulting in 'foo.bar.', i.e. remove the dot at the end.
            if import_path.rstrip('.') != '':
                # e.g. not '....'
                import_path = import_path.rstrip('.')
        # end if
        return import_path, import_name
    # end def


    def path_to_import_text(path):
        """
        Splits the text and build a nice import statement from it.
        Note: only well defined import paths are supported. Not something invalid like '..foo.bar.'

        :param path: The path to split.
        :type  path: str

        :return: The import text, like `from x import y` or `import z`
        :rtype: str
        """
        import_path, import_name = split_path(path)

        if import_path:
            return 'from {import_path} import {import_name}'.format(import_path=import_path, import_name=import_name)
        # end if
        return 'import {import_name}'.format(import_name=import_name)
    # end def
# end try


class RelEnvironment(Environment):
    """
    Override join_path() to enable relative template paths.

    http://stackoverflow.com/a/8530761/3423324
    """
    def join_path(self, template, parent):
        return os.path.join(os.path.dirname(parent), template)
    # end def join_path
# end class RelEnvironment


def get_template(file_name):
    env = RelEnvironment(loader=FileSystemLoader("templates"))
    import os
    try:
        return env.get_template(file_name)
    except TemplateSyntaxError as e:
        logger.warn("{file}:{line} {msg}".format(msg=e.message, file=e.filename if e.filename else file_name, line=e.lineno))
        raise e
    # end with
# end def get_template


def clazz(clazz, parent_clazz, description, link, params_string, init_super_args=None):
    """
    Live template for pycharm:

    y = clazz(clazz="$clazz$", parent_clazz="%parent$", description="$description$", link="$lnk$", params_string="$first_param$")
    """
    variables_needed = []
    variables_optional = []
    imports: Set[Variable] = set()
    for param in params_string.split("\n"):
        variable = parse_param_types(param)
        # any variable.types has always_is_value => lenght must be 1.
        assert(not any([type_.always_is_value is not None for type_ in variable.types]) or len(variable.types) == 1)
        if variable.optional:
            variables_optional.append(variable)
        else:
            variables_needed.append(variable)
        # end if
        imports.update(variable.all_imports)
    # end for
    imports: List[Variable] = list(imports)
    imports.sort()
    if isinstance(parent_clazz, str):
        parent_clazz = to_type(parent_clazz, "parent class", int_is_unix_timestamp=False)
    assert isinstance(parent_clazz, Type)

    clazz_object = Clazz(
        imports=imports,
        clazz=clazz, parent_clazz=parent_clazz, link=link, description=description,
        parameters=variables_needed, keywords=variables_optional
    )
    return clazz_object
# end def clazz


def func(command, description, link, params_string, returns="On success, the sent Message is returned.", return_type="Message"):
    """
    Live template for pycharm:

    y = func(command="$cmd$", description="$desc$", link="$lnk$", params_string="$first_param$", returns="$returns$", return_type="$returntype$")
    """
    variables_needed = []
    variables_optional = []
    imports = set()
    if params_string:  # WHITELISTED_FUNCS have no params
        for param in params_string.split("\n"):
            variable = parse_param_types(param)
            # any variable.types has always_is_value => lenght must be 1.
            assert (not any([type_.always_is_value is not None for type_ in variable.types]) or len(variable.types) == 1)
            if variable.optional:
                variables_optional.append(variable)
            else:
                variables_needed.append(variable)
            # end if
            imports.update(variable.all_imports)
        # end for
    # end if
    imports = list(imports)
    imports.sort()
    returns = Variable(types=as_types(return_type, variable_name="return type", int_is_unix_timestamp=False), description=returns)
    func_object = Function(
        imports=imports, api_name=command, link=link, description=description, returns=returns,
        parameters=variables_needed, keywords=variables_optional
    )
    return func_object
# end def


class KwargableObject(Mapping):
    """ allow `**self`, and include all @property s """
    def __getitem__(self, key):
        try:
            return self.__getattribute__(key)
        except AttributeError as e:
            raise KeyError(key)
        # end try
    # end def __getitem__

    def __len__(self):
        return len(list(self.__iter__()))
    # end def __len__

    def __iter__(self):
        import inspect
        def is_allowed(value):
            return isinstance(value, property)
        # end def is_allowed
        return iter(
            [name for (name) in vars(self) if not name.startswith("_")] +
            [name for (name, value) in inspect.getmembers(Clazz, is_allowed)]
        )
    # end def __iter__

    def __repr__(self):
        return (
            "{s.__class__.__name__}(" +
            (", ".join(["{key}={value!r}".format(key=k, value=self[k]) for k in self])) +
            ")"
        ).format(s=self)
    # end def __repr__
# end class KwargableObject


class ClassOrFunction(KwargableObject):
    def __init__(self, filepath=None):
        """
        :param filepath: where this function or class should be stored.
        """
        self.filepath = filepath
# end class ClassOrFunction


class Clazz(ClassOrFunction):
    def __init__(
        self, clazz: Union[None, str] = None, import_path: Union[None, 'Import'] = None,
        imports: Union[None, List['Import']]=None,
        parent_clazz=None, link=None, description=None, parameters=None, keywords=None,
    ):
        super(Clazz, self).__init__()
        self.clazz = clazz
        self.import_path = import_path if import_path else self.calculate_import_path()
        self.imports = imports if imports else []  # Imports needed by parameters and keywords.
        self.parent_clazz = parent_clazz if parent_clazz is not None else Type("object", is_builtin=True)
        assert_type_or_raise(self.parent_clazz, Type, parameter_name="self.parent_clazz")
        self.link = link
        self.description = description
        self.parameters = parameters if parameters else []
        self.keywords = keywords if keywords else []
    # end def __init__

    def calculate_import_path(self) -> 'Import':
        import_path = get_type_path(self.clazz, as_object=True)
        return import_path
    # end def

    def calculate_filepath(self, folder: str):
        from code_generator_online import calc_path_and_create_folders
        return calc_path_and_create_folders(folder, self.import_path.path + '.' + self.import_path.name)
    # end def

    @property
    def variables(self):
        return self.parameters + self.keywords
    # end def variables

    def __repr__(self):
        return (
            "Clazz("
                "clazz={s.clazz!r}, import_path={s.import_path!r}, imports={s.imports!r}, parent_clazz={s.parent_clazz!r}"
                ", link={s.link!r}, description={s.description!r}, parameters={s.parameters!r}, keywords={s.keywords!r}"
            ")"
        ).format(s=self)
    # end def __repr__
# end class Clazz

class CustomClazz(Clazz):
    """
    Like a class, but contains text.
    """




class Function(ClassOrFunction):
    def __init__(self, api_name=None, imports: List['Import']=None, link=None, description=None, returns=None, parameters: List['Variable']=None, keywords=None):
        super(Function, self).__init__()
        self.api_name = api_name  # api_name
        self.imports = imports if imports else []
        self.link = link
        self.description = description
        self.returns = returns
        self.parameters = parameters
        self.keywords = keywords
    # end def __init__

    @property
    def variables(self):
        return self.parameters + self.keywords
    # end def variables

    @property
    def variable_names(self):
        return [var.name for var in self.variables]
    # end def variable_names

    @property
    def name(self):
        return convert_to_underscore(self.api_name)
    # end def name

    def __repr__(self):
        return (
            "Function("
                "api_name={s.api_name!r}, imports={s.imports!r}, link={s.link!r}, description={s.description!r}, "
                "returns={s.returns!r}, parameters={s.parameters!r}, keywords={s.keywords!r}"
            ")".format(s=self)
        )
    # end def __repr__

    @property
    def class_name(self) -> str:
        """
        Makes the fist letter big, keep the rest of the camelCaseApiName.
        """
        if not self.api_name:  # empty string
            return self.api_name
        # end if
        return self.api_name[0].upper() + self.api_name[1:]
    # end def

    @property
    def class_name_teleflask_message(self) -> str:
        """
        If it starts with `Send` remove that.
        """
        # strip leading "Send"
        name = self.class_name  # "sendPhoto" -> "SendPhoto"
        name = name[4:] if name.startswith('Send') else name  # "SendPhoto" -> "Photo"
        name = name + "Message"  # "Photo" -> "PhotoMessage"

        # e.g. "MessageMessage" will be replaced as "TextMessage"
        # b/c "sendMessage" -> "SendMessage" -> "Message" -> "MessageMessage"  ==> "TextMessage"
        if name in MESSAGE_CLASS_OVERRIDES:
            return MESSAGE_CLASS_OVERRIDES[name]
        # end if
        return name
    # end def

    @property
    @cached
    def class_variables_separated(self) -> Tuple[List['Variable'], List['Variable'], List['Variable']]:
        args = []
        special_kwargs = []  # receiver and reply_id
        kwargs = []
        args_and_kwargs = chain((('arg', arg) for arg in self.parameters), (('kwarg', kwarg) for kwarg in self.keywords))
        for variable, param in args_and_kwargs:
            if param.name == "chat_id":
                # :param receiver: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                # :type  receiver: int|str
                default = Type(
                    'None',
                    is_builtin=True,
                    always_is_value=None,
                    is_list=False,
                    import_path=None,
                    description="Use the chat from the update context."
                )

                special_kwargs.append(Variable(
                    api_name=param.api_name,
                    pytg_name=param.name,
                    name='receiver',
                    types=[
                        default,
                        Type(
                            'str',
                            is_builtin=True,
                            always_is_value=None,
                            is_list=False,
                            import_path=None,
                            description="The @username of user/group/channel."
                        ),
                        Type(
                            'int',
                            is_builtin=True,
                            always_is_value=None,
                            is_list=False,
                            import_path=None,
                            description="The chat's id."
                        )
                    ],
                    optional=True,
                    default=default,
                    description="Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations."
                ))
            elif param.name == "reply_to_message_id":
                # :param reply_id: If the messages are a reply, ID of the original message
                # :type  reply_id: int
                default = Type(
                    'DEFAULT_MESSAGE_ID',
                    is_builtin=True,
                    always_is_value='DEFAULT_MESSAGE_ID',
                    is_list=False,
                    import_path=None,
                    description="So you can overwrite it with `None` if you don't want a reply."
                )
                special_kwargs.append(Variable(
                    api_name=param.api_name,
                    name='reply_id',
                    pytg_name=param.name,
                    types=[
                        default,
                        Type(
                            'int',
                            is_builtin=True,
                            always_is_value=None,
                            is_list=False,
                            import_path=None,
                            description="A different `message_id` to reply to."
                        )
                    ],
                    optional=True,
                    default=default,
                    description="Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot."
                ))
            elif variable == 'arg':
                args.append(param)
            else:
                assert variable == 'kwarg'
                kwargs.append(param)
            # end if
        # end for
        return args, special_kwargs, kwargs
    # end def

    @property
    def class_parameters(self) -> List['Variable']:
        return self.class_variables_separated[0]
    # end def

    @property
    def class_keywords(self) -> List['Variable']:
        return self.class_variables_separated[1] + self.class_variables_separated[2]
    # end def

    @property
    @cached
    def class_variables(self):
        return self.class_parameters + self.class_keywords
    # end def

    @property
    def variables(self):
        return self.parameters + self.keywords
    # end def variables
# end class Function


class Variable(dict):
    def __init__(
            self,
            api_name: str = None,
            name: str = None,
            pytg_name: str = None,
            types: List['Type'] = None,
            optional: bool = None,
            default: Union[None, str, 'Type'] = None,
            description: Optional[str] = None
    ):
        """
        :param api_name: Name the telegram api uses.
        :param name: Internal name we use.
        :param pytg_name: Internal name we use with pytg's send_* functions in the teleflask message classes.
        :param types: `list` of :class:`Type`.  [Type(int), Type(bool)]  or  [Type(Message)]  etc.
        :param optional: If it is not needed. `True` will be a normal parameter, `False` means a kwarg.
        :param default: If it is optional, that is the default value. Else it uses "None" via templating.
        :param description:
        """
        self.api_name = api_name                           # parse_param_types(param)
        self.name = name if name else api_name             # parse_param_types(param)
        self.types = types if types else []                # parse_param_types(param)
        self.pytg_name = pytg_name if pytg_name else name  # teleflask messages
        self.optional = optional  # bool                   # parse_param_types(param)
        self.default = default  # bool
        self.description = description  # some text about it.  # parse_param_types(param)
    # end def

    """
    Get all needed Imports.

    :return: Return set of all needed :class:`Import` s.
    :rtype: set
    """
    @property
    def all_imports(self):
        imports = set()
        for type in self.types:
            if type.import_path:
                imports.add(Import(type.import_path.rstrip('.'), type.string))
            # end if
        # end for
        return imports
    # end def all_imports

    @property
    def typehint(self) -> str:
        """
        Returns a python 3.5+ type hint string.

        Depending on the amount of types in the self.types list.
        - For 0 elements, the returned type is `Any`.
        - For 1 element it's just that type.
        - For more elements it's a `Union[...]`.

        :uses: Variable.types
        :uses: Type.typehint
        """
        if len(self.types) == 0:
            return "Any"
        # end if
        if len(self.types) == 1:
            return self.types[0].typehint
        # end if
        return (", ".join(t.typehint for t in self.types)).join(("Union[", "]"))
    # end def

    @property
    def typehint_optional(self):
        if self.optional:
            return self.typehint.join(("Optional[", "]"))
        # end if
        return self.typehint
    # end def

    @property
    def typehint_has_model(self):
        for t in self.types:
            if not t.is_builtin:
                return True
            # end if
        # end for
        return False
    # end def

    @property
    def typehint_optional_model(self):
        """
        Creates a typehint without Json type.
        For type annotations of the parsed variable, and for final validation.
        See https://github.com/tiangolo/fastapi/issues/884.
        """
        return self.create_typehint_optional_model(json_mode=False)
    # end def

    @property
    def typehint_optional_model_json(self):
        """
        Creates a typehint with Json type for fastapi query params.
        See https://github.com/tiangolo/fastapi/issues/884.
        """
        return self.create_typehint_optional_model(json_mode=True)
    # end def

    def create_typehint_optional_model(self, json_mode: bool = False, quote_models: bool = True):
        """
        :param json_mode: If we should wrap the thing in `Json[...]`
        :param quote_models: If we should wrap models in quotes for resolving them later.

        Examples:
            - `param.create_typehint_optional_model(json_mode=True, quote_models=True)`:
              Creates a typehint with Json[...'FooModel'...] type for fastapi query params.

            - `param.create_typehint_optional_model(json_mode=True, quote_models=True)`:
              Creates a typehint with a quoted 'FooModel' for lazy loading models, i.e. when using in arguments of depending models.

            - `param.create_typehint_optional_model(json_mode=False, quote_models=False)`
              Creates a typehint without `Json` type, for type annotations of the parsed variable, and e.g. for final validation with `parse_obj_as`.
        """
        if len(self.types) == 0:
            type_str = "Any"
        else:
            if quote_models:
                wrap_models: Callable[[str], str] = lambda type_str: f'{f"{type_str}Model"!r}'
            else:
                wrap_models: Callable[[str], str] = lambda type_str: f'{type_str}Model'
            # end if
            if len(self.types) == 1:
                type_str = self.create_model(self.types[0], wrap_models=wrap_models)
            else:
                type_str = (
                    ", ".join(self.create_model(t, wrap_models=wrap_models) for t in self.types)
                ).join(("Union[", "]"))
            # end if
        # end if

        if json_mode and self.typehint_has_model:
            type_str = type_str.join(("Json[", "]"))
        # end def

        if self.optional:
            type_str = type_str.join(("Optional[", "]"))
        # end if
        return type_str
    # end def


    @staticmethod
    def create_model(the_type: 'Type', wrap_models: Union[None, Callable[[str], str]] = None):
        type_str = the_type.string
        if wrap_models and not the_type.is_builtin:
            # noinspection PyCompatibility
            type_str = wrap_models(type_str)
        # end def
        for i in range(the_type.is_list):
            type_str = type_str.join(("List[", "]"))
        # end def
        return type_str
    # end def

    def __repr__(self):
        return (
            "Variable("
                "api_name={s.api_name!r}, name={s.name!r}, pytg_name={s.pytg_name!r}, types={s.types!r}, "
                "optional={s.optional!r}, default={s.default!r}, description={s.description!r}"
            ")"
        ).format(s=self)
    # end def __repr__
# end class Variable


class Type(dict):
    def __init__(self, string=None, is_builtin=None, always_is_value=None, is_list=0, import_path=None, description=None):
        """
        Stores variable types.

        :param string: the type (e.g. "bool")
        :type  string: str

        :param is_builtin: If it is a build in type (:class:`float`, :class:`int`, ...)
                           or not (classes like :class:`Message`, :class:`Peer`...)
        :type  is_builtin: bool

        :param always_is_value: None or the only possible value (e.g. a bool, always "True")
        :type  always_is_value: None or str

        :param is_list:  Levels of lists.
                        `0` = not a list.
                        `1` = it is an list of :param:`string`s type (e.g. list of bool could be [True, False] ).
                        If is "list of list of" that value is `2`
        :type  is_list: int

        :param import_path: from <import_path> import <string>. None for builtins.
        :type  import_path: str or None

        :param description:  if there are additional comments needed.
        :type  description: str or None
        """
        super(Type, self).__init__()
        self.string = string  # the type (e.g. "bool")
        self.is_builtin = is_builtin  # bool.  If it is a build in type (float, int, ...) or not.
        self.always_is_value = always_is_value  # None or the only possible value (e.g. a bool, always "True")
        self.is_list = is_list
        self.import_path = import_path  # from <import_path> import <string>
        self.description = description  # if there are additional comments needed.
    # end def __init__

    @property
    def as_import(self):
        return Import(self.import_path, self.string)
    # end def as_import

    @property
    def typehint(self) -> str:
        """
        Returns a python 3.5+ type hint string.
        """
        type_str = self.string
        for i in range(self.is_list):
            type_str = type_str.join(("List[", "]"))
        # end for
        return type_str
    # end def

    def __str__(self):
        return "{list}<{name}>".format(list="list of " * self.is_list, name=self.string)
    # end def __str__

    def __repr__(self):
        return (
            "Type("
                "string={s.string!r}, is_builtin={s.is_builtin!r}, always_is_value={s.always_is_value!r}, "
                "is_list={s.is_list!r}, import_path={s.import_path!r}, description={s.description!r}"
            ")"
        ).format(s=self)
    # end def __repr__
# end class Type


class Import(dict):
    """ from <path> import <name> """
    def __init__(self, path=None, name=None):
        super(Import, self).__init__()
        self.path = path
        self.name = name
    # end def __init__

    def relative_import_full(self, base_path: Union[str, 'Import']):
        if isinstance(base_path, Import):
            base_path: str = base_path.path
        # end if

        return relimport(self.full, base_path)
    # end def

    @property
    def full(self):
        """ self.path + "." + self.name """
        if self.path:
            if self.name:
                return self.path + "." + self.name
            else:
                return self.path
            # end if
        else:
            if self.name:
                return self.name
            else:
                return ""
            # end if
        # end if
    # end def full

    def import_statement_from_file(self, base_path: Union[str, None] = None):
        """
        :param base_path: If None does absolute import.
        :return:
        """
        if base_path is None:
            path = self.full
        else:
            path = self.relative_import_full(base_path=base_path)
        # end if
        return path_to_import_text(path)
    # end def

    def __str__(self):
        return self.full
    # end def

    def __hash__(self):
        path = self.path if self.path else "%$none"
        name = self.name if self.name else "%$none"
        return hash(path + name)
    # end def __hash__

    """
    If it is bigger (+1), equal (0) or less (-1)
    :return: +1, 0 or -1
    :rtype: int
    """
    def compare(self, other):
        self_path = "" if self.path is None else self.path
        other_path = "" if other.path is None else other.path
        if self_path < other_path:
            return -1
        elif self_path > other_path:
            return +1
        elif self.name < other.name:
            return -1
        elif self.name > other.name:
            return +1
        else:
            return 0
        # end if
    # end def compare

    """ self >= other """
    def __ge__(self, other):
        return self.compare(other) >= 0
    # end def __ge__

    """ self > other """
    def __gt__(self, other):
        return self.compare(other) > 0
    # end def __gt__

    """ self == other """
    def __eq__(self, other):
        return self.compare(other) == 0
    # end def __eq__

    """ self <= other """
    def __le__(self, other):
        return self.compare(other) <= 0
    # end def __le__

    """ self < other """
    def __lt__(self, other):
        return self.compare(other) < 0
    # end def __lt__

    """ self != other """
    def __ne__(self, other):
        return self.compare(other) != 0
    # end def __ne__

    def __repr__(self):
        return (
            "Import("
                "path={s.path!r}, name={s.name!r}"
            ")"
        ).format(s=self)
    # end def __repr__
# end class Import


def parse_param_types(param) -> Variable:
    # ## "message_id\tString or Boolean\tUnique message identifier"
    table = param.split("\t")
    variable = Variable()

    variable.api_name = table[0].strip()
    if len(table) == 3:  # class
        variable.description = table[2].replace('“', '"').replace('”', '"')
        variable.optional = variable.description.startswith("Optional.")
    else:  # function
        variable.description = table[3].replace('“', '"').replace('”', '"')
        param_required = table[2].strip().lower()
        if param_required == "yes":
            variable.optional = False
        elif param_required == "optional":
            variable.optional = True
        elif param_required == "no":
            variable.optional = True  # https://core.telegram.org/bots/api#editmessagetext
        else:
            raise AssertionError("table[2] required \"{requiered}\" not in [\"yes\", \"optional\"]".format(requiered=param_required))
        # end if
    # end
    if not variable.optional and "optional" in variable.description.lower():
        logger.warn("Found \"optional\" in non-optional variable {variable_name}. Description:\n".format(variable_name=variable.api_name))

    if variable.api_name in safe_var_translations:
        variable.name = safe_var_translations[variable.api_name]
    else:
        variable.name = variable.api_name
    # end if

    param_types = table[1]
    # ## " String or Boolean "
    is_unix_timestamp = "unix" in variable.description.lower()
    variable.types = as_types(param_types, variable.api_name, int_is_unix_timestamp=is_unix_timestamp)
    return variable
# end def


def as_types(types_string, variable_name, int_is_unix_timestamp: bool):
    # ## types_string = "String or Boolean"  or  [Type(str), Type(bool)]

    if isinstance(types_string, list):
        for typ in types_string:
            assert isinstance(typ, Type)
            # [Type(), Type(), ...]
        return types_string
    # end if

    # ## types_string = "String or Boolean"
    if types_string in TYPE_STRING_OVERRIDES:
        types_string = TYPE_STRING_OVERRIDES[types_string]
    else:
        types_string = types_string.strip().join([" ", " "])

        # ## types_string = " String or Boolean "
        types_string = types_string.replace(" Float number ", " float ")
        types_string = types_string.replace(" Float ", " float ")
        types_string = types_string.replace(" Array ", " list ")
        types_string = types_string.replace(" String ", " str ")
        types_string = types_string.replace(" Integer ", " int ")
        types_string = types_string.replace(" Int ", " int ")  # https://core.telegram.org/bots/api#getchatmemberscount
        types_string = types_string.replace(" Boolean ", " bool ")
        types_string = types_string.replace(" Nothing ", " None ")
        types_string = types_string.replace(" Null ", " None ")
        types_string = types_string.replace(" true ", " True ")

        types_string = types_string.replace(" or ", " | ")
        types_string = types_string.replace(" and ", " | ")
    # end if
    types_string = types_string.strip()
    # ## "str | bool"

    the_types = types_string.split("|")
    types = []
    for t in the_types:
        var_type = to_type(t.strip(), variable_name=variable_name, int_is_unix_timestamp=int_is_unix_timestamp)
        types.append(var_type)
    # end for
    return types
# end def


def to_type(type_string, variable_name, int_is_unix_timestamp: bool) -> Type:
    """
    Returns a :class:`Type` object of a given type name. Lookup is done via :var:`code_generator_settings.CLASS_TYPE_PATHS`

    :param type_string: The type as string. E.g "bool". Need to be valid python.
    :param variable_name: Only for logging, if an unrecognized type is found.
    :param int_is_unix_timestamp: if we encounter an `int`, should we instead assume a `datetime`?
    :return: a :class:`Type` instance
    :rtype: Type
    """
    # type_string = type_string.strip()
    # remove "list of " and set .is_list accordingly.
    # is_list, type_string = can_strip_prefix(type_string, "list of ")
    # var_type = Type(string=type_string, is_list=is_list)

    var_type = Type(type_string)
    # remove "list of " and set .is_list accordingly.
    is_list = True
    while is_list:
        is_list, var_type.string = can_strip_prefix(var_type.string, "list of ")
        if is_list:
            var_type.is_list += 1
        # end if
    # end for
    if var_type.string == "True":
        var_type.string = "bool"
        var_type.always_is_value = "True"
    # end if
    if var_type.string == "int" and int_is_unix_timestamp:
        var_type.is_builtin = False
        var_type.string = "datetime"
        var_type.import_path = "datetime"  # from datetime import datetime
    elif var_type.string in ["int", "bool", "float", "object", "None", "str"]:
        var_type.is_builtin = True
    elif var_type.string == "unicode_type":
        var_type.string = "unicode_type"
        var_type.is_builtin = False
        var_type.import_path = "luckydonaldUtils.encoding"
        var_type.description = "py2: unicode, py3: str"
    elif var_type.string in CLASS_TYPE_PATHS:
        var_type.import_path = CLASS_TYPE_PATHS[var_type.string][CLASS_TYPE_PATHS__IMPORT].rstrip(".")
        var_type.is_builtin = False
    else:
        logger.warn(
            "Added unrecognized type in param <{var}>: {type!r}".format(var=variable_name, type=var_type.string))
    # end if
    return var_type
# end def


def can_strip_prefix(text:str, prefix:str) -> (bool, str):
    """
    If the given text starts with the given prefix, True and the text without that prefix is returned.
    Else False and the original text is returned.

    Note: the text always is stripped, before returning.

    :param text:
    :param prefix:
    :return: (bool, str)  :class:`bool` whether he text started with given prefix, :class:`str` the text without prefix
    """
    if text.startswith(prefix):
        return True, text[len(prefix):].strip()
    return False, text.strip()
