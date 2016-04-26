# -*- coding: utf-8 -*-
import json
from pytgbot import Bot
from luckydonaldUtils.logger import logging
from luckydonaldUtils.interactions import input, answer

try:
    from somewhere import API_KEY  # so I don't upload them to github :D
except ImportError:
    API_KEY = None
# end if

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)



from threading import Thread

# get you bot instance.


def main(API_KEY):
    if API_KEY is None:
        API_KEY = answer("Input API key")
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
        print("Would do something with {cmd}".format(cmd=repr(cmd)))  # TODO.
        try:
            command, args = cmd.split(" ", maxsplit=1)
            # print(bot.do(command, **json.loads(args)))
        except Exception as e:
            print(e)
    # end while
# end def


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


def update_to_string(data):
    if "message" in data:
        msg = data.message
        msg["update_id"] = data.update_id
        msg["from"]["print"] = peer_to_string(msg["from"])
        if msg.chat.type == 'private':
            if "text" in msg:
                return "[msg {message_id}] {from.print}: {text}".format(**msg)
        elif msg.chat.type == 'group':
            if "text" in msg:
                return "[msg {message_id}] {from.print} ({chat.title}): {text}".format(**msg)
    elif "inline_query" in data:
        qry = data.inline_query
        qry["update_id"] = data.update_id
        qry["from"]["print"] = peer_to_string(qry["from"])
        return "[query {id}] {from.print}: {query}".format(**qry)
    # end if message
    return str(data)
# end def


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
