#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from .syncrounous import Bot

__author__ = 'luckydonald'
__all__ = ["Bot", "syncrounous", "asyncrounous"]

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


