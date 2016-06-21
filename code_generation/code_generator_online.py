# -*- coding: utf-8 -*-
from code_generator import get_type_path
from code_generator_template import clazz, func, get_template, Clazz, Function, ClassOrFunction, as_types, Type
from luckydonaldUtils.files import mkdir_p  # luckydonaldUtils v0.43+
from luckydonaldUtils.interactions import answer
from luckydonaldUtils.logger import logging

from code_generation.code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__PARENT

FILE_HEADER = "# -*- coding: utf-8 -*-\n"
MAIN_FILE_CLASS_HEADER = "class Bot(object):\n    _base_url = \"https://api.telegram.org/bot{api_key}/{command}\"\n"

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from os.path import abspath, dirname, join as path_join, sep as folder_seperator, isfile

BASE_URL = "https://core.telegram.org/bots/api"

def lol1(tag):
    return tag.has_attr("class") and "anchor" in tag["class"]


class_fields = ["Field", "Type", "Description"]
func_fields = ["Parameters", "Type", "Required", "Description"]

def parse_table(tag):
    """
    returns tuple of type ("class"/"func") and list of param strings.
    :param tag:
    :return:
    """
    first = True
    table_header = None
    param_strings = []
    for row in tag.find_all("tr"):
        i = 0
        if first:
            for column in row.find_all("td"):
                try:
                    col_text = column.find("strong").text
                    if i == 0:
                        if col_text == func_fields[0]:
                            table_header = func_fields
                        elif col_text == class_fields[0]:
                            table_header = class_fields
                        else:
                            raise AssertionError("Unknown table, starting with {}".format(col_text))
                    else:
                        assert col_text == table_header[i] , "Failed in column {i}, {text_is} != {text_should}.".format(
                            text_is=col_text, i=i, text_should=table_header[i]
                        )
                    # end if
                    i += 1
                except Exception:
                    raise
                # end try
            # end for column
        else: # is not first
            string = "\t".join([col.text for col in row.find_all("td")])
            logger.debug("t: " + string)
            param_strings.append(string)
            pass
        # end if first - else
        first = False
    # end for row
    type = "func" if table_header == func_fields else "class"
    return type, param_strings
# end def


def main():
    bot_template = get_template("bot.template")
    folder = get_folder_path()
    filter = get_filter()
    document = requests.get(BASE_URL)
    bs = BeautifulSoup(document.content)
    results = []
    for h in bs.select("#dev_page_content > h4"):
        print("------")
        anchor = h.find(lol1)
        if not anchor or not anchor.has_attr("name"):
            continue
        link = "{base_url}#{anchor}".format(base_url=BASE_URL, anchor=anchor["name"])
        title = h.text
        descr = []
        table_type, param_strings = None, None
        print("title: " + title)
        print("link: " + link)
        if filter and title not in filter:
            print("Skipping {title}, filtered.".format(title=title))
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
                        default_returns = (". ".join(return_text__).strip(), " or ".join(returns__).strip())
                    # end if
                # end if
                descr.append(sibling.text)
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
                print("unknown: " + sibling.name)
                # end if
        # end for
        if not all([table_type, param_strings, link, title, descr]):
            continue
        descr = "\n".join(descr)
        print("descr: " + repr(descr))
        params_string = "\n".join(param_strings)
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
                    default_returns = ("On success, True is returned", "True")
                # end if "return" in description
            else:
                seems_valid = len(default_returns[0].split(".")) == 1
            # end if default set
            if not seems_valid:
                returns       = answer("Textual description what the function returns", default_returns[0])
                return_type   = answer("Return type", default_returns[1])
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
                print("superclass: " + parent_clazz)
            else:
                parent_clazz = answer("Parent class name", "TgBotApiObject")
            # end if
            result = clazz(title, parent_clazz, descr, link, params_string)
            results.append(result)
        # end if
    # end for
    safe_to_file(folder, results)
    print("#########")
    # print("\n\n".join(results))


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


def get_folder_path():
    file = answer("Folder path to store the results.", default="/tmp/pytgbotapi/")
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



def safe_to_file(folder, results):
    """
    Receives a list of results (type :class:`Clazz` or :class:`Function`), and put them into the right files in :var:`folder`

    :param folder: Where the files should be in.
    :type  folder: str

    :param results: A list of :class:`Clazz` or :class:`Function` objects, which will be used to calculate the source code.
    :type  results: Union(Clazz, Function)

    """
    functions = []
    clazzes = {} # "filepath": [Class, Class, ...]

    # split results into functions and classes
    for result in results:
        assert isinstance(result, (Clazz, Function))
        if isinstance(result, Clazz):
            import_path = get_type_path(result.clazz)
            import_path = import_path.rstrip(".")
            file_path = calc_path_and_create_folders(folder, import_path)
            result.filepath = file_path
            if file_path not in clazzes:
                clazzes[file_path] = []
            clazzes[file_path].append(result)
        else:
            assert isinstance(result, Function)
            import_path = "pytgbot.bot."
            file_path = calc_path_and_create_folders(folder, import_path)
            result.filepath = file_path
            functions.append(result)
        # end if
    # end for

    bot_template = get_template("bot.template")
    clazzfile_template = get_template("classfile.template")
    for path, clazz_list in clazzes.items():
        clazz_imports = set()
        for clazz_ in clazz_list:
            assert isinstance(clazz_, Clazz)
            assert isinstance(clazz_.parent_clazz, Type)
            clazz_imports.add(clazz_.parent_clazz.as_import)
        # end for
        clazz_imports = list(clazz_imports)
        clazz_imports.sort()
        try:
            with open(path, "w") as f:
                result = clazzfile_template.render(clazzes=clazz_list, imports=clazz_imports)
                result = result.replace("\t", "    ")
                f.write(result)
                # end with
        except IOError:
            raise  # lol
            # end try
    # end for classes
    if functions:
        txt = bot_template.render(functions=functions)
        with open(functions[0].filepath, "w") as f:
            f.write(txt)
        # end with
    # end if
# end def


def calc_path_and_create_folders(folder, import_path):
    """ calculate the path and create the needed folders """
    file_path = abspath(path_join(folder, import_path[:import_path.rfind(".")].replace(".", folder_seperator) + ".py"))
    mkdir_p(dirname(file_path))
    return file_path


if __name__ == '__main__':
    main()