# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.encoding import unicode_type

from pytgbot.api_types.receivable import Result

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
        assert(isinstance(first_name, str))
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, str))
        self.last_name = last_name

        assert(username is None or isinstance(username, str))
        self.username = username
    # end def __init__

    def to_array(self):
        """
        Serializes this User to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(User, self).to_array()
        array['id'] = int(self.id)  # type int
        array['first_name'] = str(self.first_name)  # type str
        if self.last_name is not None:
            array['last_name'] = str(self.last_name)  # type str
        if self.username is not None:
            array['username'] = str(self.username)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new User from a given dictionary.

        :return: new User instance.
        :rtype: User
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['id'] = int(array.get('id'))
        data['first_name'] = str(array.get('first_name'))
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        data['username'] = str(array.get('username')) if array.get('username') is not None else None
        return User(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(user_instance)`
        """
        return "User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in user_instance`
        """
        return key in ["id", "first_name", "last_name", "username"]
    # end def __contains__
# end class User


class Chat(Peer):
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat
    """
    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None, all_members_are_administrators=None):
        """
        This object represents a chat.

        https://core.telegram.org/bots/api#chat


        Parameters:

        :param id: Unique identifier for this chat.
                   This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier
        :type  id: int

        :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
        :type  type: str


        Optional keyword parameters:

        :keyword title: Optional. Title, for supergroups, channels and group chats
        :type    title: str

        :keyword username: Optional. Username, for private chats, supergroups and channels if available
        :type    username: str

        :keyword first_name: Optional. First name of the other party in a private chat
        :type    first_name: str

        :keyword last_name: Optional. Last name of the other party in a private chat
        :type    last_name: str
        
        :keyword all_members_are_administrators: Optional. True if a group has ‘All Members Are Admins’ enabled.
        :type    all_members_are_administrators: bool
        """
        super(Chat, self).__init__()
        assert(id is not None)
        assert(isinstance(id, int))
        self.id = id

        assert(type is not None)
        assert(isinstance(type, str))
        self.type = type

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(username is None or isinstance(username, str))
        self.username = username

        assert(first_name is None or isinstance(first_name, str))
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, str))
        self.last_name = last_name
        
        assert(all_members_are_administrators is None or isinstance(all_members_are_administrators, bool))
        self.all_members_are_administrators = all_members_are_administrators
    # end def __init__

    def to_array(self):
        """
        Serializes this Chat to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Chat, self).to_array()
        array['id'] = int(self.id)  # type int
        array['type'] = str(self.type)  # type str
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.username is not None:
            array['username'] = str(self.username)  # type str
        if self.first_name is not None:
            array['first_name'] = str(self.first_name)  # type str
        if self.last_name is not None:
            array['last_name'] = str(self.last_name)  # type str
        if self.all_members_are_administrators is not None:
            array['all_members_are_administrators'] = bool(self.all_members_are_administrators)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Chat from a given dictionary.

        :return: new Chat instance.
        :rtype: Chat
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['id'] = int(array.get('id'))
        data['type'] = str(array.get('type'))
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['username'] = str(array.get('username')) if array.get('username') is not None else None
        data['first_name'] = str(array.get('first_name')) if array.get('first_name') is not None else None
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        data['all_members_are_administrators'] = bool(array.get('all_members_are_administrators')) if array.get('all_members_are_administrators') is not None else None
        return Chat(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chat_instance)`
        """
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, all_members_are_administrators={self.all_members_are_administrators!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in chat_instance`
        """
        return key in ["id", "type", "title", "username", "first_name", "last_name", "all_members_are_administrators"]
    # end def __contains__
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
        :type  user: pytgbot.api_types.receivable.peer.User

        :param status: The member's status in the chat. Can be “creator”, “administrator”, “member”, “left” or “kicked”
        :type  status: str
        """
        super(ChatMember, self).__init__()

        assert(user is not None)
        assert(isinstance(user, User))
        self.user = user

        assert(status is not None)
        assert(isinstance(status, str))
        self.status = status
    # end def __init__

    def to_array(self):
        """
        Serializes this ChatMember to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ChatMember, self).to_array()
        array['user'] = self.user.to_array()  # type User
        array['status'] = str(self.status)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ChatMember from a given dictionary.

        :return: new ChatMember instance.
        :rtype: ChatMember
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['user'] = User.from_array(array.get('user'))
        data['status'] = str(array.get('status'))
        return ChatMember(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmember_instance)`
        """
        return "ChatMember(user={self.user!r}, status={self.status!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in chatmember_instance`
        """
        return key in ["user", "status"]
    # end def __contains__
# end class ChatMember
