# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'


class Sendable(TgBotApiObject):
    """
    Base class for all classes for stuff which we throw in requests towards the telegram servers.

    Optional keyword parameters:
    """
# end class Sendable
