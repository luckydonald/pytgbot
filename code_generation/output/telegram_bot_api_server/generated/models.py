# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from pydantic import BaseModel
from typing import Any, Union, List, Optional

__author__ = 'luckydonald'

__all__ = [
    'MediaModel', 'ServiceMessageModel', 'PeerModel', 'UpdateTypeModel', 'CallbackGameModel', 'InlineQueryResultModel', 'InlineQueryCachedResultModel', 'InputMessageContentModel', 'InputMediaModel', 'InputMediaWithThumbModel', 'InputMediaPlayableModel', 'InputMediaVideolikeModel', 'PassportElementErrorModel', 'ButtonModel', 'ReplyMarkupModel', 'ReceivableModel', 'SendableModel', 'ResultModel', 'TgBotApiObjectModel', 'UpdateModel', 'WebhookInfoModel', 'UserModel', 'ChatModel', 'MessageModel', 'MessageIdModel', 'MessageEntityModel', 'PhotoSizeModel', 'AnimationModel', 'AudioModel', 'DocumentModel', 'VideoModel', 'VideoNoteModel', 'VoiceModel', 'ContactModel', 'DiceModel', 'PollOptionModel', 'PollAnswerModel', 'PollModel', 'LocationModel', 'VenueModel', 'ProximityAlertTriggeredModel', 'MessageAutoDeleteTimerChangedModel', 'VoiceChatEndedModel', 'VoiceChatParticipantsInvitedModel', 'UserProfilePhotosModel', 'FileModel', 'ReplyKeyboardMarkupModel', 'KeyboardButtonModel', 'KeyboardButtonPollTypeModel', 'ReplyKeyboardRemoveModel', 'InlineKeyboardMarkupModel', 'InlineKeyboardButtonModel', 'LoginUrlModel', 'CallbackQueryModel', 'ForceReplyModel', 'ChatPhotoModel', 'ChatInviteLinkModel', 'ChatMemberModel', 'ChatMemberUpdatedModel', 'ChatPermissionsModel', 'ChatLocationModel', 'BotCommandModel', 'ResponseParametersModel', 'InputMediaPhotoModel', 'InputMediaVideoModel', 'InputMediaAnimationModel', 'InputMediaAudioModel', 'InputMediaDocumentModel', 'StickerModel', 'StickerSetModel', 'MaskPositionModel', 'InlineQueryModel', 'InlineQueryResultArticleModel', 'InlineQueryResultPhotoModel', 'InlineQueryResultGifModel', 'InlineQueryResultMpeg4GifModel', 'InlineQueryResultVideoModel', 'InlineQueryResultAudioModel', 'InlineQueryResultVoiceModel', 'InlineQueryResultDocumentModel', 'InlineQueryResultLocationModel', 'InlineQueryResultVenueModel', 'InlineQueryResultContactModel', 'InlineQueryResultGameModel', 'InlineQueryResultCachedPhotoModel', 'InlineQueryResultCachedGifModel', 'InlineQueryResultCachedMpeg4GifModel', 'InlineQueryResultCachedStickerModel', 'InlineQueryResultCachedDocumentModel', 'InlineQueryResultCachedVideoModel', 'InlineQueryResultCachedVoiceModel', 'InlineQueryResultCachedAudioModel', 'InputTextMessageContentModel', 'InputLocationMessageContentModel', 'InputVenueMessageContentModel', 'InputContactMessageContentModel', 'ChosenInlineResultModel', 'LabeledPriceModel', 'InvoiceModel', 'ShippingAddressModel', 'OrderInfoModel', 'ShippingOptionModel', 'SuccessfulPaymentModel', 'ShippingQueryModel', 'PreCheckoutQueryModel', 'PassportDataModel', 'PassportFileModel', 'EncryptedPassportElementModel', 'EncryptedCredentialsModel', 'PassportElementErrorDataFieldModel', 'PassportElementErrorFrontSideModel', 'PassportElementErrorReverseSideModel', 'PassportElementErrorSelfieModel', 'PassportElementErrorFileModel', 'PassportElementErrorFilesModel', 'PassportElementErrorTranslationFileModel', 'PassportElementErrorTranslationFilesModel', 'PassportElementErrorUnspecifiedModel', 'GameModel', 'GameHighScoreModel',
]

FAST_API_ISSUE_884_IS_FIXED = False


if FAST_API_ISSUE_884_IS_FIXED:
    from pydantic import Json

    def parse_obj_as(_, obj, *__, **___):
        """
        we don't need any additional parsing as fastapi now does that correctly
        """
        return obj
    # end def
else:
    class __JsonWrapper:
        from pydantic import Json

        def __getitem__(self, item):
            """ Basically throw away `[Type]` when used like `Json[Type]` """
            return self.Json
        # end def
    # end def
    Json = __JsonWrapper()  # so Json[Type] does call Json.__getitem__(self, item=Type)

    from pydantic import parse_obj_as
# end if




