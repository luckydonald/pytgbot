# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type
from luckydonaldUtils.logger import logging

from ..receivable import Receivable

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

class ChosenInlineResult (Receivable):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    https://core.telegram.org/bots/api#choseninlineresult
    """
    def __init__(self, result_id, from_peer, query, location = None, inline_message_id = None):
        """
        Represents a result of an inline query that was chosen by the user and sent to their chat partner.

        https://core.telegram.org/bots/api#choseninlineresult


        Parameters:

        :param result_id: The unique identifier for the result that was chosen
        :type  result_id:  str

        :param from_peer: The user that chose the result
        :type  from_peer:  User

        :param query: The query that was used to obtain the result
        :type  query:  str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that require user location
        :type    location:  Location

        :keyword inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        :type    inline_message_id:  str
        """
        super(ChosenInlineResult, self).__init__(id)

        assert(result_id is not None)
        assert(isinstance(result_id, unicode_type))  # unicode on python 2, str on python 3
        self.result_id = result_id

        self.from_peer = from_peer

        self.location = location

        assert(inline_message_id is None or isinstance(inline_message_id, unicode_type))  # unicode on python 2, str on python 3
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
# end class ChosenInlineResult