# -*- coding: utf-8 -*-
from typing import Dict, List, Union

from code_generator import get_type_path
from code_generator_template import clazz, func, get_template, as_types
from code_generator_classes import Clazz, Function, Variable, Type, Import, CustomClazz
from luckydonaldUtils.files.basics import mkdir_p  # luckydonaldUtils v0.49+
from luckydonaldUtils.interactions import answer, confirm
from luckydonaldUtils.logger import logging

from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__PARENT, WHITELISTED_FUNCS, CUSTOM_CLASSES
from code_generator_template import path_to_import_text, split_path
from jinja2.exceptions import TemplateError, TemplateSyntaxError

import requests


import black  # code formatter
from yapf.yapflib.yapf_api import FormatFile  # code formatter

from bs4 import BeautifulSoup
from bs4.element import NavigableString
from os.path import abspath, dirname, join as path_join, sep as folder_seperator, isfile, exists, isdir
from luckydonaldUtils.interactions import safe_eval, NoBuiltins

__author__ = "luckydonald"
logger = logging.getLogger(__name__)


from logging import LogRecord


def log_filter(record: LogRecord):
    if f'{record.name}.{record.funcName}' == 'luckydonaldUtils.functions.wrapper':
        return False
    return True
# end def


root_logger = logging.add_colored_handler(level=logging.DEBUG, filter=log_filter)


FILE_HEADER = "# -*- coding: utf-8 -*-\n"
MAIN_FILE_CLASS_HEADER = "class Bot(object):\n    _base_url = \"https://api.telegram.org/bot{api_key}/{command}\"\n"

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


BASE_URL = "https://core.telegram.org/bots/api"
SAVE_VALUES = NoBuiltins([], {}, {"Function": Function, "Clazz": Clazz, "Import": Import, "Type": Type, "Variable": Variable})


def lol1(tag):
    return tag.has_attr("class") and "anchor" in tag["class"]


class_fields = [
    ["Field", "Type", "Description"],
    ["Parameters", "Type", "Description"],
]
func_fields = [
    ["Parameters", "Type", "Required", "Description"],
    ["Parameter", "Type", "Required", "Description"],
]


use_back = False
use_yapf = False

