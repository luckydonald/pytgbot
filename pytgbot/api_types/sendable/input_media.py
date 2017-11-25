# -*- coding: utf-8 -*-
from . import Sendable
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
    """

    def __init__(self, type, media):
        """
        This object represents the content of a media message to be sent.

        https://core.telegram.org/bots/api#inputmedia


        Parameters:

        :param type: Type of the result
        :type  type: str|unicode

        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode
        """
        super(InputMedia, self).__init__()

        assert_type_or_raise(type, unicode_type, parameter_name="type")
        self.type = type

        assert_type_or_raise(media, unicode_type, parameter_name="media")
        self.media = media
    # end def __init__

    def to_array(self):
        return {
            "type": u(self.type),
            "media": u(self.media),
        }
    # end def to_array
# end class InputMedia


class InputMediaPhoto(InputMedia):
    """
    Represents a photo to be sent.

    https://core.telegram.org/bots/api#inputmediaphoto


    Optional keyword parameters:
    
    :param caption: Optional. Caption of the photo to be sent, 0-200 characters
    :type  caption: str|unicode
    """

    def __init__(self, media, caption=None):
        """
        Represents a photo to be sent.
    
        https://core.telegram.org/bots/api#inputmediaphoto


        Optional keyword parameters:
        
        :param caption: Optional. Caption of the photo to be sent, 0-200 characters
        :type  caption: str|unicode
        """
        super(InputMediaPhoto, self).__init__("photo", media)

        # type is set by InputMedia base class
        # media is set by InputMedia base class

        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaPhoto to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InputMediaPhoto, self).to_array()
        # 'type' and 'media' given by superclass
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
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
        
        instance = InputMediaPhoto(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediaphoto_instance)`
        """
        return "InputMediaPhoto(type={self.type!r}, media={self.media!r}, caption={self.caption!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediaphoto_instance)`
        """
        if self._raw:
            return "InputMediaPhoto.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaPhoto(type={self.type!r}, media={self.media!r}, caption={self.caption!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediaphoto_instance`
        """
        return key in ["type", "media", "caption"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class InputMediaPhoto



class InputMediaVideo(InputMedia):
    """
    Represents a video to be sent.

    https://core.telegram.org/bots/api#inputmediavideo
    

    Parameters:
    
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: str|unicode
    

    Optional keyword parameters:
    
    :param caption: Optional. Caption of the video to be sent, 0-200 characters
    :type  caption: str|unicode
    
    :param width: Optional. Video width
    :type  width: int
    
    :param height: Optional. Video height
    :type  height: int
    
    :param duration: Optional. Video duration
    :type  duration: int
    """

    def __init__(self, media, caption=None, width=None, height=None, duration=None):
        """
        Represents a video to be sent.
    
        https://core.telegram.org/bots/api#inputmediavideo
        
    
        Parameters:
        
        :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
        :type  media: str|unicode
        
    
        Optional keyword parameters:
        
        :param caption: Optional. Caption of the video to be sent, 0-200 characters
        :type  caption: str|unicode
        
        :param width: Optional. Video width
        :type  width: int
        
        :param height: Optional. Video height
        :type  height: int
        
        :param duration: Optional. Video duration
        :type  duration: int
        """
        super(InputMediaVideo, self).__init__("video", media)

        # type is set by InputMedia base class
        # media is set by InputMedia base class
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(width, None, int, parameter_name="width")
        self.width = width
        
        assert_type_or_raise(height, None, int, parameter_name="height")
        self.height = height
        
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
    # end def __init__

    def to_array(self):
        """
        Serializes this InputMediaVideo to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InputMediaVideo, self).to_array()
        # 'type' and 'media' given by superclass
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
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
        Deserialize a new InputMediaVideo from a given dictionary.

        :return: new InputMediaVideo instance.
        :rtype: InputMediaVideo
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        # 'type' is given by class type
        data['media'] = u(array.get('media'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['width'] = int(array.get('width')) if array.get('width') is not None else None
        data['height'] = int(array.get('height')) if array.get('height') is not None else None
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        
        instance = InputMediaVideo(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputmediavideo_instance)`
        """
        return "InputMediaVideo(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputmediavideo_instance)`
        """
        if self._raw:
            return "InputMediaVideo.from_array({self._raw})".format(self=self)
        # end if
        return "InputMediaVideo(type={self.type!r}, media={self.media!r}, caption={self.caption!r}, width={self.width!r}, height={self.height!r}, duration={self.duration!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputmediavideo_instance`
        """
        return key in ["type", "media", "caption", "width", "height", "duration"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class InputMediaVideo

