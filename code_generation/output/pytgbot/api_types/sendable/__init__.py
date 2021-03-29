# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import TgBotApiObject

__author__ = 'luckydonald'
__all__ = [
    'Sendable',
]


class Sendable(TgBotApiObject):
    """
    Base class for all classes for stuff which we throw in requests towards the telegram servers.

    Optional keyword parameters:
    """

    pass
# end class Sendable