black_settings = dict(
    write_back=black.WriteBack.from_configuration(check=False, diff=False),
    report=black.Report(check=False, quiet=False, verbose=False),
    mode=black.FileMode(
        target_versions=set(),
        line_length=black.DEFAULT_LINE_LENGTH,
        is_pyi=False,
        string_normalization=True,
    ),
)
yapf_settings = dict(
    style={
        'ALIGN_CLOSING_BRACKET_WITH_VISUAL_INDENT': True,
        'ALLOW_MULTILINE_LAMBDAS': True,
        'ALLOW_MULTILINE_DICTIONARY_KEYS': False,
        'ALLOW_SPLIT_BEFORE_DEFAULT_OR_NAMED_ASSIGNS': True,
        'ALLOW_SPLIT_BEFORE_DICT_VALUE': False,
        'ARITHMETIC_PRECEDENCE_INDICATION': False,
        'BLANK_LINE_BEFORE_NESTED_CLASS_OR_DEF': False,
        'BLANK_LINE_BEFORE_MODULE_DOCSTRING': True,
        'BLANK_LINE_BEFORE_CLASS_DOCSTRING': False,
        'BLANK_LINES_AROUND_TOP_LEVEL_DEFINITION': 2,  # Sets the number of desired blank lines surrounding top-level function and class definitions.
        'COALESCE_BRACKETS': True,
        'COLUMN_LIMIT': black.DEFAULT_LINE_LENGTH,
        'CONTINUATION_ALIGN_STYLE': "space",
        'CONTINUATION_INDENT_WIDTH': 2,
        'DEDENT_CLOSING_BRACKETS': True,
        'DISABLE_ENDING_COMMA_HEURISTIC': True,
        'EACH_DICT_ENTRY_ON_SEPARATE_LINE': False,
        'INDENT_DICTIONARY_VALUE': False,  # Indent the dictionary value if it cannot fit on the same line as the dictionary key.
        'INDENT_WIDTH': 2,
        'INDENT_BLANK_LINES': False,  # Set to True to prefer indented blank lines rather than empty
        'JOIN_MULTIPLE_LINES': False,  # Join short lines into one line. E.g., single line if statements.
        'NO_SPACES_AROUND_SELECTED_BINARY_OPERATORS': False,  # Do not include spaces around selected binary operators. For example: 1 + 2*3 - 4/5
        'SPACES_AROUND_POWER_OPERATOR': True,  # Set to True to prefer using spaces around **.
        # 'SPACES_AROUND_DEFAULT_OR_NAMED_ASSIGN': False,  # Set to True to prefer spaces around the assignment operator for default or keyword arguments.
        'SPACES_BEFORE_COMMENT': 2,
        'SPACE_BETWEEN_ENDING_COMMA_AND_CLOSING_BRACKET': False,  # Insert a space between the ending comma and closing bracket of a list, etc.
        'SPLIT_ARGUMENTS_WHEN_COMMA_TERMINATED': True,  # Split before arguments if the argument list is terminated by a comma.
        'SPLIT_ALL_COMMA_SEPARATED_VALUES': True,  # If a comma separated list (dict, list, tuple, or function def) is on a line that is too long, split such that all elements are on a single line.
        'SPLIT_ALL_TOP_LEVEL_COMMA_SEPARATED_VALUES': True,  # Variation on SPLIT_ALL_COMMA_SEPARATED_VALUES in which, if a subexpression with a comma fits in its starting line, then the subexpression is not split. This avoids splits like the one for b in this code:
        'SPLIT_BEFORE_BITWISE_OPERATOR': False,  # Set to True to prefer splitting before &, | or ^ rather than after.
        'SPLIT_BEFORE_ARITHMETIC_OPERATOR': False,  # Set to True to prefer splitting before +, -, *, /, //, or @ rather than after.
        'SPLIT_BEFORE_CLOSING_BRACKET': True,  # Split before the closing bracket if a list or dict literal doesn't fit on a single line.
        'SPLIT_BEFORE_DICT_SET_GENERATOR': True,  # Split before a dictionary or set generator (comp_for). For example, note the split before the for:
        'SPLIT_BEFORE_DOT': False,  # Split before the . if we need to split a longer expression:
        # 'SPLIT_BEFORE_EXPRESSION_AFTER_OPENING_PAREN': False,  # Split after the opening paren which surrounds an expression if it doesn't fit on a single line.
        'SPLIT_BEFORE_FIRST_ARGUMENT': True,  # If an argument / parameter list is going to be split, then split before the first argument.
        'SPLIT_BEFORE_LOGICAL_OPERATOR': True,  # Set to True to prefer splitting before and or or rather than after.
        # 'SPLIT_BEFORE_NAMED_ASSIGNS': False,  # Split named assignments onto individual lines.
        'SPLIT_COMPLEX_COMPREHENSION': True,  # For list comprehensions and generator expressions with multiple clauses (e.g multiple for calls, if filter expressions) and which need to be reflowed, split each clause onto its own line.
        'USE_TABS': False,

        # 'SPLIT_PENALTY_AFTER_OPENING_BRACKET': 0
        # 'SPLIT_PENALTY_AFTER_UNARY_OPERATOR':
        # 'SPLIT_PENALTY_ARITHMETIC_OPERATOR':
        # 'SPLIT_PENALTY_BEFORE_IF_EXPR':
        # 'SPLIT_PENALTY_BEFORE_IF_EXPR': 30
        # 'SPLIT_PENALTY_FOR_ADDED_LINE_SPLIT': 30
    },
)


