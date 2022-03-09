# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Receivable
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.media import Media

__author__ = 'luckydonald'


class Media(Receivable):
    """
    parent class for all receivable media.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class Media

class MessageEntity(Result):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity


    Parameters:

    :param type: Type of the entity. Currently, can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "spoiler" (spoiler message), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames)
    :type  type: str|unicode

    :param offset: Offset in UTF-16 code units to the start of the entity
    :type  offset: int

    :param length: Length of the entity in UTF-16 code units
    :type  length: int


    Optional keyword parameters:

    :param url: Optional. For "text_link" only, url that will be opened after user taps on the text
    :type  url: str|unicode

    :param user: Optional. For "text_mention" only, the mentioned user
    :type  user: pytgbot.api_types.receivable.peer.User

    :param language: Optional. For "pre" only, the programming language of the entity text
    :type  language: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    type: str
    offset: int
    length: int
    url: str
    user: User
    language: str
# end class MessageEntity

class PhotoSize(Result):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param width: Photo width
    :type  width: int

    :param height: Photo height
    :type  height: int


    Optional keyword parameters:

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int
# end class PhotoSize

class Animation(Media):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    https://core.telegram.org/bots/api#animation


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param width: Video width as defined by sender
    :type  width: int

    :param height: Video height as defined by sender
    :type  height: int

    :param duration: Duration of the video in seconds as defined by sender
    :type  duration: int


    Optional keyword parameters:

    :param thumb: Optional. Animation thumbnail as defined by sender
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param file_name: Optional. Original animation filename as defined by sender
    :type  file_name: str|unicode

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type  mime_type: str|unicode

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int
# end class Animation

class Audio(Media):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param duration: Duration of the audio in seconds as defined by sender
    :type  duration: int


    Optional keyword parameters:

    :param performer: Optional. Performer of the audio as defined by sender or by audio tags
    :type  performer: str|unicode

    :param title: Optional. Title of the audio as defined by sender or by audio tags
    :type  title: str|unicode

    :param file_name: Optional. Original filename as defined by sender
    :type  file_name: str|unicode

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type  mime_type: str|unicode

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param thumb: Optional. Thumbnail of the album cover to which the music file belongs
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    duration: int
    performer: str
    title: str
    file_name: str
    mime_type: str
    file_size: int
    thumb: PhotoSize
# end class Audio

class Document(Media):
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode


    Optional keyword parameters:

    :param thumb: Optional. Document thumbnail as defined by sender
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param file_name: Optional. Original filename as defined by sender
    :type  file_name: str|unicode

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type  mime_type: str|unicode

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int
# end class Document

class Video(Media):
    """
    This object represents a video file.

    https://core.telegram.org/bots/api#video


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param width: Video width as defined by sender
    :type  width: int

    :param height: Video height as defined by sender
    :type  height: int

    :param duration: Duration of the video in seconds as defined by sender
    :type  duration: int


    Optional keyword parameters:

    :param thumb: Optional. Video thumbnail
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param file_name: Optional. Original filename as defined by sender
    :type  file_name: str|unicode

    :param mime_type: Optional. Mime type of a file as defined by sender
    :type  mime_type: str|unicode

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize
    file_name: str
    mime_type: str
    file_size: int
# end class Video

class VideoNote(Media):
    """
    This object represents a video message (available in Telegram apps as of v.4.0).

    https://core.telegram.org/bots/api#videonote


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param length: Video width and height (diameter of the video message) as defined by sender
    :type  length: int

    :param duration: Duration of the video in seconds as defined by sender
    :type  duration: int


    Optional keyword parameters:

    :param thumb: Optional. Video thumbnail
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: PhotoSize
    file_size: int
# end class VideoNote

class Voice(Media):
    """
    This object represents a voice note.

    https://core.telegram.org/bots/api#voice


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param duration: Duration of the audio in seconds as defined by sender
    :type  duration: int


    Optional keyword parameters:

    :param mime_type: Optional. MIME type of the file as defined by sender
    :type  mime_type: str|unicode

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str
    file_size: int
