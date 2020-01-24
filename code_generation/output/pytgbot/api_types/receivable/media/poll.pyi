# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Receivable
from pytgbot.api_types.receivable.media import Media

__author__ = 'luckydonald'


class PollOption(Receivable):
    """
    This object contains information about one answer option in a poll.

    https://core.telegram.org/bots/api#polloption
    

    Parameters:
    
    :param text: Option text, 1-100 characters
    :type  text: str|unicode
    
    :param voter_count: Number of users that voted for this option
    :type  voter_count: int
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    text: str
    voter_count: int
# end class PollOption

class PollAnswer(Receivable):
    """
    This object represents an answer of a user in a non-anonymous poll.

    https://core.telegram.org/bots/api#pollanswer
    

    Parameters:
    
    :param poll_id: Unique poll identifier
    :type  poll_id: str|unicode
    
    :param user: The user, who changed the answer to the poll
    :type  user: pytgbot.api_types.receivable.peer.User
    
    :param option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    :type  option_ids: list of int
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    poll_id: str
    user: User
    option_ids: List[int]
# end class PollAnswer

class Poll(Media):
    """
    This object contains information about a poll.

    https://core.telegram.org/bots/api#poll
    

    Parameters:
    
    :param id: Unique poll identifier
    :type  id: str|unicode
    
    :param question: Poll question, 1-255 characters
    :type  question: str|unicode
    
    :param options: List of poll options
    :type  options: list of pytgbot.api_types.receivable.media.poll.PollOption
    
    :param total_voter_count: Total number of users that voted in the poll
    :type  total_voter_count: int
    
    :param is_closed: True, if the poll is closed
    :type  is_closed: bool
    
    :param is_anonymous: True, if the poll is anonymous
    :type  is_anonymous: bool
    
    :param type: Poll type, currently can be "regular" or "quiz"
    :type  type: str|unicode
    
    :param allows_multiple_answers: True, if the poll allows multiple answers
    :type  allows_multiple_answers: bool
    

    Optional keyword parameters:
    
    :param correct_option_id: Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :type  correct_option_id: int
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int
# end class Poll
