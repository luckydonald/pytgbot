# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.encoding import unicode_type

from pytgbot.api_types.responses import Result

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Peer(Result):
    pass


class User(Peer):
    """
    This object represents a Telegram user or bot.

    https://core.telegram.org/bots/api#user
    """

    def __init__(self, id, first_name, last_name=None, username=None):
        """
        This object represents a Telegram user or bot.

        https://core.telegram.org/bots/api#user


        Parameters:

        :param id: Unique identifier for this user or bot
        :type  id: int

        :param first_name: User‘s or bot’s first name
        :type  first_name: str


        Optional keyword parameters:

        :keyword last_name: Optional. User‘s or bot’s last name
        :type    last_name: str

        :keyword username: Optional. User‘s or bot’s username
        :type    username: str
        """
        super(User, self).__init__()

        assert(id is not None)
        assert(isinstance(id, int))
        self.id = id

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name

        assert(username is None or isinstance(username, unicode_type))  # unicode on python 2, str on python 3
        self.username = username
    # end def __init__

    def to_array(self):
        array = super(User, self).to_array()
        array["id"] = self.id
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        if self.username is not None:
            array["username"] = self.username
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        return User(**array)
        # end def from_array


# end class User


class Chat(Peer):
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat
    """
    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None):
        """
        This object represents a chat.

        https://core.telegram.org/bots/api#chat


        Parameters:

        :param id: Unique identifier for this chat, not exceeding 1e13 by absolute value
        :type  id: int

        :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
        :type  type: str


        Optional keyword parameters:

        :keyword title: Optional. Title, for channels and group chats
        :type    title: str

        :keyword username: Optional. Username, for private chats, supergroups and channels if available
        :type    username: str

        :keyword first_name: Optional. First name of the other party in a private chat
        :type    first_name:  str

        :keyword last_name: Optional. Last name of the other party in a private chat
        :type    last_name:  str
        """
        super(Chat, self).__init__()

        assert(id is not None)
        assert(isinstance(id, int))
        self.id = id

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(username is None or isinstance(username, unicode_type))  # unicode on python 2, str on python 3
        self.username = username

        assert(first_name is None or isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name

    # end def __init__

    def to_array(self):
        array = super(Chat, self).to_array()
        array["id"] = self.id
        array["type"] = self.type
        if self.title is not None:
            array["title"] = self.title
        if self.username is not None:
            array["username"] = self.username
        if self.first_name is not None:
            array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        return Chat(**array)
    # end def from_array
# end class Chat


class ChatMember(Result):
    """
    This object contains information about one member of the chat.

    https://core.telegram.org/bots/api#chatmember
    """

    def __init__(self, user, status):
        """
        This object contains information about one member of the chat.

        https://core.telegram.org/bots/api#chatmember


        Parameters:

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.responses.peer.User

        :param status: The member's status in the chat. Can be “creator”, “administrator”, “member”, “left” or “kicked”
        :type  status: str
        """
        super(ChatMember, self).__init__()

        assert (user is not None)
        assert (isinstance(user, User))
        self.user = user

        assert (status is not None)
        assert (isinstance(status, unicode_type))  # unicode on python 2, str on python 3
        self.status = status

    # end def __init__

    def to_array(self):
        array = super(ChatMember, self).to_array()
        array["user"] = self.user
        array["status"] = self.status
        return array

    # end def to_array

    @staticmethod
    def from_array(array):
        array['user'] = User.from_array(array.get('user'))
        return ChatMember(**array)
        # end def from_array
        # end class ChatMember