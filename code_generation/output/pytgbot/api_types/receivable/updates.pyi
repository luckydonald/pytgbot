# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Receivable
from pytgbot.api_types.receivable.updates import UpdateType

__author__ = 'luckydonald'


class UpdateType(Receivable):
    """
    All extending classes are an property of the Update type.
    Like Message: Update.message

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class UpdateType

class CallbackGame(UpdateType):
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.

    https://core.telegram.org/bots/api#callbackgame

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class CallbackGame

class Update(Receivable):
    """
    This object represents an incoming update.At most one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update
    

    Parameters:
    
    :param update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    :type  update_id: int
    

    Optional keyword parameters:
    
    :param message: Optional. New incoming message of any kind — text, photo, sticker, etc.
    :type  message: pytgbot.api_types.receivable.updates.Message
    
    :param edited_message: Optional. New version of a message that is known to the bot and was edited
    :type  edited_message: pytgbot.api_types.receivable.updates.Message
    
    :param channel_post: Optional. New incoming channel post of any kind — text, photo, sticker, etc.
    :type  channel_post: pytgbot.api_types.receivable.updates.Message
    
    :param edited_channel_post: Optional. New version of a channel post that is known to the bot and was edited
    :type  edited_channel_post: pytgbot.api_types.receivable.updates.Message
    
    :param inline_query: Optional. New incoming inline query
    :type  inline_query: pytgbot.api_types.receivable.inline.InlineQuery
    
    :param chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
    :type  chosen_inline_result: pytgbot.api_types.receivable.inline.ChosenInlineResult
    
    :param callback_query: Optional. New incoming callback query
    :type  callback_query: pytgbot.api_types.receivable.updates.CallbackQuery
    
    :param shipping_query: Optional. New incoming shipping query. Only for invoices with flexible price
    :type  shipping_query: pytgbot.api_types.receivable.payments.ShippingQuery
    
    :param pre_checkout_query: Optional. New incoming pre-checkout query. Contains full information about checkout
    :type  pre_checkout_query: pytgbot.api_types.receivable.payments.PreCheckoutQuery
    
    :param poll: Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
    :type  poll: pytgbot.api_types.receivable.media.Poll
    
    :param poll_answer: Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    :type  poll_answer: pytgbot.api_types.receivable.media.PollAnswer
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    update_id: int
    message: Message
    edited_message: Message
    channel_post: Message
    edited_channel_post: Message
    inline_query: InlineQuery
    chosen_inline_result: ChosenInlineResult
    callback_query: CallbackQuery
    shipping_query: ShippingQuery
    pre_checkout_query: PreCheckoutQuery
    poll: Poll
    poll_answer: PollAnswer
# end class Update

