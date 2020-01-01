# -*- coding: utf-8 -*-
from . import updates
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from pytgbot.api_types.receivable import Receivable
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.media import Media

__author__ = 'luckydonald'


class MessageEntity(Result, BaseModel):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    

    Parameters:
    
    :param type: Type of the entity. Can be "mention" (@username), "hashtag" (#hashtag), "cashtag" ($USD), "bot_command" (/start@jobs_bot), "url" (https://telegram.org), "email" (do-not-reply@telegram.org), "phone_number" (+1-212-555-0123), "bold" (bold text), "italic" (italic text), "underline" (underlined text), "strikethrough" (strikethrough text), "code" (monowidth string), "pre" (monowidth block), "text_link" (for clickable text URLs), "text_mention" (for users without usernames)
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
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    type: str
    offset: int
    length: int
    url: str
    user: User
# end class MessageEntity

class PhotoSize(Result, BaseModel):
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
    
    :param file_size: Optional. File size
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

class Audio(Media, BaseModel):
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
    
    :param mime_type: Optional. MIME type of the file as defined by sender
    :type  mime_type: str|unicode
    
    :param file_size: Optional. File size
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
    mime_type: str
    file_size: int
    thumb: PhotoSize
# end class Audio

class Document(Media, BaseModel):
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
    
    :param file_size: Optional. File size
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

class Video(Media, BaseModel):
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
    
    :param mime_type: Optional. Mime type of a file as defined by sender
    :type  mime_type: str|unicode
    
    :param file_size: Optional. File size
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
    mime_type: str
    file_size: int
# end class Video

class Animation(Media, BaseModel):
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
    
    :param file_size: Optional. File size
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

class Voice(Media, BaseModel):
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
    
    :param file_size: Optional. File size
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

class VideoNote(Media, BaseModel):
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
    
    :param file_size: Optional. File size
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

class Contact(Media, BaseModel):
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
    
    :param user_id: Optional. Contact's user identifier in Telegram
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

class Location(Media, BaseModel):
    """
    This object represents a point on the map.

    https://core.telegram.org/bots/api#location
    

    Parameters:
    
    :param longitude: Longitude as defined by sender
    :type  longitude: float
    
    :param latitude: Latitude as defined by sender
    :type  latitude: float
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    longitude: float
    latitude: float
# end class Location

class Venue(Media, BaseModel):
    """
    This object represents a venue.

    https://core.telegram.org/bots/api#venue
    

    Parameters:
    
    :param location: Venue location
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
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    location: Location
    title: str
    address: str
    foursquare_id: str
    foursquare_type: str
# end class Venue

class PollOption(Receivable, BaseModel):
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

class Poll(Media, BaseModel):
    """
    This object contains information about a poll.

    https://core.telegram.org/bots/api#poll
    

    Parameters:
    
    :param id: Unique poll identifier
    :type  id: str|unicode
    
    :param question: Poll question, 1-255 characters
    :type  question: str|unicode
    
    :param options: List of poll options
    :type  options: list of pytgbot.api_types.receivable.media.PollOption
    
    :param is_closed: True, if the poll is closed
    :type  is_closed: bool
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    id: str
    question: str
    options: List[PollOption]
    is_closed: bool
# end class Poll

class UserProfilePhotos(Result, BaseModel):
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

class File(Receivable, BaseModel):
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
    
    :param file_size: Optional. File size, if known
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

class ChatPhoto(Result, BaseModel):
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

class Sticker(Media, BaseModel):
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
    

    Optional keyword parameters:
    
    :param thumb: Optional. Sticker thumbnail in the .webp or .jpg format
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize
    
    :param emoji: Optional. Emoji associated with the sticker
    :type  emoji: str|unicode
    
    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :type  set_name: str|unicode
    
    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :type  mask_position: pytgbot.api_types.receivable.stickers.MaskPosition
    
    :param file_size: Optional. File size
    :type  file_size: int
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    thumb: PhotoSize
    emoji: str
    set_name: str
    mask_position: MaskPosition
    file_size: int
# end class Sticker

class Game(Media, BaseModel):
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
