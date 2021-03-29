# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result

__author__ = 'luckydonald'


class MessageId(Result):
    """
    This object represents a unique message identifier.

    https://core.telegram.org/bots/api#messageid


    Parameters:

    :param message_id: Unique message identifier
    :type  message_id: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    message_id: int
# end class MessageId
