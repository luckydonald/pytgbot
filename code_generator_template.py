# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from code_generator import get_type_path, safe_var_translations

from jinja2 import Template
from jinja2.exceptions import TemplateSyntaxError

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

    imports = [[], []]

    variables_needed = []
    variables_optional = []
    for param in params_string.split("\n"):
        variable = parse_param_types(param)
        # any variable.types has always_is_value => lenght must be 1.
        assert(not any([type_.always_is_value is not None for type_ in variable.types]) or len(variable.types) == 1)
        if variable.optional:
            variables_optional.append(variable)
        else:
            variables_needed.append(variable)
        # end if
    # end for

    result = class_template.render(imports=[Import("..somewhere", "File")],
        clazz=clazz, parent_clazz=parent_clazz, link=link, description=description,
        variables=variables_needed + variables_optional,
        parameters=variables_needed, keywords=variables_optional,
    )
    result = result.replace("\t", "    ")
    return result
# end def clazz


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

    """Note: if self.types is empty, the result of this function is undefined."""
    @property
    def all_builtin(self):
        builtin = True
        for type in self.types:
            builtin = builtin and type.is_builtin  # keeps being True until False is found.
        # end for
        return builtin
    # end def is_builtin
# end class Variable


class Type(dict):
    def __init__(self, string=None, is_builtin=None, always_is_value=None, is_list=False):
        self.string = string  # the type (e.g. "bool")
        self.is_builtin = is_builtin  # bool.  If it is a build in type (float, int, ...) or not (classes like "Message", "Peer"...)
        self.always_is_value = always_is_value  # None or the only possible value (e.g. a bool, always True) default: None.
        self.is_list = is_list  # if it is an list of that type. (e.g. list of bool would be [True, False] )
# end class Type


class Import(dict):
    """ from <path> import <name> """
    def __init__(self, path=None, name=None):
        self.path = path
        self.name = name
    # end def __init__
# end class Import



def parse_param_types(param) -> Variable:
    # ## "message_id\tString or Boolean\tUnique message identifier"
    table = param.split("\t")
    variable = Variable()

    variable.api_name=table[0].strip()
    variable.description=variable.description=table[2]
    variable.optional = variable.description.startswith("Optional.")
    if not variable.optional and "optional" in variable.description.lower():
        logger.warn("Found \"optional\" in non-optional variable {variable_name}. Description:\n".format(variable_name=variable.api_name))

    if variable.api_name in safe_var_translations:
        variable.name = safe_var_translations[variable.api_name]
    else:
        variable.name = variable.api_name
    # end if

    param_types = table[1].strip().join([" ", " "])
    # ## " String or Boolean "
    param_types = param_types.replace(" Float number ", " float ")
    param_types = param_types.replace(" Float ",   " float ")
    param_types = param_types.replace(" Array ",   " list ")
    param_types = param_types.replace(" String ",  " str ")
    param_types = param_types.replace(" Integer ", " int ")
    param_types = param_types.replace(" Boolean ", " bool ")
    param_types = param_types.replace(" Nothing ", " None ")
    param_types = param_types.replace(" Null ",    " None ")
    param_types = param_types.replace(" true ",    " True ")

    param_types = param_types.replace(" or ", " | ")
    param_types = param_types.strip()
    # ## "str | bool"

    the_types = param_types.split("|")
    variable.types = []
    for t in the_types:
        var_type = Type(t.strip())
        # remove "list of ", set .is_list accordingly.
        var_type.is_list, var_type.string = can_strip_prefix(var_type.string, "list of ")
        if var_type.string in ["int", "bool", "float", "str"]:
            var_type.is_builtin = True
        elif var_type.string == "True":
            var_type.string = "bool"
            var_type.always_is_value="True"
        else:
            logger.warn("Added unrecognized type in param {var}: {type}".format(var=variable.api_name, type=var_type.string))
        # end if
        variable.types.append(var_type)
    # end for
    return variable
# end def

"""
for asses in variable.types:  # short for asserts
    asses = asses.strip()  # always good!!
    asses = asses.strip("()")
    if asses in ["int", "bool", "float"]:
        assert_commands.append("isinstance({var}, {type})".format(var=param_name, type=asses))
    elif asses == "True":
        assert_commands.append("{var} == True".format(var=param_name, type=asses))
    elif asses == "str":
        assert_commands.append("isinstance({var}, unicode_type)".format(var=param_name, type=asses))
        assert_comments.append("unicode on python 2, str on python 3")
    elif asses.startswith("Array") or asses.startswith("list"):
        assert_commands.append("isinstance({var}, (list, tuple))".format(var=param_name))
        assert_comments.append(asses.replace("\n", " "))
    elif " or " in asses or " | " in asses:
        asses2 = asses.replace(" or ", ", ").replace(" | ", ", ")
        assert_commands.append("isinstance({var}, ({type}))".format(var=param_name, type=asses2))
    else:
        assert_commands.append("isinstance({var}, {type})".format(var=param_name, type=asses))
        non_buildin_type = asses
        logger.warn("Added unrecognized type in param {var}: {type}".format(var=param_name, type=asses))
# end for

to_array = ["array = super({clazz}, self).to_array()".format(clazz=clazz)]
    to_array.extend(to_array1)
    to_array.extend(to_array2)
    from_array = ["data = super({clazz}).from_array(array)".format(clazz=clazz)]
    from_array.extend(from_array1)
    from_array.extend(from_array2)
    from_array.append("return {clazz}(**data)".format(clazz=clazz))
"""


def can_strip_prefix(text:str, prefix:str) -> (bool, str):
    if text.startswith(prefix):
        return True, text[len(prefix):]
    return False, text
"""
if asses in ["int", "bool", "float"]:
    assert_commands.append("isinstance({var}, {type})".format(var=param_name, type=asses))
elif asses == "True":
    assert_commands.append("{var} == True".format(var=param_name, type=asses))
elif asses == "str":
    assert_commands.append("isinstance({var}, unicode_type)".format(var=param_name, type=asses))
    assert_comments.append("unicode on python 2, str on python 3")
elif asses.startswith("Array") or asses.startswith("list"):
    assert_commands.append("isinstance({var}, (list, tuple))".format(var=param_name))
    assert_comments.append(asses.replace("\n", " "))
elif " or " in asses or " | " in asses:
    asses2 = asses.replace(" or ", ", ").replace(" | ", ", ")
    assert_commands.append("isinstance({var}, ({type}))".format(var=param_name, type=asses2))
else:
    assert_commands.append("isinstance({var}, {type})".format(var=param_name, type=asses))
    """""""""