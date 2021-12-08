# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.inline import InlineQueryCachedResult
from pytgbot.api_types.sendable.inline import InlineQueryResult
from pytgbot.api_types.sendable.inline import InputMessageContent

__author__ = 'luckydonald'


class InlineQueryResult(Sendable):
    """
    This object represents one result of an inline query.

    Telegram clients currently support results of 20 types.

    https://core.telegram.org/bots/api#inlinequeryresult

    Optional keyword parameters:
    """
# end class InlineQueryResult

class InlineQueryCachedResult(InlineQueryResult):
    """
    Parent class of all those cached inline results.

    Optional keyword parameters:
    """
# end class InlineQueryCachedResult

class InputMessageContent(Sendable):
    """
    Parent class of all those input message content.

    Optional keyword parameters:
    """
# end class InputMessageContent

class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle


    Parameters:

    :param type: Type of the result, must be article
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 Bytes
    :type  id: str|unicode

    :param title: Title of the result
    :type  title: str|unicode

    :param input_message_content: Content of the message to be sent
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent


    Optional keyword parameters:

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param url: Optional. URL of the result
    :type  url: str|unicode

    :param hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
    :type  hide_url: bool

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param thumb_url: Optional. Url of the thumbnail for the result
    :type  thumb_url: str|unicode

    :param thumb_width: Optional. Thumbnail width
    :type  thumb_width: int

    :param thumb_height: Optional. Thumbnail height
    :type  thumb_height: int
    """
    type: str
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: InlineKeyboardMarkup
    url: str
    hide_url: bool
    description: str
    thumb_url: str
    thumb_width: int
    thumb_height: int
# end class InlineQueryResultArticle

class InlineQueryResultPhoto(InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto


    Parameters:

    :param type: Type of the result, must be photo
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param photo_url: A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
    :type  photo_url: str|unicode

    :param thumb_url: URL of the thumbnail for the photo
    :type  thumb_url: str|unicode


    Optional keyword parameters:

    :param photo_width: Optional. Width of the photo
    :type  photo_width: int

    :param photo_height: Optional. Height of the photo
    :type  photo_height: int

    :param title: Optional. Title for the result
    :type  title: str|unicode

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    photo_url: str
    thumb_url: str
    photo_width: int
    photo_height: int
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultPhoto

class InlineQueryResultGif(InlineQueryResult):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif


    Parameters:

    :param type: Type of the result, must be gif
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB
    :type  gif_url: str|unicode

    :param thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :type  thumb_url: str|unicode


    Optional keyword parameters:

    :param gif_width: Optional. Width of the GIF
    :type  gif_width: int

    :param gif_height: Optional. Height of the GIF
    :type  gif_height: int

    :param gif_duration: Optional. Duration of the GIF in seconds
    :type  gif_duration: int

    :param thumb_mime_type: Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
    :type  thumb_mime_type: str|unicode

    :param title: Optional. Title for the result
    :type  title: str|unicode

    :param caption: Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the GIF animation
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    gif_url: str
    thumb_url: str
    gif_width: int
    gif_height: int
    gif_duration: int
    thumb_mime_type: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultGif

class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif


    Parameters:

    :param type: Type of the result, must be mpeg4_gif
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB
    :type  mpeg4_url: str|unicode

    :param thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :type  thumb_url: str|unicode


    Optional keyword parameters:

    :param mpeg4_width: Optional. Video width
    :type  mpeg4_width: int

    :param mpeg4_height: Optional. Video height
    :type  mpeg4_height: int

    :param mpeg4_duration: Optional. Video duration in seconds
    :type  mpeg4_duration: int

    :param thumb_mime_type: Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
    :type  thumb_mime_type: str|unicode

    :param title: Optional. Title for the result
    :type  title: str|unicode

    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    mpeg4_url: str
    thumb_url: str
    mpeg4_width: int
    mpeg4_height: int
    mpeg4_duration: int
    thumb_mime_type: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultMpeg4Gif

class InlineQueryResultVideo(InlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.

    https://core.telegram.org/bots/api#inlinequeryresultvideo


    Parameters:

    :param type: Type of the result, must be video
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param video_url: A valid URL for the embedded video player or video file
    :type  video_url: str|unicode

    :param mime_type: Mime type of the content of video url, "text/html" or "video/mp4"
    :type  mime_type: str|unicode

    :param thumb_url: URL of the thumbnail (JPEG only) for the video
    :type  thumb_url: str|unicode

    :param title: Title for the result
    :type  title: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param video_width: Optional. Video width
    :type  video_width: int

    :param video_height: Optional. Video height
    :type  video_height: int

    :param video_duration: Optional. Video duration in seconds
    :type  video_duration: int

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the video. This field is required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    video_url: str
    mime_type: str
    thumb_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    video_width: int
    video_height: int
    video_duration: int
    description: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultVideo

class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio


    Parameters:

    :param type: Type of the result, must be audio
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param audio_url: A valid URL for the audio file
    :type  audio_url: str|unicode

    :param title: Title
    :type  title: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param performer: Optional. Performer
    :type  performer: str|unicode

    :param audio_duration: Optional. Audio duration in seconds
    :type  audio_duration: int

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    audio_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    performer: str
    audio_duration: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultAudio

class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice


    Parameters:

    :param type: Type of the result, must be voice
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param voice_url: A valid URL for the voice recording
    :type  voice_url: str|unicode

    :param title: Recording title
    :type  title: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param voice_duration: Optional. Recording duration in seconds
    :type  voice_duration: int

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the voice recording
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    voice_url: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    voice_duration: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultVoice

class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultdocument


    Parameters:

    :param type: Type of the result, must be document
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param title: Title for the result
    :type  title: str|unicode

    :param document_url: A valid URL for the file
    :type  document_url: str|unicode

    :param mime_type: Mime type of the content of the file, either "application/pdf" or "application/zip"
    :type  mime_type: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the file
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent

    :param thumb_url: Optional. URL of the thumbnail (JPEG only) for the file
    :type  thumb_url: str|unicode

    :param thumb_width: Optional. Thumbnail width
    :type  thumb_width: int

    :param thumb_height: Optional. Thumbnail height
    :type  thumb_height: int
    """
    type: str
    id: str
    title: str
    document_url: str
    mime_type: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    description: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int
