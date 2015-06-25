# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from pytgbot import Bot

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345


bot = Bot(API_KEY)

bot.send_msg(TEST_CHAT, "another test.")
for x in bot.get_updates()["result"]:
	print(x)
bot.get_me()