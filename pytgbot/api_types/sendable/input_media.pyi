# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.input_media import InputMedia
from pytgbot.api_types.sendable.input_media import InputMediaPlayable
from pytgbot.api_types.sendable.input_media import InputMediaVideolike
from pytgbot.api_types.sendable.input_media import InputMediaWithThumb

__author__ = 'luckydonald'


class InputMedia(Sendable):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the media to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """
    type: str
    media: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
# end class InputMedia

class InputMediaWithThumb(InputMedia):
    """
    InputMedia but with a thumb field.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode

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
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
# end class InputMediaWithThumb

class InputMediaPlayable(InputMediaWithThumb):
    """
    InputMedia with a thumb and duration.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode

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
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    duration: int
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
# end class InputMediaPlayable

class InputMediaVideolike(InputMediaPlayable):
    """
    This object represents the content of a media message to be sent.

    https://core.telegram.org/bots/api#inputmedia


    Parameters:

    :param type: Type of the result, a fixed value per subclass
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode

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
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    duration: int
    width: int
    height: int
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
# end class InputMediaVideolike

class InputMediaPhoto(InputMedia):
    """
    Represents a photo to be sent.

    https://core.telegram.org/bots/api#inputmediaphoto


    Parameters:

    :param type: Type of the result, must be photo
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode


    Optional keyword parameters:

    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity
    """
    type: str
    media: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
# end class InputMediaPhoto

class InputMediaVideo(InputMediaVideolike):
    """
    Represents a video to be sent.

    https://core.telegram.org/bots/api#inputmediavideo


    Parameters:

    :param type: Type of the result, must be video
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode


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

    :param duration: Optional. Video duration in seconds
    :type  duration: int

    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    :type  supports_streaming: bool
    """
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    width: int
    height: int
    duration: int
    supports_streaming: bool
# end class InputMediaVideo

class InputMediaAnimation(InputMediaVideolike):
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be sent.

    https://core.telegram.org/bots/api#inputmediaanimation


    Parameters:

    :param type: Type of the result, must be animation
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode


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

    :param duration: Optional. Animation duration in seconds
    :type  duration: int
    """
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    width: int
    height: int
    duration: int
# end class InputMediaAnimation

class InputMediaAudio(InputMediaPlayable):
    """
    Represents an audio file to be treated as music to be sent.

    https://core.telegram.org/bots/api#inputmediaaudio


    Parameters:

    :param type: Type of the result, must be audio
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode


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
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    duration: int
    performer: str
    title: str
# end class InputMediaAudio

class InputMediaDocument(InputMediaWithThumb):
    """
    Represents a general file to be sent.

    https://core.telegram.org/bots/api#inputmediadocument


    Parameters:

    :param type: Type of the result, must be document
    :type  type: str|unicode

    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass "attach://<file_attach_name>" to upload a new one using multipart/form-data under <file_attach_name> name. More info on Sending Files »
    :type  media: pytgbot.api_types.sendable.files.InputFile | str|unicode


    Optional keyword parameters:

    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode

    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
    :type  caption: str|unicode

    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options for more details.
    :type  parse_mode: str|unicode

    :param caption_entities: Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param disable_content_type_detection: Optional. Disables automatic server-side content type detection for files uploaded using multipart/form-data. Always True, if the document is sent as part of an album.
    :type  disable_content_type_detection: bool
    """
    type: str
    media: Union[InputFile, str]
    thumb: Union[InputFile, str]
    caption: str
    parse_mode: str
    caption_entities: List[MessageEntity]
    disable_content_type_detection: bool
# end class InputMediaDocument