class MediaModel(BaseModel):  # Receivable"""parent class for all receivable media.
    """

# end class Media


class ServiceMessageModel(BaseModel):  # ServiceMessage"""parent class for all service messages, those are not directly media related special attributes of the Message object.
    """

# end class ServiceMessage


class PeerModel(BaseModel):  # Result"""parent class for both users and chats.
    """

# end class Peer


class UpdateTypeModel(BaseModel):  # Receivable"""All extending classes are an property of the Update type.
    Like Message: Update.message
    """

# end class UpdateType


class CallbackGameModel(BaseModel):  # UpdateType"""A placeholder, currently holds no information. Use BotFather to set up your game.

    https://core.telegram.org/bots/api#callbackgame
    """

# end class CallbackGame


class InlineQueryResultModel(BaseModel):  # Sendable"""This object represents one result of an inline query.

    Telegram clients currently support results of 20 types.

    https://core.telegram.org/bots/api#inlinequeryresult
    """

# end class InlineQueryResult


class InlineQueryCachedResultModel(BaseModel):  # InlineQueryResult"""Parent class of all those cached inline results.
    """

# end class InlineQueryCachedResult


class InputMessageContentModel(BaseModel):  # Sendable"""Parent class of all those input message content.
    """

# end class InputMessageContent


class InputMediaModel(BaseModel):  # Sendable"""This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia
    """

    type: str
    media: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
# end class InputMedia


class InputMediaWithThumbModel(BaseModel):  # InputMedia"""This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia
    """

    type: str
    media: str
    thumb: Union['InputFileModel', str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
# end class InputMediaWithThumb


class InputMediaPlayableModel(BaseModel):  # InputMediaWithThumb"""This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia
    """

    type: str
    media: str
    thumb: Union['InputFileModel', str]
    duration: Optional[int]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
# end class InputMediaPlayable


class InputMediaVideolikeModel(BaseModel):  # InputMediaPlayable"""This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia
    """

    type: str
    media: str
    thumb: Union['InputFileModel', str]
    duration: Optional[int]
    width: Optional[int]
    height: Optional[int]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
# end class InputMediaVideolike


class PassportElementErrorModel(BaseModel):  # Sendable"""This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user.

    https://core.telegram.org/bots/api#inputmedia
    """

# end class PassportElementError


class ButtonModel(BaseModel):  # Sendable"""Class for grouping KeyboardButton, KeyboardButtonPollType and InlineKeyboardButton.
    """

# end class Button


class ReplyMarkupModel(BaseModel):  # Sendable"""Class for grouping ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup and ForceReply.
    """

# end class ReplyMarkup


class ReceivableModel(BaseModel):  # TgBotApiObject"""Base class for all classes for stuff which telegram sends us.
    """

# end class Receivable


class SendableModel(BaseModel):  # TgBotApiObject"""Base class for all classes for stuff which we throw in requests towards the telegram servers.
    """

# end class Sendable


class ResultModel(BaseModel):  # Receivable"""Base class for all classes for stuff which we throw in requests towards the telegram servers.
    """

# end class Result


class TgBotApiObjectModel(BaseModel):  # object"""Base class for every api object class.
    """

# end class TgBotApiObject


class UpdateModel(BaseModel):  # Receivable"""This object represents an incoming update.At most one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update
    """

    update_id: int
    message: Optional['MessageModel']
    edited_message: Optional['MessageModel']
    channel_post: Optional['MessageModel']
    edited_channel_post: Optional['MessageModel']
    inline_query: Optional['InlineQueryModel']
    chosen_inline_result: Optional['ChosenInlineResultModel']
    callback_query: Optional['CallbackQueryModel']
    shipping_query: Optional['ShippingQueryModel']
    pre_checkout_query: Optional['PreCheckoutQueryModel']
    poll: Optional['PollModel']
    poll_answer: Optional['PollAnswerModel']
    my_chat_member: Optional['ChatMemberUpdatedModel']
    chat_member: Optional['ChatMemberUpdatedModel']
# end class Update


class WebhookInfoModel(BaseModel):  # Receivable"""Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    """

    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: Optional[str]
    last_error_date: Optional[int]
    last_error_message: Optional[str]
    max_connections: Optional[int]
    allowed_updates: Optional[List[str]]
# end class WebhookInfo


class UserModel(BaseModel):  # Peer"""This object represents a Telegram user or bot.

    https://core.telegram.org/bots/api#user
    """

    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str]
    username: Optional[str]
    language_code: Optional[str]
    can_join_groups: Optional[bool]
    can_read_all_group_messages: Optional[bool]
    supports_inline_queries: Optional[bool]
# end class User


class ChatModel(BaseModel):  # Peer"""This object represents a chat.

    https://core.telegram.org/bots/api#chat
    """

    id: int
    type: str
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    photo: Optional['ChatPhotoModel']
    bio: Optional[str]
    description: Optional[str]
    invite_link: Optional[str]
    pinned_message: Optional['MessageModel']
    permissions: Optional['ChatPermissionsModel']
    slow_mode_delay: Optional[int]
    message_auto_delete_time: Optional[int]
    sticker_set_name: Optional[str]
    can_set_sticker_set: Optional[bool]
    linked_chat_id: Optional[int]
    location: Optional['ChatLocationModel']
# end class Chat


class MessageModel(BaseModel):  # UpdateType"""This object represents a message.

    https://core.telegram.org/bots/api#message
    """

    message_id: int
    date: int
    chat: 'ChatModel'
    from_peer: Optional['UserModel']
    sender_chat: Optional['ChatModel']
    forward_from: Optional['UserModel']
    forward_from_chat: Optional['ChatModel']
    forward_from_message_id: Optional[int]
    forward_signature: Optional[str]
    forward_sender_name: Optional[str]
    forward_date: Optional[int]
    reply_to_message: Optional['MessageModel']
    via_bot: Optional['UserModel']
    edit_date: Optional[int]
    media_group_id: Optional[str]
    author_signature: Optional[str]
    text: Optional[str]
    entities: Optional[List['MessageEntityModel']]
    animation: Optional['AnimationModel']
    audio: Optional['AudioModel']
    document: Optional['DocumentModel']
    photo: Optional[List['PhotoSizeModel']]
    sticker: Optional['StickerModel']
    video: Optional['VideoModel']
    video_note: Optional['VideoNoteModel']
    voice: Optional['VoiceModel']
    caption: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    contact: Optional['ContactModel']
    dice: Optional['DiceModel']
    game: Optional['GameModel']
    poll: Optional['PollModel']
    venue: Optional['VenueModel']
    location: Optional['LocationModel']
    new_chat_members: Optional[List['UserModel']]
    left_chat_member: Optional['UserModel']
    new_chat_title: Optional[str]
    new_chat_photo: Optional[List['PhotoSizeModel']]
    delete_chat_photo: Optional[bool]
    group_chat_created: Optional[bool]
    supergroup_chat_created: Optional[bool]
    channel_chat_created: Optional[bool]
    message_auto_delete_timer_changed: Optional['MessageAutoDeleteTimerChangedModel']
    migrate_to_chat_id: Optional[int]
    migrate_from_chat_id: Optional[int]
    pinned_message: Optional['MessageModel']
    invoice: Optional['InvoiceModel']
    successful_payment: Optional['SuccessfulPaymentModel']
    connected_website: Optional[str]
    passport_data: Optional['PassportDataModel']
    proximity_alert_triggered: Optional['ProximityAlertTriggeredModel']
    voice_chat_started: Optional['VoiceChatStartedModel']
    voice_chat_ended: Optional['VoiceChatEndedModel']
    voice_chat_participants_invited: Optional['VoiceChatParticipantsInvitedModel']
    reply_markup: Optional['InlineKeyboardMarkupModel']
# end class Message


class MessageIdModel(BaseModel):  # Result"""This object represents a unique message identifier.

    https://core.telegram.org/bots/api#messageid
    """

    message_id: int
# end class MessageId


class MessageEntityModel(BaseModel):  # Result"""This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    """

    type: str
    offset: int
    length: int
    url: Optional[str]
    user: Optional['UserModel']
    language: Optional[str]
# end class MessageEntity


class PhotoSizeModel(BaseModel):  # Result"""This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int]
# end class PhotoSize


