#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unittest import TestCase

from luckydonaldUtils.logger import logging

from pytgbot.api_types.receivable.updates import Update, Message

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)


# end if

class TestUpdate(TestCase):
    def test_1(self):
        data = {
            "update_id": 1234,
        }
        update = Update.from_array(data)
        self.assertEqual(1234, update.update_id)

        self.assertIsNone(update.message, "element should be not set")
        self.assertIsNone(update.callback_query, "element should be not set")
        self.assertIsNone(update.inline_query, "element should be not set")
        self.assertIsNone(update.channel_post, "element should be not set")
        self.assertIsNone(update.chosen_inline_result, "element should be not set")
        self.assertIsNone(update.edited_channel_post, "element should be not set")
        self.assertIsNone(update.poll, "element should be not set")
        self.assertIsNone(update.pre_checkout_query, "element should be not set")
        self.assertIsNone(update.shipping_query, "element should be not set")

        self.assertNotIn("message", update, "__contains__ should be false as well")
        self.assertNotIn("callback_query", update, "__contains__ should be false as well")
        self.assertNotIn("inline_query", update, "__contains__ should be false as well")
        self.assertNotIn("channel_post", update, "__contains__ should be false as well")
        self.assertNotIn("chosen_inline_result", update, "__contains__ should be false as well")
        self.assertNotIn("edited_channel_post", update, "__contains__ should be false as well")
        self.assertNotIn("poll", update, "__contains__ should be false as well")
        self.assertNotIn("pre_checkout_query", update, "__contains__ should be false as well")
        self.assertNotIn("shipping_query", update, "__contains__ should be false as well")

        new = Update(update_id=1234)
        self.assertEqual(data, new.to_array(), 'to_array()')
    # end def


class TestMessage(TestCase):
    def test_1(self):
        data = {
                "date": 1441645532,
                "chat": {
                    "id": 1111101,
                    "type": "private",
                    "first_name": "Alfred",
                    "last_name": "Alfons",
                },
                "message_id": 1365,
                "from": {
                    "id": 1111101,
                    "first_name": "Alfred",
                    "last_name": "Alfons",
                },
                "text": "/start"
            }
        msg = Message.from_array(data)
        self.assertEqual(1441645532, msg.date)

        from api_types.receivable.peer import Chat, User
        new = Message(
            message_id=1365, date=1441645532,
            chat=Chat(id=1111101, type="private", first_name="Alfred", last_name="Alfons"),
            from_peer=User(id=1111101, first_name="Alfred", last_name="Alfons"),
            text="/start"
        )
        self.assertEqual(data, new.to_array(), 'to_array()')
    # end def
# end class
