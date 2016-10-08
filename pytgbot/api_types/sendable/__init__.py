# -*- coding: utf-8 -*-
from luckydonaldUtils.functions import deprecated
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["inline", "reply_markup", "files", "Sendable", "InputFile", "InputFileFromURL", "InputFileFromDisk"]

# UPCOMING CHANGE IN v2.2.0:
from . import files  # backwards compatibility, before v2.2.0

logger = logging.getLogger(__name__)


class Sendable(TgBotApiObject):
    def __init__(self):
        super(Sendable, self).__init__()
    # end def __init__
# end class


class InputFile(files.InputFile):
    @deprecated
    def __init__(self, *args, **kwargs):
        super(InputFile, self).__init__(*args, **kwargs)
        logger.warning("Depricated! Import this class from pytgbot.api_types.sendable.files instead!")
    # end def
# end class


class InputFileFromURL(files.InputFileFromURL):
    @deprecated
    def __init__(self, *args, **kwargs):
        super(InputFileFromURL, self).__init__(*args, **kwargs)
        logger.warning("Depricated! Import this class from pytgbot.api_types.sendable.files instead!")
    # end def
# end class


class InputFileFromDisk(files.InputFileFromDisk):
    @deprecated
    def __init__(self, *args, **kwargs):
        super(InputFileFromDisk, self).__init__(*args, **kwargs)
        logger.warning("Depricated! Import this class from pytgbot.api_types.sendable.files instead!")
    # end def
# end class
