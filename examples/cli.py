# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)



# -*- coding: utf-8 -*-

__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from pytgbot import Bot, InputFile

from somewhere import API_KEY  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

from queue import Queue

from threading import Thread

# get you bot instance.
from luckydonaldUtils.interactions import input


def main():
    bot = Bot(API_KEY)
    my_info=bot.get_me()
    print("Information about myself: {info}".format(info=my_info))
    in_tread = Thread(target=get_updates, name="cli input thread", args=(bot,))
    in_tread.daemon = True
    in_tread.start()
    notice = "You can enter commands now.\n"
    while True:
        cmd = input(notice)
        notice = ""
        print("would do something with {cmd}".format(cmd=repr(cmd)))  # TODO.
    # end while
# end def


def get_updates(bot):
    last_update_id = 0  # something.

    while True:  # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:  # for every new update
            last_update_id = update["update_id"]
            print(update_to_string(update))


def update_to_string(data):
    {'message': {'text': 'asd', 'from': {'username': 'luckydonald', 'id': 10717954, 'first_name': 'Luckydonald'},
                 'chat': {'username': 'luckydonald', 'id': 10717954, 'type': 'private', 'first_name': 'Luckydonald'},
                 'message_id': 5, 'date': 1461674481}, 'update_id': 307711634}

    {'message': {'from': {'username': 'luckydonald', 'id': 10717954, 'first_name': 'Luckydonald'},
                 'new_chat_member': {'username': 'test4458bot', 'id': 133378542, 'first_name': 'Derpibot'},
                 'message_id': 6, 'date': 1461674709, 'chat': {'id': -142938350, 'type': 'group', 'title': 'derpytest'},
                 'new_chat_participant': {'username': 'test4458bot', 'id': 133378542, 'first_name': 'Derpibot'}},
     'update_id': 307711635}


    if data.message.chat.type == 'private':
        return "{message_id} {from.first_name}: {text}".format(**data.message)
    elif data.message.chat.type == 'group':
        return "{message_id} {from.first_name} ({chat.title}): {text}".format(**data.message)
    return str(data)
# end def

"""
[*Revision 60: first steps kinect connect*](https://sep.isf.cs.tu-bs.de/redmine/projects/16-cg-2/repository/revisions/60
) — _Kay-Kristian Donner_
Die Fenstergröße wird zum Programmstart einmalig gesetzt, und kann/soll anschließend nur zwischen dieser Größe und de...
"""

if __name__ == '__main__':
    main()
# end if

# end file
