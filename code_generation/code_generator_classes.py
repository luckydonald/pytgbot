from itertools import chain
from typing import Mapping, Union, List, Tuple, Optional, Callable

from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.functions import cached
from luckydonaldUtils.imports.relative import relimport


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


# noinspection PyCompatibility
class Clazz(ClassOrFunction):
    def __init__(
        self,
        clazz: Union[None, str] = None,
        import_path: Union[None, 'Import'] = None,
        imports: Union[None, List['Import']] = None,
        parent_clazz: Union[None, 'Type'] = None,
        link: Union[None, str] = None,
        description: Union[None, str] = None,
        parameters: Union[None, List['Variable']] = None,
        keywords: Union[None, List['Variable']] = None,
    ):
        super(Clazz, self).__init__()
        self.clazz = clazz
        self.import_path = import_path if import_path is not None else self.calculate_import_path()
        self.imports = imports if imports else []  # Imports needed by parameters and keywords.
        self.parent_clazz = parent_clazz if parent_clazz is not None else Type("object", is_builtin=True)
        self._parent_clazz_clazz = None
        assert_type_or_raise(self.parent_clazz, Type, parameter_name="self.parent_clazz")
        self.link = link
        self.description = description
        self.parameters = parameters if parameters else []
        self.keywords = keywords if keywords else []
    # end def __init__

    _parent_clazz_clazz: Union[None, 'Clazz']

    def calculate_import_path(self) -> 'Import':
        from code_generator import get_type_path
        import_path = get_type_path(self.clazz, as_object=True)
        return import_path
    # end def

    def calculate_filepath(self, folder: str) -> str:
        return self.import_path.calculate_filepath(folder)
    # end def

    @property
    def variables(self):
        return self.parameters + self.keywords
    # end def variables

    @cached
    def parent_clazz_has_same_variable(self, variable: 'Variable'):
        if not self._parent_clazz_clazz:
            return False
        # end if
        for parent_variable in self._parent_clazz_clazz.variables:
            if variable.compare(parent_variable, ignore_description=True):
                return True
            # end if
        # end for
        return False
    # end if

    def __repr__(self):
        return (
            "Clazz("
                "clazz={s.clazz!r}, import_path={s.import_path!r}, imports={s.imports!r}, parent_clazz={s.parent_clazz!r}"
                ", link={s.link!r}, description={s.description!r}, parameters={s.parameters!r}, keywords={s.keywords!r}"
            ")"
        ).format(s=self)
    # end def __repr__
# end class Clazz


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
        from code_generator import convert_to_underscore
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
        from code_generator_settings import MESSAGE_CLASS_OVERRIDES
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


# noinspection PyCompatibility
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

    @property
    def is_fixed_value(self) -> bool:
        if self.optional:
            # if it is "True or None" it is not "always True"
            return False
        # end if
        if len(self.types) != 1:
            # more than one possible value
            return False
        # end if
        # noinspection PyShadowingBuiltins
        type: Type = self.types[0]
        if type.always_is_value is None:
            # we have no such 'always' value set.
            return False
        # end if

        # we did all the checks, so it must be always be the same value.
        return True
    # end if

    @property
    def value_to_set(self):
        if not self.is_fixed_value:
            return self.name
        # end if

        # noinspection PyShadowingBuiltins
        type: Type = self.types[0]
        if type.always_is_value in ('True', 'False', 'None'):
            return type.always_is_value
        # end if
        return repr(type.always_is_value)  # so we get 'photo'
    # end def

    def __repr__(self):
        return (
            "Variable("
                "api_name={s.api_name!r}, name={s.name!r}, pytg_name={s.pytg_name!r}, types={s.types!r}, "
                "optional={s.optional!r}, default={s.default!r}, description={s.description!r}"
            ")"
        ).format(s=self)
    # end def __repr__

    def __eq__(self, other: object) -> bool:
        """ self == other """
        if not isinstance(other, self.__class__):
            return super().__eq__(other)
        # end if
        return self.compare(other, ignore_description=False)
    # end def __eq__

    def compare(self, other: 'Variable', ignore_description: bool = False):
        assert_type_or_raise(other, Variable, parameter_name='other')
        return (
            self.api_name == other.api_name and
            self.name == other.name and
            self.types == other.types and
            self.pytg_name == other.pytg_name and
            self.optional == other.optional and
            self.default == other.default and
            (ignore_description or self.description == other.description) and
            True
        )
    # end def compare
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
        self.is_list = is_list  # number denoting the list level. 0 means 'no list'. 1 is foo[], and 2 would be foo[][].
        self.import_path = import_path  # from <import_path> import <string>
        self.description = description  # if there are additional comments needed.
    # end def __init__

    @property
    def as_import(self) -> 'Import':
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

    def __eq__(self, other: object) -> bool:
        """ self == other """
        if not isinstance(other, self.__class__):
            return super().__eq__(other)
        # end if
        return self.compare(other, ignore_description=False)
    # end def __eq__

    def compare(self, other: 'Type', ignore_description: bool = False):
        assert_type_or_raise(other, Type, parameter_name='other')
        return (
            self.string == other.string and  # the type (e.g. "bool")
            self.is_builtin == other.is_builtin and  # bool.  If it is a build in type (float, int, ...) or not.
            self.always_is_value == other.always_is_value and  # None or the only possible value (e.g. a bool, always "True")
            self.is_list == other.is_list and  # number denoting the list level. 0 means 'no list'. 1 is foo[], and 2 would be foo[][].
            self.import_path == other.import_path and  # from <import_path> import <string>
            (ignore_description or self.description == other.description) and  # if there are additional comments needed.
            True
        )
    # end def compare
