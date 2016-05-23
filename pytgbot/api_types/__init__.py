# -*- coding: utf-8 -*-
import logging
__author__ = 'luckydonald'

logger = logging.getLogger(__name__)


class TgBotApiObject(object):
    def to_array(self):
        array = dict()
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        if not array:
            return None
        array = array.copy()
        return array
    # end def
# end class
