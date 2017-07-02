# -*- coding: utf-8 -*-
import logging
from .bot import Bot

__author__ = 'luckydonald'
__version__ = "3.1.0"
__all__ = ["api_types", "Bot"]
VERSION = __version__

API_VERSION = "3" + "." + "1"  # so the bumpversion script doesn't breaks this.
API_DATE = "June 30, 2017"

logger = logging.getLogger(__name__)

