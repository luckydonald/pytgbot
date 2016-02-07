# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

from pytgbot import Bot
from pytgbot.types.inline import InlineQueryResultArticle

# get you bot instance.
bot = Bot(API_KEY)


my_info=bot.get_me()
print("Information about myself: {info}".format(info=my_info))
last_update_id = 0
while True:
    # loop forever.
    for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:
        last_update_id = update["update_id"]
        print(update)
        if not "inline_query" in update:
            continue
        query_obj = update.inline_query
        query = query_obj.query
        print (query)
        foo = InlineQueryResultArticle()

