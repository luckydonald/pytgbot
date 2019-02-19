# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise

from . import Result

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Peer(Result):
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

    :param first_name: User‘s or bot’s first name
    :type  first_name: str|unicode


    Optional keyword parameters:

    :param last_name: Optional. User‘s or bot’s last name
    :type  last_name: str|unicode

    :param username: Optional. User‘s or bot’s username
    :type  username: str|unicode

    :param language_code: Optional. IETF language tag of the user's language
    :type  language_code: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, is_bot, first_name, last_name=None, username=None, language_code=None, _raw=None):
        """
        This object represents a Telegram user or bot.

        https://core.telegram.org/bots/api#user


        Parameters:

        :param id: Unique identifier for this user or bot
        :type  id: int

        :param is_bot: True, if this user is a bot
        :type  is_bot: bool

        :param first_name: User‘s or bot’s first name
        :type  first_name: str|unicode


        Optional keyword parameters:

        :param last_name: Optional. User‘s or bot’s last name
        :type  last_name: str|unicode

        :param username: Optional. User‘s or bot’s username
        :type  username: str|unicode

        :param language_code: Optional. IETF language tag of the user's language
        :type  language_code: str|unicode

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

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this User to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(User, self).to_array()
        array['id'] = int(self.id)  # type int
        array['is_bot'] = bool(self.is_bot)  # type bool
        array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        if self.username is not None:
            array['username'] = u(self.username)  # py2: type unicode, py3: type str
        if self.language_code is not None:
            array['language_code'] = u(self.language_code)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new User from a given dictionary.

        :return: new User instance.
        :rtype: User
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['id'] = int(array.get('id'))
        data['is_bot'] = bool(array.get('is_bot'))
        data['first_name'] = u(array.get('first_name'))
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['username'] = u(array.get('username')) if array.get('username') is not None else None
        data['language_code'] = u(array.get('language_code')) if array.get('language_code') is not None else None
        data['_raw'] = array
        return User(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(user_instance)`
        """
        return "User(id={self.id!r}, is_bot={self.is_bot!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, language_code={self.language_code!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(user_instance)`
        """
        if self._raw:
            return "User.from_array({self._raw})".format(self=self)
        # end if
        return "User(id={self.id!r}, is_bot={self.is_bot!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, language_code={self.language_code!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in user_instance`
        """
        return key in ["id", "is_bot", "first_name", "last_name", "username", "language_code"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class User


class Chat(Peer):
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat


    Parameters:

    :param id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  id: int

    :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
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

    :param all_members_are_administrators: Optional. True if a group has ‘All Members Are Admins’ enabled.
    :type  all_members_are_administrators: bool

    :param photo: Optional. Chat photo. Returned only in getChat.
    :type  photo: pytgbot.api_types.receivable.media.ChatPhoto

    :param description: Optional. Description, for supergroups and channel chats. Returned only in getChat.
    :type  description: str|unicode

    :param invite_link: Optional. Chat invite link, for supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
    :type  invite_link: str|unicode

    :param pinned_message: Optional. Pinned message, for supergroups and channel chats. Returned only in getChat.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message

    :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :type  sticker_set_name: str|unicode

    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    :type  can_set_sticker_set: bool

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None, all_members_are_administrators=None, photo=None, description=None, invite_link=None, pinned_message=None, sticker_set_name=None, can_set_sticker_set=None, _raw=None):
        """
        This object represents a chat.

        https://core.telegram.org/bots/api#chat


        Parameters:

        :param id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type  id: int

        :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
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

        :param all_members_are_administrators: Optional. True if a group has ‘All Members Are Admins’ enabled.
        :type  all_members_are_administrators: bool

        :param photo: Optional. Chat photo. Returned only in getChat.
        :type  photo: pytgbot.api_types.receivable.media.ChatPhoto

        :param description: Optional. Description, for supergroups and channel chats. Returned only in getChat.
        :type  description: str|unicode

        :param invite_link: Optional. Chat invite link, for supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
        :type  invite_link: str|unicode

        :param pinned_message: Optional. Pinned message, for supergroups and channel chats. Returned only in getChat.
        :type  pinned_message: pytgbot.api_types.receivable.updates.Message

        :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
        :type  sticker_set_name: str|unicode

        :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in getChat.
        :type  can_set_sticker_set: bool

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

        assert_type_or_raise(all_members_are_administrators, None, bool, parameter_name="all_members_are_administrators")
        self.all_members_are_administrators = all_members_are_administrators

        assert_type_or_raise(photo, None, ChatPhoto, parameter_name="photo")
        self.photo = photo

        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description

        assert_type_or_raise(invite_link, None, unicode_type, parameter_name="invite_link")
        self.invite_link = invite_link

        assert_type_or_raise(pinned_message, None, Message, parameter_name="pinned_message")
        self.pinned_message = pinned_message

        assert_type_or_raise(sticker_set_name, None, unicode_type, parameter_name="sticker_set_name")
        self.sticker_set_name = sticker_set_name

        assert_type_or_raise(can_set_sticker_set, None, bool, parameter_name="can_set_sticker_set")
        self.can_set_sticker_set = can_set_sticker_set

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this Chat to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(Chat, self).to_array()
        array['id'] = int(self.id)  # type int
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.username is not None:
            array['username'] = u(self.username)  # py2: type unicode, py3: type str
        if self.first_name is not None:
            array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        if self.all_members_are_administrators is not None:
            array['all_members_are_administrators'] = bool(self.all_members_are_administrators)  # type bool
        if self.photo is not None:
            array['photo'] = self.photo.to_array()  # type ChatPhoto
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        if self.invite_link is not None:
            array['invite_link'] = u(self.invite_link)  # py2: type unicode, py3: type str
        if self.pinned_message is not None:
            array['pinned_message'] = self.pinned_message.to_array()  # type Message
        if self.sticker_set_name is not None:
            array['sticker_set_name'] = u(self.sticker_set_name)  # py2: type unicode, py3: type str
        if self.can_set_sticker_set is not None:
            array['can_set_sticker_set'] = bool(self.can_set_sticker_set)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Chat from a given dictionary.

        :return: new Chat instance.
        :rtype: Chat
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import ChatPhoto
        from .updates import Message

        data = {}
        data['id'] = int(array.get('id'))
        data['type'] = u(array.get('type'))
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['username'] = u(array.get('username')) if array.get('username') is not None else None
        data['first_name'] = u(array.get('first_name')) if array.get('first_name') is not None else None
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['all_members_are_administrators'] = bool(array.get('all_members_are_administrators')) if array.get('all_members_are_administrators') is not None else None
        data['photo'] = ChatPhoto.from_array(array.get('photo')) if array.get('photo') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['invite_link'] = u(array.get('invite_link')) if array.get('invite_link') is not None else None
        data['pinned_message'] = Message.from_array(array.get('pinned_message')) if array.get('pinned_message') is not None else None
        data['sticker_set_name'] = u(array.get('sticker_set_name')) if array.get('sticker_set_name') is not None else None
        data['can_set_sticker_set'] = bool(array.get('can_set_sticker_set')) if array.get('can_set_sticker_set') is not None else None
        data['_raw'] = array
        return Chat(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chat_instance)`
        """
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, all_members_are_administrators={self.all_members_are_administrators!r}, photo={self.photo!r}, description={self.description!r}, invite_link={self.invite_link!r}, pinned_message={self.pinned_message!r}, sticker_set_name={self.sticker_set_name!r}, can_set_sticker_set={self.can_set_sticker_set!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chat_instance)`
        """
        if self._raw:
            return "Chat.from_array({self._raw})".format(self=self)
        # end if
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, all_members_are_administrators={self.all_members_are_administrators!r}, photo={self.photo!r}, description={self.description!r}, invite_link={self.invite_link!r}, pinned_message={self.pinned_message!r}, sticker_set_name={self.sticker_set_name!r}, can_set_sticker_set={self.can_set_sticker_set!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chat_instance`
        """
        return key in ["id", "type", "title", "username", "first_name", "last_name", "all_members_are_administrators", "photo", "description", "invite_link", "pinned_message", "sticker_set_name", "can_set_sticker_set"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class Chat


class ChatMember(Result):
    """
    This object contains information about one member of a chat.

    https://core.telegram.org/bots/api#chatmember


    Parameters:

    :param user: Information about the user
    :type  user: pytgbot.api_types.receivable.peer.User

    :param status: The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”
    :type  status: str|unicode


    Optional keyword parameters:

    :param until_date: Optional. Restricted and kicked only. Date when restrictions will be lifted for this user, unix time
    :type  until_date: int

    :param can_be_edited: Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
    :type  can_be_edited: bool

    :param can_change_info: Optional. Administrators only. True, if the administrator can change the chat title, photo and other settings
    :type  can_change_info: bool

    :param can_post_messages: Optional. Administrators only. True, if the administrator can post in the channel, channels only
    :type  can_post_messages: bool

    :param can_edit_messages: Optional. Administrators only. True, if the administrator can edit messages of other users and can pin messages, channels only
    :type  can_edit_messages: bool

    :param can_delete_messages: Optional. Administrators only. True, if the administrator can delete messages of other users
    :type  can_delete_messages: bool

    :param can_invite_users: Optional. Administrators only. True, if the administrator can invite new users to the chat
    :type  can_invite_users: bool

    :param can_restrict_members: Optional. Administrators only. True, if the administrator can restrict, ban or unban chat members
    :type  can_restrict_members: bool

    :param can_pin_messages: Optional. Administrators only. True, if the administrator can pin messages, supergroups only
    :type  can_pin_messages: bool

    :param can_promote_members: Optional. Administrators only. True, if the administrator can add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    :type  can_promote_members: bool

    :param can_send_messages: Optional. Restricted only. True, if the user can send text messages, contacts, locations and venues
    :type  can_send_messages: bool

    :param can_send_media_messages: Optional. Restricted only. True, if the user can send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
    :type  can_send_media_messages: bool

    :param can_send_other_messages: Optional. Restricted only. True, if the user can send animations, games, stickers and use inline bots, implies can_send_media_messages
    :type  can_send_other_messages: bool

    :param can_add_web_page_previews: Optional. Restricted only. True, if user may add web page previews to his messages, implies can_send_media_messages
    :type  can_add_web_page_previews: bool

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, user, status, until_date=None, can_be_edited=None, can_change_info=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_invite_users=None, can_restrict_members=None, can_pin_messages=None, can_promote_members=None, can_send_messages=None, can_send_media_messages=None, can_send_other_messages=None, can_add_web_page_previews=None, _raw=None):
        """
        This object contains information about one member of a chat.

        https://core.telegram.org/bots/api#chatmember


        Parameters:

        :param user: Information about the user
        :type  user: pytgbot.api_types.receivable.peer.User

        :param status: The member's status in the chat. Can be “creator”, “administrator”, “member”, “restricted”, “left” or “kicked”
        :type  status: str|unicode


        Optional keyword parameters:

        :param until_date: Optional. Restricted and kicked only. Date when restrictions will be lifted for this user, unix time
        :type  until_date: int

        :param can_be_edited: Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
        :type  can_be_edited: bool

        :param can_change_info: Optional. Administrators only. True, if the administrator can change the chat title, photo and other settings
        :type  can_change_info: bool

        :param can_post_messages: Optional. Administrators only. True, if the administrator can post in the channel, channels only
        :type  can_post_messages: bool

        :param can_edit_messages: Optional. Administrators only. True, if the administrator can edit messages of other users and can pin messages, channels only
        :type  can_edit_messages: bool

        :param can_delete_messages: Optional. Administrators only. True, if the administrator can delete messages of other users
        :type  can_delete_messages: bool

        :param can_invite_users: Optional. Administrators only. True, if the administrator can invite new users to the chat
        :type  can_invite_users: bool

        :param can_restrict_members: Optional. Administrators only. True, if the administrator can restrict, ban or unban chat members
        :type  can_restrict_members: bool

        :param can_pin_messages: Optional. Administrators only. True, if the administrator can pin messages, supergroups only
        :type  can_pin_messages: bool

        :param can_promote_members: Optional. Administrators only. True, if the administrator can add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
        :type  can_promote_members: bool

        :param can_send_messages: Optional. Restricted only. True, if the user can send text messages, contacts, locations and venues
        :type  can_send_messages: bool

        :param can_send_media_messages: Optional. Restricted only. True, if the user can send audios, documents, photos, videos, video notes and voice notes, implies can_send_messages
        :type  can_send_media_messages: bool

        :param can_send_other_messages: Optional. Restricted only. True, if the user can send animations, games, stickers and use inline bots, implies can_send_media_messages
        :type  can_send_other_messages: bool

        :param can_add_web_page_previews: Optional. Restricted only. True, if user may add web page previews to his messages, implies can_send_media_messages
        :type  can_add_web_page_previews: bool

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ChatMember, self).__init__()

        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user

        assert_type_or_raise(status, unicode_type, parameter_name="status")
        self.status = status

        assert_type_or_raise(until_date, None, int, parameter_name="until_date")
        self.until_date = until_date

        assert_type_or_raise(can_be_edited, None, bool, parameter_name="can_be_edited")
        self.can_be_edited = can_be_edited

        assert_type_or_raise(can_change_info, None, bool, parameter_name="can_change_info")
        self.can_change_info = can_change_info

        assert_type_or_raise(can_post_messages, None, bool, parameter_name="can_post_messages")
        self.can_post_messages = can_post_messages

        assert_type_or_raise(can_edit_messages, None, bool, parameter_name="can_edit_messages")
        self.can_edit_messages = can_edit_messages

        assert_type_or_raise(can_delete_messages, None, bool, parameter_name="can_delete_messages")
        self.can_delete_messages = can_delete_messages

        assert_type_or_raise(can_invite_users, None, bool, parameter_name="can_invite_users")
        self.can_invite_users = can_invite_users

        assert_type_or_raise(can_restrict_members, None, bool, parameter_name="can_restrict_members")
        self.can_restrict_members = can_restrict_members

        assert_type_or_raise(can_pin_messages, None, bool, parameter_name="can_pin_messages")
        self.can_pin_messages = can_pin_messages

        assert_type_or_raise(can_promote_members, None, bool, parameter_name="can_promote_members")
        self.can_promote_members = can_promote_members

        assert_type_or_raise(can_send_messages, None, bool, parameter_name="can_send_messages")
        self.can_send_messages = can_send_messages

        assert_type_or_raise(can_send_media_messages, None, bool, parameter_name="can_send_media_messages")
        self.can_send_media_messages = can_send_media_messages

        assert_type_or_raise(can_send_other_messages, None, bool, parameter_name="can_send_other_messages")
        self.can_send_other_messages = can_send_other_messages

        assert_type_or_raise(can_add_web_page_previews, None, bool, parameter_name="can_add_web_page_previews")
        self.can_add_web_page_previews = can_add_web_page_previews

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this ChatMember to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(ChatMember, self).to_array()
        array['user'] = self.user.to_array()  # type User
        array['status'] = u(self.status)  # py2: type unicode, py3: type str
        if self.until_date is not None:
            array['until_date'] = int(self.until_date)  # type int
        if self.can_be_edited is not None:
            array['can_be_edited'] = bool(self.can_be_edited)  # type bool
        if self.can_change_info is not None:
            array['can_change_info'] = bool(self.can_change_info)  # type bool
        if self.can_post_messages is not None:
            array['can_post_messages'] = bool(self.can_post_messages)  # type bool
        if self.can_edit_messages is not None:
            array['can_edit_messages'] = bool(self.can_edit_messages)  # type bool
        if self.can_delete_messages is not None:
            array['can_delete_messages'] = bool(self.can_delete_messages)  # type bool
        if self.can_invite_users is not None:
            array['can_invite_users'] = bool(self.can_invite_users)  # type bool
        if self.can_restrict_members is not None:
            array['can_restrict_members'] = bool(self.can_restrict_members)  # type bool
        if self.can_pin_messages is not None:
            array['can_pin_messages'] = bool(self.can_pin_messages)  # type bool
        if self.can_promote_members is not None:
            array['can_promote_members'] = bool(self.can_promote_members)  # type bool
        if self.can_send_messages is not None:
            array['can_send_messages'] = bool(self.can_send_messages)  # type bool
        if self.can_send_media_messages is not None:
            array['can_send_media_messages'] = bool(self.can_send_media_messages)  # type bool
        if self.can_send_other_messages is not None:
            array['can_send_other_messages'] = bool(self.can_send_other_messages)  # type bool
        if self.can_add_web_page_previews is not None:
            array['can_add_web_page_previews'] = bool(self.can_add_web_page_previews)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatMember from a given dictionary.

        :return: new ChatMember instance.
        :rtype: ChatMember
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['user'] = User.from_array(array.get('user'))
        data['status'] = u(array.get('status'))
        data['until_date'] = int(array.get('until_date')) if array.get('until_date') is not None else None
        data['can_be_edited'] = bool(array.get('can_be_edited')) if array.get('can_be_edited') is not None else None
        data['can_change_info'] = bool(array.get('can_change_info')) if array.get('can_change_info') is not None else None
        data['can_post_messages'] = bool(array.get('can_post_messages')) if array.get('can_post_messages') is not None else None
        data['can_edit_messages'] = bool(array.get('can_edit_messages')) if array.get('can_edit_messages') is not None else None
        data['can_delete_messages'] = bool(array.get('can_delete_messages')) if array.get('can_delete_messages') is not None else None
        data['can_invite_users'] = bool(array.get('can_invite_users')) if array.get('can_invite_users') is not None else None
        data['can_restrict_members'] = bool(array.get('can_restrict_members')) if array.get('can_restrict_members') is not None else None
        data['can_pin_messages'] = bool(array.get('can_pin_messages')) if array.get('can_pin_messages') is not None else None
        data['can_promote_members'] = bool(array.get('can_promote_members')) if array.get('can_promote_members') is not None else None
        data['can_send_messages'] = bool(array.get('can_send_messages')) if array.get('can_send_messages') is not None else None
        data['can_send_media_messages'] = bool(array.get('can_send_media_messages')) if array.get('can_send_media_messages') is not None else None
        data['can_send_other_messages'] = bool(array.get('can_send_other_messages')) if array.get('can_send_other_messages') is not None else None
        data['can_add_web_page_previews'] = bool(array.get('can_add_web_page_previews')) if array.get('can_add_web_page_previews') is not None else None
        data['_raw'] = array
        return ChatMember(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatmember_instance)`
        """
        return "ChatMember(user={self.user!r}, status={self.status!r}, until_date={self.until_date!r}, can_be_edited={self.can_be_edited!r}, can_change_info={self.can_change_info!r}, can_post_messages={self.can_post_messages!r}, can_edit_messages={self.can_edit_messages!r}, can_delete_messages={self.can_delete_messages!r}, can_invite_users={self.can_invite_users!r}, can_restrict_members={self.can_restrict_members!r}, can_pin_messages={self.can_pin_messages!r}, can_promote_members={self.can_promote_members!r}, can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatmember_instance)`
        """
        if self._raw:
            return "ChatMember.from_array({self._raw})".format(self=self)
        # end if
        return "ChatMember(user={self.user!r}, status={self.status!r}, until_date={self.until_date!r}, can_be_edited={self.can_be_edited!r}, can_change_info={self.can_change_info!r}, can_post_messages={self.can_post_messages!r}, can_edit_messages={self.can_edit_messages!r}, can_delete_messages={self.can_delete_messages!r}, can_invite_users={self.can_invite_users!r}, can_restrict_members={self.can_restrict_members!r}, can_pin_messages={self.can_pin_messages!r}, can_promote_members={self.can_promote_members!r}, can_send_messages={self.can_send_messages!r}, can_send_media_messages={self.can_send_media_messages!r}, can_send_other_messages={self.can_send_other_messages!r}, can_add_web_page_previews={self.can_add_web_page_previews!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatmember_instance`
        """
        return key in ["user", "status", "until_date", "can_be_edited", "can_change_info", "can_post_messages", "can_edit_messages", "can_delete_messages", "can_invite_users", "can_restrict_members", "can_pin_messages", "can_promote_members", "can_send_messages", "can_send_media_messages", "can_send_other_messages", "can_add_web_page_previews"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class ChatMember
