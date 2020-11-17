# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

__author__ = 'luckydonald'


class InlineQueryResult(Sendable):
    """
    This object represents one result of an inline query.

    Telegram clients currently support results of 20 types.

    https://core.telegram.org/bots/api#inlinequeryresult

    Optional keyword parameters:
    """

    def __init__(self, id, type):
        assert_type_or_raise(id, unicode_type, int, parameter_name="id")
        if not isinstance(id, unicode_type):
            id = u(id)
        assert(isinstance(id, unicode_type))
        self.id = id
        self.type = type
        super(InlineQueryResult, self).__init__()
    # end def

    def to_array(self):
        return {
            "type": u(self.type),
            "id": u(self.id),
        }
    # end def to_array
# end class InlineQueryResult


class InlineQueryCachedResult(InlineQueryResult):
    """
    Parent class of all those cached inline results.

    Optional keyword parameters:
    """

    pass
# end class InlineQueryCachedResult


class InputMessageContent(Sendable):
    """
    Parent class of all those input message content.

    Optional keyword parameters:
    """

    pass
# end class InputMessageContent


class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle


    Parameters:

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

    def __init__(self, id, title, input_message_content, reply_markup=None, url=None, hide_url=None, description=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a link to an article or web page.

        https://core.telegram.org/bots/api#inlinequeryresultarticle


        Parameters:

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
        super(InlineQueryResultArticle, self).__init__(id, "article")
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(input_message_content, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(url, None, unicode_type, parameter_name="url")
        self.url = url
        assert_type_or_raise(hide_url, None, bool, parameter_name="hide_url")
        self.hide_url = hide_url
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(thumb_url, None, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(thumb_width, None, int, parameter_name="thumb_width")
        self.thumb_width = thumb_width
        assert_type_or_raise(thumb_height, None, int, parameter_name="thumb_height")
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultArticle to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultArticle, self).to_array()

        # 'type' given by superclass
        # 'id' given by superclass
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.url is not None:
            array['url'] = u(self.url)  # py2: type unicode, py3: type str
        # end if
        if self.hide_url is not None:
            array['hide_url'] = bool(self.hide_url)  # type bool
        # end if
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.thumb_url is not None:
            array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        # end if
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        # end if
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultArticle constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        data['id'] = u(array.get('id'))
        data['title'] = u(array.get('title'))
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['url'] = u(array.get('url')) if array.get('url') is not None else None
        data['hide_url'] = bool(array.get('hide_url')) if array.get('hide_url') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['thumb_url'] = u(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultArticle from a given dictionary.

        :return: new InlineQueryResultArticle instance.
        :rtype: InlineQueryResultArticle
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultArticle.validate_array(array)
        instance = InlineQueryResultArticle(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultarticle_instance)`
        """
        return "InlineQueryResultArticle(type={self.type!r}, id={self.id!r}, title={self.title!r}, input_message_content={self.input_message_content!r}, reply_markup={self.reply_markup!r}, url={self.url!r}, hide_url={self.hide_url!r}, description={self.description!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultarticle_instance)`
        """
        if self._raw:
            return "InlineQueryResultArticle.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultArticle(type={self.type!r}, id={self.id!r}, title={self.title!r}, input_message_content={self.input_message_content!r}, reply_markup={self.reply_markup!r}, url={self.url!r}, hide_url={self.hide_url!r}, description={self.description!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultarticle_instance`
        """
        return (
            key in ["type", "id", "title", "input_message_content", "reply_markup", "url", "hide_url", "description", "thumb_url", "thumb_width", "thumb_height"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultArticle


class InlineQueryResultPhoto(InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto


    Parameters:

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
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

    def __init__(self, id, photo_url, thumb_url, photo_width=None, photo_height=None, title=None, description=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultphoto


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str|unicode

        :param photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
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
        super(InlineQueryResultPhoto, self).__init__(id, "photo")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(photo_url, unicode_type, parameter_name="photo_url")
        self.photo_url = photo_url
        assert_type_or_raise(thumb_url, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(photo_width, None, int, parameter_name="photo_width")
        self.photo_width = photo_width
        assert_type_or_raise(photo_height, None, int, parameter_name="photo_height")
        self.photo_height = photo_height
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultPhoto to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultPhoto, self).to_array()

        # 'type' given by superclass
        # 'id' given by superclass
        array['photo_url'] = u(self.photo_url)  # py2: type unicode, py3: type str
        array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        if self.photo_width is not None:
            array['photo_width'] = int(self.photo_width)  # type int
        # end if
        if self.photo_height is not None:
            array['photo_height'] = int(self.photo_height)  # type int
        # end if
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultPhoto constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        data['id'] = u(array.get('id'))
        data['photo_url'] = u(array.get('photo_url'))
        data['thumb_url'] = u(array.get('thumb_url'))
        data['photo_width'] = int(array.get('photo_width')) if array.get('photo_width') is not None else None
        data['photo_height'] = int(array.get('photo_height')) if array.get('photo_height') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultPhoto from a given dictionary.

        :return: new InlineQueryResultPhoto instance.
        :rtype: InlineQueryResultPhoto
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultPhoto.validate_array(array)
        instance = InlineQueryResultPhoto(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultphoto_instance)`
        """
        return "InlineQueryResultPhoto(type={self.type!r}, id={self.id!r}, photo_url={self.photo_url!r}, thumb_url={self.thumb_url!r}, photo_width={self.photo_width!r}, photo_height={self.photo_height!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultphoto_instance)`
        """
        if self._raw:
            return "InlineQueryResultPhoto.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultPhoto(type={self.type!r}, id={self.id!r}, photo_url={self.photo_url!r}, thumb_url={self.thumb_url!r}, photo_width={self.photo_width!r}, photo_height={self.photo_height!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultphoto_instance`
        """
        return (
            key in ["type", "id", "photo_url", "thumb_url", "photo_width", "photo_height", "title", "description", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultPhoto


class InlineQueryResultGif(InlineQueryResult):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif


    Parameters:

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

    :param gif_duration: Optional. Duration of the GIF
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

    def __init__(self, id, gif_url, thumb_url, gif_width=None, gif_height=None, gif_duration=None, thumb_mime_type=None, title=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultgif


        Parameters:

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

        :param gif_duration: Optional. Duration of the GIF
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
        super(InlineQueryResultGif, self).__init__(id, "gif")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(gif_url, unicode_type, parameter_name="gif_url")
        self.gif_url = gif_url
        assert_type_or_raise(thumb_url, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(gif_width, None, int, parameter_name="gif_width")
        self.gif_width = gif_width
        assert_type_or_raise(gif_height, None, int, parameter_name="gif_height")
        self.gif_height = gif_height
        assert_type_or_raise(gif_duration, None, int, parameter_name="gif_duration")
        self.gif_duration = gif_duration
        assert_type_or_raise(thumb_mime_type, None, unicode_type, parameter_name="thumb_mime_type")
        self.thumb_mime_type = thumb_mime_type
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultGif to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultGif, self).to_array()

        # 'type' given by superclass
        # 'id' given by superclass
        array['gif_url'] = u(self.gif_url)  # py2: type unicode, py3: type str
        array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        if self.gif_width is not None:
            array['gif_width'] = int(self.gif_width)  # type int
        # end if
        if self.gif_height is not None:
            array['gif_height'] = int(self.gif_height)  # type int
        # end if
        if self.gif_duration is not None:
            array['gif_duration'] = int(self.gif_duration)  # type int
        # end if
        if self.thumb_mime_type is not None:
            array['thumb_mime_type'] = u(self.thumb_mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultGif constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['gif_url'] = u(array.get('gif_url'))
        data['thumb_url'] = u(array.get('thumb_url'))
        data['gif_width'] = int(array.get('gif_width')) if array.get('gif_width') is not None else None
        data['gif_height'] = int(array.get('gif_height')) if array.get('gif_height') is not None else None
        data['gif_duration'] = int(array.get('gif_duration')) if array.get('gif_duration') is not None else None
        data['thumb_mime_type'] = u(array.get('thumb_mime_type')) if array.get('thumb_mime_type') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultGif from a given dictionary.

        :return: new InlineQueryResultGif instance.
        :rtype: InlineQueryResultGif
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultGif.validate_array(array)
        instance = InlineQueryResultGif(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultgif_instance)`
        """
        return "InlineQueryResultGif(type={self.type!r}, id={self.id!r}, gif_url={self.gif_url!r}, thumb_url={self.thumb_url!r}, gif_width={self.gif_width!r}, gif_height={self.gif_height!r}, gif_duration={self.gif_duration!r}, thumb_mime_type={self.thumb_mime_type!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultgif_instance)`
        """
        if self._raw:
            return "InlineQueryResultGif.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultGif(type={self.type!r}, id={self.id!r}, gif_url={self.gif_url!r}, thumb_url={self.thumb_url!r}, gif_width={self.gif_width!r}, gif_height={self.gif_height!r}, gif_duration={self.gif_duration!r}, thumb_mime_type={self.thumb_mime_type!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultgif_instance`
        """
        return (
            key in ["type", "id", "gif_url", "thumb_url", "gif_width", "gif_height", "gif_duration", "thumb_mime_type", "title", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    :param mpeg4_duration: Optional. Video duration
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

    def __init__(self, id, mpeg4_url, thumb_url, mpeg4_width=None, mpeg4_height=None, mpeg4_duration=None, thumb_mime_type=None, title=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif


        Parameters:

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

        :param mpeg4_duration: Optional. Video duration
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
        super(InlineQueryResultMpeg4Gif, self).__init__(id, "mpeg4_gif")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(mpeg4_url, unicode_type, parameter_name="mpeg4_url")
        self.mpeg4_url = mpeg4_url
        assert_type_or_raise(thumb_url, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(mpeg4_width, None, int, parameter_name="mpeg4_width")
        self.mpeg4_width = mpeg4_width
        assert_type_or_raise(mpeg4_height, None, int, parameter_name="mpeg4_height")
        self.mpeg4_height = mpeg4_height
        assert_type_or_raise(mpeg4_duration, None, int, parameter_name="mpeg4_duration")
        self.mpeg4_duration = mpeg4_duration
        assert_type_or_raise(thumb_mime_type, None, unicode_type, parameter_name="thumb_mime_type")
        self.thumb_mime_type = thumb_mime_type
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultMpeg4Gif to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultMpeg4Gif, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['mpeg4_url'] = u(self.mpeg4_url)  # py2: type unicode, py3: type str
        array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        if self.mpeg4_width is not None:
            array['mpeg4_width'] = int(self.mpeg4_width)  # type int
        # end if
        if self.mpeg4_height is not None:
            array['mpeg4_height'] = int(self.mpeg4_height)  # type int
        # end if
        if self.mpeg4_duration is not None:
            array['mpeg4_duration'] = int(self.mpeg4_duration)  # type int
        # end if
        if self.thumb_mime_type is not None:
            array['thumb_mime_type'] = u(self.thumb_mime_type)  # py2: type unicode, py3: type str
        # end if
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultMpeg4Gif constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['mpeg4_url'] = u(array.get('mpeg4_url'))
        data['thumb_url'] = u(array.get('thumb_url'))
        data['mpeg4_width'] = int(array.get('mpeg4_width')) if array.get('mpeg4_width') is not None else None
        data['mpeg4_height'] = int(array.get('mpeg4_height')) if array.get('mpeg4_height') is not None else None
        data['mpeg4_duration'] = int(array.get('mpeg4_duration')) if array.get('mpeg4_duration') is not None else None
        data['thumb_mime_type'] = u(array.get('thumb_mime_type')) if array.get('thumb_mime_type') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultMpeg4Gif from a given dictionary.

        :return: new InlineQueryResultMpeg4Gif instance.
        :rtype: InlineQueryResultMpeg4Gif
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultMpeg4Gif.validate_array(array)
        instance = InlineQueryResultMpeg4Gif(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultmpeg4gif_instance)`
        """
        return "InlineQueryResultMpeg4Gif(type={self.type!r}, id={self.id!r}, mpeg4_url={self.mpeg4_url!r}, thumb_url={self.thumb_url!r}, mpeg4_width={self.mpeg4_width!r}, mpeg4_height={self.mpeg4_height!r}, mpeg4_duration={self.mpeg4_duration!r}, thumb_mime_type={self.thumb_mime_type!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultmpeg4gif_instance)`
        """
        if self._raw:
            return "InlineQueryResultMpeg4Gif.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultMpeg4Gif(type={self.type!r}, id={self.id!r}, mpeg4_url={self.mpeg4_url!r}, thumb_url={self.thumb_url!r}, mpeg4_width={self.mpeg4_width!r}, mpeg4_height={self.mpeg4_height!r}, mpeg4_duration={self.mpeg4_duration!r}, thumb_mime_type={self.thumb_mime_type!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultmpeg4gif_instance`
        """
        return (
            key in ["type", "id", "mpeg4_url", "thumb_url", "mpeg4_width", "mpeg4_height", "mpeg4_duration", "thumb_mime_type", "title", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultMpeg4Gif


class InlineQueryResultVideo(InlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.

    https://core.telegram.org/bots/api#inlinequeryresultvideo


    Parameters:

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param video_url: A valid URL for the embedded video player or video file
    :type  video_url: str|unicode

    :param mime_type: Mime type of the content of video url, "text/html" or "video/mp4"
    :type  mime_type: str|unicode

    :param thumb_url: URL of the thumbnail (jpeg only) for the video
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

    def __init__(self, id, video_url, mime_type, thumb_url, title, caption=None, parse_mode=None, caption_entities=None, video_width=None, video_height=None, video_duration=None, description=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you must replace its content using input_message_content.

        https://core.telegram.org/bots/api#inlinequeryresultvideo


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str|unicode

        :param video_url: A valid URL for the embedded video player or video file
        :type  video_url: str|unicode

        :param mime_type: Mime type of the content of video url, "text/html" or "video/mp4"
        :type  mime_type: str|unicode

        :param thumb_url: URL of the thumbnail (jpeg only) for the video
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
        super(InlineQueryResultVideo, self).__init__(id, "video")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # type is given by class type
        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(video_url, unicode_type, parameter_name="video_url")
        self.video_url = video_url
        assert_type_or_raise(mime_type, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(thumb_url, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(video_width, None, int, parameter_name="video_width")
        self.video_width = video_width
        assert_type_or_raise(video_height, None, int, parameter_name="video_height")
        self.video_height = video_height
        assert_type_or_raise(video_duration, None, int, parameter_name="video_duration")
        self.video_duration = video_duration
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultVideo to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultVideo, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['video_url'] = u(self.video_url)  # py2: type unicode, py3: type str
        array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.video_width is not None:
            array['video_width'] = int(self.video_width)  # type int
        # end if
        if self.video_height is not None:
            array['video_height'] = int(self.video_height)  # type int
        # end if
        if self.video_duration is not None:
            array['video_duration'] = int(self.video_duration)  # type int
        # end if
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultVideo constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['video_url'] = u(array.get('video_url'))
        data['mime_type'] = u(array.get('mime_type'))
        data['thumb_url'] = u(array.get('thumb_url'))
        data['title'] = u(array.get('title'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['video_width'] = int(array.get('video_width')) if array.get('video_width') is not None else None
        data['video_height'] = int(array.get('video_height')) if array.get('video_height') is not None else None
        data['video_duration'] = int(array.get('video_duration')) if array.get('video_duration') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultVideo from a given dictionary.

        :return: new InlineQueryResultVideo instance.
        :rtype: InlineQueryResultVideo
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultVideo.validate_array(array)
        instance = InlineQueryResultVideo(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultvideo_instance)`
        """
        return "InlineQueryResultVideo(type={self.type!r}, id={self.id!r}, video_url={self.video_url!r}, mime_type={self.mime_type!r}, thumb_url={self.thumb_url!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, video_width={self.video_width!r}, video_height={self.video_height!r}, video_duration={self.video_duration!r}, description={self.description!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultvideo_instance)`
        """
        if self._raw:
            return "InlineQueryResultVideo.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultVideo(type={self.type!r}, id={self.id!r}, video_url={self.video_url!r}, mime_type={self.mime_type!r}, thumb_url={self.thumb_url!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, video_width={self.video_width!r}, video_height={self.video_height!r}, video_duration={self.video_duration!r}, description={self.description!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultvideo_instance`
        """
        return (
            key in ["type", "id", "video_url", "mime_type", "thumb_url", "title", "caption", "parse_mode", "caption_entities", "video_width", "video_height", "video_duration", "description", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultVideo


class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio


    Parameters:

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

    def __init__(self, id, audio_url, title, caption=None, parse_mode=None, caption_entities=None, performer=None, audio_duration=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultaudio


        Parameters:

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
        super(InlineQueryResultAudio, self).__init__(id, "audio")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # type is given by class type
        # id is given by class type
        assert_type_or_raise(audio_url, unicode_type, parameter_name="audio_url")
        self.audio_url = audio_url
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(performer, None, unicode_type, parameter_name="performer")
        self.performer = performer
        assert_type_or_raise(audio_duration, None, int, parameter_name="audio_duration")
        self.audio_duration = audio_duration
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultAudio to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultAudio, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['audio_url'] = u(self.audio_url)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.performer is not None:
            array['performer'] = u(self.performer)  # py2: type unicode, py3: type str
        # end if
        if self.audio_duration is not None:
            array['audio_duration'] = int(self.audio_duration)  # type int
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultAudio constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['audio_url'] = u(array.get('audio_url'))
        data['title'] = u(array.get('title'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['performer'] = u(array.get('performer')) if array.get('performer') is not None else None
        data['audio_duration'] = int(array.get('audio_duration')) if array.get('audio_duration') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultAudio from a given dictionary.

        :return: new InlineQueryResultAudio instance.
        :rtype: InlineQueryResultAudio
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultAudio.validate_array(array)
        instance = InlineQueryResultAudio(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultaudio_instance)`
        """
        return "InlineQueryResultAudio(type={self.type!r}, id={self.id!r}, audio_url={self.audio_url!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, performer={self.performer!r}, audio_duration={self.audio_duration!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultaudio_instance)`
        """
        if self._raw:
            return "InlineQueryResultAudio.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultAudio(type={self.type!r}, id={self.id!r}, audio_url={self.audio_url!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, performer={self.performer!r}, audio_duration={self.audio_duration!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultaudio_instance`
        """
        return (
            key in ["type", "id", "audio_url", "title", "caption", "parse_mode", "caption_entities", "performer", "audio_duration", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultAudio


class InlineQueryResultVoice(InlineQueryResult):
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice


    Parameters:

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

    def __init__(self, id, voice_url, title, caption=None, parse_mode=None, caption_entities=None, voice_duration=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvoice


        Parameters:

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
        super(InlineQueryResultVoice, self).__init__(id, "voice")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(voice_url, unicode_type, parameter_name="voice_url")
        self.voice_url = voice_url
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(voice_duration, None, int, parameter_name="voice_duration")
        self.voice_duration = voice_duration
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultVoice to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultVoice, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['voice_url'] = u(self.voice_url)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.voice_duration is not None:
            array['voice_duration'] = int(self.voice_duration)  # type int
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultVoice constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['voice_url'] = u(array.get('voice_url'))
        data['title'] = u(array.get('title'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['voice_duration'] = int(array.get('voice_duration')) if array.get('voice_duration') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultVoice from a given dictionary.

        :return: new InlineQueryResultVoice instance.
        :rtype: InlineQueryResultVoice
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultVoice.validate_array(array)
        instance = InlineQueryResultVoice(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultvoice_instance)`
        """
        return "InlineQueryResultVoice(type={self.type!r}, id={self.id!r}, voice_url={self.voice_url!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, voice_duration={self.voice_duration!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultvoice_instance)`
        """
        if self._raw:
            return "InlineQueryResultVoice.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultVoice(type={self.type!r}, id={self.id!r}, voice_url={self.voice_url!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, voice_duration={self.voice_duration!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultvoice_instance`
        """
        return (
            key in ["type", "id", "voice_url", "title", "caption", "parse_mode", "caption_entities", "voice_duration", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultVoice


class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultdocument


    Parameters:

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

    :param thumb_url: Optional. URL of the thumbnail (jpeg only) for the file
    :type  thumb_url: str|unicode

    :param thumb_width: Optional. Thumbnail width
    :type  thumb_width: int

    :param thumb_height: Optional. Thumbnail height
    :type  thumb_height: int
    """

    def __init__(self, id, title, document_url, mime_type, caption=None, parse_mode=None, caption_entities=None, description=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultdocument


        Parameters:

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

        :param thumb_url: Optional. URL of the thumbnail (jpeg only) for the file
        :type  thumb_url: str|unicode

        :param thumb_width: Optional. Thumbnail width
        :type  thumb_width: int

        :param thumb_height: Optional. Thumbnail height
        :type  thumb_height: int
        """
        super(InlineQueryResultDocument, self).__init__(id, "document")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(document_url, unicode_type, parameter_name="document_url")
        self.document_url = document_url
        assert_type_or_raise(mime_type, unicode_type, parameter_name="mime_type")
        self.mime_type = mime_type
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
        assert_type_or_raise(thumb_url, None, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(thumb_width, None, int, parameter_name="thumb_width")
        self.thumb_width = thumb_width
        assert_type_or_raise(thumb_height, None, int, parameter_name="thumb_height")
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultDocument to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultDocument, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['document_url'] = u(self.document_url)  # py2: type unicode, py3: type str
        array['mime_type'] = u(self.mime_type)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if
        if self.thumb_url is not None:
            array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        # end if
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        # end if
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultDocument constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['title'] = u(array.get('title'))
        data['document_url'] = u(array.get('document_url'))
        data['mime_type'] = u(array.get('mime_type'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = u(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultDocument from a given dictionary.

        :return: new InlineQueryResultDocument instance.
        :rtype: InlineQueryResultDocument
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultDocument.validate_array(array)
        instance = InlineQueryResultDocument(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultdocument_instance)`
        """
        return "InlineQueryResultDocument(type={self.type!r}, id={self.id!r}, title={self.title!r}, document_url={self.document_url!r}, mime_type={self.mime_type!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, description={self.description!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultdocument_instance)`
        """
        if self._raw:
            return "InlineQueryResultDocument.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultDocument(type={self.type!r}, id={self.id!r}, title={self.title!r}, document_url={self.document_url!r}, mime_type={self.mime_type!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, description={self.description!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultdocument_instance`
        """
        return (
            key in ["type", "id", "title", "document_url", "mime_type", "caption", "parse_mode", "caption_entities", "description", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultDocument


class InlineQueryResultLocation(InlineQueryResult):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation


    Parameters:

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

    def __init__(self, id, latitude, longitude, title, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultlocation


        Parameters:

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
        super(InlineQueryResultLocation, self).__init__(id, "location")
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(horizontal_accuracy, None, float, parameter_name="horizontal_accuracy")
        self.horizontal_accuracy = horizontal_accuracy
        assert_type_or_raise(live_period, None, int, parameter_name="live_period")
        self.live_period = live_period
        assert_type_or_raise(heading, None, int, parameter_name="heading")
        self.heading = heading
        assert_type_or_raise(proximity_alert_radius, None, int, parameter_name="proximity_alert_radius")
        self.proximity_alert_radius = proximity_alert_radius
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
        assert_type_or_raise(thumb_url, None, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(thumb_width, None, int, parameter_name="thumb_width")
        self.thumb_width = thumb_width
        assert_type_or_raise(thumb_height, None, int, parameter_name="thumb_height")
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultLocation to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultLocation, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
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
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if
        if self.thumb_url is not None:
            array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        # end if
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        # end if
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultLocation constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['title'] = u(array.get('title'))
        data['horizontal_accuracy'] = float(array.get('horizontal_accuracy')) if array.get('horizontal_accuracy') is not None else None
        data['live_period'] = int(array.get('live_period')) if array.get('live_period') is not None else None
        data['heading'] = int(array.get('heading')) if array.get('heading') is not None else None
        data['proximity_alert_radius'] = int(array.get('proximity_alert_radius')) if array.get('proximity_alert_radius') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = u(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultLocation from a given dictionary.

        :return: new InlineQueryResultLocation instance.
        :rtype: InlineQueryResultLocation
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultLocation.validate_array(array)
        instance = InlineQueryResultLocation(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultlocation_instance)`
        """
        return "InlineQueryResultLocation(type={self.type!r}, id={self.id!r}, latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, horizontal_accuracy={self.horizontal_accuracy!r}, live_period={self.live_period!r}, heading={self.heading!r}, proximity_alert_radius={self.proximity_alert_radius!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultlocation_instance)`
        """
        if self._raw:
            return "InlineQueryResultLocation.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultLocation(type={self.type!r}, id={self.id!r}, latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, horizontal_accuracy={self.horizontal_accuracy!r}, live_period={self.live_period!r}, heading={self.heading!r}, proximity_alert_radius={self.proximity_alert_radius!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultlocation_instance`
        """
        return (
            key in ["type", "id", "latitude", "longitude", "title", "horizontal_accuracy", "live_period", "heading", "proximity_alert_radius", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultLocation


class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue


    Parameters:

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

    def __init__(self, id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvenue


        Parameters:

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
        super(InlineQueryResultVenue, self).__init__(id, "venue")
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
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
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
        assert_type_or_raise(thumb_url, None, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(thumb_width, None, int, parameter_name="thumb_width")
        self.thumb_width = thumb_width
        assert_type_or_raise(thumb_height, None, int, parameter_name="thumb_height")
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultVenue to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultVenue, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
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
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if
        if self.thumb_url is not None:
            array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        # end if
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        # end if
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultVenue constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['title'] = u(array.get('title'))
        data['address'] = u(array.get('address'))
        data['foursquare_id'] = u(array.get('foursquare_id')) if array.get('foursquare_id') is not None else None
        data['foursquare_type'] = u(array.get('foursquare_type')) if array.get('foursquare_type') is not None else None
        data['google_place_id'] = u(array.get('google_place_id')) if array.get('google_place_id') is not None else None
        data['google_place_type'] = u(array.get('google_place_type')) if array.get('google_place_type') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = u(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultVenue from a given dictionary.

        :return: new InlineQueryResultVenue instance.
        :rtype: InlineQueryResultVenue
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultVenue.validate_array(array)
        instance = InlineQueryResultVenue(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultvenue_instance)`
        """
        return "InlineQueryResultVenue(type={self.type!r}, id={self.id!r}, latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, google_place_id={self.google_place_id!r}, google_place_type={self.google_place_type!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultvenue_instance)`
        """
        if self._raw:
            return "InlineQueryResultVenue.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultVenue(type={self.type!r}, id={self.id!r}, latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, google_place_id={self.google_place_id!r}, google_place_type={self.google_place_type!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultvenue_instance`
        """
        return (
            key in ["type", "id", "latitude", "longitude", "title", "address", "foursquare_id", "foursquare_type", "google_place_id", "google_place_type", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultVenue


class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact


    Parameters:

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

    def __init__(self, id, phone_number, first_name, last_name=None, vcard=None, reply_markup=None, input_message_content=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcontact


        Parameters:

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
        super(InlineQueryResultContact, self).__init__(id, "contact")
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(phone_number, unicode_type, parameter_name="phone_number")
        self.phone_number = phone_number
        assert_type_or_raise(first_name, unicode_type, parameter_name="first_name")
        self.first_name = first_name
        assert_type_or_raise(last_name, None, unicode_type, parameter_name="last_name")
        self.last_name = last_name
        assert_type_or_raise(vcard, None, unicode_type, parameter_name="vcard")
        self.vcard = vcard
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
        assert_type_or_raise(thumb_url, None, unicode_type, parameter_name="thumb_url")
        self.thumb_url = thumb_url
        assert_type_or_raise(thumb_width, None, int, parameter_name="thumb_width")
        self.thumb_width = thumb_width
        assert_type_or_raise(thumb_height, None, int, parameter_name="thumb_height")
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultContact to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultContact, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['phone_number'] = u(self.phone_number)  # py2: type unicode, py3: type str
        array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        # end if
        if self.vcard is not None:
            array['vcard'] = u(self.vcard)  # py2: type unicode, py3: type str
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if
        if self.thumb_url is not None:
            array['thumb_url'] = u(self.thumb_url)  # py2: type unicode, py3: type str
        # end if
        if self.thumb_width is not None:
            array['thumb_width'] = int(self.thumb_width)  # type int
        # end if
        if self.thumb_height is not None:
            array['thumb_height'] = int(self.thumb_height)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultContact constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is set by class type
        # 'id' is set by class type
        data['id'] = u(array.get('id'))
        data['phone_number'] = u(array.get('phone_number'))
        data['first_name'] = u(array.get('first_name'))
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['vcard'] = u(array.get('vcard')) if array.get('vcard') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        data['thumb_url'] = u(array.get('thumb_url')) if array.get('thumb_url') is not None else None
        data['thumb_width'] = int(array.get('thumb_width')) if array.get('thumb_width') is not None else None
        data['thumb_height'] = int(array.get('thumb_height')) if array.get('thumb_height') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultContact from a given dictionary.

        :return: new InlineQueryResultContact instance.
        :rtype: InlineQueryResultContact
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultContact.validate_array(array)
        instance = InlineQueryResultContact(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcontact_instance)`
        """
        return "InlineQueryResultContact(type={self.type!r}, id={self.id!r}, phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, vcard={self.vcard!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcontact_instance)`
        """
        if self._raw:
            return "InlineQueryResultContact.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultContact(type={self.type!r}, id={self.id!r}, phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, vcard={self.vcard!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r}, thumb_url={self.thumb_url!r}, thumb_width={self.thumb_width!r}, thumb_height={self.thumb_height!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcontact_instance`
        """
        return (
            key in ["type", "id", "phone_number", "first_name", "last_name", "vcard", "reply_markup", "input_message_content", "thumb_url", "thumb_width", "thumb_height"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultContact


class InlineQueryResultGame(InlineQueryResult):
    """
    Represents a Game.
    Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

    https://core.telegram.org/bots/api#inlinequeryresultgame


    Parameters:

    :param id: Unique identifier for this result, 1-64 bytes
    :type  id: str|unicode

    :param game_short_name: Short name of the game
    :type  game_short_name: str|unicode


    Optional keyword parameters:

    :param reply_markup: Optional. Inline keyboard attached to the message
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
    """

    def __init__(self, id, game_short_name, reply_markup=None):
        """
        Represents a Game.
        Note: This will only work in Telegram versions released after October 1, 2016. Older clients will not display any inline results if a game result is among them.

        https://core.telegram.org/bots/api#inlinequeryresultgame


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id: str|unicode

        :param game_short_name: Short name of the game
        :type  game_short_name: str|unicode


        Optional keyword parameters:

        :param reply_markup: Optional. Inline keyboard attached to the message
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
        """
        super(InlineQueryResultGame, self).__init__(id, "game")
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(game_short_name, unicode_type, parameter_name="game_short_name")
        self.game_short_name = game_short_name
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultGame to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultGame, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['game_short_name'] = u(self.game_short_name)  # py2: type unicode, py3: type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultGame constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['game_short_name'] = u(array.get('game_short_name'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultGame from a given dictionary.

        :return: new InlineQueryResultGame instance.
        :rtype: InlineQueryResultGame
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultGame.validate_array(array)
        instance = InlineQueryResultGame(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultgame_instance)`
        """
        return "InlineQueryResultGame(type={self.type!r}, id={self.id!r}, game_short_name={self.game_short_name!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultgame_instance)`
        """
        if self._raw:
            return "InlineQueryResultGame.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultGame(type={self.type!r}, id={self.id!r}, game_short_name={self.game_short_name!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultgame_instance`
        """
        return (
            key in ["type", "id", "game_short_name", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultGame


class InlineQueryResultCachedPhoto(InlineQueryCachedResult):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto


    Parameters:

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

    def __init__(self, id, photo_file_id, title=None, description=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultcachedphoto


        Parameters:

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
        super(InlineQueryResultCachedPhoto, self).__init__(id, "photo")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(photo_file_id, unicode_type, parameter_name="photo_file_id")
        self.photo_file_id = photo_file_id
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedPhoto to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedPhoto, self).to_array()

        # 'type' given by superclass
        # 'id' given by superclass
        array['photo_file_id'] = u(self.photo_file_id)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedPhoto constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['photo_file_id'] = u(array.get('photo_file_id'))
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedPhoto from a given dictionary.

        :return: new InlineQueryResultCachedPhoto instance.
        :rtype: InlineQueryResultCachedPhoto
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedPhoto.validate_array(array)
        instance = InlineQueryResultCachedPhoto(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedphoto_instance)`
        """
        return "InlineQueryResultCachedPhoto(type={self.type!r}, id={self.id!r}, photo_file_id={self.photo_file_id!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedphoto_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedPhoto.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedPhoto(type={self.type!r}, id={self.id!r}, photo_file_id={self.photo_file_id!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedphoto_instance`
        """
        return (
            key in ["type", "id", "photo_file_id", "title", "description", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedPhoto


class InlineQueryResultCachedGif(InlineQueryCachedResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif


    Parameters:

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

    def __init__(self, id, gif_file_id, title=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedgif


        Parameters:

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
        super(InlineQueryResultCachedGif, self).__init__(id, "gif")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(gif_file_id, unicode_type, parameter_name="gif_file_id")
        self.gif_file_id = gif_file_id
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedGif to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedGif, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['gif_file_id'] = u(self.gif_file_id)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedGif constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['gif_file_id'] = u(array.get('gif_file_id'))
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedGif from a given dictionary.

        :return: new InlineQueryResultCachedGif instance.
        :rtype: InlineQueryResultCachedGif
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedGif.validate_array(array)
        instance = InlineQueryResultCachedGif(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedgif_instance)`
        """
        return "InlineQueryResultCachedGif(type={self.type!r}, id={self.id!r}, gif_file_id={self.gif_file_id!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedgif_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedGif.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedGif(type={self.type!r}, id={self.id!r}, gif_file_id={self.gif_file_id!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedgif_instance`
        """
        return (
            key in ["type", "id", "gif_file_id", "title", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedGif


class InlineQueryResultCachedMpeg4Gif(InlineQueryCachedResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif


    Parameters:

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

    def __init__(self, id, mpeg4_file_id, title=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif


        Parameters:

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
        super(InlineQueryResultCachedMpeg4Gif, self).__init__(id, "mpeg4_gif")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(mpeg4_file_id, unicode_type, parameter_name="mpeg4_file_id")
        self.mpeg4_file_id = mpeg4_file_id
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedMpeg4Gif to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedMpeg4Gif, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['mpeg4_file_id'] = u(self.mpeg4_file_id)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedMpeg4Gif constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['mpeg4_file_id'] = u(array.get('mpeg4_file_id'))
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedMpeg4Gif from a given dictionary.

        :return: new InlineQueryResultCachedMpeg4Gif instance.
        :rtype: InlineQueryResultCachedMpeg4Gif
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedMpeg4Gif.validate_array(array)
        instance = InlineQueryResultCachedMpeg4Gif(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedmpeg4gif_instance)`
        """
        return "InlineQueryResultCachedMpeg4Gif(type={self.type!r}, id={self.id!r}, mpeg4_file_id={self.mpeg4_file_id!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedmpeg4gif_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedMpeg4Gif.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedMpeg4Gif(type={self.type!r}, id={self.id!r}, mpeg4_file_id={self.mpeg4_file_id!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedmpeg4gif_instance`
        """
        return (
            key in ["type", "id", "mpeg4_file_id", "title", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedMpeg4Gif


class InlineQueryResultCachedSticker(InlineQueryCachedResult):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker


    Parameters:

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

    def __init__(self, id, sticker_file_id, reply_markup=None, input_message_content=None):
        """
        Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
        Note: This will only work in Telegram versions released after 9 April, 2016 for static stickers and after 06 July, 2019 for animated stickers. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedsticker


        Parameters:

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
        super(InlineQueryResultCachedSticker, self).__init__(id, "sticker")
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(sticker_file_id, unicode_type, parameter_name="sticker_file_id")
        self.sticker_file_id = sticker_file_id
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedSticker to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedSticker, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['sticker_file_id'] = u(self.sticker_file_id)  # py2: type unicode, py3: type str
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedSticker constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['sticker_file_id'] = u(array.get('sticker_file_id'))
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedSticker from a given dictionary.

        :return: new InlineQueryResultCachedSticker instance.
        :rtype: InlineQueryResultCachedSticker
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedSticker.validate_array(array)
        instance = InlineQueryResultCachedSticker(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedsticker_instance)`
        """
        return "InlineQueryResultCachedSticker(type={self.type!r}, id={self.id!r}, sticker_file_id={self.sticker_file_id!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedsticker_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedSticker.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedSticker(type={self.type!r}, id={self.id!r}, sticker_file_id={self.sticker_file_id!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedsticker_instance`
        """
        return (
            key in ["type", "id", "sticker_file_id", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedSticker


class InlineQueryResultCachedDocument(InlineQueryCachedResult):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument


    Parameters:

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

    def __init__(self, id, title, document_file_id, description=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcacheddocument


        Parameters:

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
        super(InlineQueryResultCachedDocument, self).__init__(id, "document")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(document_file_id, unicode_type, parameter_name="document_file_id")
        self.document_file_id = document_file_id
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedDocument to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedDocument, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['document_file_id'] = u(self.document_file_id)  # py2: type unicode, py3: type str
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedDocument constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['title'] = u(array.get('title'))
        data['document_file_id'] = u(array.get('document_file_id'))
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedDocument from a given dictionary.

        :return: new InlineQueryResultCachedDocument instance.
        :rtype: InlineQueryResultCachedDocument
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedDocument.validate_array(array)
        instance = InlineQueryResultCachedDocument(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcacheddocument_instance)`
        """
        return "InlineQueryResultCachedDocument(type={self.type!r}, id={self.id!r}, title={self.title!r}, document_file_id={self.document_file_id!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcacheddocument_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedDocument.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedDocument(type={self.type!r}, id={self.id!r}, title={self.title!r}, document_file_id={self.document_file_id!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcacheddocument_instance`
        """
        return (
            key in ["type", "id", "title", "document_file_id", "description", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedDocument


class InlineQueryResultCachedVideo(InlineQueryCachedResult):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo


    Parameters:

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

    def __init__(self, id, video_file_id, title, description=None, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvideo


        Parameters:

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
        super(InlineQueryResultCachedVideo, self).__init__(id, "video")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(video_file_id, unicode_type, parameter_name="video_file_id")
        self.video_file_id = video_file_id
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(description, None, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedVideo to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedVideo, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['video_file_id'] = u(self.video_file_id)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.description is not None:
            array['description'] = u(self.description)  # py2: type unicode, py3: type str
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedVideo constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['video_file_id'] = u(array.get('video_file_id'))
        data['title'] = u(array.get('title'))
        data['description'] = u(array.get('description')) if array.get('description') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedVideo from a given dictionary.

        :return: new InlineQueryResultCachedVideo instance.
        :rtype: InlineQueryResultCachedVideo
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedVideo.validate_array(array)
        instance = InlineQueryResultCachedVideo(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedvideo_instance)`
        """
        return "InlineQueryResultCachedVideo(type={self.type!r}, id={self.id!r}, video_file_id={self.video_file_id!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedvideo_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedVideo.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedVideo(type={self.type!r}, id={self.id!r}, video_file_id={self.video_file_id!r}, title={self.title!r}, description={self.description!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedvideo_instance`
        """
        return (
            key in ["type", "id", "video_file_id", "title", "description", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedVideo


class InlineQueryResultCachedVoice(InlineQueryCachedResult):
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice


    Parameters:

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

    def __init__(self, id, voice_file_id, title, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvoice


        Parameters:

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
        super(InlineQueryResultCachedVoice, self).__init__(id, "voice")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(voice_file_id, unicode_type, parameter_name="voice_file_id")
        self.voice_file_id = voice_file_id
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedVoice to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedVoice, self).to_array()
        # 'type' given by superclass
        # 'id' given by superclass
        array['voice_file_id'] = u(self.voice_file_id)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedVoice constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['voice_file_id'] = u(array.get('voice_file_id'))
        data['title'] = u(array.get('title'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedVoice from a given dictionary.

        :return: new InlineQueryResultCachedVoice instance.
        :rtype: InlineQueryResultCachedVoice
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedVoice.validate_array(array)
        instance = InlineQueryResultCachedVoice(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedvoice_instance)`
        """
        return "InlineQueryResultCachedVoice(type={self.type!r}, id={self.id!r}, voice_file_id={self.voice_file_id!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedvoice_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedVoice.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedVoice(type={self.type!r}, id={self.id!r}, voice_file_id={self.voice_file_id!r}, title={self.title!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedvoice_instance`
        """
        return (
            key in ["type", "id", "voice_file_id", "title", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineQueryResultCachedVoice


class InlineQueryResultCachedAudio(InlineQueryCachedResult):
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio


    Parameters:

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

    def __init__(self, id, audio_file_id, caption=None, parse_mode=None, caption_entities=None, reply_markup=None, input_message_content=None):
        """
        Represents a link to an MP3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedaudio


        Parameters:

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
        super(InlineQueryResultCachedAudio, self).__init__(id, "audio")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        # 'type' is given by class type
        # 'id' is given by class type
        assert_type_or_raise(audio_file_id, unicode_type, parameter_name="audio_file_id")
        self.audio_file_id = audio_file_id
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        assert_type_or_raise(input_message_content, None, InputMessageContent, parameter_name="input_message_content")
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineQueryResultCachedAudio to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineQueryResultCachedAudio, self).to_array()

        # 'type' given by superclass
        # 'id' given by superclass
        array['audio_file_id'] = u(self.audio_file_id)  # py2: type unicode, py3: type str
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if
        if self.input_message_content is not None:
            array['input_message_content'] = self.input_message_content.to_array()  # type InputMessageContent
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineQueryResultCachedAudio constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity
        from .reply_markup import InlineKeyboardMarkup

        data = InlineQueryCachedResult.validate_array(array)
        # 'type' is given by class type
        # 'id' is given by class type
        data['audio_file_id'] = u(array.get('audio_file_id'))
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        data['input_message_content'] = InputMessageContent.from_array(array.get('input_message_content')) if array.get('input_message_content') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineQueryResultCachedAudio from a given dictionary.

        :return: new InlineQueryResultCachedAudio instance.
        :rtype: InlineQueryResultCachedAudio
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineQueryResultCachedAudio.validate_array(array)
        instance = InlineQueryResultCachedAudio(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinequeryresultcachedaudio_instance)`
        """
        return "InlineQueryResultCachedAudio(type={self.type!r}, id={self.id!r}, audio_file_id={self.audio_file_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinequeryresultcachedaudio_instance)`
        """
        if self._raw:
            return "InlineQueryResultCachedAudio.from_array({self._raw})".format(self=self)
        # end if
        return "InlineQueryResultCachedAudio(type={self.type!r}, id={self.id!r}, audio_file_id={self.audio_file_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, caption_entities={self.caption_entities!r}, reply_markup={self.reply_markup!r}, input_message_content={self.input_message_content!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinequeryresultcachedaudio_instance`
        """
        return (
            key in ["type", "id", "audio_file_id", "caption", "parse_mode", "caption_entities", "reply_markup", "input_message_content"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, message_text, parse_mode=None, entities=None, disable_web_page_preview=False):
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
        super(InputTextMessageContent, self).__init__()
        from ..receivable.media import MessageEntity

        assert_type_or_raise(message_text, unicode_type, parameter_name="message_text")
        self.message_text = message_text
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        assert_type_or_raise(entities, None, list, parameter_name="entities")
        self.entities = entities
        assert_type_or_raise(disable_web_page_preview, None, bool, parameter_name="disable_web_page_preview")
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputTextMessageContent to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputTextMessageContent, self).to_array()

        array['message_text'] = u(self.message_text)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        # end if
        if self.entities is not None:
            array['entities'] = self._as_array(self.entities)  # type list of MessageEntity
        # end if
        if self.disable_web_page_preview is not None:
            array['disable_web_page_preview'] = bool(self.disable_web_page_preview)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputTextMessageContent constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.media import MessageEntity

        data = InputMessageContent.validate_array(array)
        data['message_text'] = u(array.get('message_text'))
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['entities'] = MessageEntity.from_array_list(array.get('entities'), list_level=1) if array.get('entities') is not None else None
        data['disable_web_page_preview'] = bool(array.get('disable_web_page_preview')) if array.get('disable_web_page_preview') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputTextMessageContent from a given dictionary.

        :return: new InputTextMessageContent instance.
        :rtype: InputTextMessageContent
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputTextMessageContent.validate_array(array)
        instance = InputTextMessageContent(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputtextmessagecontent_instance)`
        """
        return "InputTextMessageContent(message_text={self.message_text!r}, parse_mode={self.parse_mode!r}, entities={self.entities!r}, disable_web_page_preview={self.disable_web_page_preview!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputtextmessagecontent_instance)`
        """
        if self._raw:
            return "InputTextMessageContent.from_array({self._raw})".format(self=self)
        # end if
        return "InputTextMessageContent(message_text={self.message_text!r}, parse_mode={self.parse_mode!r}, entities={self.entities!r}, disable_web_page_preview={self.disable_web_page_preview!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputtextmessagecontent_instance`
        """
        return (
            key in ["message_text", "parse_mode", "entities", "disable_web_page_preview"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputTextMessageContent


class InputLocationMessageContent(InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

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

    def __init__(self, latitude, longitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None):
        """
        Represents the content of a location message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

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
        super(InputLocationMessageContent, self).__init__()
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
        assert_type_or_raise(horizontal_accuracy, None, float, parameter_name="horizontal_accuracy")
        self.horizontal_accuracy = horizontal_accuracy
        assert_type_or_raise(live_period, None, int, parameter_name="live_period")
        self.live_period = live_period
        assert_type_or_raise(heading, None, int, parameter_name="heading")
        self.heading = heading
        assert_type_or_raise(proximity_alert_radius, None, int, parameter_name="proximity_alert_radius")
        self.proximity_alert_radius = proximity_alert_radius
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputLocationMessageContent to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputLocationMessageContent, self).to_array()

        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
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
        Builds a new array with valid values for the InputLocationMessageContent constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = InputMessageContent.validate_array(array)
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['horizontal_accuracy'] = float(array.get('horizontal_accuracy')) if array.get('horizontal_accuracy') is not None else None
        data['live_period'] = int(array.get('live_period')) if array.get('live_period') is not None else None
        data['heading'] = int(array.get('heading')) if array.get('heading') is not None else None
        data['proximity_alert_radius'] = int(array.get('proximity_alert_radius')) if array.get('proximity_alert_radius') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputLocationMessageContent from a given dictionary.

        :return: new InputLocationMessageContent instance.
        :rtype: InputLocationMessageContent
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputLocationMessageContent.validate_array(array)
        instance = InputLocationMessageContent(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputlocationmessagecontent_instance)`
        """
        return "InputLocationMessageContent(latitude={self.latitude!r}, longitude={self.longitude!r}, horizontal_accuracy={self.horizontal_accuracy!r}, live_period={self.live_period!r}, heading={self.heading!r}, proximity_alert_radius={self.proximity_alert_radius!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputlocationmessagecontent_instance)`
        """
        if self._raw:
            return "InputLocationMessageContent.from_array({self._raw})".format(self=self)
        # end if
        return "InputLocationMessageContent(latitude={self.latitude!r}, longitude={self.longitude!r}, horizontal_accuracy={self.horizontal_accuracy!r}, live_period={self.live_period!r}, heading={self.heading!r}, proximity_alert_radius={self.proximity_alert_radius!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputlocationmessagecontent_instance`
        """
        return (
            key in ["latitude", "longitude", "horizontal_accuracy", "live_period", "heading", "proximity_alert_radius"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputLocationMessageContent


class InputVenueMessageContent(InputMessageContent):
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

    def __init__(self, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None):
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
        super(InputVenueMessageContent, self).__init__()
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
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
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputVenueMessageContent to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputVenueMessageContent, self).to_array()

        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
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
        Builds a new array with valid values for the InputVenueMessageContent constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = InputMessageContent.validate_array(array)
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
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
        Deserialize a new InputVenueMessageContent from a given dictionary.

        :return: new InputVenueMessageContent instance.
        :rtype: InputVenueMessageContent
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputVenueMessageContent.validate_array(array)
        instance = InputVenueMessageContent(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputvenuemessagecontent_instance)`
        """
        return "InputVenueMessageContent(latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, google_place_id={self.google_place_id!r}, google_place_type={self.google_place_type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputvenuemessagecontent_instance)`
        """
        if self._raw:
            return "InputVenueMessageContent.from_array({self._raw})".format(self=self)
        # end if
        return "InputVenueMessageContent(latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, google_place_id={self.google_place_id!r}, google_place_type={self.google_place_type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputvenuemessagecontent_instance`
        """
        return (
            key in ["latitude", "longitude", "title", "address", "foursquare_id", "foursquare_type", "google_place_id", "google_place_type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputVenueMessageContent


class InputContactMessageContent(InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

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

    def __init__(self, phone_number, first_name, last_name=None, vcard=None):
        """
        Represents the content of a contact message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

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
        super(InputContactMessageContent, self).__init__()
        assert_type_or_raise(phone_number, unicode_type, parameter_name="phone_number")
        self.phone_number = phone_number
        assert_type_or_raise(first_name, unicode_type, parameter_name="first_name")
        self.first_name = first_name
        assert_type_or_raise(last_name, None, unicode_type, parameter_name="last_name")
        self.last_name = last_name
        assert_type_or_raise(vcard, None, unicode_type, parameter_name="vcard")
        self.vcard = vcard
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InputContactMessageContent to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InputContactMessageContent, self).to_array()

        array['phone_number'] = u(self.phone_number)  # py2: type unicode, py3: type str
        array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        # end if
        if self.vcard is not None:
            array['vcard'] = u(self.vcard)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InputContactMessageContent constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = InputMessageContent.validate_array(array)
        data['phone_number'] = u(array.get('phone_number'))
        data['first_name'] = u(array.get('first_name'))
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['vcard'] = u(array.get('vcard')) if array.get('vcard') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InputContactMessageContent from a given dictionary.

        :return: new InputContactMessageContent instance.
        :rtype: InputContactMessageContent
        """
        if not array:  # None or {}
            return None
        # end if

        data = InputContactMessageContent.validate_array(array)
        instance = InputContactMessageContent(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inputcontactmessagecontent_instance)`
        """
        return "InputContactMessageContent(phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, vcard={self.vcard!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inputcontactmessagecontent_instance)`
        """
        if self._raw:
            return "InputContactMessageContent.from_array({self._raw})".format(self=self)
        # end if
        return "InputContactMessageContent(phone_number={self.phone_number!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, vcard={self.vcard!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inputcontactmessagecontent_instance`
        """
        return (
            key in ["phone_number", "first_name", "last_name", "vcard"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InputContactMessageContent

