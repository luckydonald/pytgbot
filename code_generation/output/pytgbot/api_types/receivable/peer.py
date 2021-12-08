# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result

__author__ = 'luckydonald'
__all__ = [
    'Peer',
    'User',
    'Chat',
    'ChatInviteLink',
    'ChatMember',
    'ChatMemberOwner',
    'ChatMemberAdministrator',
    'ChatMemberMember',
    'ChatMemberRestricted',
    'ChatMemberLeft',
    'ChatMemberBanned',
    'ChatMemberUpdated',
    'ChatJoinRequest',
    'ChatPermissions',
    'ChatLocation',
]


class Peer(Result):
    """
    parent class for both users and chats.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    pass
# end class Peer


class User(Peer):
    """
    This object represents a Telegram user or bot.

    https://core.telegram.org/bots/api#user


    Parameters:

    :param id: Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type  id: int

    :param is_bot: True, if this user is a bot
    :type  is_bot: bool

    :param first_name: User's or bot's first name
    :type  first_name: str|unicode


    Optional keyword parameters:

    :param last_name: Optional. User's or bot's last name.
    :type  last_name: str|unicode

    :param username: Optional. User's or bot's username.
    :type  username: str|unicode

    :param language_code: Optional. IETF language tag of the user's language.
    :type  language_code: str|unicode

    :param can_join_groups: Optional. True, if the bot can be invited to groups.
                            Returned only in getMe.
    :type  can_join_groups: bool

    :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot.
                                        Returned only in getMe.
    :type  can_read_all_group_messages: bool

    :param supports_inline_queries: Optional. True, if the bot supports inline queries.
                                    Returned only in getMe.
    :type  supports_inline_queries: bool

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, is_bot, first_name, last_name=None, username=None, language_code=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None, _raw=None):
        """
        This object represents a Telegram user or bot.

        https://core.telegram.org/bots/api#user


        Parameters:

        :param id: Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
        :type  id: int

        :param is_bot: True, if this user is a bot
        :type  is_bot: bool

        :param first_name: User's or bot's first name
        :type  first_name: str|unicode


        Optional keyword parameters:

        :param last_name: Optional. User's or bot's last name.
        :type  last_name: str|unicode

        :param username: Optional. User's or bot's username.
        :type  username: str|unicode

        :param language_code: Optional. IETF language tag of the user's language.
        :type  language_code: str|unicode

        :param can_join_groups: Optional. True, if the bot can be invited to groups.
                                Returned only in getMe.
        :type  can_join_groups: bool

        :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot.
                                            Returned only in getMe.
        :type  can_read_all_group_messages: bool

        :param supports_inline_queries: Optional. True, if the bot supports inline queries.
                                        Returned only in getMe.
        :type  supports_inline_queries: bool

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(User, self).__init__()
        assert_type_or_raise(id, int, parameter_name="id")
        self.id = id
        assert_type_or_raise(is_bot, bool, parameter_name="is_bot")
        self.is_bot = is_bot
        assert_type_or_raise(first_name, unicode_type, parameter_name="first_name")
        self.first_name = first_name
        assert_type_or_raise(last_name, None, unicode_type, parameter_name="last_name")
        self.last_name = last_name
        assert_type_or_raise(username, None, unicode_type, parameter_name="username")
        self.username = username
        assert_type_or_raise(language_code, None, unicode_type, parameter_name="language_code")
        self.language_code = language_code
        assert_type_or_raise(can_join_groups, None, bool, parameter_name="can_join_groups")
        self.can_join_groups = can_join_groups
        assert_type_or_raise(can_read_all_group_messages, None, bool, parameter_name="can_read_all_group_messages")
        self.can_read_all_group_messages = can_read_all_group_messages
        assert_type_or_raise(supports_inline_queries, None, bool, parameter_name="supports_inline_queries")
        self.supports_inline_queries = supports_inline_queries

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this User to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(User, self).to_array()

        array['id'] = int(self.id)  # type int
        array['is_bot'] = bool(self.is_bot)  # type bool
        array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        # end if
        if self.username is not None:
            array['username'] = u(self.username)  # py2: type unicode, py3: type str
        # end if
        if self.language_code is not None:
            array['language_code'] = u(self.language_code)  # py2: type unicode, py3: type str
        # end if
        if self.can_join_groups is not None:
            array['can_join_groups'] = bool(self.can_join_groups)  # type bool
        # end if
        if self.can_read_all_group_messages is not None:
            array['can_read_all_group_messages'] = bool(self.can_read_all_group_messages)  # type bool
        # end if
        if self.supports_inline_queries is not None:
            array['supports_inline_queries'] = bool(self.supports_inline_queries)  # type bool
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the User constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Peer.validate_array(array)
        data['id'] = int(array.get('id'))
        data['is_bot'] = bool(array.get('is_bot'))
        data['first_name'] = u(array.get('first_name'))
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['username'] = u(array.get('username')) if array.get('username') is not None else None
        data['language_code'] = u(array.get('language_code')) if array.get('language_code') is not None else None
        data['can_join_groups'] = bool(array.get('can_join_groups')) if array.get('can_join_groups') is not None else None
        data['can_read_all_group_messages'] = bool(array.get('can_read_all_group_messages')) if array.get('can_read_all_group_messages') is not None else None
        data['supports_inline_queries'] = bool(array.get('supports_inline_queries')) if array.get('supports_inline_queries') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new User from a given dictionary.

        :return: new User instance.
        :rtype: User
        """
        if not array:  # None or {}
            return None
        # end if

        data = User.validate_array(array)
        data['_raw'] = array
        return User(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(user_instance)`
        """
        return "User(id={self.id!r}, is_bot={self.is_bot!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, language_code={self.language_code!r}, can_join_groups={self.can_join_groups!r}, can_read_all_group_messages={self.can_read_all_group_messages!r}, supports_inline_queries={self.supports_inline_queries!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(user_instance)`
        """
        if self._raw:
            return "User.from_array({self._raw})".format(self=self)
        # end if
        return "User(id={self.id!r}, is_bot={self.is_bot!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, language_code={self.language_code!r}, can_join_groups={self.can_join_groups!r}, can_read_all_group_messages={self.can_read_all_group_messages!r}, supports_inline_queries={self.supports_inline_queries!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in user_instance`
        """
        return (
            key in ["id", "is_bot", "first_name", "last_name", "username", "language_code", "can_join_groups", "can_read_all_group_messages", "supports_inline_queries"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class User


class Chat(Peer):
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat


    Parameters:

    :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    :type  id: int

    :param type: Type of chat, can be either "private", "group", "supergroup" or "channel"
    :type  type: str|unicode


    Optional keyword parameters:

    :param title: Optional. Title, for supergroups, channels and group chats.
    :type  title: str|unicode

    :param username: Optional. Username, for private chats, supergroups and channels if available.
    :type  username: str|unicode

    :param first_name: Optional. First name of the other party in a private chat.
    :type  first_name: str|unicode

    :param last_name: Optional. Last name of the other party in a private chat.
    :type  last_name: str|unicode

    :param photo: Optional. Chat photo.
                  Returned only in getChat.
    :type  photo: pytgbot.api_types.receivable.media.ChatPhoto

    :param bio: Optional. Bio of the other party in a private chat.
                Returned only in getChat.
    :type  bio: str|unicode

    :param has_private_forwards: Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user.
                                 Returned only in getChat.
    :type  has_private_forwards: bool

    :param description: Optional. Description, for groups, supergroups and channel chats.
                        Returned only in getChat.
    :type  description: str|unicode

    :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats.
                        Returned only in getChat.
    :type  invite_link: str|unicode

    :param pinned_message: Optional. The most recent pinned message (by sending date).
                           Returned only in getChat.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message

    :param permissions: Optional. Default chat member permissions, for groups and supergroups.
                        Returned only in getChat.
    :type  permissions: pytgbot.api_types.receivable.peer.ChatPermissions

    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds.
                            Returned only in getChat.
    :type  slow_mode_delay: int

    :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds.
                                     Returned only in getChat.
    :type  message_auto_delete_time: int

    :param has_protected_content: Optional. True, if messages from the chat can't be forwarded to other chats.
                                  Returned only in getChat.
    :type  has_protected_content: bool

    :param sticker_set_name: Optional. For supergroups, name of group sticker set.
                             Returned only in getChat.
    :type  sticker_set_name: str|unicode

    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set.
                                Returned only in getChat.
    :type  can_set_sticker_set: bool

    :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e.
                           the discussion group identifier for a channel and vice versa; for supergroups and channel chats.
                           This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it.
                           But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
                           Returned only in getChat.
    :type  linked_chat_id: int

    :param location: Optional. For supergroups, the location to which the supergroup is connected.
                     Returned only in getChat.
    :type  location: pytgbot.api_types.receivable.peer.ChatLocation

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None, photo=None, bio=None, has_private_forwards=None, description=None, invite_link=None, pinned_message=None, permissions=None, slow_mode_delay=None, message_auto_delete_time=None, has_protected_content=None, sticker_set_name=None, can_set_sticker_set=None, linked_chat_id=None, location=None, _raw=None):
        """
        This object represents a chat.

        https://core.telegram.org/bots/api#chat


        Parameters:

        :param id: Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        :type  id: int

        :param type: Type of chat, can be either "private", "group", "supergroup" or "channel"
        :type  type: str|unicode


        Optional keyword parameters:

        :param title: Optional. Title, for supergroups, channels and group chats.
        :type  title: str|unicode

        :param username: Optional. Username, for private chats, supergroups and channels if available.
        :type  username: str|unicode

        :param first_name: Optional. First name of the other party in a private chat.
        :type  first_name: str|unicode

        :param last_name: Optional. Last name of the other party in a private chat.
        :type  last_name: str|unicode

        :param photo: Optional. Chat photo.
                      Returned only in getChat.
        :type  photo: pytgbot.api_types.receivable.media.ChatPhoto

        :param bio: Optional. Bio of the other party in a private chat.
                    Returned only in getChat.
        :type  bio: str|unicode

        :param has_private_forwards: Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user.
                                     Returned only in getChat.
        :type  has_private_forwards: bool

        :param description: Optional. Description, for groups, supergroups and channel chats.
                            Returned only in getChat.
        :type  description: str|unicode

        :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats.
                            Returned only in getChat.
        :type  invite_link: str|unicode

        :param pinned_message: Optional. The most recent pinned message (by sending date).
                               Returned only in getChat.
        :type  pinned_message: pytgbot.api_types.receivable.updates.Message

        :param permissions: Optional. Default chat member permissions, for groups and supergroups.
                            Returned only in getChat.
        :type  permissions: pytgbot.api_types.receivable.peer.ChatPermissions

        :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds.
                                Returned only in getChat.
        :type  slow_mode_delay: int

        :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds.
                                         Returned only in getChat.
        :type  message_auto_delete_time: int

        :param has_protected_content: Optional. True, if messages from the chat can't be forwarded to other chats.
                                      Returned only in getChat.
        :type  has_protected_content: bool

        :param sticker_set_name: Optional. For supergroups, name of group sticker set.
                                 Returned only in getChat.
        :type  sticker_set_name: str|unicode

        :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set.
                                    Returned only in getChat.
        :type  can_set_sticker_set: bool

        :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e.
                               the discussion group identifier for a channel and vice versa; for supergroups and channel chats.
                               This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it.
                               But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
                               Returned only in getChat.
        :type  linked_chat_id: int

        :param location: Optional. For supergroups, the location to which the supergroup is connected.
                         Returned only in getChat.
        :type  location: pytgbot.api_types.receivable.peer.ChatLocation

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Chat, self).__init__()
        from .media import ChatPhoto
        from .updates import Message
        assert_type_or_raise(id, int, parameter_name="id")
        self.id = id
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(username, None, unicode_type, parameter_name="username")
        self.username = username
        assert_type_or_raise(first_name, None, unicode_type, parameter_name="first_name")
        self.first_name = first_name
        assert_type_or_raise(last_name, None, unicode_type, parameter_name="last_name")
        self.last_name = last_name
        assert_type_or_raise(photo, None, ChatPhoto, parameter_name="photo")
        self.photo = photo
        assert_type_or_raise(bio, None, unicode_type, parameter_name="bio")
        self.bio = bio
        assert_type_or_raise(has_private_forwards, None, bool, parameter_name="has_private_forwards")
        self.has_private_forwards = has_private_forwards
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(invite_link, None, unicode_type, parameter_name="invite_link")
        self.invite_link = invite_link
        assert_type_or_raise(pinned_message, None, Message, parameter_name="pinned_message")
        self.pinned_message = pinned_message
        assert_type_or_raise(permissions, None, ChatPermissions, parameter_name="permissions")
        self.permissions = permissions
        assert_type_or_raise(slow_mode_delay, None, int, parameter_name="slow_mode_delay")
        self.slow_mode_delay = slow_mode_delay
        assert_type_or_raise(message_auto_delete_time, None, int, parameter_name="message_auto_delete_time")
        self.message_auto_delete_time = message_auto_delete_time
        assert_type_or_raise(has_protected_content, None, bool, parameter_name="has_protected_content")
        self.has_protected_content = has_protected_content
        assert_type_or_raise(sticker_set_name, None, unicode_type, parameter_name="sticker_set_name")
        self.sticker_set_name = sticker_set_name
        assert_type_or_raise(can_set_sticker_set, None, bool, parameter_name="can_set_sticker_set")
        self.can_set_sticker_set = can_set_sticker_set
        assert_type_or_raise(linked_chat_id, None, int, parameter_name="linked_chat_id")
        self.linked_chat_id = linked_chat_id
        assert_type_or_raise(location, None, ChatLocation, parameter_name="location")
        self.location = location

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Chat to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        from .media import ChatPhoto
        from .updates import Message
        array = super(Chat, self).to_array()

        array['id'] = int(self.id)  # type int
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.username is not None:
            array['username'] = u(self.username)  # py2: type unicode, py3: type str
        # end if
        if self.first_name is not None:
            array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        # end if
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        # end if
        if self.photo is not None:
            array['photo'] = self.photo.to_array()  # type ChatPhoto
        # end if
        if self.bio is not None:
            array['bio'] = u(self.bio)  # py2: type unicode, py3: type str
        # end if
        if self.has_private_forwards is not None:
            array['has_private_forwards'] = bool(self.has_private_forwards)  # type bool
        # end if
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.invite_link is not None:
            array['invite_link'] = u(self.invite_link)  # py2: type unicode, py3: type str
        # end if
        if self.pinned_message is not None:
            array['pinned_message'] = self.pinned_message.to_array()  # type Message
        # end if
        if self.permissions is not None:
            array['permissions'] = self.permissions.to_array()  # type ChatPermissions
        # end if
        if self.slow_mode_delay is not None:
            array['slow_mode_delay'] = int(self.slow_mode_delay)  # type int
        # end if
        if self.message_auto_delete_time is not None:
            array['message_auto_delete_time'] = int(self.message_auto_delete_time)  # type int
        # end if
        if self.has_protected_content is not None:
            array['has_protected_content'] = bool(self.has_protected_content)  # type bool
        # end if
        if self.sticker_set_name is not None:
            array['sticker_set_name'] = u(self.sticker_set_name)  # py2: type unicode, py3: type str
        # end if
        if self.can_set_sticker_set is not None:
            array['can_set_sticker_set'] = bool(self.can_set_sticker_set)  # type bool
        # end if
        if self.linked_chat_id is not None:
            array['linked_chat_id'] = int(self.linked_chat_id)  # type int
        # end if
        if self.location is not None:
            array['location'] = self.location.to_array()  # type ChatLocation
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Chat constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import ChatPhoto
        from .updates import Message
        data = Peer.validate_array(array)
        data['id'] = int(array.get('id'))
        data['type'] = u(array.get('type'))
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['username'] = u(array.get('username')) if array.get('username') is not None else None
        data['first_name'] = u(array.get('first_name')) if array.get('first_name') is not None else None
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['photo'] = ChatPhoto.from_array(array.get('photo')) if array.get('photo') is not None else None
        data['bio'] = u(array.get('bio')) if array.get('bio') is not None else None
        data['has_private_forwards'] = True if array.get('has_private_forwards') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['invite_link'] = u(array.get('invite_link')) if array.get('invite_link') is not None else None
        data['pinned_message'] = Message.from_array(array.get('pinned_message')) if array.get('pinned_message') is not None else None
        data['permissions'] = ChatPermissions.from_array(array.get('permissions')) if array.get('permissions') is not None else None
        data['slow_mode_delay'] = int(array.get('slow_mode_delay')) if array.get('slow_mode_delay') is not None else None
        data['message_auto_delete_time'] = int(array.get('message_auto_delete_time')) if array.get('message_auto_delete_time') is not None else None
        data['has_protected_content'] = True if array.get('has_protected_content') is not None else None
        data['sticker_set_name'] = u(array.get('sticker_set_name')) if array.get('sticker_set_name') is not None else None
        data['can_set_sticker_set'] = bool(array.get('can_set_sticker_set')) if array.get('can_set_sticker_set') is not None else None
        data['linked_chat_id'] = int(array.get('linked_chat_id')) if array.get('linked_chat_id') is not None else None
        data['location'] = ChatLocation.from_array(array.get('location')) if array.get('location') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Chat from a given dictionary.

        :return: new Chat instance.
        :rtype: Chat
        """
        if not array:  # None or {}
            return None
        # end if

        data = Chat.validate_array(array)
        data['_raw'] = array
        return Chat(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chat_instance)`
        """
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, photo={self.photo!r}, bio={self.bio!r}, has_private_forwards={self.has_private_forwards!r}, description={self.description!r}, invite_link={self.invite_link!r}, pinned_message={self.pinned_message!r}, permissions={self.permissions!r}, slow_mode_delay={self.slow_mode_delay!r}, message_auto_delete_time={self.message_auto_delete_time!r}, has_protected_content={self.has_protected_content!r}, sticker_set_name={self.sticker_set_name!r}, can_set_sticker_set={self.can_set_sticker_set!r}, linked_chat_id={self.linked_chat_id!r}, location={self.location!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chat_instance)`
        """
        if self._raw:
            return "Chat.from_array({self._raw})".format(self=self)
        # end if
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, photo={self.photo!r}, bio={self.bio!r}, has_private_forwards={self.has_private_forwards!r}, description={self.description!r}, invite_link={self.invite_link!r}, pinned_message={self.pinned_message!r}, permissions={self.permissions!r}, slow_mode_delay={self.slow_mode_delay!r}, message_auto_delete_time={self.message_auto_delete_time!r}, has_protected_content={self.has_protected_content!r}, sticker_set_name={self.sticker_set_name!r}, can_set_sticker_set={self.can_set_sticker_set!r}, linked_chat_id={self.linked_chat_id!r}, location={self.location!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chat_instance`
        """
        return (
            key in ["id", "type", "title", "username", "first_name", "last_name", "photo", "bio", "has_private_forwards", "description", "invite_link", "pinned_message", "permissions", "slow_mode_delay", "message_auto_delete_time", "has_protected_content", "sticker_set_name", "can_set_sticker_set", "linked_chat_id", "location"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Chat


class ChatInviteLink(Result):
    """
    Represents an invite link for a chat.

    https://core.telegram.org/bots/api#chatinvitelink


    Parameters:

    :param invite_link: The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "…".
    :type  invite_link: str|unicode

    :param creator: Creator of the link
    :type  creator: pytgbot.api_types.receivable.peer.User

    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators
    :type  creates_join_request: bool

    :param is_primary: True, if the link is primary
    :type  is_primary: bool

    :param is_revoked: True, if the link is revoked
    :type  is_revoked: bool


    Optional keyword parameters:

    :param name: Optional. Invite link name.
    :type  name: str|unicode

    :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been expired.
    :type  expire_date: int

    :param member_limit: Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.
    :type  member_limit: int

    :param pending_join_request_count: Optional. Number of pending join requests created using this link.
    :type  pending_join_request_count: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, invite_link, creator, creates_join_request, is_primary, is_revoked, name=None, expire_date=None, member_limit=None, pending_join_request_count=None, _raw=None):
        """
        Represents an invite link for a chat.

        https://core.telegram.org/bots/api#chatinvitelink


        Parameters:

        :param invite_link: The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with "…".
        :type  invite_link: str|unicode

        :param creator: Creator of the link
        :type  creator: pytgbot.api_types.receivable.peer.User

        :param creates_join_request: True, if users joining the chat via the link need to be approved by chat administrators
        :type  creates_join_request: bool

        :param is_primary: True, if the link is primary
        :type  is_primary: bool

        :param is_revoked: True, if the link is revoked
        :type  is_revoked: bool


        Optional keyword parameters:

        :param name: Optional. Invite link name.
        :type  name: str|unicode

        :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been expired.
        :type  expire_date: int

        :param member_limit: Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999.
        :type  member_limit: int

        :param pending_join_request_count: Optional. Number of pending join requests created using this link.
        :type  pending_join_request_count: int

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatInviteLink, self).__init__()
        assert_type_or_raise(invite_link, unicode_type, parameter_name="invite_link")
        self.invite_link = invite_link
        assert_type_or_raise(creator, User, parameter_name="creator")
        self.creator = creator
        assert_type_or_raise(creates_join_request, bool, parameter_name="creates_join_request")
        self.creates_join_request = creates_join_request
        assert_type_or_raise(is_primary, bool, parameter_name="is_primary")
        self.is_primary = is_primary
        assert_type_or_raise(is_revoked, bool, parameter_name="is_revoked")
        self.is_revoked = is_revoked
        assert_type_or_raise(name, None, unicode_type, parameter_name="name")
        self.name = name
        assert_type_or_raise(expire_date, None, int, parameter_name="expire_date")
        self.expire_date = expire_date
        assert_type_or_raise(member_limit, None, int, parameter_name="member_limit")
        self.member_limit = member_limit
        assert_type_or_raise(pending_join_request_count, None, int, parameter_name="pending_join_request_count")
        self.pending_join_request_count = pending_join_request_count

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatInviteLink to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatInviteLink, self).to_array()

        array['invite_link'] = u(self.invite_link)  # py2: type unicode, py3: type str
        array['creator'] = self.creator.to_array()  # type User
        array['creates_join_request'] = bool(self.creates_join_request)  # type bool
        array['is_primary'] = bool(self.is_primary)  # type bool
        array['is_revoked'] = bool(self.is_revoked)  # type bool
        if self.name is not None:
            array['name'] = u(self.name)  # py2: type unicode, py3: type str
        # end if
        if self.expire_date is not None:
            array['expire_date'] = int(self.expire_date)  # type int
        # end if
        if self.member_limit is not None:
            array['member_limit'] = int(self.member_limit)  # type int
        # end if
        if self.pending_join_request_count is not None:
            array['pending_join_request_count'] = int(self.pending_join_request_count)  # type int
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatInviteLink constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['invite_link'] = u(array.get('invite_link'))
        data['creator'] = User.from_array(array.get('creator'))
        data['creates_join_request'] = bool(array.get('creates_join_request'))
        data['is_primary'] = bool(array.get('is_primary'))
        data['is_revoked'] = bool(array.get('is_revoked'))
        data['name'] = u(array.get('name')) if array.get('name') is not None else None
        data['expire_date'] = int(array.get('expire_date')) if array.get('expire_date') is not None else None
        data['member_limit'] = int(array.get('member_limit')) if array.get('member_limit') is not None else None
        data['pending_join_request_count'] = int(array.get('pending_join_request_count')) if array.get('pending_join_request_count') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatInviteLink from a given dictionary.

        :return: new ChatInviteLink instance.
        :rtype: ChatInviteLink
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatInviteLink.validate_array(array)
        data['_raw'] = array
        return ChatInviteLink(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatinvitelink_instance)`
        """
        return "ChatInviteLink(invite_link={self.invite_link!r}, creator={self.creator!r}, creates_join_request={self.creates_join_request!r}, is_primary={self.is_primary!r}, is_revoked={self.is_revoked!r}, name={self.name!r}, expire_date={self.expire_date!r}, member_limit={self.member_limit!r}, pending_join_request_count={self.pending_join_request_count!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatinvitelink_instance)`
        """
        if self._raw:
            return "ChatInviteLink.from_array({self._raw})".format(self=self)
        # end if
        return "ChatInviteLink(invite_link={self.invite_link!r}, creator={self.creator!r}, creates_join_request={self.creates_join_request!r}, is_primary={self.is_primary!r}, is_revoked={self.is_revoked!r}, name={self.name!r}, expire_date={self.expire_date!r}, member_limit={self.member_limit!r}, pending_join_request_count={self.pending_join_request_count!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatinvitelink_instance`
        """
        return (
            key in ["invite_link", "creator", "creates_join_request", "is_primary", "is_revoked", "name", "expire_date", "member_limit", "pending_join_request_count"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatInviteLink


class ChatMember(Result):
    """
    This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:

    https://core.telegram.org/bots/api#chatmember

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, _raw=None):
        """
        This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:

        https://core.telegram.org/bots/api#chatmember

        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMember, self).__init__()

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMember to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMember, self).to_array()

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMember constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMember from a given dictionary.

        :return: new ChatMember instance.
        :rtype: ChatMember
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMember.validate_array(array)
        data['_raw'] = array
        return ChatMember(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmember_instance)`
        """
        return "ChatMember()".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmember_instance)`
        """
        if self._raw:
            return "ChatMember.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMember()".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmember_instance`
        """
        return (
            key in []
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMember


class ChatMemberOwner(ChatMember):
    """
    Represents a chat member that owns the chat and has all administrator privileges.

    https://core.telegram.org/bots/api#chatmemberowner


    Parameters:

    :param status: The member's status in the chat, always "creator"
    :type  status: str|unicode

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type  is_anonymous: bool


    Optional keyword parameters:

    :param custom_title: Optional. Custom title for this user.
    :type  custom_title: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, status, user, is_anonymous, custom_title=None, _raw=None):
        """
        Represents a chat member that owns the chat and has all administrator privileges.

        https://core.telegram.org/bots/api#chatmemberowner


        Parameters:

        :param status: The member's status in the chat, always "creator"
        :type  status: str|unicode

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User

        :param is_anonymous: True, if the user's presence in the chat is hidden
        :type  is_anonymous: bool


        Optional keyword parameters:

        :param custom_title: Optional. Custom title for this user.
        :type  custom_title: str|unicode

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberOwner, self).__init__()
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(is_anonymous, bool, parameter_name="is_anonymous")
        self.is_anonymous = is_anonymous
        assert_type_or_raise(custom_title, None, unicode_type, parameter_name="custom_title")
        self.custom_title = custom_title

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberOwner to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberOwner, self).to_array()

        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        array['is_anonymous'] = bool(self.is_anonymous)  # type bool
        if self.custom_title is not None:
            array['custom_title'] = u(self.custom_title)  # py2: type unicode, py3: type str
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberOwner constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ChatMember.validate_array(array)
        data['status'] = u(array.get('status'))
        data['user'] = User.from_array(array.get('user'))
        data['is_anonymous'] = bool(array.get('is_anonymous'))
        data['custom_title'] = u(array.get('custom_title')) if array.get('custom_title') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberOwner from a given dictionary.

        :return: new ChatMemberOwner instance.
        :rtype: ChatMemberOwner
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberOwner.validate_array(array)
        data['_raw'] = array
        return ChatMemberOwner(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmemberowner_instance)`
        """
        return "ChatMemberOwner(status={self.status!r}, user={self.user!r}, is_anonymous={self.is_anonymous!r}, custom_title={self.custom_title!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmemberowner_instance)`
        """
        if self._raw:
            return "ChatMemberOwner.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberOwner(status={self.status!r}, user={self.user!r}, is_anonymous={self.is_anonymous!r}, custom_title={self.custom_title!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmemberowner_instance`
        """
        return (
            key in ["status", "user", "is_anonymous", "custom_title"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberOwner


class ChatMemberAdministrator(ChatMember):
    """
    Represents a chat member that has some additional privileges.

    https://core.telegram.org/bots/api#chatmemberadministrator


    Parameters:

    :param status: The member's status in the chat, always "administrator"
    :type  status: str|unicode

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User

    :param can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
    :type  can_be_edited: bool

    :param is_anonymous: True, if the user's presence in the chat is hidden
    :type  is_anonymous: bool

    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    :type  can_manage_chat: bool

    :param can_delete_messages: True, if the administrator can delete messages of other users
    :type  can_delete_messages: bool

    :param can_manage_voice_chats: True, if the administrator can manage voice chats
    :type  can_manage_voice_chats: bool

    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :type  can_restrict_members: bool

    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    :type  can_promote_members: bool

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type  can_change_info: bool

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type  can_invite_users: bool


    Optional keyword parameters:

    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only.
    :type  can_post_messages: bool

    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin messages; channels only.
    :type  can_edit_messages: bool

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only.
    :type  can_pin_messages: bool

    :param custom_title: Optional. Custom title for this user.
    :type  custom_title: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, status, user, can_be_edited, is_anonymous, can_manage_chat, can_delete_messages, can_manage_voice_chats, can_restrict_members, can_promote_members, can_change_info, can_invite_users, can_post_messages=None, can_edit_messages=None, can_pin_messages=None, custom_title=None, _raw=None):
        """
        Represents a chat member that has some additional privileges.

        https://core.telegram.org/bots/api#chatmemberadministrator


        Parameters:

        :param status: The member's status in the chat, always "administrator"
        :type  status: str|unicode

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User

        :param can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
        :type  can_be_edited: bool

        :param is_anonymous: True, if the user's presence in the chat is hidden
        :type  is_anonymous: bool

        :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
        :type  can_manage_chat: bool

        :param can_delete_messages: True, if the administrator can delete messages of other users
        :type  can_delete_messages: bool

        :param can_manage_voice_chats: True, if the administrator can manage voice chats
        :type  can_manage_voice_chats: bool

        :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
        :type  can_restrict_members: bool

        :param can_promote_members: True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
        :type  can_promote_members: bool

        :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
        :type  can_change_info: bool

        :param can_invite_users: True, if the user is allowed to invite new users to the chat
        :type  can_invite_users: bool


        Optional keyword parameters:

        :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only.
        :type  can_post_messages: bool

        :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin messages; channels only.
        :type  can_edit_messages: bool

        :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only.
        :type  can_pin_messages: bool

        :param custom_title: Optional. Custom title for this user.
        :type  custom_title: str|unicode

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberAdministrator, self).__init__()
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(can_be_edited, bool, parameter_name="can_be_edited")
        self.can_be_edited = can_be_edited
        assert_type_or_raise(is_anonymous, bool, parameter_name="is_anonymous")
        self.is_anonymous = is_anonymous
        assert_type_or_raise(can_manage_chat, bool, parameter_name="can_manage_chat")
        self.can_manage_chat = can_manage_chat
        assert_type_or_raise(can_delete_messages, bool, parameter_name="can_delete_messages")
        self.can_delete_messages = can_delete_messages
        assert_type_or_raise(can_manage_voice_chats, bool, parameter_name="can_manage_voice_chats")
        self.can_manage_voice_chats = can_manage_voice_chats
        assert_type_or_raise(can_restrict_members, bool, parameter_name="can_restrict_members")
        self.can_restrict_members = can_restrict_members
        assert_type_or_raise(can_promote_members, bool, parameter_name="can_promote_members")
        self.can_promote_members = can_promote_members
        assert_type_or_raise(can_change_info, bool, parameter_name="can_change_info")
        self.can_change_info = can_change_info
        assert_type_or_raise(can_invite_users, bool, parameter_name="can_invite_users")
        self.can_invite_users = can_invite_users
        assert_type_or_raise(can_post_messages, None, bool, parameter_name="can_post_messages")
        self.can_post_messages = can_post_messages
        assert_type_or_raise(can_edit_messages, None, bool, parameter_name="can_edit_messages")
        self.can_edit_messages = can_edit_messages
        assert_type_or_raise(can_pin_messages, None, bool, parameter_name="can_pin_messages")
        self.can_pin_messages = can_pin_messages
        assert_type_or_raise(custom_title, None, unicode_type, parameter_name="custom_title")
        self.custom_title = custom_title

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberAdministrator to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberAdministrator, self).to_array()

        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        array['can_be_edited'] = bool(self.can_be_edited)  # type bool
        array['is_anonymous'] = bool(self.is_anonymous)  # type bool
        array['can_manage_chat'] = bool(self.can_manage_chat)  # type bool
        array['can_delete_messages'] = bool(self.can_delete_messages)  # type bool
        array['can_manage_voice_chats'] = bool(self.can_manage_voice_chats)  # type bool
        array['can_restrict_members'] = bool(self.can_restrict_members)  # type bool
        array['can_promote_members'] = bool(self.can_promote_members)  # type bool
        array['can_change_info'] = bool(self.can_change_info)  # type bool
        array['can_invite_users'] = bool(self.can_invite_users)  # type bool
        if self.can_post_messages is not None:
            array['can_post_messages'] = bool(self.can_post_messages)  # type bool
        # end if
        if self.can_edit_messages is not None:
            array['can_edit_messages'] = bool(self.can_edit_messages)  # type bool
        # end if
        if self.can_pin_messages is not None:
            array['can_pin_messages'] = bool(self.can_pin_messages)  # type bool
        # end if
        if self.custom_title is not None:
            array['custom_title'] = u(self.custom_title)  # py2: type unicode, py3: type str
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberAdministrator constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ChatMember.validate_array(array)
        data['status'] = u(array.get('status'))
        data['user'] = User.from_array(array.get('user'))
        data['can_be_edited'] = bool(array.get('can_be_edited'))
        data['is_anonymous'] = bool(array.get('is_anonymous'))
        data['can_manage_chat'] = bool(array.get('can_manage_chat'))
        data['can_delete_messages'] = bool(array.get('can_delete_messages'))
        data['can_manage_voice_chats'] = bool(array.get('can_manage_voice_chats'))
        data['can_restrict_members'] = bool(array.get('can_restrict_members'))
        data['can_promote_members'] = bool(array.get('can_promote_members'))
        data['can_change_info'] = bool(array.get('can_change_info'))
        data['can_invite_users'] = bool(array.get('can_invite_users'))
        data['can_post_messages'] = bool(array.get('can_post_messages')) if array.get('can_post_messages') is not None else None
        data['can_edit_messages'] = bool(array.get('can_edit_messages')) if array.get('can_edit_messages') is not None else None
        data['can_pin_messages'] = bool(array.get('can_pin_messages')) if array.get('can_pin_messages') is not None else None
        data['custom_title'] = u(array.get('custom_title')) if array.get('custom_title') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberAdministrator from a given dictionary.

        :return: new ChatMemberAdministrator instance.
        :rtype: ChatMemberAdministrator
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberAdministrator.validate_array(array)
        data['_raw'] = array
        return ChatMemberAdministrator(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmemberadministrator_instance)`
        """
        return "ChatMemberAdministrator(status={self.status!r}, user={self.user!r}, can_be_edited={self.can_be_edited!r}, is_anonymous={self.is_anonymous!r}, can_manage_chat={self.can_manage_chat!r}, can_delete_messages={self.can_delete_messages!r}, can_manage_voice_chats={self.can_manage_voice_chats!r}, can_restrict_members={self.can_restrict_members!r}, can_promote_members={self.can_promote_members!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_post_messages={self.can_post_messages!r}, can_edit_messages={self.can_edit_messages!r}, can_pin_messages={self.can_pin_messages!r}, custom_title={self.custom_title!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmemberadministrator_instance)`
        """
        if self._raw:
            return "ChatMemberAdministrator.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberAdministrator(status={self.status!r}, user={self.user!r}, can_be_edited={self.can_be_edited!r}, is_anonymous={self.is_anonymous!r}, can_manage_chat={self.can_manage_chat!r}, can_delete_messages={self.can_delete_messages!r}, can_manage_voice_chats={self.can_manage_voice_chats!r}, can_restrict_members={self.can_restrict_members!r}, can_promote_members={self.can_promote_members!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_post_messages={self.can_post_messages!r}, can_edit_messages={self.can_edit_messages!r}, can_pin_messages={self.can_pin_messages!r}, custom_title={self.custom_title!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmemberadministrator_instance`
        """
        return (
            key in ["status", "user", "can_be_edited", "is_anonymous", "can_manage_chat", "can_delete_messages", "can_manage_voice_chats", "can_restrict_members", "can_promote_members", "can_change_info", "can_invite_users", "can_post_messages", "can_edit_messages", "can_pin_messages", "custom_title"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberAdministrator


class ChatMemberMember(ChatMember):
    """
    Represents a chat member that has no additional privileges or restrictions.

    https://core.telegram.org/bots/api#chatmembermember


    Parameters:

    :param status: The member's status in the chat, always "member"
    :type  status: str|unicode

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, status, user, _raw=None):
        """
        Represents a chat member that has no additional privileges or restrictions.

        https://core.telegram.org/bots/api#chatmembermember


        Parameters:

        :param status: The member's status in the chat, always "member"
        :type  status: str|unicode

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberMember, self).__init__()
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberMember to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberMember, self).to_array()

        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberMember constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ChatMember.validate_array(array)
        data['status'] = u(array.get('status'))
        data['user'] = User.from_array(array.get('user'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberMember from a given dictionary.

        :return: new ChatMemberMember instance.
        :rtype: ChatMemberMember
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberMember.validate_array(array)
        data['_raw'] = array
        return ChatMemberMember(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmembermember_instance)`
        """
        return "ChatMemberMember(status={self.status!r}, user={self.user!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmembermember_instance)`
        """
        if self._raw:
            return "ChatMemberMember.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberMember(status={self.status!r}, user={self.user!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmembermember_instance`
        """
        return (
            key in ["status", "user"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberMember


class ChatMemberRestricted(ChatMember):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups only.

    https://core.telegram.org/bots/api#chatmemberrestricted


    Parameters:

    :param status: The member's status in the chat, always "restricted"
    :type  status: str|unicode

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User

    :param is_member: True, if the user is a member of the chat at the moment of the request
    :type  is_member: bool

    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :type  can_change_info: bool

    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :type  can_invite_users: bool

    :param can_pin_messages: True, if the user is allowed to pin messages
    :type  can_pin_messages: bool

    :param can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    :type  can_send_messages: bool

    :param can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    :type  can_send_media_messages: bool

    :param can_send_polls: True, if the user is allowed to send polls
    :type  can_send_polls: bool

    :param can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots
    :type  can_send_other_messages: bool

    :param can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
    :type  can_add_web_page_previews: bool

    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
    :type  until_date: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, status, user, is_member, can_change_info, can_invite_users, can_pin_messages, can_send_messages, can_send_media_messages, can_send_polls, can_send_other_messages, can_add_web_page_previews, until_date, _raw=None):
        """
        Represents a chat member that is under certain restrictions in the chat. Supergroups only.

        https://core.telegram.org/bots/api#chatmemberrestricted


        Parameters:

        :param status: The member's status in the chat, always "restricted"
        :type  status: str|unicode

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User

        :param is_member: True, if the user is a member of the chat at the moment of the request
        :type  is_member: bool

        :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
        :type  can_change_info: bool

        :param can_invite_users: True, if the user is allowed to invite new users to the chat
        :type  can_invite_users: bool

        :param can_pin_messages: True, if the user is allowed to pin messages
        :type  can_pin_messages: bool

        :param can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
        :type  can_send_messages: bool

        :param can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
        :type  can_send_media_messages: bool

        :param can_send_polls: True, if the user is allowed to send polls
        :type  can_send_polls: bool

        :param can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots
        :type  can_send_other_messages: bool

        :param can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
        :type  can_add_web_page_previews: bool

        :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
        :type  until_date: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberRestricted, self).__init__()
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(is_member, bool, parameter_name="is_member")
        self.is_member = is_member
        assert_type_or_raise(can_change_info, bool, parameter_name="can_change_info")
        self.can_change_info = can_change_info
        assert_type_or_raise(can_invite_users, bool, parameter_name="can_invite_users")
        self.can_invite_users = can_invite_users
        assert_type_or_raise(can_pin_messages, bool, parameter_name="can_pin_messages")
        self.can_pin_messages = can_pin_messages
        assert_type_or_raise(can_send_messages, bool, parameter_name="can_send_messages")
        self.can_send_messages = can_send_messages
        assert_type_or_raise(can_send_media_messages, bool, parameter_name="can_send_media_messages")
        self.can_send_media_messages = can_send_media_messages
        assert_type_or_raise(can_send_polls, bool, parameter_name="can_send_polls")
        self.can_send_polls = can_send_polls
        assert_type_or_raise(can_send_other_messages, bool, parameter_name="can_send_other_messages")
        self.can_send_other_messages = can_send_other_messages
        assert_type_or_raise(can_add_web_page_previews, bool, parameter_name="can_add_web_page_previews")
        self.can_add_web_page_previews = can_add_web_page_previews
        assert_type_or_raise(until_date, int, parameter_name="until_date")
        self.until_date = until_date

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberRestricted to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberRestricted, self).to_array()

        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        array['is_member'] = bool(self.is_member)  # type bool
        array['can_change_info'] = bool(self.can_change_info)  # type bool
        array['can_invite_users'] = bool(self.can_invite_users)  # type bool
        array['can_pin_messages'] = bool(self.can_pin_messages)  # type bool
        array['can_send_messages'] = bool(self.can_send_messages)  # type bool
        array['can_send_media_messages'] = bool(self.can_send_media_messages)  # type bool
        array['can_send_polls'] = bool(self.can_send_polls)  # type bool
        array['can_send_other_messages'] = bool(self.can_send_other_messages)  # type bool
        array['can_add_web_page_previews'] = bool(self.can_add_web_page_previews)  # type bool
        array['until_date'] = int(self.until_date)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberRestricted constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ChatMember.validate_array(array)
        data['status'] = u(array.get('status'))
        data['user'] = User.from_array(array.get('user'))
        data['is_member'] = bool(array.get('is_member'))
        data['can_change_info'] = bool(array.get('can_change_info'))
        data['can_invite_users'] = bool(array.get('can_invite_users'))
        data['can_pin_messages'] = bool(array.get('can_pin_messages'))
        data['can_send_messages'] = bool(array.get('can_send_messages'))
        data['can_send_media_messages'] = bool(array.get('can_send_media_messages'))
        data['can_send_polls'] = bool(array.get('can_send_polls'))
        data['can_send_other_messages'] = bool(array.get('can_send_other_messages'))
        data['can_add_web_page_previews'] = bool(array.get('can_add_web_page_previews'))
        data['until_date'] = int(array.get('until_date'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberRestricted from a given dictionary.

        :return: new ChatMemberRestricted instance.
        :rtype: ChatMemberRestricted
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberRestricted.validate_array(array)
        data['_raw'] = array
        return ChatMemberRestricted(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmemberrestricted_instance)`
        """
        return "ChatMemberRestricted(status={self.status!r}, user={self.user!r}, is_member={self.is_member!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_pin_messages={self.can_pin_messages!r}, can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_polls={self.can_send_polls!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r}, until_date={self.until_date!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmemberrestricted_instance)`
        """
        if self._raw:
            return "ChatMemberRestricted.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberRestricted(status={self.status!r}, user={self.user!r}, is_member={self.is_member!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_pin_messages={self.can_pin_messages!r}, can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_polls={self.can_send_polls!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r}, until_date={self.until_date!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmemberrestricted_instance`
        """
        return (
            key in ["status", "user", "is_member", "can_change_info", "can_invite_users", "can_pin_messages", "can_send_messages", "can_send_media_messages", "can_send_polls", "can_send_other_messages", "can_add_web_page_previews", "until_date"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberRestricted


class ChatMemberLeft(ChatMember):
    """
    Represents a chat member that isn't currently a member of the chat, but may join it themselves.

    https://core.telegram.org/bots/api#chatmemberleft


    Parameters:

    :param status: The member's status in the chat, always "left"
    :type  status: str|unicode

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, status, user, _raw=None):
        """
        Represents a chat member that isn't currently a member of the chat, but may join it themselves.

        https://core.telegram.org/bots/api#chatmemberleft


        Parameters:

        :param status: The member's status in the chat, always "left"
        :type  status: str|unicode

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberLeft, self).__init__()
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberLeft to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberLeft, self).to_array()

        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberLeft constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ChatMember.validate_array(array)
        data['status'] = u(array.get('status'))
        data['user'] = User.from_array(array.get('user'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberLeft from a given dictionary.

        :return: new ChatMemberLeft instance.
        :rtype: ChatMemberLeft
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberLeft.validate_array(array)
        data['_raw'] = array
        return ChatMemberLeft(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmemberleft_instance)`
        """
        return "ChatMemberLeft(status={self.status!r}, user={self.user!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmemberleft_instance)`
        """
        if self._raw:
            return "ChatMemberLeft.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberLeft(status={self.status!r}, user={self.user!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmemberleft_instance`
        """
        return (
            key in ["status", "user"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberLeft


class ChatMemberBanned(ChatMember):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

    https://core.telegram.org/bots/api#chatmemberbanned


    Parameters:

    :param status: The member's status in the chat, always "kicked"
    :type  status: str|unicode

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User

    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
    :type  until_date: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, status, user, until_date, _raw=None):
        """
        Represents a chat member that was banned in the chat and can't return to the chat or view chat messages.

        https://core.telegram.org/bots/api#chatmemberbanned


        Parameters:

        :param status: The member's status in the chat, always "kicked"
        :type  status: str|unicode

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User

        :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
        :type  until_date: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberBanned, self).__init__()
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(until_date, int, parameter_name="until_date")
        self.until_date = until_date

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberBanned to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberBanned, self).to_array()

        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        array['until_date'] = int(self.until_date)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberBanned constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ChatMember.validate_array(array)
        data['status'] = u(array.get('status'))
        data['user'] = User.from_array(array.get('user'))
        data['until_date'] = int(array.get('until_date'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberBanned from a given dictionary.

        :return: new ChatMemberBanned instance.
        :rtype: ChatMemberBanned
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberBanned.validate_array(array)
        data['_raw'] = array
        return ChatMemberBanned(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmemberbanned_instance)`
        """
        return "ChatMemberBanned(status={self.status!r}, user={self.user!r}, until_date={self.until_date!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmemberbanned_instance)`
        """
        if self._raw:
            return "ChatMemberBanned.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberBanned(status={self.status!r}, user={self.user!r}, until_date={self.until_date!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmemberbanned_instance`
        """
        return (
            key in ["status", "user", "until_date"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberBanned


class ChatMemberUpdated(Result):
    """
    This object represents changes in the status of a chat member.

    https://core.telegram.org/bots/api#chatmemberupdated


    Parameters:

    :param chat: Chat the user belongs to
    :type  chat: pytgbot.api_types.receivable.peer.Chat

    :param from_peer: Performer of the action, which resulted in the change
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param date: Date the change was done in Unix time
    :type  date: int

    :param old_chat_member: Previous information about the chat member
    :type  old_chat_member: pytgbot.api_types.receivable.peer.ChatMember

    :param new_chat_member: New information about the chat member
    :type  new_chat_member: pytgbot.api_types.receivable.peer.ChatMember


    Optional keyword parameters:

    :param invite_link: Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
    :type  invite_link: pytgbot.api_types.receivable.peer.ChatInviteLink

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, chat, from_peer, date, old_chat_member, new_chat_member, invite_link=None, _raw=None):
        """
        This object represents changes in the status of a chat member.

        https://core.telegram.org/bots/api#chatmemberupdated


        Parameters:

        :param chat: Chat the user belongs to
        :type  chat: pytgbot.api_types.receivable.peer.Chat

        :param from_peer: Performer of the action, which resulted in the change
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param date: Date the change was done in Unix time
        :type  date: int

        :param old_chat_member: Previous information about the chat member
        :type  old_chat_member: pytgbot.api_types.receivable.peer.ChatMember

        :param new_chat_member: New information about the chat member
        :type  new_chat_member: pytgbot.api_types.receivable.peer.ChatMember


        Optional keyword parameters:

        :param invite_link: Optional. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
        :type  invite_link: pytgbot.api_types.receivable.peer.ChatInviteLink

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMemberUpdated, self).__init__()
        assert_type_or_raise(chat, Chat, parameter_name="chat")
        self.chat = chat
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(date, int, parameter_name="date")
        self.date = date
        assert_type_or_raise(old_chat_member, ChatMember, parameter_name="old_chat_member")
        self.old_chat_member = old_chat_member
        assert_type_or_raise(new_chat_member, ChatMember, parameter_name="new_chat_member")
        self.new_chat_member = new_chat_member
        assert_type_or_raise(invite_link, None, ChatInviteLink, parameter_name="invite_link")
        self.invite_link = invite_link

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatMemberUpdated to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatMemberUpdated, self).to_array()

        array['chat'] = self.chat.to_array()  # type Chat
        array['from'] = self.from_peer.to_array()  # type User
        array['date'] = int(self.date)  # type int
        array['old_chat_member'] = self.old_chat_member.to_array()  # type ChatMember
        array['new_chat_member'] = self.new_chat_member.to_array()  # type ChatMember
        if self.invite_link is not None:
            array['invite_link'] = self.invite_link.to_array()  # type ChatInviteLink
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatMemberUpdated constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['chat'] = Chat.from_array(array.get('chat'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['date'] = int(array.get('date'))
        data['old_chat_member'] = ChatMember.from_array(array.get('old_chat_member'))
        data['new_chat_member'] = ChatMember.from_array(array.get('new_chat_member'))
        data['invite_link'] = ChatInviteLink.from_array(array.get('invite_link')) if array.get('invite_link') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMemberUpdated from a given dictionary.

        :return: new ChatMemberUpdated instance.
        :rtype: ChatMemberUpdated
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatMemberUpdated.validate_array(array)
        data['_raw'] = array
        return ChatMemberUpdated(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmemberupdated_instance)`
        """
        return "ChatMemberUpdated(chat={self.chat!r}, from_peer={self.from_peer!r}, date={self.date!r}, old_chat_member={self.old_chat_member!r}, new_chat_member={self.new_chat_member!r}, invite_link={self.invite_link!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmemberupdated_instance)`
        """
        if self._raw:
            return "ChatMemberUpdated.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMemberUpdated(chat={self.chat!r}, from_peer={self.from_peer!r}, date={self.date!r}, old_chat_member={self.old_chat_member!r}, new_chat_member={self.new_chat_member!r}, invite_link={self.invite_link!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmemberupdated_instance`
        """
        return (
            key in ["chat", "from_peer", "date", "old_chat_member", "new_chat_member", "invite_link"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMemberUpdated


class ChatJoinRequest(Result):
    """
    Represents a join request sent to a chat.

    https://core.telegram.org/bots/api#chatjoinrequest


    Parameters:

    :param chat: Chat to which the request was sent
    :type  chat: pytgbot.api_types.receivable.peer.Chat

    :param from_peer: User that sent the join request
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param date: Date the request was sent in Unix time
    :type  date: int


    Optional keyword parameters:

    :param bio: Optional. Bio of the user.
    :type  bio: str|unicode

    :param invite_link: Optional. Chat invite link that was used by the user to send the join request.
    :type  invite_link: pytgbot.api_types.receivable.peer.ChatInviteLink

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, chat, from_peer, date, bio=None, invite_link=None, _raw=None):
        """
        Represents a join request sent to a chat.

        https://core.telegram.org/bots/api#chatjoinrequest


        Parameters:

        :param chat: Chat to which the request was sent
        :type  chat: pytgbot.api_types.receivable.peer.Chat

        :param from_peer: User that sent the join request
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param date: Date the request was sent in Unix time
        :type  date: int


        Optional keyword parameters:

        :param bio: Optional. Bio of the user.
        :type  bio: str|unicode

        :param invite_link: Optional. Chat invite link that was used by the user to send the join request.
        :type  invite_link: pytgbot.api_types.receivable.peer.ChatInviteLink

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatJoinRequest, self).__init__()
        assert_type_or_raise(chat, Chat, parameter_name="chat")
        self.chat = chat
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(date, int, parameter_name="date")
        self.date = date
        assert_type_or_raise(bio, None, unicode_type, parameter_name="bio")
        self.bio = bio
        assert_type_or_raise(invite_link, None, ChatInviteLink, parameter_name="invite_link")
        self.invite_link = invite_link

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatJoinRequest to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatJoinRequest, self).to_array()

        array['chat'] = self.chat.to_array()  # type Chat
        array['from'] = self.from_peer.to_array()  # type User
        array['date'] = int(self.date)  # type int
        if self.bio is not None:
            array['bio'] = u(self.bio)  # py2: type unicode, py3: type str
        # end if
        if self.invite_link is not None:
            array['invite_link'] = self.invite_link.to_array()  # type ChatInviteLink
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatJoinRequest constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['chat'] = Chat.from_array(array.get('chat'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['date'] = int(array.get('date'))
        data['bio'] = u(array.get('bio')) if array.get('bio') is not None else None
        data['invite_link'] = ChatInviteLink.from_array(array.get('invite_link')) if array.get('invite_link') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatJoinRequest from a given dictionary.

        :return: new ChatJoinRequest instance.
        :rtype: ChatJoinRequest
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatJoinRequest.validate_array(array)
        data['_raw'] = array
        return ChatJoinRequest(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatjoinrequest_instance)`
        """
        return "ChatJoinRequest(chat={self.chat!r}, from_peer={self.from_peer!r}, date={self.date!r}, bio={self.bio!r}, invite_link={self.invite_link!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatjoinrequest_instance)`
        """
        if self._raw:
            return "ChatJoinRequest.from_array({self._raw})".format(self=self)
        # end if
        return "ChatJoinRequest(chat={self.chat!r}, from_peer={self.from_peer!r}, date={self.date!r}, bio={self.bio!r}, invite_link={self.invite_link!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatjoinrequest_instance`
        """
        return (
            key in ["chat", "from_peer", "date", "bio", "invite_link"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatJoinRequest


class ChatPermissions(Result):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

    https://core.telegram.org/bots/api#chatpermissions

    Optional keyword parameters:

    :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations and venues.
    :type  can_send_messages: bool

    :param can_send_media_messages: Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages.
    :type  can_send_media_messages: bool

    :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages.
    :type  can_send_polls: bool

    :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages.
    :type  can_send_other_messages: bool

    :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages.
    :type  can_add_web_page_previews: bool

    :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other settings.
                            Ignored in public supergroups.
    :type  can_change_info: bool

    :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat.
    :type  can_invite_users: bool

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages.
                             Ignored in public supergroups.
    :type  can_pin_messages: bool

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, can_send_messages=None, can_send_media_messages=None, can_send_polls=None, can_send_other_messages=None, can_add_web_page_previews=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, _raw=None):
        """
        Describes actions that a non-administrator user is allowed to take in a chat.

        https://core.telegram.org/bots/api#chatpermissions

        Optional keyword parameters:

        :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations and venues.
        :type  can_send_messages: bool

        :param can_send_media_messages: Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages.
        :type  can_send_media_messages: bool

        :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages.
        :type  can_send_polls: bool

        :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages.
        :type  can_send_other_messages: bool

        :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages.
        :type  can_add_web_page_previews: bool

        :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other settings.
                                Ignored in public supergroups.
        :type  can_change_info: bool

        :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat.
        :type  can_invite_users: bool

        :param can_pin_messages: Optional. True, if the user is allowed to pin messages.
                                 Ignored in public supergroups.
        :type  can_pin_messages: bool

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatPermissions, self).__init__()
        assert_type_or_raise(can_send_messages, None, bool, parameter_name="can_send_messages")
        self.can_send_messages = can_send_messages
        assert_type_or_raise(can_send_media_messages, None, bool, parameter_name="can_send_media_messages")
        self.can_send_media_messages = can_send_media_messages
        assert_type_or_raise(can_send_polls, None, bool, parameter_name="can_send_polls")
        self.can_send_polls = can_send_polls
        assert_type_or_raise(can_send_other_messages, None, bool, parameter_name="can_send_other_messages")
        self.can_send_other_messages = can_send_other_messages
        assert_type_or_raise(can_add_web_page_previews, None, bool, parameter_name="can_add_web_page_previews")
        self.can_add_web_page_previews = can_add_web_page_previews
        assert_type_or_raise(can_change_info, None, bool, parameter_name="can_change_info")
        self.can_change_info = can_change_info
        assert_type_or_raise(can_invite_users, None, bool, parameter_name="can_invite_users")
        self.can_invite_users = can_invite_users
        assert_type_or_raise(can_pin_messages, None, bool, parameter_name="can_pin_messages")
        self.can_pin_messages = can_pin_messages

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatPermissions to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatPermissions, self).to_array()

        if self.can_send_messages is not None:
            array['can_send_messages'] = bool(self.can_send_messages)  # type bool
        # end if
        if self.can_send_media_messages is not None:
            array['can_send_media_messages'] = bool(self.can_send_media_messages)  # type bool
        # end if
        if self.can_send_polls is not None:
            array['can_send_polls'] = bool(self.can_send_polls)  # type bool
        # end if
        if self.can_send_other_messages is not None:
            array['can_send_other_messages'] = bool(self.can_send_other_messages)  # type bool
        # end if
        if self.can_add_web_page_previews is not None:
            array['can_add_web_page_previews'] = bool(self.can_add_web_page_previews)  # type bool
        # end if
        if self.can_change_info is not None:
            array['can_change_info'] = bool(self.can_change_info)  # type bool
        # end if
        if self.can_invite_users is not None:
            array['can_invite_users'] = bool(self.can_invite_users)  # type bool
        # end if
        if self.can_pin_messages is not None:
            array['can_pin_messages'] = bool(self.can_pin_messages)  # type bool
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatPermissions constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['can_send_messages'] = bool(array.get('can_send_messages')) if array.get('can_send_messages') is not None else None
        data['can_send_media_messages'] = bool(array.get('can_send_media_messages')) if array.get('can_send_media_messages') is not None else None
        data['can_send_polls'] = bool(array.get('can_send_polls')) if array.get('can_send_polls') is not None else None
        data['can_send_other_messages'] = bool(array.get('can_send_other_messages')) if array.get('can_send_other_messages') is not None else None
        data['can_add_web_page_previews'] = bool(array.get('can_add_web_page_previews')) if array.get('can_add_web_page_previews') is not None else None
        data['can_change_info'] = bool(array.get('can_change_info')) if array.get('can_change_info') is not None else None
        data['can_invite_users'] = bool(array.get('can_invite_users')) if array.get('can_invite_users') is not None else None
        data['can_pin_messages'] = bool(array.get('can_pin_messages')) if array.get('can_pin_messages') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatPermissions from a given dictionary.

        :return: new ChatPermissions instance.
        :rtype: ChatPermissions
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatPermissions.validate_array(array)
        data['_raw'] = array
        return ChatPermissions(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatpermissions_instance)`
        """
        return "ChatPermissions(can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_polls={self.can_send_polls!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_pin_messages={self.can_pin_messages!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatpermissions_instance)`
        """
        if self._raw:
            return "ChatPermissions.from_array({self._raw})".format(self=self)
        # end if
        return "ChatPermissions(can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_polls={self.can_send_polls!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_pin_messages={self.can_pin_messages!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatpermissions_instance`
        """
        return (
            key in ["can_send_messages", "can_send_media_messages", "can_send_polls", "can_send_other_messages", "can_add_web_page_previews", "can_change_info", "can_invite_users", "can_pin_messages"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatPermissions


class ChatLocation(Result):
    """
    Represents a location to which a chat is connected.

    https://core.telegram.org/bots/api#chatlocation


    Parameters:

    :param location: The location to which the supergroup is connected. Can't be a live location.
    :type  location: pytgbot.api_types.receivable.media.Location

    :param address: Location address; 1-64 characters, as defined by the chat owner
    :type  address: str|unicode


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, location, address, _raw=None):
        """
        Represents a location to which a chat is connected.

        https://core.telegram.org/bots/api#chatlocation


        Parameters:

        :param location: The location to which the supergroup is connected. Can't be a live location.
        :type  location: pytgbot.api_types.receivable.media.Location

        :param address: Location address; 1-64 characters, as defined by the chat owner
        :type  address: str|unicode


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatLocation, self).__init__()
        from .media import Location
        assert_type_or_raise(location, Location, parameter_name="location")
        self.location = location
        assert_type_or_raise(address, unicode_type, parameter_name="address")
        self.address = address

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatLocation to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        from .media import Location
        array = super(ChatLocation, self).to_array()

        array['location'] = self.location.to_array()  # type Location
        array['address'] = u(self.address)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatLocation constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import Location
        data = Result.validate_array(array)
        data['location'] = Location.from_array(array.get('location'))
        data['address'] = u(array.get('address'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatLocation from a given dictionary.

        :return: new ChatLocation instance.
        :rtype: ChatLocation
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatLocation.validate_array(array)
        data['_raw'] = array
        return ChatLocation(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatlocation_instance)`
        """
        return "ChatLocation(location={self.location!r}, address={self.address!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatlocation_instance)`
        """
        if self._raw:
            return "ChatLocation.from_array({self._raw})".format(self=self)
        # end if
        return "ChatLocation(location={self.location!r}, address={self.address!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatlocation_instance`
        """
        return (
            key in ["location", "address"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatLocation
