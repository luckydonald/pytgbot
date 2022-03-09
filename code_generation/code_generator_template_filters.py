#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Match
import re

from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


SPLIT_LINE_REGEX = re.compile(r'(?P<char>:|\.|!|\?)(?P<whitespace>[\r\t\f\v ]+)')


def split_line_regex_replacer(match: Match) -> str:
    return match.group('char') + len(match.group('whitespace')) * "\n"
# end def


# noinspection PyShadowingBuiltins
def add_linebreaks(input: str) -> str:
    return SPLIT_LINE_REGEX.sub(split_line_regex_replacer, input)
# end def