# end class Voice

class Contact(Media):
    """
    This object represents a phone contact.

    https://core.telegram.org/bots/api#contact


    Parameters:

    :param phone_number: Contact's phone number
    :type  phone_number: str|unicode

    :param first_name: Contact's first name
    :type  first_name: str|unicode


    Optional keyword parameters:

    :param last_name: Optional. Contact's last name
    :type  last_name: str|unicode

    :param user_id: Optional. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    :type  user_id: int

    :param vcard: Optional. Additional data about the contact in the form of a vCard
    :type  vcard: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    phone_number: str
    first_name: str
    last_name: str
    user_id: int
    vcard: str
# end class Contact

class Dice(Media):
    """
    This object represents an animated emoji that displays a random value.

    https://core.telegram.org/bots/api#dice


    Parameters:

    :param emoji: Emoji on which the dice throw animation is based
    :type  emoji: str|unicode

    :param value: Value of the dice, 1-6 for "🎲", "🎯" and "🎳" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji
    :type  value: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    emoji: str
    value: int
# end class Dice

class PollOption(Receivable):
    """
    This object contains information about one answer option in a poll.

    https://core.telegram.org/bots/api#polloption


    Parameters:

    :param text: Option text, 1-100 characters
    :type  text: str|unicode

    :param voter_count: Number of users that voted for this option
    :type  voter_count: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    text: str
    voter_count: int
# end class PollOption

class PollAnswer(Receivable):
    """
    This object represents an answer of a user in a non-anonymous poll.

    https://core.telegram.org/bots/api#pollanswer


    Parameters:

    :param poll_id: Unique poll identifier
    :type  poll_id: str|unicode

    :param user: The user, who changed the answer to the poll
    :type  user: pytgbot.api_types.receivable.peer.User

    :param option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    :type  option_ids: list of int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    poll_id: str
    user: User
    option_ids: List[int]
# end class PollAnswer

class Poll(Media):
    """
    This object contains information about a poll.

    https://core.telegram.org/bots/api#poll


    Parameters:

    :param id: Unique poll identifier
    :type  id: str|unicode

    :param question: Poll question, 1-300 characters
    :type  question: str|unicode

    :param options: List of poll options
    :type  options: list of pytgbot.api_types.receivable.media.PollOption

    :param total_voter_count: Total number of users that voted in the poll
    :type  total_voter_count: int

    :param is_closed: True, if the poll is closed
    :type  is_closed: bool

    :param is_anonymous: True, if the poll is anonymous
    :type  is_anonymous: bool

    :param type: Poll type, currently can be "regular" or "quiz"
    :type  type: str|unicode

    :param allows_multiple_answers: True, if the poll allows multiple answers
    :type  allows_multiple_answers: bool


    Optional keyword parameters:

    :param correct_option_id: Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    :type  correct_option_id: int

    :param explanation: Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    :type  explanation: str|unicode

    :param explanation_entities: Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation
    :type  explanation_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param open_period: Optional. Amount of time in seconds the poll will be active after creation
    :type  open_period: int

    :param close_date: Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    :type  close_date: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    id: str
    question: str
    options: List[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int
    explanation: str
    explanation_entities: List[MessageEntity]
    open_period: int
    close_date: int
# end class Poll

class Location(Media):
    """
    This object represents a point on the map.

    https://core.telegram.org/bots/api#location


    Parameters:

    :param longitude: Longitude as defined by sender
    :type  longitude: float

    :param latitude: Latitude as defined by sender
    :type  latitude: float


    Optional keyword parameters:

    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :type  horizontal_accuracy: float

    :param live_period: Optional. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
    :type  live_period: int

    :param heading: Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    :type  heading: int

    :param proximity_alert_radius: Optional. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    :type  proximity_alert_radius: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    longitude: float
    latitude: float
    horizontal_accuracy: float
    live_period: int
    heading: int
    proximity_alert_radius: int
