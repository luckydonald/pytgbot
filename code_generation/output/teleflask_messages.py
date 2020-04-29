# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from pytgbot.api_types.receivable.updates import Message as PytgbotApiMessage
from pytgbot.bot import Bot as PytgbotApiBot

from .messages import DEFAULT_MESSAGE_ID


__author__ = "luckydonald"


class SendableMessageBase(object):
    def _apply_update_receiver(self, receiver, reply_id):
        """
        Updates `self.receiver` and/or `self.reply_id` if they still contain the default value.
        :param receiver: The receiver `chat_id` to use.
                         Either `self.receiver`, if set, e.g. when instancing `TextMessage(receiver=10001231231, ...)`,
                         or the `chat.id` of the update context, being the id of groups or the user's `from_peer.id` in private messages.
        :type  receiver: None | str|unicode | int


        :param reply_id: Reply to that `message_id` in the chat we send to.
                         Either `self.reply_id`, if set, e.g. when instancing `TextMessage(reply_id=123123, ...)`,
                         or the `message_id` of the update which triggered the bot's functions.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        """
        if self.receiver is None:
            self.receiver = receiver
        # end if
        if self.reply_id is DEFAULT_MESSAGE_ID:
            self.reply_id = reply_id
        # end if
    # end def

    def send(self, sender: PytgbotApiBot) -> PytgbotApiMessage:
        raise NotImplementedError("Overwrite this function.")
# end def


