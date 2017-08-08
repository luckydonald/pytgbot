# -*- coding: utf-8 -*-
"""
A cli for bot api.
Supported commands are all `Bot.*` commands.
They need to be called with the parameter being json.
For the command
Custom commands to make stuff easier:
`msg <peer> <text>`
"""
import requests

from pytgbot.api_types.receivable.inline import InlineQuery
from pytgbot.api_types.receivable.updates import Message, Update
from pytgbot.api_types.receivable.peer import Peer, Chat, User
from pytgbot.exceptions import TgApiException
from pytgbot import Bot
from luckydonaldUtils.logger import logging
from luckydonaldUtils.interactions import input, answer
from luckydonaldUtils.encoding import to_binary as b, to_native as n
from inspect import getmembers, ismethod, getargspec, formatargspec
from threading import Thread

# cool input
import readline

# cool output
# see iterm2_image module source,
# at https://github.com/zakx/iterm2_image/blob/f1134a720c37a515c5b15c438ae7bca92d4d4c55/iterm2_image.py
from io import BytesIO
from base64 import b64encode
import sys


def read_file_to_buffer(filename):
    """
    Reads a file to string buffer
    :param filename: 
    :return: 
    """
    f = open(filename, "r")
    buf = BytesIO(f.read())
    f.close()
    return buf
# end def


def iterm_show_file(filename, data=None, inline=True, width="auto", height="auto", preserve_aspect_ratio=True):
    """

    https://iterm2.com/documentation-images.html
    
    :param filename: 
    :param data: 
    :param inline: 
    :param width:  
    :param height: 
    :param preserve_aspect_ratio: 
    
    Size:
        - N   (Number only): N character cells.
        - Npx (Number + px): N pixels.
        - N%  (Number + %):  N percent of the session's width or height.
        - auto:              The image's inherent size will be used to determine an appropriate dimension.
    :return: 
    """
    width = str(width) if width is not None else "auto"
    height = str(height) if height is not None else "auto"
    if data is None:
        data = read_file_to_buffer(filename)
    # end if
    data_bytes = data.getvalue()
    output = "\033]1337;File=" \
             "name={filename};size={size};inline={inline};" \
             "preserveAspectRatio={preserve};width={width};height={height}:{data}\a\n".format(
        filename=n(b64encode(b(filename))), size=len(data_bytes), inline=1 if inline else 0,
        width=width, height=height, preserve=1 if preserve_aspect_ratio else 0,
        data=n(b64encode(data_bytes)),
    )
    #sys.stdout.write(output)
    return output
# end if


try:
    from somewhere import API_KEY  # so I don't upload them to github :D
except ImportError:
    API_KEY = None
# end if

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)#
logging.add_colored_handler(level=logging.INFO)

METHOD_EXCLUDES = ("do",)

cached_chats = {}