# end class Type


class Import(dict):
    """ from <path> import <name> """
    def __init__(self, path: Union[str, None] = None, name: Union[str, None] = None, is_init: bool = False):
        """
        from <path> import <name>

        :param path: part where to import from
        :param name: actual name to import
        :param is_init: if this is not `<name>.py`, but `<name>/__init__.py`.
        """
        super(Import, self).__init__()
        self.path = path
        self.name = name
        self.is_init = is_init
    # end def __init__

    def relative_import_full(self, base_path: Union[str, 'Import']):
        if isinstance(base_path, Import):
            base_path = base_path.path
        # end if
        base_path: str

        return relimport(self.full, base_path)
    # end def

    def relative_import(self, base_path: Union[str, 'Import']):
        from code_generator_template import split_path
        import_path, import_name = split_path(self.relative_import_full(base_path=base_path))
        return Import(import_path, import_name)
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
        from code_generator_template import path_to_import_text
        return path_to_import_text(path)
    # end def

    def calculate_filepath(self, folder: str) -> str:
        from code_generator_online import calc_path_and_create_folders
        full_path = ''
        if self.path:
            full_path += self.path
        # end if
        if self.is_init:
            full_path += '.__init__'
        # end if
        if self.name:
            full_path += '.' + self.name
        # end if
        full_path = full_path.strip('.')

        return calc_path_and_create_folders(folder, full_path)
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
                "path={s.path!r}, name={s.name!r}, is_init={s.is_init!r}"
            ")"
        ).format(s=self)
    # end def __repr__
# end class Import


class CustomClazz(Clazz):
    def __init__(
        self,
        clazz: Union[None, str] = None,
        import_path: Union[None, 'Import'] = None,
        imports: Union[None, List['Import']] = None,
        parent_clazz: Union[None, 'Type'] = None,
        link: Union[None, str] = None,
        description: Union[None, str] = None,
        parameters: Union[None, List['Variable']] = None,
        keywords: Union[None, List['Variable']] = None,
        body: Union[None, 'ReplacementBody'] = None,
    ):
        """
        Like a class, but contains text.
        :param text: str[]
        :param imports: str[]
        """
        super().__init__(clazz, import_path, imports, parent_clazz, link, description, parameters, keywords)
        assert_type_or_raise(body, ReplacementBody, None, parameter_name='body')
        self.body = body if body else ReplacementBody()
    # end def
# end class


class ReplacementBody(object):
    # noinspection PyShadowingBuiltins
    def __init__(
        self,
        before: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        init: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        to_array: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        validate_array: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        from_array: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        str: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        repr: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        contains: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
        after: Union[None, List[str]] = None,  # None: keep, empty list: remove, filled list: print every line
    ):
        self.before = before
        self.init = init
        self.to_array = to_array
        self.validate_array = validate_array
        self.from_array = from_array
        self.str = str
        self.repr = repr
        self.contains = contains
        self.after = after
    # end def
# end class
