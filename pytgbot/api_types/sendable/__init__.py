# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Sendable(TgBotApiObject):
    def __init__(self):
        super(Sendable, self).__init__()
    # end def __init__
# end class
