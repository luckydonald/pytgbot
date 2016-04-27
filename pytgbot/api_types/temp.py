from pytgbot import InlineQueryResult
from pytgbot.responses import Result

class InlineQueryResultPhoto (InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto
    """
    def __init__(self, type, id, photo_url, thumb_url, photo_width = None, photo_height = None, title = None, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultphoto


        Parameters:

        :param type: Type of the result, must be photo
        :type  type:  str

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
        super(InlineQueryResultPhoto, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

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

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultPhoto, self).to_array()
        array["type"] = self.type
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

        :param type: Type of the result, must be gif
        :type  type:  str

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
        :type    input_message_content:  inputMessageContent
        """
        super(InlineQueryResultGif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

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

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultGif, self).to_array()
        array["type"] = self.type
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
    def __init__(self, type, id, mpeg4_url, thumb_url, mpeg4_width = None, mpeg4_height = None, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif


        Parameters:

        :param type: Type of the result, must be mpeg4_gif
        :type  type:  str

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
        super(InlineQueryResultMpeg4Gif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

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

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultMpeg4Gif, self).to_array()
        array["type"] = self.type
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
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultvideo
    """
    def __init__(self, type, id, video_url, mime_type, thumb_url, title, caption = None, video_width = None, video_height = None, video_duration = None, description = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultvideo


        Parameters:

        :param type: Type of the result, must be video
        :type  type:  str

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
        super(InlineQueryResultVideo, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

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

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVideo, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
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

class InlineQueryResultAudio (InlineQueryResult):
    """
    Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """
    def __init__(self, type, id, audio_url, title, performer = None, audio_duration = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultaudio


        Parameters:

        :param type: Type of the result, must be audio
        :type  type:  str

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
        super(InlineQueryResultAudio, self).__init__(id)

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

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

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
    def __init__(self, type, id, voice_url, title, voice_duration = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvoice


        Parameters:

        :param type: Type of the result, must be voice
        :type  type:  str

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
        super(InlineQueryResultVoice, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(voice_url is not None)
        assert(isinstance(voice_url, unicode_type))  # unicode on python 2, str on python 3
        self.voice_url = voice_url

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(voice_duration is None or isinstance(voice_duration, int))
        self.voice_duration = voice_duration

        self.reply_markup = reply_markup

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
    def __init__(self, type, id, title, document_url, mime_type, caption = None, description = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultdocument


        Parameters:

        :param type: Type of the result, must be document
        :type  type:  str

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
        super(InlineQueryResultDocument, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

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

        self.reply_markup = reply_markup

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
    def __init__(self, type, id, latitude, longitude, title, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultlocation


        Parameters:

        :param type: Type of the result, must be location
        :type  type:  str

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

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        self.latitude = latitude

        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        self.reply_markup = reply_markup

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

class InlineQueryResultVenue (InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue
    """
    def __init__(self, type, id, latitude, longitude, title, address, foursquare_id = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvenue


        Parameters:

        :param type: Type of the result, must be venue
        :type  type:  str

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
        super(InlineQueryResultVenue, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        self.latitude = latitude

        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(address is not None)
        assert(isinstance(address, unicode_type))  # unicode on python 2, str on python 3
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, unicode_type))  # unicode on python 2, str on python 3
        self.foursquare_id = foursquare_id

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVenue, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
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
# end class InlineQueryResultVenue

class InlineQueryResultContact (InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact
    """
    def __init__(self, type, id, phone_number, first_name, last_name = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
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
        super(InlineQueryResultContact, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name

        self.reply_markup = reply_markup

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
        array["type"] = self.type
        array["id"] = self.id
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

class InlineQueryResultCachedPhoto (InlineQueryResult):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """
    def __init__(self, type, id, photo_file_id, title = None, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultcachedphoto


        Parameters:

        :param type: Type of the result, must be photo
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param photo_file_id: A valid file identifier of the photo
        :type  photo_file_id:  str


        Optional keyword parameters:

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
        super(InlineQueryResultCachedPhoto, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(photo_file_id is not None)
        assert(isinstance(photo_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.photo_file_id = photo_file_id

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedPhoto, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["photo_file_id"] = self.photo_file_id
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
# end class InlineQueryResultCachedPhoto

class InlineQueryResultCachedGif (InlineQueryResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    """
    def __init__(self, type, id, gif_file_id, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedgif


        Parameters:

        :param type: Type of the result, must be gif
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param gif_file_id: A valid file identifier for the GIF file
        :type  gif_file_id:  str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword caption: Optional. Caption of the GIF file to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the GIF animation
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedGif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(gif_file_id is not None)
        assert(isinstance(gif_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.gif_file_id = gif_file_id

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedGif, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["gif_file_id"] = self.gif_file_id
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
# end class InlineQueryResultCachedGif

class InlineQueryResultCachedMpeg4Gif (InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """
    def __init__(self, type, id, mpeg4_file_id, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif


        Parameters:

        :param type: Type of the result, must be mpeg4_gif
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param mpeg4_file_id: A valid file identifier for the MP4 file
        :type  mpeg4_file_id:  str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword caption: Optional. Caption of the MPEG-4 file to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video animation
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedMpeg4Gif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(mpeg4_file_id is not None)
        assert(isinstance(mpeg4_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.mpeg4_file_id = mpeg4_file_id

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedMpeg4Gif, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["mpeg4_file_id"] = self.mpeg4_file_id
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
# end class InlineQueryResultCachedMpeg4Gif

class InlineQueryResultCachedSticker (InlineQueryResult):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """
    def __init__(self, type, id, sticker_file_id, reply_markup = None, input_message_content = None):
        """
        Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedsticker


        Parameters:

        :param type: Type of the result, must be sticker
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param sticker_file_id: A valid file identifier of the sticker
        :type  sticker_file_id:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the sticker
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedSticker, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(sticker_file_id is not None)
        assert(isinstance(sticker_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.sticker_file_id = sticker_file_id

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedSticker, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["sticker_file_id"] = self.sticker_file_id
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedSticker

class InlineQueryResultCachedDocument (InlineQueryResult):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only pdf-files and zip archives can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """
    def __init__(self, type, id, title, document_file_id, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only pdf-files and zip archives can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcacheddocument


        Parameters:

        :param type: Type of the result, must be document
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param title: Title for the result
        :type  title:  str

        :param document_file_id: A valid file identifier for the file
        :type  document_file_id:  str


        Optional keyword parameters:

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword caption: Optional. Caption of the document to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the file
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedDocument, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(document_file_id is not None)
        assert(isinstance(document_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.document_file_id = document_file_id

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedDocument, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["title"] = self.title
        array["document_file_id"] = self.document_file_id
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
# end class InlineQueryResultCachedDocument

class InlineQueryResultCachedVideo (InlineQueryResult):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    """
    def __init__(self, type, id, video_file_id, title, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvideo


        Parameters:

        :param type: Type of the result, must be video
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param video_file_id: A valid file identifier for the video file
        :type  video_file_id:  str

        :param title: Title for the result
        :type  title:  str


        Optional keyword parameters:

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword caption: Optional. Caption of the video to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedVideo, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(video_file_id is not None)
        assert(isinstance(video_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.video_file_id = video_file_id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedVideo, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["video_file_id"] = self.video_file_id
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
# end class InlineQueryResultCachedVideo

class InlineQueryResultCachedVoice (InlineQueryResult):
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    """
    def __init__(self, type, id, voice_file_id, title, reply_markup = None, input_message_content = None):
        """
        Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvoice


        Parameters:

        :param type: Type of the result, must be voice
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param voice_file_id: A valid file identifier for the voice message
        :type  voice_file_id:  str

        :param title: Voice message title
        :type  title:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the voice message
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedVoice, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(voice_file_id is not None)
        assert(isinstance(voice_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.voice_file_id = voice_file_id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedVoice, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["voice_file_id"] = self.voice_file_id
        array["title"] = self.title
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedVoice

class InlineQueryResultCachedAudio (InlineQueryResult):
    """
    Represents a link to an mp3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """
    def __init__(self, type, id, audio_file_id, reply_markup = None, input_message_content = None):
        """
        Represents a link to an mp3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedaudio


        Parameters:

        :param type: Type of the result, must be audio
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param audio_file_id: A valid file identifier for the audio file
        :type  audio_file_id:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the audio
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedAudio, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(audio_file_id is not None)
        assert(isinstance(audio_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.audio_file_id = audio_file_id

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedAudio, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["audio_file_id"] = self.audio_file_id
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedAudio

class InputTextMessageContent (InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    def __init__(self, message_text, parse_mode = None, disable_web_page_preview = None):
        """
        Represents the content of a text message to be sent as the result of an inline query.

        https://core.telegram.org/bots/api#inputtextmessagecontent


        Parameters:

        :param message_text: Text of the message to be sent, 1-4096 characters
        :type  message_text:  str


        Optional keyword parameters:

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool
        """
        super(InputTextMessageContent, self).__init__(id)

        assert(message_text is not None)
        assert(isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text

        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode

        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self):
        array = super(InputTextMessageContent, self).to_array()
        array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        return array
    # end def to_array
# end class InputTextMessageContent

class InputLocationMessageContent (InputMessageContent):
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
        :type  latitude:  Float

        :param longitude: Longitude of the location in degrees
        :type  longitude:  Float
        """
        super(InputLocationMessageContent, self).__init__(id)

        self.latitude = latitude

        self.longitude = longitude
    # end def __init__

    def to_array(self):
        array = super(InputLocationMessageContent, self).to_array()
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        return array
    # end def to_array
# end class InputLocationMessageContent

class InputVenueMessageContent (InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    def __init__(self, latitude, longitude, title, address, foursquare_id = None):
        """
        Represents the content of a venue message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputvenuemessagecontent


        Parameters:

        :param latitude: Latitude of the venue in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the venue in degrees
        :type  longitude:  Float

        :param title: Name of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue, if known
        :type    foursquare_id:  str
        """
        super(InputVenueMessageContent, self).__init__(id)

        self.latitude = latitude

        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(address is not None)
        assert(isinstance(address, unicode_type))  # unicode on python 2, str on python 3
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, unicode_type))  # unicode on python 2, str on python 3
        self.foursquare_id = foursquare_id
    # end def __init__

    def to_array(self):
        array = super(InputVenueMessageContent, self).to_array()
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
        return array
    # end def to_array
# end class InputVenueMessageContent

class InputContactMessageContent (InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    def __init__(self, phone_number, first_name, last_name = None):
        """
        Represents the content of a contact message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputcontactmessagecontent


        Parameters:

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name:  str
        """
        super(InputContactMessageContent, self).__init__(id)

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name
    # end def __init__

    def to_array(self):
        array = super(InputContactMessageContent, self).to_array()
        array["phone_number"] = self.phone_number
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        return array
    # end def to_array
# end class InputContactMessageContent

class ChosenInlineResult (InlineQueryResult):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    https://core.telegram.org/bots/api#choseninlineresult
    """
    def __init__(self, result_id, from_peer, query, location = None, inline_message_id = None):
        """
        Represents a result of an inline query that was chosen by the user and sent to their chat partner.

        https://core.telegram.org/bots/api#choseninlineresult


        Parameters:

        :param result_id: The unique identifier for the result that was chosen
        :type  result_id:  str

        :param from_peer: The user that chose the result
        :type  from_peer:  User

        :param query: The query that was used to obtain the result
        :type  query:  str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that require user location
        :type    location:  Location

        :keyword inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        :type    inline_message_id:  str
        """
        super(ChosenInlineResult, self).__init__(id)

        assert(result_id is not None)
        assert(isinstance(result_id, unicode_type))  # unicode on python 2, str on python 3
        self.result_id = result_id

        self.from_peer = from_peer

        self.location = location

        assert(inline_message_id is None or isinstance(inline_message_id, unicode_type))  # unicode on python 2, str on python 3
        self.inline_message_id = inline_message_id

        assert(query is not None)
        assert(isinstance(query, unicode_type))  # unicode on python 2, str on python 3
        self.query = query
    # end def __init__

    def to_array(self):
        array = super(ChosenInlineResult, self).to_array()
        array["result_id"] = self.result_id
        array["from_peer"] = self.from_peer
        array["query"] = self.query
        if self.location is not None:
            array["location"] = self.location
        if self.inline_message_id is not None:
            array["inline_message_id"] = self.inline_message_id
        return array
    # end def to_array
# end class ChosenInlineResult

