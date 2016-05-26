# -*- coding: utf-8 -*-
import json

from pytgbot import Bot
from pytgbot.api_types import as_array
from pytgbot.api_types.sendable.reply_markup import ForceReply, ReplyKeyboardHide, ReplyKeyboardMarkup, KeyboardButton

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

__author__ = 'luckydonald'


# get you bot instance.
bot = Bot(API_KEY)

def main():
    my_info=bot.get_me()
    print("Information about myself: {info}".format(info=my_info))
    last_update_id = -1
    while True:
        for update in bot.get_updates(limit=1, offset=last_update_id+1)["result"]:
            last_update_id = update["update_id"]
            print(update)
            if "message" not in update or "entities" not in update.message:
                continue
            for entity in update.message.entities:
                # MessageEntity
                if entity.type == "bot_command":
                    command = update.message.text[entity.offset:entity.offset+entity.length]
                    if command == "/key":
                        do_keyboard(update.message.chat.id)
                    elif command == "/unkey":
                        hide_keyboard(update.message.chat.id)
                    # end if

            # end for
        # end for update
    # end while forever
# end def main


def do_keyboard(chat_id):
    buttons = [
        ["YES", "NO"],
        ["Maybe", "lol"]  # KeyboardButton("Contact?", request_contact=True)]
    ]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    print(bot.send_msg(chat_id, "test!", reply_markup=markup))


def hide_keyboard(chat_id):
    print(bot.send_msg(chat_id, "okey, keyboard hidden.", reply_markup=ReplyKeyboardHide()))
main()

