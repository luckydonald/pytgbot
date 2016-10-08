# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.logger import logging

from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)

class InlineQueryResult(Sendable):
    def __init__(self, id, type):
        assert(id is not None)
        if not isinstance(id, unicode_type):
            id = u(str(id))
        assert(isinstance(id, unicode_type))
        self.id = id

        self.type = type
        super(InlineQueryResult, self).__init__()

    def to_array(self):
        return {
            "type": self.type,
            "id": self.id,
        }
    # end def to_array
# end class InlineQueryResult


class InlineQueryCachedResult(InlineQueryResult):
    pass


class InputMessageContent(Sendable):
    pass


class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """
    def __init__(self, id, title, input_message_content, reply_markup=None, url=None, hide_url=None, description=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a link to an article or web page.

        https://core.telegram.org/bots/api#inlinequeryresultarticle


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id: str

        :param title: Title of the result
        :type  title: str

        :param input_message_content: Content of the message to be sent
        :type  input_message_content: InputMessageContent


        Optional keyword parameters:

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword url: Optional. URL of the result
        :type    url: str

        :keyword hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
        :type    hide_url: bool

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url: str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width: int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height: int
        """
        super(InlineQueryResultArticle, self).__init__(id, "article")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(input_message_content is not None)
        assert(isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(url is None or isinstance(url, str))
        self.url = url

        assert(hide_url is None or isinstance(hide_url, bool))
        self.hide_url = hide_url

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(thumb_url is None or isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultArticle to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultArticle, self).to_array()
        # 'type' and 'id' given by superclass
        array['title'] = str(self.title)  # type str
        array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.url is not None:
            array['url'] = str(self.url)  # type str
        if self.hide_url is not None:
            array['hide_url'] = bool(self.hide_url)  # type bool
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.thumb_url is not None:
            array['thumb_url'] = str(self.thumb_url)  # type str
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultArticle from a given dictionary.

        :return: new InlineQueryResultArticle instance.
        :rtype: InlineQueryResultArticle
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['title'] = str(array.get('title'))
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['url'] = str(array.get('url')) if array.get('url') is not None else None
        data['hide_url'] = bool(array.get('hide_url')) if array.get('hide_url') is not None else None
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['thumb_url'] = str(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return InlineQueryResultArticle(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultarticle_instance)`
        """
        return "InlineQueryResultArticle(type={self.type!r}, id={self.id!r}, title={self.title!r}, input_message_content={self.input_message_content!r}, reply_markup={self.reply_markup!r}, url={self.url!r}, hide_url={self.hide_url!r}, description={self.description!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultarticle_instance`
        """
        return key in ["type", "id", "title", "input_message_content", "reply_markup", "url", "hide_url", "description", "thumb_url", "thumb_width", "thumb_height"]
    # end def __contains__
# end class InlineQueryResultArticle


class InlineQueryResultPhoto(InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto
    """
    def __init__(self, id, photo_url, thumb_url, photo_width=None, photo_height=None, title=None, description=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultphoto


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
        :type  photo_url: str

        :param thumb_url: URL of the thumbnail for the photo
        :type  thumb_url: str


        Optional keyword parameters:

        :keyword photo_width: Optional. Width of the photo
        :type    photo_width: int

        :keyword photo_height: Optional. Height of the photo
        :type    photo_height: int

        :keyword title: Optional. Title for the result
        :type    title: str

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword caption: Optional. Caption of the photo to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the photo
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultPhoto, self).__init__(id, "photo")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(photo_url is not None)
        assert(isinstance(photo_url, str))
        self.photo_url = photo_url

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(photo_width is None or isinstance(photo_width, int))
        self.photo_width = photo_width

        assert(photo_height is None or isinstance(photo_height, int))
        self.photo_height = photo_height

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultPhoto to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultPhoto, self).to_array()
        # 'type' and 'id' given by superclass
        array['photo_url'] = str(self.photo_url)  # type str
        array['thumb_url'] = str(self.thumb_url)  # type str
        if self.photo_width is not None:
            array['photo_width'] = int(self.photo_width)  # type int
        if self.photo_height is not None:
            array['photo_height'] = int(self.photo_height)  # type int
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultPhoto from a given dictionary.

        :return: new InlineQueryResultPhoto instance.
        :rtype: InlineQueryResultPhoto
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['photo_url'] = str(array.get('photo_url'))
        data['thumb_url'] = str(array.get('thumb_url'))
        data['photo_width'] = int(array.get('photo_width')) if array.get('photo_width') is not None else None
        data['photo_height'] = int(array.get('photo_height')) if array.get('photo_height') is not None else None
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultPhoto(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultphoto_instance)`
        """
        return "InlineQueryResultPhoto(type={self.type!r}, id={self.id!r}, photo_url={self.photo_url!r}, thumb_url={self.thumb_url!r}, photo_width={self.photo_width!r}, photo_height={self.photo_height!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultphoto_instance`
        """
        return key in ["type", "id", "photo_url", "thumb_url", "photo_width", "photo_height", "title", "description", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultPhoto


class InlineQueryResultGif(InlineQueryResult):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif
    """
    def __init__(self, id, gif_url, thumb_url, gif_width=None, gif_height=None, title=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultgif


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB
        :type  gif_url: str

        :param thumb_url: URL of the static thumbnail for the result (jpeg or gif)
        :type  thumb_url: str


        Optional keyword parameters:

        :keyword gif_width: Optional. Width of the GIF
        :type    gif_width: int

        :keyword gif_height: Optional. Height of the GIF
        :type    gif_height: int

        :keyword title: Optional. Title for the result
        :type    title: str

        :keyword caption: Optional. Caption of the GIF file to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the GIF animation
        :type    input_message_content: inputMessageContent
        """
        super(InlineQueryResultGif, self).__init__(id, "gif")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(gif_url is not None)
        assert(isinstance(gif_url, str))
        self.gif_url = gif_url

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(gif_width is None or isinstance(gif_width, int))
        self.gif_width = gif_width

        assert(gif_height is None or isinstance(gif_height, int))
        self.gif_height = gif_height

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultGif to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultGif, self).to_array()
        # 'type' and 'id' given by superclass
        array['gif_url'] = str(self.gif_url)  # type str
        array['thumb_url'] = str(self.thumb_url)  # type str
        if self.gif_width is not None:
            array['gif_width'] = int(self.gif_width)  # type int
        if self.gif_height is not None:
            array['gif_height'] = int(self.gif_height)  # type int
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultGif from a given dictionary.

        :return: new InlineQueryResultGif instance.
        :rtype: InlineQueryResultGif
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['gif_url'] = str(array.get('gif_url'))
        data['thumb_url'] = str(array.get('thumb_url'))
        data['gif_width'] = int(array.get('gif_width')) if array.get('gif_width') is not None else None
        data['gif_height'] = int(array.get('gif_height')) if array.get('gif_height') is not None else None
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultGif(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultgif_instance)`
        """
        return "InlineQueryResultGif(type={self.type!r}, id={self.id!r}, gif_url={self.gif_url!r}, thumb_url={self.thumb_url!r}, gif_width={self.gif_width!r}, gif_height={self.gif_height!r}, title={self.title!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultgif_instance`
        """
        return key in ["type", "id", "gif_url", "thumb_url", "gif_width", "gif_height", "title", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultGif


class InlineQueryResultMpeg4Gif(InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """
    def __init__(self, id, mpeg4_url, thumb_url, mpeg4_width=None, mpeg4_height=None, title=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB
        :type  mpeg4_url: str

        :param thumb_url: URL of the static thumbnail (jpeg or gif) for the result
        :type  thumb_url: str


        Optional keyword parameters:

        :keyword mpeg4_width: Optional. Video width
        :type    mpeg4_width: int

        :keyword mpeg4_height: Optional. Video height
        :type    mpeg4_height: int

        :keyword title: Optional. Title for the result
        :type    title: str

        :keyword caption: Optional. Caption of the MPEG-4 file to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video animation
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultMpeg4Gif, self).__init__(id, "mpeg4_gif")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(mpeg4_url is not None)
        assert(isinstance(mpeg4_url, str))
        self.mpeg4_url = mpeg4_url

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(mpeg4_width is None or isinstance(mpeg4_width, int))
        self.mpeg4_width = mpeg4_width

        assert(mpeg4_height is None or isinstance(mpeg4_height, int))
        self.mpeg4_height = mpeg4_height

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultMpeg4Gif to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultMpeg4Gif, self).to_array()
        # 'type' and 'id' given by superclass
        array['mpeg4_url'] = str(self.mpeg4_url)  # type str
        array['thumb_url'] = str(self.thumb_url)  # type str
        if self.mpeg4_width is not None:
            array['mpeg4_width'] = int(self.mpeg4_width)  # type int
        if self.mpeg4_height is not None:
            array['mpeg4_height'] = int(self.mpeg4_height)  # type int
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultMpeg4Gif from a given dictionary.

        :return: new InlineQueryResultMpeg4Gif instance.
        :rtype: InlineQueryResultMpeg4Gif
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['mpeg4_url'] = str(array.get('mpeg4_url'))
        data['thumb_url'] = str(array.get('thumb_url'))
        data['mpeg4_width'] = int(array.get('mpeg4_width')) if array.get('mpeg4_width') is not None else None
        data['mpeg4_height'] = int(array.get('mpeg4_height')) if array.get('mpeg4_height') is not None else None
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultMpeg4Gif(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultmpeg4gif_instance)`
        """
        return "InlineQueryResultMpeg4Gif(type={self.type!r}, id={self.id!r}, mpeg4_url={self.mpeg4_url!r}, thumb_url={self.thumb_url!r}, mpeg4_width={self.mpeg4_width!r}, mpeg4_height={self.mpeg4_height!r}, title={self.title!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultmpeg4gif_instance`
        """
        return key in ["type", "id", "mpeg4_url", "thumb_url", "mpeg4_width", "mpeg4_height", "title", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultMpeg4Gif


class InlineQueryResultVideo(InlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultvideo
    """
    def __init__(self, id, video_url, mime_type, thumb_url, title, caption=None, video_width=None, video_height=None, video_duration=None, description=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultvideo


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param video_url: A valid URL for the embedded video player or video file
        :type  video_url: str

        :param mime_type: Mime type of the content of video url, “text/html” or “video/mp4”
        :type  mime_type: str

        :param thumb_url: URL of the thumbnail (jpeg only) for the video
        :type  thumb_url: str

        :param title: Title for the result
        :type  title: str


        Optional keyword parameters:

        :keyword caption: Optional. Caption of the video to be sent, 0-200 characters
        :type    caption: str

        :keyword video_width: Optional. Video width
        :type    video_width: int

        :keyword video_height: Optional. Video height
        :type    video_height: int

        :keyword video_duration: Optional. Video duration in seconds
        :type    video_duration: int

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultVideo, self).__init__(id, "video")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(video_url is not None)
        assert(isinstance(video_url, str))
        self.video_url = video_url

        assert(mime_type is not None)
        assert(isinstance(mime_type, str))
        self.mime_type = mime_type

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(video_width is None or isinstance(video_width, int))
        self.video_width = video_width

        assert(video_height is None or isinstance(video_height, int))
        self.video_height = video_height

        assert(video_duration is None or isinstance(video_duration, int))
        self.video_duration = video_duration

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultVideo to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultVideo, self).to_array()
        # 'type' and 'id' given by superclass
        array['video_url'] = str(self.video_url)  # type str
        array['mime_type'] = str(self.mime_type)  # type str
        array['thumb_url'] = str(self.thumb_url)  # type str
        array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.video_width is not None:
            array['video_width'] = int(self.video_width)  # type int
        if self.video_height is not None:
            array['video_height'] = int(self.video_height)  # type int
        if self.video_duration is not None:
            array['video_duration'] = int(self.video_duration)  # type int
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultVideo from a given dictionary.

        :return: new InlineQueryResultVideo instance.
        :rtype: InlineQueryResultVideo
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['video_url'] = str(array.get('video_url'))
        data['mime_type'] = str(array.get('mime_type'))
        data['thumb_url'] = str(array.get('thumb_url'))
        data['title'] = str(array.get('title'))
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['video_width'] = int(array.get('video_width')) if array.get('video_width') is not None else None
        data['video_height'] = int(array.get('video_height')) if array.get('video_height') is not None else None
        data['video_duration'] = int(array.get('video_duration')) if array.get('video_duration') is not None else None
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultVideo(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultvideo_instance)`
        """
        return "InlineQueryResultVideo(type={self.type!r}, id={self.id!r}, video_url={self.video_url!r}, mime_type={self.mime_type!r}, thumb_url={self.thumb_url!r}, title={self.title!r}, caption={self.caption!r}, video_width={self.video_width!r}, video_height={self.video_height!r}, video_duration={self.video_duration!r}, description={self.description!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultvideo_instance`
        """
        return key in ["type", "id", "video_url", "mime_type", "thumb_url", "title", "caption", "video_width", "video_height", "video_duration", "description", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultVideo


class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """
    def __init__(self, id, audio_url, title, caption=None, performer=None, audio_duration=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultaudio


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param audio_url: A valid URL for the audio file
        :type  audio_url: str

        :param title: Title
        :type  title: str


        Optional keyword parameters:

        :keyword caption: Optional. Caption, 0-200 characters
        :type    caption: str

        :keyword performer: Optional. Performer
        :type    performer: str

        :keyword audio_duration: Optional. Audio duration in seconds
        :type    audio_duration: int

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the audio
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultAudio, self).__init__(id, "audio")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(audio_url is not None)
        assert(isinstance(audio_url, str))
        self.audio_url = audio_url

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(performer is None or isinstance(performer, str))
        self.performer = performer

        assert(audio_duration is None or isinstance(audio_duration, int))
        self.audio_duration = audio_duration

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultAudio to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultAudio, self).to_array()
        # 'type' and 'id' given by superclass
        array['audio_url'] = str(self.audio_url)  # type str
        array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.performer is not None:
            array['performer'] = str(self.performer)  # type str
        if self.audio_duration is not None:
            array['audio_duration'] = int(self.audio_duration)  # type int
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultAudio from a given dictionary.

        :return: new InlineQueryResultAudio instance.
        :rtype: InlineQueryResultAudio
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['audio_url'] = str(array.get('audio_url'))
        data['title'] = str(array.get('title'))
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['performer'] = str(array.get('performer')) if array.get('performer') is not None else None
        data['audio_duration'] = int(array.get('audio_duration')) if array.get('audio_duration') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultAudio(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultaudio_instance)`
        """
        return "InlineQueryResultAudio(type={self.type!r}, id={self.id!r}, audio_url={self.audio_url!r}, title={self.title!r}, caption={self.caption!r}, performer={self.performer!r}, audio_duration={self.audio_duration!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultaudio_instance`
        """
        return key in ["type", "id", "audio_url", "title", "caption", "performer", "audio_duration", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultAudio


class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice
    """
    def __init__(self, id, voice_url, title, caption=None, voice_duration=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvoice


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param voice_url: A valid URL for the voice recording
        :type  voice_url: str

        :param title: Recording title
        :type  title: str


        Optional keyword parameters:

        :keyword caption: Optional. Caption, 0-200 characters
        :type    caption: str

        :keyword voice_duration: Optional. Recording duration in seconds
        :type    voice_duration: int

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the voice recording
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultVoice, self).__init__(id, "voice")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(voice_url is not None)
        assert(isinstance(voice_url, str))
        self.voice_url = voice_url

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(voice_duration is None or isinstance(voice_duration, int))
        self.voice_duration = voice_duration

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultVoice to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultVoice, self).to_array()
        # 'type' and 'id' given by superclass
        array['voice_url'] = str(self.voice_url)  # type str
        array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.voice_duration is not None:
            array['voice_duration'] = int(self.voice_duration)  # type int
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultVoice from a given dictionary.

        :return: new InlineQueryResultVoice instance.
        :rtype: InlineQueryResultVoice
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['voice_url'] = str(array.get('voice_url'))
        data['title'] = str(array.get('title'))
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['voice_duration'] = int(array.get('voice_duration')) if array.get('voice_duration') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultVoice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultvoice_instance)`
        """
        return "InlineQueryResultVoice(type={self.type!r}, id={self.id!r}, voice_url={self.voice_url!r}, title={self.title!r}, caption={self.caption!r}, voice_duration={self.voice_duration!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultvoice_instance`
        """
        return key in ["type", "id", "voice_url", "title", "caption", "voice_duration", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultVoice


class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultdocument
    """
    def __init__(self, id, title, document_url, mime_type, caption=None, description=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultdocument


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param title: Title for the result
        :type  title: str

        :param document_url: A valid URL for the file
        :type  document_url: str

        :param mime_type: Mime type of the content of the file, either “application/pdf” or “application/zip”
        :type  mime_type: str


        Optional keyword parameters:

        :keyword caption: Optional. Caption of the document to be sent, 0-200 characters
        :type    caption: str

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the file
        :type    input_message_content: InputMessageContent

        :keyword thumb_url: Optional. URL of the thumbnail (jpeg only) for the file
        :type    thumb_url: str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width: int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height: int
        """
        super(InlineQueryResultDocument, self).__init__(id, "document")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(document_url is not None)
        assert(isinstance(document_url, str))
        self.document_url = document_url

        assert(mime_type is not None)
        assert(isinstance(mime_type, str))
        self.mime_type = mime_type

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultDocument to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultDocument, self).to_array()
        # 'type' and 'id' given by superclass
        array['title'] = str(self.title)  # type str
        array['document_url'] = str(self.document_url)  # type str
        array['mime_type'] = str(self.mime_type)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        if self.thumb_url is not None:
            array['thumb_url'] = str(self.thumb_url)  # type str
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultDocument from a given dictionary.

        :return: new InlineQueryResultDocument instance.
        :rtype: InlineQueryResultDocument
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['title'] = str(array.get('title'))
        data['document_url'] = str(array.get('document_url'))
        data['mime_type'] = str(array.get('mime_type'))
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = str(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return InlineQueryResultDocument(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultdocument_instance)`
        """
        return "InlineQueryResultDocument(type={self.type!r}, id={self.id!r}, title={self.title!r}, document_url={self.document_url!r}, mime_type={self.mime_type!r}, caption={self.caption!r}, description={self.description!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultdocument_instance`
        """
        return key in ["type", "id", "title", "document_url", "mime_type", "caption", "description", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
    # end def __contains__
# end class InlineQueryResultDocument


class InlineQueryResultLocation(InlineQueryResult):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation
    """
    def __init__(self, id, latitude, longitude, title, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultlocation


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id: str

        :param latitude: Location latitude in degrees
        :type  latitude: float

        :param longitude: Location longitude in degrees
        :type  longitude: float

        :param title: Location title
        :type  title: str


        Optional keyword parameters:

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the location
        :type    input_message_content: InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url: str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width: int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height: int
        """
        super(InlineQueryResultLocation, self).__init__(id, "location")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude

        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultLocation to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultLocation, self).to_array()
        # 'type' and 'id' given by superclass
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        array['title'] = str(self.title)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        if self.thumb_url is not None:
            array['thumb_url'] = str(self.thumb_url)  # type str
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultLocation from a given dictionary.

        :return: new InlineQueryResultLocation instance.
        :rtype: InlineQueryResultLocation
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['title'] = str(array.get('title'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = str(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return InlineQueryResultLocation(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultlocation_instance)`
        """
        return "InlineQueryResultLocation(type={self.type!r}, id={self.id!r}, latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultlocation_instance`
        """
        return key in ["type", "id", "latitude", "longitude", "title", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
    # end def __contains__
# end class InlineQueryResultLocation


class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue
    """
    def __init__(self, id, latitude, longitude, title, address, foursquare_id=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvenue


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id: str

        :param latitude: Latitude of the venue location in degrees
        :type  latitude: float

        :param longitude: Longitude of the venue location in degrees
        :type  longitude: float

        :param title: Title of the venue
        :type  title: str

        :param address: Address of the venue
        :type  address: str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue if known
        :type    foursquare_id: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the venue
        :type    input_message_content: InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url: str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width: int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height: int
        """
        super(InlineQueryResultVenue, self).__init__(id, "venue")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude

        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(address is not None)
        assert(isinstance(address, str))
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, str))
        self.foursquare_id = foursquare_id

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultVenue to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultVenue, self).to_array()
        # 'type' and 'id' given by superclass
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        array['title'] = str(self.title)  # type str
        array['address'] = str(self.address)  # type str
        if self.foursquare_id is not None:
            array['foursquare_id'] = str(self.foursquare_id)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        if self.thumb_url is not None:
            array['thumb_url'] = str(self.thumb_url)  # type str
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultVenue from a given dictionary.

        :return: new InlineQueryResultVenue instance.
        :rtype: InlineQueryResultVenue
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['title'] = str(array.get('title'))
        data['address'] = str(array.get('address'))
        data['foursquare_id'] = str(array.get('foursquare_id')) if array.get('foursquare_id') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = str(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return InlineQueryResultVenue(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultvenue_instance)`
        """
        return "InlineQueryResultVenue(type={self.type!r}, id={self.id!r}, latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultvenue_instance`
        """
        return key in ["type", "id", "latitude", "longitude", "title", "address", "foursquare_id", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
    # end def __contains__
# end class InlineQueryResultVenue


class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact
    """
    def __init__(self, id, phone_number, first_name, last_name=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcontact


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id: str

        :param phone_number: Contact's phone number
        :type  phone_number: str

        :param first_name: Contact's first name
        :type  first_name: str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the contact
        :type    input_message_content: InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url: str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width: int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height: int
        """
        super(InlineQueryResultContact, self).__init__(id, "contact")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(phone_number is not None)
        assert(isinstance(phone_number, str))
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, str))
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, str))
        self.last_name = last_name

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, str))
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultContact to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultContact, self).to_array()
        # 'type' and 'id' given by superclass
        array['phone_number'] = str(self.phone_number)  # type str
        array['first_name'] = str(self.first_name)  # type str
        if self.last_name is not None:
            array['last_name'] = str(self.last_name)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        if self.thumb_url is not None:
            array['thumb_url'] = str(self.thumb_url)  # type str
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultContact from a given dictionary.

        :return: new InlineQueryResultContact instance.
        :rtype: InlineQueryResultContact
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # type is given by class type
        data['id'] = str(array.get('id'))
        data['phone_number'] = str(array.get('phone_number'))
        data['first_name'] = str(array.get('first_name'))
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = str(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return InlineQueryResultContact(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcontact_instance)`
        """
        return "InlineQueryResultContact(type={self.type!r}, id={self.id!r}, phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcontact_instance`
        """
        return key in ["type", "id", "phone_number", "first_name", "last_name", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
    # end def __contains__
# end class InlineQueryResultContact



class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    https://core.telegram.org/bots/api#inlinequeryresultgame
    """
    def __init__(self, type, id, game_short_name, reply_markup=None):
        """
        Represents a Game.
        Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

        https://core.telegram.org/bots/api#inlinequeryresultgame


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param game_short_name: Short name of the game
        :type  game_short_name: str


        Optional keyword parameters:

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
        """
        super(InlineQueryResultGame, self).__init__(id, "game")
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(game_short_name is not None)
        assert(isinstance(game_short_name, str))
        self.game_short_name = game_short_name

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultGame to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultGame, self).to_array()
        # 'type' and 'id' given by superclass
        array['game_short_name'] = str(self.game_short_name)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultGame from a given dictionary.

        :return: new InlineQueryResultGame instance.
        :rtype: InlineQueryResultGame
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # type is given by class type
        data['id'] = str(array.get('id'))
        data['game_short_name'] = str(array.get('game_short_name'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        return InlineQueryResultGame(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultgame_instance)`
        """
        return "InlineQueryResultGame(type={self.type!r}, id={self.id!r}, game_short_name={self.game_short_name!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultgame_instance`
        """
        return key in ["type", "id", "game_short_name", "reply_markup"]
    # end def __contains__
# end class InlineQueryResultGame



class InlineQueryResultCachedPhoto(InlineQueryCachedResult):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """
    def __init__(self, id, photo_file_id, title=None, description=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultcachedphoto


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param photo_file_id: A valid file identifier of the photo
        :type  photo_file_id: str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title: str

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword caption: Optional. Caption of the photo to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the photo
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedPhoto, self).__init__(id, "photo")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(photo_file_id is not None)
        assert(isinstance(photo_file_id, str))
        self.photo_file_id = photo_file_id

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedPhoto to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedPhoto, self).to_array()
        array['photo_file_id'] = str(self.photo_file_id)  # type str
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedPhoto from a given dictionary.

        :return: new InlineQueryResultCachedPhoto instance.
        :rtype: InlineQueryResultCachedPhoto
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['photo_file_id'] = str(array.get('photo_file_id'))
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedPhoto(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedphoto_instance)`
        """
        return "InlineQueryResultCachedPhoto(type={self.type!r}, id={self.id!r}, photo_file_id={self.photo_file_id!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedphoto_instance`
        """
        return key in ["type", "id", "photo_file_id", "title", "description", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedPhoto


class InlineQueryResultCachedGif(InlineQueryCachedResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    """
    def __init__(self, id, gif_file_id, title=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedgif


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param gif_file_id: A valid file identifier for the GIF file
        :type  gif_file_id: str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title: str

        :keyword caption: Optional. Caption of the GIF file to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the GIF animation
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedGif, self).__init__(id, "gif")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(gif_file_id is not None)
        assert(isinstance(gif_file_id, str))
        self.gif_file_id = gif_file_id

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedGif to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedGif, self).to_array()
        # 'type' and 'id' given by superclass
        array['gif_file_id'] = str(self.gif_file_id)  # type str
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedGif from a given dictionary.

        :return: new InlineQueryResultCachedGif instance.
        :rtype: InlineQueryResultCachedGif
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # type is given by class type
        data['id'] = str(array.get('id'))
        data['gif_file_id'] = str(array.get('gif_file_id'))
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedGif(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedgif_instance)`
        """
        return "InlineQueryResultCachedGif(type={self.type!r}, id={self.id!r}, gif_file_id={self.gif_file_id!r}, title={self.title!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedgif_instance`
        """
        return key in ["type", "id", "gif_file_id", "title", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedGif


class InlineQueryResultCachedMpeg4Gif(InlineQueryCachedResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """
    def __init__(self, id, mpeg4_file_id, title=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param mpeg4_file_id: A valid file identifier for the MP4 file
        :type  mpeg4_file_id: str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title: str

        :keyword caption: Optional. Caption of the MPEG-4 file to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video animation
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedMpeg4Gif, self).__init__(id, "mpeg4_gif")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(mpeg4_file_id is not None)
        assert(isinstance(mpeg4_file_id, str))
        self.mpeg4_file_id = mpeg4_file_id

        assert(title is None or isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedMpeg4Gif to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedMpeg4Gif, self).to_array()
        # 'type' and 'id' given by superclass
        array['mpeg4_file_id'] = str(self.mpeg4_file_id)  # type str
        if self.title is not None:
            array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedMpeg4Gif from a given dictionary.

        :return: new InlineQueryResultCachedMpeg4Gif instance.
        :rtype: InlineQueryResultCachedMpeg4Gif
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['mpeg4_file_id'] = str(array.get('mpeg4_file_id'))
        data['title'] = str(array.get('title')) if array.get('title') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedMpeg4Gif(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedmpeg4gif_instance)`
        """
        return "InlineQueryResultCachedMpeg4Gif(type={self.type!r}, id={self.id!r}, mpeg4_file_id={self.mpeg4_file_id!r}, title={self.title!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedmpeg4gif_instance`
        """
        return key in ["type", "id", "mpeg4_file_id", "title", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedMpeg4Gif



class InlineQueryResultCachedSticker(InlineQueryCachedResult):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """
    def __init__(self, id, sticker_file_id, reply_markup=None, input_message_content=None):
        """
        Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedsticker


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param sticker_file_id: A valid file identifier of the sticker
        :type  sticker_file_id: str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the sticker
        :type    input_message_content: pytgbot.api_types.sendable.inline.InputMessageContent
        """
        super(InlineQueryResultCachedSticker, self).__init__(id, "sicker")
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(sticker_file_id is not None)
        assert(isinstance(sticker_file_id, str))
        self.sticker_file_id = sticker_file_id

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedSticker to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedSticker, self).to_array()
        # 'type' and 'id' given by superclass
        array['sticker_file_id'] = str(self.sticker_file_id)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedSticker from a given dictionary.

        :return: new InlineQueryResultCachedSticker instance.
        :rtype: InlineQueryResultCachedSticker
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['sticker_file_id'] = str(array.get('sticker_file_id'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedSticker(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedsticker_instance)`
        """
        return "InlineQueryResultCachedSticker(type={self.type!r}, id={self.id!r}, sticker_file_id={self.sticker_file_id!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedsticker_instance`
        """
        return key in ["type", "id", "sticker_file_id", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedSticker



class InlineQueryResultCachedDocument(InlineQueryCachedResult):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only pdf-files and zip archives can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """
    def __init__(self, id, title, document_file_id, description=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only pdf-files and zip archives can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcacheddocument


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param title: Title for the result
        :type  title: str

        :param document_file_id: A valid file identifier for the file
        :type  document_file_id: str


        Optional keyword parameters:

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword caption: Optional. Caption of the document to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the file
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedDocument, self).__init__(id, "document")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(document_file_id is not None)
        assert(isinstance(document_file_id, str))
        self.document_file_id = document_file_id

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedDocument to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedDocument, self).to_array()
        # 'type' and 'id' given by superclass
        array['title'] = str(self.title)  # type str
        array['document_file_id'] = str(self.document_file_id)  # type str
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedDocument from a given dictionary.

        :return: new InlineQueryResultCachedDocument instance.
        :rtype: InlineQueryResultCachedDocument
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        data['id'] = str(array.get('id'))
        data['title'] = str(array.get('title'))
        data['document_file_id'] = str(array.get('document_file_id'))
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedDocument(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcacheddocument_instance)`
        """
        return "InlineQueryResultCachedDocument(type={self.type!r}, id={self.id!r}, title={self.title!r}, document_file_id={self.document_file_id!r}, description={self.description!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcacheddocument_instance`
        """
        return key in ["type", "id", "title", "document_file_id", "description", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedDocument


class InlineQueryResultCachedVideo(InlineQueryCachedResult):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    """
    def __init__(self, id, video_file_id, title, description=None, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvideo


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param video_file_id: A valid file identifier for the video file
        :type  video_file_id: str

        :param title: Title for the result
        :type  title: str


        Optional keyword parameters:

        :keyword description: Optional. Short description of the result
        :type    description: str

        :keyword caption: Optional. Caption of the video to be sent, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedVideo, self).__init__(id, "video")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(video_file_id is not None)
        assert(isinstance(video_file_id, str))
        self.video_file_id = video_file_id

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(description is None or isinstance(description, str))
        self.description = description

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedVideo to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedVideo, self).to_array()
        # 'type' and 'id' given by superclass
        array['video_file_id'] = str(self.video_file_id)  # type str
        array['title'] = str(self.title)  # type str
        if self.description is not None:
            array['description'] = str(self.description)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedVideo from a given dictionary.

        :return: new InlineQueryResultCachedVideo instance.
        :rtype: InlineQueryResultCachedVideo
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['video_file_id'] = str(array.get('video_file_id'))
        data['title'] = str(array.get('title'))
        data['description'] = str(array.get('description')) if array.get('description') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedVideo(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedvideo_instance)`
        """
        return "InlineQueryResultCachedVideo(type={self.type!r}, id={self.id!r}, video_file_id={self.video_file_id!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedvideo_instance`
        """
        return key in ["type", "id", "video_file_id", "title", "description", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedVideo


class InlineQueryResultCachedVoice(InlineQueryCachedResult):
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    """
    def __init__(self, id, voice_file_id, title, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvoice


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param voice_file_id: A valid file identifier for the voice message
        :type  voice_file_id: str

        :param title: Voice message title
        :type  title: str


        Optional keyword parameters:

        :keyword caption: Optional. Caption, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the voice message
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedVoice, self).__init__(id, "voice")

        # type is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(voice_file_id is not None)
        assert(isinstance(voice_file_id, str))
        self.voice_file_id = voice_file_id

        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedVoice to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedVoice, self).to_array()
        # 'type' and 'id' given by superclass
        array['voice_file_id'] = str(self.voice_file_id)  # type str
        array['title'] = str(self.title)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedVoice from a given dictionary.

        :return: new InlineQueryResultCachedVoice instance.
        :rtype: InlineQueryResultCachedVoice
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['voice_file_id'] = str(array.get('voice_file_id'))
        data['title'] = str(array.get('title'))
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedVoice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedvoice_instance)`
        """
        return "InlineQueryResultCachedVoice(type={self.type!r}, id={self.id!r}, voice_file_id={self.voice_file_id!r}, title={self.title!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedvoice_instance`
        """
        return key in ["type", "id", "voice_file_id", "title", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedVoice


class InlineQueryResultCachedAudio(InlineQueryCachedResult):
    """
    Represents a link to an mp3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """
    def __init__(self, id, audio_file_id, caption=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an mp3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedaudio


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str

        :param audio_file_id: A valid file identifier for the audio file
        :type  audio_file_id: str


        Optional keyword parameters:

        :keyword caption: Optional. Caption, 0-200 characters
        :type    caption: str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the audio
        :type    input_message_content: InputMessageContent
        """
        super(InlineQueryResultCachedAudio, self).__init__(id, "audio")

        # 'type' is given by class type

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(audio_file_id is not None)
        assert(isinstance(audio_file_id, str))
        self.audio_file_id = audio_file_id

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineQueryResultCachedAudio to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineQueryResultCachedAudio, self).to_array()
        # 'type' and 'id' given by superclass
        array['audio_file_id'] = str(self.audio_file_id)  # type str
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineQueryResultCachedAudio from a given dictionary.

        :return: new InlineQueryResultCachedAudio instance.
        :rtype: InlineQueryResultCachedAudio
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        data = {}
        # 'type' is given by class type
        data['id'] = str(array.get('id'))
        data['audio_file_id'] = str(array.get('audio_file_id'))
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return InlineQueryResultCachedAudio(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedaudio_instance)`
        """
        return "InlineQueryResultCachedAudio(type={self.type!r}, id={self.id!r}, audio_file_id={self.audio_file_id!r}, caption={self.caption!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedaudio_instance`
        """
        return key in ["type", "id", "audio_file_id", "caption", "reply_markup", "input_message_content"]
    # end def __contains__
# end class InlineQueryResultCachedAudio


class InputTextMessageContent(InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    def __init__(self, message_text, parse_mode=None, disable_web_page_preview=False):
        """
        Represents the content of a text message to be sent as the result of an inline query.

        https://core.telegram.org/bots/api#inputtextmessagecontent


        Parameters:

        :param message_text: Text of the message to be sent, 1-4096 characters
        :type  message_text: str


        Optional keyword parameters:

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode: str

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview: bool
        """
        super(InputTextMessageContent, self).__init__()
        assert(message_text is not None)
        assert(isinstance(message_text, str))
        self.message_text = message_text

        assert(parse_mode is None or isinstance(parse_mode, str))
        self.parse_mode = parse_mode

        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self):
        """
        Serializes this InputTextMessageContent to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InputTextMessageContent, self).to_array()
        array['message_text'] = str(self.message_text)  # type str
        if self.parse_mode is not None:
            array['parse_mode'] = str(self.parse_mode)  # type str
        if self.disable_web_page_preview is not None:
            array['disable_web_page_preview'] = bool(self.disable_web_page_preview)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InputTextMessageContent from a given dictionary.

        :return: new InputTextMessageContent instance.
        :rtype: InputTextMessageContent
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['message_text'] = str(array.get('message_text'))
        data['parse_mode'] = str(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['disable_web_page_preview'] = bool(array.get('disable_web_page_preview')) if array.get('disable_web_page_preview') is not None else None
        return InputTextMessageContent(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputtextmessagecontent_instance)`
        """
        return "InputTextMessageContent(message_text={self.message_text!r}, parse_mode={self.parse_mode!r}, disable_web_page_preview={self.disable_web_page_preview!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inputtextmessagecontent_instance`
        """
        return key in ["message_text", "parse_mode", "disable_web_page_preview"]
    # end def __contains__
# end class InputTextMessageContent


class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    def __init__(self, latitude, longitude):
        """
        Represents the content of a location message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputlocationmessagecontent


        Parameters:

        :param latitude: Latitude of the location in degrees
        :type  latitude: float

        :param longitude: Longitude of the location in degrees
        :type  longitude: float
        """
        super(InputLocationMessageContent, self).__init__()
        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude

        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude
    # end def __init__

    def to_array(self):
        """
        Serializes this InputLocationMessageContent to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InputLocationMessageContent, self).to_array()
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InputLocationMessageContent from a given dictionary.

        :return: new InputLocationMessageContent instance.
        :rtype: InputLocationMessageContent
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        return InputLocationMessageContent(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputlocationmessagecontent_instance)`
        """
        return "InputLocationMessageContent(latitude={self.latitude!r}, longitude={self.longitude!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inputlocationmessagecontent_instance`
        """
        return key in ["latitude", "longitude"]
    # end def __contains__
# end class InputLocationMessageContent


class InputVenueMessageContent(InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    def __init__(self, latitude, longitude, title, address, foursquare_id=None):
        """
        Represents the content of a venue message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputvenuemessagecontent


        Parameters:

        :param latitude: Latitude of the venue in degrees
        :type  latitude: float

        :param longitude: Longitude of the venue in degrees
        :type  longitude: float

        :param title: Name of the venue
        :type  title: str

        :param address: Address of the venue
        :type  address: str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue, if known
        :type    foursquare_id: str
        """
        super(InputVenueMessageContent, self).__init__()
        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude

        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude

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
        Serializes this InputVenueMessageContent to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InputVenueMessageContent, self).to_array()
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        array['title'] = str(self.title)  # type str
        array['address'] = str(self.address)  # type str
        if self.foursquare_id is not None:
            array['foursquare_id'] = str(self.foursquare_id)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InputVenueMessageContent from a given dictionary.

        :return: new InputVenueMessageContent instance.
        :rtype: InputVenueMessageContent
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['title'] = str(array.get('title'))
        data['address'] = str(array.get('address'))
        data['foursquare_id'] = str(array.get('foursquare_id')) if array.get('foursquare_id') is not None else None
        return InputVenueMessageContent(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputvenuemessagecontent_instance)`
        """
        return "InputVenueMessageContent(latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inputvenuemessagecontent_instance`
        """
        return key in ["latitude", "longitude", "title", "address", "foursquare_id"]
    # end def __contains__
# end class InputVenueMessageContent


class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    def __init__(self, phone_number, first_name, last_name=None):
        """
        Represents the content of a contact message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputcontactmessagecontent


        Parameters:

        :param phone_number: Contact's phone number
        :type  phone_number: str

        :param first_name: Contact's first name
        :type  first_name: str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name: str
        """
        super(InputContactMessageContent, self).__init__()
        assert(phone_number is not None)
        assert(isinstance(phone_number, str))
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, str))
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, str))
        self.last_name = last_name
    # end def __init__

    def to_array(self):
        """
        Serializes this InputContactMessageContent to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InputContactMessageContent, self).to_array()
        array['phone_number'] = str(self.phone_number)  # type str
        array['first_name'] = str(self.first_name)  # type str
        if self.last_name is not None:
            array['last_name'] = str(self.last_name)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InputContactMessageContent from a given dictionary.

        :return: new InputContactMessageContent instance.
        :rtype: InputContactMessageContent
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['phone_number'] = str(array.get('phone_number'))
        data['first_name'] = str(array.get('first_name'))
        data['last_name'] = str(array.get('last_name')) if array.get('last_name') is not None else None
        return InputContactMessageContent(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputcontactmessagecontent_instance)`
        """
        return "InputContactMessageContent(phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inputcontactmessagecontent_instance`
        """
        return key in ["phone_number", "first_name", "last_name"]
    # end def __contains__
# end class InputContactMessageContent
