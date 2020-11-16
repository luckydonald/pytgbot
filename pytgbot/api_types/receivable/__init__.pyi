# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types import TgBotApiObject
from pytgbot.api_types.receivable import Receivable

__author__ = 'luckydonald'


class Receivable(TgBotApiObject):
    """
    Base class for all classes for stuff which telegram sends us.

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class Receivable

class Result(Receivable):
    """
    Base class for all classes for stuff which we throw in requests towards the telegram servers.

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class Result
