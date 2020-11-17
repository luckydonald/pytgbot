# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["game", "inline", "media", "payments", "peer", "stickers", "updates", "command", "Receivable", "Result", "WebhookInfo"]


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