class CLI(object):
    def __init__(self, API_KEY):
        if API_KEY is None:
            API_KEY = self.ask_for_apikey()
        self._api_key = API_KEY

        self.bot = Bot(API_KEY, return_python_objects=True)

        self.me = self.bot.get_me()
        logger.info("Information about myself: {info}".format(info=self.me))

        self.completer = self.register_tab_completion()

        self.update_thread = self.create_update_thread()

    # end def

    def ask_for_apikey(self):
        return answer("Input your bot API key.")
    # end def

    def register_tab_completion(self):
        # Register our completer function
        completer = FunctionCompleter(self)
        readline.parse_and_bind('tab: complete')
        readline.set_completer(completer.complete)
        # Use the tab key for completion
        return completer
    # end def

    def create_update_thread(self):
        tg_update_thread = Thread(target=get_updates, name="telegram update thread", args=(self.bot,), kwargs={"callback": self.print_update})
        tg_update_thread.daemon = True
        tg_update_thread.start()
        return tg_update_thread
    # end def

    def run(self):
        print("You can enter commands now.")
        while True:
            cmd = input("pytgbot> ")
            try:
                result_str = parse_input(self.bot, cmd)
                if result_str:
                    print(result_str)
            except Exception as e:
                logger.exception("Error.")
                print("Error: " + str(e))
            # end try
        # end while
    # end def

    def print_update(self, update):
        print(self.process_update(update))
    # end def

    def process_update(self, update):
        assert isinstance(update, Update)  # is message
        if update.message:
            return self.process_message(update.message)
        elif update.inline_query:
            qry = update.inline_query
            assert isinstance(qry, InlineQuery)
            qry_from_print = peer_to_string_and_cache(qry.from_peer)
            return "[query {id}] {from_print}: {text}".format(from_print=qry_from_print, id=qry.id, text=qry.query)
        else:
            return str(update)
        # end if
    # end def

    def process_message(self, msg):
        # prepare prefix with chat infos:
        assert isinstance(msg, Message)
        user_print = peer_to_string_and_cache(msg.from_peer, id_prefix="user")
        if msg.chat.type == 'private':
            prefix = "[msg {message_id}] {user}: ".format(
                message_id=msg.message_id, user=user_print
            )
        elif msg.chat.type in ('group', 'supergroup', 'channel'):
            group_print = peer_to_string_and_cache(msg.chat, id_prefix=True)
            prefix = "[msg {message_id}] {user} in {title}: ".format(
                message_id=msg.message_id, user=user_print, title=group_print
            )
        else:
            prefix = "[msg {message_id}] UNKNOWN ORIGIN: ".format(
                message_id=msg.message_id
            )
        # end if

        # now the message types
        if "text" in msg:
            return prefix + msg.text
        if "photo" in msg:
            photo = msg.photo[0]
            for p in msg.photo[1:]:
                if p.file_size > photo.file_size:
                    photo = p
                # end if
            # end for
            return prefix + self.process_file(photo, msg.caption, file_type="photo", height="100px")
        if "sticker" in msg:
            return prefix + self.process_file(msg.sticker, msg.caption, file_type="sticker", as_png=True, height="100px")
        # end if
    # end def

    def process_file(self, file, caption, file_type="file", as_png=False, inline=True, height=None):
        file_object = self.bot.get_file(file.file_id)
        file_url = self.bot.get_download_url(file_object)
        file_content = get_file(file_url, as_png=as_png)
        file_name = file_url.split("/")[-1]
        if as_png:
            file_name = file_name + ".png"
        # end if
        save_file_name = str(file.file_id) + "__" + file_name
        return "[{type} {file_id}]{caption}\n{image}\n{file_name}".format(
            file_id=file.file_id, caption=(" " + caption if caption else ""),
            image=iterm_show_file(save_file_name, data=file_content, inline=inline, height=height),
            type=file_type, file_name=save_file_name,
        )
    # end def

# end class


def get_file(file_url, as_png=True):
    r = requests.get(file_url)
    if r.status_code != 200:
        logger.error("Download returned: {}".format(r.content))
        return None
    # end if
    fake_input = BytesIO(r.content)
    if not as_png:
        return fake_input
    # end if
    from PIL import Image  # pip install Pillow
    im = Image.open(fake_input)
    del fake_input
    fake_output = BytesIO()
    im.save(fake_output, "PNG")
    del im
    fake_output.seek(0)
    return fake_output
# end def

