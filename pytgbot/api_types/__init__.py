# -*- coding: utf-8 -*-
import logging
from json import dumps as _json_dumps
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


def as_array(object):
    if hasattr(object, "to_array"):
        return object.to_array()
    elif isinstance(object, (list,tuple)):
        return [as_array(x) for x in object]
    elif isinstance(object, dict):
        array = {}
        for key in object.keys():
            array[key] = as_array(object[key])
        # end for
        return array
    else:
        _json_dumps(object)  # raises error if is wrong json
        return object