class WebhookInfo(Receivable):
    """
    Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    

    Parameters:
    
    :param url: Webhook URL, may be empty if webhook is not set up
    :type  url: str|unicode
    
    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    :type  has_custom_certificate: bool
    
    :param pending_update_count: Number of updates awaiting delivery
    :type  pending_update_count: int
    

    Optional keyword parameters:
    
    :param ip_address: Optional. Currently used webhook IP address
    :type  ip_address: str|unicode
    
    :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
    :type  last_error_date: int
    
    :param last_error_message: Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    :type  last_error_message: str|unicode
    
    :param max_connections: Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    :type  max_connections: int
    
    :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update types
    :type  allowed_updates: list of str|unicode
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: str
    last_error_date: int
    last_error_message: str
    max_connections: int
    allowed_updates: List[str]
# end class WebhookInfo

class Message(UpdateType):
    """
    This object represents a message.

    https://core.telegram.org/bots/api#message
    

    Parameters:
    
    :param message_id: Unique message identifier inside this chat
    :type  message_id: int
    
    :param date: Date the message was sent in Unix time
    :type  date: int
    
    :param chat: Conversation the message belongs to
    :type  chat: pytgbot.api_types.receivable.peer.Chat
    

    Optional keyword parameters:
    
    :param from_peer: Optional. Sender, empty for messages sent to channels
    :type  from_peer: pytgbot.api_types.receivable.peer.User
    
    :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group
    :type  sender_chat: pytgbot.api_types.receivable.peer.Chat
    
    :param forward_from: Optional. For forwarded messages, sender of the original message
    :type  forward_from: pytgbot.api_types.receivable.peer.User
    
    :param forward_from_chat: Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
    :type  forward_from_chat: pytgbot.api_types.receivable.peer.Chat
    
    :param forward_from_message_id: Optional. For messages forwarded from channels, identifier of the original message in the channel
    :type  forward_from_message_id: int
    
    :param forward_signature: Optional. For messages forwarded from channels, signature of the post author if present
    :type  forward_signature: str|unicode
    
    :param forward_sender_name: Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    :type  forward_sender_name: str|unicode
    
    :param forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
    :type  forward_date: int
    
    :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    :type  reply_to_message: pytgbot.api_types.receivable.updates.Message
    
    :param via_bot: Optional. Bot through which the message was sent
    :type  via_bot: pytgbot.api_types.receivable.peer.User
    
    :param edit_date: Optional. Date the message was last edited in Unix time
    :type  edit_date: int
    
    :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
    :type  media_group_id: str|unicode
    
    :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
    :type  author_signature: str|unicode
    
    :param text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    :type  text: str|unicode
    
    :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    :type  entities: list of pytgbot.api_types.receivable.media.MessageEntity
    
    :param animation: Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    :type  animation: pytgbot.api_types.receivable.media.Animation
    
    :param audio: Optional. Message is an audio file, information about the file
    :type  audio: pytgbot.api_types.receivable.media.Audio
    
    :param document: Optional. Message is a general file, information about the file
    :type  document: pytgbot.api_types.receivable.media.Document
    
    :param photo: Optional. Message is a photo, available sizes of the photo
    :type  photo: list of pytgbot.api_types.receivable.media.PhotoSize
    
    :param sticker: Optional. Message is a sticker, information about the sticker
    :type  sticker: pytgbot.api_types.receivable.media.Sticker
    
    :param video: Optional. Message is a video, information about the video
    :type  video: pytgbot.api_types.receivable.media.Video
    
    :param video_note: Optional. Message is a video note, information about the video message
    :type  video_note: pytgbot.api_types.receivable.media.VideoNote
    
    :param voice: Optional. Message is a voice message, information about the file
    :type  voice: pytgbot.api_types.receivable.media.Voice
    
    :param caption: Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    :type  caption: str|unicode
    
    :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    
    :param contact: Optional. Message is a shared contact, information about the contact
    :type  contact: pytgbot.api_types.receivable.media.Contact
    
    :param dice: Optional. Message is a dice with random value from 1 to 6
    :type  dice: pytgbot.api_types.receivable.media.Dice
    
    :param game: Optional. Message is a game, information about the game. More about games »
    :type  game: pytgbot.api_types.receivable.media.Game
    
    :param poll: Optional. Message is a native poll, information about the poll
    :type  poll: pytgbot.api_types.receivable.media.Poll
    
    :param venue: Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    :type  venue: pytgbot.api_types.receivable.media.Venue
    
    :param location: Optional. Message is a shared location, information about the location
    :type  location: pytgbot.api_types.receivable.media.Location
    
    :param new_chat_members: Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    :type  new_chat_members: list of pytgbot.api_types.receivable.peer.User
    
    :param left_chat_member: Optional. A member was removed from the group, information about them (this member may be the bot itself)
    :type  left_chat_member: pytgbot.api_types.receivable.peer.User
    
    :param new_chat_title: Optional. A chat title was changed to this value
    :type  new_chat_title: str|unicode
    
    :param new_chat_photo: Optional. A chat photo was change to this value
    :type  new_chat_photo: list of pytgbot.api_types.receivable.media.PhotoSize
    
    :param delete_chat_photo: Optional. Service message: the chat photo was deleted
    :type  delete_chat_photo: bool
    
    :param group_chat_created: Optional. Service message: the group has been created
    :type  group_chat_created: bool
    
    :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    :type  supergroup_chat_created: bool
    
    :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    :type  channel_chat_created: bool
    
    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  migrate_to_chat_id: int
    
    :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  migrate_from_chat_id: int
    
    :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message
    
    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    :type  invoice: pytgbot.api_types.receivable.payments.Invoice
    
    :param successful_payment: Optional. Message is a service message about a successful payment, information about the payment. More about payments »
    :type  successful_payment: pytgbot.api_types.receivable.payments.SuccessfulPayment
    
    :param connected_website: Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
    :type  connected_website: str|unicode
    
    :param passport_data: Optional. Telegram Passport data
    :type  passport_data: pytgbot.api_types.receivable.passport.PassportData
    
    :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    :type  proximity_alert_triggered: pytgbot.api_types.receivable.media.ProximityAlertTriggered
    
    :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    message_id: int
    date: int
    chat: Chat
    from_peer: User
    sender_chat: Chat
    forward_from: User
    forward_from_chat: Chat
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    reply_to_message: Message
    via_bot: User
    edit_date: int
    media_group_id: str
    author_signature: str
    text: str
    entities: List[MessageEntity]
    animation: Animation
    audio: Audio
    document: Document
    photo: List[PhotoSize]
    sticker: Sticker
    video: Video
    video_note: VideoNote
    voice: Voice
    caption: str
    caption_entities: List[MessageEntity]
    contact: Contact
    dice: Dice
    game: Game
    poll: Poll
    venue: Venue
    location: Location
    new_chat_members: List[User]
    left_chat_member: User
    new_chat_title: str
    new_chat_photo: List[PhotoSize]
    delete_chat_photo: bool
    group_chat_created: bool
    supergroup_chat_created: bool
    channel_chat_created: bool
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: Message
    invoice: Invoice
    successful_payment: SuccessfulPayment
    connected_website: str
    passport_data: PassportData
    proximity_alert_triggered: ProximityAlertTriggered
    reply_markup: InlineKeyboardMarkup
# end class Message

class CallbackQuery(UpdateType):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    NOTE: After the user presses a callback button, Telegram clients will display a progress bar until you call answerCallbackQuery. It is, therefore, necessary to react by calling answerCallbackQuery even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

    https://core.telegram.org/bots/api#callbackquery
    

    Parameters:
    
    :param id: Unique identifier for this query
    :type  id: str|unicode
    
    :param from_peer: Sender
    :type  from_peer: pytgbot.api_types.receivable.peer.User
    
    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
    :type  chat_instance: str|unicode
    

    Optional keyword parameters:
    
    :param message: Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    :type  message: pytgbot.api_types.receivable.updates.Message
    
    :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
    :type  inline_message_id: str|unicode
    
    :param data: Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
    :type  data: str|unicode
    
    :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    :type  game_short_name: str|unicode
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    id: str
    from_peer: User
    chat_instance: str
    message: Message
    inline_message_id: str
    data: str
    game_short_name: str
# end class CallbackQuery

class ResponseParameters(Receivable):
    """
    Contains information about why a request was unsuccessful.

    https://core.telegram.org/bots/api#responseparameters

    Optional keyword parameters:
    
    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  migrate_to_chat_id: int
    
    :param retry_after: Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    :type  retry_after: int
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    migrate_to_chat_id: int
    retry_after: int
# end class ResponseParameters