# end class Location

class Venue(Media):
    """
    This object represents a venue.

    https://core.telegram.org/bots/api#venue


    Parameters:

    :param location: Venue location. Can't be a live location
    :type  location: pytgbot.api_types.receivable.media.Location

    :param title: Name of the venue
    :type  title: str|unicode

    :param address: Address of the venue
    :type  address: str|unicode


    Optional keyword parameters:

    :param foursquare_id: Optional. Foursquare identifier of the venue
    :type  foursquare_id: str|unicode

    :param foursquare_type: Optional. Foursquare type of the venue. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
    :type  foursquare_type: str|unicode

    :param google_place_id: Optional. Google Places identifier of the venue
    :type  google_place_id: str|unicode

    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :type  google_place_type: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    location: Location
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
    google_place_id: str
    google_place_type: str
# end class Venue

class UserProfilePhotos(Result):
    """
    This object represent a user's profile pictures.

    https://core.telegram.org/bots/api#userprofilephotos


    Parameters:

    :param total_count: Total number of profile pictures the target user has
    :type  total_count: int

    :param photos: Requested profile pictures (in up to 4 sizes each)
    :type  photos: list of list of pytgbot.api_types.receivable.media.PhotoSize


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    total_count: int
    photos: List[List[PhotoSize]]
# end class UserProfilePhotos

class File(Receivable):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

    Maximum file size to download is 20 MB

    https://core.telegram.org/bots/api#file


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode


    Optional keyword parameters:

    :param file_size: Optional. File size in bytes, if known
    :type  file_size: int

    :param file_path: Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
    :type  file_path: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    file_size: int
    file_path: str
# end class File

class ChatPhoto(Result):
    """
    This object represents a chat photo.

    https://core.telegram.org/bots/api#chatphoto


    Parameters:

    :param small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    :type  small_file_id: str|unicode

    :param small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  small_file_unique_id: str|unicode

    :param big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo download and only for as long as the photo is not changed.
    :type  big_file_id: str|unicode

    :param big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  big_file_unique_id: str|unicode


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str
# end class ChatPhoto

class Sticker(Media):
    """
    This object represents a sticker.

    https://core.telegram.org/bots/api#sticker


    Parameters:

    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :type  file_id: str|unicode

    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    :type  file_unique_id: str|unicode

    :param width: Sticker width
    :type  width: int

    :param height: Sticker height
    :type  height: int

    :param is_animated: True, if the sticker is animated
    :type  is_animated: bool

    :param is_video: True, if the sticker is a video sticker
    :type  is_video: bool


    Optional keyword parameters:

    :param thumb: Optional. Sticker thumbnail in the .WEBP or .JPG format
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param emoji: Optional. Emoji associated with the sticker
    :type  emoji: str|unicode

    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :type  set_name: str|unicode

    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :type  mask_position: pytgbot.api_types.receivable.stickers.MaskPosition

    :param file_size: Optional. File size in bytes
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumb: PhotoSize
    emoji: str
    set_name: str
    mask_position: MaskPosition
    file_size: int
# end class Sticker

class Game(Media):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    https://core.telegram.org/bots/api#game


    Parameters:

    :param title: Title of the game
    :type  title: str|unicode

    :param description: Description of the game
    :type  description: str|unicode

    :param photo: Photo that will be displayed in the game message in chats.
    :type  photo: list of pytgbot.api_types.receivable.media.PhotoSize


    Optional keyword parameters:

    :param text: Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    :type  text: str|unicode

    :param text_entities: Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    :type  text_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param animation: Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
    :type  animation: pytgbot.api_types.receivable.media.Animation

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    title: str
    description: str
    photo: List[PhotoSize]
    text: str
    text_entities: List[MessageEntity]
    animation: Animation
# end class Game
