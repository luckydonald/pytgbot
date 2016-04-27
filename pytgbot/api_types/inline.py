# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pytgbot.api_types.reply_markup import InlineKeyboardMarkup
from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.inline import InputMessageContent

__author__ = 'luckydonald'

from ..encoding import text_type as unicode_type, to_unicode as u
import logging
logger = logging.getLogger(__name__)

class InlineQueryResult(Sendable):
    def __init__(self, id, type):
        assert(id is not None)
        if not isinstance(id,unicode_type):
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
    

class InlineQueryResultArticle (InlineQueryResult):
    """
    Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """
    def __init__(self, id, title, input_message_content, reply_markup=None, parse_mode=None, disable_web_page_preview=None, url=None, hide_url=None, description=None, thumb_url=None, thumb_width=None, thumb_height=None):
        """
        Represents a link to an article or web page.

        https://core.telegram.org/bots/api#inlinequeryresultarticle

        Changelog:
            `message_text`, `parse_mode` and `disable_web_page_preview` are now set in a `InputTextMessageContent`.
            This allows to use other `InputMessageContent` types as well.

            For backwards compatibility, the third argument (`message_text` renamed to `input_message_content`) still
            accepts `str`, and the optional fields `parse_mode` and `disable_web_page_preview` are kept, too.
            They are depricated and might be removed later.

        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str 

        :param title: Title of the result
        :type  title:  str 

        :param input_message_content: Content of the message to be send, a InputMessageContent subclass.
                                      For backwards compatibility, this accepts text, and `parse_mode` and
                                      `disable_web_page_preview` are both given.
        :type  input_message_content:  InputMessageContent | str


        Optional keyword parameters:
        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup: InlineKeyboardMarkup

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str 

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool 

        :keyword url: Optional. URL of the result
        :type    url:  str 

        :keyword hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
        :type    hide_url:  bool 

        :keyword description: Optional. Short description of the result
        :type    description:  str 

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str 

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int 

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int 
        """
        super(InlineQueryResultArticle, self).__init__(id, "article")
        
        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title
        
        assert(input_message_content is not None)
        assert(isinstance(input_message_content, (unicode_type, InputMessageContent)))  # unicode on python 2, str on python 3
        if isinstance(input_message_content, InputMessageContent):
            assert(parse_mode is None, "InputMessageContent given. Set parse_mode there.")
            assert(disable_web_page_preview is None, "InputMessageContent given. Set disable_web_page_preview there.")
            self.input_message_content = input_message_content
        else:
            assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
            assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
            # TODO: constructor.
            logging.warning("Nope")
            self.message_text = message_text
            self.parse_mode = parse_mode
            self.disable_web_page_preview = disable_web_page_preview
        # end if

        assert(reply_markup is None or isinstance(reply_markup, ))
        self.reply_markup = reply_markup


        assert(url is None or isinstance(url, unicode_type))  # unicode on python 2, str on python 3
        self.url = url
        
        assert(hide_url is None or isinstance(hide_url, bool))
        self.hide_url = hide_url
        
        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description
        
        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url
        
        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width
        
        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultArticle, self).to_array()
        # array["id"] = self.id
        array["title"] = self.title
        array["input_message_content"] = self.input_message_content
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.url is not None:
            array["url"] = self.url
        if self.hide_url is not None:
            array["hide_url"] = self.hide_url
        if self.description is not None:
            array["description"] = self.description
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array     
    # end def to_array
# end class InlineQueryResultArticle


