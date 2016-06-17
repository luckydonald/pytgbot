# -*- coding: utf-8 -*-
from jinja2 import Template
from jinja2.exceptions import TemplateSyntaxError
from luckydonaldUtils.logger import logging

from code_generator import safe_var_translations, get_type_path, convert_to_underscore
from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

def get_template(file_name):
    class_template = Template("# TEMPLATE COULD NOT BE LOADED #")
    with open(file_name) as file:
        try:
            class_template = Template(file.read())
        except TemplateSyntaxError as e:
            logger.warn("{file}:{line}: {msg}".format(msg=e.message, file=e.filename, line=e.lineno))
            raise e
    # end with
    return class_template
# end def get_template


def clazz(clazz, parent_clazz, description, link, params_string, init_super_args=None):
    """
    Live template for pycharm:

    y = clazz(clazz="$clazz$", parent_clazz="%parent$", description="$description$", link="$lnk$", params_string="$first_param$")
    """
    class_template = get_template("class.template")

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

    result = class_template.render(imports=imports,
        clazz=clazz, parent_clazz=parent_clazz, link=link, description=description,
        variables=variables_needed + variables_optional,
        parameters=variables_needed, keywords=variables_optional,
    )
    result = result.replace("\t", "    ")
    return result
# end def clazz


def func(command, description, link, params_string, returns="On success, the sent Message is returned.", return_type="Message"):
    """
    Live template for pycharm:

    y = func(command="$cmd$", description="$desc$", link="$lnk$", params_string="$first_param$", returns="$returns$", return_type="$returntype$")
    """
    func_template = get_template("func.template")

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

    return_type = as_types(return_type, variable_name="return type")
    result = func_template.render(
        imports=imports, func=command, link=link, description=description, returns=returns, return_type=return_type,
        variables=variables_needed + variables_optional,
        parameters=variables_needed, keywords=variables_optional,
    )
    result = result.replace("\t", "    ")
    return result
# end def


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
            if type.import_path:
                imports.add(Import(type.import_path, type.string))
            # end if
        # end for
        return imports
    # end def all_imports
# end class Variable


class Type(dict):
    def __init__(self, string=None, is_builtin=None, always_is_value=None, is_list=False, import_path=None, description=None):
        self.string = string  # the type (e.g. "bool")
        self.is_builtin = is_builtin  # bool.  If it is a build in type (float, int, ...) or not (classes like "Message", "Peer"...)
        self.always_is_value = always_is_value  # None or the only possible value (e.g. a bool, always True) default: None.
        self.is_list = is_list  # if it is an list of that type. (e.g. list of bool would be [True, False] )
        self.import_path = import_path  # from <import_path> import <string>
        self.description = description  # if there are additional comments needed.
    # end def __init__

    @property
    def as_import(self):
        return Import(self.import_path, self.string)
    # end def as_import
# end class Type


class Import(dict):
    """ from <path> import <name> """
    def __init__(self, path=None, name=None):
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

    def __hash__(self):
        return hash(self.path + self.name)
    # end def __hash__

    """
    If it is bigger (+1), equal (0) or less (-1)
    :return: +1, 0 or -1
    :rtype: int
    """
    def compare(self, other):
        if self.path < other.path:
            return -1
        elif self.path > other.path:
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

    param_types = table[1].strip().join([" ", " "])
    # ## " String or Boolean "
    variable.types = as_types(param_types, variable.api_name)
    return variable
# end def


def as_types(types_string, variable_name):
    # ## types_string = " String or Boolean "
    types_string = types_string.replace(" Float number ", " float ")
    types_string = types_string.replace(" Float ", " float ")
    types_string = types_string.replace(" Array ", " list ")
    types_string = types_string.replace(" String ", " str ")
    types_string = types_string.replace(" Integer ", " int ")
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

def to_type(type_string, variable_name):
    """
    Returns a :class:`Type` object of a given type name. Lookup is done via :var:`code_generator_settings.CLASS_TYPE_PATHS`

    :param type_string: The type as string. E.g "bool".
    :param variable_name: Only for logging, if an unrecognized type is found.
    :return: a :class:`Type` instance
    :rtype: Type
    """
    var_type = Type(type_string.strip())
    # remove "list of " and set .is_list accordingly.
    var_type.is_list, var_type.string = can_strip_prefix(var_type.string, "list of ")
    if var_type.string == "True":
        var_type.string = "bool"
        var_type.always_is_value = "True"
    elif var_type.string == "str":
        var_type.string = "unicode_type"
        var_type.import_path = "luckydonaldUtils.encoding"
        var_type.description = "py2: unicode, py3: str"
    # end if
    if var_type.string in ["int", "bool", "float", "unicode_type"]:  # str is replaced by unicode_type
        var_type.is_builtin = True
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
    if text.startswith(prefix):
        return True, text[len(prefix):]
    return False, text