def parse_input(bot, cmd):
    print(">{cmd}".format(cmd=cmd))
    if " " not in cmd:  # functions like get_me doesn't need params.
        command, args = cmd, None
    else:
        command, args = cmd.split(" ", maxsplit=1)
    is_help = False
    if command in ["man", "help"]:
        return get_help(bot, args)
    if command == "msg":
        user, message = args.split(" ", maxsplit=1)
        try:
            user = cached_chats[user]
        except KeyError:
            return "[FAIL] I don't have that peer cached."
            # TODO: accept anyway? So you can use a username or something?
        try:
            result = bot.send_msg(user, message)
            return "[ OK ] {}".format(result)
        except TgApiException as e:
            return "[FAIL] {}".format(e)
    cmd_func = getattr(bot, command)  # the function to call
    try:
        if args:
            parsed_args = parse_args(args)
            if not isinstance(parsed_args, (list,dict)):
                parsed_args = [str(parsed_args)]
            # end if not isinstance
            if isinstance(parsed_args, list):
                call_result = cmd_func(*parsed_args)
            else:
                assert isinstance(parsed_args, dict)
                call_result = cmd_func(**parsed_args)
            # end if isinstance
        else:
            call_result = cmd_func()
            # end if
        # end if
        print("[ OK ] {result}".format(
            result=call_result
        ))
    except TgApiException as e:
        print("[FAIL] {exception}".format(exception=e))
    # end try
# end def


def parse_call_result(call_result):
    if "ok" in call_result and "response" in call_result and "result" in call_result:
        result_str = "[{status}] {result}".format(
            status="OK  " if call_result.ok else "FAIL",
            result=format_array(call_result.result, prefix=" ", prefix_count=7)
        )
        return result_str
    # end if has 'ok', 'response' and 'result'
    return "'ok', 'response' or 'result' missing. Data: {data}".format(data=call_result)
# end def


def get_help(bot, search="", return_string=True):
    strings = []
    for name, func in getmembers(bot):
        if name.startswith("_"):
            continue
        if name in METHOD_EXCLUDES:
            continue
        if search and not name.startswith(search):
            continue
        if ismethod(func):
            func_str = "{func} - {doc}".format(func=get_func_str(func), doc=func.__doc__.strip().split("\n")[0])
            if search and search == name:  # perfect hit
                func_def = "def " + get_func_str(func) + ":"
                seperator = ("-"*(len(func_def)-1))
                return func_def + "\n|>" + seperator + "\n|  " + ("\n| ".join(func.__doc__.strip().split("\n")) +"\n'>" +  seperator)
            strings.append(func_str)
        # end if
    # end for
    return "\n".join(strings)
# end def


def get_func_str(func):
    spec = func.__name__ + formatargspec(*getargspec(func))
    return spec


def get_updates(bot, callback=None):
    if callback is None:
        def callback(data):
            try:
                print(update_to_string(data))
            except AttributeError:
                print(update)
                raise
            # end try
        # end def
    # end if
    last_update_id = 0
    while True:  # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1, poll_timeout=60, error_as_empty=True):  # for every new update
            last_update_id = update.update_id
            print(repr(last_update_id))
            callback(update)
        # end for
    # end while
# end def


ARRAY_ROW_FORMAT = "{prefix}{key}: {value}{postfix}"


def format_array(array, prefix="", prefix_count=1):
    string_to_return = ""
    prefix_to_use = prefix * prefix_count
    for key in array.keys():
        if string_to_return == "":
            string_to_return = ARRAY_ROW_FORMAT.format(
                prefix="", key=key, value=str(array[key]), postfix="\n"
            )
        else:
            string_to_return += ARRAY_ROW_FORMAT.format(
                prefix=prefix_to_use, key=key, value=str(array[key]), postfix="\n"
            )
    # end for
    return string_to_return
# end def





def peer_to_string_and_cache(peer, show_id=True, id_prefix="", reply=True):
    """

    :param peer: 
    :param show_id: 
    :param id_prefix: Prefix of the #id thing. Set a string, or true to have it generated.
    :type  id_prefix: str|bool
    :param reply: 
    :return: 
    """
    if isinstance(id_prefix, bool):
        if id_prefix:  # True
            if isinstance(peer, User):
                id_prefix = "user"
            elif isinstance(peer, Chat):
                id_prefix = peer.type
            else:
                id_prefix = "unknown"
            # end if
        else:  # False
            id_prefix = ""
        # end if
    # end if
    peer_string = peer_to_string(peer)
    cached_chats[peer_string.strip()] = peer.id
    cached_chats[str(peer.id).strip()] = peer.id
    if reply:
        cached_chats["!"] = peer.id
    # end if
    if show_id and "id" in peer:
        peer_string += " ({id_prefix}#{id})".format(id_prefix=id_prefix, id=peer.id)
    return peer_string