class InlineQueryResultPhoto (InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can provide message_text to send it instead of photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto
    """
    def __init__(self, id, photo_url, thumb_url, photo_width = None, photo_height = None, title = None, description = None, caption = None, message_text = None, parse_mode = None, disable_web_page_preview = None):
        """
        Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can provide message_text to send it instead of photo.

        https://core.telegram.org/bots/api#inlinequeryresultphoto

        Changelog:
            Instead of `message_text`, `parse_mode` and `disable_web_page_preview` use `input_message_content`


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str 

        :param photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
        :type  photo_url:  str 

        :param thumb_url: URL of the thumbnail for the photo
        :type  thumb_url:  str 


        Optional keyword parameters:

        :keyword photo_width: Optional. Width of the photo
        :type    photo_width:  int 

        :keyword photo_height: Optional. Height of the photo
        :type    photo_height:  int 

        :keyword title: Optional. Title for the result
        :type    title:  str 

        :keyword description: Optional. Short description of the result
        :type    description:  str 

        :keyword caption: Optional. Caption of the photo to be sent, 0-200 characters
        :type    caption:  str 

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the photo
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultPhoto, self).__init__(id, "photo")
        
        assert(photo_url is not None)
        assert(isinstance(photo_url, unicode_type))  # unicode on python 2, str on python 3
        self.photo_url = photo_url
        
        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(photo_width is None or isinstance(photo_width, int))
        self.photo_width = photo_width
        
        assert(photo_height is None or isinstance(photo_height, int))
        self.photo_height = photo_height
        
        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url
        
        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title
        
        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description
        
        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption
        
        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))  # unicode on python 2, str on python 3
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))  # unicode on python 2, str on python 3
        self.input_message_content = input_message_content
        
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultPhoto, self).to_array()
        array["id"] = self.id
        array["photo_url"] = self.photo_url
        array["thumb_url"] = self.thumb_url
        if self.photo_width is not None:
            array["photo_width"] = self.photo_width
        if self.photo_height is not None:
            array["photo_height"] = self.photo_height
        if self.title is not None:
            array["title"] = self.title
        if self.description is not None:
            array["description"] = self.description
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array     
    # end def to_array
# end class InlineQueryResultPhoto


