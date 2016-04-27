# -*- coding: utf-8 -*-
import json

__author__ = 'luckydonald'

VERSION = "1.0.1"

import logging
import requests
from datetime import timedelta, datetime
from time import sleep
from DictObject import DictObject

from .encoding import to_native as n, to_unicode as u
from .encoding import native_type, text_type as unicode_type
from .api_types.files import InputFile
from .api_types.inline import InlineQueryResult

logger = logging.getLogger(__name__)


class Bot(object):
    _base_url = "https://api.telegram.org/bot{api_key}/{command}"  # do not chance.

    def __init__(self, api_key):
        if api_key is None:
            raise ValueError("No api_key given.")
        self.api_key = api_key
        self._last_update = datetime.now()

    def get_me(self):
        return self.do("getMe")

    def get_updates(self, offset=None, limit=None, timeout=None):
        """
        Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

        Notes1. This method will not work if an outgoing webhook is set up.2. In order to avoid getting duplicate updates, recalculate offset after each server response.

        https://core.telegram.org/bots/api#getupdates


        Optional keyword parameters:

        :keyword offset: Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.
        :type    offset:  int

        :keyword limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        :type    limit:  int

        :keyword timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling
        :type    timeout:  int


        Returns:

        :return: A DictObject I don't know
        :rtype:  DictObject.DictObject
        """
        assert (offset is None or isinstance(offset, int))
        assert (limit is None or isinstance(limit, int))
        assert (timeout is None or isinstance(timeout, int))
        return self.do("getUpdates", offset=offset, limit=limit, timeout=timeout)

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
        2. To use a self-signed certificate, you need to upload your public key certificate using certificate parameter. Please upload as InputFile, sending a String will not work.3. Ports currently supported for Webhooks: 443, 80, 88, 8443.

        All types used in the Bot API responses are represented as JSON-objects.
        It is safe to use 32-bit signed integers for storing all Integer fields unless otherwise noted.

        Optional fields may be not returned when irrelevant.

        https://core.telegram.org/bots/api#setwebhook


        Optional keyword parameters:

        :keyword url: HTTPS url to send updates to. Use an empty string to remove webhook integration
        :type    url:  str

        :keyword certificate: Upload your public key certificate so that the root certificate in use can be checked.
                              See our self-signed guide for details.
        :type    certificate:  InputFile


        Returns:

        :return: True if did work.
        :rtype:  bool
        """
        assert (url is None or isinstance(url, str))
        return self.do("setWebhook", url=url, certificate=certificate)
    # end def set_webhook

    def get_updates(self, offset=None, limit=100, timeout=0, delta=timedelta(milliseconds=10), error_as_empty=False):
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
                 An update is considered confirmed as soon as `get_updates` is called with
                 an offset higher than its `update_id`.
        :type offset: int

        :keyword limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100
        :type    limit: int

        :keyword timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling
        :type    timeout: int

        :keyword delta: Wait minimal 'delta' seconds, after between requests. Useful in a loop.
        :type    delta: datetime.

        :keyword error_as_empty: If errors which subclasses `requests.RequestException` will be logged but not raised.
                 Instead the returned DictObject will contain an "exception" field containing the exception occured,
                 the "result" field will be an empty list `[]`. Defaults to `False`.
        :type error_as_empty: bool

        :return: An Array of Update objects is returned, or an empty array if there was an requests.RequestException and error_as_empty is set to True.
        :rtype : dict | DictObject
        """
        now = datetime.now()
        if self._last_update - now < delta:
            wait = abs(((now - self._last_update) - delta).total_seconds())
            sleep(wait)
        self._last_update = datetime.now()
        try:
            return self.do("getUpdates", offset=offset, limit=limit, timeout=timeout)
        except requests.RequestException as e:
            if error_as_empty:
                logger.warn("Network related error happened in get_updates(), but will be ignored: " + str(e), exc_info = True)
                return DictObject(result = [], exception=e)
            else:
                raise

    def send_msg(self, chat_id, text, parse_mode=None, disable_web_page_preview=False, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send text messages. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendmessage


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param text: Text of the message to be sent
        :type  text: str


        Optional keyword parameters:

        :keyword parse_mode: Send "Markdown" or "HTML", if you want Telegram apps to show bold, italic,
                             fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str

        :keyword disable_web_page_preview: Disables link previews for links in this message
        :type    disable_web_page_preview: bool

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound.
        :type    disable_notification: bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom
                               reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: The sent Message object
        :rtype:  Message
        """
        assert(text is not None)
        assert(isinstance(text, str))
        assert(parse_mode is None or isinstance(parse_mode, str))
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self.do("sendMessage", chat_id=chat_id, text=text, parse_mode=parse_mode,
                       disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                       reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
    # end def send_message


    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=False):
        """
        Use this method to forward messages of any kind. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#forwardmessage

        Parameters:

        :param chat_id: Unique identifier for the target chat (chat id of user chat or group chat) or username of the
                        target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param from_chat_id: Unique identifier for the chat where the original message was sent
                             (id for chats or the channel's username in the format @channelusername)
        :type  from_chat_id:  int | str

        :param message_id: Unique message identifier to forward.
        :type  message_id: int


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound.
        :type    disable_notification:  bool


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(message_id is not None)
        assert(isinstance(message_id, int))
        return self.do("forwardMessage", chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id,
                       disable_notification=disable_notification
        )
    # end def forward_message

    def _do_fileupload(self, key, value, **kwargs):
        if isinstance(value, str):
            kwargs[key] = str(value)
        elif isinstance(value, unicode_type):
            kwargs[key] = n(value)
        elif isinstance(value, InputFile):
            kwargs["files"] = value.get_request_files(key)
        else:
            raise TypeError("Parameter {key} is not type (str, {text_type}, {input_file_type}), but type {type}".format(
                key=key, type=type(value), input_file_type=InputFile, text_type=unicode_type))
        return self.do("send{cmd}".format(cmd=key.capitalize()), **kwargs)

    def send_photo(self, chat_id, photo, caption=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send photos. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendphoto


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param photo: Photo to send. You can either pass a file_id as String to resend a photo file that is already on
                      the Telegram servers, or upload a new photo, specifying the file path as pytg.api_types.files.InputFile.
        :type  photo:  InputFile | str


        Optional keyword parameters:

        :keyword caption: Photo caption (may also be used when resending photos by file_id), 0-200 characters
        :type    caption: str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id: int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(caption is None or isinstance(caption, str))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self._do_fileupload("photo", photo, chat_id=chat_id, caption=caption,
                                   disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                                   reply_markup=reply_markup
        )
    # end def send_photo

    def send_audio(self, chat_id, audio, duration=None, performer=None, title=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in the .mp3 format. Bots can currently send audio files of up to 50 MB in size,
        this limit may be changed in the future.

        For sending voice messages, use the sendVoice method instead.

        https://core.telegram.org/bots/api#sendaudio


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param audio: Audio file to send. You can either pass a file_id as String to resend a audio file that is already on the Telegram servers, or upload the new audio, specifying the file path as pytg.api_types.files.InputFile.
        :type  audio:  InputFile | str


        Optional keyword parameters:

        :keyword duration: Duration of the audio in seconds
        :type    duration:  int

        :keyword performer: Performer
        :type    performer:  str

        :keyword title: Track name
        :type    title:  str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(duration is None or isinstance(duration, int))
        assert(performer is None or isinstance(performer, str))
        assert(title is None or isinstance(title, str))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self._do_fileupload("audio", audio, chat_id=chat_id, reply_to_message_id=reply_to_message_id,
                                   duration=duration, performer=performer, title=title,
                                   disable_notification=disable_notification, reply_markup=reply_markup)

    # end def send_audio

    def send_document(self, chat_id, document, caption=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send general files. On success, the sent Message is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#senddocument


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param document: Document to send. You can either pass a file_id as String to resend a
                         file that is already on the Telegram servers, or upload the new document,
                         specifying the file path as pytg.api_types.files.InputFile.
        :type  document:  InputFile | str


        Optional keyword parameters:

        :keyword caption: Document caption (may also be used when resending documents by file_id), 0-200 characters
        :type    caption:  str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(caption is None or isinstance(caption, str))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self._do_fileupload("document", document, chat_id=chat_id, document=document, caption=caption,
                                   disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                                   reply_markup=reply_markup)

    # end def send_document

    def send_sticker(self, chat_id, sticker, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send .webp stickers. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendsticker

        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param sticker: Sticker to send. You can either pass a file_id as String to resend a
                        sticker file that is already on the Telegram servers, or upload the new sticker,
                        specifying the file path as pytg.api_types.files.InputFile.
        :type  sticker:  InputFile | str


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options.
                               A JSON-serialized object for an inline keyboard, custom reply keyboard,
                               instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self._do_fileupload("sticker", sticker, chat_id=chat_id, sticker=sticker,
                                   disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                                   reply_markup=reply_markup)

    # end def send_sticker

    def send_video(self, chat_id, video, duration=None, width=None, height=None, caption=None, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send video files. On success, the sent Message is returned.
        Telegram clients support mp4 videos (other formats may be sent as Document).
        Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendvideo


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param video: Video to send. You can either pass a file_id as String to resend a
                      video file that is already on the Telegram servers, or upload the new video,
                      specifying the file path as pytg.api_types.files.InputFile.
        :type  video:  InputFile | str


        Optional keyword parameters:

        :keyword duration: Duration of sent video in seconds
        :type    duration:  int

        :keyword width: Video width
        :type    width:  int

        :keyword height: Video height
        :type    height:  int

        :keyword caption: Video caption (may also be used when resending videos by file_id), 0-200 characters
        :type    caption:  str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification,
                                       Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom
                               reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(duration is None or isinstance(duration, int))
        assert(width is None or isinstance(width, int))
        assert(height is None or isinstance(height, int))
        assert(caption is None or isinstance(caption, str))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self._do_fileupload("video", video, chat_id=chat_id, video=video,
                                   duration=duration, width=width, height=height, caption=caption,
                                   disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                                   reply_markup=reply_markup)

    # end def send_video

    def send_voice(self, chat_id, voice, duration=None, disable_notification=False, reply_to_message_id=None,
                   reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .ogg file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        https://core.telegram.org/bots/api#sendvoice


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param voice: Audio file to send. You can either pass a file_id as String to resend an audio that is already on the Telegram servers, or upload a new audio file using multipart/form-data.
        :type  voice:  InputFile | str


        Optional keyword parameters:

        :keyword duration: Duration of sent audio in seconds
        :type    duration:  int

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert (duration is None or isinstance(duration, int))
        assert (disable_notification is None or isinstance(disable_notification, bool))
        assert (reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self._do_fileupload("voice", voice, chat_id=chat_id, voice=voice, duration=duration,
                       disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                       reply_markup=reply_markup)

    # end def send_voice

    def send_location(self, chat_id, latitude, longitude, disable_notification=False, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendlocation


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param latitude: Latitude of location
        :type  latitude:  Float number

        :param longitude: Longitude of location
        :type  longitude:  Float number


        Optional keyword parameters:

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self.do("sendLocation", chat_id=chat_id, latitude=latitude, longitude=longitude,
                       disable_notification=disable_notification, reply_to_message_id=reply_to_message_id,
                       reply_markup=reply_markup)
    # end def send_location

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, disable_notification=False,
                   reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendvenue


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param latitude: Latitude of the venue
        :type  latitude:  float

        :param longitude: Longitude of the venue
        :type  longitude:  float

        :param title: Name of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Foursquare identifier of the venue
        :type    foursquare_id:  str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide reply keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert (title is not None)
        assert (isinstance(title, str))
        assert (address is not None)
        assert (isinstance(address, str))
        assert (foursquare_id is None or isinstance(foursquare_id, str))
        assert (disable_notification is None or isinstance(disable_notification, bool))
        assert (reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self.do("sendVenue", chat_id=chat_id, latitude=latitude, longitude=longitude, title=title,
                       address=address, foursquare_id=foursquare_id, disable_notification=disable_notification,
                       reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    # end def send_venue

    def send_contact(self, chat_id, phone_number, first_name, last_name=None, disable_notification=None,
                     reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendcontact


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Contact's last name
        :type    last_name:  str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert (phone_number is not None)
        assert (isinstance(phone_number, str))
        assert (first_name is not None)
        assert (isinstance(first_name, str))
        assert (last_name is None or isinstance(last_name, str))
        assert (disable_notification is None or isinstance(disable_notification, bool))
        assert (reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self.do("sendContact", chat_id=chat_id, phone_number=phone_number,
                       first_name=first_name, last_name=last_name, disable_notification=disable_notification,
                       reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
    # end def send_contact

    def send_chat_action(self, chat_id, action):
        """
        Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).

        https://core.telegram.org/bots/api#sendchataction


        Parameters:

        :param chat_id: Unique identifier for the message recipient — User or GroupChat id
        :type  chat_id:  Integer

        :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data.
        :type  action:  String


        Returns:

        :return:
        :rtype:
        """
        return self.do("sendChatAction", chat_id=chat_id, action=action)

    # end def send_chat_action

    def answer_inline_query(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None):
        """
        Use this method to send answers to an inline query. On success, True is returned.
        No more than 50 results per query are allowed.

        https://core.telegram.org/bots/api#answerinlinequery


        Parameters:

        :param inline_query_id: Unique identifier for the answered query
        :type  inline_query_id:  str

        :param results: A JSON-serialized array of results for the inline query
        :type  results:  Array of InlineQueryResult


        Optional keyword parameters:

        :keyword cache_time: The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
        :type    cache_time:  int

        :keyword is_personal: Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
        :type    is_personal:  bool

        :keyword next_offset: Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don‘t support pagination. Offset length can’t exceed 64 bytes.
        :type    next_offset:  str


        Returns:

        :return:
        :rtype:  None
        """
        assert(inline_query_id is not None)
        if isinstance(inline_query_id, int):
            inline_query_id = str(inline_query_id)
        assert(isinstance(inline_query_id, (str, unicode_type)))
        inline_query_id = n(inline_query_id)
        assert(results is not None)
        assert(isinstance(results, (list, tuple)))  # Array of InlineQueryResult
        result_objects  = []
        for result in results:
            assert isinstance(result, InlineQueryResult)  # checks all elements of results
            result_objects.append(result.to_array())
        assert(cache_time is None or isinstance(cache_time, int))
        assert(is_personal is None or isinstance(is_personal, bool))
        if next_offset is not None:
            assert(isinstance(next_offset, (str, unicode_type, int)))
            next_offset = n(str(next_offset))
        return self.do("answerInlineQuery", inline_query_id=inline_query_id, results=json.dumps(result_objects), cache_time=cache_time, is_personal=is_personal, next_offset=next_offset)
    # end def answer_inline_query

    def get_user_profile_photos(self, user_id, offset=None, limit=None):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        https://core.telegram.org/bots/api#getuserprofilephotos


        Parameters:

        :param user_id: Unique identifier of the target user
        :type  user_id:  Integer


        Optional keyword parameters:

        :keyword offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :type    offset:  Integer

        :keyword limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        :type    limit:  Integer


        Returns:

        :return: Returns a UserProfilePhotos object.
        :rtype:  UserProfilePhotos
        """
        return self.do("getUserProfilePhotos", user_id=user_id, offset=offset, limit=limit)

    # end def get_user_profile_photos

    def do(self, command, files=None, **query):
        """
        Send a request to the api.

        :param action:
        :param data:
        :param query:
        :return:
        """
        url = self._base_url.format(api_key=n(self.api_key), command=n(command))
        r = requests.post(url, params=query, files=files,
                          verify=True)  # No self signed certificates. Telegram should be trustworthy anyway...
        res = DictObject.objectify(r.json())
        res["response"] = r  # TODO: does this failes on json lists? Does TG does that?
        # TG should always return an dict, with at least a status or something.
        return res

"""
Errors:

send_msg:
{u'error_code': 400, u'ok': False, u'description': u'Error: Bad Request: Not in chat'}
"""
