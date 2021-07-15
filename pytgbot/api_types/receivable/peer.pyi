# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.peer import ChatMember
from pytgbot.api_types.receivable.peer import Peer

__author__ = 'luckydonald'


class Peer(Result):
    """
    parent class for both users and chats.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
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
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool
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

    :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
    :type  invite_link: str|unicode

    :param pinned_message: Optional. The most recent pinned message (by sending date). Returned only in getChat.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message

    :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    :type  permissions: pytgbot.api_types.receivable.peer.ChatPermissions

    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
    :type  slow_mode_delay: int

    :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
    :type  message_auto_delete_time: int

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
    id: int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
    photo: ChatPhoto
    bio: str
    description: str
    invite_link: str
    pinned_message: Message
    permissions: ChatPermissions
    slow_mode_delay: int
    message_auto_delete_time: int
    sticker_set_name: str
    can_set_sticker_set: bool
    linked_chat_id: int
    location: ChatLocation
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

    :param is_primary: True, if the link is primary
    :type  is_primary: bool

    :param is_revoked: True, if the link is revoked
    :type  is_revoked: bool


    Optional keyword parameters:

    :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been expired
    :type  expire_date: int

    :param member_limit: Optional. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    :type  member_limit: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    invite_link: str
    creator: User
    is_primary: bool
    is_revoked: bool
    expire_date: int
    member_limit: int
# end class ChatInviteLink

class ChatMember(Result):
    """
    This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:

    https://core.telegram.org/bots/api#chatmember

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
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

    :param custom_title: Optional. Custom title for this user
    :type  custom_title: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    status: str
    user: User
    is_anonymous: bool
    custom_title: str
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

    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :type  can_post_messages: bool

    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin messages; channels only
    :type  can_edit_messages: bool

    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :type  can_pin_messages: bool

    :param custom_title: Optional. Custom title for this user
    :type  custom_title: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    status: str
    user: User
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_voice_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_pin_messages: bool
    custom_title: str
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
    status: str
    user: User
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
    status: str
    user: User
    is_member: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    until_date: int
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
    status: str
    user: User
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
    status: str
    user: User
    until_date: int
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
    chat: Chat
    from_peer: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink
# end class ChatMemberUpdated

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
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
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
    location: Location
    address: str
# end class ChatLocation
