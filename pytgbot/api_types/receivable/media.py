# -*- coding: utf-8 -*-
__all__ = ["Media", "PhotoSize", "Audio", "MessageEntity"]

from . import Receivable, Result


class Media(Receivable):
    pass


class MessageEntity(Result):
    """
    This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    https://core.telegram.org/bots/api#messageentity
    """
    def __init__(self, type, offset, length, url=None, user=None):
        """
        This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

        https://core.telegram.org/bots/api#messageentity


        Parameters:

        :param type: Type of the entity. Can be mention (@username), hashtag, bot_command, url, email, bold (bold text), italic (italic text), code (monowidth string), pre (monowidth block), text_link (for clickable text URLs), text_mention (for users without usernames)
        :type  type: str

        :param offset: Offset in UTF-16 code units to the start of the entity
        :type  offset: int

        :param length: Length of the entity in UTF-16 code units
        :type  length: int


        Optional keyword parameters:

        :keyword url: Optional. For “text_link” only, url that will be opened after user taps on the text
        :type    url: str

        :keyword user: Optional. For “text_mention” only, the mentioned user
        :type    user: pytgbot.api_types.receivable.peer.User
        """
        super(MessageEntity, self).__init__()
        from pytgbot.api_types.receivable.peer import User

        assert(type is not None)
        assert(isinstance(type, str))
        self.type = type

        assert(offset is not None)
        assert(isinstance(offset, int))
        self.offset = offset

        assert(length is not None)
        assert(isinstance(length, int))
        self.length = length

        assert(url is None or isinstance(url, str))
        self.url = url

        assert(user is None or isinstance(user, User))
        self.user = user
    # end def __init__

    def to_array(self):
        """
        Serializes this MessageEntity to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(MessageEntity, self).to_array()
        array['type'] = str(self.type)  # type str
        array['offset'] = int(self.offset)  # type int
        array['length'] = int(self.length)  # type int
        if self.url is not None:
            array['url'] = str(self.url)  # type str
        if self.user is not None:
            array['user'] = self.user.to_array()  # type User
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new MessageEntity from a given dictionary.

        :return: new MessageEntity instance.
        :rtype: MessageEntity
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.receivable.peer import User

        data = {}
        data['type'] = str(array.get('type'))
        data['offset'] = int(array.get('offset'))
        data['length'] = int(array.get('length'))
        data['url'] = str(array.get('url')) if array.get('url') is not None else None
        data['user'] = User.from_array(array.get('user')) if array.get('user') is not None else None
        return MessageEntity(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(messageentity_instance)`
        """
        return "MessageEntity(type={self.type!r}, offset={self.offset!r}, length={self.length!r}, url={self.url!r}, user={self.user!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        return self.__str__()
    # end def _repr__

    def __contains__(self, key):
        """
        Implements `"key" in messageentity_instance`
        """
        return key in ["type", "offset", "length", "url", "user"]
    # end def __contains__
# end class MessageEntity

class DownloadableMedia(Media):
    @staticmethod
    def from_array(array):
        """
        Subclass for all :class:`Media` which has a :py:attr:`file_id` and optionally a :def:`file_size`
        :param array: a array to parse
        :type  array: dict
        :return: a dict with file_id and file_size extracted from the array
        :rtype: dict
        """
        data = super(DownloadableMedia).from_array(array)
        data["file_id"] = array.get("file_id")
        data["file_size"] = array.get("file_size")  # can be None
        return data
# end class DownloadableMedia

