# -*- coding: utf-8 -*-
from . import Sendable
from .files import InputFile
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise


class InputMedia(Sendable):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode

    Optional keyword parameters:

    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
    :type  parse_mode: str|unicode
    """

    def __init__(self, type, media, caption=None, parse_mode=None):
        """
        This object represents the content of a media message to be sent.

        https://core.telegram.org/bots/api#inputmedia


        Parameters:

        :param type: Type of the result
        :type  type: str|unicode

        :param caption: Caption of the document to be sent, 0-200 characters
        :type  caption: str|unicode

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: InputFile|str|unicode

        """
        super(InputMedia, self).__init__()

        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type

        assert_type_or_raise(media, unicode_type, InputFile, parameter_name="media")
        self.media = media

        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption

        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
    # end def __init__

    def to_array(self):
        array = {
            "type": u(self.type),
            #"media": u(self.media),
        }
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        return array
    # end def to_array

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
    thumb field.
    """
    def __init__(self, type, media, thumb, caption=None, parse_mode=None):
        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        super(InputMediaWithThumb, self).__init__(type, media, caption, parse_mode)
    # end if

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


class InputMediaPhoto(InputMedia):
    """
    Represents a photo to be sent.

    https://core.telegram.org/bots/api#inputmediaphoto


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters
    :type  caption: str|unicode

    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
    :type  parse_mode: str|unicode
    """

    def __init__(self, media, caption=None, parse_mode=None):
        """
        Represents a photo to be sent.

        https://core.telegram.org/bots/api#inputmediaphoto


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param caption: Optional. Caption of the photo to be sent, 0-1024 characters
        :type  caption: str|unicode

        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
        :type  parse_mode: str|unicode
        """
        super(InputMediaPhoto, self).__init__("photo", media, caption=caption, parse_mode=parse_mode)

        # type is set by InputMedia base class
        # caption is set by InputMedia base class
        # media is set by InputMedia base class
        # parse_mode is set by InputMedia base class

    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaPhoto to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InputMediaPhoto, self).to_array()
        # 'type' given by superclass
        # 'media' given by superclass
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaPhoto from a given dictionary.

        :return: new InputMediaPhoto instance.
        :rtype: InputMediaPhoto
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        # 'type' is given by class type
        data['media'] = u(array.get('media'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('caption')) if array.get('caption') is not None else None

        instance = InputMediaPhoto(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaphoto_instance)`
        """
        return "InputMediaPhoto(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaphoto_instance)`
        """
        if self._raw:
            return "InputMediaPhoto.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaPhoto(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaphoto_instance`
        """
        return key in ["type", "media", "caption", "parse_mode"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class InputMediaPhoto


class InputMediaVideo(InputMediaWithThumb):
    """
    Represents a video to be sent.

    https://core.telegram.org/bots/api#inputmediavideo


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

    :param caption: Optional. Caption of the video to be sent, 0-200 characters
    :type  caption: str|unicode

    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
    :type  parse_mode: str|unicode

    :param width: Optional. Video width
    :type  width: int

    :param height: Optional. Video height
    :type  height: int

    :param duration: Optional. Video duration
    :type  duration: int

    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    :type  supports_streaming: bool
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, width=None, height=None, duration=None, supports_streaming=None):
        """
        Represents a video to be sent.

        https://core.telegram.org/bots/api#inputmediavideo


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

        :param caption: Optional. Caption of the video to be sent, 0-200 characters
        :type  caption: str|unicode

        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
        :type  parse_mode: str|unicode

        :param width: Optional. Video width
        :type  width: int

        :param height: Optional. Video height
        :type  height: int

        :param duration: Optional. Video duration
        :type  duration: int

        :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
        :type  supports_streaming: bool
        """
        super(InputMediaVideo, self).__init__("video", media, thumb, caption=caption, parse_mode=parse_mode)

        # type is set by InputMedia base class
        # media is set by InputMedia base class
        # thumb is set by InputMediaWithThumb base class
        # caption is set by InputMedia base class
        # parse_mode is set by InputMedia base class

        assert_type_or_raise(width, None, int, parameter_name="width")
        self.width = width

        assert_type_or_raise(height, None, int, parameter_name="height")
        self.height = height

        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration

        assert_type_or_raise(supports_streaming, None, bool, parameter_name="supports_streaming")
        self.supports_streaming = supports_streaming
    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaVideo to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        from .files import InputFile
        array = super(InputMediaVideo, self).to_array()
        # 'type' given by superclass
        # 'media' given by superclass
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = None  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type str
            else:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        if self.width is not None:
            array['width'] = int(self.width)  # type int
        if self.height is not None:
            array['height'] = int(self.height)  # type int
        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.supports_streaming is not None:
            array['supports_streaming'] = bool(self.supports_streaming)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaVideo from a given dictionary.

        :return: new InputMediaVideo instance.
        :rtype: InputMediaVideo
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile

        data = {}
        # 'type' is given by class type
        data['media'] = u(array.get('media'))
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = None  # will be filled later by get_request_data()
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['width'] = int(array.get('width')) if array.get('width') is not None else None
        data['height'] = int(array.get('height')) if array.get('height') is not None else None
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['supports_streaming'] = bool(array.get('supports_streaming')) if array.get('supports_streaming') is not None else None

        instance = InputMediaVideo(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediavideo_instance)`
        """
        return "InputMediaVideo(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, supports_streaming={self.supports_streaming!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediavideo_instance)`
        """
        if self._raw:
            return "InputMediaVideo.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaVideo(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r}, supports_streaming={self.supports_streaming!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediavideo_instance`
        """
        return key in ["type", "media", "thumb", "caption", "parse_mode", "width", "height", "duration", "supports_streaming"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class InputMediaVideo


class InputMediaAnimation(InputMediaWithThumb):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    https://core.telegram.org/bots/api#inputmediaanimation


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

    :param caption: Optional. Caption of the animation to be sent, 0-1024 characters
    :type  caption: str|unicode

    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
    :type  parse_mode: str|unicode

    :param width: Optional. Animation width
    :type  width: int

    :param height: Optional. Animation height
    :type  height: int

    :param duration: Optional. Animation duration
    :type  duration: int
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, width=None, height=None, duration=None):
        """
        Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

        https://core.telegram.org/bots/api#inputmediaanimation


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

        :param caption: Optional. Caption of the animation to be sent, 0-200 characters
        :type  caption: str|unicode

        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
        :type  parse_mode: str|unicode

        :param width: Optional. Animation width
        :type  width: int

        :param height: Optional. Animation height
        :type  height: int

        :param duration: Optional. Animation duration
        :type  duration: int
        """
        super(InputMediaAnimation, self).__init__('animation', media, thumb, caption=caption, parse_mode=parse_mode)

        # type is set by InputMedia base class
        # media is set by InputMedia base class
        # thumb is set by InputMediaWithThumb base class
        # caption is set by InputMedia base class
        # parse_mode is set by InputMedia base class

        assert_type_or_raise(width, None, int, parameter_name="width")
        self.width = width

        assert_type_or_raise(height, None, int, parameter_name="height")
        self.height = height

        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaAnimation to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InputMediaAnimation, self).to_array()
        # 'type' given by superclass
        # 'media' given by superclass
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = None  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type str
            else:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        if self.width is not None:
            array['width'] = int(self.width)  # type int
        if self.height is not None:
            array['height'] = int(self.height)  # type int
        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaAnimation from a given dictionary.

        :return: new InputMediaAnimation instance.
        :rtype: InputMediaAnimation
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile


        data = {}
        # 'type' is given by class type
        data['media'] = u(array.get('media'))
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = None  # will be filled later by get_request_data()
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['width'] = int(array.get('width')) if array.get('width') is not None else None
        data['height'] = int(array.get('height')) if array.get('height') is not None else None
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None

        instance = InputMediaAnimation(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaanimation_instance)`
        """
        return "InputMediaAnimation(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaanimation_instance)`
        """
        if self._raw:
            return "InputMediaAnimation.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaAnimation(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaanimation_instance`
        """
        return key in ["type", "media", "thumb", "caption", "parse_mode", "width", "height", "duration"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class InputMediaAnimation


class InputMediaAudio(InputMediaWithThumb):
    """
    Represents an audio file to be treated as music to be sent.

    https://core.telegram.org/bots/api#inputmediaaudio


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

    :param caption: Optional. Caption of the audio to be sent, 0-1024 characters
    :type  caption: str|unicode

    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
    :type  parse_mode: str|unicode

    :param duration: Optional. Duration of the audio in seconds
    :type  duration: int

    :param performer: Optional. Performer of the audio
    :type  performer: str|unicode

    :param title: Optional. Title of the audio
    :type  title: str|unicode
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None, duration=None, performer=None, title=None):
        """
        Represents an audio file to be treated as music to be sent.

        https://core.telegram.org/bots/api#inputmediaaudio


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

        :param caption: Optional. Caption of the audio to be sent, 0-1024 characters
        :type  caption: str|unicode

        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
        :type  parse_mode: str|unicode

        :param duration: Optional. Duration of the audio in seconds
        :type  duration: int

        :param performer: Optional. Performer of the audio
        :type  performer: str|unicode

        :param title: Optional. Title of the audio
        :type  title: str|unicode
        """
        super(InputMediaAudio, self).__init__('audio', media, thumb, caption=caption, parse_mode=parse_mode)
        from pytgbot.api_types.sendable.files import InputFile

        # type is set by InputMedia base class
        # media is set by InputMedia base class
        # thumb is set by InputMediaWithThumb base class
        # caption is set by InputMedia base class
        # parse_mode is set by InputMedia base class

        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration

        assert_type_or_raise(performer, None, unicode_type, parameter_name="performer")
        self.performer = performer

        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaAudio to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InputMediaAudio, self).to_array()
        # 'type' given by superclass
        # 'media' given by superclass
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = None  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type str
            else:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.performer is not None:
            array['performer'] = u(self.performer)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaAudio from a given dictionary.

        :return: new InputMediaAudio instance.
        :rtype: InputMediaAudio
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile


        data = {}
        # 'type' is given by class type
        data['media'] = u(array.get('media'))
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = None  # will be filled later by get_request_data()
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['performer'] = u(array.get('performer')) if array.get('performer') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None

        instance = InputMediaAudio(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaaudio_instance)`
        """
        return "InputMediaAudio(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaaudio_instance)`
        """
        if self._raw:
            return "InputMediaAudio.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaAudio(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaaudio_instance`
        """
        return key in ["type", "media", "thumb", "caption", "parse_mode", "duration", "performer", "title"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class InputMediaAudio


class InputMediaDocument(InputMediaWithThumb):
    """
    Represents a general file to be sent.

    https://core.telegram.org/bots/api#inputmediadocument


    Parameters:

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

    :param caption: Optional. Caption of the document to be sent, 0-200 characters
    :type  caption: str|unicode

    :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
    :type  parse_mode: str|unicode
    """

    def __init__(self, media, thumb=None, caption=None, parse_mode=None):
        """
        Represents a general file to be sent.

        https://core.telegram.org/bots/api#inputmediadocument


        Parameters:

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file_attach_name>” to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode|pytgbot.api_types.sendable.files.InputFile


        Optional keyword parameters:

        :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 90. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass “attach://<file_attach_name>” if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: str|unicode|pytgbot.api_types.sendable.files.InputFile

        :param caption: Optional. Caption of the document to be sent, 0-200 characters
        :type  caption: str|unicode

        :param parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in the media caption.
        :type  parse_mode: str|unicode
        """
        super(InputMediaDocument, self).__init__('document', media, thumb, caption=caption, parse_mode=parse_mode)
        # type is set by InputMedia base class
        # media is set by InputMedia base class
        # thumb is set by InputMediaWithThumb base class
        # caption is set by InputMedia base class
        # parse_mode is set by InputMedia base class
    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaDocument to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InputMediaDocument, self).to_array()
        # 'type' given by superclass
        # 'media' given by superclass
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = None  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type str
            else:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if
        # 'caption' given by superclass
        # 'parse_mode' given by superclass
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputMediaDocument from a given dictionary.

        :return: new InputMediaDocument instance.
        :rtype: InputMediaDocument
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile


        data = {}
        # 'type' is given by class type
        data['media'] = u(array.get('media'))
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = None  # will be filled later by get_request_data()
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None

        instance = InputMediaDocument(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediadocument_instance)`
        """
        return "InputMediaDocument(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediadocument_instance)`
        """
        if self._raw:
            return "InputMediaDocument.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaDocument(type={self.type!r}, media={self.media!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediadocument_instance`
        """
        return key in ["type", "media", "thumb", "caption", "parse_mode"] and hasattr(self, key) and bool(getattr(self, key, None))
    # end def __contains__
# end class InputMediaDocument

