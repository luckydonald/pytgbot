# -*- coding: utf-8 -*-
from .files import InputFile
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

__author__ = 'luckydonald'


class InputMedia(Sendable):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """

    def __init__(self, type, media, caption=None, parse_mode=None, caption_entities=None):
        """
        This object represents the content of a media message to be sent.

        https://core.telegram.org/bots/api#inputmedia


        Parameters:

        :param type: Type of the result, a fixed value per subclass
        :type  type: str|unicode

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode


        Optional keyword parameters:

        :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
        """
        super(InputMedia, self).__init__()

        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type
        assert_type_or_raise(media, unicode_type, parameter_name="media")
        self.media = media
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMedia to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMedia, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['media'] = u(self.media)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMedia constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Sendable.validate_array(array)
        data['type'] = u(array.get('type'))
        data['media'] = u(array.get('media'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMedia from a given dictionary.

        :return: new InputMedia instance.
        :rtype: InputMedia
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMedia.validate_array(array)
        instance = InputMedia(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmedia_instance)`
        """
        return "InputMedia(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmedia_instance)`
        """
        if self._raw:
            return "InputMedia.from_array({self._raw})".format(self=self)
        # end if
        return "InputMedia(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmedia_instance`
        """
        return (
            key in ["type", "media", "caption", "parse_mode", "caption_entities"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__

    def get_request_data(self, var_name, full_data=False):
        """
        :param var_name:
        :param full_data: If you want `.to_array()` with this data, ready to be sent.
        :return: A tuple of `to_array()` dict and the files (:py:func:`InputFile.get_request_files()`).
                 Files can be None, if no file was given, but an url or existing `file_id`.
                 If `media` is :py:class:`InputFile` however, the first tuple element,
                 media, will have ['media'] set to `attach://{var_name}_media` automatically.
        """
        if full_data:
            data = self.to_array()
            data['media'], file = self.get_inputfile_data(self.media, var_name, suffix='_media')
            return data, file
        # end if
        return self.get_inputfile_data(self.media, var_name, suffix='_media')
    # end def get_request_data

    @staticmethod
    def get_inputfile_data(media, var_name, suffix='_media'):
        name = "{var_name}{suffix}".format(var_name=var_name, suffix=suffix)
        if isinstance(media, InputFile):
            # is file to be uploaded
            string = 'attach://{name}'.format(name=name)
            return string, media.get_request_files(name)
        else:
            # is no upload
            return media, None
        # end if
    # end def get_inputfile_data
# end class InputMedia


class InputMediaWithThumb(InputMedia):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode

    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file.
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """

    def get_request_data(self, var_name, full_data=False):
        """
        :param var_name:
        :param full_data: If you want `.to_array()` with this data, ready to be sent.
        :return: A tuple of `to_array()` dict and the files (:py:func:`InputFile.get_request_files()`).
                 Files can be None, if no file was given, but an url or existing `file_id`.

                 If `self.media` is an `InputFile` however,
                 the first tuple element (either the string, or the dict's `['media']` if `full_data=True`),
                 will be set to `attach://{var_name}_media` automatically.
                 If `self.thumb` is an `InputFile` however, the first tuple element's `['thumb']`, will be set to `attach://{var_name}_thumb` automatically.
        """
        if not full_data:
            raise ArithmeticError('we have a thumbnail, please use `full_data=True`.')
        # end if
        file = {}
        data, file_to_add = super(InputMediaWithThumb, self).get_request_data(var_name, full_data=True)
        if file_to_add:
            file.update(file_to_add)
        # end if
        data['thumb'], file_to_add = self.get_inputfile_data(self.thumb, var_name, suffix='_thumb')
        if data['thumb'] is None:
            del data['thumb']  # having `'thumb': null` in the json produces errors.
        # end if
        if file_to_add:
            file.update(file_to_add)
        # end if
        return data, (file or None)
        # end if
    # end def

    def __init__(self, type, media, thumb, caption=None, parse_mode=None, caption_entities=None):
        """
        This object represents the content of a media message to be sent.

        https://core.telegram.org/bots/api#inputmedia


        Parameters:

        :param type: Type of the result, a fixed value per subclass
        :type  type: str|unicode

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode

        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file.
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode


        Optional keyword parameters:

        :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
        """
        super(InputMediaWithThumb, self).__init__(type, media, caption, parse_mode, caption_entities)

        # 'type' is set by InputMedia base class
        # 'media' is set by InputMedia base class
        assert_type_or_raise(thumb, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        # 'caption' is set by InputMedia base class
        # 'parse_mode' is set by InputMedia base class
        # 'caption_entities' is set by InputMedia base class
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaWithThumb to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaWithThumb, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        if isinstance(self.thumb, InputFile):
            array['thumb'] = self.thumb.to_array()  # type InputFile
        elif isinstance(self.thumb, str):
            array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaWithThumb constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = InputMedia.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        if isinstance(array.get('thumb'), InputFile):
            data['thumb'] = None  # will be filled later by get_request_data()
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaWithThumb from a given dictionary.

        :return: new InputMediaWithThumb instance.
        :rtype: InputMediaWithThumb
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaWithThumb.validate_array(array)
        instance = InputMediaWithThumb(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediawiththumb_instance)`
        """
        return "InputMediaWithThumb(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediawiththumb_instance)`
        """
        if self._raw:
            return "InputMediaWithThumb.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaWithThumb(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediawiththumb_instance`
        """
        return (
            key in ["type", "media", "thumb", "caption", "parse_mode", "caption_entities"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputMediaWithThumb


class InputMediaPlayable(InputMediaWithThumb):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode

    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file.
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param duration: Optional. Duration of the media
    :type  duration: int


    Optional keyword parameters:

    :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """



    def __init__(self, type, media, thumb, duration=None, caption=None, parse_mode=None, caption_entities=None):
        """
        This object represents the content of a media message to be sent.

        https://core.telegram.org/bots/api#inputmedia


        Parameters:

        :param type: Type of the result, a fixed value per subclass
        :type  type: str|unicode

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode

        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file.
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

        :param duration: Optional. Duration of the media
        :type  duration: int


        Optional keyword parameters:

        :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
        """
        super(InputMediaPlayable, self).__init__(type, media, thumb, caption, parse_mode, caption_entities)

        # 'type' is set by InputMediaWithThumb base class
        # 'media' is set by InputMediaWithThumb base class
        # 'thumb' is set by InputMediaWithThumb base class
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
        # 'caption' is set by InputMediaWithThumb base class
        # 'parse_mode' is set by InputMediaWithThumb base class
        # 'caption_entities' is set by InputMediaWithThumb base class
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaPlayable to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaPlayable, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'thumb' given by superclass
        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaPlayable constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = InputMediaWithThumb.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'thumb' is given by class type
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaPlayable from a given dictionary.

        :return: new InputMediaPlayable instance.
        :rtype: InputMediaPlayable
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaPlayable.validate_array(array)
        instance = InputMediaPlayable(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaplayable_instance)`
        """
        return "InputMediaPlayable(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, duration={self.duration!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaplayable_instance)`
        """
        if self._raw:
            return "InputMediaPlayable.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaPlayable(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, duration={self.duration!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaplayable_instance`
        """
        return (
            key in ["type", "media", "thumb", "duration", "caption", "parse_mode", "caption_entities"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__


# end class InputMediaPlayable


class InputMediaVideolike(InputMediaPlayable):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode

    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file.
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param duration: Optional. Duration of the media
    :type  duration: int

    :param width: Optional. Media width
    :type  width: int

    :param height: Optional. Media height
    :type  height: int


    Optional keyword parameters:

    :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """



    def __init__(self, type, media, thumb, duration=None, width=None, height=None, caption=None, parse_mode=None, caption_entities=None):
        """
        This object represents the content of a media message to be sent.

        https://core.telegram.org/bots/api#inputmedia


        Parameters:

        :param type: Type of the result, a fixed value per subclass
        :type  type: str|unicode

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode

        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file.
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

        :param duration: Optional. Duration of the media
        :type  duration: int

        :param width: Optional. Media width
        :type  width: int

        :param height: Optional. Media height
        :type  height: int


        Optional keyword parameters:

        :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
        """
        super(InputMediaVideolike, self).__init__(type, media, thumb, duration, caption, parse_mode, caption_entities)

        # 'type' is set by InputMediaPlayable base class
        # 'media' is set by InputMediaPlayable base class
        # 'thumb' is set by InputMediaPlayable base class
        # 'duration' is set by InputMediaPlayable base class
        assert_type_or_raise(width, None, int, parameter_name="width")
        self.width = width
        assert_type_or_raise(height, None, int, parameter_name="height")
        self.height = height
        # 'caption' is set by InputMediaPlayable base class
        # 'parse_mode' is set by InputMediaPlayable base class
        # 'caption_entities' is set by InputMediaPlayable base class
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaVideolike to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaVideolike, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'thumb' given by superclass
        # 'duration' given by superclass
        if self.width is not None:
            array['width'] = int(self.width)  # type int
        # end if
        if self.height is not None:
            array['height'] = int(self.height)  # type int
        # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaVideolike constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = InputMediaPlayable.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'thumb' is given by class type
        # 'duration' is given by class type
        data['width'] = int(array.get('width')) if array.get('width') is not None else None
        data['height'] = int(array.get('height')) if array.get('height') is not None else None
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaVideolike from a given dictionary.

        :return: new InputMediaVideolike instance.
        :rtype: InputMediaVideolike
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaVideolike.validate_array(array)
        instance = InputMediaVideolike(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediavideolike_instance)`
        """
        return "InputMediaVideolike(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, duration={self.duration!r}, width={self.width!r}, height={self.height!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediavideolike_instance)`
        """
        if self._raw:
            return "InputMediaVideolike.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaVideolike(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, duration={self.duration!r}, width={self.width!r}, height={self.height!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediavideolike_instance`
        """
        return (
            key in ["type", "media", "thumb", "duration", "width", "height", "caption", "parse_mode", "caption_entities"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__


# end class InputMediaVideolike


class InputMediaPhoto(InputMedia):
    """
    Represents a photo to be sent.

    https://core.telegram.org/bots/api#inputmediaphoto


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """

    def __init__(self, media, caption=None, parse_mode=None, caption_entities=None):
        """
        Represents a photo to be sent.

        https://core.telegram.org/bots/api#inputmediaphoto


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode


        Optional keyword parameters:

        :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
        """
        super(InputMediaPhoto, self).__init__('photo', media, caption, parse_mode, caption_entities)
        from ..receivable.media import MessageEntity

        # 'type' is set by InputMedia base class
        # 'media' is set by InputMedia base class
        # 'caption' is set by InputMedia base class
        # 'parse_mode' is set by InputMedia base class
        # 'caption_entities' is set by InputMedia base class
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaPhoto to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaPhoto, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaPhoto constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity

        data = InputMedia.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaPhoto from a given dictionary.

        :return: new InputMediaPhoto instance.
        :rtype: InputMediaPhoto
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaPhoto.validate_array(array)
        instance = InputMediaPhoto(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaphoto_instance)`
        """
        return "InputMediaPhoto(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaphoto_instance)`
        """
        if self._raw:
            return "InputMediaPhoto.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaPhoto(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaphoto_instance`
        """
        return (
            key in ["type", "media", "caption", "parse_mode", "caption_entities"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputMediaPhoto


class InputMediaVideo(InputMediaVideolike):
    """
    Represents a video to be sent.

    https://core.telegram.org/bots/api#inputmediavideo


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param width: Optional. Video width
    :type  width: int

    :param height: Optional. Video height
    :type  height: int

    :param duration: Optional. Video duration
    :type  duration: int

    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    :type  supports_streaming: bool
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, caption_entities=None, width=None, height=None, duration=None, supports_streaming=None):
        """
        Represents a video to be sent.

        https://core.telegram.org/bots/api#inputmediavideo


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

        :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :param width: Optional. Video width
        :type  width: int

        :param height: Optional. Video height
        :type  height: int

        :param duration: Optional. Video duration
        :type  duration: int

        :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
        :type  supports_streaming: bool
        """
        super(InputMediaVideo, self).__init__('video', media, thumb, caption, parse_mode, caption_entities, width, height, duration)
        from ..receivable.media import MessageEntity
        from .files import InputFile

        # 'type' is set by InputMediaVideolike base class
        # 'media' is set by InputMediaVideolike base class
        # 'thumb' is set by InputMediaVideolike base class
        # 'caption' is set by InputMediaVideolike base class
        # 'parse_mode' is set by InputMediaVideolike base class
        # 'caption_entities' is set by InputMediaVideolike base class
        # 'width' is set by InputMediaVideolike base class
        # 'height' is set by InputMediaVideolike base class
        # 'duration' is set by InputMediaVideolike base class
        assert_type_or_raise(supports_streaming, None, bool, parameter_name="supports_streaming")
        self.supports_streaming = supports_streaming
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaVideo to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaVideo, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'thumb' given by superclass
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass
        # 'width' given by superclass
        # 'height' given by superclass
        # 'duration' given by superclass
        if self.supports_streaming is not None:
            array['supports_streaming'] = bool(self.supports_streaming)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaVideo constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .files import InputFile

        data = InputMediaVideolike.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'thumb' is given by class type
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        # 'width' is given by class type
        # 'height' is given by class type
        # 'duration' is given by class type
        data['supports_streaming'] = bool(array.get('supports_streaming')) if array.get('supports_streaming') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaVideo from a given dictionary.

        :return: new InputMediaVideo instance.
        :rtype: InputMediaVideo
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaVideo.validate_array(array)
        instance = InputMediaVideo(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediavideo_instance)`
        """
        return "InputMediaVideo(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, supports_streaming={self.supports_streaming!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediavideo_instance)`
        """
        if self._raw:
            return "InputMediaVideo.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaVideo(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, supports_streaming={self.supports_streaming!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediavideo_instance`
        """
        return (
            key in ["type", "media", "thumb", "caption", "parse_mode", "caption_entities", "width", "height", "duration", "supports_streaming"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputMediaVideo


class InputMediaAnimation(InputMediaVideolike):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    https://core.telegram.org/bots/api#inputmediaanimation


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param caption: Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param width: Optional. Animation width
    :type  width: int

    :param height: Optional. Animation height
    :type  height: int

    :param duration: Optional. Animation duration
    :type  duration: int
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, caption_entities=None, width=None, height=None, duration=None):
        """
        Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

        https://core.telegram.org/bots/api#inputmediaanimation


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

        :param caption: Optional. Caption of the animation to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the animation caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :param width: Optional. Animation width
        :type  width: int

        :param height: Optional. Animation height
        :type  height: int

        :param duration: Optional. Animation duration
        :type  duration: int
        """
        super(InputMediaAnimation, self).__init__('animation', media, thumb, caption, parse_mode, caption_entities, width, height, duration)
        from ..receivable.media import MessageEntity
        from .files import InputFile

        # 'type' is set by InputMediaVideolike base class
        # 'media' is set by InputMediaVideolike base class
        # 'thumb' is set by InputMediaVideolike base class
        # 'caption' is set by InputMediaVideolike base class
        # 'parse_mode' is set by InputMediaVideolike base class
        # 'caption_entities' is set by InputMediaVideolike base class
        # 'width' is set by InputMediaVideolike base class
        # 'height' is set by InputMediaVideolike base class
        # 'duration' is set by InputMediaVideolike base class
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaAnimation to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaAnimation, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'thumb' given by superclass
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass
        # 'width' given by superclass
        # 'height' given by superclass
        # 'duration' given by superclass

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaAnimation constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .files import InputFile

        data = InputMediaVideolike.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'thumb' is given by class type
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        # 'width' is given by class type
        # 'height' is given by class type
        # 'duration' is given by class type
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaAnimation from a given dictionary.

        :return: new InputMediaAnimation instance.
        :rtype: InputMediaAnimation
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaAnimation.validate_array(array)
        instance = InputMediaAnimation(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaanimation_instance)`
        """
        return "InputMediaAnimation(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaanimation_instance)`
        """
        if self._raw:
            return "InputMediaAnimation.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaAnimation(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaanimation_instance`
        """
        return (
            key in ["type", "media", "thumb", "caption", "parse_mode", "caption_entities", "width", "height", "duration"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputMediaAnimation


class InputMediaAudio(InputMediaPlayable):
    """
    Represents an audio file to be treated as music to be sent.

    https://core.telegram.org/bots/api#inputmediaaudio


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param caption: Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param duration: Optional. Duration of the audio in seconds
    :type  duration: int

    :param performer: Optional. Performer of the audio
    :type  performer: str|unicode

    :param title: Optional. Title of the audio
    :type  title: str|unicode
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None):
        """
        Represents an audio file to be treated as music to be sent.

        https://core.telegram.org/bots/api#inputmediaaudio


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
       :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

        :param caption: Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :param duration: Optional. Duration of the audio in seconds
        :type  duration: int

        :param performer: Optional. Performer of the audio
        :type  performer: str|unicode

        :param title: Optional. Title of the audio
        :type  title: str|unicode
        """
        super(InputMediaAudio, self).__init__('audio', media, thumb, caption, parse_mode, caption_entities, duration)
        from ..receivable.media import MessageEntity
        from .files import InputFile

        # 'type' is set by InputMediaPlayable base class
        # 'media' is set by InputMediaPlayable base class
        # 'thumb' is set by InputMediaPlayable base class
        # 'caption' is set by InputMediaPlayable base class
        # 'parse_mode' is set by InputMediaPlayable base class
        # 'caption_entities' is set by InputMediaPlayable base class
        # 'duration' is set by InputMediaPlayable base class
        assert_type_or_raise(performer, None, unicode_type, parameter_name="performer")
        self.performer = performer
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaAudio to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaAudio, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'thumb' given by superclass
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass
        # 'duration' given by superclass
        if self.performer is not None:
            array['performer'] = u(self.performer)  # py2: type unicode, py3: type str
        # end if
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaAudio constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .files import InputFile

        data = InputMediaPlayable.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'thumb' is given by class type
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        # 'duration' is given by class type
        data['performer'] = u(array.get('performer')) if array.get('performer') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaAudio from a given dictionary.

        :return: new InputMediaAudio instance.
        :rtype: InputMediaAudio
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaAudio.validate_array(array)
        instance = InputMediaAudio(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaaudio_instance)`
        """
        return "InputMediaAudio(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaaudio_instance)`
        """
        if self._raw:
            return "InputMediaAudio.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaAudio(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaaudio_instance`
        """
        return (
            key in ["type", "media", "thumb", "caption", "parse_mode", "caption_entities", "duration", "performer", "title"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputMediaAudio


class InputMediaDocument(InputMediaWithThumb):
    """
    Represents a general file to be sent.

    https://core.telegram.org/bots/api#inputmediadocument


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param disable_content_type_detection: Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always true, if the document is sent as part of an album.
    :type  disable_content_type_detection: bool
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None):
        """
        Represents a general file to be sent.

        https://core.telegram.org/bots/api#inputmediadocument


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

        :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
        :type  caption: str|unicode

        :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more details.
        :type  parse_mode: str|unicode

        :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :param disable_content_type_detection: Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always true, if the document is sent as part of an album.
        :type  disable_content_type_detection: bool
        """
        super(InputMediaDocument, self).__init__('document', media, thumb, caption, parse_mode, caption_entities)
        from ..receivable.media import MessageEntity
        from .files import InputFile

        # 'type' is set by InputMediaWithThumb base class
        # 'media' is set by InputMediaWithThumb base class
        # 'thumb' is set by InputMediaWithThumb base class
        # 'caption' is set by InputMediaWithThumb base class
        # 'parse_mode' is set by InputMediaWithThumb base class
        # 'caption_entities' is set by InputMediaWithThumb base class
        assert_type_or_raise(disable_content_type_detection, None, bool, parameter_name="disable_content_type_detection")
        self.disable_content_type_detection = disable_content_type_detection
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputMediaDocument to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputMediaDocument, self).to_array()

        # 'type' given by superclass
        # 'media' given by superclass
        # 'thumb' given by superclass
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        # 'caption_entities' given by superclass
        if self.disable_content_type_detection is not None:
            array['disable_content_type_detection'] = bool(self.disable_content_type_detection)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputMediaDocument constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .files import InputFile

        data = InputMediaWithThumb.validate_array(array)
        # 'type' is given by class type
        # 'media' is given by class type
        # 'thumb' is given by class type
        # 'caption' is given by class type
        # 'parse_mode' is given by class type
        # 'caption_entities' is given by class type
        data['disable_content_type_detection'] = bool(array.get('disable_content_type_detection')) if array.get('disable_content_type_detection') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaDocument from a given dictionary.

        :return: new InputMediaDocument instance.
        :rtype: InputMediaDocument
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputMediaDocument.validate_array(array)
        instance = InputMediaDocument(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediadocument_instance)`
        """
        return "InputMediaDocument(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, disable_content_type_detection={self.disable_content_type_detection!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediadocument_instance)`
        """
        if self._raw:
            return "InputMediaDocument.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaDocument(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, disable_content_type_detection={self.disable_content_type_detection!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediadocument_instance`
        """
        return (
            key in ["type", "media", "thumb", "caption", "parse_mode", "caption_entities", "disable_content_type_detection"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputMediaDocument

