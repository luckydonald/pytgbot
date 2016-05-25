# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type
from luckydonaldUtils.logger import logging

from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.peer import User
from ..receivable.media import Location
from ..receivable.updates import UpdateType

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class InlineQuery(Result):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery
    """
    def __init__(self, id, from_peer, query, offset, location = None):
        """
        This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

        https://core.telegram.org/bots/api#inlinequery


        Parameters:

        :param id: Unique identifier for this query
        :type  id:  str

        :param from_peer: Sender
        :type  from_peer:  User

        :param query: Text of the query
        :type  query:  str

        :param offset: Offset of the results to be returned, can be controlled by the bot
        :type  offset:  str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that request user location
        :type    location:  Location
        """
        super(InlineQuery, self).__init__()

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        self.from_peer = from_peer

        self.location = location

        assert(query is not None)
        assert(isinstance(query, unicode_type))  # unicode on python 2, str on python 3
        self.query = query

        assert(offset is not None)
        assert(isinstance(offset, unicode_type))  # unicode on python 2, str on python 3
        self.offset = offset
    # end def __init__

    def to_array(self):
        array = super(InlineQuery, self).to_array()
        array["id"] = self.id
        array["from_peer"] = self.from_peer
        array["query"] = self.query
        array["offset"] = self.offset
        if self.location is not None:
            array["location"] = self.location
        return array
    # end def to_array
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
        :type  from_peer: pytgbot.api_types.receivable.responses.peer.User

        :param query: The query that was used to obtain the result
        :type  query: str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that require user location
        :type    location: Location

        :keyword inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        :type    inline_message_id: str
        """
        super(ChosenInlineResult, self).__init__()

        assert(result_id is not None)
        assert(isinstance(result_id, unicode_type))  # unicode on python 2, str on python 3
        self.result_id = result_id

        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer

        assert(location is None or isinstance(location, Location))
        self.location = location

        assert(inline_message_id is None or isinstance(inline_message_id, unicode_type))  # py2: unicode, py3: str
        self.inline_message_id = inline_message_id

        assert(query is not None)
        assert(isinstance(query, unicode_type))  # unicode on python 2, str on python 3
        self.query = query
    # end def __init__

    def to_array(self):
        array = super(ChosenInlineResult, self).to_array()
        array["result_id"] = self.result_id
        array["from_peer"] = self.from_peer
        array["query"] = self.query
        if self.location is not None:
            array["location"] = self.location
        if self.inline_message_id is not None:
            array["inline_message_id"] = self.inline_message_id
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        if not array:
            return None
        assert (isinstance(array, dict))
        array['from_peer'] = User.from_array(array.get('from'))
        array['location'] = Location.from_array(array.get('location'))
        return ChosenInlineResult(**array)
    # end def from_array
# end class ChosenInlineResult
