# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot import PytgBotObject

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

class Sendable(PytgBotObject):
    def __init__(self):
        super(Sendable, self).__init__()
    # end def __init__

    def to_array(self):
        return {}
    # end def to_array
# end class
