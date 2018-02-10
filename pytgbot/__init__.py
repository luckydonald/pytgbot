# -*- coding: utf-8 -*-
import logging
from .bot import Bot

__author__ = 'luckydonald'
__version__ = "3.5.2.0"
__all__ = ["api_types", "Bot"]
VERSION = __version__

API_VERSION = "3" + "." + "5"  # so the bumpversion script doesn't breaks this.
API_DATE = "November 17, 2017"

logger = logging.getLogger(__name__)