class AnimationModel(BaseModel):  # Media"""This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    https://core.telegram.org/bots/api#animation
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional['PhotoSizeModel']
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Animation


class AudioModel(BaseModel):  # Media"""This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio
    """

    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str]
    title: Optional[str]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
    thumb: Optional['PhotoSizeModel']
# end class Audio


class DocumentModel(BaseModel):  # Media"""This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document
    """

    file_id: str
    file_unique_id: str
    thumb: Optional['PhotoSizeModel']
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Document


class VideoModel(BaseModel):  # Media"""This object represents a video file.

    https://core.telegram.org/bots/api#video
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional['PhotoSizeModel']
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Video


class VideoNoteModel(BaseModel):  # Media"""This object represents a video message (available in Telegram apps as of v.4.0).

    https://core.telegram.org/bots/api#videonote
    """

    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: Optional['PhotoSizeModel']
    file_size: Optional[int]
# end class VideoNote


class VoiceModel(BaseModel):  # Media"""This object represents a voice note.

    https://core.telegram.org/bots/api#voice
    """

    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Voice


class ContactModel(BaseModel):  # Media"""This object represents a phone contact.

    https://core.telegram.org/bots/api#contact
    """

    phone_number: str
    first_name: str
    last_name: Optional[str]
    user_id: Optional[int]
    vcard: Optional[str]
# end class Contact


class DiceModel(BaseModel):  # Media"""This object represents an animated emoji that displays a random value.

    https://core.telegram.org/bots/api#dice
    """

    emoji: str
    value: int
# end class Dice


class PollOptionModel(BaseModel):  # Receivable"""This object contains information about one answer option in a poll.

    https://core.telegram.org/bots/api#polloption
    """

    text: str
    voter_count: int
# end class PollOption


class PollAnswerModel(BaseModel):  # Receivable"""This object represents an answer of a user in a non-anonymous poll.

    https://core.telegram.org/bots/api#pollanswer
    """

    poll_id: str
    user: 'UserModel'
    option_ids: List[int]
# end class PollAnswer


class PollModel(BaseModel):  # Media"""This object contains information about a poll.

    https://core.telegram.org/bots/api#poll
    """

    id: str
    question: str
    options: List['PollOptionModel']
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: Optional[int]
    explanation: Optional[str]
    explanation_entities: Optional[List['MessageEntityModel']]
    open_period: Optional[int]
    close_date: Optional[int]
# end class Poll


class LocationModel(BaseModel):  # Media"""This object represents a point on the map.

    https://core.telegram.org/bots/api#location
    """

    longitude: float
    latitude: float
    horizontal_accuracy: Optional[float]
    live_period: Optional[int]
    heading: Optional[int]
    proximity_alert_radius: Optional[int]
# end class Location


class VenueModel(BaseModel):  # Media"""This object represents a venue.

    https://core.telegram.org/bots/api#venue
    """

    location: 'LocationModel'
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]
    google_place_id: Optional[str]
    google_place_type: Optional[str]
# end class Venue


class ProximityAlertTriggeredModel(BaseModel):  # ServiceMessage"""This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    https://core.telegram.org/bots/api#proximityalerttriggered
    """

    traveler: 'UserModel'
    watcher: 'UserModel'
    distance: int
# end class ProximityAlertTriggered


class MessageAutoDeleteTimerChangedModel(BaseModel):  # ServiceMessage"""This object represents a service message about a change in auto-delete timer settings.

    https://core.telegram.org/bots/api#messageautodeletetimerchanged
    """

    message_auto_delete_time: int
# end class MessageAutoDeleteTimerChanged


class VoiceChatEndedModel(BaseModel):  # ServiceMessage"""This object represents a service message about a voice chat ended in the chat.

    https://core.telegram.org/bots/api#voicechatended
    """

    duration: int
# end class VoiceChatEnded


class VoiceChatParticipantsInvitedModel(BaseModel):  # ServiceMessage"""This object represents a service message about new members invited to a voice chat.

    https://core.telegram.org/bots/api#voicechatparticipantsinvited
    """

    users: Optional[List['UserModel']]
# end class VoiceChatParticipantsInvited


class UserProfilePhotosModel(BaseModel):  # Result"""This object represent a user's profile pictures.

    https://core.telegram.org/bots/api#userprofilephotos
    """

    total_count: int
    photos: List[List['PhotoSizeModel']]
# end class UserProfilePhotos


class FileModel(BaseModel):  # Receivable"""This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

    Maximum file size to download is 20 MB

    https://core.telegram.org/bots/api#file
    """

    file_id: str
    file_unique_id: str
    file_size: Optional[int]
    file_path: Optional[str]
# end class File


class ReplyKeyboardMarkupModel(BaseModel):  # ReplyMarkup"""This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    https://core.telegram.org/bots/api#replykeyboardmarkup
    """

    keyboard: List[List['KeyboardButtonModel']]
    resize_keyboard: Optional[bool]
    one_time_keyboard: Optional[bool]
    selective: Optional[bool]
# end class ReplyKeyboardMarkup


class KeyboardButtonModel(BaseModel):  # Button"""This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#keyboardbutton
    """

    text: str
    request_contact: Optional[bool]
    request_location: Optional[bool]
    request_poll: Optional['KeyboardButtonPollTypeModel']
# end class KeyboardButton


class KeyboardButtonPollTypeModel(BaseModel):  # Button"""This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    https://core.telegram.org/bots/api#keyboardbuttonpolltype
    """

    type: Optional[str]
# end class KeyboardButtonPollType


class ReplyKeyboardRemoveModel(BaseModel):  # ReplyMarkup"""Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardremove
    """

    remove_keyboard: bool
    selective: Optional[bool]
# end class ReplyKeyboardRemove


class InlineKeyboardMarkupModel(BaseModel):  # ReplyMarkup"""This object represents an inline keyboard that appears right next to the message it belongs to.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """

    inline_keyboard: List[List['InlineKeyboardButtonModel']]
# end class InlineKeyboardMarkup


class InlineKeyboardButtonModel(BaseModel):  # Button"""This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """

    text: str
    url: Optional[str]
    login_url: Optional['LoginUrlModel']
    callback_data: Optional[str]
    switch_inline_query: Optional[str]
    switch_inline_query_current_chat: Optional[str]
    callback_game: Optional['CallbackGameModel']
    pay: Optional[bool]
# end class InlineKeyboardButton


class LoginUrlModel(BaseModel):  # Sendable"""This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.

    Sample bot: @discussbot

    https://core.telegram.org/bots/api#loginurl
    """

    url: str
    forward_text: Optional[str]
    bot_username: Optional[str]
    request_write_access: Optional[bool]
# end class LoginUrl


class CallbackQueryModel(BaseModel):  # UpdateType"""This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    NOTE: After the user presses a callback button, Telegram clients will display a progress bar until you call answerCallbackQuery. It is, therefore, necessary to react by calling answerCallbackQuery even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

    https://core.telegram.org/bots/api#callbackquery
    """

    id: str
    from_peer: 'UserModel'
    chat_instance: str
    message: Optional['MessageModel']
    inline_message_id: Optional[str]
    data: Optional[str]
    game_short_name: Optional[str]
# end class CallbackQuery


class ForceReplyModel(BaseModel):  # ReplyMarkup"""Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions). There could be two ways to create a new poll:

    Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2). May be appealing for hardcore users but lacks modern day polish.
    Guide the user through a step-by-step process. 'Please send me your question', 'Cool, now let's add the first answer option', 'Great. Keep adding answer options, then send /done when you're ready'.

    The last option is definitely more attractive. And if you use ForceReply in your bot's questions, it will receive the user's answers even if it only receives replies, commands and mentions — without any extra work for the user.

    https://core.telegram.org/bots/api#forcereply
    """

    force_reply: bool
    selective: Optional[bool]
# end class ForceReply


class ChatPhotoModel(BaseModel):  # Result"""This object represents a chat photo.

    https://core.telegram.org/bots/api#chatphoto
    """

    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str
# end class ChatPhoto


class ChatInviteLinkModel(BaseModel):  # Result"""Represents an invite link for a chat.

    https://core.telegram.org/bots/api#chatinvitelink
    """

    invite_link: str
    creator: 'UserModel'
    is_primary: bool
    is_revoked: bool
    expire_date: Optional[int]
    member_limit: Optional[int]
# end class ChatInviteLink


class ChatMemberModel(BaseModel):  # Result"""This object contains information about one member of a chat.

    https://core.telegram.org/bots/api#chatmember
    """

    user: 'UserModel'
    status: str
    custom_title: Optional[str]
    is_anonymous: Optional[bool]
    can_be_edited: Optional[bool]
    can_manage_chat: Optional[bool]
    can_post_messages: Optional[bool]
    can_edit_messages: Optional[bool]
    can_delete_messages: Optional[bool]
    can_manage_voice_chats: Optional[bool]
    can_restrict_members: Optional[bool]
    can_promote_members: Optional[bool]
    can_change_info: Optional[bool]
    can_invite_users: Optional[bool]
    can_pin_messages: Optional[bool]
    is_member: Optional[bool]
    can_send_messages: Optional[bool]
    can_send_media_messages: Optional[bool]
    can_send_polls: Optional[bool]
    can_send_other_messages: Optional[bool]
    can_add_web_page_previews: Optional[bool]
    until_date: Optional[int]
# end class ChatMember


class ChatMemberUpdatedModel(BaseModel):  # Result"""This object represents changes in the status of a chat member.

    https://core.telegram.org/bots/api#chatmemberupdated
    """

    chat: 'ChatModel'
    from_peer: 'UserModel'
    date: int
    old_chat_member: 'ChatMemberModel'
    new_chat_member: 'ChatMemberModel'
    invite_link: Optional['ChatInviteLinkModel']
# end class ChatMemberUpdated


class ChatPermissionsModel(BaseModel):  # Result"""Describes actions that a non-administrator user is allowed to take in a chat.

    https://core.telegram.org/bots/api#chatpermissions
    """

    can_send_messages: Optional[bool]
    can_send_media_messages: Optional[bool]
    can_send_polls: Optional[bool]
    can_send_other_messages: Optional[bool]
    can_add_web_page_previews: Optional[bool]
    can_change_info: Optional[bool]
    can_invite_users: Optional[bool]
    can_pin_messages: Optional[bool]
# end class ChatPermissions


class ChatLocationModel(BaseModel):  # Result"""Represents a location to which a chat is connected.

    https://core.telegram.org/bots/api#chatlocation
    """

    location: 'LocationModel'
    address: str
# end class ChatLocation


class BotCommandModel(BaseModel):  # Sendable"""This object represents a bot command.

    https://core.telegram.org/bots/api#botcommand
    """

    command: str
    description: str
# end class BotCommand


class ResponseParametersModel(BaseModel):  # Receivable"""Contains information about why a request was unsuccessful.

    https://core.telegram.org/bots/api#responseparameters
    """

    migrate_to_chat_id: Optional[int]
    retry_after: Optional[int]
# end class ResponseParameters


class InputMediaPhotoModel(BaseModel):  # InputMedia"""Represents a photo to be sent.

    https://core.telegram.org/bots/api#inputmediaphoto
    """

    type: str
    media: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
# end class InputMediaPhoto


class InputMediaVideoModel(BaseModel):  # InputMediaVideolike"""Represents a video to be sent.

    https://core.telegram.org/bots/api#inputmediavideo
    """

    type: str
    media: str
    thumb: Optional[Union['InputFileModel', str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
    supports_streaming: Optional[bool]
# end class InputMediaVideo


class InputMediaAnimationModel(BaseModel):  # InputMediaVideolike"""Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    https://core.telegram.org/bots/api#inputmediaanimation
    """

    type: str
    media: str
    thumb: Optional[Union['InputFileModel', str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
# end class InputMediaAnimation


class InputMediaAudioModel(BaseModel):  # InputMediaPlayable"""Represents an audio file to be treated as music to be sent.

    https://core.telegram.org/bots/api#inputmediaaudio
    """

    type: str
    media: str
    thumb: Optional[Union['InputFileModel', str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    duration: Optional[int]
    performer: Optional[str]
    title: Optional[str]
# end class InputMediaAudio


class InputMediaDocumentModel(BaseModel):  # InputMediaWithThumb"""Represents a general file to be sent.

    https://core.telegram.org/bots/api#inputmediadocument
    """

    type: str
    media: str
    thumb: Optional[Union['InputFileModel', str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    disable_content_type_detection: Optional[bool]
# end class InputMediaDocument


class StickerModel(BaseModel):  # Media"""This object represents a sticker.

    https://core.telegram.org/bots/api#sticker
    """

    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    thumb: Optional['PhotoSizeModel']
    emoji: Optional[str]
    set_name: Optional[str]
    mask_position: Optional['MaskPositionModel']
    file_size: Optional[int]
# end class Sticker


class StickerSetModel(BaseModel):  # Result"""This object represents a sticker set.

    https://core.telegram.org/bots/api#stickerset
    """

    name: str
    title: str
    is_animated: bool
    contains_masks: bool
    stickers: List['StickerModel']
    thumb: Optional['PhotoSizeModel']
# end class StickerSet


class MaskPositionModel(BaseModel):  # Result"""This object describes the position on faces where a mask should be placed by default.

    https://core.telegram.org/bots/api#maskposition
    """

    point: str
    x_shift: float
    y_shift: float
    scale: float
# end class MaskPosition


class InlineQueryModel(BaseModel):  # Result"""This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery
    """

    id: str
    from_peer: 'UserModel'
    query: str
    offset: str
    location: Optional['LocationModel']
# end class InlineQuery


class InlineQueryResultArticleModel(BaseModel):  # InlineQueryResult"""Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """

    type: str
    id: str
    title: str
    input_message_content: 'InputMessageContentModel'
    reply_markup: Optional['InlineKeyboardMarkupModel']
    url: Optional[str]
    hide_url: Optional[bool]
    description: Optional[str]
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultArticle


class InlineQueryResultPhotoModel(BaseModel):  # InlineQueryResult"""Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto
    """

    type: str
    id: str
    photo_url: str
    thumb_url: str
    photo_width: Optional[int]
    photo_height: Optional[int]
    title: Optional[str]
    description: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultPhoto


class InlineQueryResultGifModel(BaseModel):  # InlineQueryResult"""Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif
    """

    type: str
    id: str
    gif_url: str
    thumb_url: str
    gif_width: Optional[int]
    gif_height: Optional[int]
    gif_duration: Optional[int]
    thumb_mime_type: Optional[str]
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultGif


class InlineQueryResultMpeg4GifModel(BaseModel):  # InlineQueryResult"""Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """

    type: str
    id: str
    mpeg4_url: str
    thumb_url: str
    mpeg4_width: Optional[int]
    mpeg4_height: Optional[int]
    mpeg4_duration: Optional[int]
    thumb_mime_type: Optional[str]
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultMpeg4Gif


class InlineQueryResultVideoModel(BaseModel):  # InlineQueryResult"""Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.

    https://core.telegram.org/bots/api#inlinequeryresultvideo
    """

    type: str
    id: str
    video_url: str
    mime_type: str
    thumb_url: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    video_width: Optional[int]
    video_height: Optional[int]
    video_duration: Optional[int]
    description: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultVideo


class InlineQueryResultAudioModel(BaseModel):  # InlineQueryResult"""Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """

    type: str
    id: str
    audio_url: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    performer: Optional[str]
    audio_duration: Optional[int]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultAudio


class InlineQueryResultVoiceModel(BaseModel):  # InlineQueryResult"""Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice
    """

    type: str
    id: str
    voice_url: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    voice_duration: Optional[int]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultVoice


class InlineQueryResultDocumentModel(BaseModel):  # InlineQueryResult"""Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultdocument
    """

    type: str
    id: str
    title: str
    document_url: str
    mime_type: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    description: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultDocument


class InlineQueryResultLocationModel(BaseModel):  # InlineQueryResult"""Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation
    """

    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: Optional[float]
    live_period: Optional[int]
    heading: Optional[int]
    proximity_alert_radius: Optional[int]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultLocation


class InlineQueryResultVenueModel(BaseModel):  # InlineQueryResult"""Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue
    """

    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]
    google_place_id: Optional[str]
    google_place_type: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultVenue


class InlineQueryResultContactModel(BaseModel):  # InlineQueryResult"""Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact
    """

    type: str
    id: str
    phone_number: str
    first_name: str
    last_name: Optional[str]
    vcard: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultContact


class InlineQueryResultGameModel(BaseModel):  # InlineQueryResult"""Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    https://core.telegram.org/bots/api#inlinequeryresultgame
    """

    type: str
    id: str
    game_short_name: str
    reply_markup: Optional['InlineKeyboardMarkupModel']
# end class InlineQueryResultGame


class InlineQueryResultCachedPhotoModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """

    type: str
    id: str
    photo_file_id: str
    title: Optional[str]
    description: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedPhoto


class InlineQueryResultCachedGifModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    """

    type: str
    id: str
    gif_file_id: str
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedGif


class InlineQueryResultCachedMpeg4GifModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """

    type: str
    id: str
    mpeg4_file_id: str
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedMpeg4Gif


class InlineQueryResultCachedStickerModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """

    type: str
    id: str
    sticker_file_id: str
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedSticker


class InlineQueryResultCachedDocumentModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """

    type: str
    id: str
    title: str
    document_file_id: str
    description: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedDocument


class InlineQueryResultCachedVideoModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    """

    type: str
    id: str
    video_file_id: str
    title: str
    description: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedVideo


class InlineQueryResultCachedVoiceModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    """

    type: str
    id: str
    voice_file_id: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedVoice


class InlineQueryResultCachedAudioModel(BaseModel):  # InlineQueryCachedResult"""Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """

    type: str
    id: str
    audio_file_id: str
    caption: Optional[str]
    parse_mode: Optional[str]
    caption_entities: Optional[List['MessageEntityModel']]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedAudio


class InputTextMessageContentModel(BaseModel):  # InputMessageContent"""Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """

    message_text: str
    parse_mode: Optional[str]
    entities: Optional[List['MessageEntityModel']]
    disable_web_page_preview: Optional[bool]