def parse_table(tag):
    """
    returns tuple of type ("class"/"func") and list of param strings.
    :param tag:
    :return:
    """
    first = True
    table_header = None
    table_type = 'unknown'
    param_strings = []

    thead = tag.find('thead', recursive=False)
    theads = None  # list (items in <tr> row) of <th>/<tr> elements.
    if thead:
        theads = thead.find_all(["th", "td"])
    # end if
    tbody = tag.find('tbody', recursive=False)
    if tbody:
        tbody_rows = tbody.find_all("tr")
    else:
        tbody_rows = tag.find_all("tr")
    # end if
    tbodys = [  # list (rows) of list (items in <tr> row) of <tr> elements.
        row.find_all(["td" ,"th"]) for row in tbody_rows
    ]
    if not thead:  # so first row = header
        theads = tbody_rows[0]
        tbodys = tbody_rows[1:]
    # end if

    # TABLE HEADER

    found_columns = []
    for column in theads:
        # Either (a) `<td><strong> ... </strong></td>`
        # or new (b) `<th> ... </th>`
        col = column.find("strong")
        if col:
            # (a) `<td><strong> ... </strong></td>`
            col_text = col.text
        else:
            # (b) `<th> ... </th>`
            col_text = column.text
        # end if
        found_columns.append(col_text)
    # end def

    # if TABLE is func
    for test_columns in func_fields:
        if found_columns == test_columns:
            table_header = test_columns
            table_type = 'func'
            break
        # end if
    # end for

    # if TABLE is class
    if not table_header:  # only check if we don't have a result yet
        # search class now
        for test_columns in class_fields:
            if found_columns == test_columns:
                if table_header is not None:
                    raise AssertionError("Table detected as func and class: {!r}".format(found_columns))
                table_header = test_columns
                table_type = 'class'
                break
            # end if
        # end for
    # end if

    # TABLE is none of the above
    if not table_header:  # we don't have a result yet
        raise AssertionError("Unknown table, {!r}".format(found_columns))
    # end if

    # TABLE BODY

    for tds in tbodys:
        string = "\t".join([col.text for col in tds])
        logger.debug("t: " + string)
        param_strings.append(string)
        pass
    # end for row
    return table_type, param_strings
# end def


