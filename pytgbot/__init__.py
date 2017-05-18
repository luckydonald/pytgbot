# -*- coding: utf-8 -*-
import logging
from .bot import Bot

__author__ = 'luckydonald'
__version__ = "3.0.0"
__all__ = ["api_types", "Bot"]
VERSION = __version__

API_VERSION = "3" + "." + "0"  # so the bumpversion script doesn't breaks this.
API_DATE = "May 18, 2017"

logger = logging.getLogger(__name__)

