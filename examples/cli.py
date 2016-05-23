# -*- coding: utf-8 -*-
"""
A cli for bot api.
Supported commands are all `Bot.*` commands.
They need to be called with the parameter being json.
For the command
Custom commands to make stuff easier:
`msg <peer> <text>`
"""
import json
from pytgbot import Bot
from luckydonaldUtils.logger import logging
from luckydonaldUtils.interactions import input, answer
from inspect import getmembers, ismethod, getargspec, formatargspec
from threading import Thread

try:
    from somewhere import API_KEY  # so I don't upload them to github :D
except ImportError:
    API_KEY = None
# end if

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)

METHOD_EXCLUDES = ("do",)

cached_chats = {}

def main(API_KEY):
    if API_KEY is None:
        API_KEY = answer("Input API key")
    # get your bot instance.
    bot = Bot(API_KEY)
    my_info=bot.get_me()
    print("Information about myself: {info}".format(info=my_info))
    in_tread = Thread(target=get_updates, name="cli input thread", args=(bot,))
    in_tread.daemon = True
    in_tread.start()
    notice = "You can enter commands now.\n"
    while True:
        cmd = input(notice)
        notice = ""  # never display again.
        try:
            result_str = parse_input(bot, cmd)
            if result_str:
                print(result_str)
        except Exception as e:
            print("Error: " + str(e))
            raise
        # end try
    # end while
# end def


def parse_input(bot, cmd):
    if " " not in cmd:  # functions like get_me doesn't need params.
        print("No argument.")
        command, args = cmd, None
    else:
        command, args = cmd.split(" ", maxsplit=1)
    is_help = False
    if command in ["man", "help"]:
        return get_help(bot, args)
    if command == "msg":
        user, message = args.split(" ", maxsplit=1)
        user = cached_chats[user]
        return parse_call_result(bot.send_msg(user, message))
    cmd_func = getattr(bot, command)  # the function to call
    if args:
        parsed_args = json.loads(args)
        if not isinstance(parsed_args, (list,dict)):
            parsed_args = [str(parsed_args)]
        if isinstance(parsed_args, list):
            call_result = cmd_func(*parsed_args)
        else:
            assert isinstance(parsed_args, dict)
            call_result = cmd_func(**parsed_args)
        # end if isinstance
    else:
        return parse_call_result(cmd_func())
    # end id
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


def get_help(bot, search=""):
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


def get_updates(bot):
    last_update_id = 0
    while True:  # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:  # for every new update
            last_update_id = update["update_id"]
            try:
                print(update_to_string(update))
            except AttributeError:
                print(update)
                raise
            # end try
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


def update_to_string(data):
    if "message" in data:
        msg = data.message
        msg["update_id"] = data.update_id
        msg["from"]["print"] = peer_to_string_and_cache(msg["from"])
        if msg.chat.type == 'private':
            if "text" in msg:
                return "[msg {message_id}] {from.print}: {text}".format(**msg)
        elif msg.chat.type == 'group':
            if "text" in msg:
                return "[msg {message_id}] {from.print} ({chat.title}): {text}".format(**msg)
    elif "inline_query" in data:
        qry = data.inline_query
        qry["update_id"] = data.update_id
        qry["from"]["print"] = peer_to_string_and_cache(qry["from"])
        return "[query {id}] {from.print}: {query}".format(**qry)
    # end if message
    return str(data)
# end def


def peer_to_string_and_cache(peer, show_id=True):
    peer_string = peer_to_string(peer)
    cached_chats[peer_string.strip()] = peer.id
    cached_chats[str(peer.id).strip()] = peer.id
    cached_chats["!"] = peer.id
    if show_id and "id" in peer:
        peer_string += " (#{id})".format(**peer)
    return peer_string

def peer_to_string(peer):
    if "title" in peer:  # chats
        return "{title}".format(**peer)
    if "first_name" in peer:
        if "last_name" in peer:
            return "{first_name} {last_name}".format(**peer)
        # end if last_name
        return "{first_name}".format(**peer)
    # not first_name
    elif "last_name" in peer:
        return "{last_name}".format(**peer)
    elif "username" in peer:
        return "@{username}".format(**peer)
    elif "id" in peer:
        return "#{id}"
    # end if
    return "<UNKNOWN>"
# end def

if __name__ == '__main__':
    main(API_KEY)
# end if

# end file