def load_from_html(folder):
    filter = get_filter()
    document = requests.get(BASE_URL)
    bs = BeautifulSoup(document.content)
    results = []
    for h in bs.select("#dev_page_content > h4"):
        logger.info("------")
        anchor = h.find(lol1)
        if not anchor or not anchor.has_attr("name"):
            continue
        link = "{base_url}#{anchor}".format(base_url=BASE_URL, anchor=anchor["name"])
        title = h.text
        descr = []
        table_type, param_strings = None, None
        logger.info("title: " + title)
        logger.info("link: " + link)
        if filter and title not in filter:
            logger.info("Skipping {title}, filtered.".format(title=title))
            continue
        # logger.debug(h)
        type_strings = []
        default_returns = []
        for sibling in h.next_siblings:
            if sibling == "\n":
                continue
            if sibling.name in ["p", "blockquote"]:
                if "return" in sibling.text.lower():
                    parts_splitted = []
                    is_first_element = True  # truein string,
                    for x in sibling.children:
                        if isinstance(x, NavigableString):
                            if is_first_element:  # Start of a new sentence => new list
                                parts_splitted.extend([[foo.lstrip()] for foo in x.split(".")])
                                is_first_element = False
                            else:  # not = in the middle of a sentence => append
                                parts_splitted[len(parts_splitted)-1].append(x.split(".", maxsplit=1)[0])
                                parts_splitted.extend([[foo] for foo in x.split(".")[1:]])
                                is_first_element = False
                            is_first_element = x.strip().endswith(".")
                        else:
                            obj = None
                            if x.name in ["a", "em"]:
                                obj = x
                            else:
                                obj = x.text
                            # end if
                            if is_first_element:  # if it is at the beginning of the sentence.
                                parts_splitted.append([obj])
                                is_first_element = False
                            else:
                                parts_splitted[len(parts_splitted)-1].append(obj)
                            # end if
                        # end for
                    # end for
                    returns__ = []  # array of strings
                    return_text__ = []  # array if strings. one item = one sentence. Not ending with a dot.
                    is_array = False
                    for lol_part in parts_splitted:
                        has_return = False
                        returns_ = []
                        return_text_ = ""
                        for lol_part_part in lol_part:
                            if isinstance(lol_part_part, str):
                                return_text_ += lol_part_part
                                if lol_part_part.strip().lower().endswith("array of"):
                                    is_array = True
                                if "return" in lol_part_part.lower():
                                    has_return = True
                                # end if
                            else:  # not str
                                return_text_ += lol_part_part.text
                                if is_array:
                                    returns_.append("list of " + lol_part_part.text)
                                    is_array = False
                                else:
                                    returns_.append(lol_part_part.text)
                        # end for
                        if has_return:  # append, so we can have multible sentences.
                            return_text__.append(return_text_.strip())
                            returns__.extend(returns_)
                        # end if
                    # end for
                    if return_text__ or returns__:  # finally set it.
                        default_returns = [". ".join(return_text__).strip(), " or ".join(returns__).strip()]
                    # end if
                # end if
                descr.append(sibling.text.replace('“', '"').replace('”', '"'))
            elif sibling.name == "table":
                assert sibling.has_attr("class") and "table" in sibling["class"]
                table_type, param_strings = parse_table(sibling)
            elif sibling.name == "h4":
                break
            elif sibling.name == "h3":
                break
            elif sibling.name == "hr":  # end of page
                break
            else:
                logger.info("unknown: " + sibling.name)
                # end if
        # end for
        if not all([link, title, descr]):
            logger.warning("Skipped: Missing link, title or description")
            continue
        if not all([table_type, param_strings]):
            if title not in WHITELISTED_FUNCS:
                logger.warning(
                    "Skipped. Has no table with Parameters or Fields.\n"
                    "Also isn't a whitelisted function in `code_generator_settings.WHITELISTED_FUNCS`."
                )
                continue
            # -> else: is in WHITELISTED_FUNCS:
            table_type = "func"
        # end if
        descr = "\n".join(descr)
        logger.info("descr: " + repr(descr))
        params_string = "\n".join(param_strings) if param_strings else None  # WHITELISTED_FUNCS have no params
        if table_type == "func":
            seems_valid = False
            if len(default_returns) != 2:
                if "return" in descr.lower():
                    default_returns = ["", "Message"]
                    default_returns[0] = [x for x in descr.split(".") if "return" in x.lower()][0].strip()
                    seems_valid = len(default_returns[0].split(".")) == 1
                    default_returns[1] = " or ".join(type_strings) if type_strings else "Message"
                    default_returns[1] = as_types(default_returns[1], "returns")
                else:
                    default_returns = ["On success, True is returned", "True"]
                # end if "return" in description
            else:
                seems_valid = len(default_returns[0].split(".")) == 1
            # end if default set
            replaced_valid = None  # load replacements from WHITELISTED_FUNCS.
            if title in WHITELISTED_FUNCS:
                # "func": {'return': {'expected': '', 'replace': ''}, 'rtype': {'expected': '', 'replace': ''}},
                wlist_func = WHITELISTED_FUNCS[title]
                wlist_func_return = wlist_func['return'] if 'return' in wlist_func else None
                wlist_func_r_type = wlist_func['r_type'] if 'r_type' in wlist_func else None
                if wlist_func_return and default_returns[0] != wlist_func_return['expected']:
                    logger.warning(f"whitelist: Mismatch in return. Expected {wlist_func_return['expected']!r}, got {default_returns[0]!r}.")
                    replaced_valid = False
                if wlist_func_r_type and default_returns[1] != wlist_func_r_type['expected']:
                    logger.warning(f"whitelist: Mismatch in r_type. Expected {wlist_func_r_type['expected']!r}, got {default_returns[1]!r}")
                    replaced_valid = False
                if replaced_valid is None:  # whitelist didn't fail
                    replaced_valid = True
                    logger.info("the found return: " + repr(default_returns[0]) + '.')
                    logger.info("the found r_type: " + repr(default_returns[1]) + '.')
                    logger.info("whitelist return: " + repr(wlist_func_return['replace']) + '.')
                    logger.info("whitelist r_type: " + repr(wlist_func_r_type['replace']) + '.')
                    default_returns[0] = wlist_func_return['replace']
                    default_returns[1] = wlist_func_r_type['replace']
            if not seems_valid and not replaced_valid:
                returns     = answer("Textual description what the function returns", default_returns[0])
                return_type = answer("Return type", default_returns[1])
                if isinstance(return_type, str):
                    return_type = as_types(return_type, "return type")
                # end if
            else:
                returns = default_returns[0]
                return_type = default_returns[1]
            # end if
            logger.debug("\n")
            result = func(title, descr, link, params_string, returns=returns, return_type=return_type)
            results.append(result)
        elif table_type == "class":
            if title in CLASS_TYPE_PATHS:
                parent_clazz = CLASS_TYPE_PATHS[title][CLASS_TYPE_PATHS__PARENT]
                logger.info("superclass: " + parent_clazz)
            else:
                parent_clazz = answer("Parent class name", "TgBotApiObject")
            # end if
            result = clazz(
                clazz=title, parent_clazz=parent_clazz, description=descr, link=link, params_string=params_string
            )
            results.append(result)
        # end if
    # end for

    return results, document.content
