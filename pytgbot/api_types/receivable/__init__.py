# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from .. import TgBotApiObject

__author__ = 'luckydonald'
__all__ = [
    'Receivable',
    'Result',
]
__all__ += ["game", "inline", "media", "payments", "peer", "stickers", "updates", "Receivable", "Result", "WebhookInfo"]


class Receivable(TgBotApiObject):
    """
    Base class for all classes for stuff which telegram sends us.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    pass
# end class Receivable


class Result(Receivable):
    """
    Base class for all classes for stuff which we throw in requests towards the telegram servers.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    pass
# end class Result

from .updates import WebhookInfo
