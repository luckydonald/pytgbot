# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from pydantic import BaseModel
from typing import Any, Union, List, Optional

__author__ = 'luckydonald'




class UpdateModel(BaseModel):  # Receivable
    """
    This object represents an incoming update.At most one of the optional parameters can be present in any given update.

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
# end class Update


class WebhookInfoModel(BaseModel):  # Receivable
    """
    Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    """
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    last_error_date: Optional[int]
    last_error_message: Optional[str]
    max_connections: Optional[int]
    allowed_updates: Optional[List[str]]
# end class WebhookInfo


class UserModel(BaseModel):  # Peer
    """
    This object represents a Telegram user or bot.

    https://core.telegram.org/bots/api#user
    """
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str]
    username: Optional[str]
    language_code: Optional[str]
# end class User


class ChatModel(BaseModel):  # Peer
    """
    This object represents a chat.

    https://core.telegram.org/bots/api#chat
    """
    id: int
    type: str
    title: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    photo: Optional['ChatPhotoModel']
    description: Optional[str]
    invite_link: Optional[str]
    pinned_message: Optional['MessageModel']
    permissions: Optional['ChatPermissionsModel']
    slow_mode_delay: Optional[int]
    sticker_set_name: Optional[str]
    can_set_sticker_set: Optional[bool]
# end class Chat


class MessageModel(BaseModel):  # UpdateType
    """
    This object represents a message.

    https://core.telegram.org/bots/api#message
    """
    message_id: int
    date: int
    chat: 'ChatModel'
    from_peer: Optional['UserModel']
    forward_from: Optional['UserModel']
    forward_from_chat: Optional['ChatModel']
    forward_from_message_id: Optional[int]
    forward_signature: Optional[str]
    forward_sender_name: Optional[str]
    forward_date: Optional[int]
    reply_to_message: Optional['MessageModel']
    edit_date: Optional[int]
    media_group_id: Optional[str]
    author_signature: Optional[str]
    text: Optional[str]
    entities: Optional[List['MessageEntityModel']]
    caption_entities: Optional[List['MessageEntityModel']]
    audio: Optional['AudioModel']
    document: Optional['DocumentModel']
    animation: Optional['AnimationModel']
    game: Optional['GameModel']
    photo: Optional[List['PhotoSizeModel']]
    sticker: Optional['StickerModel']
    video: Optional['VideoModel']
    voice: Optional['VoiceModel']
    video_note: Optional['VideoNoteModel']
    caption: Optional[str]
    contact: Optional['ContactModel']
    location: Optional['LocationModel']
    venue: Optional['VenueModel']
    poll: Optional['PollModel']
    new_chat_members: Optional[List['UserModel']]
    left_chat_member: Optional['UserModel']
    new_chat_title: Optional[str]
    new_chat_photo: Optional[List['PhotoSizeModel']]
    delete_chat_photo: Optional[bool]
    group_chat_created: Optional[bool]
    supergroup_chat_created: Optional[bool]
    channel_chat_created: Optional[bool]
    migrate_to_chat_id: Optional[int]
    migrate_from_chat_id: Optional[int]
    pinned_message: Optional['MessageModel']
    invoice: Optional['InvoiceModel']
    successful_payment: Optional['SuccessfulPaymentModel']
    connected_website: Optional[str]
    passport_data: Optional['PassportDataModel']
    reply_markup: Optional['InlineKeyboardMarkupModel']
# end class Message


class MessageEntityModel(BaseModel):  # Result
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    """
    type: str
    offset: int
    length: int
    url: Optional[str]
    user: Optional['UserModel']
# end class MessageEntity


class PhotoSizeModel(BaseModel):  # Result
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int]
# end class PhotoSize


class AudioModel(BaseModel):  # Media
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio
    """
    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str]
    title: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
    thumb: Optional['PhotoSizeModel']
# end class Audio


class DocumentModel(BaseModel):  # Media
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document
    """
    file_id: str
    file_unique_id: str
    thumb: Optional['PhotoSizeModel']
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Document


class VideoModel(BaseModel):  # Media
    """
    This object represents a video file.

    https://core.telegram.org/bots/api#video
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional['PhotoSizeModel']
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Video


class AnimationModel(BaseModel):  # Media
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

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


class VoiceModel(BaseModel):  # Media
    """
    This object represents a voice note.

    https://core.telegram.org/bots/api#voice
    """
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str]
    file_size: Optional[int]
# end class Voice


class VideoNoteModel(BaseModel):  # Media
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    https://core.telegram.org/bots/api#videonote
    """
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: Optional['PhotoSizeModel']
    file_size: Optional[int]