# end def main


def main():
    folder, html_document, results = load_api_definitions()
    output(folder, results, html_content=html_document)


def load_api_definitions():
    folder = get_folder_path()
    mode = confirm("Offline Mode: Load from a dump instead of the API Docs?")
    if not mode:  # API
        results, html_document = load_from_html(folder)
    else:  # Dump
        results, html_document = load_from_dump(folder)
    # end def
    results = preprocess_results(results, additional_items=list(CUSTOM_CLASSES.values()))
    return folder, html_document, results
# end def


def load_from_dump(folder):
    # read dump
    dump = ""
    with open(path_join(folder, "api.py"), "r") as f:
        dump = "".join(f.readlines())
    # end with

    # existing old api.html
    html_document = None
    if exists(path_join(folder, "api.html")):
        with open(path_join(folder, "api.html"), "rb") as f:
            html_document = f.read()
        # end with
    # end if
    results = safe_eval(dump, SAVE_VALUES)
    return results, html_document
# end def


# noinspection PyCompatibility
def preprocess_results(results: List[Union[Clazz, Function]], additional_items: Union[None, List[Clazz]] = None):
    """
    Sets `variable.duplicate_of_parent` appropriately for all variables of all classes in the results list.
    :param results:
    :param additional_items: e.g. CUSTOM_CLASSES.values()
    :return:
    """
    if additional_items is None:
        additional_items = []
    # end if

    logger.info('Calculating duplicate_of_parent.')
    clazzes_by_name: Dict[str, Clazz] = {}  # "Class": Class

    for other in additional_items:
        clazzes_by_name[other.clazz] = other
    # end for
    for result in results:
        if isinstance(result, Clazz):
            clazzes_by_name[result.clazz] = result
        # end if
    # end for
    for result in results:
        if not isinstance(result, Clazz):
            continue
        # end if

        # fill in clazz._parent_clazz_clazz, so we can check our parents
        if result.parent_clazz is None or result.parent_clazz.string == 'object':
            continue
        # end if
        if result.parent_clazz.string in clazzes_by_name:
            parent_clazz: Clazz = clazzes_by_name[result.parent_clazz.string]
            for variable in result.variables:
                variable: Variable
                variable.duplicate_of_parent = parent_clazz.has_same_variable(variable, ignore_pytg_name=True, ignore_description=True)
            # end for
        else:
            logger.warning(f'Could not resolve parent class: {result.parent_clazz}')
        # end if
    # end for
    return results
# end def


def output(folder, results, html_content=None):
    can_quit = False
    do_overwrite = confirm("Can the folder {path} be overwritten?".format(path=folder))
    logger.info("vvvvvvvvv")
    while not can_quit:
        if do_overwrite:
            try:
                import Send2Trash
                Send2Trash.send2trash(folder)
            except ImportError:
                import shutil
                shutil.rmtree(folder)
            # end try
        # end if

        # write crawled data
        mkdir_p(folder)
        with open(path_join(folder, "api.py"), "w") as f:
            f.write("[\n    ")
            f.write(",\n    ".join([repr(result) for result in results]))
            f.write("\n]")
            # end for
        # end with
        if html_content:
            with open(path_join(folder, "api.html"), "wb") as f:
                f.write(html_content)
            # end with
        # end if

        # write templates
        try:
            safe_to_file(folder, results)
        except TemplateError as e:
            if isinstance(e, TemplateSyntaxError):
                logger.exception("Template error at {file}:{line}".format(file=e.filename, line=e.lineno))
            else:
                logger.exception("Template error.")
                # end if
        # end try
        logger.info("Writen to file.")
        can_quit = not confirm("Write again after reloading templates?", default=True)
    logger.info("#########")
    logger.info("Exit.")
# end def


def get_filter():
    filter = answer(
        "Only generate the doc for specific functions/classes. Comma seperated list. Leave empty to generate all.",
        default=""
        # getChat, leaveChat, getChatAdministrators, getChatMember, getChatMembersCount, Message, MessageEntity"
    )
    if filter.strip():
        filter = [x.strip() for x in filter.split(",")]
    else:
        filter = None
    # end if
    return filter
