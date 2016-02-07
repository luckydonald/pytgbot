# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

import re
_first_cap_re = re.compile(r'(.)([A-Z][a-z]+)')
_all_cap_re = re.compile(r'([a-z0-9])([A-Z])')


def convert_to_underscore(name):
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
        table = param.split("\t")
        param_name = table[0].strip()
        param_type = table[1].strip().join([" "," "])
        # " String or Boolean "
        param_type = param_type.replace(" String ",  " str ")
        param_type = param_type.replace(" Integer ", " int ")
        param_type = param_type.replace(" Boolean ", " bool ")
        param_type = param_type.replace(" Nothing ", " None ")
        assert_types = param_type
        param_type = param_type.replace(" or ", " | ")
        assert_commands = []
        assert_comments = []
        for asses in assert_types.split("|"):  # short for asserts
            asses = asses.strip()  # always good!!
            asses = asses.strip("()")
            if asses in ["int", "bool", "str"]:
                assert_commands.append("isinstance({var}, {type})".format(var=param_name, type=asses))
            elif asses.startswith("Array"):
                assert_commands.append("isinstance({var}, (list, tuple))".format(var=param_name))
                assert_comments.append(asses.replace("\n"," "))
            else:
                logger.warn("unrecognized type in param {var}: {type}".format(var=param_name, type=asses))
        # end for
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
    print (result)
    return result


# func(command="", description="", link="", param_string="", returns="", return_type="")




class Param(object):
    def __init__(self, name, type, needed, desc):
        super(Param, self).__init__()
        self.name = name
        self.type = type
        self.needed = needed
        self.desc = desc

func("answerInlineQuery", """Use this method to send answers to an inline query. On success, True is returned.
No more than 50 results per query are allowed.""", "https://core.telegram.org/bots/api#answerinlinequery", "inline_query_id	String	Yes	Unique identifier for the answered query\nresults	Array of InlineQueryResult	Yes	A JSON-serialized array of results for the inline query\ncache_time	Integer	Optional	The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.\nis_personal	Boolean	Optional	Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query\nnext_offset	String	Optional	Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don‘t support pagination. Offset length can’t exceed 64 bytes.", "", "None")

print ("")
"""

regex for def -> class def

"def ([a-z_]+)\((?!\))" -> "def $1(self, "

"""