class InlineQueryResultGif (InlineQueryResult):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif
    """
    def __init__(self, type, id, gif_url, thumb_url, gif_width = None, gif_height = None, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultgif


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str 

        :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB
        :type  gif_url:  str 

        :param thumb_url: URL of the static thumbnail for the result (jpeg or gif)
        :type  thumb_url:  str 


        Optional keyword parameters:

        :keyword gif_width: Optional. Width of the GIF
        :type    gif_width:  int 

        :keyword gif_height: Optional. Height of the GIF
        :type    gif_height:  int 

        :keyword title: Optional. Title for the result
        :type    title:  str 

        :keyword caption: Optional. Caption of the GIF file to be sent, 0-200 characters
        :type    caption:  str 

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the GIF animation
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultGif, self).__init__(id, "gif")
        
        assert(gif_url is not None)
        assert(isinstance(gif_url, unicode_type))  # unicode on python 2, str on python 3
        self.gif_url = gif_url
        
        assert(gif_width is None or isinstance(gif_width, int))
        self.gif_width = gif_width
        
        assert(gif_height is None or isinstance(gif_height, int))
        self.gif_height = gif_height
        
        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url
        
        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title
        
        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption
        
        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultGif, self).to_array()
        array["gif_url"] = self.gif_url
        array["thumb_url"] = self.thumb_url
        if self.gif_width is not None:
            array["gif_width"] = self.gif_width
        if self.gif_height is not None:
            array["gif_height"] = self.gif_height
        if self.title is not None:
            array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array     
    # end def to_array
# end class InlineQueryResultGif


class InlineQueryResultMpeg4Gif (InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """
    def __init__(self, id, mpeg4_url, thumb_url, mpeg4_width = None, mpeg4_height = None, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str 

        :param mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB
        :type  mpeg4_url:  str 

        :param thumb_url: URL of the static thumbnail (jpeg or gif) for the result
        :type  thumb_url:  str 


        Optional keyword parameters:

        :keyword mpeg4_width: Optional. Video width
        :type    mpeg4_width:  int 

        :keyword mpeg4_height: Optional. Video height
        :type    mpeg4_height:  int 

        :keyword title: Optional. Title for the result
        :type    title:  str 

        :keyword caption: Optional. Caption of the MPEG-4 file to be sent, 0-200 characters
        :type    caption:  str 

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video animation
        :type    input_message_content:  InputMessageContent
        """

        super(InlineQueryResultMpeg4Gif, self).__init__(id, "mpeg4_gif")
        
        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id
        
        assert(mpeg4_url is not None)
        assert(isinstance(mpeg4_url, unicode_type))  # unicode on python 2, str on python 3
        self.mpeg4_url = mpeg4_url
        
        assert(mpeg4_width is None or isinstance(mpeg4_width, int))
        self.mpeg4_width = mpeg4_width
        
        assert(mpeg4_height is None or isinstance(mpeg4_height, int))
        self.mpeg4_height = mpeg4_height
        
        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url
        
        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title
        
        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption
        
        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))  # unicode on python 2, str on python 3
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))  # unicode on python 2, str on python 3
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultMpeg4Gif, self).to_array()
        array["id"] = self.id
        array["mpeg4_url"] = self.mpeg4_url
        array["thumb_url"] = self.thumb_url
        if self.mpeg4_width is not None:
            array["mpeg4_width"] = self.mpeg4_width
        if self.mpeg4_height is not None:
            array["mpeg4_height"] = self.mpeg4_height
        if self.title is not None:
            array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array     
    # end def to_array
# end class InlineQueryResultMpeg4Gif


class InlineQueryResultVideo (InlineQueryResult):
    """
    Represents link to a page containing an embedded video player or a video file.

    https://core.telegram.org/bots/api#inlinequeryresultvideo
    """
    def __init__(self, id, video_url, mime_type, thumb_url, title, caption = None, video_width = None, video_height = None, video_duration = None, description = None, reply_markup = None, input_message_content = None):
        """
        Represents link to a page containing an embedded video player or a video file.

        https://core.telegram.org/bots/api#inlinequeryresultvideo


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str 

        :param video_url: A valid URL for the embedded video player or video file
        :type  video_url:  str 

        :param mime_type: Mime type of the content of video url, “text/html” or “video/mp4”
        :type  mime_type:  str 

        :param thumb_url: URL of the thumbnail (jpeg only) for the video
        :type  thumb_url:  str 

        :param title: Title for the result
        :type  title:  str 


        Optional keyword parameters:

        :keyword caption: Optional. Caption of the video to be sent, 0-200 characters
        :type    caption:  str

        :keyword video_width: Optional. Video width
        :type    video_width:  int 

        :keyword video_height: Optional. Video height
        :type    video_height:  int 

        :keyword video_duration: Optional. Video duration in seconds
        :type    video_duration:  int 

        :keyword description: Optional. Short description of the result
        :type    description:  str 

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultVideo, self).__init__(id, "video")
        
        assert(video_url is not None)
        assert(isinstance(video_url, unicode_type))  # unicode on python 2, str on python 3
        self.video_url = video_url
        
        assert(mime_type is not None)
        assert(isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type
        
        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url
        
        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title
        
        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption
        
        assert(video_width is None or isinstance(video_width, int))
        self.video_width = video_width
        
        assert(video_height is None or isinstance(video_height, int))
        self.video_height = video_height
        
        assert(video_duration is None or isinstance(video_duration, int))
        self.video_duration = video_duration
        
        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVideo, self).to_array()
        array["video_url"] = self.video_url
        array["mime_type"] = self.mime_type
        array["thumb_url"] = self.thumb_url
        array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.video_width is not None:
            array["video_width"] = self.video_width
        if self.video_height is not None:
            array["video_height"] = self.video_height
        if self.video_duration is not None:
            array["video_duration"] = self.video_duration
        if self.description is not None:
            array["description"] = self.description
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultVideo

