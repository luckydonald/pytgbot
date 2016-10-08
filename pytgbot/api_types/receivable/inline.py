# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type
from luckydonaldUtils.logger import logging

from ..receivable import Result
from ..receivable.updates import UpdateType

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class InlineQuery(Result):
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery
    """
    def __init__(self, id, from_peer, query, offset, location=None):
        """
        This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

        https://core.telegram.org/bots/api#inlinequery


        Parameters:

        :param id: Unique identifier for this query
        :type  id: str

        :param from_peer: Sender
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param query: Text of the query (up to 512 characters)
        :type  query: str

        :param offset: Offset of the results to be returned, can be controlled by the bot
        :type  offset: str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that request user location
        :type    location: pytgbot.api_types.receivable.media.Location
        """
        super(InlineQuery, self).__init__()
        from pytgbot.api_types.receivable.media import Location
        from pytgbot.api_types.receivable.peer import User

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer

        assert(query is not None)
        assert(isinstance(query, str))
        self.query = query

        assert(offset is not None)
        assert(isinstance(offset, str))
        self.offset = offset

        assert(location is None or isinstance(location, Location))
        self.location = location
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQuery to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQuery, self).to_array()
        array['id'] = str(self.id)  # type str
        array['from'] = self.from_peer.to_array()  # type User
        array['query'] = str(self.query)  # type str
        array['offset'] = str(self.offset)  # type str
        if self.location is not None:
            array['location'] = self.location.to_array()  # type Location
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQuery from a given dictionary.

        :return: new InlineQuery instance.
        :rtype: InlineQuery
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.receivable.media import Location
        from pytgbot.api_types.receivable.peer import User

        data = {}

        data['id'] = str(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['query'] = str(array.get('query'))
        data['offset'] = str(array.get('offset'))
        data['location'] = Location.from_array(array.get('location')) if array.get('location') is not None else None
        return InlineQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequery_instance)`
        """
        return "InlineQuery(id={self.id!r}, from_peer={self.from_peer!r}, query={self.query!r}, offset={self.offset!r}, location={self.location!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequery_instance`
        """
        return key in ["id", "from_peer", "query", "offset", "location"]
        # end def __contains__
# end class InlineQuery


class ChosenInlineResult(UpdateType):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    https://core.telegram.org/bots/api#choseninlineresult
    """
    def __init__(self, result_id, from_peer, query, location=None, inline_message_id=None):
        """
        Represents a result of an inline query that was chosen by the user and sent to their chat partner.

        https://core.telegram.org/bots/api#choseninlineresult


        Parameters:

        :param result_id: The unique identifier for the result that was chosen
        :type  result_id: str

        :param from_peer: The user that chose the result
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param query: The query that was used to obtain the result
        :type  query: str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that require user location
        :type    location: pytgbot.api_types.receivable.media.Location

        :keyword inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        :type    inline_message_id: str
        """
        super(ChosenInlineResult, self).__init__()

        from ..receivable.peer import User
        from ..receivable.media import Location

        assert(result_id is not None)
        assert(isinstance(result_id, str))
        self.result_id = result_id

        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer

        assert(query is not None)
        assert(isinstance(query, str))
        self.query = query

        assert(location is None or isinstance(location, Location))
        self.location = location

        assert(inline_message_id is None or isinstance(inline_message_id, str))
        self.inline_message_id = inline_message_id
    # end def __init__

    def to_array(self):
        """
        Serializes this ChosenInlineResult to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ChosenInlineResult, self).to_array()
        array['result_id'] = str(self.result_id)  # type str
        array['from'] = self.from_peer.to_array()  # type User
        array['query'] = str(self.query)  # type str
        if self.location is not None:
            array['location'] = self.location.to_array()  # type Location
        if self.inline_message_id is not None:
            array['inline_message_id'] = str(self.inline_message_id)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ChosenInlineResult from a given dictionary.

        :return: new ChosenInlineResult instance.
        :rtype: ChosenInlineResult
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from ..receivable.peer import User
        from ..receivable.media import Location

        data = {}
        data['result_id'] = str(array.get('result_id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['query'] = str(array.get('query'))
        data['location'] = Location.from_array(array.get('location')) if array.get('location') is not None else None
        data['inline_message_id'] = str(array.get('inline_message_id')) if array.get('inline_message_id') is not None else None
        return ChosenInlineResult(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(choseninlineresult_instance)`
        """
        return "ChosenInlineResult(result_id={self.result_id!r}, from_peer={self.from_peer!r}, query={self.query!r}, location={self.location!r}, inline_message_id={self.inline_message_id!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in choseninlineresult_instance`
        """
        return key in ["result_id", "from_peer", "query", "location", "inline_message_id"]
    # end def __contains__
# end class ChosenInlineResult
