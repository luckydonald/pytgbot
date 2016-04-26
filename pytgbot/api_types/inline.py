# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'luckydonald'

from ..encoding import text_type as unicode_type, to_unicode as u
import logging
logger = logging.getLogger(__name__)


class InlineQueryResult(object):
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
    

class InlineQueryResultArticle (InlineQueryResult):
    """
    Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """
    def __init__(self, id, title, message_text, parse_mode = None, disable_web_page_preview = None, url = None, hide_url = None, description = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a link to an article or web page.

        https://core.telegram.org/bots/api#inlinequeryresultarticle


        Parameters:

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str 

        :param title: Title of the result
        :type  title:  str 

        :param message_text: Text of the message to be sent, 1-4096 characters
        :type  message_text:  str 


        Optional keyword parameters:

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
        
        assert(message_text is not None)
        assert(isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text
        
        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode
        
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
        
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
        array["id"] = self.id
        array["title"] = self.title
        array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
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

        :keyword message_text: Optional. Text of a message to be sent instead of the photo, 1-4096 characters
        :type    message_text:  str 

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str 

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool 
        """
        super(InlineQueryResultPhoto, self).__init__(id, "photo")
        
        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id
        
        assert(photo_url is not None)
        assert(isinstance(photo_url, unicode_type))  # unicode on python 2, str on python 3
        self.photo_url = photo_url
        
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
        
        assert(message_text is None or isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text
        
        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode
        
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
        if self.message_text is not None:
            array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        return array     
    # end def to_array
# end class InlineQueryResultPhoto


class InlineQueryResultGif (InlineQueryResult):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can provide message_text to send it instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif
    """
    def __init__(self, id, gif_url, thumb_url, gif_width = None, gif_height = None, title = None, caption = None, message_text = None, parse_mode = None, disable_web_page_preview = None):
        """
        Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can provide message_text to send it instead of the animation.

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

        :keyword message_text: Optional. Text of a message to be sent instead of the animation, 1-4096 characters
        :type    message_text:  str 

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str 

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool 
        """
        super(InlineQueryResultGif, self).__init__(id, "gif")
        
        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id
        
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
        
        assert(message_text is None or isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text
        
        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode
        
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultGif, self).to_array()
        array["id"] = self.id
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
        if self.message_text is not None:
            array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        return array     
    # end def to_array
# end class InlineQueryResultGif


class InlineQueryResultMpeg4Gif (InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can provide message_text to send it instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """
    def __init__(self, id, mpeg4_url, thumb_url, mpeg4_width = None, mpeg4_height = None, title = None, caption = None, message_text = None, parse_mode = None, disable_web_page_preview = None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can provide message_text to send it instead of the animation.

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

        :keyword message_text: Optional. Text of a message to be sent instead of the animation, 1-4096 characters
        :type    message_text:  str 

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str 

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool 
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
        
        assert(message_text is None or isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text
        
        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode
        
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
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
        if self.message_text is not None:
            array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        return array     
    # end def to_array
# end class InlineQueryResultMpeg4Gif


class InlineQueryResultVideo (InlineQueryResult):
    """
    Represents link to a page containing an embedded video player or a video file.

    https://core.telegram.org/bots/api#inlinequeryresultvideo
    """
    def __init__(self, id, video_url, mime_type, message_text, thumb_url, title, parse_mode = None, disable_web_page_preview = None, video_width = None, video_height = None, video_duration = None, description = None):
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

        :param message_text: Text of the message to be sent with the video, 1-4096 characters
        :type  message_text:  str 

        :param thumb_url: URL of the thumbnail (jpeg only) for the video
        :type  thumb_url:  str 

        :param title: Title for the result
        :type  title:  str 


        Optional keyword parameters:

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str 

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool 

        :keyword video_width: Optional. Video width
        :type    video_width:  int 

        :keyword video_height: Optional. Video height
        :type    video_height:  int 

        :keyword video_duration: Optional. Video duration in seconds
        :type    video_duration:  int 

        :keyword description: Optional. Short description of the result
        :type    description:  str 
        """
        super(InlineQueryResultVideo, self).__init__(id, "video")
        
        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id
        
        assert(video_url is not None)
        assert(isinstance(video_url, unicode_type))  # unicode on python 2, str on python 3
        self.video_url = video_url
        
        assert(mime_type is not None)
        assert(isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type
        
        assert(message_text is not None)
        assert(isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text
        
        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode
        
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
        
        assert(video_width is None or isinstance(video_width, int))
        self.video_width = video_width
        
        assert(video_height is None or isinstance(video_height, int))
        self.video_height = video_height
        
        assert(video_duration is None or isinstance(video_duration, int))
        self.video_duration = video_duration
        
        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url
        
        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title
        
        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVideo, self).to_array()
        array["id"] = self.id
        array["video_url"] = self.video_url
        array["mime_type"] = self.mime_type
        array["message_text"] = self.message_text
        array["thumb_url"] = self.thumb_url
        array["title"] = self.title
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        if self.video_width is not None:
            array["video_width"] = self.video_width
        if self.video_height is not None:
            array["video_height"] = self.video_height
        if self.video_duration is not None:
            array["video_duration"] = self.video_duration
        if self.description is not None:
            array["description"] = self.description
        return array     
    # end def to_array
# end class InlineQueryResultVideo
