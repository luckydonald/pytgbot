# -*- coding: utf-8 -*-
from typing import Union


try:
    # from code_generator_template import Import
    from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT
except ImportError:
    # from .code_generator_template import Import
    from .code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__IMPORT
# end try


__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)


import re
_first_cap_re = re.compile(r'(.)([A-Z][a-z]+)')
_all_cap_re = re.compile(r'([a-z0-9])([A-Z])')


def convert_to_underscore(name):
    """ "someFunctionWhatever" -> "some_function_whatever" """
    s1 = _first_cap_re.sub(r'\1_\2', name)
    return _all_cap_re.sub(r'\1_\2', s1).lower()


def func(command, description, link, params_string, returns="On success, the sent Message is returned.", return_type="Message"):
    """
    Live template for pycharm:

    y = func(command="$cmd$", description="$desc$", link="$lnk$", params_string="$first_param$", returns="$returns$", return_type="$returntype$")
    """
    description_with_tabs = "\t\t" + description.strip().replace("\n", "\n\t\t")
    param_list_args = []
    param_list_kwargs = []
    args = []
    args2 = []
    kwargs = []
    kwargs2 = []
    asserts = []
    str_args = ""
    str_kwargs = ""
    param_strings = params_string.split("\n")
    for param in param_strings:
        assert_commands, assert_comments, param_name, param_type, table, non_buildin_type, param_name_input = parse_param_types(param)
        param_required = table[2].strip()
        param_needed = None
        if param_required == "Yes":
            param_needed = True
        elif param_required == "Optional":
            param_needed = False
        param_description = table[3].strip()
        if param_needed:
            param_list_args.append(Param(param_name, param_type,param_needed, param_description))
            args.append(param_name)
            args2.append("{param_name}={param_name}".format(param_name=param_name))
            str_args += '\t\t:param {key}: {descr}\n\t\t:type  {key}: {type}\n\n'.format(key=param_name, descr=param_description, type=param_type)
            if assert_commands:
                asserts.append("assert({var} is not None)".format(var=param_name))
                asserts.append("assert({ass})".format(ass=" or ".join(assert_commands)) + (("  # {comment}".format(comment=", ".join(assert_comments))) if assert_comments else ""))
        else:
            param_list_kwargs.append(Param(param_name, param_type,param_needed, param_description))
            kwargs.append("{param_name}=None".format(param_name=param_name))
            kwargs2.append("{param_name}={param_name}".format(param_name=param_name))
            str_kwargs += '\t\t:keyword {key}: {descr}\n\t\t:type    {key}: {type}\n\n'.format(key=param_name, descr=param_description, type=param_type)
            if assert_commands:
                asserts.append("assert({var} is None or {ass})".format(var=param_name, ass=" or ".join(assert_commands)) + (("  # {comment}".format(comment=", ".join(assert_comments))) if assert_comments else ""))
    args.extend(kwargs)
    args2.extend(kwargs2)
    asserts_string = "\n\t\t" + "\n\t\t".join(asserts)
    text = ""
    if len(str_args)>0:
        text += '\n\t\tParameters:\n\n'
        text += str_args
    if len(str_kwargs)>0:
        text += '\n\t\tOptional keyword parameters:\n\n'
        text += str_kwargs
    do_args = ['"%s"' % command]
    do_args.extend(args2)
    result = '\tdef {funcname}(self, {params}):\n\t\t"""\n{description_with_tabs}\n\n\t\t{link}\n\n' \
           '{paramshit}\n' \
           '\t\tReturns:\n\n\t\t:return: {returns}\n\t\t:rtype:  {return_type}\n\t\t"""{asserts_with_tabs}\n\t\treturn self.do({do_args})\n\t# end def {funcname}'.format(
        funcname=convert_to_underscore(command),
        params=", ".join(args), description_with_tabs=description_with_tabs, link=link,
        returns=returns, return_type=return_type, command=command, do_args=", ".join(do_args),
        asserts_with_tabs=asserts_string,
        paramshit = text
    )
    result = result.replace("\t", "    ")
    return result
# end def

safe_var_translations = {
    "from": "from_peer",
    "to": "to_peer"
}


def get_type_path(param_class, as_object=False) -> Union[str, 'Import']:
    if not as_object:
        return get_type_path(param_class=param_class, as_object=True).full
    # end if
    try:
        from code_generator_template import Import
    except ImportError:
        from .code_generator_template import Import
    # end try

    param_class = param_class.strip()
    if param_class in CLASS_TYPE_PATHS:
        return Import(path=CLASS_TYPE_PATHS[param_class][CLASS_TYPE_PATHS__IMPORT].rstrip('.'), name=param_class)
    else:
        return Import(name=param_class)
    # end if
