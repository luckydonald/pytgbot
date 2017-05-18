# -*- coding: utf-8 -*-
from . import Result



class GameHighScore(Result):
    """
    This object represents one row of the high scores table for a game.

    https://core.telegram.org/bots/api#gamehighscore
    """
    def __init__(self, position, user, score):
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
        """
        super(GameHighScore, self).__init__()
        from pytgbot.api_types.receivable.peer import User
        
        assert(position is not None)
        assert(isinstance(position, int))
        self.position = position
        
        assert(user is not None)
        assert(isinstance(user, User))
        self.user = user
        
        assert(score is not None)
        assert(isinstance(score, int))
        self.score = score
    # end def __init__

    def to_array(self):
        """
        Serializes this GameHighScore to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(GameHighScore, self).to_array()
        array['position'] = int(self.position)  # type int
        array['user'] = self.user.to_array()  # type User
        array['score'] = int(self.score)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new GameHighScore from a given dictionary.

        :return: new GameHighScore instance.
        :rtype: GameHighScore
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        from pytgbot.api_types.receivable.peer import User
        
        data = {}
        data['position'] = int(array.get('position'))
        data['user'] = User.from_array(array.get('user'))
        data['score'] = int(array.get('score'))
        return GameHighScore(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(gamehighscore_instance)`
        """
        return "GameHighScore(position={self.position!r}, user={self.user!r}, score={self.score!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in gamehighscore_instance`
        """
        return key in ["position", "user", "score"]
    # end def __contains__
# end class GameHighScore