# end def


def get_folder_path():
    default = "/tmp/pytgbotapi/"
    candidate = abspath(path_join(dirname(abspath(__file__)),  'output'))
    logger.info(f'canidate: {candidate}')
    if exists(candidate) and isdir(candidate):
        default = candidate
    # end if
    file = answer("Folder path to store the results.", default=default)
    if file:
        try:
            file = abspath(file)
            mkdir_p(file)
            with open(path_join(file, "__init__.py"), "w") as f:
                f.write(FILE_HEADER)
                # end with
        except IOError:
            pass
            # end try
    # end if file
    return file
# end def


# noinspection PyCompatibility
def safe_to_file(folder, results):
    """
    Receives a list of results (type :class:`Clazz` or :class:`Function`), and put them into the right files in :var:`folder`

    :param folder: Where the files should be in.
    :type  folder: str

    :param results: A list of :class:`Clazz` or :class:`Function` objects, which will be used to calculate the source code.
    :type  results: Union(Clazz, Function)

    """
    functions = []
    message_send_functions = []
    clazzes: Dict[str, List[Clazz]] = {}  # "filepath": [Class, Class, ...]
    all_the_clazzes = []
    custom_classes = {}  # "filepath": [Class, Class, ...]
    for import_path, result in CUSTOM_CLASSES.items():
        # result.import_path = result.calculate_import_path()
        result.filepath = result.calculate_filepath(folder)
        file_path = result.filepath
        if file_path not in custom_classes:
            custom_classes[file_path] = []
        # end if
        custom_classes[file_path].append(result)
        if file_path not in clazzes:
            clazzes[file_path] = []
        # end if
        clazzes[file_path].append(result)
        all_the_clazzes.append(result)
    # end def

    # split results into functions and classes
    for result in results:
        assert isinstance(result, (Clazz, Function))
        if isinstance(result, Clazz):
            result.import_path = result.calculate_import_path()
            result.filepath = result.calculate_filepath(folder)
            file_path = result.filepath
            if file_path not in clazzes:
                clazzes[file_path] = []
            clazzes[file_path].append(result)
            all_the_clazzes.append(result)
        else:
            assert isinstance(result, Function)
            import_path = "pytgbot.bot.async."
            file_path = calc_path_and_create_folders(folder, import_path)
            result.filepath = file_path
            functions.append(result)

            if result.name.startswith('send_'):
                import_path = "teleflask_messages."
                file_path = calc_path_and_create_folders(folder, import_path)
                result2 = safe_eval(repr(result), SAVE_VALUES)  # serialize + unserialize = deepcopy
                result2.filepath = file_path
                message_send_functions.append(result2)
            # end if
        # end if
    # end for

    bot_template = get_template("bot.template")
    clazzfile_template = get_template("classfile.template")
    teleflask_messages_template = get_template("teleflask_messages_file.template")
    typehints_template = get_template("typehintsfile.template")
    telegram_bot_api_server_funcs_template = get_template("telegram_bot_api_server/funcs.template")
    telegram_bot_api_server_class_template = get_template("telegram_bot_api_server/classes.template")

    mkdir_p(path_join(folder, 'telegram_bot_api_server', 'generated'))

    if all_the_clazzes:
        txt = telegram_bot_api_server_class_template.render(clazzes=all_the_clazzes)
        render_file_to_disk(path_join(folder, 'telegram_bot_api_server', 'generated', 'models.py'), txt)
    # end if
    for path, clazz_list in clazzes.items():
        clazz_imports = set()
        for clazz_ in clazz_list:
            assert isinstance(clazz_, Clazz)
            assert isinstance(clazz_.parent_clazz, Type)
            if not clazz_.parent_clazz.is_builtin:
                clazz_imports.add(clazz_.parent_clazz.as_import)
            # end if
        # end for
        clazz_imports = list(clazz_imports)
        clazz_imports.sort()
        is_sendable = ("sendable" in path)
        try:
            txt = clazzfile_template.render(clazzes=clazz_list, manual_clazzes=[], imports=clazz_imports, is_sendable=is_sendable)
            txt = txt.replace("\t", "    ")
            render_file_to_disk(path, txt)
        except IOError:
            raise  # lol
        # end try
        try:
            txt = typehints_template.render(clazzes=clazz_list, imports=clazz_imports, is_sendable=is_sendable)
            txt = txt.replace("\t", "    ")
            render_file_to_disk(path + "i", txt)  # "ponies.py" + "i" => "ponies.pyi"
        except IOError:
            raise  # lol
        # end try
        try:
            txt = typehints_template.render(clazzes=clazz_list, imports=clazz_imports, is_sendable=is_sendable)
            txt = txt.replace("\t", "    ")
            render_file_to_disk(path + "i", txt)  # "ponies.py" + "i" => "ponies.pyi"
        except IOError:
            raise  # lol
        # end try
    # end for classes
    if functions:
        txt_sync = bot_template.render(functions=functions, is_asyncio=False)
        render_file_to_disk(functions[0].filepath.replace('async', 'sync'), txt_sync)
        txt_async = bot_template.render(functions=functions, is_asyncio=True)
        render_file_to_disk(functions[0].filepath, txt_async)

        imports = set()
        imports.add(('enum', 'Enum'))
        imports.add(('typing', 'Union, List, Optional'))
        imports.add(('fastapi', 'APIRouter, HTTPException'))
        imports.add(('telethon', 'TelegramClient'))
        imports.add(('serializer', 'to_web_api, get_entity'))
        imports.add(('fastapi.params', 'Query'))
        imports.add(('telethon.errors', 'BotMethodInvalidError'))
        imports.add(('telethon.tl.types', 'TypeSendMessageAction'))
        imports.add(('telethon.client.chats', '_ChatAction'))
        imports.add(('luckydonaldUtils.logger', 'logging'))
        imports.add(('telethon.tl.functions.messages', 'SetTypingRequest'))

        for function in functions:
            function: Function
            for the_import in function.imports:
                the_import: Import
                imports.add((the_import.path, the_import.name))
            # end for
        # end for
        # https://stackoverflow.com/a/613218/3423324#how-do-i-sort-a-dictionary-by-value
        # https://stackoverflow.com/a/4659539/3423324#how-to-sort-by-length-of-string-followed-by-alphabetical-order
        imports_sorted = ["from " + path + ' import ' + name for path, name in sorted(imports, key=lambda item: (-len(item[0]), item[0], -len(item[1]), item[1]))]
        # imports_sorted.sort(key=lambda item: (-len(item), item))

        txt = telegram_bot_api_server_funcs_template.render(functions=functions, imports=imports_sorted)
        render_file_to_disk(path_join(folder, 'telegram_bot_api_server', 'generated', 'funcs.py'), txt)
    # end if
    if message_send_functions:
        txt = teleflask_messages_template.render(functions=message_send_functions)
        render_file_to_disk(message_send_functions[0].filepath, txt)
    # end if
    if message_send_functions:
        txt = teleflask_messages_template.render(functions=message_send_functions)
        render_file_to_disk(message_send_functions[0].filepath, txt)
    # end if


