# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)


import requests

#from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

base_url = "https://api.telegram.org/bot"
if __name__ == '__main__':
	pass


class Bot(object):
	def __init__(self, api_key):
		self.api_key = api_key

	def get_me(self):
		return self.do("getMe")

	def get_updates(self, offset=None, limit=100, timeout=0):
		"""
		Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

		:keyword offset: (Optional)	Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id.
		:type    offset: int

		:keyword limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100
		:type    limit: int
		
		:keyword timeout: Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling
		:type    timeout: int

		:return: An Array of Update objects is returned.
		:rtype : list of Update
		"""
		return self.do("getUpdates", offset=offset, limit=limit, timeout=timeout)

	def send_msg(self, chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
		"""
		Use this method to send text messages. On success, the sent Message is returned.

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
		pass


	def do(self, action, data=None, **query):
		"""
		Send a request to the api.

		:param action:
		:param data:
		:param query:
		:return:
		"""
		url = base_url + self.api_key + "/" + action
		r = requests.post(url, data=data, params=query)
		return r.json()


	#requests.utils.quote()


bot = Bot(API_KEY)
bot.send_msg(TEST_CHAT, "another test.")
bot.get_me()


"""
Errors:

send_msg:
{u'error_code': 400, u'ok': False, u'description': u'Error: Bad Request: Not in chat'}
"""