class TextMessage(SendableMessageBase):
    """
    Use this method to send text messages. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendmessage

    
    Parameters:
    
    :param text: Text of the message to be sent, 1-4096 characters after entities parsing
    :type  text: str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param parse_mode: Mode for parsing entities in the message text. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param disable_web_page_preview: Disables link previews for links in this message
    :type  disable_web_page_preview: bool
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, text, receiver=None, reply_id=DEFAULT_MESSAGE_ID, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send text messages. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendmessage

        
        Parameters:
        
        :param text: Text of the message to be sent, 1-4096 characters after entities parsing
        :type  text: str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param parse_mode: Mode for parsing entities in the message text. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param disable_web_page_preview: Disables link previews for links in this message
        :type  disable_web_page_preview: bool
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(TextMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(text, unicode_type, parameter_name="text")
        self.text = text
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(disable_web_page_preview, None, bool, parameter_name="disable_web_page_preview")
        self.disable_web_page_preview = disable_web_page_preview
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_message(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            text=self.text, chat_id=self.receiver, reply_to_message_id=self.reply_id, parse_mode=self.parse_mode, disable_web_page_preview=self.disable_web_page_preview, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this TextMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(TextMessage, self).to_array()
        array['text'] = u(self.text)  # py2: type unicode, py3: type str
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.disable_web_page_preview is not None:
            array['disable_web_page_preview'] = bool(self.disable_web_page_preview)  # type bool
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the TextMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        data['text'] = u(array.get('text'))
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['disable_web_page_preview'] = bool(array.get('disable_web_page_preview')) if array.get('disable_web_page_preview') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new TextMessage from a given dictionary.

        :return: new TextMessage instance.
        :rtype: TextMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = TextMessage.validate_array(array)
        return TextMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(textmessage_instance)`
        """
        return "TextMessage(text={self.text!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, parse_mode={self.parse_mode!r}, disable_web_page_preview={self.disable_web_page_preview!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(textmessage_instance)`
        """
        return "TextMessage(text={self.text!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, parse_mode={self.parse_mode!r}, disable_web_page_preview={self.disable_web_page_preview!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in textmessage_instance`
        """
        return (
            key in ["text", "receiver", "reply_id", "parse_mode", "disable_web_page_preview", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class TextMessage

class PhotoMessage(SendableMessageBase):
    """
    Use this method to send photos. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendphoto

    
    Parameters:
    
    :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. More info on Sending Files »
    :type  photo: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
    :type  caption: str|unicode
    
    :param parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, photo, receiver=None, reply_id=DEFAULT_MESSAGE_ID, caption=None, parse_mode=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send photos. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendphoto

        
        Parameters:
        
        :param photo: Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. More info on Sending Files »
        :type  photo: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param caption: Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
        :type  caption: str|unicode
        
        :param parse_mode: Mode for parsing entities in the photo caption. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(PhotoMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(photo, InputFile, unicode_type, parameter_name="photo")
        self.photo = photo
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_photo(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            photo=self.photo, chat_id=self.receiver, reply_to_message_id=self.reply_id, caption=self.caption, parse_mode=self.parse_mode, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this PhotoMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PhotoMessage, self).to_array()
        if isinstance(self.photo, InputFile):
            array['photo'] = self.photo.to_array()  # type InputFile
        elif isinstance(self.photo, str):
            array['photo'] = u(self.photo)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PhotoMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('photo'), InputFile):
            data['photo'] = InputFile.from_array(array.get('photo'))
        elif isinstance(array.get('photo'), str):
            data['photo'] = u(array.get('photo'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PhotoMessage from a given dictionary.

        :return: new PhotoMessage instance.
        :rtype: PhotoMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = PhotoMessage.validate_array(array)
        return PhotoMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(photomessage_instance)`
        """
        return "PhotoMessage(photo={self.photo!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(photomessage_instance)`
        """
        return "PhotoMessage(photo={self.photo!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in photomessage_instance`
        """
        return (
            key in ["photo", "receiver", "reply_id", "caption", "parse_mode", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class PhotoMessage

class AudioMessage(SendableMessageBase):
    """
    Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
        For sending voice messages, use the sendVoice method instead.

    https://core.telegram.org/bots/api#sendaudio

    
    Parameters:
    
    :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :type  audio: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param caption: Audio caption, 0-1024 characters after entities parsing
    :type  caption: str|unicode
    
    :param parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param duration: Duration of the audio in seconds
    :type  duration: int
    
    :param performer: Performer
    :type  performer: str|unicode
    
    :param title: Track name
    :type  title: str|unicode
    
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, audio, receiver=None, reply_id=DEFAULT_MESSAGE_ID, caption=None, parse_mode=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
            For sending voice messages, use the sendVoice method instead.

        https://core.telegram.org/bots/api#sendaudio

        
        Parameters:
        
        :param audio: Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
        :type  audio: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param caption: Audio caption, 0-1024 characters after entities parsing
        :type  caption: str|unicode
        
        :param parse_mode: Mode for parsing entities in the audio caption. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param duration: Duration of the audio in seconds
        :type  duration: int
        
        :param performer: Performer
        :type  performer: str|unicode
        
        :param title: Track name
        :type  title: str|unicode
        
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(AudioMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(audio, InputFile, unicode_type, parameter_name="audio")
        self.audio = audio
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
        
        assert_type_or_raise(performer, None, unicode_type, parameter_name="performer")
        self.performer = performer
        
        assert_type_or_raise(title, None, unicode_type, parameter_name="title")
        self.title = title
        
        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_audio(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            audio=self.audio, chat_id=self.receiver, reply_to_message_id=self.reply_id, caption=self.caption, parse_mode=self.parse_mode, duration=self.duration, performer=self.performer, title=self.title, thumb=self.thumb, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this AudioMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(AudioMessage, self).to_array()
        if isinstance(self.audio, InputFile):
            array['audio'] = self.audio.to_array()  # type InputFile
        elif isinstance(self.audio, str):
            array['audio'] = u(self.audio)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.performer is not None:
            array['performer'] = u(self.performer)  # py2: type unicode, py3: type str
        if self.title is not None:
            array['title'] = u(self.title)  # py2: type unicode, py3: type str
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = self.thumb.to_array()  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type strelse:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if

        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the AudioMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('audio'), InputFile):
            data['audio'] = InputFile.from_array(array.get('audio'))
        elif isinstance(array.get('audio'), str):
            data['audio'] = u(array.get('audio'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['performer'] = u(array.get('performer')) if array.get('performer') is not None else None
        data['title'] = u(array.get('title')) if array.get('title') is not None else None
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = InputFile.from_array(array.get('thumb'))
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new AudioMessage from a given dictionary.

        :return: new AudioMessage instance.
        :rtype: AudioMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = AudioMessage.validate_array(array)
        return AudioMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(audiomessage_instance)`
        """
        return "AudioMessage(audio={self.audio!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r}, thumb={self.thumb!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(audiomessage_instance)`
        """
        return "AudioMessage(audio={self.audio!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, duration={self.duration!r}, performer={self.performer!r}, title={self.title!r}, thumb={self.thumb!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in audiomessage_instance`
        """
        return (
            key in ["audio", "receiver", "reply_id", "caption", "parse_mode", "duration", "performer", "title", "thumb", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class AudioMessage

class DocumentMessage(SendableMessageBase):
    """
    Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#senddocument

    
    Parameters:
    
    :param document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :type  document: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    :param caption: Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
    :type  caption: str|unicode
    
    :param parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, document, receiver=None, reply_id=DEFAULT_MESSAGE_ID, thumb=None, caption=None, parse_mode=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#senddocument

        
        Parameters:
        
        :param document: File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
        :type  document: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        :param caption: Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing
        :type  caption: str|unicode
        
        :param parse_mode: Mode for parsing entities in the document caption. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(DocumentMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(document, InputFile, unicode_type, parameter_name="document")
        self.document = document
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_document(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            document=self.document, chat_id=self.receiver, reply_to_message_id=self.reply_id, thumb=self.thumb, caption=self.caption, parse_mode=self.parse_mode, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this DocumentMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(DocumentMessage, self).to_array()
        if isinstance(self.document, InputFile):
            array['document'] = self.document.to_array()  # type InputFile
        elif isinstance(self.document, str):
            array['document'] = u(self.document)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = self.thumb.to_array()  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type strelse:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if

        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the DocumentMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('document'), InputFile):
            data['document'] = InputFile.from_array(array.get('document'))
        elif isinstance(array.get('document'), str):
            data['document'] = u(array.get('document'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = InputFile.from_array(array.get('thumb'))
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new DocumentMessage from a given dictionary.

        :return: new DocumentMessage instance.
        :rtype: DocumentMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = DocumentMessage.validate_array(array)
        return DocumentMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(documentmessage_instance)`
        """
        return "DocumentMessage(document={self.document!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(documentmessage_instance)`
        """
        return "DocumentMessage(document={self.document!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in documentmessage_instance`
        """
        return (
            key in ["document", "receiver", "reply_id", "thumb", "caption", "parse_mode", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class DocumentMessage

class VideoMessage(SendableMessageBase):
    """
    Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#sendvideo

    
    Parameters:
    
    :param video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files »
    :type  video: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param duration: Duration of sent video in seconds
    :type  duration: int
    
    :param width: Video width
    :type  width: int
    
    :param height: Video height
    :type  height: int
    
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    :param caption: Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
    :type  caption: str|unicode
    
    :param parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param supports_streaming: Pass True, if the uploaded video is suitable for streaming
    :type  supports_streaming: bool
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, video, receiver=None, reply_id=DEFAULT_MESSAGE_ID, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, supports_streaming=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendvideo

        
        Parameters:
        
        :param video: Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files »
        :type  video: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param duration: Duration of sent video in seconds
        :type  duration: int
        
        :param width: Video width
        :type  width: int
        
        :param height: Video height
        :type  height: int
        
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        :param caption: Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
        :type  caption: str|unicode
        
        :param parse_mode: Mode for parsing entities in the video caption. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param supports_streaming: Pass True, if the uploaded video is suitable for streaming
        :type  supports_streaming: bool
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(VideoMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(video, InputFile, unicode_type, parameter_name="video")
        self.video = video
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
        
        assert_type_or_raise(width, None, int, parameter_name="width")
        self.width = width
        
        assert_type_or_raise(height, None, int, parameter_name="height")
        self.height = height
        
        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(supports_streaming, None, bool, parameter_name="supports_streaming")
        self.supports_streaming = supports_streaming
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_video(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            video=self.video, chat_id=self.receiver, reply_to_message_id=self.reply_id, duration=self.duration, width=self.width, height=self.height, thumb=self.thumb, caption=self.caption, parse_mode=self.parse_mode, supports_streaming=self.supports_streaming, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this VideoMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(VideoMessage, self).to_array()
        if isinstance(self.video, InputFile):
            array['video'] = self.video.to_array()  # type InputFile
        elif isinstance(self.video, str):
            array['video'] = u(self.video)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.width is not None:
            array['width'] = int(self.width)  # type int
        if self.height is not None:
            array['height'] = int(self.height)  # type int
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = self.thumb.to_array()  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type strelse:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if

        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.supports_streaming is not None:
            array['supports_streaming'] = bool(self.supports_streaming)  # type bool
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VideoMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('video'), InputFile):
            data['video'] = InputFile.from_array(array.get('video'))
        elif isinstance(array.get('video'), str):
            data['video'] = u(array.get('video'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['width'] = int(array.get('width')) if array.get('width') is not None else None
        data['height'] = int(array.get('height')) if array.get('height') is not None else None
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = InputFile.from_array(array.get('thumb'))
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['supports_streaming'] = bool(array.get('supports_streaming')) if array.get('supports_streaming') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VideoMessage from a given dictionary.

        :return: new VideoMessage instance.
        :rtype: VideoMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = VideoMessage.validate_array(array)
        return VideoMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(videomessage_instance)`
        """
        return "VideoMessage(video={self.video!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, duration={self.duration!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, supports_streaming={self.supports_streaming!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(videomessage_instance)`
        """
        return "VideoMessage(video={self.video!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, duration={self.duration!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, supports_streaming={self.supports_streaming!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in videomessage_instance`
        """
        return (
            key in ["video", "receiver", "reply_id", "duration", "width", "height", "thumb", "caption", "parse_mode", "supports_streaming", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VideoMessage

class AnimationMessage(SendableMessageBase):
    """
    Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#sendanimation

    
    Parameters:
    
    :param animation: Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files »
    :type  animation: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param duration: Duration of sent animation in seconds
    :type  duration: int
    
    :param width: Animation width
    :type  width: int
    
    :param height: Animation height
    :type  height: int
    
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    :param caption: Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
    :type  caption: str|unicode
    
    :param parse_mode: Mode for parsing entities in the animation caption. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, animation, receiver=None, reply_id=DEFAULT_MESSAGE_ID, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendanimation

        
        Parameters:
        
        :param animation: Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files »
        :type  animation: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param duration: Duration of sent animation in seconds
        :type  duration: int
        
        :param width: Animation width
        :type  width: int
        
        :param height: Animation height
        :type  height: int
        
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        :param caption: Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing
        :type  caption: str|unicode
        
        :param parse_mode: Mode for parsing entities in the animation caption. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(AnimationMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(animation, InputFile, unicode_type, parameter_name="animation")
        self.animation = animation
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
        
        assert_type_or_raise(width, None, int, parameter_name="width")
        self.width = width
        
        assert_type_or_raise(height, None, int, parameter_name="height")
        self.height = height
        
        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_animation(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            animation=self.animation, chat_id=self.receiver, reply_to_message_id=self.reply_id, duration=self.duration, width=self.width, height=self.height, thumb=self.thumb, caption=self.caption, parse_mode=self.parse_mode, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this AnimationMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(AnimationMessage, self).to_array()
        if isinstance(self.animation, InputFile):
            array['animation'] = self.animation.to_array()  # type InputFile
        elif isinstance(self.animation, str):
            array['animation'] = u(self.animation)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.width is not None:
            array['width'] = int(self.width)  # type int
        if self.height is not None:
            array['height'] = int(self.height)  # type int
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = self.thumb.to_array()  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type strelse:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if

        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the AnimationMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('animation'), InputFile):
            data['animation'] = InputFile.from_array(array.get('animation'))
        elif isinstance(array.get('animation'), str):
            data['animation'] = u(array.get('animation'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['width'] = int(array.get('width')) if array.get('width') is not None else None
        data['height'] = int(array.get('height')) if array.get('height') is not None else None
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = InputFile.from_array(array.get('thumb'))
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new AnimationMessage from a given dictionary.

        :return: new AnimationMessage instance.
        :rtype: AnimationMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = AnimationMessage.validate_array(array)
        return AnimationMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(animationmessage_instance)`
        """
        return "AnimationMessage(animation={self.animation!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, duration={self.duration!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(animationmessage_instance)`
        """
        return "AnimationMessage(animation={self.animation!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, duration={self.duration!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in animationmessage_instance`
        """
        return (
            key in ["animation", "receiver", "reply_id", "duration", "width", "height", "thumb", "caption", "parse_mode", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class AnimationMessage

class VoiceMessage(SendableMessageBase):
    """
    Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#sendvoice

    
    Parameters:
    
    :param voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :type  voice: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param caption: Voice message caption, 0-1024 characters after entities parsing
    :type  caption: str|unicode
    
    :param parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.
    :type  parse_mode: str|unicode
    
    :param duration: Duration of the voice message in seconds
    :type  duration: int
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, voice, receiver=None, reply_id=DEFAULT_MESSAGE_ID, caption=None, parse_mode=None, duration=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendvoice

        
        Parameters:
        
        :param voice: Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
        :type  voice: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param caption: Voice message caption, 0-1024 characters after entities parsing
        :type  caption: str|unicode
        
        :param parse_mode: Mode for parsing entities in the voice message caption. See formatting options for more details.
        :type  parse_mode: str|unicode
        
        :param duration: Duration of the voice message in seconds
        :type  duration: int
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(VoiceMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(voice, InputFile, unicode_type, parameter_name="voice")
        self.voice = voice
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        
        assert_type_or_raise(parse_mode, None, unicode_type, parameter_name="parse_mode")
        self.parse_mode = parse_mode
        
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_voice(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            voice=self.voice, chat_id=self.receiver, reply_to_message_id=self.reply_id, caption=self.caption, parse_mode=self.parse_mode, duration=self.duration, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this VoiceMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(VoiceMessage, self).to_array()
        if isinstance(self.voice, InputFile):
            array['voice'] = self.voice.to_array()  # type InputFile
        elif isinstance(self.voice, str):
            array['voice'] = u(self.voice)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        if self.parse_mode is not None:
            array['parse_mode'] = u(self.parse_mode)  # py2: type unicode, py3: type str
        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VoiceMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('voice'), InputFile):
            data['voice'] = InputFile.from_array(array.get('voice'))
        elif isinstance(array.get('voice'), str):
            data['voice'] = u(array.get('voice'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['parse_mode'] = u(array.get('parse_mode')) if array.get('parse_mode') is not None else None
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VoiceMessage from a given dictionary.

        :return: new VoiceMessage instance.
        :rtype: VoiceMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = VoiceMessage.validate_array(array)
        return VoiceMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voicemessage_instance)`
        """
        return "VoiceMessage(voice={self.voice!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, duration={self.duration!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(voicemessage_instance)`
        """
        return "VoiceMessage(voice={self.voice!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, caption={self.caption!r}, parse_mode={self.parse_mode!r}, duration={self.duration!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in voicemessage_instance`
        """
        return (
            key in ["voice", "receiver", "reply_id", "caption", "parse_mode", "duration", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VoiceMessage

class VideoNoteMessage(SendableMessageBase):
    """
    As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendvideonote

    
    Parameters:
    
    :param video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files ». Sending video notes by a URL is currently unsupported
    :type  video_note: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param duration: Duration of sent video in seconds
    :type  duration: int
    
    :param length: Video width and height, i.e. diameter of the video message
    :type  length: int
    
    :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
    :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, video_note, receiver=None, reply_id=DEFAULT_MESSAGE_ID, duration=None, length=None, thumb=None, disable_notification=None, reply_markup=None):
        """
        As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendvideonote

        
        Parameters:
        
        :param video_note: Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files ». Sending video notes by a URL is currently unsupported
        :type  video_note: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param duration: Duration of sent video in seconds
        :type  duration: int
        
        :param length: Video width and height, i.e. diameter of the video message
        :type  length: int
        
        :param thumb: Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail‘s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can’t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »
        :type  thumb: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(VideoNoteMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(video_note, InputFile, unicode_type, parameter_name="video_note")
        self.video_note = video_note
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(duration, None, int, parameter_name="duration")
        self.duration = duration
        
        assert_type_or_raise(length, None, int, parameter_name="length")
        self.length = length
        
        assert_type_or_raise(thumb, None, InputFile, unicode_type, parameter_name="thumb")
        self.thumb = thumb
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_video_note(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            video_note=self.video_note, chat_id=self.receiver, reply_to_message_id=self.reply_id, duration=self.duration, length=self.length, thumb=self.thumb, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this VideoNoteMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(VideoNoteMessage, self).to_array()
        if isinstance(self.video_note, InputFile):
            array['video_note'] = self.video_note.to_array()  # type InputFile
        elif isinstance(self.video_note, str):
            array['video_note'] = u(self.video_note)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.duration is not None:
            array['duration'] = int(self.duration)  # type int
        if self.length is not None:
            array['length'] = int(self.length)  # type int
        if self.thumb is not None:
            if isinstance(self.thumb, InputFile):
                array['thumb'] = self.thumb.to_array()  # type InputFile
            elif isinstance(self.thumb, str):
                array['thumb'] = u(self.thumb)  # py2: type unicode, py3: type strelse:
                raise TypeError('Unknown type, must be one of InputFile, str.')
            # end if

        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VideoNoteMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('video_note'), InputFile):
            data['video_note'] = InputFile.from_array(array.get('video_note'))
        elif isinstance(array.get('video_note'), str):
            data['video_note'] = u(array.get('video_note'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['duration'] = int(array.get('duration')) if array.get('duration') is not None else None
        data['length'] = int(array.get('length')) if array.get('length') is not None else None
        if array.get('thumb') is None:
            data['thumb'] = None
        elif isinstance(array.get('thumb'), InputFile):
            data['thumb'] = InputFile.from_array(array.get('thumb'))
        elif isinstance(array.get('thumb'), str):
            data['thumb'] = u(array.get('thumb'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str or None.')
        # end if
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VideoNoteMessage from a given dictionary.

        :return: new VideoNoteMessage instance.
        :rtype: VideoNoteMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = VideoNoteMessage.validate_array(array)
        return VideoNoteMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(videonotemessage_instance)`
        """
        return "VideoNoteMessage(video_note={self.video_note!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, duration={self.duration!r}, length={self.length!r}, thumb={self.thumb!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(videonotemessage_instance)`
        """
        return "VideoNoteMessage(video_note={self.video_note!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, duration={self.duration!r}, length={self.length!r}, thumb={self.thumb!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in videonotemessage_instance`
        """
        return (
            key in ["video_note", "receiver", "reply_id", "duration", "length", "thumb", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VideoNoteMessage

class MediaGroupMessage(SendableMessageBase):
    """
    Use this method to send a group of photos or videos as an album. On success, an array of the sent Messages is returned.

    https://core.telegram.org/bots/api#sendmediagroup

    
    Parameters:
    
    :param media: A JSON-serialized array describing photos and videos to be sent, must include 2-10 items
    :type  media: list of pytgbot.api_types.sendable.input_media.InputMediaPhoto | list of pytgbot.api_types.sendable.input_media.InputMediaVideo
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param disable_notification: Sends the messages silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    """

    def __init__(self, media, receiver=None, reply_id=DEFAULT_MESSAGE_ID, disable_notification=None):
        """
        Use this method to send a group of photos or videos as an album. On success, an array of the sent Messages is returned.

        https://core.telegram.org/bots/api#sendmediagroup

        
        Parameters:
        
        :param media: A JSON-serialized array describing photos and videos to be sent, must include 2-10 items
        :type  media: list of pytgbot.api_types.sendable.input_media.InputMediaPhoto | list of pytgbot.api_types.sendable.input_media.InputMediaVideo
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param disable_notification: Sends the messages silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        """
        super(MediaGroupMessage, self).__init__()
        from pytgbot.api_types.sendable.input_media import InputMediaPhoto
        from pytgbot.api_types.sendable.input_media import InputMediaVideo
        
        assert_type_or_raise(media, list, list, parameter_name="media")
        self.media = media
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_media_group(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            media=self.media, chat_id=self.receiver, reply_to_message_id=self.reply_id, disable_notification=self.disable_notification
        )
    # end def send

    def to_array(self):
        """
        Serializes this MediaGroupMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(MediaGroupMessage, self).to_array()
        if isinstance(self.media, InputMediaPhoto):
            array['media'] = self._as_array(self.media)  # type list of InputMediaPhoto | list of InputMediaVideo
        elif isinstance(self.media, InputMediaVideo):
            array['media'] = self._as_array(self.media)  # type list of InputMediaPhoto | list of InputMediaVideo
        else:
            raise TypeError('Unknown type, must be one of InputMediaPhoto, InputMediaVideo.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the MediaGroupMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.input_media import InputMediaPhoto
        from pytgbot.api_types.sendable.input_media import InputMediaVideo
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('media'), InputMediaPhoto):
            data['media'] = InputMediaPhoto.from_array_list(array.get('media'), list_level=1)
        elif isinstance(array.get('media'), InputMediaVideo):
            data['media'] = InputMediaVideo.from_array_list(array.get('media'), list_level=1)
        else:
            raise TypeError('Unknown type, must be one of InputMediaPhoto, InputMediaVideo.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new MediaGroupMessage from a given dictionary.

        :return: new MediaGroupMessage instance.
        :rtype: MediaGroupMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = MediaGroupMessage.validate_array(array)
        return MediaGroupMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(mediagroupmessage_instance)`
        """
        return "MediaGroupMessage(media={self.media!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, disable_notification={self.disable_notification!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(mediagroupmessage_instance)`
        """
        return "MediaGroupMessage(media={self.media!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, disable_notification={self.disable_notification!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in mediagroupmessage_instance`
        """
        return (
            key in ["media", "receiver", "reply_id", "disable_notification"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class MediaGroupMessage

class LocationMessage(SendableMessageBase):
    """
    Use this method to send point on the map. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendlocation

    
    Parameters:
    
    :param latitude: Latitude of the location
    :type  latitude: float
    
    :param longitude: Longitude of the location
    :type  longitude: float
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param live_period: Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.
    :type  live_period: int
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, latitude, longitude, receiver=None, reply_id=DEFAULT_MESSAGE_ID, live_period=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendlocation

        
        Parameters:
        
        :param latitude: Latitude of the location
        :type  latitude: float
        
        :param longitude: Longitude of the location
        :type  longitude: float
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param live_period: Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.
        :type  live_period: int
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(LocationMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(live_period, None, int, parameter_name="live_period")
        self.live_period = live_period
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_location(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            latitude=self.latitude, longitude=self.longitude, chat_id=self.receiver, reply_to_message_id=self.reply_id, live_period=self.live_period, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this LocationMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(LocationMessage, self).to_array()
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.live_period is not None:
            array['live_period'] = int(self.live_period)  # type int
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the LocationMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['live_period'] = int(array.get('live_period')) if array.get('live_period') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new LocationMessage from a given dictionary.

        :return: new LocationMessage instance.
        :rtype: LocationMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = LocationMessage.validate_array(array)
        return LocationMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(locationmessage_instance)`
        """
        return "LocationMessage(latitude={self.latitude!r}, longitude={self.longitude!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, live_period={self.live_period!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(locationmessage_instance)`
        """
        return "LocationMessage(latitude={self.latitude!r}, longitude={self.longitude!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, live_period={self.live_period!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in locationmessage_instance`
        """
        return (
            key in ["latitude", "longitude", "receiver", "reply_id", "live_period", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class LocationMessage

class VenueMessage(SendableMessageBase):
    """
    Use this method to send information about a venue. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendvenue

    
    Parameters:
    
    :param latitude: Latitude of the venue
    :type  latitude: float
    
    :param longitude: Longitude of the venue
    :type  longitude: float
    
    :param title: Name of the venue
    :type  title: str|unicode
    
    :param address: Address of the venue
    :type  address: str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param foursquare_id: Foursquare identifier of the venue
    :type  foursquare_id: str|unicode
    
    :param foursquare_type: Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
    :type  foursquare_type: str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, latitude, longitude, title, address, receiver=None, reply_id=DEFAULT_MESSAGE_ID, foursquare_id=None, foursquare_type=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendvenue

        
        Parameters:
        
        :param latitude: Latitude of the venue
        :type  latitude: float
        
        :param longitude: Longitude of the venue
        :type  longitude: float
        
        :param title: Name of the venue
        :type  title: str|unicode
        
        :param address: Address of the venue
        :type  address: str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param foursquare_id: Foursquare identifier of the venue
        :type  foursquare_id: str|unicode
        
        :param foursquare_type: Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)
        :type  foursquare_type: str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(VenueMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(latitude, float, parameter_name="latitude")
        self.latitude = latitude
        
        assert_type_or_raise(longitude, float, parameter_name="longitude")
        self.longitude = longitude
        
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        
        assert_type_or_raise(address, unicode_type, parameter_name="address")
        self.address = address
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(foursquare_id, None, unicode_type, parameter_name="foursquare_id")
        self.foursquare_id = foursquare_id
        
        assert_type_or_raise(foursquare_type, None, unicode_type, parameter_name="foursquare_type")
        self.foursquare_type = foursquare_type
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_venue(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            latitude=self.latitude, longitude=self.longitude, title=self.title, address=self.address, chat_id=self.receiver, reply_to_message_id=self.reply_id, foursquare_id=self.foursquare_id, foursquare_type=self.foursquare_type, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this VenueMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(VenueMessage, self).to_array()
        array['latitude'] = float(self.latitude)  # type float
        array['longitude'] = float(self.longitude)  # type float
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['address'] = u(self.address)  # py2: type unicode, py3: type str
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.foursquare_id is not None:
            array['foursquare_id'] = u(self.foursquare_id)  # py2: type unicode, py3: type str
        if self.foursquare_type is not None:
            array['foursquare_type'] = u(self.foursquare_type)  # py2: type unicode, py3: type str
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VenueMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        data['latitude'] = float(array.get('latitude'))
        data['longitude'] = float(array.get('longitude'))
        data['title'] = u(array.get('title'))
        data['address'] = u(array.get('address'))
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['foursquare_id'] = u(array.get('foursquare_id')) if array.get('foursquare_id') is not None else None
        data['foursquare_type'] = u(array.get('foursquare_type')) if array.get('foursquare_type') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VenueMessage from a given dictionary.

        :return: new VenueMessage instance.
        :rtype: VenueMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = VenueMessage.validate_array(array)
        return VenueMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(venuemessage_instance)`
        """
        return "VenueMessage(latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(venuemessage_instance)`
        """
        return "VenueMessage(latitude={self.latitude!r}, longitude={self.longitude!r}, title={self.title!r}, address={self.address!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, foursquare_id={self.foursquare_id!r}, foursquare_type={self.foursquare_type!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in venuemessage_instance`
        """
        return (
            key in ["latitude", "longitude", "title", "address", "receiver", "reply_id", "foursquare_id", "foursquare_type", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VenueMessage

class ContactMessage(SendableMessageBase):
    """
    Use this method to send phone contacts. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendcontact

    
    Parameters:
    
    :param phone_number: Contact's phone number
    :type  phone_number: str|unicode
    
    :param first_name: Contact's first name
    :type  first_name: str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param last_name: Contact's last name
    :type  last_name: str|unicode
    
    :param vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes
    :type  vcard: str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, phone_number, first_name, receiver=None, reply_id=DEFAULT_MESSAGE_ID, last_name=None, vcard=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendcontact

        
        Parameters:
        
        :param phone_number: Contact's phone number
        :type  phone_number: str|unicode
        
        :param first_name: Contact's first name
        :type  first_name: str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param last_name: Contact's last name
        :type  last_name: str|unicode
        
        :param vcard: Additional data about the contact in the form of a vCard, 0-2048 bytes
        :type  vcard: str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(ContactMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(phone_number, unicode_type, parameter_name="phone_number")
        self.phone_number = phone_number
        
        assert_type_or_raise(first_name, unicode_type, parameter_name="first_name")
        self.first_name = first_name
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(last_name, None, unicode_type, parameter_name="last_name")
        self.last_name = last_name
        
        assert_type_or_raise(vcard, None, unicode_type, parameter_name="vcard")
        self.vcard = vcard
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_contact(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            phone_number=self.phone_number, first_name=self.first_name, chat_id=self.receiver, reply_to_message_id=self.reply_id, last_name=self.last_name, vcard=self.vcard, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this ContactMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(ContactMessage, self).to_array()
        array['phone_number'] = u(self.phone_number)  # py2: type unicode, py3: type str
        array['first_name'] = u(self.first_name)  # py2: type unicode, py3: type str
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.last_name is not None:
            array['last_name'] = u(self.last_name)  # py2: type unicode, py3: type str
        if self.vcard is not None:
            array['vcard'] = u(self.vcard)  # py2: type unicode, py3: type str
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ContactMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        data['phone_number'] = u(array.get('phone_number'))
        data['first_name'] = u(array.get('first_name'))
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['last_name'] = u(array.get('last_name')) if array.get('last_name') is not None else None
        data['vcard'] = u(array.get('vcard')) if array.get('vcard') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ContactMessage from a given dictionary.

        :return: new ContactMessage instance.
        :rtype: ContactMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = ContactMessage.validate_array(array)
        return ContactMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(contactmessage_instance)`
        """
        return "ContactMessage(phone_number={self.phone_number!r}, first_name={self.first_name!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, last_name={self.last_name!r}, vcard={self.vcard!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(contactmessage_instance)`
        """
        return "ContactMessage(phone_number={self.phone_number!r}, first_name={self.first_name!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, last_name={self.last_name!r}, vcard={self.vcard!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in contactmessage_instance`
        """
        return (
            key in ["phone_number", "first_name", "receiver", "reply_id", "last_name", "vcard", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ContactMessage

class PollMessage(SendableMessageBase):
    """
    Use this method to send a native poll. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendpoll

    
    Parameters:
    
    :param question: Poll question, 1-255 characters
    :type  question: str|unicode
    
    :param options: A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
    :type  options: list of str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
    :type  is_anonymous: bool
    
    :param type: Poll type, "quiz" or "regular", defaults to "regular"
    :type  type: str|unicode
    
    :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
    :type  allows_multiple_answers: bool
    
    :param correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode
    :type  correct_option_id: int
    
    :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
    :type  explanation: str|unicode
    
    :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.
    :type  explanation_parse_mode: str|unicode
    
    :param open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
    :type  open_period: int
    
    :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
    :type  close_date: int
    
    :param is_closed: Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
    :type  is_closed: bool
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, question, options, receiver=None, reply_id=DEFAULT_MESSAGE_ID, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, open_period=None, close_date=None, is_closed=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send a native poll. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendpoll

        
        Parameters:
        
        :param question: Poll question, 1-255 characters
        :type  question: str|unicode
        
        :param options: A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
        :type  options: list of str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param is_anonymous: True, if the poll needs to be anonymous, defaults to True
        :type  is_anonymous: bool
        
        :param type: Poll type, "quiz" or "regular", defaults to "regular"
        :type  type: str|unicode
        
        :param allows_multiple_answers: True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False
        :type  allows_multiple_answers: bool
        
        :param correct_option_id: 0-based identifier of the correct answer option, required for polls in quiz mode
        :type  correct_option_id: int
        
        :param explanation: Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
        :type  explanation: str|unicode
        
        :param explanation_parse_mode: Mode for parsing entities in the explanation. See formatting options for more details.
        :type  explanation_parse_mode: str|unicode
        
        :param open_period: Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date.
        :type  open_period: int
        
        :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period.
        :type  close_date: int
        
        :param is_closed: Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.
        :type  is_closed: bool
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(PollMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(question, unicode_type, parameter_name="question")
        self.question = question
        
        assert_type_or_raise(options, list, parameter_name="options")
        self.options = options
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(is_anonymous, None, bool, parameter_name="is_anonymous")
        self.is_anonymous = is_anonymous
        
        assert_type_or_raise(type, None, unicode_type, parameter_name="type")
        self.type = type
        
        assert_type_or_raise(allows_multiple_answers, None, bool, parameter_name="allows_multiple_answers")
        self.allows_multiple_answers = allows_multiple_answers
        
        assert_type_or_raise(correct_option_id, None, int, parameter_name="correct_option_id")
        self.correct_option_id = correct_option_id
        
        assert_type_or_raise(explanation, None, unicode_type, parameter_name="explanation")
        self.explanation = explanation
        
        assert_type_or_raise(explanation_parse_mode, None, unicode_type, parameter_name="explanation_parse_mode")
        self.explanation_parse_mode = explanation_parse_mode
        
        assert_type_or_raise(open_period, None, int, parameter_name="open_period")
        self.open_period = open_period
        
        assert_type_or_raise(close_date, None, int, parameter_name="close_date")
        self.close_date = close_date
        
        assert_type_or_raise(is_closed, None, bool, parameter_name="is_closed")
        self.is_closed = is_closed
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_poll(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            question=self.question, options=self.options, chat_id=self.receiver, reply_to_message_id=self.reply_id, is_anonymous=self.is_anonymous, type=self.type, allows_multiple_answers=self.allows_multiple_answers, correct_option_id=self.correct_option_id, explanation=self.explanation, explanation_parse_mode=self.explanation_parse_mode, open_period=self.open_period, close_date=self.close_date, is_closed=self.is_closed, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this PollMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(PollMessage, self).to_array()
        array['question'] = u(self.question)  # py2: type unicode, py3: type str
        array['options'] = self._as_array(self.options)  # type list of str

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.is_anonymous is not None:
            array['is_anonymous'] = bool(self.is_anonymous)  # type bool
        if self.type is not None:
            array['type'] = u(self.type)  # py2: type unicode, py3: type str
        if self.allows_multiple_answers is not None:
            array['allows_multiple_answers'] = bool(self.allows_multiple_answers)  # type bool
        if self.correct_option_id is not None:
            array['correct_option_id'] = int(self.correct_option_id)  # type int
        if self.explanation is not None:
            array['explanation'] = u(self.explanation)  # py2: type unicode, py3: type str
        if self.explanation_parse_mode is not None:
            array['explanation_parse_mode'] = u(self.explanation_parse_mode)  # py2: type unicode, py3: type str
        if self.open_period is not None:
            array['open_period'] = int(self.open_period)  # type int
        if self.close_date is not None:
            array['close_date'] = int(self.close_date)  # type int
        if self.is_closed is not None:
            array['is_closed'] = bool(self.is_closed)  # type bool
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PollMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        data['question'] = u(array.get('question'))
        data['options'] = PollMessage._builtin_from_array_list(required_type=unicode_type, value=array.get('options'), list_level=1)
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['is_anonymous'] = bool(array.get('is_anonymous')) if array.get('is_anonymous') is not None else None
        data['type'] = u(array.get('type')) if array.get('type') is not None else None
        data['allows_multiple_answers'] = bool(array.get('allows_multiple_answers')) if array.get('allows_multiple_answers') is not None else None
        data['correct_option_id'] = int(array.get('correct_option_id')) if array.get('correct_option_id') is not None else None
        data['explanation'] = u(array.get('explanation')) if array.get('explanation') is not None else None
        data['explanation_parse_mode'] = u(array.get('explanation_parse_mode')) if array.get('explanation_parse_mode') is not None else None
        data['open_period'] = int(array.get('open_period')) if array.get('open_period') is not None else None
        data['close_date'] = int(array.get('close_date')) if array.get('close_date') is not None else None
        data['is_closed'] = bool(array.get('is_closed')) if array.get('is_closed') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PollMessage from a given dictionary.

        :return: new PollMessage instance.
        :rtype: PollMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = PollMessage.validate_array(array)
        return PollMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(pollmessage_instance)`
        """
        return "PollMessage(question={self.question!r}, options={self.options!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, is_anonymous={self.is_anonymous!r}, type={self.type!r}, allows_multiple_answers={self.allows_multiple_answers!r}, correct_option_id={self.correct_option_id!r}, explanation={self.explanation!r}, explanation_parse_mode={self.explanation_parse_mode!r}, open_period={self.open_period!r}, close_date={self.close_date!r}, is_closed={self.is_closed!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(pollmessage_instance)`
        """
        return "PollMessage(question={self.question!r}, options={self.options!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, is_anonymous={self.is_anonymous!r}, type={self.type!r}, allows_multiple_answers={self.allows_multiple_answers!r}, correct_option_id={self.correct_option_id!r}, explanation={self.explanation!r}, explanation_parse_mode={self.explanation_parse_mode!r}, open_period={self.open_period!r}, close_date={self.close_date!r}, is_closed={self.is_closed!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in pollmessage_instance`
        """
        return (
            key in ["question", "options", "receiver", "reply_id", "is_anonymous", "type", "allows_multiple_answers", "correct_option_id", "explanation", "explanation_parse_mode", "open_period", "close_date", "is_closed", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class PollMessage

class DiceMessage(SendableMessageBase):
    """
    Use this method to send a dice, which will have a random value from 1 to 6. On success, the sent Message is returned. (Yes, we're aware of the "proper" singular of die. But it's awkward, and we decided to help it change. One dice at a time!)

    https://core.telegram.org/bots/api#senddice

    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param emoji: Emoji on which the dice throw animation is based. Currently, must be one of "" or "". Defauts to ""
    :type  emoji: str|unicode
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, receiver=None, reply_id=DEFAULT_MESSAGE_ID, emoji=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send a dice, which will have a random value from 1 to 6. On success, the sent Message is returned. (Yes, we're aware of the "proper" singular of die. But it's awkward, and we decided to help it change. One dice at a time!)

        https://core.telegram.org/bots/api#senddice

        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param emoji: Emoji on which the dice throw animation is based. Currently, must be one of "" or "". Defauts to ""
        :type  emoji: str|unicode
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(DiceMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(emoji, None, unicode_type, parameter_name="emoji")
        self.emoji = emoji
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_dice(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            chat_id=self.receiver, reply_to_message_id=self.reply_id, emoji=self.emoji, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this DiceMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(DiceMessage, self).to_array()
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.emoji is not None:
            array['emoji'] = u(self.emoji)  # py2: type unicode, py3: type str
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the DiceMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['emoji'] = u(array.get('emoji')) if array.get('emoji') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new DiceMessage from a given dictionary.

        :return: new DiceMessage instance.
        :rtype: DiceMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = DiceMessage.validate_array(array)
        return DiceMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(dicemessage_instance)`
        """
        return "DiceMessage(receiver={self.receiver!r}, reply_id={self.reply_id!r}, emoji={self.emoji!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(dicemessage_instance)`
        """
        return "DiceMessage(receiver={self.receiver!r}, reply_id={self.reply_id!r}, emoji={self.emoji!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in dicemessage_instance`
        """
        return (
            key in ["receiver", "reply_id", "emoji", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class DiceMessage

class ChatActionMessage(SendableMessageBase):
    """
    Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.

        Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of "Retrieving image, please wait…", the bot may use sendChatAction with action = upload_photo. The user will see a "sending photo" status for the bot.

        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

    https://core.telegram.org/bots/api#sendchataction

    
    Parameters:
    
    :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data, record_video_note or upload_video_note for video notes.
    :type  action: str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    """

    def __init__(self, action, receiver=None):
        """
        Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.

            Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of "Retrieving image, please wait…", the bot may use sendChatAction with action = upload_photo. The user will see a "sending photo" status for the bot.

            We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

        https://core.telegram.org/bots/api#sendchataction

        
        Parameters:
        
        :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data, record_video_note or upload_video_note for video notes.
        :type  action: str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        """
        super(ChatActionMessage, self).__init__()
        assert_type_or_raise(action, unicode_type, parameter_name="action")
        self.action = action
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_chat_action(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            action=self.action, chat_id=self.receiver
        )
    # end def send

    def to_array(self):
        """
        Serializes this ChatActionMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(ChatActionMessage, self).to_array()
        array['action'] = u(self.action)  # py2: type unicode, py3: type str
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ChatActionMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = SendableMessageBase.validate_array(array)
        data['action'] = u(array.get('action'))
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ChatActionMessage from a given dictionary.

        :return: new ChatActionMessage instance.
        :rtype: ChatActionMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = ChatActionMessage.validate_array(array)
        return ChatActionMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(chatactionmessage_instance)`
        """
        return "ChatActionMessage(action={self.action!r}, receiver={self.receiver!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(chatactionmessage_instance)`
        """
        return "ChatActionMessage(action={self.action!r}, receiver={self.receiver!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in chatactionmessage_instance`
        """
        return (
            key in ["action", "receiver"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ChatActionMessage

class StickerMessage(SendableMessageBase):
    """
    Use this method to send static .WEBP or animated .TGS stickers. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendsticker

    
    Parameters:
    
    :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
    :type  sticker: pytgbot.api_types.sendable.files.InputFile | str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
    
    """

    def __init__(self, sticker, receiver=None, reply_id=DEFAULT_MESSAGE_ID, disable_notification=None, reply_markup=None):
        """
        Use this method to send static .WEBP or animated .TGS stickers. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendsticker

        
        Parameters:
        
        :param sticker: Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »
        :type  sticker: pytgbot.api_types.sendable.files.InputFile | str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardRemove | pytgbot.api_types.sendable.reply_markup.ForceReply
        
        """
        super(StickerMessage, self).__init__()
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        assert_type_or_raise(sticker, InputFile, unicode_type, parameter_name="sticker")
        self.sticker = sticker
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_sticker(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            sticker=self.sticker, chat_id=self.receiver, reply_to_message_id=self.reply_id, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this StickerMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(StickerMessage, self).to_array()
        if isinstance(self.sticker, InputFile):
            array['sticker'] = self.sticker.to_array()  # type InputFile
        elif isinstance(self.sticker, str):
            array['sticker'] = u(self.sticker)  # py2: type unicode, py3: type strelse:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            if isinstance(self.reply_markup, InlineKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardMarkup):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardMarkup
            elif isinstance(self.reply_markup, ReplyKeyboardRemove):
                array['reply_markup'] = self.reply_markup.to_array()  # type ReplyKeyboardRemove
            elif isinstance(self.reply_markup, ForceReply):
                array['reply_markup'] = self.reply_markup.to_array()  # type ForceReply
            else:
                raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply.')
            # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the StickerMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
        
        data = SendableMessageBase.validate_array(array)
        if isinstance(array.get('sticker'), InputFile):
            data['sticker'] = InputFile.from_array(array.get('sticker'))
        elif isinstance(array.get('sticker'), str):
            data['sticker'] = u(array.get('sticker'))
        else:
            raise TypeError('Unknown type, must be one of InputFile, str.')
        # end if
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        if array.get('reply_markup') is None:
            data['reply_markup'] = None
        elif isinstance(array.get('reply_markup'), InlineKeyboardMarkup):
            data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardMarkup):
            data['reply_markup'] = ReplyKeyboardMarkup.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ReplyKeyboardRemove):
            data['reply_markup'] = ReplyKeyboardRemove.from_array(array.get('reply_markup'))
        elif isinstance(array.get('reply_markup'), ForceReply):
            data['reply_markup'] = ForceReply.from_array(array.get('reply_markup'))
        else:
            raise TypeError('Unknown type, must be one of InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply or None.')
        # end if
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new StickerMessage from a given dictionary.

        :return: new StickerMessage instance.
        :rtype: StickerMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = StickerMessage.validate_array(array)
        return StickerMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(stickermessage_instance)`
        """
        return "StickerMessage(sticker={self.sticker!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(stickermessage_instance)`
        """
        return "StickerMessage(sticker={self.sticker!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in stickermessage_instance`
        """
        return (
            key in ["sticker", "receiver", "reply_id", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class StickerMessage

class InvoiceMessage(SendableMessageBase):
    """
    Use this method to send invoices. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendinvoice

    
    Parameters:
    
    :param title: Product name, 1-32 characters
    :type  title: str|unicode
    
    :param description: Product description, 1-255 characters
    :type  description: str|unicode
    
    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    :type  payload: str|unicode
    
    :param provider_token: Payments provider token, obtained via Botfather
    :type  provider_token: str|unicode
    
    :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter
    :type  start_parameter: str|unicode
    
    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :type  currency: str|unicode
    
    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    :type  prices: list of pytgbot.api_types.sendable.payments.LabeledPrice
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param provider_data: JSON-encoded data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
    :type  provider_data: str|unicode
    
    :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    :type  photo_url: str|unicode
    
    :param photo_size: Photo size
    :type  photo_size: int
    
    :param photo_width: Photo width
    :type  photo_width: int
    
    :param photo_height: Photo height
    :type  photo_height: int
    
    :param need_name: Pass True, if you require the user's full name to complete the order
    :type  need_name: bool
    
    :param need_phone_number: Pass True, if you require the user's phone number to complete the order
    :type  need_phone_number: bool
    
    :param need_email: Pass True, if you require the user's email address to complete the order
    :type  need_email: bool
    
    :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
    :type  need_shipping_address: bool
    
    :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
    :type  send_phone_number_to_provider: bool
    
    :param send_email_to_provider: Pass True, if user's email address should be sent to provider
    :type  send_email_to_provider: bool
    
    :param is_flexible: Pass True, if the final price depends on the shipping method
    :type  is_flexible: bool
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
    
    """

    def __init__(self, title, description, payload, provider_token, start_parameter, currency, prices, receiver=None, reply_id=DEFAULT_MESSAGE_ID, provider_data=None, photo_url=None, photo_size=None, photo_width=None, photo_height=None, need_name=None, need_phone_number=None, need_email=None, need_shipping_address=None, send_phone_number_to_provider=None, send_email_to_provider=None, is_flexible=None, disable_notification=None, reply_markup=None):
        """
        Use this method to send invoices. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendinvoice

        
        Parameters:
        
        :param title: Product name, 1-32 characters
        :type  title: str|unicode
        
        :param description: Product description, 1-255 characters
        :type  description: str|unicode
        
        :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
        :type  payload: str|unicode
        
        :param provider_token: Payments provider token, obtained via Botfather
        :type  provider_token: str|unicode
        
        :param start_parameter: Unique deep-linking parameter that can be used to generate this invoice when used as a start parameter
        :type  start_parameter: str|unicode
        
        :param currency: Three-letter ISO 4217 currency code, see more on currencies
        :type  currency: str|unicode
        
        :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
        :type  prices: list of pytgbot.api_types.sendable.payments.LabeledPrice
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param provider_data: JSON-encoded data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
        :type  provider_data: str|unicode
        
        :param photo_url: URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
        :type  photo_url: str|unicode
        
        :param photo_size: Photo size
        :type  photo_size: int
        
        :param photo_width: Photo width
        :type  photo_width: int
        
        :param photo_height: Photo height
        :type  photo_height: int
        
        :param need_name: Pass True, if you require the user's full name to complete the order
        :type  need_name: bool
        
        :param need_phone_number: Pass True, if you require the user's phone number to complete the order
        :type  need_phone_number: bool
        
        :param need_email: Pass True, if you require the user's email address to complete the order
        :type  need_email: bool
        
        :param need_shipping_address: Pass True, if you require the user's shipping address to complete the order
        :type  need_shipping_address: bool
        
        :param send_phone_number_to_provider: Pass True, if user's phone number should be sent to provider
        :type  send_phone_number_to_provider: bool
        
        :param send_email_to_provider: Pass True, if user's email address should be sent to provider
        :type  send_email_to_provider: bool
        
        :param is_flexible: Pass True, if the final price depends on the shipping method
        :type  is_flexible: bool
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
        
        """
        super(InvoiceMessage, self).__init__()
        from pytgbot.api_types.sendable.payments import LabeledPrice
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        
        assert_type_or_raise(description, unicode_type, parameter_name="description")
        self.description = description
        
        assert_type_or_raise(payload, unicode_type, parameter_name="payload")
        self.payload = payload
        
        assert_type_or_raise(provider_token, unicode_type, parameter_name="provider_token")
        self.provider_token = provider_token
        
        assert_type_or_raise(start_parameter, unicode_type, parameter_name="start_parameter")
        self.start_parameter = start_parameter
        
        assert_type_or_raise(currency, unicode_type, parameter_name="currency")
        self.currency = currency
        
        assert_type_or_raise(prices, list, parameter_name="prices")
        self.prices = prices
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(provider_data, None, unicode_type, parameter_name="provider_data")
        self.provider_data = provider_data
        
        assert_type_or_raise(photo_url, None, unicode_type, parameter_name="photo_url")
        self.photo_url = photo_url
        
        assert_type_or_raise(photo_size, None, int, parameter_name="photo_size")
        self.photo_size = photo_size
        
        assert_type_or_raise(photo_width, None, int, parameter_name="photo_width")
        self.photo_width = photo_width
        
        assert_type_or_raise(photo_height, None, int, parameter_name="photo_height")
        self.photo_height = photo_height
        
        assert_type_or_raise(need_name, None, bool, parameter_name="need_name")
        self.need_name = need_name
        
        assert_type_or_raise(need_phone_number, None, bool, parameter_name="need_phone_number")
        self.need_phone_number = need_phone_number
        
        assert_type_or_raise(need_email, None, bool, parameter_name="need_email")
        self.need_email = need_email
        
        assert_type_or_raise(need_shipping_address, None, bool, parameter_name="need_shipping_address")
        self.need_shipping_address = need_shipping_address
        
        assert_type_or_raise(send_phone_number_to_provider, None, bool, parameter_name="send_phone_number_to_provider")
        self.send_phone_number_to_provider = send_phone_number_to_provider
        
        assert_type_or_raise(send_email_to_provider, None, bool, parameter_name="send_email_to_provider")
        self.send_email_to_provider = send_email_to_provider
        
        assert_type_or_raise(is_flexible, None, bool, parameter_name="is_flexible")
        self.is_flexible = is_flexible
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_invoice(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            title=self.title, description=self.description, payload=self.payload, provider_token=self.provider_token, start_parameter=self.start_parameter, currency=self.currency, prices=self.prices, chat_id=self.receiver, reply_to_message_id=self.reply_id, provider_data=self.provider_data, photo_url=self.photo_url, photo_size=self.photo_size, photo_width=self.photo_width, photo_height=self.photo_height, need_name=self.need_name, need_phone_number=self.need_phone_number, need_email=self.need_email, need_shipping_address=self.need_shipping_address, send_phone_number_to_provider=self.send_phone_number_to_provider, send_email_to_provider=self.send_email_to_provider, is_flexible=self.is_flexible, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this InvoiceMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(InvoiceMessage, self).to_array()
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['description'] = u(self.description)  # py2: type unicode, py3: type str
        array['payload'] = u(self.payload)  # py2: type unicode, py3: type str
        array['provider_token'] = u(self.provider_token)  # py2: type unicode, py3: type str
        array['start_parameter'] = u(self.start_parameter)  # py2: type unicode, py3: type str
        array['currency'] = u(self.currency)  # py2: type unicode, py3: type str
        array['prices'] = self._as_array(self.prices)  # type list of LabeledPrice

        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.provider_data is not None:
            array['provider_data'] = u(self.provider_data)  # py2: type unicode, py3: type str
        if self.photo_url is not None:
            array['photo_url'] = u(self.photo_url)  # py2: type unicode, py3: type str
        if self.photo_size is not None:
            array['photo_size'] = int(self.photo_size)  # type int
        if self.photo_width is not None:
            array['photo_width'] = int(self.photo_width)  # type int
        if self.photo_height is not None:
            array['photo_height'] = int(self.photo_height)  # type int
        if self.need_name is not None:
            array['need_name'] = bool(self.need_name)  # type bool
        if self.need_phone_number is not None:
            array['need_phone_number'] = bool(self.need_phone_number)  # type bool
        if self.need_email is not None:
            array['need_email'] = bool(self.need_email)  # type bool
        if self.need_shipping_address is not None:
            array['need_shipping_address'] = bool(self.need_shipping_address)  # type bool
        if self.send_phone_number_to_provider is not None:
            array['send_phone_number_to_provider'] = bool(self.send_phone_number_to_provider)  # type bool
        if self.send_email_to_provider is not None:
            array['send_email_to_provider'] = bool(self.send_email_to_provider)  # type bool
        if self.is_flexible is not None:
            array['is_flexible'] = bool(self.is_flexible)  # type bool
        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InvoiceMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.payments import LabeledPrice
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        
        data = SendableMessageBase.validate_array(array)
        data['title'] = u(array.get('title'))
        data['description'] = u(array.get('description'))
        data['payload'] = u(array.get('payload'))
        data['provider_token'] = u(array.get('provider_token'))
        data['start_parameter'] = u(array.get('start_parameter'))
        data['currency'] = u(array.get('currency'))
        data['prices'] = LabeledPrice.from_array_list(array.get('prices'), list_level=1)
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['provider_data'] = u(array.get('provider_data')) if array.get('provider_data') is not None else None
        data['photo_url'] = u(array.get('photo_url')) if array.get('photo_url') is not None else None
        data['photo_size'] = int(array.get('photo_size')) if array.get('photo_size') is not None else None
        data['photo_width'] = int(array.get('photo_width')) if array.get('photo_width') is not None else None
        data['photo_height'] = int(array.get('photo_height')) if array.get('photo_height') is not None else None
        data['need_name'] = bool(array.get('need_name')) if array.get('need_name') is not None else None
        data['need_phone_number'] = bool(array.get('need_phone_number')) if array.get('need_phone_number') is not None else None
        data['need_email'] = bool(array.get('need_email')) if array.get('need_email') is not None else None
        data['need_shipping_address'] = bool(array.get('need_shipping_address')) if array.get('need_shipping_address') is not None else None
        data['send_phone_number_to_provider'] = bool(array.get('send_phone_number_to_provider')) if array.get('send_phone_number_to_provider') is not None else None
        data['send_email_to_provider'] = bool(array.get('send_email_to_provider')) if array.get('send_email_to_provider') is not None else None
        data['is_flexible'] = bool(array.get('is_flexible')) if array.get('is_flexible') is not None else None
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InvoiceMessage from a given dictionary.

        :return: new InvoiceMessage instance.
        :rtype: InvoiceMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = InvoiceMessage.validate_array(array)
        return InvoiceMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(invoicemessage_instance)`
        """
        return "InvoiceMessage(title={self.title!r}, description={self.description!r}, payload={self.payload!r}, provider_token={self.provider_token!r}, start_parameter={self.start_parameter!r}, currency={self.currency!r}, prices={self.prices!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, provider_data={self.provider_data!r}, photo_url={self.photo_url!r}, photo_size={self.photo_size!r}, photo_width={self.photo_width!r}, photo_height={self.photo_height!r}, need_name={self.need_name!r}, need_phone_number={self.need_phone_number!r}, need_email={self.need_email!r}, need_shipping_address={self.need_shipping_address!r}, send_phone_number_to_provider={self.send_phone_number_to_provider!r}, send_email_to_provider={self.send_email_to_provider!r}, is_flexible={self.is_flexible!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(invoicemessage_instance)`
        """
        return "InvoiceMessage(title={self.title!r}, description={self.description!r}, payload={self.payload!r}, provider_token={self.provider_token!r}, start_parameter={self.start_parameter!r}, currency={self.currency!r}, prices={self.prices!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, provider_data={self.provider_data!r}, photo_url={self.photo_url!r}, photo_size={self.photo_size!r}, photo_width={self.photo_width!r}, photo_height={self.photo_height!r}, need_name={self.need_name!r}, need_phone_number={self.need_phone_number!r}, need_email={self.need_email!r}, need_shipping_address={self.need_shipping_address!r}, send_phone_number_to_provider={self.send_phone_number_to_provider!r}, send_email_to_provider={self.send_email_to_provider!r}, is_flexible={self.is_flexible!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in invoicemessage_instance`
        """
        return (
            key in ["title", "description", "payload", "provider_token", "start_parameter", "currency", "prices", "receiver", "reply_id", "provider_data", "photo_url", "photo_size", "photo_width", "photo_height", "need_name", "need_phone_number", "need_email", "need_shipping_address", "send_phone_number_to_provider", "send_email_to_provider", "is_flexible", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InvoiceMessage

class GameMessage(SendableMessageBase):
    """
    Use this method to send a game. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendgame

    
    Parameters:
    
    :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.
    :type  game_short_name: str|unicode
    
    
    Optional keyword parameters:
    
    :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
    :type  receiver: None | str|unicode | int
    
    :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
    :type  reply_id: DEFAULT_MESSAGE_ID | int
    
    :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
    :type  disable_notification: bool
    
    :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
    
    """

    def __init__(self, game_short_name, receiver=None, reply_id=DEFAULT_MESSAGE_ID, disable_notification=None, reply_markup=None):
        """
        Use this method to send a game. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendgame

        
        Parameters:
        
        :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.
        :type  game_short_name: str|unicode
        
        
        Optional keyword parameters:
        
        :param receiver: Set if you want to overwrite the receiver, which automatically is the chat_id in group chats, and the from_peer id in private conversations.
        :type  receiver: None | str|unicode | int
        
        :param reply_id: Set if you want to overwrite the `reply_to_message_id`, which automatically is the message triggering the bot.
        :type  reply_id: DEFAULT_MESSAGE_ID | int
        
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :type  disable_notification: bool
        
        :param reply_markup: A JSON-serialized object for an inline keyboard. If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup
        
        """
        super(GameMessage, self).__init__()
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        
        assert_type_or_raise(game_short_name, unicode_type, parameter_name="game_short_name")
        self.game_short_name = game_short_name
        
        assert_type_or_raise(receiver, None, None, unicode_type, int, parameter_name="receiver")
        self.receiver = receiver
        
        assert_type_or_raise(reply_id, None, DEFAULT_MESSAGE_ID, int, parameter_name="reply_id")
        self.reply_id = reply_id
        
        assert_type_or_raise(disable_notification, None, bool, parameter_name="disable_notification")
        self.disable_notification = disable_notification
        
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup
        self._next_msg = None
    # end def __init__

    @backoff.on_exception(backoff.expo, DoRetryException, max_tries=20, jitter=None)
    def send(self, sender: PytgbotApiBot):
        """
        Send the message via pytgbot.

        :param sender: The bot instance to send with.
        :type  sender: pytgbot.bot.Bot

        :rtype: PytgbotApiMessage
        """
        return sender.send_game(
            # receiver, self.media, disable_notification=self.disable_notification, reply_to_message_id=reply_id
            game_short_name=self.game_short_name, chat_id=self.receiver, reply_to_message_id=self.reply_id, disable_notification=self.disable_notification, reply_markup=self.reply_markup
        )
    # end def send

    def to_array(self):
        """
        Serializes this GameMessage to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(GameMessage, self).to_array()
        array['game_short_name'] = u(self.game_short_name)  # py2: type unicode, py3: type str
        if self.receiver is not None:
            if isinstance(self.receiver, None):
                array['chat_id'] = None
            elif isinstance(self.receiver, str):
                array['chat_id'] = u(self.receiver)  # py2: type unicode, py3: type strelif isinstance(self.receiver, int):
                array['chat_id'] = int(self.receiver)  # type intelse:
                raise TypeError('Unknown type, must be one of None, str, int.')
            # end if

        if self.reply_id is not None:
            if isinstance(self.reply_id, DEFAULT_MESSAGE_ID):
                array['reply_to_message_id'] = DEFAULT_MESSAGE_ID(self.reply_id)  # type DEFAULT_MESSAGE_IDelif isinstance(self.reply_id, int):
                array['reply_to_message_id'] = int(self.reply_id)  # type intelse:
                raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int.')
            # end if

        if self.disable_notification is not None:
            array['disable_notification'] = bool(self.disable_notification)  # type bool
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the GameMessage constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        
        data = SendableMessageBase.validate_array(array)
        data['game_short_name'] = u(array.get('game_short_name'))
        if array.get('chat_id') is None:
            data['receiver'] = None
        elif isinstance(array.get('chat_id'), None):
            data['receiver'] = None(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['receiver'] = u(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), int):
            data['receiver'] = int(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of None, str, int or None.')
        # end if
        if array.get('reply_to_message_id') is None:
            data['reply_id'] = None
        elif isinstance(array.get('reply_to_message_id'), DEFAULT_MESSAGE_ID):
            data['reply_id'] = DEFAULT_MESSAGE_ID(array.get('reply_to_message_id'))
        elif isinstance(array.get('reply_to_message_id'), int):
            data['reply_id'] = int(array.get('reply_to_message_id'))
        else:
            raise TypeError('Unknown type, must be one of DEFAULT_MESSAGE_ID, int or None.')
        # end if
        data['disable_notification'] = bool(array.get('disable_notification')) if array.get('disable_notification') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new GameMessage from a given dictionary.

        :return: new GameMessage instance.
        :rtype: GameMessage
        """
        if not array:  # None or {}
            return None
        # end if

        data = GameMessage.validate_array(array)
        return GameMessage(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(gamemessage_instance)`
        """
        return "GameMessage(game_short_name={self.game_short_name!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(gamemessage_instance)`
        """
        return "GameMessage(game_short_name={self.game_short_name!r}, receiver={self.receiver!r}, reply_id={self.reply_id!r}, disable_notification={self.disable_notification!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in gamemessage_instance`
        """
        return (
            key in ["game_short_name", "receiver", "reply_id", "disable_notification", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class GameMessage