# noinspection PyCompatibility
def render_file_to_disk(file, txt):
    with open(file, "w") as f:
        f.write(txt)
    # end with
    logger.info(f'Written {file!r} to disk, {len(txt)} chars.')
    if use_back:
        black.reformat_one(
            src=black.Path(file),
            write_back=black_settings['write_back'],
            fast=False,
            mode=black_settings['mode'],
            report=black_settings['report'],
        )
    # end if
    if use_yapf:
        try:
            FormatFile(file, in_place=True, style_config=yapf_settings['style'])
        except:
            logger.exception("Formatting file {file} failed.".format(file=file))
        # end try
    # end if


# end def


def calc_path_and_create_folders(folder, import_path, create_folder=True):
    """
    calculate the path and create the needed folders

    >>> calc_path_and_create_folders(folder='/somewhere/', import_path='foo.bar.BarClass', create_folder=False)
    '/somewhere/foo/bar/BarClass'

    :param import_path:  'foo.bar.BarClass'
    :param folder: base folder where we wanna place 'foo.bar.BarClass' in.
     """
    file_path = abspath(path_join(folder, import_path[:import_path.rfind(".")].replace(".", folder_seperator) + ".py"))
    if create_folder:
        mkdir_p(dirname(file_path))
    # end if
    return file_path
# end def


if __name__ == '__main__':
    main()
# end if
