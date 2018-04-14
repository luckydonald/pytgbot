# -*- coding: utf-8 -*-
import logging
from .bot import Bot

__author__ = 'luckydonald'
__version__ = "3.6.0"
__all__ = ["api_types", "Bot"]
VERSION = __version__

API_VERSION = "3" + "." + "6"  # so the bumpversion script doesn't breaks this accidentally.
API_DATE = "February 13, 2018"

logger = logging.getLogger(__name__)

