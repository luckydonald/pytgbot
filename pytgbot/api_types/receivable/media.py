# -*- coding: utf-8 -*-
__all__ = ['Media', 'MessageEntity', 'DownloadableMedia', 'PhotoSize', 'Audio', 'Animation', 'Document', 'Sticker', 'Video', 'Voice', 'VideoNote', 'Contact', 'Location', 'Venue', 'UserProfilePhotos', 'File', 'ChatPhoto', 'Game']

from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Receivable
from . import Result

__author__ = 'luckydonald'


class Media(Receivable):
    """
    parent class for all receivable media.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    pass
# end class Media


class MessageEntity(Result):
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

    :param language: Optional. For "pre" only, the programming language of the entity text
    :type  language: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, type, offset, length, url=None, user=None, language=None, _raw=None):
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

        :param language: Optional. For "pre" only, the programming language of the entity text
        :type  language: str|unicode

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(MessageEntity, self).__init__()
        from .peer import User

        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        assert_type_or_raise(offset, int, parameter_name="offset")
        self.offset = offset
        assert_type_or_raise(length, int, parameter_name="length")
        self.length = length
        assert_type_or_raise(url, None, unicode_type, parameter_name="url")
        self.url = url
        assert_type_or_raise(user, None, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(language, None, unicode_type, parameter_name="language")
        self.language = language

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this MessageEntity to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(MessageEntity, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['offset'] = int(self.offset)  # type int
        array['length'] = int(self.length)  # type int
        if self.url is not None:
            array['url'] = u(self.url)  # py2: type unicode, py3: type str
        # end if
        if self.user is not None:
            array['user'] = self.user.to_array()  # type User
        # end if
        if self.language is not None:
            array['language'] = u(self.language)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the MessageEntity constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User

        data = Result.validate_array(array)
        data['type'] = u(array.get('type'))
        data['offset'] = int(array.get('offset'))
        data['length'] = int(array.get('length'))
        data['url'] = u(array.get('url')) if array.get('url') is not None else None
        data['user'] = User.from_array(array.get('user')) if array.get('user') is not None else None
        data['language'] = u(array.get('language')) if array.get('language') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new MessageEntity from a given dictionary.

        :return: new MessageEntity instance.
        :rtype: MessageEntity
        """
        if not array:  # None or {}
            return None
        # end if

        data = MessageEntity.validate_array(array)
        data['_raw'] = array
        return MessageEntity(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(messageentity_instance)`
        """
        return "MessageEntity(type={self.type!r}, offset={self.offset!r}, length={self.length!r}, url={self.url!r}, user={self.user!r}, language={self.language!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(messageentity_instance)`
        """
        if self._raw:
            return "MessageEntity.from_array({self._raw})".format(self=self)
        # end if
        return "MessageEntity(type={self.type!r}, offset={self.offset!r}, length={self.length!r}, url={self.url!r}, user={self.user!r}, language={self.language!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in messageentity_instance`
        """
        return (
            key in ["type", "offset", "length", "url", "user", "language"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class MessageEntity


class DownloadableMedia(Media):
    @staticmethod
    def validate_array(array):
        """
        Subclass for all :class:`Media` which has a :py:attr:`file_id` and optionally a :py:attr:`file_size`
        :param array: a array to parse
        :type  array: dict
        :return: a dict with file_id and file_size extracted from the array
        :rtype: dict
        """
        data = Media.from_array(array)
        data["file_id"] = array.get("file_id")
        data["file_size"] = array.get("file_size")  # can be None
        return data
# end class DownloadableMedia


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

    :param file_size: Optional. File size
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, width, height, file_size=None, _raw=None):
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
        super(PhotoSize, self).__init__()
        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(width, int, parameter_name="width")
        self.width = width
        assert_type_or_raise(height, int, parameter_name="height")
        self.height = height
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this PhotoSize to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(PhotoSize, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PhotoSize constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PhotoSize from a given dictionary.

        :return: new PhotoSize instance.
        :rtype: PhotoSize
        """
        if not array:  # None or {}
            return None
        # end if

        data = PhotoSize.validate_array(array)
        data['_raw'] = array
        return PhotoSize(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(photosize_instance)`
        """
        return "PhotoSize(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(photosize_instance)`
        """
        if self._raw:
            return "PhotoSize.from_array({self._raw})".format(self=self)
        # end if
        return "PhotoSize(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in photosize_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "width", "height", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param file_size: Optional. File size
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, width, height, duration, thumb=None, file_name=None, mime_type=None, file_size=None, _raw=None):
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
        super(Animation, self).__init__()

        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(width, int, parameter_name="width")
        self.width = width
        assert_type_or_raise(height, int, parameter_name="height")
        self.height = height
        assert_type_or_raise(duration, int, parameter_name="duration")
        self.duration = duration
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb
        assert_type_or_raise(file_name, None, unicode_type, parameter_name="file_name")
        self.file_name = file_name
        assert_type_or_raise(mime_type, None, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Animation to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Animation, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        array['duration'] = int(self.duration)  # type int
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if
        if self.file_name is not None:
            array['file_name'] = u(self.file_name)  # py2: type unicode, py3: type str
        # end if
        if self.mime_type is not None:
            array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Animation constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['duration'] = int(array.get('duration'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['file_name'] = u(array.get('file_name')) if array.get('file_name') is not None else None
        data['mime_type'] = u(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Animation from a given dictionary.

        :return: new Animation instance.
        :rtype: Animation
        """
        if not array:  # None or {}
            return None
        # end if

        data = Animation.validate_array(array)
        data['_raw'] = array
        return Animation(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(animation_instance)`
        """
        return "Animation(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(animation_instance)`
        """
        if self._raw:
            return "Animation.from_array({self._raw})".format(self=self)
        # end if
        return "Animation(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in animation_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "width", "height", "duration", "thumb", "file_name", "mime_type", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param file_size: Optional. File size
    :type  file_size: int

    :param thumb: Optional. Thumbnail of the album cover to which the music file belongs
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, duration, performer=None, title=None, file_name=None, mime_type=None, file_size=None, thumb=None, _raw=None):
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

        :param file_size: Optional. File size
        :type  file_size: int

        :param thumb: Optional. Thumbnail of the album cover to which the music file belongs
        :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Audio, self).__init__()

        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(duration, int, parameter_name="duration")
        self.duration = duration
        assert_type_or_raise(performer, None, unicode_type, parameter_name="performer")
        self.performer = performer
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(file_name, None, unicode_type, parameter_name="file_name")
        self.file_name = file_name
        assert_type_or_raise(mime_type, None, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Audio to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Audio, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['duration'] = int(self.duration)  # type int
        if self.performer is not None:
            array['performer'] = u(self.performer)  # py2: type unicode, py3: type str
        # end if
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.file_name is not None:
            array['file_name'] = u(self.file_name)  # py2: type unicode, py3: type str
        # end if
        if self.mime_type is not None:
            array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Audio constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['duration'] = int(array.get('duration'))
        data['performer'] = u(array.get('performer')) if array.get('performer') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['file_name'] = u(array.get('file_name')) if array.get('file_name') is not None else None
        data['mime_type'] = u(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Audio from a given dictionary.

        :return: new Audio instance.
        :rtype: Audio
        """
        if not array:  # None or {}
            return None
        # end if

        data = Audio.validate_array(array)
        data['_raw'] = array
        return Audio(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(audio_instance)`
        """
        return "Audio(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r}, thumb={self.thumb!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(audio_instance)`
        """
        if self._raw:
            return "Audio.from_array({self._raw})".format(self=self)
        # end if
        return "Audio(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r}, thumb={self.thumb!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in audio_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "duration", "performer", "title", "file_name", "mime_type", "file_size", "thumb"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param file_size: Optional. File size
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, thumb=None, file_name=None, mime_type=None, file_size=None, _raw=None):
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
        super(Document, self).__init__()

        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb
        assert_type_or_raise(file_name, None, unicode_type, parameter_name="file_name")
        self.file_name = file_name
        assert_type_or_raise(mime_type, None, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Document to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Document, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if
        if self.file_name is not None:
            array['file_name'] = u(self.file_name)  # py2: type unicode, py3: type str
        # end if
        if self.mime_type is not None:
            array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Document constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['file_name'] = u(array.get('file_name')) if array.get('file_name') is not None else None
        data['mime_type'] = u(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Document from a given dictionary.

        :return: new Document instance.
        :rtype: Document
        """
        if not array:  # None or {}
            return None
        # end if

        data = Document.validate_array(array)
        data['_raw'] = array
        return Document(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(document_instance)`
        """
        return "Document(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(document_instance)`
        """
        if self._raw:
            return "Document.from_array({self._raw})".format(self=self)
        # end if
        return "Document(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in document_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "thumb", "file_name", "mime_type", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param file_size: Optional. File size
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, width, height, duration, thumb=None, file_name=None, mime_type=None, file_size=None, _raw=None):
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

        :param file_size: Optional. File size
        :type  file_size: int

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Video, self).__init__()

        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(width, int, parameter_name="width")
        self.width = width
        assert_type_or_raise(height, int, parameter_name="height")
        self.height = height
        assert_type_or_raise(duration, int, parameter_name="duration")
        self.duration = duration
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb
        assert_type_or_raise(file_name, None, unicode_type, parameter_name="file_name")
        self.file_name = file_name
        assert_type_or_raise(mime_type, None, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Video to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Video, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        array['duration'] = int(self.duration)  # type int
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if
        if self.file_name is not None:
            array['file_name'] = u(self.file_name)  # py2: type unicode, py3: type str
        # end if
        if self.mime_type is not None:
            array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Video constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['duration'] = int(array.get('duration'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['file_name'] = u(array.get('file_name')) if array.get('file_name') is not None else None
        data['mime_type'] = u(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Video from a given dictionary.

        :return: new Video instance.
        :rtype: Video
        """
        if not array:  # None or {}
            return None
        # end if

        data = Video.validate_array(array)
        data['_raw'] = array
        return Video(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(video_instance)`
        """
        return "Video(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(video_instance)`
        """
        if self._raw:
            return "Video.from_array({self._raw})".format(self=self)
        # end if
        return "Video(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in video_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "width", "height", "duration", "thumb", "file_name", "mime_type", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param file_size: Optional. File size
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, length, duration, thumb=None, file_size=None, _raw=None):
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
        super(VideoNote, self).__init__()

        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(length, int, parameter_name="length")
        self.length = length
        assert_type_or_raise(duration, int, parameter_name="duration")
        self.duration = duration
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this VideoNote to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(VideoNote, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['length'] = int(self.length)  # type int
        array['duration'] = int(self.duration)  # type int
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VideoNote constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['length'] = int(array.get('length'))
        data['duration'] = int(array.get('duration'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VideoNote from a given dictionary.

        :return: new VideoNote instance.
        :rtype: VideoNote
        """
        if not array:  # None or {}
            return None
        # end if

        data = VideoNote.validate_array(array)
        data['_raw'] = array
        return VideoNote(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(videonote_instance)`
        """
        return "VideoNote(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, length={self.length!r}, duration={self.duration!r}, thumb={self.thumb!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(videonote_instance)`
        """
        if self._raw:
            return "VideoNote.from_array({self._raw})".format(self=self)
        # end if
        return "VideoNote(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, length={self.length!r}, duration={self.duration!r}, thumb={self.thumb!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in videonote_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "length", "duration", "thumb", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param file_size: Optional. File size
    :type  file_size: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, file_unique_id, duration, mime_type=None, file_size=None, _raw=None):
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
        super(Voice, self).__init__()
        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(duration, int, parameter_name="duration")
        self.duration = duration
        assert_type_or_raise(mime_type, None, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Voice to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Voice, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['duration'] = int(self.duration)  # type int
        if self.mime_type is not None:
            array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Voice constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['duration'] = int(array.get('duration'))
        data['mime_type'] = u(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Voice from a given dictionary.

        :return: new Voice instance.
        :rtype: Voice
        """
        if not array:  # None or {}
            return None
        # end if

        data = Voice.validate_array(array)
        data['_raw'] = array
        return Voice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voice_instance)`
        """
        return "Voice(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, duration={self.duration!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(voice_instance)`
        """
        if self._raw:
            return "Voice.from_array({self._raw})".format(self=self)
        # end if
        return "Voice(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, duration={self.duration!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in voice_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "duration", "mime_type", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param user_id: Optional. Contact's user identifier in Telegram
    :type  user_id: int

    :param vcard: Optional. Additional data about the contact in the form of a vCard
    :type  vcard: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, phone_number, first_name, last_name=None, user_id=None, vcard=None, _raw=None):
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
        super(Contact, self).__init__()
        assert_type_or_raise(phone_number, unicode_type, parameter_name="phone_number")
        self.phone_number = phone_number
        assert_type_or_raise(first_name, unicode_type, parameter_name="first_name")
        self.first_name = first_name
        assert_type_or_raise(last_name, None, unicode_type, parameter_name="last_name")
        self.last_name = last_name
        assert_type_or_raise(user_id, None, int, parameter_name="user_id")
        self.user_id = user_id
        assert_type_or_raise(vcard, None, unicode_type, parameter_name="vcard")
        self.vcard = vcard

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Contact to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Contact, self).to_array()

        array['phone_number'] = u(self.phone_number)  # py2: type unicode, py3: type str
        array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        # end if
        if self.user_id is not None:
            array['user_id'] = int(self.user_id)  # type int
        # end if
        if self.vcard is not None:
            array['vcard'] = u(self.vcard)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Contact constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Media.validate_array(array)
        data['phone_number'] = u(array.get('phone_number'))
        data['first_name'] = u(array.get('first_name'))
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['user_id'] = int(array.get('user_id')) if array.get('user_id') is not None else None
        data['vcard'] = u(array.get('vcard')) if array.get('vcard') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Contact from a given dictionary.

        :return: new Contact instance.
        :rtype: Contact
        """
        if not array:  # None or {}
            return None
        # end if

        data = Contact.validate_array(array)
        data['_raw'] = array
        return Contact(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(contact_instance)`
        """
        return "Contact(phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, user_id={self.user_id!r}, vcard={self.vcard!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(contact_instance)`
        """
        if self._raw:
            return "Contact.from_array({self._raw})".format(self=self)
        # end if
        return "Contact(phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, user_id={self.user_id!r}, vcard={self.vcard!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in contact_instance`
        """
        return (
            key in ["phone_number", "first_name", "last_name", "user_id", "vcard"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Contact


class Dice(Media):
    """
    This object represents an animated emoji that displays a random value.

    https://core.telegram.org/bots/api#dice


    Parameters:

    :param emoji: Emoji on which the dice throw animation is based
    :type  emoji: str|unicode

    :param value: Value of the dice, 1-6 for "🎲" and "🎯" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji
    :type  value: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, emoji, value, _raw=None):
        """
        This object represents an animated emoji that displays a random value.

        https://core.telegram.org/bots/api#dice


        Parameters:

        :param emoji: Emoji on which the dice throw animation is based
        :type  emoji: str|unicode

        :param value: Value of the dice, 1-6 for "🎲" and "🎯" base emoji, 1-5 for "🏀" and "⚽" base emoji, 1-64 for "🎰" base emoji
        :type  value: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Dice, self).__init__()
        assert_type_or_raise(emoji, unicode_type, parameter_name="emoji")
        self.emoji = emoji
        assert_type_or_raise(value, int, parameter_name="value")
        self.value = value

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Dice to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Dice, self).to_array()

        array['emoji'] = u(self.emoji)  # py2: type unicode, py3: type str
        array['value'] = int(self.value)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Dice constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Media.validate_array(array)
        data['emoji'] = u(array.get('emoji'))
        data['value'] = int(array.get('value'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Dice from a given dictionary.

        :return: new Dice instance.
        :rtype: Dice
        """
        if not array:  # None or {}
            return None
        # end if

        data = Dice.validate_array(array)
        data['_raw'] = array
        return Dice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(dice_instance)`
        """
        return "Dice(emoji={self.emoji!r}, value={self.value!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(dice_instance)`
        """
        if self._raw:
            return "Dice.from_array({self._raw})".format(self=self)
        # end if
        return "Dice(emoji={self.emoji!r}, value={self.value!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in dice_instance`
        """
        return (
            key in ["emoji", "value"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, text, voter_count, _raw=None):
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
        super(PollOption, self).__init__()
        assert_type_or_raise(text, unicode_type, parameter_name="text")
        self.text = text
        assert_type_or_raise(voter_count, int, parameter_name="voter_count")
        self.voter_count = voter_count

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this PollOption to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(PollOption, self).to_array()

        array['text'] = u(self.text)  # py2: type unicode, py3: type str
        array['voter_count'] = int(self.voter_count)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PollOption constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Receivable.validate_array(array)
        data['text'] = u(array.get('text'))
        data['voter_count'] = int(array.get('voter_count'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PollOption from a given dictionary.

        :return: new PollOption instance.
        :rtype: PollOption
        """
        if not array:  # None or {}
            return None
        # end if

        data = PollOption.validate_array(array)
        data['_raw'] = array
        return PollOption(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(polloption_instance)`
        """
        return "PollOption(text={self.text!r}, voter_count={self.voter_count!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(polloption_instance)`
        """
        if self._raw:
            return "PollOption.from_array({self._raw})".format(self=self)
        # end if
        return "PollOption(text={self.text!r}, voter_count={self.voter_count!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in polloption_instance`
        """
        return (
            key in ["text", "voter_count"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, poll_id, user, option_ids, _raw=None):
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
        super(PollAnswer, self).__init__()
        from .peer import User

        assert_type_or_raise(poll_id, unicode_type, parameter_name="poll_id")
        self.poll_id = poll_id
        assert_type_or_raise(user, User, parameter_name="user")
        self.user = user
        assert_type_or_raise(option_ids, list, parameter_name="option_ids")
        self.option_ids = option_ids

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this PollAnswer to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(PollAnswer, self).to_array()

        array['poll_id'] = u(self.poll_id)  # py2: type unicode, py3: type str
        array['user'] = self.user.to_array()  # type User
        array['option_ids'] = self._as_array(self.option_ids)  # type list of int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PollAnswer constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User

        data = Receivable.validate_array(array)
        data['poll_id'] = u(array.get('poll_id'))
        data['user'] = User.from_array(array.get('user'))
        data['option_ids'] = PollAnswer._builtin_from_array_list(required_type=int, value=array.get('option_ids'), list_level=1)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PollAnswer from a given dictionary.

        :return: new PollAnswer instance.
        :rtype: PollAnswer
        """
        if not array:  # None or {}
            return None
        # end if

        data = PollAnswer.validate_array(array)
        data['_raw'] = array
        return PollAnswer(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(pollanswer_instance)`
        """
        return "PollAnswer(poll_id={self.poll_id!r}, user={self.user!r}, option_ids={self.option_ids!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(pollanswer_instance)`
        """
        if self._raw:
            return "PollAnswer.from_array({self._raw})".format(self=self)
        # end if
        return "PollAnswer(poll_id={self.poll_id!r}, user={self.user!r}, option_ids={self.option_ids!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in pollanswer_instance`
        """
        return (
            key in ["poll_id", "user", "option_ids"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class PollAnswer


class Poll(Media):
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

    def __init__(self, id, question, options, total_voter_count, is_closed, is_anonymous, type, allows_multiple_answers, correct_option_id=None, explanation=None, explanation_entities=None, open_period=None, close_date=None, _raw=None):
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
        super(Poll, self).__init__()

        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(question, unicode_type, parameter_name="question")
        self.question = question
        assert_type_or_raise(options, list, parameter_name="options")
        self.options = options
        assert_type_or_raise(total_voter_count, int, parameter_name="total_voter_count")
        self.total_voter_count = total_voter_count
        assert_type_or_raise(is_closed, bool, parameter_name="is_closed")
        self.is_closed = is_closed
        assert_type_or_raise(is_anonymous, bool, parameter_name="is_anonymous")
        self.is_anonymous = is_anonymous
        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        assert_type_or_raise(allows_multiple_answers, bool, parameter_name="allows_multiple_answers")
        self.allows_multiple_answers = allows_multiple_answers
        assert_type_or_raise(correct_option_id, None, int, parameter_name="correct_option_id")
        self.correct_option_id = correct_option_id
        assert_type_or_raise(explanation, None, unicode_type, parameter_name="explanation")
        self.explanation = explanation
        assert_type_or_raise(explanation_entities, None, list, parameter_name="explanation_entities")
        self.explanation_entities = explanation_entities
        assert_type_or_raise(open_period, None, int, parameter_name="open_period")
        self.open_period = open_period
        assert_type_or_raise(close_date, None, int, parameter_name="close_date")
        self.close_date = close_date

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Poll to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Poll, self).to_array()

        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['question'] = u(self.question)  # py2: type unicode, py3: type str
        array['options'] = self._as_array(self.options)  # type list of PollOption
        array['total_voter_count'] = int(self.total_voter_count)  # type int
        array['is_closed'] = bool(self.is_closed)  # type bool
        array['is_anonymous'] = bool(self.is_anonymous)  # type bool
        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['allows_multiple_answers'] = bool(self.allows_multiple_answers)  # type bool
        if self.correct_option_id is not None:
            array['correct_option_id'] = int(self.correct_option_id)  # type int
        # end if
        if self.explanation is not None:
            array['explanation'] = u(self.explanation)  # py2: type unicode, py3: type str
        # end if
        if self.explanation_entities is not None:
            array['explanation_entities'] = self._as_array(self.explanation_entities)  # type list of MessageEntity
        # end if
        if self.open_period is not None:
            array['open_period'] = int(self.open_period)  # type int
        # end if
        if self.close_date is not None:
            array['close_date'] = int(self.close_date)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Poll constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['id'] = u(array.get('id'))
        data['question'] = u(array.get('question'))
        data['options'] = PollOption.from_array_list(array.get('options'), list_level=1)
        data['total_voter_count'] = int(array.get('total_voter_count'))
        data['is_closed'] = bool(array.get('is_closed'))
        data['is_anonymous'] = bool(array.get('is_anonymous'))
        data['type'] = u(array.get('type'))
        data['allows_multiple_answers'] = bool(array.get('allows_multiple_answers'))
        data['correct_option_id'] = int(array.get('correct_option_id')) if array.get('correct_option_id') is not None else None
        data['explanation'] = u(array.get('explanation')) if array.get('explanation') is not None else None
        data['explanation_entities'] = MessageEntity.from_array_list(array.get('explanation_entities'), list_level=1) if array.get('explanation_entities') is not None else None
        data['open_period'] = int(array.get('open_period')) if array.get('open_period') is not None else None
        data['close_date'] = int(array.get('close_date')) if array.get('close_date') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Poll from a given dictionary.

        :return: new Poll instance.
        :rtype: Poll
        """
        if not array:  # None or {}
            return None
        # end if

        data = Poll.validate_array(array)
        data['_raw'] = array
        return Poll(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(poll_instance)`
        """
        return "Poll(id={self.id!r}, question={self.question!r}, options={self.options!r}, total_voter_count={self.total_voter_count!r}, is_closed={self.is_closed!r}, is_anonymous={self.is_anonymous!r}, type={self.type!r}, allows_multiple_answers={self.allows_multiple_answers!r}, correct_option_id={self.correct_option_id!r}, explanation={self.explanation!r}, explanation_entities={self.explanation_entities!r}, open_period={self.open_period!r}, close_date={self.close_date!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(poll_instance)`
        """
        if self._raw:
            return "Poll.from_array({self._raw})".format(self=self)
        # end if
        return "Poll(id={self.id!r}, question={self.question!r}, options={self.options!r}, total_voter_count={self.total_voter_count!r}, is_closed={self.is_closed!r}, is_anonymous={self.is_anonymous!r}, type={self.type!r}, allows_multiple_answers={self.allows_multiple_answers!r}, correct_option_id={self.correct_option_id!r}, explanation={self.explanation!r}, explanation_entities={self.explanation_entities!r}, open_period={self.open_period!r}, close_date={self.close_date!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in poll_instance`
        """
        return (
            key in ["id", "question", "options", "total_voter_count", "is_closed", "is_anonymous", "type", "allows_multiple_answers", "correct_option_id", "explanation", "explanation_entities", "open_period", "close_date"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param live_period: Optional. Time relative to the message sending date, during which the location can be updated, in seconds. For active live locations only.
    :type  live_period: int

    :param heading: Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    :type  heading: int

    :param proximity_alert_radius: Optional. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    :type  proximity_alert_radius: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, longitude, latitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, _raw=None):
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

        :param live_period: Optional. Time relative to the message sending date, during which the location can be updated, in seconds. For active live locations only.
        :type  live_period: int

        :param heading: Optional. The direction in which user is moving, in degrees; 1-360. For active live locations only.
        :type  heading: int

        :param proximity_alert_radius: Optional. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
        :type  proximity_alert_radius: int

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Location, self).__init__()
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        assert_type_or_raise(horizontal_accuracy, None, float, parameter_name="horizontal_accuracy")
        self.horizontal_accuracy = horizontal_accuracy
        assert_type_or_raise(live_period, None, int, parameter_name="live_period")
        self.live_period = live_period
        assert_type_or_raise(heading, None, int, parameter_name="heading")
        self.heading = heading
        assert_type_or_raise(proximity_alert_radius, None, int, parameter_name="proximity_alert_radius")
        self.proximity_alert_radius = proximity_alert_radius

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Location to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Location, self).to_array()

        array['longitude'] = float(self.longitude)  # type float
        array['latitude'] = float(self.latitude)  # type float
        if self.horizontal_accuracy is not None:
            array['horizontal_accuracy'] = float(self.horizontal_accuracy)  # type float
        # end if
        if self.live_period is not None:
            array['live_period'] = int(self.live_period)  # type int
        # end if
        if self.heading is not None:
            array['heading'] = int(self.heading)  # type int
        # end if
        if self.proximity_alert_radius is not None:
            array['proximity_alert_radius'] = int(self.proximity_alert_radius)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Location constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Media.validate_array(array)
        data['longitude'] = float(array.get('longitude'))
        data['latitude'] = float(array.get('latitude'))
        data['horizontal_accuracy'] = float(array.get('horizontal_accuracy')) if array.get('horizontal_accuracy') is not None else None
        data['live_period'] = int(array.get('live_period')) if array.get('live_period') is not None else None
        data['heading'] = int(array.get('heading')) if array.get('heading') is not None else None
        data['proximity_alert_radius'] = int(array.get('proximity_alert_radius')) if array.get('proximity_alert_radius') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Location from a given dictionary.

        :return: new Location instance.
        :rtype: Location
        """
        if not array:  # None or {}
            return None
        # end if

        data = Location.validate_array(array)
        data['_raw'] = array
        return Location(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(location_instance)`
        """
        return "Location(longitude={self.longitude!r}, latitude={self.latitude!r}, horizontal_accuracy={self.horizontal_accuracy!r}, live_period={self.live_period!r}, heading={self.heading!r}, proximity_alert_radius={self.proximity_alert_radius!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(location_instance)`
        """
        if self._raw:
            return "Location.from_array({self._raw})".format(self=self)
        # end if
        return "Location(longitude={self.longitude!r}, latitude={self.latitude!r}, horizontal_accuracy={self.horizontal_accuracy!r}, live_period={self.live_period!r}, heading={self.heading!r}, proximity_alert_radius={self.proximity_alert_radius!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in location_instance`
        """
        return (
            key in ["longitude", "latitude", "horizontal_accuracy", "live_period", "heading", "proximity_alert_radius"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, location, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, _raw=None):
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
        super(Venue, self).__init__()

        assert_type_or_raise(location, Location, parameter_name="location")
        self.location = location
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(address, unicode_type, parameter_name="address")
        self.address = address
        assert_type_or_raise(foursquare_id, None, unicode_type, parameter_name="foursquare_id")
        self.foursquare_id = foursquare_id
        assert_type_or_raise(foursquare_type, None, unicode_type, parameter_name="foursquare_type")
        self.foursquare_type = foursquare_type
        assert_type_or_raise(google_place_id, None, unicode_type, parameter_name="google_place_id")
        self.google_place_id = google_place_id
        assert_type_or_raise(google_place_type, None, unicode_type, parameter_name="google_place_type")
        self.google_place_type = google_place_type

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Venue to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Venue, self).to_array()

        array['location'] = self.location.to_array()  # type Location
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['address'] = u(self.address)  # py2: type unicode, py3: type str
        if self.foursquare_id is not None:
            array['foursquare_id'] = u(self.foursquare_id)  # py2: type unicode, py3: type str
        # end if
        if self.foursquare_type is not None:
            array['foursquare_type'] = u(self.foursquare_type)  # py2: type unicode, py3: type str
        # end if
        if self.google_place_id is not None:
            array['google_place_id'] = u(self.google_place_id)  # py2: type unicode, py3: type str
        # end if
        if self.google_place_type is not None:
            array['google_place_type'] = u(self.google_place_type)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Venue constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['location'] = Location.from_array(array.get('location'))
        data['title'] = u(array.get('title'))
        data['address'] = u(array.get('address'))
        data['foursquare_id'] = u(array.get('foursquare_id')) if array.get('foursquare_id') is not None else None
        data['foursquare_type'] = u(array.get('foursquare_type')) if array.get('foursquare_type') is not None else None
        data['google_place_id'] = u(array.get('google_place_id')) if array.get('google_place_id') is not None else None
        data['google_place_type'] = u(array.get('google_place_type')) if array.get('google_place_type') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Venue from a given dictionary.

        :return: new Venue instance.
        :rtype: Venue
        """
        if not array:  # None or {}
            return None
        # end if

        data = Venue.validate_array(array)
        data['_raw'] = array
        return Venue(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(venue_instance)`
        """
        return "Venue(location={self.location!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, google_place_id={self.google_place_id!r}, google_place_type={self.google_place_type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(venue_instance)`
        """
        if self._raw:
            return "Venue.from_array({self._raw})".format(self=self)
        # end if
        return "Venue(location={self.location!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, google_place_id={self.google_place_id!r}, google_place_type={self.google_place_type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in venue_instance`
        """
        return (
            key in ["location", "title", "address", "foursquare_id", "foursquare_type", "google_place_id", "google_place_type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Venue


class ProximityAlertTriggered(Media):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    https://core.telegram.org/bots/api#proximityalerttriggered


    Parameters:

    :param traveler: User that triggered the alert
    :type  traveler: pytgbot.api_types.receivable.peer.User

    :param watcher: User that set the alert
    :type  watcher: pytgbot.api_types.receivable.peer.User

    :param distance: The distance between the users
    :type  distance: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, traveler, watcher, distance, _raw=None):
        """
        This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

        https://core.telegram.org/bots/api#proximityalerttriggered


        Parameters:

        :param traveler: User that triggered the alert
        :type  traveler: pytgbot.api_types.receivable.peer.User

        :param watcher: User that set the alert
        :type  watcher: pytgbot.api_types.receivable.peer.User

        :param distance: The distance between the users
        :type  distance: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ProximityAlertTriggered, self).__init__()
        from .peer import User

        assert_type_or_raise(traveler, User, parameter_name="traveler")
        self.traveler = traveler
        assert_type_or_raise(watcher, User, parameter_name="watcher")
        self.watcher = watcher
        assert_type_or_raise(distance, int, parameter_name="distance")
        self.distance = distance

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ProximityAlertTriggered to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ProximityAlertTriggered, self).to_array()

        array['traveler'] = self.traveler.to_array()  # type User
        array['watcher'] = self.watcher.to_array()  # type User
        array['distance'] = int(self.distance)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ProximityAlertTriggered constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User

        data = Media.validate_array(array)
        data['traveler'] = User.from_array(array.get('traveler'))
        data['watcher'] = User.from_array(array.get('watcher'))
        data['distance'] = int(array.get('distance'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ProximityAlertTriggered from a given dictionary.

        :return: new ProximityAlertTriggered instance.
        :rtype: ProximityAlertTriggered
        """
        if not array:  # None or {}
            return None
        # end if

        data = ProximityAlertTriggered.validate_array(array)
        data['_raw'] = array
        return ProximityAlertTriggered(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(proximityalerttriggered_instance)`
        """
        return "ProximityAlertTriggered(traveler={self.traveler!r}, watcher={self.watcher!r}, distance={self.distance!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(proximityalerttriggered_instance)`
        """
        if self._raw:
            return "ProximityAlertTriggered.from_array({self._raw})".format(self=self)
        # end if
        return "ProximityAlertTriggered(traveler={self.traveler!r}, watcher={self.watcher!r}, distance={self.distance!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in proximityalerttriggered_instance`
        """
        return (
            key in ["traveler", "watcher", "distance"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ProximityAlertTriggered


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

    def __init__(self, total_count, photos, _raw=None):
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
        super(UserProfilePhotos, self).__init__()

        assert_type_or_raise(total_count, int, parameter_name="total_count")
        self.total_count = total_count
        assert_type_or_raise(photos, list, parameter_name="photos")
        self.photos = photos

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this UserProfilePhotos to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(UserProfilePhotos, self).to_array()

        array['total_count'] = int(self.total_count)  # type int
        array['photos'] = self._as_array(self.photos)  # type list of list of PhotoSize

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the UserProfilePhotos constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Result.validate_array(array)
        data['total_count'] = int(array.get('total_count'))
        data['photos'] = PhotoSize.from_array_list(array.get('photos'), list_level=2)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new UserProfilePhotos from a given dictionary.

        :return: new UserProfilePhotos instance.
        :rtype: UserProfilePhotos
        """
        if not array:  # None or {}
            return None
        # end if

        data = UserProfilePhotos.validate_array(array)
        data['_raw'] = array
        return UserProfilePhotos(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(userprofilephotos_instance)`
        """
        return "UserProfilePhotos(total_count={self.total_count!r}, photos={self.photos!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(userprofilephotos_instance)`
        """
        if self._raw:
            return "UserProfilePhotos.from_array({self._raw})".format(self=self)
        # end if
        return "UserProfilePhotos(total_count={self.total_count!r}, photos={self.photos!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in userprofilephotos_instance`
        """
        return (
            key in ["total_count", "photos"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class UserProfilePhotos


class File(Receivable):
    """
    This object represents a file ready to be downloaded.
    The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>.
    It is guaranteed that the link will be valid for at least 1 hour.
    When the link expires, a new one can be requested by calling getFile.

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

    def __init__(self, file_id, file_unique_id, file_size=None, file_path=None, _raw=None):
        """
        This object represents a file ready to be downloaded.
        The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>.
        It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling getFile.

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
        super(File, self).__init__()
        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size
        assert_type_or_raise(file_path, None, unicode_type, parameter_name="file_path")
        self.file_path = file_path

        self._raw = _raw
    # end def __init__

    def get_download_url(self, token):
        """
        Creates a url to download the file.

        Note: Contains the secret API key, so you should not share this url!

        :param token: API key
        :type  token: str

        :return: url
        :rtype: str
        """
        return "https://api.telegram.org/file/bot{token}/{file_path}".format(token=token, file_path=self.file_path)
    # end def get_download_url

    def to_array(self, prefer_original=False):
        """
        Serializes this File to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(File, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if
        if self.file_path is not None:
            array['file_path'] = u(self.file_path)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the File constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Receivable.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        data['file_path'] = u(array.get('file_path')) if array.get('file_path') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new File from a given dictionary.

        :return: new File instance.
        :rtype: File
        """
        if not array:  # None or {}
            return None
        # end if

        data = File.validate_array(array)
        data['_raw'] = array
        return File(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(file_instance)`
        """
        return "File(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, file_size={self.file_size!r}, file_path={self.file_path!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(file_instance)`
        """
        if self._raw:
            return "File.from_array({self._raw})".format(self=self)
        # end if
        return "File(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, file_size={self.file_size!r}, file_path={self.file_path!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in file_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "file_size", "file_path"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, small_file_id, small_file_unique_id, big_file_id, big_file_unique_id, _raw=None):
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
        super(ChatPhoto, self).__init__()
        assert_type_or_raise(small_file_id, unicode_type, parameter_name="small_file_id")
        self.small_file_id = small_file_id
        assert_type_or_raise(small_file_unique_id, unicode_type, parameter_name="small_file_unique_id")
        self.small_file_unique_id = small_file_unique_id
        assert_type_or_raise(big_file_id, unicode_type, parameter_name="big_file_id")
        self.big_file_id = big_file_id
        assert_type_or_raise(big_file_unique_id, unicode_type, parameter_name="big_file_unique_id")
        self.big_file_unique_id = big_file_unique_id

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ChatPhoto to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ChatPhoto, self).to_array()

        array['small_file_id'] = u(self.small_file_id)  # py2: type unicode, py3: type str
        array['small_file_unique_id'] = u(self.small_file_unique_id)  # py2: type unicode, py3: type str
        array['big_file_id'] = u(self.big_file_id)  # py2: type unicode, py3: type str
        array['big_file_unique_id'] = u(self.big_file_unique_id)  # py2: type unicode, py3: type str

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatPhoto constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['small_file_id'] = u(array.get('small_file_id'))
        data['small_file_unique_id'] = u(array.get('small_file_unique_id'))
        data['big_file_id'] = u(array.get('big_file_id'))
        data['big_file_unique_id'] = u(array.get('big_file_unique_id'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatPhoto from a given dictionary.

        :return: new ChatPhoto instance.
        :rtype: ChatPhoto
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatPhoto.validate_array(array)
        data['_raw'] = array
        return ChatPhoto(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatphoto_instance)`
        """
        return "ChatPhoto(small_file_id={self.small_file_id!r}, small_file_unique_id={self.small_file_unique_id!r}, big_file_id={self.big_file_id!r}, big_file_unique_id={self.big_file_unique_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatphoto_instance)`
        """
        if self._raw:
            return "ChatPhoto.from_array({self._raw})".format(self=self)
        # end if
        return "ChatPhoto(small_file_id={self.small_file_id!r}, small_file_unique_id={self.small_file_unique_id!r}, big_file_id={self.big_file_id!r}, big_file_unique_id={self.big_file_unique_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatphoto_instance`
        """
        return (
            key in ["small_file_id", "small_file_unique_id", "big_file_id", "big_file_unique_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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


    Optional keyword parameters:

    :param thumb: Optional. Sticker thumbnail in the .WEBP or .JPG format
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

    def __init__(self, file_id, file_unique_id, width, height, is_animated, thumb=None, emoji=None, set_name=None, mask_position=None, file_size=None, _raw=None):
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

        :param thumb: Optional. Sticker thumbnail in the .WEBP or .JPG format
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
        super(Sticker, self).__init__()
        from .stickers import MaskPosition

        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        assert_type_or_raise(file_unique_id, unicode_type, parameter_name="file_unique_id")
        self.file_unique_id = file_unique_id
        assert_type_or_raise(width, int, parameter_name="width")
        self.width = width
        assert_type_or_raise(height, int, parameter_name="height")
        self.height = height
        assert_type_or_raise(is_animated, bool, parameter_name="is_animated")
        self.is_animated = is_animated
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb
        assert_type_or_raise(emoji, None, unicode_type, parameter_name="emoji")
        self.emoji = emoji
        assert_type_or_raise(set_name, None, unicode_type, parameter_name="set_name")
        self.set_name = set_name
        assert_type_or_raise(mask_position, None, MaskPosition, parameter_name="mask_position")
        self.mask_position = mask_position
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Sticker to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Sticker, self).to_array()

        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['file_unique_id'] = u(self.file_unique_id)  # py2: type unicode, py3: type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        array['is_animated'] = bool(self.is_animated)  # type bool
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if
        if self.emoji is not None:
            array['emoji'] = u(self.emoji)  # py2: type unicode, py3: type str
        # end if
        if self.set_name is not None:
            array['set_name'] = u(self.set_name)  # py2: type unicode, py3: type str
        # end if
        if self.mask_position is not None:
            array['mask_position'] = self.mask_position.to_array()  # type MaskPosition
        # end if
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Sticker constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .stickers import MaskPosition

        data = Media.validate_array(array)
        data['file_id'] = u(array.get('file_id'))
        data['file_unique_id'] = u(array.get('file_unique_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['is_animated'] = bool(array.get('is_animated'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['emoji'] = u(array.get('emoji')) if array.get('emoji') is not None else None
        data['set_name'] = u(array.get('set_name')) if array.get('set_name') is not None else None
        data['mask_position'] = MaskPosition.from_array(array.get('mask_position')) if array.get('mask_position') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Sticker from a given dictionary.

        :return: new Sticker instance.
        :rtype: Sticker
        """
        if not array:  # None or {}
            return None
        # end if

        data = Sticker.validate_array(array)
        data['_raw'] = array
        return Sticker(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(sticker_instance)`
        """
        return "Sticker(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, is_animated={self.is_animated!r}, thumb={self.thumb!r}, emoji={self.emoji!r}, set_name={self.set_name!r}, mask_position={self.mask_position!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(sticker_instance)`
        """
        if self._raw:
            return "Sticker.from_array({self._raw})".format(self=self)
        # end if
        return "Sticker(file_id={self.file_id!r}, file_unique_id={self.file_unique_id!r}, width={self.width!r}, height={self.height!r}, is_animated={self.is_animated!r}, thumb={self.thumb!r}, emoji={self.emoji!r}, set_name={self.set_name!r}, mask_position={self.mask_position!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in sticker_instance`
        """
        return (
            key in ["file_id", "file_unique_id", "width", "height", "is_animated", "thumb", "emoji", "set_name", "mask_position", "file_size"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, title, description, photo, text=None, text_entities=None, animation=None, _raw=None):
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
        super(Game, self).__init__()

        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(description, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(photo, list, parameter_name="photo")
        self.photo = photo
        assert_type_or_raise(text, None, unicode_type, parameter_name="text")
        self.text = text
        assert_type_or_raise(text_entities, None, list, parameter_name="text_entities")
        self.text_entities = text_entities
        assert_type_or_raise(animation, None, Animation, parameter_name="animation")
        self.animation = animation

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Game to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Game, self).to_array()

        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['description'] = u(self.description)  # py2: type unicode, py3: type str
        array['photo'] = self._as_array(self.photo)  # type list of PhotoSize
        if self.text is not None:
            array['text'] = u(self.text)  # py2: type unicode, py3: type str
        # end if
        if self.text_entities is not None:
            array['text_entities'] = self._as_array(self.text_entities)  # type list of MessageEntity
        # end if
        if self.animation is not None:
            array['animation'] = self.animation.to_array()  # type Animation
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Game constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Media.validate_array(array)
        data['title'] = u(array.get('title'))
        data['description'] = u(array.get('description'))
        data['photo'] = PhotoSize.from_array_list(array.get('photo'), list_level=1)
        data['text'] = u(array.get('text')) if array.get('text') is not None else None
        data['text_entities'] = MessageEntity.from_array_list(array.get('text_entities'), list_level=1) if array.get('text_entities') is not None else None
        data['animation'] = Animation.from_array(array.get('animation')) if array.get('animation') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Game from a given dictionary.

        :return: new Game instance.
        :rtype: Game
        """
        if not array:  # None or {}
            return None
        # end if

        data = Game.validate_array(array)
        data['_raw'] = array
        return Game(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(game_instance)`
        """
        return "Game(title={self.title!r}, description={self.description!r}, photo={self.photo!r}, text={self.text!r}, text_entities={self.text_entities!r}, animation={self.animation!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(game_instance)`
        """
        if self._raw:
            return "Game.from_array({self._raw})".format(self=self)
        # end if
        return "Game(title={self.title!r}, description={self.description!r}, photo={self.photo!r}, text={self.text!r}, text_entities={self.text_entities!r}, animation={self.animation!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in game_instance`
        """
        return (
            key in ["title", "description", "photo", "text", "text_entities", "animation"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Game