class PhotoSize(Result):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize
    """
    def __init__(self, file_id, width, height, file_size=None):
        """
        This object represents one size of a photo or a file / sticker thumbnail.

        https://core.telegram.org/bots/api#photosize


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str

        :param width: Photo width
        :type  width: int

        :param height: Photo height
        :type  height: int


        Optional keyword parameters:

        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(PhotoSize, self).__init__()
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(width is not None)
        assert(isinstance(width, int))
        self.width = width
        
        assert(height is not None)
        assert(isinstance(height, int))
        self.height = height
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        """
        Serializes this PhotoSize to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(PhotoSize, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new PhotoSize from a given dictionary.

        :return: new PhotoSize instance.
        :rtype: PhotoSize
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return PhotoSize(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(photosize_instance)`
        """
        return "PhotoSize(file_id={self.file_id!r}, width={self.width!r}, height={self.height!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in photosize_instance`
        """
        return key in ["file_id", "width", "height", "file_size"]
    # end def __contains__
# end class PhotoSize


class Audio(Media):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio
    """
    def __init__(self, file_id, duration, performer=None, title=None, mime_type=None, file_size=None):
        """
        This object represents an audio file to be treated as music by the Telegram clients.

        https://core.telegram.org/bots/api#audio


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str

        :param duration: Duration of the audio in seconds as defined by sender
        :type  duration: int


        Optional keyword parameters:

        :keyword performer: Optional. Performer of the audio as defined by sender or by audio tags
        :type    performer: str

        :keyword title: Optional. Title of the audio as defined by sender or by audio tags
        :type    title: str

        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type: str

        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(Audio, self).__init__()
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(duration is not None)
        assert(isinstance(duration, int))
        self.duration = duration
        
        assert(performer is None or isinstance(performer, str))
        self.performer = performer
        
        assert(title is None or isinstance(title, str))
        self.title = title
        
        assert(mime_type is None or isinstance(mime_type, str))
        self.mime_type = mime_type
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        """
        Serializes this Audio to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Audio, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        array['duration'] = int(self.duration)  # type int
        if self.performer is not None:
            array['performer'] = str(self.performer)  # type str
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.mime_type is not None:
            array['mime_type'] = str(self.mime_type)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Audio from a given dictionary.

        :return: new Audio instance.
        :rtype: Audio
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['duration'] = int(array.get('duration'))
        data['performer'] = str(array.get('performer')) if array.get('performer') is not None else None
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['mime_type'] = str(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return Audio(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(audio_instance)`
        """
        return "Audio(file_id={self.file_id!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in audio_instance`
        """
        return key in ["file_id", "duration", "performer", "title", "mime_type", "file_size"]
    # end def __contains__
# end class Audio


class Document(Media):
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document
    """
    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None, file_size=None):
        """
        This object represents a general file (as opposed to photos, voice messages and audio files).

        https://core.telegram.org/bots/api#document


        Parameters:

        :param file_id: Unique file identifier
        :type  file_id: str


        Optional keyword parameters:

        :keyword thumb: Optional. Document thumbnail as defined by sender
        :type    thumb: pytgbot.api_types.receivable.media.PhotoSize

        :keyword file_name: Optional. Original filename as defined by sender
        :type    file_name: str

        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type: str

        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(Document, self).__init__()
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(thumb is None or isinstance(thumb, PhotoSize))
        self.thumb = thumb
        
        assert(file_name is None or isinstance(file_name, str))
        self.file_name = file_name
        
        assert(mime_type is None or isinstance(mime_type, str))
        self.mime_type = mime_type
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        """
        Serializes this Document to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Document, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        if self.file_name is not None:
            array['file_name'] = str(self.file_name)  # type str
        if self.mime_type is not None:
            array['mime_type'] = str(self.mime_type)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Document from a given dictionary.

        :return: new Document instance.
        :rtype: Document
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['file_name'] = str(array.get('file_name')) if array.get('file_name') is not None else None
        data['mime_type'] = str(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return Document(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(document_instance)`
        """
        return "Document(file_id={self.file_id!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in document_instance`
        """
        return key in ["file_id", "thumb", "file_name", "mime_type", "file_size"]
    # end def __contains__
# end class Document


class Sticker(Media):
    """
    This object represents a sticker.

    https://core.telegram.org/bots/api#sticker
    """
    def __init__(self, file_id, width, height, thumb=None, emoji=None, file_size=None):
        """
        This object represents a sticker.

        https://core.telegram.org/bots/api#sticker


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str

        :param width: Sticker width
        :type  width: int

        :param height: Sticker height
        :type  height: int


        Optional keyword parameters:

        :keyword thumb: Optional. Sticker thumbnail in .webp or .jpg format
        :type    thumb: pytgbot.api_types.receivable.media.PhotoSize

        :keyword emoji: Optional. Emoji associated with the sticker
        :type    emoji: str

        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(Sticker, self).__init__()
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(width is not None)
        assert(isinstance(width, int))
        self.width = width
        
        assert(height is not None)
        assert(isinstance(height, int))
        self.height = height
        
        assert(thumb is None or isinstance(thumb, PhotoSize))
        self.thumb = thumb
        
        assert(emoji is None or isinstance(emoji, str))
        self.emoji = emoji

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
        self.mime_type = "image/webp"
    # end def __init__

    def to_array(self):
        """
        Serializes this Sticker to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Sticker, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        if self.emoji is not None:
            array['emoji'] = str(self.emoji)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Sticker from a given dictionary.

        :return: new Sticker instance.
        :rtype: Sticker
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['emoji'] = str(array.get('emoji')) if array.get('emoji') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return Sticker(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(sticker_instance)`
        """
        return "Sticker(file_id={self.file_id!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, emoji={self.emoji!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in sticker_instance`
        """
        return key in ["file_id", "width", "height", "thumb", "emoji", "file_size"]
    # end def __contains__
# end class Sticker


class Video(Media):
    """
    This object represents a video file.

    https://core.telegram.org/bots/api#video
    """
    def __init__(self, file_id, width, height, duration, thumb=None, mime_type=None, file_size=None):
        """
        This object represents a video file.

        https://core.telegram.org/bots/api#video


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str

        :param width: Video width as defined by sender
        :type  width: int

        :param height: Video height as defined by sender
        :type  height: int

        :param duration: Duration of the video in seconds as defined by sender
        :type  duration: int


        Optional keyword parameters:

        :keyword thumb: Optional. Video thumbnail
        :type    thumb: pytgbot.api_types.receivable.media.PhotoSize

        :keyword mime_type: Optional. Mime type of a file as defined by sender
        :type    mime_type: str

        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(Video, self).__init__()
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(width is not None)
        assert(isinstance(width, int))
        self.width = width
        
        assert(height is not None)
        assert(isinstance(height, int))
        self.height = height
        
        assert(duration is not None)
        assert(isinstance(duration, int))
        self.duration = duration
        
        assert(thumb is None or isinstance(thumb, PhotoSize))
        self.thumb = thumb
        
        assert(mime_type is None or isinstance(mime_type, str))
        self.mime_type = mime_type
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        """
        Serializes this Video to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Video, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        array['duration'] = int(self.duration)  # type int
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        if self.mime_type is not None:
            array['mime_type'] = str(self.mime_type)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Video from a given dictionary.

        :return: new Video instance.
        :rtype: Video
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['duration'] = int(array.get('duration'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['mime_type'] = str(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return Video(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(video_instance)`
        """
        return "Video(file_id={self.file_id!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, thumb={self.thumb!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in video_instance`
        """
        return key in ["file_id", "width", "height", "duration", "thumb", "mime_type", "file_size"]
    # end def __contains__
# end class Video


class Voice(Media):
    """
    This object represents a voice note.

    https://core.telegram.org/bots/api#voice
    """
    def __init__(self, file_id, duration, mime_type=None, file_size=None):
        """
        This object represents a voice note.

        https://core.telegram.org/bots/api#voice


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str

        :param duration: Duration of the audio in seconds as defined by sender
        :type  duration: int


        Optional keyword parameters:

        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type: str

        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(Voice, self).__init__()
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(duration is not None)
        assert(isinstance(duration, int))
        self.duration = duration
        
        assert(mime_type is None or isinstance(mime_type, str))
        self.mime_type = mime_type
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        """
        Serializes this Voice to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Voice, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        array['duration'] = int(self.duration)  # type int
        if self.mime_type is not None:
            array['mime_type'] = str(self.mime_type)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Voice from a given dictionary.

        :return: new Voice instance.
        :rtype: Voice
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['duration'] = int(array.get('duration'))
        data['mime_type'] = str(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return Voice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voice_instance)`
        """
        return "Voice(file_id={self.file_id!r}, duration={self.duration!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in voice_instance`
        """
        return key in ["file_id", "duration", "mime_type", "file_size"]
    # end def __contains__
# end class Voice


class Contact(Media):
    """
    This object represents a phone contact.

    https://core.telegram.org/bots/api#contact
    """
    def __init__(self, phone_number, first_name, last_name=None, user_id=None):
        """
        This object represents a phone contact.

        https://core.telegram.org/bots/api#contact


        Parameters:

        :param phone_number: Contact's phone number
        :type  phone_number: str

        :param first_name: Contact's first name
        :type  first_name: str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name: str

        :keyword user_id: Optional. Contact's user identifier in Telegram
        :type    user_id: int
        """
        super(Contact, self).__init__()
        assert(phone_number is not None)
        assert(isinstance(phone_number, str))
        self.phone_number = phone_number
        
        assert(first_name is not None)
        assert(isinstance(first_name, str))
        self.first_name = first_name
        
        assert(last_name is None or isinstance(last_name, str))
        self.last_name = last_name
        
        assert(user_id is None or isinstance(user_id, int))
        self.user_id = user_id
    # end def __init__

    def to_array(self):
        """
        Serializes this Contact to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Contact, self).to_array()
        array['phone_number'] = str(self.phone_number)  # type str
        array['first_name'] = str(self.first_name)  # type str
        if self.last_name is not None:
            array['last_name'] = str(self.last_name)  # type str
        if self.user_id is not None:
            array['user_id'] = int(self.user_id)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Contact from a given dictionary.

        :return: new Contact instance.
        :rtype: Contact
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['phone_number'] = str(array.get('phone_number'))
        data['first_name'] = str(array.get('first_name'))
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        data['user_id'] = int(array.get('user_id')) if array.get('user_id') is not None else None
        return Contact(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(contact_instance)`
        """
        return "Contact(phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, user_id={self.user_id!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in contact_instance`
        """
        return key in ["phone_number", "first_name", "last_name", "user_id"]
    # end def __contains__
# end class Contact


class Location(Media):
    """
    This object represents a point on the map.

    https://core.telegram.org/bots/api#location
    """
    def __init__(self, longitude, latitude):
        """
        This object represents a point on the map.

        https://core.telegram.org/bots/api#location


        Parameters:

        :param longitude: Longitude as defined by sender
        :type  longitude: float

        :param latitude: Latitude as defined by sender
        :type  latitude: float
        """
        super(Location, self).__init__()
        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude
        
        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude
    # end def __init__

    def to_array(self):
        """
        Serializes this Location to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Location, self).to_array()
        array['longitude'] = float(self.longitude)  # type float
        array['latitude'] = float(self.latitude)  # type float
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Location from a given dictionary.

        :return: new Location instance.
        :rtype: Location
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['longitude'] = float(array.get('longitude'))
        data['latitude'] = float(array.get('latitude'))
        return Location(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(location_instance)`
        """
        return "Location(longitude={self.longitude!r}, latitude={self.latitude!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in location_instance`
        """
        return key in ["longitude", "latitude"]
    # end def __contains__
# end class Location


class Venue(Media):
    """
    This object represents a venue.

    https://core.telegram.org/bots/api#venue
    """
    def __init__(self, location, title, address, foursquare_id=None):
        """
        This object represents a venue.

        https://core.telegram.org/bots/api#venue


        Parameters:

        :param location: Venue location
        :type  location: pytgbot.api_types.receivable.media.Location

        :param title: Name of the venue
        :type  title: str

        :param address: Address of the venue
        :type  address: str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue
        :type    foursquare_id: str
        """
        super(Venue, self).__init__()
        assert(location is not None)
        assert(isinstance(location, Location))
        self.location = location
        
        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title
        
        assert(address is not None)
        assert(isinstance(address, str))
        self.address = address
        
        assert(foursquare_id is None or isinstance(foursquare_id, str))
        self.foursquare_id = foursquare_id
    # end def __init__

    def to_array(self):
        """
        Serializes this Venue to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Venue, self).to_array()
        array['location'] = self.location.to_array()  # type Location
        array['title'] = str(self.title)  # type str
        array['address'] = str(self.address)  # type str
        if self.foursquare_id is not None:
            array['foursquare_id'] = str(self.foursquare_id)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Venue from a given dictionary.

        :return: new Venue instance.
        :rtype: Venue
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['location'] = Location.from_array(array.get('location'))
        data['title'] = str(array.get('title'))
        data['address'] = str(array.get('address'))
        data['foursquare_id'] = str(array.get('foursquare_id')) if array.get('foursquare_id') is not None else None
        return Venue(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(venue_instance)`
        """
        return "Venue(location={self.location!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in venue_instance`
        """
        return key in ["location", "title", "address", "foursquare_id"]
    # end def __contains__
# end class Venue


class UserProfilePhotos(Result):
    """
    This object represent a user's profile pictures.

    https://core.telegram.org/bots/api#userprofilephotos
    """
    def __init__(self, total_count, photos):
        """
        This object represent a user's profile pictures.

        https://core.telegram.org/bots/api#userprofilephotos


        Parameters:

        :param total_count: Total number of profile pictures the target user has
        :type  total_count: int

        :param photos: Requested profile pictures (in up to 4 sizes each)
        :type  photos: list of list of pytgbot.api_types.receivable.media.PhotoSize
        """
        super(UserProfilePhotos, self).__init__()
        assert(total_count is not None)
        assert(isinstance(total_count, int))
        self.total_count = total_count
        
        assert(photos is not None)
        assert(isinstance(photos, (list, tuple)))  # list of list of PhotoSize
        self.photos = photos
    # end def __init__

    def to_array(self):
        """
        Serializes this UserProfilePhotos to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        from api_types import as_array
        array = super(UserProfilePhotos, self).to_array()
        array['total_count'] = int(self.total_count)  # type int
        array['photos'] = self._as_array(self.photos)  # type list of list of PhotoSize
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new UserProfilePhotos from a given dictionary.

        :return: new UserProfilePhotos instance.
        :rtype: UserProfilePhotos
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['total_count'] = int(array.get('total_count'))
        data['photos'] = PhotoSize.from_array_list(array.get('photos'), list_level=2)
        return UserProfilePhotos(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(userprofilephotos_instance)`
        """
        return "UserProfilePhotos(total_count={self.total_count!r}, photos={self.photos!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in userprofilephotos_instance`
        """
        return key in ["total_count", "photos"]
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
    """
    def __init__(self, file_id, file_size=None, file_path=None):
        """
        This object represents a file ready to be downloaded.
        The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>.
        It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling getFile.
        
        Maximum file size to download is 20 MB

        https://core.telegram.org/bots/api#file


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id: str


        Optional keyword parameters:

        :keyword file_size: Optional. File size, if known
        :type    file_size: int

        :keyword file_path: Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file
        :type    file_path: str
        """
        super(File, self).__init__()
        
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
        
        assert(file_path is None or isinstance(file_path, str))
        self.file_path = file_path
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

    def to_array(self):
        """
        Serializes this File to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(File, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        if self.file_path is not None:
            array['file_path'] = str(self.file_path)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new File from a given dictionary.

        :return: new File instance.
        :rtype: File
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        data['file_path'] = str(array.get('file_path')) if array.get('file_path') is not None else None
        return File(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(file_instance)`
        """
        return "File(file_id={self.file_id!r}, file_size={self.file_size!r}, file_path={self.file_path!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in file_instance`
        """
        return key in ["file_id", "file_size", "file_path"]
    # end def __contains__
# end class File



class Game(Media):
    """
    This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    https://core.telegram.org/bots/api#game
    """
    def __init__(self, title, description, photo, text=None, text_entities=None, animation=None):
        """
        This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.
    
        https://core.telegram.org/bots/api#game


        Parameters:
        
        :param title: Title of the game
        :type  title: str
        
        :param description: Description of the game
        :type  description: str
        
        :param photo: Photo that will be displayed in the game message in chats.
        :type  photo: list of pytgbot.api_types.receivable.media.PhotoSize
        

        Optional keyword parameters:
        
        :keyword text: Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
        :type    text: str
        
        :keyword text_entities: Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
        :type    text_entities: list of pytgbot.api_types.receivable.media.MessageEntity
        
        :keyword animation: Optional. Animation that will be displayed in the game message in chats. Upload via BotFather
        :type    animation: pytgbot.api_types.receivable.media.Animation
        """
        super(Game, self).__init__()
        from pytgbot.api_types.receivable.media import Animation
        from pytgbot.api_types.receivable.media import MessageEntity
        from pytgbot.api_types.receivable.media import PhotoSize
        
        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title
        
        assert(description is not None)
        assert(isinstance(description, str))
        self.description = description
        
        assert(photo is not None)
        assert(isinstance(photo, list))
        self.photo = photo
        
        assert(text is None or isinstance(text, str))
        self.text = text
        
        assert(text_entities is None or isinstance(text_entities, list))
        self.text_entities = text_entities
        
        assert(animation is None or isinstance(animation, Animation))
        self.animation = animation
    # end def __init__

    def to_array(self):
        """
        Serializes this Game to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Game, self).to_array()
        array['title'] = str(self.title)  # type str
        array['description'] = str(self.description)  # type str
        array['photo'] = self._as_array(self.photo)  # type list of PhotoSize
        if self.text is not None:
            array['text'] = str(self.text)  # type str
        if self.text_entities is not None:
            array['text_entities'] = self._as_array(self.text_entities)  # type list of MessageEntity
        if self.animation is not None:
            array['animation'] = self.animation.to_array()  # type Animation
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Game from a given dictionary.

        :return: new Game instance.
        :rtype: Game
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        from pytgbot.api_types.receivable.media import Animation
        from pytgbot.api_types.receivable.media import MessageEntity
        from pytgbot.api_types.receivable.media import PhotoSize
        
        data = {}
        data['title'] = str(array.get('title'))
        data['description'] = str(array.get('description'))
        data['photo'] = PhotoSize.from_array_list(array.get('photo'), list_level=1)
        data['text'] = str(array.get('text')) if array.get('text') is not None else None
        data['text_entities'] = MessageEntity.from_array_list(array.get('text_entities'), list_level=1) if array.get('text_entities') is not None else None
        data['animation'] = Animation.from_array(array.get('animation')) if array.get('animation') is not None else None
        return Game(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(game_instance)`
        """
        return "Game(title={self.title!r}, description={self.description!r}, photo={self.photo!r}, text={self.text!r}, text_entities={self.text_entities!r}, animation={self.animation!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in game_instance`
        """
        return key in ["title", "description", "photo", "text", "text_entities", "animation"]
    # end def __contains__
# end class Game



class Animation(Media):
    """
    You can provide an animation for your game so that it looks stylish in chats (check out Lumberjack for an example). This object represents an animation file to be displayed in the message containing a game.

    https://core.telegram.org/bots/api#animation
    """
    def __init__(self, file_id, thumb=None, file_name=None, mime_type=None, file_size=None):
        """
        You can provide an animation for your game so that it looks stylish in chats (check out Lumberjack for an example). This object represents an animation file to be displayed in the message containing a game.
    
        https://core.telegram.org/bots/api#animation


        Parameters:
        
        :param file_id: Unique file identifier
        :type  file_id: str
        

        Optional keyword parameters:
        
        :keyword thumb: Optional. Animation thumbnail as defined by sender
        :type    thumb: pytgbot.api_types.receivable.media.PhotoSize
        
        :keyword file_name: Optional. Original animation filename as defined by sender
        :type    file_name: str
        
        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type: str
        
        :keyword file_size: Optional. File size
        :type    file_size: int
        """
        super(Animation, self).__init__()
        from pytgbot.api_types.receivable.media import PhotoSize
        
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        self.file_id = file_id
        
        assert(thumb is None or isinstance(thumb, PhotoSize))
        self.thumb = thumb
        
        assert(file_name is None or isinstance(file_name, str))
        self.file_name = file_name
        
        assert(mime_type is None or isinstance(mime_type, str))
        self.mime_type = mime_type
        
        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        """
        Serializes this Animation to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Animation, self).to_array()
        array['file_id'] = str(self.file_id)  # type str
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        if self.file_name is not None:
            array['file_name'] = str(self.file_name)  # type str
        if self.mime_type is not None:
            array['mime_type'] = str(self.mime_type)  # type str
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Animation from a given dictionary.

        :return: new Animation instance.
        :rtype: Animation
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        from pytgbot.api_types.receivable.media import PhotoSize
        
        data = {}
        data['file_id'] = str(array.get('file_id'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['file_name'] = str(array.get('file_name')) if array.get('file_name') is not None else None
        data['mime_type'] = str(array.get('mime_type')) if array.get('mime_type') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        return Animation(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(animation_instance)`
        """
        return "Animation(file_id={self.file_id!r}, thumb={self.thumb!r}, file_name={self.file_name!r}, mime_type={self.mime_type!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in animation_instance`
        """
        return key in ["file_id", "thumb", "file_name", "mime_type", "file_size"]
    # end def __contains__
# end class Animation

