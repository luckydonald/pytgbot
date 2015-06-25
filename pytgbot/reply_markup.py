# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)


class ReplyMarkup(object):
	def __init__(self):
		super(ReplyMarkup, self).__init__()


class ReplyKeyboardMarkup(ReplyMarkup):
	"""
	This object represents a custom keyboard with reply options.
	"""
	def __init__(self, keyboard, resize_keyboard=False, one_time_keyboard=False, selective=False):
		"""
		This object represents a custom keyboard with reply options.
		
		:param keyboard: Array of button rows, each represented by an Array of Strings
		:type  keyboard: list of (list of str)

		:keyword resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
		:type    resize_keyboard: bool

		:keyword one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. Defaults to false.
		:type    one_time_keyboard: bool

		:keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
							Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
		:type    selective: bool
		"""
		super(ReplyKeyboardMarkup, self).__init__()
		self.keyboard = keyboard
		self.resize_keyboard = resize_keyboard
		self.one_time_keyboard = one_time_keyboard
		self.selective = selective


class ReplyKeyboardHide(ReplyMarkup):
	"""
	Upon receiving a message with this object, Telegram clients will hide the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).
	"""
	def __init__(self, selective=False):
		"""
		Upon receiving a message with this object, Telegram clients will hide the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

		:keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
							Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
		:type    selective: bool
		"""
		super(ReplyKeyboardHide, self).__init__()
		self.hide_keyboard = True
		self.selective = selective


class ForceReply(ReplyMarkup):
	def __init__(self, selective=False):
		"""
		Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot‘s message and tapped ’Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

		:keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
							Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
		:type    selective: bool
		"""
		super(ForceReply, self).__init__()
		self.force_reply = True
		self.selective = selective