# end class InputTextMessageContent


class InputLocationMessageContentModel(BaseModel):  # InputMessageContent"""Represents the content of a location message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """

    latitude: float
    longitude: float
    horizontal_accuracy: Optional[float]
    live_period: Optional[int]
    heading: Optional[int]
    proximity_alert_radius: Optional[int]
# end class InputLocationMessageContent


class InputVenueMessageContentModel(BaseModel):  # InputMessageContent"""Represents the content of a venue message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """

    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]
    google_place_id: Optional[str]
    google_place_type: Optional[str]
# end class InputVenueMessageContent


class InputContactMessageContentModel(BaseModel):  # InputMessageContent"""Represents the content of a contact message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """

    phone_number: str
    first_name: str
    last_name: Optional[str]
    vcard: Optional[str]
# end class InputContactMessageContent


class ChosenInlineResultModel(BaseModel):  # UpdateType"""Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    Note: It is necessary to enable inline feedback via @Botfather in order to receive these objects in updates.

    https://core.telegram.org/bots/api#choseninlineresult
    """

    result_id: str
    from_peer: 'UserModel'
    query: str
    location: Optional['LocationModel']
    inline_message_id: Optional[str]
# end class ChosenInlineResult


class LabeledPriceModel(BaseModel):  # Sendable"""This object represents a portion of the price for goods or services.

    https://core.telegram.org/bots/api#labeledprice
    """

    label: str
    amount: int
# end class LabeledPrice


class InvoiceModel(BaseModel):  # Result"""This object contains basic information about an invoice.

    https://core.telegram.org/bots/api#invoice
    """

    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int
# end class Invoice


class ShippingAddressModel(BaseModel):  # Result"""This object represents a shipping address.

    https://core.telegram.org/bots/api#shippingaddress
    """

    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str
# end class ShippingAddress


class OrderInfoModel(BaseModel):  # Result"""This object represents information about an order.

    https://core.telegram.org/bots/api#orderinfo
    """

    name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    shipping_address: Optional['ShippingAddressModel']
# end class OrderInfo


class ShippingOptionModel(BaseModel):  # Sendable"""This object represents one shipping option.

    https://core.telegram.org/bots/api#shippingoption
    """

    id: str
    title: str
    prices: List['LabeledPriceModel']
# end class ShippingOption


class SuccessfulPaymentModel(BaseModel):  # Result"""This object contains basic information about a successful payment.

    https://core.telegram.org/bots/api#successfulpayment
    """

    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    shipping_option_id: Optional[str]
    order_info: Optional['OrderInfoModel']
# end class SuccessfulPayment


class ShippingQueryModel(BaseModel):  # UpdateType"""This object contains information about an incoming shipping query.

    https://core.telegram.org/bots/api#shippingquery
    """

    id: str
    from_peer: 'UserModel'
    invoice_payload: str
    shipping_address: 'ShippingAddressModel'
# end class ShippingQuery


class PreCheckoutQueryModel(BaseModel):  # UpdateType"""This object contains information about an incoming pre-checkout query.

    https://core.telegram.org/bots/api#precheckoutquery
    """

    id: str
    from_peer: 'UserModel'
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str]
    order_info: Optional['OrderInfoModel']
# end class PreCheckoutQuery


class PassportDataModel(BaseModel):  # Result"""Contains information about Telegram Passport data shared with the bot by the user.

    https://core.telegram.org/bots/api#passportdata
    """

    data: List['EncryptedPassportElementModel']
    credentials: 'EncryptedCredentialsModel'
# end class PassportData


class PassportFileModel(BaseModel):  # Result"""This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    https://core.telegram.org/bots/api#passportfile
    """

    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int
# end class PassportFile


class EncryptedPassportElementModel(BaseModel):  # Result"""Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    https://core.telegram.org/bots/api#encryptedpassportelement
    """

    type: str
    hash: str
    data: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    files: Optional[List['PassportFileModel']]
    front_side: Optional['PassportFileModel']
    reverse_side: Optional['PassportFileModel']
    selfie: Optional['PassportFileModel']
    translation: Optional[List['PassportFileModel']]
# end class EncryptedPassportElement


class EncryptedCredentialsModel(BaseModel):  # Result"""Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

    https://core.telegram.org/bots/api#encryptedcredentials
    """

    data: str
    hash: str
    secret: str
# end class EncryptedCredentials


class PassportElementErrorDataFieldModel(BaseModel):  # PassportElementError"""Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    https://core.telegram.org/bots/api#passportelementerrordatafield
    """

    source: str
    type: str
    field_name: str
    data_hash: str
    message: str
# end class PassportElementErrorDataField


class PassportElementErrorFrontSideModel(BaseModel):  # PassportElementError"""Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorfrontside
    """

    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorFrontSide


class PassportElementErrorReverseSideModel(BaseModel):  # PassportElementError"""Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorreverseside
    """

    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorReverseSide


class PassportElementErrorSelfieModel(BaseModel):  # PassportElementError"""Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    https://core.telegram.org/bots/api#passportelementerrorselfie
    """

    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorSelfie


class PassportElementErrorFileModel(BaseModel):  # PassportElementError"""Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    https://core.telegram.org/bots/api#passportelementerrorfile
    """

    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorFile


class PassportElementErrorFilesModel(BaseModel):  # PassportElementError"""Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    https://core.telegram.org/bots/api#passportelementerrorfiles
    """

    source: str
    type: str
    file_hashes: List[str]
    message: str
# end class PassportElementErrorFiles


class PassportElementErrorTranslationFileModel(BaseModel):  # PassportElementError"""Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    https://core.telegram.org/bots/api#passportelementerrortranslationfile
    """

    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorTranslationFile


class PassportElementErrorTranslationFilesModel(BaseModel):  # PassportElementError"""Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    """

    source: str
    type: str
    file_hashes: List[str]
    message: str
# end class PassportElementErrorTranslationFiles


class PassportElementErrorUnspecifiedModel(BaseModel):  # PassportElementError"""Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    https://core.telegram.org/bots/api#passportelementerrorunspecified
    """

    source: str
    type: str
    element_hash: str
    message: str
# end class PassportElementErrorUnspecified


class GameModel(BaseModel):  # Media"""This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    https://core.telegram.org/bots/api#game
    """

    title: str
    description: str
    photo: List['PhotoSizeModel']
    text: Optional[str]
    text_entities: Optional[List['MessageEntityModel']]
    animation: Optional['AnimationModel']
# end class Game


class GameHighScoreModel(BaseModel):  # Result"""This object represents one row of the high scores table for a game.

    https://core.telegram.org/bots/api#gamehighscore
    """

    position: int
    user: 'UserModel'
    score: int
# end class GameHighScore


# now register all `ForwardRef`s
MediaModel.update_forward_refs()
ServiceMessageModel.update_forward_refs()
PeerModel.update_forward_refs()
UpdateTypeModel.update_forward_refs()
CallbackGameModel.update_forward_refs()
InlineQueryResultModel.update_forward_refs()
InlineQueryCachedResultModel.update_forward_refs()
InputMessageContentModel.update_forward_refs()
InputMediaModel.update_forward_refs()
InputMediaWithThumbModel.update_forward_refs()
InputMediaPlayableModel.update_forward_refs()
InputMediaVideolikeModel.update_forward_refs()
PassportElementErrorModel.update_forward_refs()
ButtonModel.update_forward_refs()
ReplyMarkupModel.update_forward_refs()
ReceivableModel.update_forward_refs()
SendableModel.update_forward_refs()
ResultModel.update_forward_refs()
TgBotApiObjectModel.update_forward_refs()
UpdateModel.update_forward_refs()
WebhookInfoModel.update_forward_refs()
UserModel.update_forward_refs()
ChatModel.update_forward_refs()
MessageModel.update_forward_refs()
MessageIdModel.update_forward_refs()
MessageEntityModel.update_forward_refs()
PhotoSizeModel.update_forward_refs()
AnimationModel.update_forward_refs()
AudioModel.update_forward_refs()
DocumentModel.update_forward_refs()
VideoModel.update_forward_refs()
VideoNoteModel.update_forward_refs()
VoiceModel.update_forward_refs()
ContactModel.update_forward_refs()
DiceModel.update_forward_refs()
PollOptionModel.update_forward_refs()
PollAnswerModel.update_forward_refs()
PollModel.update_forward_refs()
LocationModel.update_forward_refs()
VenueModel.update_forward_refs()
ProximityAlertTriggeredModel.update_forward_refs()
MessageAutoDeleteTimerChangedModel.update_forward_refs()
VoiceChatEndedModel.update_forward_refs()
VoiceChatParticipantsInvitedModel.update_forward_refs()
UserProfilePhotosModel.update_forward_refs()
FileModel.update_forward_refs()
ReplyKeyboardMarkupModel.update_forward_refs()
KeyboardButtonModel.update_forward_refs()
KeyboardButtonPollTypeModel.update_forward_refs()
ReplyKeyboardRemoveModel.update_forward_refs()
InlineKeyboardMarkupModel.update_forward_refs()
InlineKeyboardButtonModel.update_forward_refs()
LoginUrlModel.update_forward_refs()
CallbackQueryModel.update_forward_refs()
ForceReplyModel.update_forward_refs()
ChatPhotoModel.update_forward_refs()
ChatInviteLinkModel.update_forward_refs()
ChatMemberModel.update_forward_refs()
ChatMemberUpdatedModel.update_forward_refs()
ChatPermissionsModel.update_forward_refs()
ChatLocationModel.update_forward_refs()
BotCommandModel.update_forward_refs()
ResponseParametersModel.update_forward_refs()
InputMediaPhotoModel.update_forward_refs()
InputMediaVideoModel.update_forward_refs()
InputMediaAnimationModel.update_forward_refs()
InputMediaAudioModel.update_forward_refs()
InputMediaDocumentModel.update_forward_refs()
StickerModel.update_forward_refs()
StickerSetModel.update_forward_refs()
MaskPositionModel.update_forward_refs()
InlineQueryModel.update_forward_refs()
InlineQueryResultArticleModel.update_forward_refs()
InlineQueryResultPhotoModel.update_forward_refs()
InlineQueryResultGifModel.update_forward_refs()
InlineQueryResultMpeg4GifModel.update_forward_refs()
InlineQueryResultVideoModel.update_forward_refs()
InlineQueryResultAudioModel.update_forward_refs()
InlineQueryResultVoiceModel.update_forward_refs()
InlineQueryResultDocumentModel.update_forward_refs()
InlineQueryResultLocationModel.update_forward_refs()
InlineQueryResultVenueModel.update_forward_refs()
InlineQueryResultContactModel.update_forward_refs()
InlineQueryResultGameModel.update_forward_refs()
InlineQueryResultCachedPhotoModel.update_forward_refs()
InlineQueryResultCachedGifModel.update_forward_refs()
InlineQueryResultCachedMpeg4GifModel.update_forward_refs()
InlineQueryResultCachedStickerModel.update_forward_refs()
InlineQueryResultCachedDocumentModel.update_forward_refs()
InlineQueryResultCachedVideoModel.update_forward_refs()
InlineQueryResultCachedVoiceModel.update_forward_refs()
InlineQueryResultCachedAudioModel.update_forward_refs()
InputTextMessageContentModel.update_forward_refs()
InputLocationMessageContentModel.update_forward_refs()
InputVenueMessageContentModel.update_forward_refs()
InputContactMessageContentModel.update_forward_refs()
ChosenInlineResultModel.update_forward_refs()
LabeledPriceModel.update_forward_refs()
InvoiceModel.update_forward_refs()
ShippingAddressModel.update_forward_refs()
OrderInfoModel.update_forward_refs()
ShippingOptionModel.update_forward_refs()
SuccessfulPaymentModel.update_forward_refs()
ShippingQueryModel.update_forward_refs()
PreCheckoutQueryModel.update_forward_refs()
PassportDataModel.update_forward_refs()
PassportFileModel.update_forward_refs()
EncryptedPassportElementModel.update_forward_refs()
EncryptedCredentialsModel.update_forward_refs()
PassportElementErrorDataFieldModel.update_forward_refs()
PassportElementErrorFrontSideModel.update_forward_refs()
PassportElementErrorReverseSideModel.update_forward_refs()
PassportElementErrorSelfieModel.update_forward_refs()
PassportElementErrorFileModel.update_forward_refs()
PassportElementErrorFilesModel.update_forward_refs()
PassportElementErrorTranslationFileModel.update_forward_refs()
PassportElementErrorTranslationFilesModel.update_forward_refs()
PassportElementErrorUnspecifiedModel.update_forward_refs()
GameModel.update_forward_refs()
GameHighScoreModel.update_forward_refs()
