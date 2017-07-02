# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.encoding import unicode_type

from pytgbot.api_types.receivable import Result

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
    
    :param first_name: User‘s or bot’s first name
    :type  first_name: str
    

    Optional keyword parameters:
    
    :param last_name: Optional. User‘s or bot’s last name
    :type  last_name: str
    
    :param username: Optional. User‘s or bot’s username
    :type  username: str
    
    :param language_code: Optional. IETF language tag of the user's language
    :type  language_code: str
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, first_name, last_name=None, username=None, language_code=None, _raw=None):
        """
        This object represents a Telegram user or bot.

        https://core.telegram.org/bots/api#user


        Parameters:

        :param id: Unique identifier for this user or bot
        :type  id: int

        :param first_name: User‘s or bot’s first name
        :type  first_name: str


        Optional keyword parameters:

        :param last_name: Optional. User‘s or bot’s last name
        :type  last_name: str

        :param username: Optional. User‘s or bot’s username
        :type  username: str
        
        :param language_code: Optional. IETF language tag of the user's language
        :type  language_code: str
        
        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(User, self).__init__()
        assert (id is not None)
        assert (isinstance(id, int))
        self.id = id

        assert (first_name is not None)
        assert (isinstance(first_name, str))
        self.first_name = first_name

        assert (last_name is None or isinstance(last_name, str))
        self.last_name = last_name

        assert (username is None or isinstance(username, str))
        self.username = username

        assert (language_code is None or isinstance(language_code, str))
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
        array['first_name'] = str(self.first_name)  # type str
        if self.last_name is not None:
            array['last_name'] = str(self.last_name)  # type str
        if self.username is not None:
            array['username'] = str(self.username)  # type str
        if self.language_code is not None:
            array['language_code'] = str(self.language_code)  # type str
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
        assert(isinstance(array, dict))

        data = {}
        data['id'] = int(array.get('id'))
        data['first_name'] = str(array.get('first_name'))
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        data['username'] = str(array.get('username')) if array.get('username') is not None else None
        data['language_code'] = str(array.get('language_code')) if array.get('language_code') is not None else None
        data['_raw'] = array
        return User(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(user_instance)`
        """
        return "User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, language_code={self.language_code!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(user_instance)`
        """
        if self._raw:
            return "User.from_array({self._raw})".format(self=self)
        # end if
        return "User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, language_code={self.language_code!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in user_instance`
        """
        return key in ["id", "first_name", "last_name", "username", "language_code"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class User


class Chat(Peer):
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat
    

    Parameters:
    
    :param id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier
    :type  id: int
    
    :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    :type  type: str
    

    Optional keyword parameters:
    
    :param title: Optional. Title, for supergroups, channels and group chats
    :type  title: str
    
    :param username: Optional. Username, for private chats, supergroups and channels if available
    :type  username: str
    
    :param first_name: Optional. First name of the other party in a private chat
    :type  first_name: str
    
    :param last_name: Optional. Last name of the other party in a private chat
    :type  last_name: str
    
    :param all_members_are_administrators: Optional. True if a group has ‘All Members Are Admins’ enabled.
    :type  all_members_are_administrators: bool
    
    :param photo: Optional. Chat photo. Returned only in getChat.
    :type  photo: pytgbot.api_types.receivable.media.ChatPhoto
    
    :param description: Optional. Description, for supergroups and channel chats. Returned only in getChat.
    :type  description: str
    
    :param invite_link: Optional. Chat invite link, for supergroups and channel chats. Returned only in getChat.
    :type  invite_link: str
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, type, title=None, username=None, first_name=None, last_name=None, all_members_are_administrators=None, photo=None, description=None, invite_link=None, _raw=None):
        """
        This object represents a chat.

        https://core.telegram.org/bots/api#chat


        Parameters:

        :param id: Unique identifier for this chat. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier
        :type  id: int

        :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
        :type  type: str


        Optional keyword parameters:

        :param title: Optional. Title, for supergroups, channels and group chats
        :type  title: str

        :param username: Optional. Username, for private chats, supergroups and channels if available
        :type  username: str

        :param first_name: Optional. First name of the other party in a private chat
        :type  first_name: str

        :param last_name: Optional. Last name of the other party in a private chat
        :type  last_name: str
        
        :param all_members_are_administrators: Optional. True if a group has ‘All Members Are Admins’ enabled.
        :type  all_members_are_administrators: bool
        
        :param photo: Optional. Chat photo. Returned only in getChat.
        :type  photo: pytgbot.api_types.receivable.media.ChatPhoto
        
        :param description: Optional. Description, for supergroups and channel chats. Returned only in getChat.
        :type  description: str
        
        :param invite_link: Optional. Chat invite link, for supergroups and channel chats. Returned only in getChat.
        :type  invite_link: str
        
        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Chat, self).__init__()
        from pytgbot.api_types.receivable.media import ChatPhoto

        assert (id is not None)
        assert (isinstance(id, int))
        self.id = id

        assert (type is not None)
        assert (isinstance(type, str))
        self.type = type

        assert (title is None or isinstance(title, str))
        self.title = title

        assert (username is None or isinstance(username, str))
        self.username = username

        assert (first_name is None or isinstance(first_name, str))
        self.first_name = first_name

        assert (last_name is None or isinstance(last_name, str))
        self.last_name = last_name
        
        assert (all_members_are_administrators is None or isinstance(all_members_are_administrators, bool))
        self.all_members_are_administrators = all_members_are_administrators

        assert (photo is None or isinstance(photo, ChatPhoto))
        self.photo = photo

        assert (description is None or isinstance(description, str))
        self.description = description

        assert (invite_link is None or isinstance(invite_link, str))
        self.invite_link = invite_link

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
        if self.photo is not None:
            array['photo'] = self.photo.to_array()  # type ChatPhoto
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.invite_link is not None:
            array['invite_link'] = str(self.invite_link)  # type str
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
        assert(isinstance(array, dict))
        from pytgbot.api_types.receivable.media import ChatPhoto

        data = {}
        data['id'] = int(array.get('id'))
        data['type'] = str(array.get('type'))
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['username'] = str(array.get('username')) if array.get('username') is not None else None
        data['first_name'] = str(array.get('first_name')) if array.get('first_name') is not None else None
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        data['all_members_are_administrators'] = bool(array.get('all_members_are_administrators')) if array.get('all_members_are_administrators') is not None else None
        data['photo'] = ChatPhoto.from_array(array.get('photo')) if array.get('photo') is not None else None
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['invite_link'] = str(array.get('invite_link')) if array.get('invite_link') is not None else None
        data['_raw'] = array
        return Chat(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chat_instance)`
        """
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, all_members_are_administrators={self.all_members_are_administrators!r}, photo={self.photo!r}, description={self.description!r}, invite_link={self.invite_link!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chat_instance)`
        """
        if self._raw:
            return "Chat.from_array({self._raw})".format(self=self)
        # end if
        return "Chat(id={self.id!r}, type={self.type!r}, title={self.title!r}, username={self.username!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, all_members_are_administrators={self.all_members_are_administrators!r}, photo={self.photo!r}, description={self.description!r}, invite_link={self.invite_link!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chat_instance`
        """
        return key in ["id", "type", "title", "username", "first_name", "last_name", "all_members_are_administrators", "photo", "description", "invite_link"] and hasattr(self, key) and getattr(self, key)
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
    :type  status: str
    

    Optional keyword parameters:
    
    :param until_date: Optional. Restictred and kicked only. Date when restrictions will be lifted for this user, unix time
    :type  until_date: int
    
    :param can_be_edited: Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
    :type  can_be_edited: bool
    
    :param can_change_info: Optional. Administrators only. True, if the administrator can change the chat title, photo and other settings
    :type  can_change_info: bool
    
    :param can_post_messages: Optional. Administrators only. True, if the administrator can post in the channel, channels only
    :type  can_post_messages: bool
    
    :param can_edit_messages: Optional. Administrators only. True, if the administrator can edit messages of other users, channels only
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
        :type  status: str
        
    
        Optional keyword parameters:
        
        :param until_date: Optional. Restictred and kicked only. Date when restrictions will be lifted for this user, unix time
        :type  until_date: int
        
        :param can_be_edited: Optional. Administrators only. True, if the bot is allowed to edit administrator privileges of that user
        :type  can_be_edited: bool
        
        :param can_change_info: Optional. Administrators only. True, if the administrator can change the chat title, photo and other settings
        :type  can_change_info: bool
        
        :param can_post_messages: Optional. Administrators only. True, if the administrator can post in the channel, channels only
        :type  can_post_messages: bool
        
        :param can_edit_messages: Optional. Administrators only. True, if the administrator can edit messages of other users, channels only
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

        assert (user is not None)
        assert (isinstance(user, User))
        self.user = user

        assert (status is not None)
        assert (isinstance(status, str))
        self.status = status

        assert (until_date is None or isinstance(until_date, int))
        self.until_date = until_date

        assert (can_be_edited is None or isinstance(can_be_edited, bool))
        self.can_be_edited = can_be_edited

        assert (can_change_info is None or isinstance(can_change_info, bool))
        self.can_change_info = can_change_info

        assert (can_post_messages is None or isinstance(can_post_messages, bool))
        self.can_post_messages = can_post_messages

        assert (can_edit_messages is None or isinstance(can_edit_messages, bool))
        self.can_edit_messages = can_edit_messages

        assert (can_delete_messages is None or isinstance(can_delete_messages, bool))
        self.can_delete_messages = can_delete_messages

        assert (can_invite_users is None or isinstance(can_invite_users, bool))
        self.can_invite_users = can_invite_users

        assert (can_restrict_members is None or isinstance(can_restrict_members, bool))
        self.can_restrict_members = can_restrict_members

        assert (can_pin_messages is None or isinstance(can_pin_messages, bool))
        self.can_pin_messages = can_pin_messages

        assert (can_promote_members is None or isinstance(can_promote_members, bool))
        self.can_promote_members = can_promote_members

        assert (can_send_messages is None or isinstance(can_send_messages, bool))
        self.can_send_messages = can_send_messages

        assert (can_send_media_messages is None or isinstance(can_send_media_messages, bool))
        self.can_send_media_messages = can_send_media_messages

        assert (can_send_other_messages is None or isinstance(can_send_other_messages, bool))
        self.can_send_other_messages = can_send_other_messages

        assert (can_add_web_page_previews is None or isinstance(can_add_web_page_previews, bool))
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
        array['status'] = str(self.status)  # type str
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
        assert(isinstance(array, dict))

        data = {}
        data['user'] = User.from_array(array.get('user'))
        data['status'] = str(array.get('status'))
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
        return key in ["user", "status", "until_date", "can_be_edited", "can_change_info", "can_post_messages", "can_edit_messages", "can_delete_messages", "can_invite_users", "can_restrict_members", "can_pin_messages", "can_promote_members", "can_send_messages", "can_send_media_messages", "can_send_other_messages", "can_add_web_page_previews"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class ChatMember