def peer_to_string(peer):
    assert isinstance(peer, Peer)

    if isinstance(peer, Chat):  # chats
        return "{title}".format(title=peer.title)
    assert isinstance(peer, User)
    if peer.first_name:
        if peer.last_name:
            return "{first_name} {last_name}".format(first_name=peer.first_name, last_name=peer.last_name)
        # end if last_name
        return "{first_name}".format(first_name=peer.first_name)
    # not first_name
    elif peer.last_name:
        return "{last_name}".format(last_name=peer.last_name)
    elif peer.username:
        return "@{username}".format(username=peer.username)
    elif peer.id:
        return "#{id}".format(id=peer.id)
    # end if
    return "<UNKNOWN>"
# end def



def parse_args(string):
    """
    `"yada hoa" yupi yeah 12 "" None "None"` -> `["yada hoa", "yupi", "yeah", 12, "", None, "None"]`
    :param str:
    :return:
    """
    import ast
    is_quoted = False
    result_parts = []
    current_str = ""
    while len(string) > 0:
        if string[0] == "\"":
            is_quoted = not is_quoted
            current_str += string[0]
        elif string[0].isspace():
            if is_quoted:
                current_str += string[0]
            else:
                result_parts.append(current_str)
                current_str = ""
            # end if
        else:
            current_str += string[0]
        # end if
        string = string[1:]
    # end while
    if current_str:  # last part of the array
        result_parts.append(current_str)
    # end if
    for i in range(len(result_parts)):
        # Will try for each element if it is something pythonic. Parsed type will replace original list element.
        try:
            part = ast.literal_eval(result_parts[i])
            result_parts[i] = part  # write it back.
        except ValueError:
            # could not parse -> is string
            pass  # because already is str.
        # end try
    # end for
    return result_parts
# end def parse_args


class FunctionCompleter(object):
    def __init__(self, cli):
        logger.debug("Started completion!")
        self.cli = cli
        self.bot = cli.bot
        self.functions = {k:v for k,v in self.get_functions()}
        self.functions["help"] = self.cmd_help
        self.current_candidates = []
    # end def

    def cmd_help(self, *args, **kwargs):
        return help(*args, **kwargs)

    def get_functions(self):
        for name, func in getmembers(self.bot):
            if name.startswith("_"):
                continue
            # end if
            if name in METHOD_EXCLUDES:
                continue
            # end if
            elif not ismethod(func):
                continue
            # end if
            yield name, func
        # end for
    # end def

    def complete(self, text, state):
        if state == 0:  # first of list, prepare the list
            self.current_candidates = [cmd for cmd in list(self.functions.keys()) if cmd.startswith(text)]
        # end if
        try:
            return self.current_candidates[state]
        except IndexError:
            return None
        # end try
        if True:
            pass
        else:
            return None
            # This is the first time for this text, so build a match list.
            origline = readline.get_line_buffer()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            logger.debug('origline=%s', repr(origline))
            logger.debug('begin=%s', begin)
            logger.debug('end=%s', end)
            logger.debug('being_completed=%s', being_completed)
            logger.debug('words=%s', words)

            if not words:
                self.current_candidates = sorted(self.functions.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.functions.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.functions[first]

                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [w for w in candidates
                                                   if w.startswith(being_completed)]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    logging.debug('candidates=%s', self.current_candidates)

                except (KeyError, IndexError) as err:
                    logging.error('completion error: %s', err)
                    self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        logging.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response


if __name__ == '__main__':
    cli = CLI(API_KEY)
    cli.run()
# end if

# end file