# end class InlineQueryResultDocument

class InlineQueryResultLocation(InlineQueryResult):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation


    Parameters:

    :param type: Type of the result, must be location
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 Bytes
    :type  id: str|unicode

    :param latitude: Location latitude in degrees
    :type  latitude: float

    :param longitude: Location longitude in degrees
    :type  longitude: float

    :param title: Location title
    :type  title: str|unicode


    Optional keyword parameters:

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type  horizontal_accuracy: float

    :param live_period: Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    :type  live_period: int

    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type  heading: int

    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type  proximity_alert_radius: int

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the location
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent

    :param thumb_url: Optional. Url of the thumbnail for the result
    :type  thumb_url: str|unicode

    :param thumb_width: Optional. Thumbnail width
    :type  thumb_width: int

    :param thumb_height: Optional. Thumbnail height
    :type  thumb_height: int
    """
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int
# end class InlineQueryResultLocation

class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue


    Parameters:

    :param type: Type of the result, must be venue
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 Bytes
    :type  id: str|unicode

    :param latitude: Latitude of the venue location in degrees
    :type  latitude: float

    :param longitude: Longitude of the venue location in degrees
    :type  longitude: float

    :param title: Title of the venue
    :type  title: str|unicode

    :param address: Address of the venue
    :type  address: str|unicode


    Optional keyword parameters:

    :param foursquare_id: Optional. Foursquare identifier of the venue if known
    :type  foursquare_id: str|unicode

    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
    :type  foursquare_type: str|unicode

    :param google_place_id: Optional. Google Places identifier of the venue
    :type  google_place_id: str|unicode

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type  google_place_type: str|unicode

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the venue
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent

    :param thumb_url: Optional. Url of the thumbnail for the result
    :type  thumb_url: str|unicode

    :param thumb_width: Optional. Thumbnail width
    :type  thumb_width: int

    :param thumb_height: Optional. Thumbnail height
    :type  thumb_height: int
    """
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int
# end class InlineQueryResultVenue

