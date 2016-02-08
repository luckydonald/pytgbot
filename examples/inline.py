# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'luckydonald'

from random import getrandbits
import logging
logger = logging.getLogger(__name__)

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

from pytgbot import Bot
from pytgbot.types.inline import InlineQueryResultArticle
from pytgbot.encoding import to_native as n

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
        inline_query_id = update.inline_query.id
        query_obj = update.inline_query
        query = query_obj.query
        print (query)
        foo = []
        foo.append(InlineQueryResultArticle(id=1, title="test 1", message_text=query, description='Will send {}'.format(repr(n(query))), parse_mode="Markdown"))
        foo.append(InlineQueryResultArticle(id=2, title="test 2", message_text=query, description='Will send {}'.format(repr(n(query))), parse_mode="Markdown"))
        success = bot.answer_inline_query(inline_query_id, foo, cache_time=2)
        print(success)
        if not success.ok:
            print ("dayum!")
