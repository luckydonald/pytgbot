# -*- coding: utf-8 -*-
from luckydonaldUtils.interactions import answer
from luckydonaldUtils.logger import logging
from luckydonaldUtils.files import mkdir_p  # luckydonaldUtils v0.43+
from code_generator import func, clazz, get_type_path
from code_generator_settings import CLASS_TYPE_PATHS, CLASS_TYPE_PATHS__PARENT

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


file = answer("Folder path to store the results.", default="/tmp/pytgbotapi/")
if file:
    try:
        file = abspath(file)
        mkdir_p(file)
        with open(path_join(file ,"__init__.py"), "w") as f:
            f.write(FILE_HEADER)
            # end with
    except IOError:
        pass
        # end try
# end if file
filter = answer(
    "Only generate the doc for specific functions/classes. Comma seperated list. Leave empty to generate all.",
    default=""# getChat, leaveChat, getChatAdministrators, getChatMember, getChatMembersCount, Message, MessageEntity"
)
if filter.strip():
    filter = [x.strip() for x in filter.split(",")]
else:
    filter = None
# end if
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
                for lol_part in parts_splitted:
                    has_return = False
                    returns_ = []
                    return_text_ = ""
                    for lol_part_part in lol_part:
                        if isinstance(lol_part_part, str):
                            return_text_ += lol_part_part
                            if "return" in lol_part_part.lower():
                                has_return = True
                            # end if
                        else:  # not str
                            return_text_ += lol_part_part.text
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
    # clazz(clazz, parent_clazz, description, link, params_string, init_super_args=None):
    if table_type == "func":
        if len(default_returns) == 0:
            if "return" in descr.lower():
                default_returns = ["", "Message"]
                default_returns[0] = [x for x in descr.split(".") if "return" in x.lower()][0].strip()
                default_returns[1] = " or ".join(type_strings) if type_strings else "Message"
            else:
                default_returns = ("On success, the sent Message is returned.", "Message")
        returns       = answer("Textual description what the function returns", default_returns[0])
        return_type   = answer("Return type", default_returns[1])
        logger.debug("\n")
        result = func(title, descr, link, params_string, returns=returns, return_type=return_type)
    elif table_type == "class":
        if title in CLASS_TYPE_PATHS:
            parent_clazz = CLASS_TYPE_PATHS[title][CLASS_TYPE_PATHS__PARENT]
            print("superclass: " + parent_clazz)
        else:
            parent_clazz = answer("Parent class name", "TgBotApiObject")
        # end if
        result = clazz(title, parent_clazz, descr, link, params_string)
    # end if
    results.append(result)
    if file:
        try:
            if table_type == "class":
                import_path = get_type_path(title)
                import_path = import_path.rstrip(".")
                if import_path == title:
                    "pytgbot.api_types." + title.lower() + "."
            else:
                import_path = "pytgbot.__init__."
            file_path = abspath(path_join(file, import_path[:import_path.rfind(".")].replace(".", folder_seperator)+".py"))
            mkdir_p(dirname(file_path))
            need_header = not isfile(file_path)
            with open(file_path, "a") as f:
                if need_header:
                    f.write(FILE_HEADER)
                    if table_type == "func":
                        f.write(MAIN_FILE_CLASS_HEADER)
                f.write("\n" + result + "\n")
            # end with
        except IOError:
            pass
        # end try
    # end if file
# end for
print("#########")
print("\n\n".join(results))