# end class VideoNote


class ContactModel(BaseModel):  # Media
    """
    This object represents a phone contact.

    https://core.telegram.org/bots/api#contact
    """
    phone_number: str
    first_name: str
    last_name: Optional[str]
    user_id: Optional[int]
    vcard: Optional[str]
# end class Contact


class LocationModel(BaseModel):  # Media
    """
    This object represents a point on the map.

    https://core.telegram.org/bots/api#location
    """
    longitude: float
    latitude: float
# end class Location


class VenueModel(BaseModel):  # Media
    """
    This object represents a venue.

    https://core.telegram.org/bots/api#venue
    """
    location: 'LocationModel'
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]
# end class Venue


class PollOptionModel(BaseModel):  # Receivable
    """
    This object contains information about one answer option in a poll.

    https://core.telegram.org/bots/api#polloption
    """
    text: str
    voter_count: int
# end class PollOption


class PollModel(BaseModel):  # Media
    """
    This object contains information about a poll.

    https://core.telegram.org/bots/api#poll
    """
    id: str
    question: str
    options: List['PollOptionModel']
    is_closed: bool
# end class Poll


class UserProfilePhotosModel(BaseModel):  # Result
    """
    This object represent a user's profile pictures.

    https://core.telegram.org/bots/api#userprofilephotos
    """
    total_count: int
    photos: List[List['PhotoSizeModel']]
# end class UserProfilePhotos


class FileModel(BaseModel):  # Receivable
    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

    Maximum file size to download is 20 MB

    https://core.telegram.org/bots/api#file
    """
    file_id: str
    file_unique_id: str
    file_size: Optional[int]
    file_path: Optional[str]
# end class File


class ReplyKeyboardMarkupModel(BaseModel):  # ReplyMarkup
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    https://core.telegram.org/bots/api#replykeyboardmarkup
    """
    keyboard: List[List['KeyboardButtonModel']]
    resize_keyboard: Optional[bool]
    one_time_keyboard: Optional[bool]
    selective: Optional[bool]
# end class ReplyKeyboardMarkup


class KeyboardButtonModel(BaseModel):  # Button
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#keyboardbutton
    """
    text: str
    request_contact: Optional[bool]
    request_location: Optional[bool]
# end class KeyboardButton


class ReplyKeyboardRemoveModel(BaseModel):  # ReplyMarkup
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardremove
    """
    remove_keyboard: bool
    selective: Optional[bool]
# end class ReplyKeyboardRemove


class InlineKeyboardMarkupModel(BaseModel):  # ReplyMarkup
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """
    inline_keyboard: List[List['InlineKeyboardButtonModel']]
# end class InlineKeyboardMarkup


class InlineKeyboardButtonModel(BaseModel):  # Button
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

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


class LoginUrlModel(BaseModel):  # Sendable
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.

    Sample bot: @discussbot

    https://core.telegram.org/bots/api#loginurl
    """
    url: str
    forward_text: Optional[str]
    bot_username: Optional[str]
    request_write_access: Optional[bool]
# end class LoginUrl


class CallbackQueryModel(BaseModel):  # UpdateType
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

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


class ForceReplyModel(BaseModel):  # ReplyMarkup
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot‘s message and tapped ’Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions). There could be two ways to create a new poll:

    Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2). May be appealing for hardcore users but lacks modern day polish.
    Guide the user through a step-by-step process. ‘Please send me your question’, ‘Cool, now let’s add the first answer option‘, ’Great. Keep adding answer options, then send /done when you‘re ready’.

    The last option is definitely more attractive. And if you use ForceReply in your bot‘s questions, it will receive the user’s answers even if it only receives replies, commands and mentions — without any extra work for the user.

    https://core.telegram.org/bots/api#forcereply
    """
    force_reply: bool
    selective: Optional[bool]
# end class ForceReply


class ChatPhotoModel(BaseModel):  # Result
    """
    This object represents a chat photo.

    https://core.telegram.org/bots/api#chatphoto
    """
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str
# end class ChatPhoto


class ChatMemberModel(BaseModel):  # Result
    """
    This object contains information about one member of a chat.

    https://core.telegram.org/bots/api#chatmember
    """
    user: 'UserModel'
    status: str
    custom_title: Optional[str]
    until_date: Optional[int]
    can_be_edited: Optional[bool]
    can_post_messages: Optional[bool]
    can_edit_messages: Optional[bool]
    can_delete_messages: Optional[bool]
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
# end class ChatMember


class ChatPermissionsModel(BaseModel):  # Result
    """
    Describes actions that a non-administrator user is allowed to take in a chat.

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


