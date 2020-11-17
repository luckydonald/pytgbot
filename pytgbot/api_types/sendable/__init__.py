# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from .. import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["files", "inline", "payments", "reply_markup", "Sendable"]

# UPCOMING CHANGE IN v2.2.0:
from . import files  # backwards compatibility, before v2.2.0


class Sendable(TgBotApiObject):
    """
    Base class for all classes for stuff which we throw in requests towards the telegram servers.

    Optional keyword parameters:
    """

    pass
# end class Sendable

