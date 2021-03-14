# -*- coding: utf-8 -*-
import os
import re

from typing import List, Set

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateSyntaxError

from luckydonaldUtils.logger import logging

from code_generator import safe_var_translations
from code_generator_classes import Clazz, Function, Variable, Type
from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT
from code_generator_settings import TYPE_STRING_OVERRIDES

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
    if params_string is not None:  # is None for WHITELISTED_CLASSES
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
    # end if
    imports: List[Variable] = list(imports)
    imports.sort()
    if isinstance(parent_clazz, str):
        parent_clazz = to_type(parent_clazz, "parent class")
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
    returns = Variable(types=as_types(return_type, variable_name="return type"), description=returns)
    func_object = Function(
        imports=imports, api_name=command, link=link, description=description, returns=returns,
        parameters=variables_needed, keywords=variables_optional
    )
    return func_object
# end def


def parse_param_types(param) -> Variable:
    # ## "message_id\tString or Boolean\tUnique message identifier"
    table = param.split("\t")
    variable = Variable()
    is_clazz = len(table) == 3

    variable.api_name = table[0].strip()
    if is_clazz:  # class
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

    variable.types = as_types(param_types, variable.api_name)
    if is_clazz:
        # check for "must be photo" kinda stuff.
        m = re.search(r'[Mm]ust be ([a-z0-9_]+)([\.\,\!\?]|$)', variable.description)
        if m:
            for t in variable.types:
                if not t.is_builtin:
                    continue
                # end if
                value = m.group(1)
                if t.string == 'bool':
                    t.always_is_value = {'True': True, 'False': False, 'None': None}[value]
                elif t.string == 'str':
                    t.always_is_value = value
                # end if
            # end if
        # end if
    # end if
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
        types_string = types_string.replace(" Messages ", " Message ")

        types_string = types_string.replace(" or ", " | ")
        types_string = types_string.replace(" and ", " | ")
    # end if
    types_string = types_string.strip()
    # ## "str | bool"

    the_types = types_string.split("|")
    types = []
    for t in the_types:
        var_type = to_type(t.strip(), variable_name=variable_name)
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
        logger.warning(f"Added unrecognized type in param <{variable_name}>: {var_type.string!r}")
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
