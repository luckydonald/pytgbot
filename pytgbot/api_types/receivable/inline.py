# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result
from .updates import UpdateType

__author__ = 'luckydonald'


class InlineQuery(Result):
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery


    Parameters:

    :param id: Unique identifier for this query
    :type  id: str|unicode

    :param from_peer: Sender
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param query: Text of the query (up to 256 characters)
    :type  query: str|unicode

    :param offset: Offset of the results to be returned, can be controlled by the bot
    :type  offset: str|unicode


    Optional keyword parameters:

    :param location: Optional. Sender location, only for bots that request user location
    :type  location: pytgbot.api_types.receivable.media.Location

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, from_peer, query, offset, location=None, _raw=None):
        """
        This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

        https://core.telegram.org/bots/api#inlinequery


        Parameters:

        :param id: Unique identifier for this query
        :type  id: str|unicode

        :param from_peer: Sender
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param query: Text of the query (up to 256 characters)
        :type  query: str|unicode

        :param offset: Offset of the results to be returned, can be controlled by the bot
        :type  offset: str|unicode


        Optional keyword parameters:

        :param location: Optional. Sender location, only for bots that request user location
        :type  location: pytgbot.api_types.receivable.media.Location

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(InlineQuery, self).__init__()
        from .media import Location
        from .peer import User

        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(query, unicode_type, parameter_name="query")
        self.query = query
        assert_type_or_raise(offset, unicode_type, parameter_name="offset")
        self.offset = offset
        assert_type_or_raise(location, None, Location, parameter_name="location")
        self.location = location

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQuery to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQuery, self).to_array()

        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['from'] = self.from_peer.to_array()  # type User
        array['query'] = u(self.query)  # py2: type unicode, py3: type str
        array['offset'] = u(self.offset)  # py2: type unicode, py3: type str
        if self.location is not None:
            array['location'] = self.location.to_array()  # type Location
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQuery constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import Location
        from .peer import User

        data = Result.validate_array(array)
        data['id'] = u(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['query'] = u(array.get('query'))
        data['offset'] = u(array.get('offset'))
        data['location'] = Location.from_array(array.get('location')) if array.get('location') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQuery from a given dictionary.

        :return: new InlineQuery instance.
        :rtype: InlineQuery
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQuery.validate_array(array)
        data['_raw'] = array
        return InlineQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequery_instance)`
        """
        return "InlineQuery(id={self.id!r}, from_peer={self.from_peer!r}, query={self.query!r}, offset={self.offset!r}, location={self.location!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequery_instance)`
        """
        if self._raw:
            return "InlineQuery.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQuery(id={self.id!r}, from_peer={self.from_peer!r}, query={self.query!r}, offset={self.offset!r}, location={self.location!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequery_instance`
        """
        return (
            key in ["id", "from_peer", "query", "offset", "location"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQuery


class ChosenInlineResult(UpdateType):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    Note: It is necessary to enable inline feedback via @Botfather in order to receive these objects in updates.

    https://core.telegram.org/bots/api#choseninlineresult


    Parameters:

    :param result_id: The unique identifier for the result that was chosen
    :type  result_id: str|unicode

    :param from_peer: The user that chose the result
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param query: The query that was used to obtain the result
    :type  query: str|unicode


    Optional keyword parameters:

    :param location: Optional. Sender location, only for bots that require user location
    :type  location: pytgbot.api_types.receivable.media.Location

    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
    :type  inline_message_id: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, result_id, from_peer, query, location=None, inline_message_id=None, _raw=None):
        """
        Represents a result of an inline query that was chosen by the user and sent to their chat partner.
        Note: It is necessary to enable inline feedback via @Botfather in order to receive these objects in updates.

        https://core.telegram.org/bots/api#choseninlineresult


        Parameters:

        :param result_id: The unique identifier for the result that was chosen
        :type  result_id: str|unicode

        :param from_peer: The user that chose the result
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param query: The query that was used to obtain the result
        :type  query: str|unicode


        Optional keyword parameters:

        :param location: Optional. Sender location, only for bots that require user location
        :type  location: pytgbot.api_types.receivable.media.Location

        :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        :type  inline_message_id: str|unicode

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChosenInlineResult, self).__init__()
        from .media import Location
        from .peer import User

        assert_type_or_raise(result_id, unicode_type, parameter_name="result_id")
        self.result_id = result_id
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(query, unicode_type, parameter_name="query")
        self.query = query
        assert_type_or_raise(location, None, Location, parameter_name="location")
        self.location = location
        assert_type_or_raise(inline_message_id, None, unicode_type, parameter_name="inline_message_id")
        self.inline_message_id = inline_message_id

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChosenInlineResult to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChosenInlineResult, self).to_array()

        array['result_id'] = u(self.result_id)  # py2: type unicode, py3: type str
        array['from'] = self.from_peer.to_array()  # type User
        array['query'] = u(self.query)  # py2: type unicode, py3: type str
        if self.location is not None:
            array['location'] = self.location.to_array()  # type Location
        # end if
        if self.inline_message_id is not None:
            array['inline_message_id'] = u(self.inline_message_id)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChosenInlineResult constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import Location
        from .peer import User

        data = UpdateType.validate_array(array)
        data['result_id'] = u(array.get('result_id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['query'] = u(array.get('query'))
        data['location'] = Location.from_array(array.get('location')) if array.get('location') is not None else None
        data['inline_message_id'] = u(array.get('inline_message_id')) if array.get('inline_message_id') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChosenInlineResult from a given dictionary.

        :return: new ChosenInlineResult instance.
        :rtype: ChosenInlineResult
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChosenInlineResult.validate_array(array)
        data['_raw'] = array
        return ChosenInlineResult(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(choseninlineresult_instance)`
        """
        return "ChosenInlineResult(result_id={self.result_id!r}, from_peer={self.from_peer!r}, query={self.query!r}, location={self.location!r}, inline_message_id={self.inline_message_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(choseninlineresult_instance)`
        """
        if self._raw:
            return "ChosenInlineResult.from_array({self._raw})".format(self=self)
        # end if
        return "ChosenInlineResult(result_id={self.result_id!r}, from_peer={self.from_peer!r}, query={self.query!r}, location={self.location!r}, inline_message_id={self.inline_message_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in choseninlineresult_instance`
        """
        return (
            key in ["result_id", "from_peer", "query", "location", "inline_message_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChosenInlineResult

