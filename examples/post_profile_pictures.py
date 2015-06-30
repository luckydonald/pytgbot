# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

from pytgbot import Bot

from somewhere import API_KEY  # just set the key manually.
# API_KEY = "1231412:adLsIfTsTsLfEfPdIdPwdwIoSaBgEuSzTwszPdOaNdYs"

bot = Bot(API_KEY)

last_update_id = -1
while True:
	# loop forever.
	for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:
		last_update_id = update["update_id"]
		if not "message" in update:
			continue
		message = update["message"]
		logger.info("got message: {msg}".format(msg=message))
		if not "text" in message:
			continue
		logger.info("got message: {msg}".format(msg=message.text.encode("utf-8")))
		if "reply_to_message" in message and message.text == "/pics":
			name = message.reply_to_message["from"].first_name
			peer = message.reply_to_message["from"].id
			origin = message.chat.id if "chat" in message else message["from"].id
			for x in reversed(bot.get_user_profile_photos(peer)["result"]["photos"]):
				biggest_image = max(x, key=lambda p: p["file_size"]) # get the biggest image.
				bot.send_photo(origin, biggest_image["file_id"], caption="{name}".format(name=name,
												w=biggest_image["width"], h=biggest_image["height"]) )
		#end if
	# end for
#end while