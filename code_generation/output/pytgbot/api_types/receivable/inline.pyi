# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.updates import UpdateType

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
    id: str
    from_peer: User
    query: str
    offset: str
    location: Location
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
    result_id: str
    from_peer: User
    query: str
    location: Location
    inline_message_id: str
# end class ChosenInlineResult
