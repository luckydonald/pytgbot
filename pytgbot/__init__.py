# -*- coding: utf-8 -*-
from DictObject import DictObject

__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

VERSION = "0.0.0-pre0"

from . import types, encoding
from .types.files import InputFile
from .encoding import to_native as n
import requests
from datetime import timedelta, datetime
from time import sleep
class Bot(object):
	_base_url = "https://api.telegram.org/bot{api_key}/{command}" # do not chance.
	def __init__(self, api_key):
		if api_key is None:
			raise ValueError("No api_key given.")
		self.api_key = api_key
		self._last_update = datetime.now()

	def get_me(self):
		return self.do("getMe")


	def get_updates(self, offset=None, limit=100, timeout=0, delta=timedelta(milliseconds=1000)):
		"""
		Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

		:keyword offset: (Optional)	Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id.
		:type    offset: int

		:keyword limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100
		:type    limit: int
		
		:keyword timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling
		:type    timeout: int

		:keyword delta: Wait minimal 'delta' seconds, after between requests. Useful in a loop.
		:type    delta: datetime.

		:return: An Array of Update objects is returned.
		:rtype : list of Update
		"""
		now = datetime.now()
		if self._last_update - now < delta:
			wait = abs(((now - self._last_update) - delta).total_seconds())
			sleep(wait)
		self._last_update = datetime.now()
		return self.do("getUpdates", offset=offset, limit=limit, timeout=timeout)


	def send_msg(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send text messages. On success, the sent Message is returned.

		https://core.telegram.org/bots/api#sendmessage

		:param chat_id: Unique identifier for the message recepient — User or GroupChat id
		:type  chat_id: int

		:param text: Text of the message to be sent
		:type  text: str

		:keyword disable_web_page_preview: Disables link previews for links in this message
		:type    disable_web_page_preview: bool

		:keyword reply_to_message: If the message is a reply, ID of the original message
		:type    reply_to_message: int

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup: ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply

		:return: The sent Message object
		:rtype:  Message
		"""
		return self.do("SendMessage", chat_id=chat_id, text=text, disable_web_page_preview=disable_web_page_preview, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

	def forward_message(self, chat_id, from_chat_id, message_id):
		"""
		Use this method to forward messages of any kind. On success, the sent Message is returned.

		https://core.telegram.org/bots/api#forwardmessage
		
		:param chat_id: Unique identifier for the message recepient — User or GroupChat id
		:type  chat_id: int

		:param from_chat_id: Unique identifier for the chat where the original message was sent — User or GroupChat id
		:type  from_chat_id: int

		:param message_id: Unique message identifier to forward.
		:type  message_id: int

		:return: the sent Message
		:rtype:  Message
		"""
		self.do("ForwardMessage", chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)

	def _do_fileupload(self, key, value, **kwargs):
		if isinstance(value, str):
			kwargs[key] = str(value)
		elif isinstance(value, encoding.text_type):
			kwargs[key] = encoding.to_native(value)
		elif isinstance(value, types.files.InputFile):
			kwargs["files"] = value.get_request_files(key)
		else:
			raise TypeError("Parameter {key} is not type (str, {text_type}, {input_file_type}), but type {type}".format(
				key=key, type=type(value), input_file_type=types.files.InputFile, text_type=encoding.text_type))
		return self.do("send{cmd}".format(cmd=key.capitalize()), **kwargs)

	def send_photo(self, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send photos. On success, the sent Message is returned.

		https://core.telegram.org/bots/api#sendphoto


		Parameters:

		:param chat_id: Unique identifier for the message recepient — User or GroupChat id
		:type  chat_id: int

		:param photo: Photo to send. You can either pass a file_id as String to resend a photo file that is already on the Telegram servers, or upload the new photo, specifying the file path as pytg.types.files.InputFile.
		:type  photo: str | InputFile


		Optional keyword parameters:

		:keyword caption: Photo caption (may also be used when resending photos by file_id).
		:type    caption: str

		:keyword reply_to_message_id: If the message is a reply, ID of the original message
		:type    reply_to_message_id: int

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup: ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


		Returns:

		:return: the sent Message
		:rtype:  Message
		"""
		return self._do_fileupload("photo", photo, chat_id=chat_id, caption=caption, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)


	def send_audio(self, chat_id, audio, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .ogg file encoded with OPUS (other formats may be sent as Document). On success, the sent Message is returned.

		https://core.telegram.org/bots/api#sendaudio


		Parameters:

		:param chat_id: Unique identifier for the message recepient — User or GroupChat id
		:type  chat_id:  Integer

		:param audio: Audio to send. You can either pass a file_id as String to resend a audio file that is already on the Telegram servers, or upload the new audio, specifying the file path as pytg.types.files.InputFile.
		:type  audio: str | InputFile


		Optional keyword parameters:

		:keyword reply_to_message_id: If the message is a reply, ID of the original message
		:type    reply_to_message_id:  Integer

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup:  ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply


		Returns:

		:return: On success, the sent Message is returned.
		:rtype:  Message
		"""
		return self._do_fileupload("audio", audio, chat_id=chat_id, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
	# end def send_audio


	def send_document(self, chat_id, document, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send general files. On success, the sent Message is returned.

		https://core.telegram.org/bots/api#senddocument


		Parameters:

		:param chat_id: Unique identifier for the message recepient — User or GroupChat id
		:type  chat_id:  Integer

		:param document: Document to send. You can either pass a file_id as String to resend a document file that is already on the Telegram servers, or upload the new document, specifying the file path as pytg.types.files.InputFile.
		:type  document: str | InputFile


		Optional keyword parameters:

		:keyword reply_to_message_id: If the message is a reply, ID of the original message
		:type    reply_to_message_id:  Integer

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup:  ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply


		Returns:

		:return: On success, the sent Message is returned.
		:rtype:  Message
		"""
		return self._do_fileupload("document", document, chat_id=chat_id, document=document, reply_to_message_id=reply_to_message_id)
	# end def send_document

	def send_sticker(self, chat_id, sticker, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send .webp stickers. On success, the sent Message is returned.

		https://core.telegram.org/bots/api#sendsticker

		Parameters:

		:param chat_id: Unique identifier for the message recepient — User or GroupChat id
		:type  chat_id:  Integer

		:param sticker: Sticker to send. You can either pass a file_id as String to resend a sticker file that is already on the Telegram servers, or upload the new sticker, specifying the file path as pytg.types.files.InputFile.
		:type  sticker: str | InputFile


		Optional keyword parameters:

		:keyword reply_to_message_id: If the message is a reply, ID of the original message
		:type    reply_to_message_id:  Integer

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup:  ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply


		Returns:

		:return: On success, the sent Message is returned.
		:rtype:  Message
		"""
		return self._do_fileupload("sticker", sticker, chat_id=chat_id, sticker=sticker, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
	# end def send_sticker

	def send_video(self, chat_id, video, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned.

		https://core.telegram.org/bots/api#sendvideo


		Parameters:

		:param chat_id: Unique identifier for the message recipient — User or GroupChat id
		:type  chat_id:  Integer

		:param video: Video to send. You can either pass a file_id as String to resend a video file that is already on the Telegram servers, or upload the new video, specifying the file path as pytg.types.files.InputFile.
		:type  video: str | InputFile


		Optional keyword parameters:

		:keyword reply_to_message_id: If the message is a reply, ID of the original message
		:type    reply_to_message_id:  Integer

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup:  ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply


		Returns:

		:return: On success, the sent Message is returned.
		:rtype:  Message
		"""
		return self._do_fileupload("video", video, chat_id=chat_id, video=video, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
	# end def

	def send_location(self, chat_id, latitude, longitude, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send point on the map. On success, the sent Message is returned.

		https://core.telegram.org/bots/api#sendlocation


		Parameters:

		:param chat_id: Unique identifier for the message recipient — User or GroupChat id
		:type  chat_id:  Integer

		:param latitude: Latitude of location
		:type  latitude:  Float number

		:param longitude: Longitude of location
		:type  longitude:  Float number


		Optional keyword parameters:

		:keyword reply_to_message_id: If the message is a reply, ID of the original message
		:type    reply_to_message_id:  Integer

		:keyword reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
		:type    reply_markup:  ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply


		Returns:

		:return: On success, the sent Message is returned.
		:rtype:  Message
		"""
		return self.do("sendLocation", chat_id=chat_id, latitude=latitude, longitude=longitude, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
	# end def send_location

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
		r = requests.post(url, params=query, files=files, verify=True) # No self signed certificates. Telegram should be trustworthy anyway...
		return DictObject.objectify(r.json())


"""
Errors:

send_msg:
{u'error_code': 400, u'ok': False, u'description': u'Error: Bad Request: Not in chat'}
"""