class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """
    def __init__(self, id, audio_url, title, performer = None, audio_duration = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultaudio


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param audio_url: A valid URL for the audio file
        :type  audio_url:  str

        :param title: Title
        :type  title:  str


        Optional keyword parameters:

        :keyword performer: Optional. Performer
        :type    performer:  str

        :keyword audio_duration: Optional. Audio duration in seconds
        :type    audio_duration:  int

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the audio
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultAudio, self).__init__(id, "video")

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(audio_url is not None)
        assert(isinstance(audio_url, unicode_type))  # unicode on python 2, str on python 3
        self.audio_url = audio_url

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(performer is None or isinstance(performer, unicode_type))  # unicode on python 2, str on python 3
        self.performer = performer

        assert(audio_duration is None or isinstance(audio_duration, int))
        self.audio_duration = audio_duration
        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content # end def __init__

    def to_array(self):
        array = super(InlineQueryResultAudio, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["audio_url"] = self.audio_url
        array["title"] = self.title
        if self.performer is not None:
            array["performer"] = self.performer
        if self.audio_duration is not None:
            array["audio_duration"] = self.audio_duration
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultAudio

class InlineQueryResultVoice (InlineQueryResult):
    """
    Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice
    """
    def __init__(self, id, voice_url, title, voice_duration = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvoice


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param voice_url: A valid URL for the voice recording
        :type  voice_url:  str

        :param title: Recording title
        :type  title:  str


        Optional keyword parameters:

        :keyword voice_duration: Optional. Recording duration in seconds
        :type    voice_duration:  int

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the voice recording
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultVoice, self).__init__(id, "voice")

        assert(voice_url is not None)
        assert(isinstance(voice_url, unicode_type))  # unicode on python 2, str on python 3
        self.voice_url = voice_url

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(voice_duration is None or isinstance(voice_duration, int))
        self.voice_duration = voice_duration


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVoice, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["voice_url"] = self.voice_url
        array["title"] = self.title
        if self.voice_duration is not None:
            array["voice_duration"] = self.voice_duration
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultVoice


class InlineQueryResultDocument (InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultdocument
    """
    def __init__(self, id, title, document_url, mime_type, caption = None, description = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultdocument


        Parameters:

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param title: Title for the result
        :type  title:  str

        :param document_url: A valid URL for the file
        :type  document_url:  str

        :param mime_type: Mime type of the content of the file, either “application/pdf” or “application/zip”
        :type  mime_type:  str


        Optional keyword parameters:

        :keyword caption: Optional. Caption of the document to be sent, 0-200 characters
        :type    caption:  str

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the file
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. URL of the thumbnail (jpeg only) for the file
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultDocument, self).__init__(id, "document")

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        assert(document_url is not None)
        assert(isinstance(document_url, unicode_type))  # unicode on python 2, str on python 3
        self.document_url = document_url

        assert(mime_type is not None)
        assert(isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultDocument, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["title"] = self.title
        array["document_url"] = self.document_url
        array["mime_type"] = self.mime_type
        if self.caption is not None:
            array["caption"] = self.caption
        if self.description is not None:
            array["description"] = self.description
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultDocument


class InlineQueryResultLocation (InlineQueryResult):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation
    """
    def __init__(self, id, latitude, longitude, title, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultlocation


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param latitude: Location latitude in degrees
        :type  latitude:  Float number

        :param longitude: Location longitude in degrees
        :type  longitude:  Float number

        :param title: Location title
        :type  title:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the location
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultLocation, self).__init__(id)

        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude

        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultLocation, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultLocation


class InlineQueryResultVenue (InlineQueryResultLocation):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue
    """
    def __init__(self, id, latitude, longitude, title, address, foursquare_id = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvenue


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param latitude: Latitude of the venue location in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the venue location in degrees
        :type  longitude:  Float

        :param title: Title of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue if known
        :type    foursquare_id:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the venue
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultVenue, self).__init__(
            id=id, latitude=latitude, longitude=longitude, title=title, reply_markup=reply_markup,
            input_message_content=input_message_content, thumb_url=thumb_url,
            thumb_width=thumb_width, thumb_height=thumb_height
        )
        self.type = "venue"

        assert(address is not None)
        assert(isinstance(address, unicode_type))  # unicode on python 2, str on python 3
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, unicode_type))  # unicode on python 2, str on python 3
        self.foursquare_id = foursquare_id
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVenue, self).to_array()
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
        return array
    # end def to_array
# end class InlineQueryResultVenue

class InlineQueryResultContact (InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact
    """
    def __init__(self, id, phone_number, first_name, last_name = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcontact


        Parameters:

        :param type: Type of the result, must be contact
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the contact
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultContact, self).__init__(id, "contact")

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup

        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content
        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultContact, self).to_array()
        array["phone_number"] = self.phone_number
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultContact