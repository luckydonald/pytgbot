# -*- coding: utf-8 -*-
from jinja2 import Template, Environment, FileSystemLoader
from jinja2.exceptions import TemplateSyntaxError
from luckydonaldUtils.logger import logging
from collections import Mapping
import os


from code_generator import safe_var_translations, get_type_path, convert_to_underscore
from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

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
    imports = set()
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
    imports = list(imports)
    imports.sort()
    if isinstance(parent_clazz, str):
        parent_clazz = to_type(parent_clazz, "parent class")
    assert isinstance(parent_clazz, Type)

    clazz_object = Clazz(imports=imports,
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
    imports = list(imports)
    imports.sort()
    returns = Variable(types=as_types(return_type, variable_name="return type"), description=returns)
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
# end class KwargableObject


class ClassOrFunction(KwargableObject):
    def __init__(self, filepath=None):
        """
        :param filepath: where this function or class should be stored.
        """
        self.filepath = filepath
# end class ClassOrFunction


class Clazz(ClassOrFunction):
    def __init__(self, clazz=None, imports=None, parent_clazz=None, link=None, description=None, parameters=None, keywords=None):
        super(Clazz, self).__init__()
        self.clazz = clazz
        self.imports = imports if imports else []  # Imports needed by parameters and keywords.
        self.parent_clazz = parent_clazz if parent_clazz is not None else Type("object", is_builtin=True)
        assert(isinstance(parent_clazz, Type))
        self.link = link
        self.description = description
        self.parameters = parameters if parameters else []
        self.keywords = keywords if keywords else []
    # end def __init__

    @property
    def variables(self):
        return self.parameters + self.keywords
    # end def variables
# end class Clazz


class Function(ClassOrFunction):
    def __init__(self, api_name=None, imports=None, link=None, description=None, returns=None, parameters=None, keywords=None):
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
    def name(self):
        return convert_to_underscore(self.api_name)
    # end def name
# end class Function


class Variable(dict):
    def __init__(self, api_name=None, name=None, types=None, optional=None, description=None):
        """

        :param api_name:
        :param name:
        :param types: `list` of :class:`Type`.  [Type(int), Type(bool)]  or  [Type(Message)]  etc.
        :param optional: If it is not needed. `True` will be a normal parameter, `False` means a kwarg.
        :param description:
        """
        self.api_name = api_name                    # parse_param_types(param)
        self.name = name if name else api_name      # parse_param_types(param)
        self.types = types if types else []         # parse_param_types(param)
        self.optional = optional  # bool            # parse_param_types(param)
        self.description = description  # some text about it.     # parse_param_types(param)
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
            if type.is_list:
                imports.add(Import(CLASS_TYPE_PATHS["as_array"][CLASS_TYPE_PATHS__IMPORT].rstrip("."), "as_array"))
            if type.import_path:
                imports.add(Import(type.import_path, type.string))
            # end if
        # end for
        return imports
    # end def all_imports
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

    def __str__(self):
        return "{list}<{name}>".format(list="list of " * self.is_list, name=self.string)
# end class Type


class Import(dict):
    """ from <path> import <name> """
    def __init__(self, path=None, name=None):
        super(Import, self).__init__()
        self.path = path
        self.name = name
    # end def __init__

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

    def __str__(self):
        return self.full
    # end def

    def __hash__(self):
        return hash(self.path + self.name)
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
# end class Import


def parse_param_types(param) -> Variable:
    # ## "message_id\tString or Boolean\tUnique message identifier"
    table = param.split("\t")
    variable = Variable()

    variable.api_name=table[0].strip()
    if len(table) == 3: # class
        variable.description = variable.description = table[2]
        variable.optional = variable.description.startswith("Optional.")
    else:
        variable.description = table[3]
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
    variable.types = as_types(param_types, variable.api_name)
    return variable
# end def


def as_types(types_string, variable_name):
    # ## types_string = "String or Boolean"  or  [Type(str), Type(bool)]

    if isinstance(types_string, list):
        for typ in types_string:
            assert isinstance(typ, Type)
            # [Type(), Type(), ...]
        return types_string
    # end if

    # ## types_string = "String or Boolean"
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
    types_string = types_string.strip()
    # ## "str | bool"

    the_types = types_string.split("|")
    types = []
    for t in the_types:
        var_type = to_type(t, variable_name=variable_name)
        types.append(var_type)
    # end for
    return types
# end def


def to_type(type_string, variable_name) -> Type:
    """
    Returns a :class:`Type` object of a given type name. Lookup is done via :var:`code_generator_settings.CLASS_TYPE_PATHS`

    :param type_string: The type as string. E.g "bool". Need to be valid python.
    :param variable_name: Only for logging, if an unrecognized type is found.
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
    if var_type.string in ["int", "bool", "float", "object", "None", "str"]:
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
            "Added unrecognized type in param <{var}>: {type}".format(var=variable_name, type=var_type.string))
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