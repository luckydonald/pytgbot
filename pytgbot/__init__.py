# -*- coding: utf-8 -*-
import logging
from .bot import Bot

__author__ = 'luckydonald'
__version__ = "3.3.0"
__all__ = ["api_types", "Bot"]
VERSION = __version__

API_VERSION = "3" + "." + "3"  # so the bumpversion script doesn't breaks this.
API_DATE = "August 23, 2017"

logger = logging.getLogger(__name__)

