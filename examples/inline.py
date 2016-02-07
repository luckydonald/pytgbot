# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

from pytgbot import Bot
from pytgbot.types.reply_markup import ReplyKeyboardMarkup, ForceReply

# get you bot instance.
bot = Bot(API_KEY)


my_info=bot.get_me()
print("Information about myself: {info}".format(info=my_info))
while True:
	# loop forever.
	for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:
		last_update_id = update["update_id"]
        print(update)
