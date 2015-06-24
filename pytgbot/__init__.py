# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)


import requests
#from urllib import parse

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D

base_url = "https://api.telegram.org/bot"
if __name__ == '__main__':
	pass

def do(action, data=None, **query):
	url = base_url + API_KEY + "/" + action
	r = requests.post(url, data=data, params=query)
	return r.json()

def send_msg(chat_id, text, disable_web_page_preview=False, reply_to_message_id=None, reply_markup=None):
	return do("SendMessage", chat_id=chat_id, text=text)
	#requests.utils.quote()

send_msg(TEST_CHAT, "another test.")