class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact


    Parameters:

    :param type: Type of the result, must be contact
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 Bytes
    :type  id: str|unicode

    :param phone_number: Contact's phone number
    :type  phone_number: str|unicode

    :param first_name: Contact's first name
    :type  first_name: str|unicode


    Optional keyword parameters:

    :param last_name: Optional. Contact's last name
    :type  last_name: str|unicode

    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :type  vcard: str|unicode

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the contact
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent

    :param thumb_url: Optional. Url of the thumbnail for the result
    :type  thumb_url: str|unicode

    :param thumb_width: Optional. Thumbnail width
    :type  thumb_width: int

    :param thumb_height: Optional. Thumbnail height
    :type  thumb_height: int
    """
    type: str
    id: str
    phone_number: str
    first_name: str
    last_name: str
    vcard: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
    thumb_url: str
    thumb_width: int
    thumb_height: int
# end class InlineQueryResultContact

class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    https://core.telegram.org/bots/api#inlinequeryresultgame


    Parameters:

    :param type: Type of the result, must be game
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param game_short_name: Short name of the game
    :type  game_short_name: str|unicode


    Optional keyword parameters:

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
    """
    type: str
    id: str
    game_short_name: str
    reply_markup: InlineKeyboardMarkup
# end class InlineQueryResultGame

class InlineQueryResultCachedPhoto(InlineQueryCachedResult):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto


    Parameters:

    :param type: Type of the result, must be photo
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param photo_file_id: A valid file identifier of the photo
    :type  photo_file_id: str|unicode


    Optional keyword parameters:

    :param title: Optional. Title for the result
    :type  title: str|unicode

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    photo_file_id: str
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedPhoto

