# -*- coding: utf-8 -*-
from . import updates
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from pytgbot.api_types.receivable import Result

__author__ = 'luckydonald'


class GameHighScore(Result, BaseModel):
    """
    This object represents one row of the high scores table for a game.

    https://core.telegram.org/bots/api#gamehighscore
    

    Parameters:
    
    :param position: Position in high score table for the game
    :type  position: int
    
    :param user: User
    :type  user: pytgbot.api_types.receivable.peer.User
    
    :param score: Score
    :type  score: int
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    position: int
    user: User
    score: int
# end class GameHighScore
