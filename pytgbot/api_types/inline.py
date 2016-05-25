# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.inline import InputMessageContent
from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

__author__ = 'luckydonald'

from ..encoding import text_type as unicode_type, to_unicode as u
import logging
logger = logging.getLogger(__name__)
