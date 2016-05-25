# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject
from pytgbot.api_types.receivable.peer import User

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Receivable(TgBotApiObject):
    pass
# end class Receivable


class Result(Receivable):
    def to_array(self):
        return {}
    pass
# end class Result