class InlineQueryResultCachedGif(InlineQueryCachedResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif


    Parameters:

    :param type: Type of the result, must be gif
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param gif_file_id: A valid file identifier for the GIF file
    :type  gif_file_id: str|unicode


    Optional keyword parameters:

    :param title: Optional. Title for the result
    :type  title: str|unicode

    :param caption: Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the GIF animation
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    gif_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedGif

class InlineQueryResultCachedMpeg4Gif(InlineQueryCachedResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif


    Parameters:

    :param type: Type of the result, must be mpeg4_gif
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param mpeg4_file_id: A valid file identifier for the MP4 file
    :type  mpeg4_file_id: str|unicode


    Optional keyword parameters:

    :param title: Optional. Title for the result
    :type  title: str|unicode

    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    mpeg4_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedMpeg4Gif

class InlineQueryResultCachedSticker(InlineQueryCachedResult):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker


    Parameters:

    :param type: Type of the result, must be sticker
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param sticker_file_id: A valid file identifier of the sticker
    :type  sticker_file_id: str|unicode


    Optional keyword parameters:

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the sticker
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    sticker_file_id: str
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedSticker

class InlineQueryResultCachedDocument(InlineQueryCachedResult):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument


    Parameters:

    :param type: Type of the result, must be document
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param title: Title for the result
    :type  title: str|unicode

    :param document_file_id: A valid file identifier for the file
    :type  document_file_id: str|unicode


    Optional keyword parameters:

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the file
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    title: str
    document_file_id: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedDocument

class InlineQueryResultCachedVideo(InlineQueryCachedResult):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo


    Parameters:

    :param type: Type of the result, must be video
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param video_file_id: A valid file identifier for the video file
    :type  video_file_id: str|unicode

    :param title: Title for the result
    :type  title: str|unicode


    Optional keyword parameters:

    :param description: Optional. Short description of the result
    :type  description: str|unicode

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the video
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    video_file_id: str
    title: str
    description: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedVideo

class InlineQueryResultCachedVoice(InlineQueryCachedResult):
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice


    Parameters:

    :param type: Type of the result, must be voice
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param voice_file_id: A valid file identifier for the voice message
    :type  voice_file_id: str|unicode

    :param title: Voice message title
    :type  title: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the voice message caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the voice message
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    voice_file_id: str
    title: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedVoice

class InlineQueryResultCachedAudio(InlineQueryCachedResult):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio


    Parameters:

    :param type: Type of the result, must be audio
    :type  type: str|unicode

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param audio_file_id: A valid file identifier for the audio file
    :type  audio_file_id: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    :type  input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
    """
    type: str
    id: str
    audio_file_id: str
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    reply_markup: InlineKeyboardMarkup
    input_message_content: InputMessageContent
# end class InlineQueryResultCachedAudio

class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent


    Parameters:

    :param message_text: Text of the message to be sent, 1-4096 characters
    :type  message_text: str|unicode


    Optional keyword parameters:

    :param parse_mode: Optional. Mode for parsing entities in the message text. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param entities: Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
    :type  entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param disable_web_page_preview: Optional. Disables link previews for links in the sent message
    :type  disable_web_page_preview: bool
    """
    message_text: str
    parse_mode: str
    entities: List[MessageEntity]
    disable_web_page_preview: bool
# end class InputTextMessageContent

class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputlocationmessagecontent


    Parameters:

    :param latitude: Latitude of the location in degrees
    :type  latitude: float

    :param longitude: Longitude of the location in degrees
    :type  longitude: float


    Optional keyword parameters:

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type  horizontal_accuracy: float

    :param live_period: Optional. Period in seconds for which the location can be updated, should be between 60 and 86400.
    :type  live_period: int

    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    :type  heading: int

    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    :type  proximity_alert_radius: int
    """
    latitude: float
    longitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int
# end class InputLocationMessageContent

class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputvenuemessagecontent


    Parameters:

    :param latitude: Latitude of the venue in degrees
    :type  latitude: float

    :param longitude: Longitude of the venue in degrees
    :type  longitude: float

    :param title: Name of the venue
    :type  title: str|unicode

    :param address: Address of the venue
    :type  address: str|unicode


    Optional keyword parameters:

    :param foursquare_id: Optional. Foursquare identifier of the venue, if known
    :type  foursquare_id: str|unicode

    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
    :type  foursquare_type: str|unicode

    :param google_place_id: Optional. Google Places identifier of the venue
    :type  google_place_id: str|unicode

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type  google_place_type: str|unicode
    """
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str
# end class InputVenueMessageContent

class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputcontactmessagecontent


    Parameters:

    :param phone_number: Contact's phone number
    :type  phone_number: str|unicode

    :param first_name: Contact's first name
    :type  first_name: str|unicode


    Optional keyword parameters:

    :param last_name: Optional. Contact's last name
    :type  last_name: str|unicode

    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :type  vcard: str|unicode
    """
    phone_number: str
    first_name: str
    last_name: str
    vcard: str
# end class InputContactMessageContent

class InputInvoiceMessageContent(InputMessageContent):
    """
    Represents the content of an invoice message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputinvoicemessagecontent


    Parameters:

    :param title: Product name, 1-32 characters
    :type  title: str|unicode

    :param description: Product description, 1-255 characters
    :type  description: str|unicode

    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :type  payload: str|unicode

    :param provider_token: Payment provider token, obtained via Botfather
    :type  provider_token: str|unicode

    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :type  currency: str|unicode

    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    :type  prices: list of pytgbot.api_types.sendable.payments.LabeledPrice


    Optional keyword parameters:

    :param max_tip_amount: Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
    :type  max_tip_amount: int

    :param suggested_tip_amounts: Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
    :type  suggested_tip_amounts: list of int

    :param provider_data: Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
    :type  provider_data: str|unicode

    :param photo_url: Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    :type  photo_url: str|unicode

    :param photo_size: Optional. Photo size
    :type  photo_size: int

    :param photo_width: Optional. Photo width
    :type  photo_width: int

    :param photo_height: Optional. Photo height
    :type  photo_height: int

    :param need_name: Optional. Pass True, if you require the user's full name to complete the order
    :type  need_name: bool

    :param need_phone_number: Optional. Pass True, if you require the user's phone number to complete the order
    :type  need_phone_number: bool

    :param need_email: Optional. Pass True, if you require the user's email address to complete the order
    :type  need_email: bool

    :param need_shipping_address: Optional. Pass True, if you require the user's shipping address to complete the order
    :type  need_shipping_address: bool

    :param send_phone_number_to_provider: Optional. Pass True, if user's phone number should be sent to provider
    :type  send_phone_number_to_provider: bool

    :param send_email_to_provider: Optional. Pass True, if user's email address should be sent to provider
    :type  send_email_to_provider: bool

    :param is_flexible: Optional. Pass True, if the final price depends on the shipping method
    :type  is_flexible: bool
    """
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: List[LabeledPrice]
    max_tip_amount: int
    suggested_tip_amounts: List[int]
    provider_data: str
    photo_url: str
    photo_size: int
    photo_width: int
    photo_height: int
    need_name: bool
    need_phone_number: bool
    need_email: bool
    need_shipping_address: bool
    send_phone_number_to_provider: bool
    send_email_to_provider: bool
    is_flexible: bool
# end class InputInvoiceMessageContent
