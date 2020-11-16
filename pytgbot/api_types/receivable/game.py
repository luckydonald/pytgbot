# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result

__author__ = 'luckydonald'


class GameHighScore(Result):
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

    def __init__(self, position, user, score, _raw=None):
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
        super(GameHighScore, self).__init__()
        from .peer import User

        assert_type_or_raise(position, int, parameter_name="position")
        self.position = position
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(score, int, parameter_name="score")
        self.score = score

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this GameHighScore to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(GameHighScore, self).to_array()

        array['position'] = int(self.position)  # type int
        array['user'] = self.user.to_array()  # type User
        array['score'] = int(self.score)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the GameHighScore constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User

        data = Result.validate_array(array)
        data['position'] = int(array.get('position'))
        data['user'] = User.from_array(array.get('user'))
        data['score'] = int(array.get('score'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new GameHighScore from a given dictionary.

        :return: new GameHighScore instance.
        :rtype: GameHighScore
        """
        if not array:  # None or {}
            return None
        # end if

        data = GameHighScore.validate_array(array)
        data['_raw'] = array
        return GameHighScore(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(gamehighscore_instance)`
        """
        return "GameHighScore(position={self.position!r}, user={self.user!r}, score={self.score!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(gamehighscore_instance)`
        """
        if self._raw:
            return "GameHighScore.from_array({self._raw})".format(self=self)
        # end if
        return "GameHighScore(position={self.position!r}, user={self.user!r}, score={self.score!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in gamehighscore_instance`
        """
        return (
            key in ["position", "user", "score"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class GameHighScore

