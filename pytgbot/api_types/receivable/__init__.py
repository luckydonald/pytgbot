# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["game", "inline", "media", "payments", "peer", "stickers", "updates", "Receivable", "Result", "WebhookInfo"]
logger = logging.getLogger(__name__)


class Receivable(TgBotApiObject):
    pass
# end class Receivable


class Result(Receivable):
    def to_array(self):
        return {}
    pass
# end class Result

from .updates import WebhookInfo
