# -*- coding: utf-8 -*-
from luckydonaldUtils.functions import deprecated
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["files", "inline", "payments", "reply_markup", "Sendable", "InputFile", "InputFileFromURL", "InputFileFromDisk"]

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


class InputFile(files.InputFile):
    @deprecated
    def __init__(self, *args, **kwargs):
        super(InputFile, self).__init__(*args, **kwargs)
        logger.warning("Deprecated! Import this class from pytgbot.api_types.sendable.files instead!")
    # end def
# end class


class InputFileFromURL(files.InputFileFromURL):
    @deprecated
    def __init__(self, *args, **kwargs):
        super(InputFileFromURL, self).__init__(*args, **kwargs)
        logger.warning("Deprecated! Import this class from pytgbot.api_types.sendable.files instead!")
    # end def
# end class


class InputFileFromDisk(files.InputFileFromDisk):
    @deprecated
    def __init__(self, *args, **kwargs):
        super(InputFileFromDisk, self).__init__(*args, **kwargs)
        logger.warning("Deprecated! Import this class from pytgbot.api_types.sendable.files instead!")
    # end def
# end class
