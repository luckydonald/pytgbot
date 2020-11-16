# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result

__author__ = 'luckydonald'


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
    
    :param id: Unique identifier for this user or bot
    :type  id: int
    
    :param is_bot: True, if this user is a bot
    :type  is_bot: bool
    
    :param first_name: User's or bot's first name
    :type  first_name: str|unicode
    

    Optional keyword parameters:
    
    :param last_name: Optional. User's or bot's last name
    :type  last_name: str|unicode
    
    :param username: Optional. User's or bot's username
    :type  username: str|unicode
    
    :param language_code: Optional. IETF language tag of the user's language
    :type  language_code: str|unicode
    
    :param can_join_groups: Optional. True, if the bot can be invited to groups. Returned only in getMe.
    :type  can_join_groups: bool
    
    :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    :type  can_read_all_group_messages: bool
    
    :param supports_inline_queries: Optional. True, if the bot supports inline queries. Returned only in getMe.
    :type  supports_inline_queries: bool
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, is_bot, first_name, last_name=None, username=None, language_code=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None, _raw=None):
        """
        This object represents a Telegram user or bot.

        https://core.telegram.org/bots/api#user
        

        Parameters:
        
        :param id: Unique identifier for this user or bot
        :type  id: int
        
        :param is_bot: True, if this user is a bot
        :type  is_bot: bool
        
        :param first_name: User's or bot's first name
        :type  first_name: str|unicode
        

        Optional keyword parameters:
        
        :param last_name: Optional. User's or bot's last name
        :type  last_name: str|unicode
        
        :param username: Optional. User's or bot's username
        :type  username: str|unicode
        
        :param language_code: Optional. IETF language tag of the user's language
        :type  language_code: str|unicode
        
        :param can_join_groups: Optional. True, if the bot can be invited to groups. Returned only in getMe.
        :type  can_join_groups: bool
        
        :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
        :type  can_read_all_group_messages: bool
        
        :param supports_inline_queries: Optional. True, if the bot supports inline queries. Returned only in getMe.
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
    
    :param id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  id: int
    
    :param type: Type of chat, can be either "private", "group", "supergroup" or "channel"
    :type  type: str|unicode
    

    Optional keyword parameters:
    
    :param title: Optional. Title, for supergroups, channels and group chats
    :type  title: str|unicode
    
    :param username: Optional. Username, for private chats, supergroups and channels if available
    :type  username: str|unicode
    
    :param first_name: Optional. First name of the other party in a private chat
    :type  first_name: str|unicode
    
    :param last_name: Optional. Last name of the other party in a private chat
    :type  last_name: str|unicode
    
    :param photo: Optional. Chat photo. Returned only in getChat.
    :type  photo: pytgbot.api_types.receivable.media.ChatPhoto
    
    :param bio: Optional. Bio of the other party in a private chat. Returned only in getChat.
    :type  bio: str|unicode
    
    :param description: Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    :type  description: str|unicode
    
    :param invite_link: Optional. Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
    :type  invite_link: str|unicode
    
    :param pinned_message: Optional. The most recent pinned message (by sending date). Returned only in getChat.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message
    
    :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    :type  permissions: pytgbot.api_types.receivable.peer.ChatPermissions
    
    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
    :type  slow_mode_delay: int
    
    :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :type  sticker_set_name: str|unicode
    
    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    :type  can_set_sticker_set: bool
    
    :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
    :type  linked_chat_id: int
    
    :param location: Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
    :type  location: pytgbot.api_types.receivable.peer.ChatLocation
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None, photo=None, bio=None, description=None, invite_link=None, pinned_message=None, permissions=None, slow_mode_delay=None, sticker_set_name=None, can_set_sticker_set=None, linked_chat_id=None, location=None, _raw=None):
        """
        This object represents a chat.

        https://core.telegram.org/bots/api#chat
        

        Parameters:
        
        :param id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type  id: int
        
        :param type: Type of chat, can be either "private", "group", "supergroup" or "channel"
        :type  type: str|unicode
        

        Optional keyword parameters:
        
        :param title: Optional. Title, for supergroups, channels and group chats
        :type  title: str|unicode
        
        :param username: Optional. Username, for private chats, supergroups and channels if available
        :type  username: str|unicode
        
        :param first_name: Optional. First name of the other party in a private chat
        :type  first_name: str|unicode
        
        :param last_name: Optional. Last name of the other party in a private chat
        :type  last_name: str|unicode
        
        :param photo: Optional. Chat photo. Returned only in getChat.
        :type  photo: pytgbot.api_types.receivable.media.ChatPhoto
        
        :param bio: Optional. Bio of the other party in a private chat. Returned only in getChat.
        :type  bio: str|unicode
        
        :param description: Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
        :type  description: str|unicode
        
        :param invite_link: Optional. Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
        :type  invite_link: str|unicode
        
        :param pinned_message: Optional. The most recent pinned message (by sending date). Returned only in getChat.
        :type  pinned_message: pytgbot.api_types.receivable.updates.Message
        
        :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
        :type  permissions: pytgbot.api_types.receivable.peer.ChatPermissions
        
        :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
        :type  slow_mode_delay: int
        
        :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
        :type  sticker_set_name: str|unicode
        
        :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in getChat.
        :type  can_set_sticker_set: bool
        
        :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in getChat.
        :type  linked_chat_id: int
        
        :param location: Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat.
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
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['invite_link'] = u(array.get('invite_link')) if array.get('invite_link') is not None else None
        data['pinned_message'] = Message.from_array(array.get('pinned_message')) if array.get('pinned_message') is not None else None
        data['permissions'] = ChatPermissions.from_array(array.get('permissions')) if array.get('permissions') is not None else None
        data['slow_mode_delay'] = int(array.get('slow_mode_delay')) if array.get('slow_mode_delay') is not None else None
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
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, photo={self.photo!r}, bio={self.bio!r}, description={self.description!r}, invite_link={self.invite_link!r}, pinned_message={self.pinned_message!r}, permissions={self.permissions!r}, slow_mode_delay={self.slow_mode_delay!r}, sticker_set_name={self.sticker_set_name!r}, can_set_sticker_set={self.can_set_sticker_set!r}, linked_chat_id={self.linked_chat_id!r}, location={self.location!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chat_instance)`
        """
        if self._raw:
            return "Chat.from_array({self._raw})".format(self=self)
        # end if
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, photo={self.photo!r}, bio={self.bio!r}, description={self.description!r}, invite_link={self.invite_link!r}, pinned_message={self.pinned_message!r}, permissions={self.permissions!r}, slow_mode_delay={self.slow_mode_delay!r}, sticker_set_name={self.sticker_set_name!r}, can_set_sticker_set={self.can_set_sticker_set!r}, linked_chat_id={self.linked_chat_id!r}, location={self.location!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chat_instance`
        """
        return (
            key in ["id", "type", "title", "username", "first_name", "last_name", "photo", "bio", "description", "invite_link", "pinned_message", "permissions", "slow_mode_delay", "sticker_set_name", "can_set_sticker_set", "linked_chat_id", "location"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Chat


class ChatMember(Result):
    """
    This object contains information about one member of a chat.

    https://core.telegram.org/bots/api#chatmember
    

    Parameters:
    
    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User
    
    :param status: The member's status in the chat. Can be "creator", "administrator", "member", "restricted", "left" or "kicked"
    :type  status: str|unicode
    

    Optional keyword parameters:
    
    :param custom_title: Optional. Owner and administrators only. Custom title for this user
    :type  custom_title: str|unicode
    
    :param is_anonymous: Optional. Owner and administrators only. True, if the user's presence in the chat is hidden
    :type  is_anonymous: bool
    
    :param can_be_edited: Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
    :type  can_be_edited: bool
    
    :param can_post_messages: Optional. Administrators only. True, if the administrator can post in the channel; channels only
    :type  can_post_messages: bool
    
    :param can_edit_messages: Optional. Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only
    :type  can_edit_messages: bool
    
    :param can_delete_messages: Optional. Administrators only. True, if the administrator can delete messages of other users
    :type  can_delete_messages: bool
    
    :param can_restrict_members: Optional. Administrators only. True, if the administrator can restrict, ban or unban chat members
    :type  can_restrict_members: bool
    
    :param can_promote_members: Optional. Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    :type  can_promote_members: bool
    
    :param can_change_info: Optional. Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings
    :type  can_change_info: bool
    
    :param can_invite_users: Optional. Administrators and restricted only. True, if the user is allowed to invite new users to the chat
    :type  can_invite_users: bool
    
    :param can_pin_messages: Optional. Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only
    :type  can_pin_messages: bool
    
    :param is_member: Optional. Restricted only. True, if the user is a member of the chat at the moment of the request
    :type  is_member: bool
    
    :param can_send_messages: Optional. Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues
    :type  can_send_messages: bool
    
    :param can_send_media_messages: Optional. Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    :type  can_send_media_messages: bool
    
    :param can_send_polls: Optional. Restricted only. True, if the user is allowed to send polls
    :type  can_send_polls: bool
    
    :param can_send_other_messages: Optional. Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots
    :type  can_send_other_messages: bool
    
    :param can_add_web_page_previews: Optional. Restricted only. True, if the user is allowed to add web page previews to their messages
    :type  can_add_web_page_previews: bool
    
    :param until_date: Optional. Restricted and kicked only. Date when restrictions will be lifted for this user; unix time
    :type  until_date: int
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, user, status, custom_title=None, is_anonymous=None, can_be_edited=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, is_member=None, can_send_messages=None, can_send_media_messages=None, can_send_polls=None, can_send_other_messages=None, can_add_web_page_previews=None, until_date=None, _raw=None):
        """
        This object contains information about one member of a chat.

        https://core.telegram.org/bots/api#chatmember
        

        Parameters:
        
        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User
        
        :param status: The member's status in the chat. Can be "creator", "administrator", "member", "restricted", "left" or "kicked"
        :type  status: str|unicode
        

        Optional keyword parameters:
        
        :param custom_title: Optional. Owner and administrators only. Custom title for this user
        :type  custom_title: str|unicode
        
        :param is_anonymous: Optional. Owner and administrators only. True, if the user's presence in the chat is hidden
        :type  is_anonymous: bool
        
        :param can_be_edited: Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
        :type  can_be_edited: bool
        
        :param can_post_messages: Optional. Administrators only. True, if the administrator can post in the channel; channels only
        :type  can_post_messages: bool
        
        :param can_edit_messages: Optional. Administrators only. True, if the administrator can edit messages of other users and can pin messages; channels only
        :type  can_edit_messages: bool
        
        :param can_delete_messages: Optional. Administrators only. True, if the administrator can delete messages of other users
        :type  can_delete_messages: bool
        
        :param can_restrict_members: Optional. Administrators only. True, if the administrator can restrict, ban or unban chat members
        :type  can_restrict_members: bool
        
        :param can_promote_members: Optional. Administrators only. True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
        :type  can_promote_members: bool
        
        :param can_change_info: Optional. Administrators and restricted only. True, if the user is allowed to change the chat title, photo and other settings
        :type  can_change_info: bool
        
        :param can_invite_users: Optional. Administrators and restricted only. True, if the user is allowed to invite new users to the chat
        :type  can_invite_users: bool
        
        :param can_pin_messages: Optional. Administrators and restricted only. True, if the user is allowed to pin messages; groups and supergroups only
        :type  can_pin_messages: bool
        
        :param is_member: Optional. Restricted only. True, if the user is a member of the chat at the moment of the request
        :type  is_member: bool
        
        :param can_send_messages: Optional. Restricted only. True, if the user is allowed to send text messages, contacts, locations and venues
        :type  can_send_messages: bool
        
        :param can_send_media_messages: Optional. Restricted only. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
        :type  can_send_media_messages: bool
        
        :param can_send_polls: Optional. Restricted only. True, if the user is allowed to send polls
        :type  can_send_polls: bool
        
        :param can_send_other_messages: Optional. Restricted only. True, if the user is allowed to send animations, games, stickers and use inline bots
        :type  can_send_other_messages: bool
        
        :param can_add_web_page_previews: Optional. Restricted only. True, if the user is allowed to add web page previews to their messages
        :type  can_add_web_page_previews: bool
        
        :param until_date: Optional. Restricted and kicked only. Date when restrictions will be lifted for this user; unix time
        :type  until_date: int
        
        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMember, self).__init__()
        
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status
        assert_type_or_raise(custom_title, None, unicode_type, parameter_name="custom_title")
        self.custom_title = custom_title
        assert_type_or_raise(is_anonymous, None, bool, parameter_name="is_anonymous")
        self.is_anonymous = is_anonymous
        assert_type_or_raise(can_be_edited, None, bool, parameter_name="can_be_edited")
        self.can_be_edited = can_be_edited
        assert_type_or_raise(can_post_messages, None, bool, parameter_name="can_post_messages")
        self.can_post_messages = can_post_messages
        assert_type_or_raise(can_edit_messages, None, bool, parameter_name="can_edit_messages")
        self.can_edit_messages = can_edit_messages
        assert_type_or_raise(can_delete_messages, None, bool, parameter_name="can_delete_messages")
        self.can_delete_messages = can_delete_messages
        assert_type_or_raise(can_restrict_members, None, bool, parameter_name="can_restrict_members")
        self.can_restrict_members = can_restrict_members
        assert_type_or_raise(can_promote_members, None, bool, parameter_name="can_promote_members")
        self.can_promote_members = can_promote_members
        assert_type_or_raise(can_change_info, None, bool, parameter_name="can_change_info")
        self.can_change_info = can_change_info
        assert_type_or_raise(can_invite_users, None, bool, parameter_name="can_invite_users")
        self.can_invite_users = can_invite_users
        assert_type_or_raise(can_pin_messages, None, bool, parameter_name="can_pin_messages")
        self.can_pin_messages = can_pin_messages
        assert_type_or_raise(is_member, None, bool, parameter_name="is_member")
        self.is_member = is_member
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
        assert_type_or_raise(until_date, None, int, parameter_name="until_date")
        self.until_date = until_date

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
        
        array['user'] = self.user.to_array()  # type User
        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        if self.custom_title is not None:
            array['custom_title'] = u(self.custom_title)  # py2: type unicode, py3: type str
        # end if
        if self.is_anonymous is not None:
            array['is_anonymous'] = bool(self.is_anonymous)  # type bool
        # end if
        if self.can_be_edited is not None:
            array['can_be_edited'] = bool(self.can_be_edited)  # type bool
        # end if
        if self.can_post_messages is not None:
            array['can_post_messages'] = bool(self.can_post_messages)  # type bool
        # end if
        if self.can_edit_messages is not None:
            array['can_edit_messages'] = bool(self.can_edit_messages)  # type bool
        # end if
        if self.can_delete_messages is not None:
            array['can_delete_messages'] = bool(self.can_delete_messages)  # type bool
        # end if
        if self.can_restrict_members is not None:
            array['can_restrict_members'] = bool(self.can_restrict_members)  # type bool
        # end if
        if self.can_promote_members is not None:
            array['can_promote_members'] = bool(self.can_promote_members)  # type bool
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
        if self.is_member is not None:
            array['is_member'] = bool(self.is_member)  # type bool
        # end if
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
        if self.until_date is not None:
            array['until_date'] = int(self.until_date)  # type int
        # end if

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
        data['user'] = User.from_array(array.get('user'))
        data['status'] = u(array.get('status'))
        data['custom_title'] = u(array.get('custom_title')) if array.get('custom_title') is not None else None
        data['is_anonymous'] = bool(array.get('is_anonymous')) if array.get('is_anonymous') is not None else None
        data['can_be_edited'] = bool(array.get('can_be_edited')) if array.get('can_be_edited') is not None else None
        data['can_post_messages'] = bool(array.get('can_post_messages')) if array.get('can_post_messages') is not None else None
        data['can_edit_messages'] = bool(array.get('can_edit_messages')) if array.get('can_edit_messages') is not None else None
        data['can_delete_messages'] = bool(array.get('can_delete_messages')) if array.get('can_delete_messages') is not None else None
        data['can_restrict_members'] = bool(array.get('can_restrict_members')) if array.get('can_restrict_members') is not None else None
        data['can_promote_members'] = bool(array.get('can_promote_members')) if array.get('can_promote_members') is not None else None
        data['can_change_info'] = bool(array.get('can_change_info')) if array.get('can_change_info') is not None else None
        data['can_invite_users'] = bool(array.get('can_invite_users')) if array.get('can_invite_users') is not None else None
        data['can_pin_messages'] = bool(array.get('can_pin_messages')) if array.get('can_pin_messages') is not None else None
        data['is_member'] = bool(array.get('is_member')) if array.get('is_member') is not None else None
        data['can_send_messages'] = bool(array.get('can_send_messages')) if array.get('can_send_messages') is not None else None
        data['can_send_media_messages'] = bool(array.get('can_send_media_messages')) if array.get('can_send_media_messages') is not None else None
        data['can_send_polls'] = bool(array.get('can_send_polls')) if array.get('can_send_polls') is not None else None
        data['can_send_other_messages'] = bool(array.get('can_send_other_messages')) if array.get('can_send_other_messages') is not None else None
        data['can_add_web_page_previews'] = bool(array.get('can_add_web_page_previews')) if array.get('can_add_web_page_previews') is not None else None
        data['until_date'] = int(array.get('until_date')) if array.get('until_date') is not None else None
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
        return "ChatMember(user={self.user!r}, status={self.status!r}, custom_title={self.custom_title!r}, is_anonymous={self.is_anonymous!r}, can_be_edited={self.can_be_edited!r}, can_post_messages={self.can_post_messages!r}, can_edit_messages={self.can_edit_messages!r}, can_delete_messages={self.can_delete_messages!r}, can_restrict_members={self.can_restrict_members!r}, can_promote_members={self.can_promote_members!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_pin_messages={self.can_pin_messages!r}, is_member={self.is_member!r}, can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_polls={self.can_send_polls!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r}, until_date={self.until_date!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmember_instance)`
        """
        if self._raw:
            return "ChatMember.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMember(user={self.user!r}, status={self.status!r}, custom_title={self.custom_title!r}, is_anonymous={self.is_anonymous!r}, can_be_edited={self.can_be_edited!r}, can_post_messages={self.can_post_messages!r}, can_edit_messages={self.can_edit_messages!r}, can_delete_messages={self.can_delete_messages!r}, can_restrict_members={self.can_restrict_members!r}, can_promote_members={self.can_promote_members!r}, can_change_info={self.can_change_info!r}, can_invite_users={self.can_invite_users!r}, can_pin_messages={self.can_pin_messages!r}, is_member={self.is_member!r}, can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_polls={self.can_send_polls!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r}, until_date={self.until_date!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmember_instance`
        """
        return (
            key in ["user", "status", "custom_title", "is_anonymous", "can_be_edited", "can_post_messages", "can_edit_messages", "can_delete_messages", "can_restrict_members", "can_promote_members", "can_change_info", "can_invite_users", "can_pin_messages", "is_member", "can_send_messages", "can_send_media_messages", "can_send_polls", "can_send_other_messages", "can_add_web_page_previews", "until_date"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatMember


class ChatPermissions(Result):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

    https://core.telegram.org/bots/api#chatpermissions

    Optional keyword parameters:
    
    :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations and venues
    :type  can_send_messages: bool
    
    :param can_send_media_messages: Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    :type  can_send_media_messages: bool
    
    :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages
    :type  can_send_polls: bool
    
    :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
    :type  can_send_other_messages: bool
    
    :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
    :type  can_add_web_page_previews: bool
    
    :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    :type  can_change_info: bool
    
    :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat
    :type  can_invite_users: bool
    
    :param can_pin_messages: Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
    :type  can_pin_messages: bool
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, can_send_messages=None, can_send_media_messages=None, can_send_polls=None, can_send_other_messages=None, can_add_web_page_previews=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, _raw=None):
        """
        Describes actions that a non-administrator user is allowed to take in a chat.

        https://core.telegram.org/bots/api#chatpermissions

        Optional keyword parameters:
        
        :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations and venues
        :type  can_send_messages: bool
        
        :param can_send_media_messages: Optional. True, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
        :type  can_send_media_messages: bool
        
        :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages
        :type  can_send_polls: bool
        
        :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use inline bots, implies can_send_media_messages
        :type  can_send_other_messages: bool
        
        :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their messages, implies can_send_media_messages
        :type  can_add_web_page_previews: bool
        
        :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
        :type  can_change_info: bool
        
        :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat
        :type  can_invite_users: bool
        
        :param can_pin_messages: Optional. True, if the user is allowed to pin messages. Ignored in public supergroups
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