# end def


def clazz(clazz, parent_clazz, description, link, params_string, init_super_args=None):
    """
    Live template for pycharm:

    y = clazz(clazz="$clazz$", parent_clazz="%parent$", description="$desc$", link="$lnk$", params_string="$first_param$")
    """
    init_description_w_tabs  = description.strip().replace("\n", "\n\t\t")
    clazz_description_w_tabs = description.strip().replace("\n", "\n\t")
    imports = [[], []]
    args = []
    args2 = []
    kwargs = []
    kwargs2 = []
    asserts = []
    str_args = ""
    str_kwargs = ""
    to_array1 = []
    to_array2 = []
    from_array1 = []
    from_array2 = []
    param_strings = params_string.split("\n")
    for param in param_strings:
        assert_commands, assert_comments, param_name, param_type, table, non_buildin_type, param_name_input = parse_param_types(param)
        param_description = table[2].strip()
        param_needed = not param_description.startswith("Optional.")
        asserts.append("")
        if param_needed:
            args.append(param_name)
            str_args += '\n\n\t\t:param {key}: {descr}\n\t\t:type  {key}: {type}'.format(key=param_name, descr=param_description, type=get_type_path(param_type))
            if assert_commands:
                asserts.append("assert({var} is not None)".format(var=param_name))
                asserts.append("assert({ass})".format(ass=" or ".join(assert_commands)) + (("  # {comment}".format(comment=", ".join(assert_comments))) if assert_comments else ""))
            if non_buildin_type:
                to_array1.append('array["{var}"] = self.{var}.to_array()'.format(var=param_name))
                from_array1.append("data['{var}'] = {type}.from_array(array.get('{array_key}'))".format(var=param_name, array_key=param_name_input, type=non_buildin_type))
            else:
                to_array1.append('array["{var}"] = self.{var}'.format(var=param_name))
                from_array2.append("data['{var}'] = array.get('{array_key}')  # type {type}".format(var=param_name, array_key=param_name_input, type=non_buildin_type))
            # end if non_buildin_type
        else:
            kwargs.append("{param_name}=None".format(param_name=param_name))
            str_kwargs += '\n\n\t\t:keyword {key}: {descr}\n\t\t:type    {key}: {type}'.format(key=param_name, descr=param_description, type=param_type)
            if assert_commands:
                asserts.append("assert({var} is None or {ass})".format(var=param_name, ass=" or ".join(assert_commands)) + (("  # {comment}".format(comment=", ".join(assert_comments))) if assert_comments else ""))
            to_array2.append('if self.{var} is not None:'.format(var=param_name))
            if non_buildin_type:
                to_array2.append('\tarray["{var}"] = self.{var}.to_array()'.format(var=param_name))
                from_array2.append("data['{var}'] = {type}.from_array(array.get('{array_key}'))".format(var=param_name, array_key=param_name_input, type=non_buildin_type))
            else:
                to_array2.append('\tarray["{var}"] = self.{var}'.format(var=param_name))
                from_array2.append("data['{var}'] = array.get('{array_key}')  # type {type}".format(var=param_name, array_key=param_name_input, type=non_buildin_type))
        # end if non_buildin_type
        asserts.append("self.{param_name} = {param_name}".format(param_name=param_name))
    param_description = ""
    if len(str_args)>0:
        param_description += '\n\t\tParameters:'
        param_description += str_args
    if len(str_kwargs)>0:
        param_description += '\n\n\n\t\tOptional keyword parameters:'
        param_description += str_kwargs
    args.extend(kwargs)
    to_array = ["array = super({clazz}, self).to_array()".format(clazz=clazz)]
    to_array.extend(to_array1)
    to_array.extend(to_array2)
    from_array = ["data = super({clazz}).from_array(array)".format(clazz=clazz)]
    from_array.extend(from_array1)
    from_array.extend(from_array2)
    from_array.append("return {clazz}(**data)".format(clazz=clazz))
    result = 'class {clazz}({parent_clazz}):\n' \
             '\t"""\n' \
             '\t{clazz_description_w_tabs}\n' \
             '\n' \
             '\t{link}\n' \
             '\t"""\n' \
             '\tdef __init__(self, {params}):\n' \
             '\t\t"""\n' \
             '\t\t{init_description_w_tabs}\n' \
             '\n' \
             '\t\t{link}\n' \
             '\n' \
             '{param_description}\n' \
             '\t\t"""\n' \
             '\t\tsuper({clazz}, self).__init__({init_super_args})\n' \
             '\t\t{asserts_with_tabs}\n' \
             '\t# end def __init__\n' \
             '\n' \
             '\tdef to_array(self):\n' \
             '\t\t{to_array_with_tabs}\n' \
             '\t\treturn array\n' \
             '\t# end def to_array\n' \
             '\n' \
             '\t@staticmethod\n' \
             '\tdef from_array(array):\n' \
             '\t\tif array is None:\n' \
             '\t\t\treturn None\n' \
             '\t\t# end if\n' \
             '\t\t{from_array_with_tabs}\n' \
             '\t# end def from_array\n' \
             '# end class {clazz}\n'.format(
        clazz=clazz, parent_clazz=parent_clazz, params=", ".join(args), param_description = param_description,
        clazz_description_w_tabs=clazz_description_w_tabs, init_description_w_tabs=init_description_w_tabs, link=link,
        asserts_with_tabs="\n\t\t".join(asserts), to_array_with_tabs="\n\t\t".join(to_array),
        from_array_with_tabs="\n\t\t".join(from_array),
        init_super_args=(", ".join(init_super_args) if init_super_args else "")
    )
    result = result.replace("\t", "    ")
    return result


# func(command="", description="", link="", param_string="", returns="", return_type="")

def parse_param_types(param):
    table = param.split("\t")
    param_name_input = table[0].strip()
    if param_name_input in safe_var_translations:
        param_name = safe_var_translations[param_name_input]
    else:
        param_name = param_name_input
    # end if
    param_type = table[1].strip().join([" ", " "])
    # " String or Boolean "
    param_type = param_type.replace(" Float number ", " float ")
    param_type = param_type.replace(" Float ", " float ")
    param_type = param_type.replace(" Array ", " list ")
    param_type = param_type.replace(" String ", " str ")
    param_type = param_type.replace(" Integer ", " int ")
    param_type = param_type.replace(" Boolean ", " bool ")
    param_type = param_type.replace(" Nothing ", " None ")
    assert_types = param_type
    param_type = param_type.replace(" or ", " | ")
    param_type = param_type.strip()
    assert_commands = []
    assert_comments = []
    non_buildin_type = None
    for asses in assert_types.split("|"):  # short for asserts
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
            logger.warn("parse_params: Added unrecognized type in param {var}: {type}".format(var=param_name, type=asses))
    # end for
    # non_buildin_type is None if is build in, else is ==
    return assert_commands, assert_comments, param_name, param_type, table, non_buildin_type, param_name_input
# end def


class Param(object):
    def __init__(self, name, type, needed, desc):
        super(Param, self).__init__()
        self.name = name
        self.type = type
        self.needed = needed
        self.desc = desc


def command_line_input():
    from luckydonaldUtils.interactions import confirm, answer
    do_func = confirm("Choose between generating function or class. Do you want a function?", True)
    if do_func:
        command       = answer("Command (the Title)")
        description   = answer("Description")
        link          = answer("The link on the api page")
        params_string = "---"
        params_strings = []
        while params_string != "":
            params_string = answer("Parameters (sepereated by tabs, and new lines)\nParameters	Type	Required	Description", "")
            if params_string and not params_string.strip() == "":
                params_strings.append(params_string)
            # end if
        # end while
        returns       = answer("Textual description what the function returns", "On success, the sent Message is returned.")
        return_type   = answer("Return type", "Message")
        print("\n")
        func(command, description, link, params_string, returns , return_type)
    else:
        clazze        = answer("Class name")
        parent_clazz  = answer("Parent class name", "object")
        description   = answer("Description")
        link          = answer("The link on the api page")
        params_string = "--"
        params_strings = []
        while params_string != "":
            params_string = answer("Parameters (separated by tabs, and new lines)\nParameters	Type	Description", "")
            if params_string and not params_string.strip() == "":
                params_strings.append(params_string)
            # end if
        # end while
        print("\n")
        clazz(clazze, parent_clazz, description, link, "\n".join(params_strings))
    # end if
# end if main

"""

regex for def -> class def

"def ([a-z_]+)\((?!\))" -> "def $1(self, "

"""

if __name__ == '__main__':
    command_line_input()