class ResponseParametersModel(BaseModel):  # Receivable
    """
    Contains information about why a request was unsuccessful.

    https://core.telegram.org/bots/api#responseparameters
    """
    migrate_to_chat_id: Optional[int]
    retry_after: Optional[int]
# end class ResponseParameters


class InputMediaPhotoModel(BaseModel):  # InputMedia
    """
    Represents a photo to be sent.

    https://core.telegram.org/bots/api#inputmediaphoto
    """
    type: str
    media: str
    caption: Optional[str]
    parse_mode: Optional[str]
# end class InputMediaPhoto


class InputMediaVideoModel(BaseModel):  # InputMediaWithThumb
    """
    Represents a video to be sent.

    https://core.telegram.org/bots/api#inputmediavideo
    """
    type: str
    media: str
    thumb: Union[Optional['InputFileModel'], Optional[str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
    supports_streaming: Optional[bool]
# end class InputMediaVideo


class InputMediaAnimationModel(BaseModel):  # InputMediaWithThumb
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    https://core.telegram.org/bots/api#inputmediaanimation
    """
    type: str
    media: str
    thumb: Union[Optional['InputFileModel'], Optional[str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    width: Optional[int]
    height: Optional[int]
    duration: Optional[int]
# end class InputMediaAnimation


class InputMediaAudioModel(BaseModel):  # InputMediaWithThumb
    """
    Represents an audio file to be treated as music to be sent.

    https://core.telegram.org/bots/api#inputmediaaudio
    """
    type: str
    media: str
    thumb: Union[Optional['InputFileModel'], Optional[str]]
    caption: Optional[str]
    parse_mode: Optional[str]
    duration: Optional[int]
    performer: Optional[str]
    title: Optional[str]
# end class InputMediaAudio


class InputMediaDocumentModel(BaseModel):  # InputMediaWithThumb
    """
    Represents a general file to be sent.

    https://core.telegram.org/bots/api#inputmediadocument
    """
    type: str
    media: str
    thumb: Union[Optional['InputFileModel'], Optional[str]]
    caption: Optional[str]
    parse_mode: Optional[str]
# end class InputMediaDocument


class StickerModel(BaseModel):  # Media
    """
    This object represents a sticker.

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


class StickerSetModel(BaseModel):  # Result
    """
    This object represents a sticker set.

    https://core.telegram.org/bots/api#stickerset
    """
    name: str
    title: str
    is_animated: bool
    contains_masks: bool
    stickers: List['StickerModel']
# end class StickerSet


class MaskPositionModel(BaseModel):  # Result
    """
    This object describes the position on faces where a mask should be placed by default.

    https://core.telegram.org/bots/api#maskposition
    """
    point: str
    x_shift: float
    y_shift: float
    scale: float
# end class MaskPosition


class InlineQueryModel(BaseModel):  # Result
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery
    """
    id: str
    from_peer: 'UserModel'
    query: str
    offset: str
    location: Optional['LocationModel']
# end class InlineQuery


class InlineQueryResultArticleModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to an article or web page.

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


class InlineQueryResultPhotoModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

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
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultPhoto


class InlineQueryResultGifModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif
    """
    type: str
    id: str
    gif_url: str
    thumb_url: str
    gif_width: Optional[int]
    gif_height: Optional[int]
    gif_duration: Optional[int]
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultGif


class InlineQueryResultMpeg4GifModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """
    type: str
    id: str
    mpeg4_url: str
    thumb_url: str
    mpeg4_width: Optional[int]
    mpeg4_height: Optional[int]
    mpeg4_duration: Optional[int]
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultMpeg4Gif


class InlineQueryResultVideoModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

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
    video_width: Optional[int]
    video_height: Optional[int]
    video_duration: Optional[int]
    description: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultVideo


class InlineQueryResultAudioModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """
    type: str
    id: str
    audio_url: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    performer: Optional[str]
    audio_duration: Optional[int]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultAudio


class InlineQueryResultVoiceModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice
    """
    type: str
    id: str
    voice_url: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    voice_duration: Optional[int]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultVoice


class InlineQueryResultDocumentModel(BaseModel):  # InlineQueryResult
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
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
    description: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultDocument


class InlineQueryResultLocationModel(BaseModel):  # InlineQueryResult
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation
    """
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    live_period: Optional[int]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultLocation


class InlineQueryResultVenueModel(BaseModel):  # InlineQueryResult
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
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
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
    thumb_url: Optional[str]
    thumb_width: Optional[int]
    thumb_height: Optional[int]
# end class InlineQueryResultVenue


class InlineQueryResultContactModel(BaseModel):  # InlineQueryResult
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
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


class InlineQueryResultGameModel(BaseModel):  # InlineQueryResult
    """
    Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    https://core.telegram.org/bots/api#inlinequeryresultgame
    """
    type: str
    id: str
    game_short_name: str
    reply_markup: Optional['InlineKeyboardMarkupModel']
# end class InlineQueryResultGame


class InlineQueryResultCachedPhotoModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """
    type: str
    id: str
    photo_file_id: str
    title: Optional[str]
    description: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedPhoto


class InlineQueryResultCachedGifModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    """
    type: str
    id: str
    gif_file_id: str
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedGif


class InlineQueryResultCachedMpeg4GifModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """
    type: str
    id: str
    mpeg4_file_id: str
    title: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedMpeg4Gif


class InlineQueryResultCachedStickerModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """
    type: str
    id: str
    sticker_file_id: str
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedSticker


class InlineQueryResultCachedDocumentModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
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
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedDocument


class InlineQueryResultCachedVideoModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    """
    type: str
    id: str
    video_file_id: str
    title: str
    description: Optional[str]
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedVideo


class InlineQueryResultCachedVoiceModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    """
    type: str
    id: str
    voice_file_id: str
    title: str
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedVoice


class InlineQueryResultCachedAudioModel(BaseModel):  # InlineQueryCachedResult
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """
    type: str
    id: str
    audio_file_id: str
    caption: Optional[str]
    parse_mode: Optional[str]
    reply_markup: Optional['InlineKeyboardMarkupModel']
    input_message_content: Optional['InputMessageContentModel']
# end class InlineQueryResultCachedAudio


class InputTextMessageContentModel(BaseModel):  # InputMessageContent
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    message_text: str
    parse_mode: Optional[str]
    disable_web_page_preview: Optional[bool]
# end class InputTextMessageContent


class InputLocationMessageContentModel(BaseModel):  # InputMessageContent
    """
    Represents the content of a location message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    latitude: float
    longitude: float
    live_period: Optional[int]
# end class InputLocationMessageContent


class InputVenueMessageContentModel(BaseModel):  # InputMessageContent
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str]
    foursquare_type: Optional[str]
# end class InputVenueMessageContent


class InputContactMessageContentModel(BaseModel):  # InputMessageContent
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    phone_number: str
    first_name: str
    last_name: Optional[str]
    vcard: Optional[str]
# end class InputContactMessageContent


class ChosenInlineResultModel(BaseModel):  # UpdateType
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.
    Note: It is necessary to enable inline feedback via @Botfather in order to receive these objects in updates.

    https://core.telegram.org/bots/api#choseninlineresult
    """
    result_id: str
    from_peer: 'UserModel'
    query: str
    location: Optional['LocationModel']
    inline_message_id: Optional[str]
# end class ChosenInlineResult


class LabeledPriceModel(BaseModel):  # Sendable
    """
    This object represents a portion of the price for goods or services.

    https://core.telegram.org/bots/api#labeledprice
    """
    label: str
    amount: int
# end class LabeledPrice


class InvoiceModel(BaseModel):  # Result
    """
    This object contains basic information about an invoice.

    https://core.telegram.org/bots/api#invoice
    """
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int
# end class Invoice


class ShippingAddressModel(BaseModel):  # Result
    """
    This object represents a shipping address.

    https://core.telegram.org/bots/api#shippingaddress
    """
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str
# end class ShippingAddress


class OrderInfoModel(BaseModel):  # Result
    """
    This object represents information about an order.

    https://core.telegram.org/bots/api#orderinfo
    """
    name: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    shipping_address: Optional['ShippingAddressModel']
# end class OrderInfo


class ShippingOptionModel(BaseModel):  # Sendable
    """
    This object represents one shipping option.

    https://core.telegram.org/bots/api#shippingoption
    """
    id: str
    title: str
    prices: List['LabeledPriceModel']
# end class ShippingOption


class SuccessfulPaymentModel(BaseModel):  # Result
    """
    This object contains basic information about a successful payment.

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


class ShippingQueryModel(BaseModel):  # UpdateType
    """
    This object contains information about an incoming shipping query.

    https://core.telegram.org/bots/api#shippingquery
    """
    id: str
    from_peer: 'UserModel'
    invoice_payload: str
    shipping_address: 'ShippingAddressModel'
# end class ShippingQuery


class PreCheckoutQueryModel(BaseModel):  # UpdateType
    """
    This object contains information about an incoming pre-checkout query.

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


class PassportDataModel(BaseModel):  # Result
    """
    Contains information about Telegram Passport data shared with the bot by the user.

    https://core.telegram.org/bots/api#passportdata
    """
    data: List['EncryptedPassportElementModel']
    credentials: 'EncryptedCredentialsModel'
# end class PassportData


class PassportFileModel(BaseModel):  # Result
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    https://core.telegram.org/bots/api#passportfile
    """
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int
# end class PassportFile


class EncryptedPassportElementModel(BaseModel):  # Result
    """
    Contains information about documents or other Telegram Passport elements shared with the bot by the user.

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


class EncryptedCredentialsModel(BaseModel):  # Result
    """
    Contains data required for decrypting and authenticating EncryptedPassportElement. See the Telegram Passport Documentation for a complete description of the data decryption and authentication processes.

    https://core.telegram.org/bots/api#encryptedcredentials
    """
    data: str
    hash: str
    secret: str
# end class EncryptedCredentials


class PassportElementErrorDataFieldModel(BaseModel):  # PassportElementError
    """
    Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    https://core.telegram.org/bots/api#passportelementerrordatafield
    """
    source: str
    type: str
    field_name: str
    data_hash: str
    message: str
# end class PassportElementErrorDataField


class PassportElementErrorFrontSideModel(BaseModel):  # PassportElementError
    """
    Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorfrontside
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorFrontSide


class PassportElementErrorReverseSideModel(BaseModel):  # PassportElementError
    """
    Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    https://core.telegram.org/bots/api#passportelementerrorreverseside
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorReverseSide


class PassportElementErrorSelfieModel(BaseModel):  # PassportElementError
    """
    Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    https://core.telegram.org/bots/api#passportelementerrorselfie
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorSelfie


class PassportElementErrorFileModel(BaseModel):  # PassportElementError
    """
    Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    https://core.telegram.org/bots/api#passportelementerrorfile
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorFile


class PassportElementErrorFilesModel(BaseModel):  # PassportElementError
    """
    Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    https://core.telegram.org/bots/api#passportelementerrorfiles
    """
    source: str
    type: str
    file_hashes: List[str]
    message: str
# end class PassportElementErrorFiles


class PassportElementErrorTranslationFileModel(BaseModel):  # PassportElementError
    """
    Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    https://core.telegram.org/bots/api#passportelementerrortranslationfile
    """
    source: str
    type: str
    file_hash: str
    message: str
# end class PassportElementErrorTranslationFile


class PassportElementErrorTranslationFilesModel(BaseModel):  # PassportElementError
    """
    Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    https://core.telegram.org/bots/api#passportelementerrortranslationfiles
    """
    source: str
    type: str
    file_hashes: List[str]
    message: str
# end class PassportElementErrorTranslationFiles


class PassportElementErrorUnspecifiedModel(BaseModel):  # PassportElementError
    """
    Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    https://core.telegram.org/bots/api#passportelementerrorunspecified
    """
    source: str
    type: str
    element_hash: str
    message: str
# end class PassportElementErrorUnspecified


class GameModel(BaseModel):  # Media
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    https://core.telegram.org/bots/api#game
    """
    title: str
    description: str
    photo: List['PhotoSizeModel']
    text: Optional[str]
    text_entities: Optional[List['MessageEntityModel']]
    animation: Optional['AnimationModel']
# end class Game


class GameHighScoreModel(BaseModel):  # Result
    """
    This object represents one row of the high scores table for a game.

    https://core.telegram.org/bots/api#gamehighscore
    """
    position: int
    user: 'UserModel'
    score: int
# end class GameHighScore
