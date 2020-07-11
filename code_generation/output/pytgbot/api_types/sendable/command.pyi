# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result

__author__ = 'luckydonald'


class BotCommand(Result):
    """
    This object represents a bot command.

    https://core.telegram.org/bots/api#botcommand
    

    Parameters:
    
    :param command: Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    :type  command: str|unicode
    
    :param description: Description of the command, 3-256 characters.
    :type  description: str|unicode
    

    Optional keyword parameters:
    """
    command: str
    description: str
# end class BotCommand
