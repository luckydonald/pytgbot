# -*- coding: utf-8 -*-
import json
import requests
from time import sleep
from datetime import timedelta
from DictObject import DictObject

from luckydonaldUtils.encoding import to_native as n
from luckydonaldUtils.logger import logging

from .exceptions import TgApiServerException, TgApiParseException, TgApiTypeError, TgApiException
from .api_types.sendable.inline import InlineQueryResult
from .api_types import from_array_list


__author__ = 'luckydonald'
__all__ = ["Bot"]

logger = logging.getLogger(__name__)


class Bot(object):
    _base_url = "https://api.telegram.org/bot{api_key}/{command}"  # do not change.

    def __init__(self, api_key, return_python_objects=True):
        """
        A Bot instance. From here you can call all the functions.
        The api key can be optained from @BotFather, see https://core.telegram.org/bots#6-botfather

        :param api_key: The API key. Something like "ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
        :type  api_key: str

        :keyword return_python_objects: If it should convert the json to `pytgbot.api_types.**` objects.
        :type    return_python_objects: bool
        """
        from datetime import datetime

        if api_key is None or not api_key:
            raise ValueError("No api_key given.")
        self.api_key = api_key
        self.return_python_objects = return_python_objects
        self._last_update = datetime.now()
    # end def __init__

    def get_me(self):
        """
        A simple method for testing your bot's auth token. Requires no parameters.
        Returns basic information about the bot in form of a :class:`pytgbot.api_types.receivable.peer.User` object.

        https://core.telegram.org/bots/api#getme

        :return: Returns basic information about the bot in form of a User object.
        :rtype: User
        """
        result = self.do("getMe")
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.peer import User
            try:
                return User.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_me

    def get_updates(self, offset=None, limit=100, poll_timeout=0, request_timeout=None, delta=timedelta(milliseconds=100), error_as_empty=False):
        """
        Use this method to receive incoming updates using long polling. An Array of Update objects is returned.

        You can choose to set `error_as_empty` to `True` or `False`.
        If `error_as_empty` is set to `True`, it will log that exception as warning, and fake an empty result,
        intended for use in for loops. In case of such error (and only in such case) it contains an "exception" field.
        Ìt will look like this: `{"result": [], "exception": e}`
        This is useful if you want to use a for loop, but ignore Network related burps.

        If `error_as_empty` is set to `False` however, all `requests.RequestException` exceptions are normally raised.

        :keyword offset: (Optional)	Identifier of the first update to be returned.
                 Must be greater by one than the highest among the identifiers of previously received updates.
                 By default, updates starting with the earliest unconfirmed update are returned.
                 An update is considered confirmed as soon as :func:`get_updates` is called with
                 an offset higher than its `update_id`.
        :type offset: int

        :keyword limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100
        :type    limit: int

        :keyword poll_timeout: Timeout in seconds for long polling, e.g. how long we want to wait maximum.
                               Defaults to 0, i.e. usual short polling.
        :type    poll_timeout: int

        :keyword request_timeout: Timeout of the request. Not the long polling server side timeout.
                                  If not specified, it is set to `poll_timeout`+2.
        :type    request_timeout: int

        :keyword delta: Wait minimal 'delta' seconds, between requests. Useful in a loop.
        :type    delta: datetime.

        :keyword error_as_empty: If errors which subclasses `requests.RequestException` will be logged but not raised.
                 Instead the returned DictObject will contain an "exception" field containing the exception occured,
                 the "result" field will be an empty list `[]`. Defaults to `False`.
        :type error_as_empty: bool


        Returns:

        :return: An Array of Update objects is returned,
                 or an empty array if there was an requests.RequestException and error_as_empty is set to True.
        :rtype: list of pytgbot.api_types.receivable.updates.Update
        """
        from datetime import datetime

        assert(offset is None or isinstance(offset, int))
        assert(limit is None or isinstance(limit, int))
        assert(poll_timeout is None or isinstance(poll_timeout, int))
        if poll_timeout and not request_timeout is None:
            request_timeout = poll_timeout + 2
        # end if

        if delta.total_seconds() > poll_timeout:
            now = datetime.now()
            if self._last_update - now < delta:
                wait = ((now - self._last_update) - delta).total_seconds()  # can be 0.2
                wait = 0 if wait < 0 else wait
                if wait != 0:
                    logger.debug("Sleeping {i} seconds.".format(i=wait))
                # end if
                sleep(wait)
            # end if
        # end if
        self._last_update = datetime.now()
        try:
            result = self.do(
                "getUpdates", offset=offset, limit=limit, timeout=poll_timeout, use_long_polling=poll_timeout != 0,
                request_timeout=request_timeout
            )
            if self.return_python_objects:
                logger.debug("Trying to parse {data}".format(data=repr(result)))
                from pytgbot.api_types.receivable.updates import Update
                try:
                    return Update.from_array_list(result, 1)
                except TgApiParseException:
                    logger.debug("Failed parsing as api_type Update", exc_info=True)
                # end try
                # no valid parsing so far
                raise TgApiParseException("Could not parse result.")  # See debug log for details!
            # end if return_python_objects
            return result
        except (requests.RequestException, TgApiException) as e:
            if error_as_empty:
                logger.warn("Network related error happened in get_updates(), but will be ignored: " + str(e),
                            exc_info=True)
                self._last_update = datetime.now()
                return DictObject(result=[], exception=e)
            else:
                raise
    # end def get_updates

    def set_webhook(self, url=None, certificate=None):
        """
        Use this method to specify a url and receive incoming updates via an outgoing webhook.
        Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url,
        containing a JSON-serialized Update.
        In case of an unsuccessful request, we will give up after a reasonable amount of attempts.

        If you'd like to make sure that the Webhook request comes from Telegram,
        we recommend using a secret path in the URL, e.g. https://www.example.com/<token>.
        Since nobody else knows your bot‘s token, you can be pretty sure it’s us.

        Notes:

        1. You will not be able to receive updates using getUpdates for as long as an outgoing webhook is set up.
        2. To use a self-signed certificate, you need to upload your public key certificate using certificate parameter.
           Please upload as pytg.api_types.sendable.files.InputFile, sending a String will not work.
        3. Ports currently supported for Webhooks: 443, 80, 88, 8443.

        All types used in the Bot API responses are represented as JSON-objects.
        It is safe to use 32-bit signed integers for storing all Integer fields unless otherwise noted.

        Optional fields may be not returned when irrelevant.

        https://core.telegram.org/bots/api#setwebhook


        Optional keyword parameters:

        :keyword url: HTTPS url to send updates to. Use an empty string to remove webhook integration
        :type    url: str

        :keyword certificate: Upload your public key certificate so that the root certificate in use can be checked.
                              See our self-signed guide for details.
        :type    certificate: pytgbot.api_types.sendable.files.InputFile

        Returns:

        :return: On success, True is returned
        :rtype:  bool
        """
        from pytgbot.api_types.sendable.files import InputFile

        assert(url is None or isinstance(url, str))
        assert(certificate is None or isinstance(certificate, InputFile))

        result = self.do("setWebhook", url=url, certificate=certificate)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def set_webhook

    def send_message(self, chat_id, text, parse_mode=None, disable_web_page_preview=False, disable_notification=False,
                     reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send text messages. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendmessage


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel
                        (in the format @channelusername)
        :type  chat_id: int | str

        :param text: Text of the message to be sent
        :type  text: str


        Optional keyword parameters:

        :keyword parse_mode: Send "Markdown" or "HTML", if you want Telegram apps to show bold, italic,
                             fixed-width text or inline URLs in your bot's message.
        :type    parse_mode: str

        :keyword disable_web_page_preview: Disables link previews for links in this message
        :type    disable_web_page_preview: bool

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(text is not None)
        assert(isinstance(text, str))
        assert(parse_mode is None or isinstance(parse_mode, str))
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
        )))
        result = self.do("sendMessage", chat_id=chat_id, text=text, parse_mode=parse_mode,
            disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_message
    send_msg = send_message  # alias to send_message(...)

    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=False):
        """
        Use this method to forward messages of any kind. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#forwardmessage

        Parameters:

        :param chat_id: Unique identifier for the target chat (chat id of user chat or group chat) or username of the
                        target channel (in the format @channelusername)
        :type  chat_id: int | str

        :param from_chat_id: Unique identifier for the chat where the original message was sent
                             (id for chats or the channel's username in the format @channelusername)
        :type  from_chat_id: int | str

        :param message_id: Unique message identifier to forward
        :type  message_id: int


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool


        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))
        assert(from_chat_id is not None)
        assert(isinstance(from_chat_id, (int, str)))
        assert(message_id is not None)
        assert(isinstance(message_id, int))
        assert(disable_notification is None or isinstance(disable_notification, bool))

        result = self.do(
            "forwardMessage", chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id,
            disable_notification=disable_notification
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def forward_message

    def send_photo(self, chat_id, photo, caption=None, disable_notification=False, reply_to_message_id=None,
                   reply_markup=None):
        """
        Use this method to send photos. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendphoto


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                        @channelusername)
        :type  chat_id: int | str

        :param photo: Photo to send. You can either pass a file_id as String to resend a photo
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a photo from the Internet,
                      or upload a new photo, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
        :type  photo: pytgbot.api_types.sendable.files.InputFile | str


        Optional keyword parameters:

        :keyword caption: Photo caption (may also be used when resending photos by file_id), 0-200 characters
        :type    caption: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup |
                               pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup |
                               pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide |
                               pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(photo is not None)
        assert(isinstance(photo, (InputFile, str)))

        assert(caption is None or isinstance(caption, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))

        assert(reply_markup is None or isinstance(reply_markup, (InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)))

        result = self._do_fileupload(
            "photo", photo, chat_id=chat_id, caption=caption, disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id, reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_photo

    def send_audio(self, chat_id, audio, caption=None, duration=None, performer=None, title=None, disable_notification=False,
                   reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in the .mp3 format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size,
        this limit may be changed in the future.

        For sending voice messages, use the sendVoice method instead.

        https://core.telegram.org/bots/api#sendaudio


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                        @channelusername)
        :type  chat_id: int | str

        :param audio: Audio file to send. You can either pass a file_id as String to resend an audio
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get an audio from the Internet,
                      or upload a new audio, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
        :type  audio: pytgbot.api_types.sendable.files.InputFile | str


        Optional keyword parameters:

        :keyword duration: Duration of the audio in seconds
        :type    duration: int

        :keyword performer: Performer
        :type    performer: str

        :keyword title: Track name
        :type    title: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(audio is not None)
        assert(isinstance(audio, (InputFile, str)))

        assert(duration is None or isinstance(duration, int))

        assert(performer is None or isinstance(performer, str))

        assert(title is None or isinstance(title, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
        )))
        result = self._do_fileupload(
            "audio", audio, caption=caption, chat_id=chat_id, reply_to_message_id=reply_to_message_id, duration=duration,
            performer=performer, title=title, disable_notification=disable_notification, reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_audio

    def send_document(self, chat_id, document, caption=None, disable_notification=False, reply_to_message_id=None,
                      reply_markup=None):
        """
        Use this method to send general files. On success, the sent Message is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#senddocument


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                        @channelusername)
        :type  chat_id: int | str

        :param document: Document to send. You can either pass a file_id as String to resend a document
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a document from the Internet,
                      or upload a new document, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
        :type  document: pytgbot.api_types.sendable.files.InputFile | str


        Optional keyword parameters:

        :keyword caption: Document caption (may also be used when resending documents by file_id), 0-200 characters
        :type    caption: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(document is not None)
        assert(isinstance(document, (InputFile, str)))

        assert(caption is None or isinstance(caption, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
        )))
        result = self._do_fileupload(
            "document", document, chat_id=chat_id, document=document, caption=caption,
            disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_document

    def send_sticker(self, chat_id, sticker, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send .webp stickers. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendsticker


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                        @channelusername)
        :type  chat_id: int | str

        :param sticker: Sticker to send. You can either pass a file_id as String to resend a sticker
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a sticker from the Internet,
                      or upload a new sticker, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
        :type  sticker: pytgbot.api_types.sendable.files.InputFile | str


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(sticker is not None)
        assert(isinstance(sticker, (InputFile, str)))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
            InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
        )))
        result = self._do_fileupload(
            "sticker", sticker, chat_id=chat_id, sticker=sticker, disable_notification=disable_notification,
            reply_to_message_id=reply_to_message_id, reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_sticker

    def send_video(self, chat_id, video, duration=None, width=None, height=None, caption=None,
                   disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send video files. On success, the sent Message is returned.
        Telegram clients support mp4 videos (other formats may be sent as Document).
        Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendvideo


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                        @channelusername)
        :type  chat_id: int | str

        :param video: Video to send. You can either pass a file_id as String to resend a video
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get a video from the Internet,
                      or upload a new video, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
        :type  video: pytgbot.api_types.sendable.files.InputFile | str


        Optional keyword parameters:

        :keyword duration: Duration of sent video in seconds
        :type    duration: int

        :keyword width: Video width
        :type    width: int

        :keyword height: Video height
        :type    height: int

        :keyword caption: Video caption (may also be used when resending videos by file_id), 0-200 characters
        :type    caption: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                        Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(video is not None)
        assert(isinstance(video, (InputFile, str)))

        assert(duration is None or isinstance(duration, int))

        assert(width is None or isinstance(width, int))

        assert(height is None or isinstance(height, int))

        assert(caption is None or isinstance(caption, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
             InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
         )))
        result = self._do_fileupload(
            "video", video, chat_id=chat_id, video=video, duration=duration, width=width, height=height,
            caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_video

    def send_voice(self, chat_id, voice, caption=None, duration=None, disable_notification=False,
                   reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send audio files,
        if you want Telegram clients to display the file as a playable voice message.
        For this to work, your audio must be in an .ogg file encoded with OPUS (other formats may be sent as Audio or
        Document).

        On success, the sent Message is returned.
        Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendvoice


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                         @channelusername)
        :type  chat_id: int | str

        :param voice: Audio file to send. You can either pass a file_id as String to resend an audio
                      file that is already on the Telegram servers (recommended),
                      pass an HTTP URL as a String for Telegram to get an audio from the Internet,
                      or upload a new audio, by specifying the file path as
                      :class:`InputFile <pytgbot/pytgbot.api_types.sendable.files.InputFile>`.
        :type  voice: pytgbot.api_types.sendable.files.InputFile | str


        Optional keyword parameters:

        :keyword duration: Duration of sent audio in seconds
        :type    duration: int

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                     Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.files import InputFile
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(voice is not None)
        assert(isinstance(voice, (InputFile, str)))

        assert(duration is None or isinstance(duration, int))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
             InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
         )))
        result = self._do_fileupload(
            "voice", voice, caption=caption, chat_id=chat_id, voice=voice, duration=duration,
            disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_voice

    def send_location(self, chat_id, latitude, longitude, disable_notification=False, reply_to_message_id=None,
                      reply_markup=None):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendlocation


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                         @channelusername)
        :type  chat_id: int | str

        :param latitude: Latitude of location
        :type  latitude: float

        :param longitude: Longitude of location
        :type  longitude: float


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(latitude is not None)
        assert(isinstance(latitude, float))


        assert(longitude is not None)
        assert(isinstance(longitude, float))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
             InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
         )))
        result = self.do("sendLocation", chat_id=chat_id, latitude=latitude, longitude=longitude,
                       disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                       reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_location

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, disable_notification=False,
                   reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendvenue


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                         @channelusername)
        :type  chat_id: int | str

        :param latitude: Latitude of the venue
        :type  latitude: float

        :param longitude: Longitude of the venue
        :type  longitude: float

        :param title: Name of the venue
        :type  title: str

        :param address: Address of the venue
        :type  address: str


        Optional keyword parameters:

        :keyword foursquare_id: Foursquare identifier of the venue
        :type    foursquare_id: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                                A JSON-serialized object for an inline keyboard, custom reply keyboard,
                                instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(latitude is not None)
        assert(isinstance(latitude, float))

        assert(longitude is not None)
        assert(isinstance(longitude, float))

        assert(title is not None)
        assert(isinstance(title, str))

        assert(address is not None)
        assert(isinstance(address, str))

        assert(foursquare_id is None or isinstance(foursquare_id, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
             InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
         )))
        result = self.do("sendVenue", chat_id=chat_id, latitude=latitude, longitude=longitude, title=title,
                       address=address, foursquare_id=foursquare_id, disable_notification=disable_notification,
                       reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_venue

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendcontact


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                         @channelusername)
        :type  chat_id: int | str

        :param phone_number: Contact's phone number
        :type  phone_number: str

        :param first_name: Contact's first name
        :type  first_name: str


        Optional keyword parameters:

        :keyword last_name: Contact's last name
        :type    last_name: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide keyboard or to force a reply from the user.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardMarkup | pytgbot.api_types.sendable.reply_markup.ReplyKeyboardHide | pytgbot.api_types.sendable.reply_markup.ForceReply

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.reply_markup import ForceReply
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardHide
        from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(phone_number is not None)
        assert(isinstance(phone_number, str))

        assert(first_name is not None)
        assert(isinstance(first_name, str))

        assert(last_name is None or isinstance(last_name, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        assert(reply_markup is None or isinstance(reply_markup, (
             InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply
         )))
        result = self.do("sendContact", chat_id=chat_id, phone_number=phone_number,
                       first_name=first_name, last_name=last_name, disable_notification=disable_notification,
                       reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_contact

    def send_chat_action(self, chat_id, action):
        """
        Use this method when you need to tell the user that something is happening on the bot's side.
        The status is set for 5 seconds or less (when a message arrives from your bot,
        Telegram clients clear its typing status).

        Example: The ImageBot needs some time to process a request and upload the image.
                 Instead of sending a text message along the lines of "Retrieving image, please wait...",
                 the bot may use sendChatAction with action = "upload_photo".
                 The user will see a "sending photo" status for the bot.

        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive

        https://core.telegram.org/bots/api#sendchataction


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format
                         @channelusername)
        :type  chat_id: int | str

        :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive:
                        "typing" for text messages, "upload_photo" for photos,
                        "record_video" or "upload_video" for videos, "record_audio" or "upload_audio" for audio files,
                        "upload_document" for general files, "find_location" for location data.
        :type  action: str


        Returns:

        :return: On success, True is returned
        :rtype:  bool
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(action is not None)
        assert(isinstance(action, str))
        result = self.do("sendChatAction", chat_id=chat_id, action=action)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_chat_action

    def get_user_profile_photos(self, user_id, offset=None, limit=None):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        https://core.telegram.org/bots/api#getuserprofilephotos


        Parameters:

        :param user_id: Unique identifier of the target user
        :type  user_id: int


        Optional keyword parameters:

        :keyword offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :type    offset: int

        :keyword limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        :type    limit: int


        Returns:

        :return: Returns a UserProfilePhotos object
        :rtype:  pytgbot.api_types.receivable.media.UserProfilePhotos

        """
        assert(user_id is not None)
        assert(isinstance(user_id, int))

        assert(offset is None or isinstance(offset, int))

        assert(limit is None or isinstance(limit, int))
        result = self.do("getUserProfilePhotos", user_id=user_id, offset=offset, limit=limit)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.media import UserProfilePhotos
            try:
                return UserProfilePhotos.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type UserProfilePhotos", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_user_profile_photos

    def get_file(self, file_id):
        """
        Use this method to get basic info about a file and prepare it for downloading.
        For the moment, bots can download files of up to 20MB in size.

        On success, a File object is returned.
        The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>,
        where <file_path> is taken from the response.
        It is guaranteed that the link will be valid for at least 1 hour.
        When the link expires, a new one can be requested by calling get_file again.

        Note: This function may not preserve the original file name.
              The MIME type of the file and its name (if available)
              should be saved when the File object is received.


        https://core.telegram.org/bots/api#getfile


        Parameters:

        :param file_id: File identifier to get info about
        :type  file_id: str


        Returns:

        :return: On success, a File object is returned
        :rtype:  pytgbot.api_types.receivable.media.File
        """
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        result = self.do("getFile", file_id=file_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.media import File
            try:
                return File.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type File", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_file

    def kick_chat_member(self, chat_id, user_id):
        """
        Use this method to kick a user from a group or a supergroup. In the case of supergroups,
        the user will not be able to return to the group on their own using invite links, etc., unless unbanned first.

        The bot must be an administrator in the group for this to work. Returns True on success.

        Note: This will method only work if the ‘All Members Are Admins’ setting is off in the target group.
              Otherwise members may only be removed by the group's creator or by the member that added them.

        https://core.telegram.org/bots/api#kickchatmember


        Parameters:

        :param chat_id: Unique identifier for the target group or username of the target supergroup (in the format
                        @supergroupusername)
        :type  chat_id: int | str

        :param user_id: Unique identifier of the target user
        :type  user_id: int


        Returns:

        :return: Returns True on success
        :rtype:  bool
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(user_id is not None)
        assert(isinstance(user_id, int))

        result = self.do("kickChatMember", chat_id=chat_id, user_id=user_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def kick_chat_member

    def leave_chat(self, chat_id):
        """
        Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

        https://core.telegram.org/bots/api#leavechat


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the
                        format @channelusername)
        :type  chat_id: int | str


        Returns:

        :return: Returns True on success
        :rtype:  bool
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))
        result = self.do("leaveChat", chat_id=chat_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def leave_chat

    def unban_chat_member(self, chat_id, user_id):
        """
        Use this method to unban a previously kicked user in a supergroup.
        The user will not return to the group automatically, but will be able to join via link, etc.

        The bot must be an administrator in the group for this to work. Returns True on success.

        https://core.telegram.org/bots/api#unbanchatmember


        Parameters:

        :param chat_id: Unique identifier for the target group or username of the target supergroup (in the format
                         @supergroupusername)
        :type  chat_id: int | str

        :param user_id: Unique identifier of the target user
        :type  user_id: int


        Returns:

        :return: Returns True on success
        :rtype:  bool
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(user_id is not None)
        assert(isinstance(user_id, int))
        result = self.do("unbanChatMember", chat_id=chat_id, user_id=user_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def unban_chat_member

    def get_chat(self, chat_id):
        """
        Use this method to get up to date information about the chat (current name of the user for one-on-one
        conversations, current username of a user, group or channel, etc.)

        Returns a Chat object on success.

        https://core.telegram.org/bots/api#getchat


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the
                        format @channelusername)
        :type  chat_id: int | str


        Returns:

        :return: Returns a Chat object on success
        :rtype:  pytgbot.api_types.receivable.peer.Chat
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))
        result = self.do("getChat", chat_id=chat_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.peer import Chat
            try:
                return Chat.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Chat", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_chat

    def get_chat_administrators(self, chat_id):
        """
        Use this method to get a list of administrators in a chat.

        On success, returns an Array of ChatMember objects that contains information about all chat administrators
        except other bots. If the chat is a group or a supergroup and no administrators were appointed,
        only the creator will be returned.

        https://core.telegram.org/bots/api#getchatadministrators


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the\n
                        format @channelusername)
        :type  chat_id: int | str


        Returns:

        :return: On success, returns an Array of ChatMember objects that contains information about all
                 chat administrators except other bots. If the chat is a group or a supergroup and no administrators
                 were appointed, only the creator will be returned
        :rtype:  list of pytgbot.api_types.receivable.peer.ChatMember
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))
        result = self.do("getChatAdministrators", chat_id=chat_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.peer import ChatMember
            try:
                return ChatMember.from_array_list(result, list_level=1)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type ChatMember", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_chat_administrators

    def get_chat_members_count(self, chat_id):
        """
        Use this method to get the number of members in a chat. Returns Int on success.

        https://core.telegram.org/bots/api#getchatmemberscount


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the
                         format @channelusername)
        :type  chat_id: int | str


        Returns:

        :return: Returns Int on success
        :rtype:  int
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))
        result = self.do("getChatMembersCount", chat_id=chat_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(int, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive int", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_chat_members_count

    def get_chat_member(self, chat_id, user_id):
        """
        Use this method to get information about a member of a chat. Returns a ChatMember object on success.

        https://core.telegram.org/bots/api#getchatmember


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the
                         format @channelusername)
        :type  chat_id: int | str

        :param user_id: Unique identifier of the target user
        :type  user_id: int


        Returns:

        :return: Returns a ChatMember object on success
        :rtype:  pytgbot.api_types.receivable.peer.ChatMember
        """
        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))


        assert(user_id is not None)
        assert(isinstance(user_id, int))
        result = self.do("getChatMember", chat_id=chat_id, user_id=user_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.peer import ChatMember
            try:
                return ChatMember.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type ChatMember", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_chat_member

    def answer_callback_query(self, callback_query_id, text=None, show_alert=None, url=None):
        """
        Use this method to send answers to callback queries sent from inline keyboards.
        The answer will be displayed to the user as a notification at the top of the chat screen or as an alert.
        On success, True is returned.

        Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via BotFather and accept the terms. Otherwise, you may use links like telegram.me/your_bot?start=XXXX that open your bot with a parameter.

        https://core.telegram.org/bots/api#answercallbackquery


        Parameters:

        :param callback_query_id: Unique identifier for the query to be answered
        :type  callback_query_id: str


        Optional keyword parameters:

        :keyword text: Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
        :type    text: str

        :keyword show_alert: If true, an alert will be shown by the client instead of a notification at the top of the
                             chat screen. Defaults to false
        :type    show_alert: bool

        :keyword url: URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game – note that this will only work if the query comes from a callback_game button.Otherwise, you may use links like telegram.me/your_bot?start=XXXX that open your bot with a parameter.
        :type    url: str

        Returns:

        :return: On success, True is returned
        :rtype: bool
        """
        assert(callback_query_id is not None)
        assert(isinstance(callback_query_id, str))

        assert(text is None or isinstance(text, str))

        assert(show_alert is None or isinstance(show_alert, bool))

        assert(url is None or isinstance(url, str))

        result = self.do("answerCallbackQuery", callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def answer_callback_query

    def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None,
                          disable_web_page_preview=None, reply_markup=None):
        """
        Use this method to edit text messages sent by the bot or via the bot (for inline bots).
        On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        https://core.telegram.org/bots/api#editmessagetext


        Parameters:

        :param text: New text of the message
        :type  text: str


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or
                          username of the target channel (in the format @channelusername)
        :type    chat_id: int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id: int

        :keyword inline_message_id: Required if chat_id and message_id are not specified.
                                    Identifier of the inline message
        :type    inline_message_id: str

        :keyword parse_mode: Send "Markdown" or "HTML", if you want Telegram apps to show bold, italic, fixed-width text
                             or inline URLs in your bot's message.
        :type    parse_mode: str

        :keyword disable_web_page_preview: Disables link previews for links in this message
        :type    disable_web_page_preview: bool

        :keyword reply_markup: A JSON-serialized object for an inline keyboard.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        Returns:

        :return: On success, if edited message is sent by the bot, the edited Message is returned,
                 otherwise True is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message | bool
        """
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        assert(text is not None)
        assert(isinstance(text, str))

        assert(chat_id is None or isinstance(chat_id, (int, str)))

        assert(message_id is None or isinstance(message_id, int))

        assert(inline_message_id is None or isinstance(inline_message_id, str))

        assert(parse_mode is None or isinstance(parse_mode, str))

        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))

        result = self.do("editMessageText", text=text, chat_id=chat_id, message_id=message_id,
                       inline_message_id=inline_message_id, parse_mode=parse_mode,
                       disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def edit_message_text

    def edit_message_caption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None,
                             reply_markup=None):
        """
        Use this method to edit captions of messages sent by the bot or via the bot (for inline bots).

        On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        https://core.telegram.org/bots/api#editmessagecaption


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or
                          username of the target channel (in the format @channelusername)
        :type    chat_id: int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id: int

        :keyword inline_message_id: Required if chat_id and message_id are not specified.
                                    Identifier of the inline message
        :type    inline_message_id: str

        :keyword caption: New caption of the message
        :type    caption: str

        :keyword reply_markup: A JSON-serialized object for an inline keyboard.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        Returns:

        :return: On success, if edited message is sent by the bot, the edited Message is returned,
                 otherwise True is returned.
        :rtype:  pytgbot.api_types.receivable.updates.Message | bool
        """
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        assert(chat_id is None or isinstance(chat_id, (int, str)))

        assert(message_id is None or isinstance(message_id, int))

        assert(inline_message_id is None or isinstance(inline_message_id, str))

        assert(caption is None or isinstance(caption, str))

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))

        result = self.do("editMessageCaption", chat_id=chat_id, message_id=message_id,
                       inline_message_id=inline_message_id, caption=caption, reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def edit_message_caption

    def edit_message_reply_markup(self, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
        """
        Use this method to edit only the reply markup of messages sent by the bot or via the bot (for inline bots).
        On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        https://core.telegram.org/bots/api#editmessagereplymarkup


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or
                          username of the target channel (in the format @channelusername)
        :type    chat_id: int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id: int

        :keyword inline_message_id: Required if chat_id and message_id are not specified.
                                    Identifier of the inline message
        :type    inline_message_id: str

        :keyword reply_markup: A JSON-serialized object for an inline keyboard.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        Returns:

        :return: On success, if edited message is sent by the bot, the edited Message is returned,
                 otherwise True is returned.
        :rtype:  pytgbot.api_types.receivable.updates.Message | bool
        """
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        assert(chat_id is None or isinstance(chat_id, (int, str)))

        assert(message_id is None or isinstance(message_id, int))

        assert(inline_message_id is None or isinstance(inline_message_id, str))

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))
        result = self.do(
            "editMessageReplyMarkup", chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
            reply_markup=reply_markup
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def edit_message_reply_markup

    def answer_inline_query(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None,
                            switch_pm_text=None, switch_pm_parameter=None):
        """
        Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.

        https://core.telegram.org/bots/api#answerinlinequery


        Parameters:

        :param inline_query_id: Unique identifier for the answered query
        :type  inline_query_id: str

        :param results: A JSON-serialized array of results for the inline query
        :type  results: list of pytgbot.api_types.sendable.inline.InlineQueryResult


        Optional keyword parameters:

        :keyword cache_time: The maximum amount of time in seconds that the result of the inline query may be cached on
                             the server. Defaults to 300.
        :type    cache_time: int

        :keyword is_personal: Pass True, if results may be cached on the server side only for the user that sent the
                              query. By default, results may be returned to any user who sends the same query
        :type    is_personal: bool

        :keyword next_offset: Pass the offset that a client should send in the next query with the same text to receive
                              more results. Pass an empty string if there are no more results or if you don‘t support
                              pagination. Offset length can’t exceed 64 bytes.
        :type    next_offset: str

        :keyword switch_pm_text: If passed, clients will display a button with specified text that switches
                                 the user to a private chat with the bot and sends the bot a start message with the
                                 parameter switch_pm_parameter
        :type    switch_pm_text: str

        :keyword switch_pm_parameter: Parameter for the start message sent to the bot when user presses
                                      the switch button
                                         Example:
                                            An inline bot that sends YouTube videos can ask the user to connect the
                                            bot to their YouTube account to adapt search results accordingly.
                                            To do this, it displays a "Connect your YouTube account" button above the
                                            results, or even before showing any.
                                            The user presses the button, switches to a private chat with the bot and,
                                            in doing so, passes a start parameter that instructs the bot to return an
                                            oauth link.
                                            Once done, the bot can offer a switch_inline button so that
                                            the user can easily return to the chat where they wanted to use the bot's
                                            inline capabilities.
        :type    switch_pm_parameter: str


        Returns:

        :return: On success, True is returned
        :rtype: bool
        """
        from luckydonaldUtils.encoding import unicode_type
        assert(inline_query_id is not None)
        if isinstance(inline_query_id, int):
            inline_query_id = str(inline_query_id)
        assert(isinstance(inline_query_id, str))
        inline_query_id = n(inline_query_id)

        assert(results is not None)
        if isinstance(results, InlineQueryResult):
            results = [results]
        assert(isinstance(results, (list, tuple)))  # list of InlineQueryResult
        result_objects = []
        for result in results:
            assert isinstance(result, InlineQueryResult)  # checks all elements of results
            result_objects.append(result.to_array())
        # end for results

        assert(cache_time is None or isinstance(cache_time, int))

        assert(is_personal is None or isinstance(is_personal, bool))

        if next_offset is not None:
            assert(isinstance(next_offset, (str, unicode_type, int)))
            next_offset = n(str(next_offset))
        # end if

        assert(switch_pm_text is None or isinstance(switch_pm_text, unicode_type))  # py2: unicode, py3: str

        assert(switch_pm_parameter is None or isinstance(switch_pm_parameter, str))

        result = self.do(
            "answerInlineQuery", inline_query_id=inline_query_id, results=json.dumps(result_objects),
            cache_time=cache_time, is_personal=is_personal, next_offset=next_offset, switch_pm_text=switch_pm_text,
            switch_pm_parameter=switch_pm_parameter
        )
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def answer_inline_query

    def send_game(self, chat_id, game_short_name, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send a game. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendgame


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id: int | str

        :param game_short_name: Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.
        :type  game_short_name: str


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: A JSON-serialized object for an inline keyboard. If empty, one ‘Play game_title’ button will be shown. If not empty, the first button must launch the game.
        :type    reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        Returns:

        :return: On success, the sent Message is returned
        :rtype:  pytgbot.api_types.receivable.updates.Message
        """
        from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup

        assert(chat_id is not None)
        assert(isinstance(chat_id, (int, str)))

        assert(game_short_name is not None)
        assert(isinstance(game_short_name, str))

        assert(disable_notification is None or isinstance(disable_notification, bool))

        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))

        assert(reply_markup is None or isinstance(reply_markup, InlineKeyboardMarkup))

        result = self.do("sendGame", chat_id=chat_id, game_short_name=game_short_name, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def send_game

    def set_game_score(self, user_id, score, chat_id=None, message_id=None, inline_message_id=None, edit_message=None):
        """
        Use this method to set the score of the specified user in a game.
        On success, if the message was sent by the bot, returns the edited Message, otherwise returns True.
        Returns an error, if the new score is not greater than the user's current score in the chat.

        https://core.telegram.org/bots/api#setgamescore


        Parameters:

        :param user_id: User identifier
        :type  user_id: int

        :param score: New score, must be positive
        :type  score: int


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat (or username of the target channel in the format @channelusername)
        :type    chat_id: int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id: int

        :keyword inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type    inline_message_id: str

        :keyword edit_message: Pass True, if the game message should be automatically edited to include the current scoreboard
        :type    edit_message: bool

        Returns:

        :return: On success, if the message was sent by the bot, returns the edited Message, otherwise returns True. Returns an error, if the new score is not greater than the user's current score in the chat
        :rtype:  pytgbot.api_types.receivable.updates.Message | bool
        """
        assert(user_id is not None)
        assert(isinstance(user_id, int))

        assert(score is not None)
        assert(isinstance(score, int))

        assert(chat_id is None or isinstance(chat_id, (int, str)))

        assert(message_id is None or isinstance(message_id, int))

        assert(inline_message_id is None or isinstance(inline_message_id, str))

        assert(edit_message is None or isinstance(edit_message, bool))

        result = self.do("setGameScore", user_id=user_id, score=score, chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id, edit_message=edit_message)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.updates import Message
            try:
                return Message.from_array(result)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type Message", exc_info=True)
            # end try

            try:
                return from_array_list(bool, result, list_level=0, is_builtin=True)
            except TgApiParseException:
                logger.debug("Failed parsing as primitive bool", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def set_game_score

    def get_game_high_scores(self, user_id, chat_id=None, message_id=None, inline_message_id=None):
        """
        Use this method to get data for high score tables. Will return the score of the specified user and several of his neighbors in a game. On success, returns an Array of GameHighScore objects.

        This method will currently return scores for the target user, plus two of his closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.

        https://core.telegram.org/bots/api#getgamehighscores


        Parameters:

        :param user_id: Target user id
        :type  user_id: int


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat (or username of the target channel in the format @channelusername)
        :type    chat_id: int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id: int

        :keyword inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type    inline_message_id: str

        Returns:

        :return: This method will currently return scores for the target user, plus two of his closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.
        :rtype:  list of pytgbot.api_types.receivable.game.GameHighScore
        """
        assert(user_id is not None)
        assert(isinstance(user_id, int))

        assert(chat_id is None or isinstance(chat_id, (int, str)))

        assert(message_id is None or isinstance(message_id, int))

        assert(inline_message_id is None or isinstance(inline_message_id, str))

        result = self.do("getGameHighScores", user_id=user_id, chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id)
        if self.return_python_objects:
            logger.debug("Trying to parse {data}".format(data=repr(result)))
            from pytgbot.api_types.receivable.game import GameHighScore
            try:
                return GameHighScore.from_array_list(result, list_level=1)
            except TgApiParseException:
                logger.debug("Failed parsing as api_type GameHighScore", exc_info=True)
            # end try
            # no valid parsing so far
            raise TgApiParseException("Could not parse result.")  # See debug log for details!
        # end if return_python_objects
        return result
    # end def get_game_high_scores

    def send_msg(self, *args, **kwargs):
        """ alias to :func:`send_message` """
        return self.send_message(*args, **kwargs)
    # end def send_msg

    def do(self, command, files=None, use_long_polling=False, request_timeout=None, **query):
        """
        Send a request to the api.

        If the bot is set to return the json objects, it will look like this:

        ```json
        {
            "ok": bool,
            "result": {...},
            # optionally present:
            "description": "human-readable description of the result",
            "error_code": int
        }
        ```

        :param command: The Url command parameter
        :type  command: str

        :keyword request_timeout: When the request should time out.
        :type    request_timeout: int

        :param files: if it needs to send files.

        :keyword use_long_polling: if it should use long polling.
                                (see http://docs.python-requests.org/en/latest/api/#requests.Response.iter_content)
        :type    use_long_polling: bool

        :param query: will get json encoded.

        :return: The json response from the server, or, if `self.return_python_objects` is `True`, a parsed return type.
        :rtype: DictObject.DictObject | pytgbot.api_types.receivable.Receivable
        """
        import requests

        url, params = self._prepare_request(command, query)
        r = requests.post(url, params=params, files=files, stream=use_long_polling,
                          verify=True,  # No self signed certificates. Telegram should be trustworthy anyway...
                          timeout=request_timeout)
        return self._postprocess_request(r)
    # end def do

    def _prepare_request(self, command, query):
        """
        Prepares the command url, and converts the query json.

        :param command: The Url command parameter
        :type  command: str

        :param query: Will get json encoded.

        :return: params and a url, for use with requests etc.
        """
        from pytgbot.api_types.sendable import Sendable
        from pytgbot.api_types import as_array
        import json

        params = {}
        for key in query.keys():
            element = query[key]
            if element is not None:
                if isinstance(element, Sendable):
                    params[key] = json.dumps(as_array(element))
                else:
                    params[key] = element
        url = self._base_url.format(api_key=n(self.api_key), command=n(command))
        return url, params
    # end def _prepare_request

    def _postprocess_request(self, r):
        """
        This converts the response to either the response or a parsed :class:`pytgbot.api_types.receivable.Receivable`.

        :param r: the request response
        :type  r: requests.Response
        :return: The json response from the server, or, if `self.return_python_objects` is `True`, a parsed return type.
        :rtype: DictObject.DictObject | pytgbot.api_types.receivable.Receivable
        """
        from DictObject import DictObject
        import requests

        assert isinstance(r, requests.Response)

        try:
            logger.debug(r.json())
            res = DictObject.objectify(r.json())
        except Exception:
            logger.exception("Parsing answer failed.\nRequest: {r!s}\nContent: {r.content}".format(r=r))
            raise
        # end if
        res["response"] = r  # TODO: does this failes on json lists? Does TG does that?
        # TG should always return an dict, with at least a status or something.
        if self.return_python_objects:
            if res.ok != True:
                raise TgApiServerException(
                    error_code=res.error_code if "error_code" in res else None,
                    response=res.response if "response" in res else None,
                    description=res.description if "description" in res else None,
                    request=r.request
                )
            # end if not ok
            if "result" not in res:
                raise TgApiParseException('Key "result" is missing.')
            # end if no result
            return res.result
        # end if return_python_objects
        return res
    # end def _postprocess_request

    def _do_fileupload(self, file_param_name, value, **kwargs):
        """
        :param file_param_name: For what field the file should be uploaded.
        :type  file_param_name: str

        :param value: File to send. You can either pass a file_id as String to resend a file
                      file that is already on the Telegram servers, or upload a new file,
                      specifying the file path as :class:`pytgbot.api_types.sendable.files.InputFile`.
        :type  value: pytgbot.api_types.sendable.files.InputFile | str

        :param kwargs: will get json encoded.

        :return: The json response from the server, or, if `self.return_python_objects` is `True`, a parsed return type.
        :rtype: DictObject.DictObject | pytgbot.api_types.receivable.Receivable

        :raises TgApiTypeError, TgApiParseException, TgApiServerException: Everything from :meth:`Bot.do`, and :class:`TgApiTypeError`
        """
        from pytgbot.api_types.sendable.files import InputFile
        from luckydonaldUtils.encoding import unicode_type
        from luckydonaldUtils.encoding import to_native as n

        if isinstance(value, str):
            kwargs[file_param_name] = str(value)
        elif isinstance(value, unicode_type):
            kwargs[file_param_name] = n(value)
        elif isinstance(value, InputFile):
            kwargs["files"] = value.get_request_files(file_param_name)
        else:
            raise TgApiTypeError("Parameter {key} is not type (str, {text_type}, {input_file_type}), but type {type}".format(
                key=file_param_name, type=type(value), input_file_type=InputFile, text_type=unicode_type))
        return self.do("send{cmd}".format(cmd=file_param_name.capitalize()), **kwargs)
    # end def _do_fileupload

    def get_download_url(self, file):
        """
        Creates a url to download the file.

        Note: Contains the secret API key, so you should not share this url!

        :param file: The File you want to get the url to download.
        :type  file: pytgbot.api_types.receivable.media.File

        :return: url
        :rtype: str
        """
        from .api_types.receivable.media import File
        assert isinstance(file, File)
        return file.get_download_url(self.api_key)
    # end def get_download_url
# end class Bot
