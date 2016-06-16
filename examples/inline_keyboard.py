# -*- coding: utf-8 -*-
from pytgbot.api_types.sendable.reply_markup import InlineKeyboardButton

__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from pytgbot import Bot
from pytgbot.api_types.sendable.inline import InlineKeyboardMarkup

from somewhere import API_KEY  # just set the key manually.
# API_KEY = "1231412:adLsIfTsTsLfEfPdIdPwdwIoSaBgEuSzTwszPdOaNdYs"


# get a bot instance
bot = Bot(API_KEY)

last_update_id = -1


while True:
    # loop forever.
    for update in bot.get_updates(limit=100, offset=last_update_id+1, timeout=30).result:
        last_update_id = update["update_id"]
        if not "message" in update and "/start" in update.message.text:
            continue
        message = update.message
        print("got message: {msg}".format(msg=update))
        # peer = message.reply_to_message["from"].id
        peer = message["from"].id
        photos = bot.get_user_profile_photos(peer)["result"]["photos"]
        origin = message.chat.id if "chat" in message else message["from"].id
        current_image = 0
        selected_photo = photos[current_image]
        biggest_image = max(selected_photo, key=lambda p: p["file_size"])  # get the biggest image.
        buttons = [[]]
        buttons[0].append(InlineKeyboardButton("<<", callback_data="<<"))
        markup = InlineKeyboardMarkup(buttons)
        print(bot.send_photo(origin, biggest_image["file_id"], caption="test", reply_markup=markup))