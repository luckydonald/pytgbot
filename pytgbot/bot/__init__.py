#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from .synchronous import SyncBot as Bot

__author__ = 'luckydonald'
__all__ = ["Bot", "asynchronous", "synchronous"]

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


