# -*- coding: utf-8 -*-
from luckydonaldUtils.functions import deprecated
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["files", "inline", "payments", "reply_markup", "Sendable"]

# UPCOMING CHANGE IN v2.2.0:
from . import files  # backwards compatibility, before v2.2.0

logger = logging.getLogger(__name__)


class Sendable(TgBotApiObject):
    """
    Base class for all classes for stuff which we throw in requests towards the telegram servers.

    Optional keyword parameters:
    """

    pass
# end class Sendable
