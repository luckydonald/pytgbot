# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.peer import Peer

__author__ = 'luckydonald'


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
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str
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
    
    :param description: Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    :type  description: str|unicode
    
    :param invite_link: Optional. Chat invite link, for groups, supergroups and channel chats. Each administrator in a chat generates their own invite links, so the bot must first generate the link using exportChatInviteLink. Returned only in getChat.
    :type  invite_link: str|unicode
    
    :param pinned_message: Optional. Pinned message, for groups, supergroups and channels. Returned only in getChat.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message
    
    :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    :type  permissions: pytgbot.api_types.receivable.peer.ChatPermissions
    
    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user. Returned only in getChat.
    :type  slow_mode_delay: int
    
    :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :type  sticker_set_name: str|unicode
    
    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    :type  can_set_sticker_set: bool
    
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
    description: str
    invite_link: str
    pinned_message: Message
    permissions: ChatPermissions
    slow_mode_delay: int
    sticker_set_name: str
    can_set_sticker_set: bool
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
    
    :param until_date: Optional. Restricted and kicked only. Date when restrictions will be lifted for this user; unix time
    :type  until_date: int
    
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
    
    :param can_promote_members: Optional. Administrators only. True, if the administrator can add new administrators with a subset of his own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
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
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    user: User
    status: str
    custom_title: str
    until_date: int
    can_be_edited: bool
    can_post_messages: bool
    can_edit_messages: bool
    can_delete_messages: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    is_member: bool
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
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
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
# end class ChatPermissions
