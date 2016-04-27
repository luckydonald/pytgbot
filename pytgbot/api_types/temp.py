from pytgbot import InlineQueryResult
from pytgbot.responses import Result

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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


        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        self.reply_markup = reply_markup
        
        assert(input_message_content is None or isinstance(input_message_content, InputMessageContent))
        self.input_message_content = input_message_content     # end def __init__

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

