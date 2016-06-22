# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pytgbot.exceptions import TgApiException
from pytgbot.api_types.sendable.inline import InlineQueryResultArticle, InputTextMessageContent
from pytgbot.api_types.receivable.inline import InlineQuery
from pytgbot.api_types.receivable.updates import Update

__author__ = 'luckydonald'

from random import getrandbits
import logging
logger = logging.getLogger(__name__)

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

from pytgbot import Bot
from luckydonaldUtils.encoding import to_native as n
# get you bot instance.
bot = Bot(API_KEY)


my_info=bot.get_me()
print("Information about myself: {info}".format(info=my_info))
last_update_id = 0
while True:
    # loop forever.
    for update in bot.get_updates(limit=100, offset=last_update_id+1, error_as_empty=True):
        assert isinstance(update, Update)
        last_update_id = update.update_id
        print(update)
        if not update.inline_query:
            continue
        query_obj = update.inline_query
        assert isinstance(query_obj, InlineQuery)
        inline_query_id = query_obj.id
        query = query_obj.query
        print(query)
        foo = list()
        foo.append(InlineQueryResultArticle(
            id=query+"_normal",
            title="test 1 (normal)",
            input_message_content=InputTextMessageContent(query),
            description='Will send {}'.format(repr(n(query)))
        ))
        foo.append(InlineQueryResultArticle(
            id=query+"_markdown",
            title="test 2 (markdown)",
            input_message_content=InputTextMessageContent(query, parse_mode="Markdown"),
            description='Will send {}'.format(repr(n(query)))
        ))
        foo.append(InlineQueryResultArticle(
            id=query+"_html",
            title="test 3 (html)",
            input_message_content=InputTextMessageContent(query, parse_mode="HTML"),
            description='Will send {}'.format(repr(n(query)))
        ))
        try:
            success = bot.answer_inline_query(inline_query_id, foo, cache_time=2)
        except TgApiException:
            logger.warn("failed.", exc_info=True)
