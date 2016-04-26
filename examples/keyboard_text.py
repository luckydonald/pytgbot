# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from pytgbot import Bot
from pytgbot.api_types.reply_markup import ReplyKeyboardMarkup, ForceReply

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

# get you bot instance.
bot = Bot(API_KEY)


my_info=bot.get_me()
print("Information about myself: {info}".format(info=my_info))
print(bot.send_msg(TEST_CHAT, "test", reply_markup=ForceReply([["YES", "NO"]])))



