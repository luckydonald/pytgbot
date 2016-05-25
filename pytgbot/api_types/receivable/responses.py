# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type

from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.media import Location
from pytgbot.api_types.receivable.peer import User


class MessageEntity(Result):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    """
    def __init__(self, type, offset, length, url=None, user=None):
        """
        This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

        https://core.telegram.org/bots/api#messageentity


        Parameters:

        :param type: Type of the entity. Can be "mention" (@username), "hashtag", "bot_command", "url", "email",
                     "bold" (bold text), "italic" (italic text), "code" (monowidth string), "pre" (monowidth block),
                     "text_link" (for clickable text URLs), "text_mention" (for users without usernames)
        :type  type: str

        :param offset: Offset in UTF-16 code units to the start of the entity
        :type  offset: int

        :param length: Length of the entity in UTF-16 code units
        :type  length: int


        Optional keyword parameters:

        :keyword url: Optional. For “text_link” only, url that will be opened after user taps on the text
        :type    url: str

        :keyword user: Optional. For “text_mention” only, the mentioned user
        :type    user: User
        """
        super(MessageEntity, self).__init__()
        
        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type
        
        assert(offset is not None)
        assert(isinstance(offset, int))
        self.offset = offset
        
        assert(length is not None)
        assert(isinstance(length, int))
        self.length = length
        
        assert(url is None or isinstance(url, unicode_type))  # unicode on python 2, str on python 3
        self.url = url
        
        assert(user is None or isinstance(user, User))
        self.user = user
    # end def __init__

    def to_array(self):
        array = super(MessageEntity, self).to_array()
        array["type"] = self.type
        array["offset"] = self.offset
        array["length"] = self.length
        if self.url is not None:
            array["url"] = self.url
        if self.user is not None:
            array["user"] = self.user
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        array['user'] = User.from_array(array.get('user'))
        return MessageEntity(**array)
    # end def from_array
# end class MessageEntity


class InlineQuery(Result):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery
    """
    def __init__(self, id, from_peer, query, offset, location=None):
        """
        This object represents an incoming inline query. When the user sends an empty query,
        your bot could return some default or trending results.

        https://core.telegram.org/bots/api#inlinequery


        Parameters:

        :param id: Unique identifier for this query
        :type  id: str

        :param from_peer: Sender
        :type  from_peer: pytgbot.api_types.receivable.responses.peer.User

        :param query: Text of the query (up to 512 characters)
        :type  query: str

        :param offset: Offset of the results to be returned, can be controlled by the bot
        :type  offset: str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that request user location
        :type    location: Location
        """
        super(InlineQuery, self).__init__()
        
        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id
        
        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer
        
        assert(location is None or isinstance(location, Location))
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

    @staticmethod
    def from_array(array):
        array['from_peer'] = User.from_array(array.get('from'))
        array['location'] = Location.from_array(array.get('location'))
        return InlineQuery(**array)
    # end def from_array
# end class InlineQuery
