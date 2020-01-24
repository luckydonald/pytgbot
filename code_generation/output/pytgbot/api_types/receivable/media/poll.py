# -*- coding: utf-8 -*-
from . import updates
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
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

    def __init__(self, text, voter_count, _raw=None):
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
        super(PollOption, self).__init__()
        assert_type_or_raise(text, unicode_type, parameter_name="text")
        self.text = text
        
        assert_type_or_raise(voter_count, int, parameter_name="voter_count")
        self.voter_count = voter_count

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this PollOption to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PollOption, self).to_array()
        array['text'] = u(self.text)  # py2: type unicode, py3: type str
        array['voter_count'] = int(self.voter_count)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PollOption constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Receivable.validate_array(array)
        data['text'] = u(array.get('text'))
        data['voter_count'] = int(array.get('voter_count'))
        
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PollOption from a given dictionary.

        :return: new PollOption instance.
        :rtype: PollOption
        """
        if not array:  # None or {}
            return None
        # end if

        data = PollOption.validate_array(array)
        data['_raw'] = array
        return PollOption(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(polloption_instance)`
        """
        return "PollOption(text={self.text!r}, voter_count={self.voter_count!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(polloption_instance)`
        """
        if self._raw:
            return "PollOption.from_array({self._raw})".format(self=self)
        # end if
        return "PollOption(text={self.text!r}, voter_count={self.voter_count!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in polloption_instance`
        """
        return (
            key in ["text", "voter_count"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, poll_id, user, option_ids, _raw=None):
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
        super(PollAnswer, self).__init__()
        from pytgbot.api_types.receivable.peer import User
        
        assert_type_or_raise(poll_id, unicode_type, parameter_name="poll_id")
        self.poll_id = poll_id
        
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        
        assert_type_or_raise(option_ids, list, parameter_name="option_ids")
        self.option_ids = option_ids

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this PollAnswer to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PollAnswer, self).to_array()
        array['poll_id'] = u(self.poll_id)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User

        array['option_ids'] = self._as_array(self.option_ids)  # type list of int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PollAnswer constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.receivable.peer import User
        
        data = Receivable.validate_array(array)
        data['poll_id'] = u(array.get('poll_id'))
        data['user'] = User.from_array(array.get('user'))
        data['option_ids'] = PollAnswer._builtin_from_array_list(required_type=int, value=array.get('option_ids'), list_level=1)
        
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PollAnswer from a given dictionary.

        :return: new PollAnswer instance.
        :rtype: PollAnswer
        """
        if not array:  # None or {}
            return None
        # end if

        data = PollAnswer.validate_array(array)
        data['_raw'] = array
        return PollAnswer(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(pollanswer_instance)`
        """
        return "PollAnswer(poll_id={self.poll_id!r}, user={self.user!r}, option_ids={self.option_ids!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(pollanswer_instance)`
        """
        if self._raw:
            return "PollAnswer.from_array({self._raw})".format(self=self)
        # end if
        return "PollAnswer(poll_id={self.poll_id!r}, user={self.user!r}, option_ids={self.option_ids!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in pollanswer_instance`
        """
        return (
            key in ["poll_id", "user", "option_ids"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, id, question, options, total_voter_count, is_closed, is_anonymous, type, allows_multiple_answers, correct_option_id=None, _raw=None):
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
        super(Poll, self).__init__()
        from pytgbot.api_types.receivable.media.poll import PollOption
        
        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        
        assert_type_or_raise(question, unicode_type, parameter_name="question")
        self.question = question
        
        assert_type_or_raise(options, list, parameter_name="options")
        self.options = options
        
        assert_type_or_raise(total_voter_count, int, parameter_name="total_voter_count")
        self.total_voter_count = total_voter_count
        
        assert_type_or_raise(is_closed, bool, parameter_name="is_closed")
        self.is_closed = is_closed
        
        assert_type_or_raise(is_anonymous, bool, parameter_name="is_anonymous")
        self.is_anonymous = is_anonymous
        
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(allows_multiple_answers, bool, parameter_name="allows_multiple_answers")
        self.allows_multiple_answers = allows_multiple_answers
        
        assert_type_or_raise(correct_option_id, None, int, parameter_name="correct_option_id")
        self.correct_option_id = correct_option_id

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this Poll to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(Poll, self).to_array()
        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['question'] = u(self.question)  # py2: type unicode, py3: type str
        array['options'] = self._as_array(self.options)  # type list of PollOption

        array['total_voter_count'] = int(self.total_voter_count)  # type int
        array['is_closed'] = bool(self.is_closed)  # type bool
        array['is_anonymous'] = bool(self.is_anonymous)  # type bool
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['allows_multiple_answers'] = bool(self.allows_multiple_answers)  # type bool
        if self.correct_option_id is not None:
            array['correct_option_id'] = int(self.correct_option_id)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Poll constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.receivable.media.poll import PollOption
        
        data = Media.validate_array(array)
        data['id'] = u(array.get('id'))
        data['question'] = u(array.get('question'))
        data['options'] = PollOption.from_array_list(array.get('options'), list_level=1)
        data['total_voter_count'] = int(array.get('total_voter_count'))
        data['is_closed'] = bool(array.get('is_closed'))
        data['is_anonymous'] = bool(array.get('is_anonymous'))
        data['type'] = u(array.get('type'))
        data['allows_multiple_answers'] = bool(array.get('allows_multiple_answers'))
        data['correct_option_id'] = int(array.get('correct_option_id')) if array.get('correct_option_id') is not None else None
        
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Poll from a given dictionary.

        :return: new Poll instance.
        :rtype: Poll
        """
        if not array:  # None or {}
            return None
        # end if

        data = Poll.validate_array(array)
        data['_raw'] = array
        return Poll(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(poll_instance)`
        """
        return "Poll(id={self.id!r}, question={self.question!r}, options={self.options!r}, total_voter_count={self.total_voter_count!r}, is_closed={self.is_closed!r}, is_anonymous={self.is_anonymous!r}, type={self.type!r}, allows_multiple_answers={self.allows_multiple_answers!r}, correct_option_id={self.correct_option_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(poll_instance)`
        """
        if self._raw:
            return "Poll.from_array({self._raw})".format(self=self)
        # end if
        return "Poll(id={self.id!r}, question={self.question!r}, options={self.options!r}, total_voter_count={self.total_voter_count!r}, is_closed={self.is_closed!r}, is_anonymous={self.is_anonymous!r}, type={self.type!r}, allows_multiple_answers={self.allows_multiple_answers!r}, correct_option_id={self.correct_option_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in poll_instance`
        """
        return (
            key in ["id", "question", "options", "total_voter_count", "is_closed", "is_anonymous", "type", "allows_multiple_answers", "correct_option_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Poll

