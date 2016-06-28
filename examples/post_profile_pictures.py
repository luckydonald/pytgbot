# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)

from pytgbot import Bot

from somewhere import API_KEY  # just set the key manually.
# API_KEY = "1231412:adLsIfTsTsLfEfPdIdPwdwIoSaBgEuSzTwszPdOaNdYs"


# get a bot instance
bot = Bot(API_KEY)

last_update_id = -1
while True:
    # loop forever.
    for update in bot.get_updates(limit=100, offset=last_update_id+1, poll_timeout=30):
        last_update_id = update.update_id
        print("got message: {msg}".format(msg=update))
        if not "message" in update:
            continue
        message = update.message
        if not "text" in message:
            continue
        logger.debug("got text: {msg}".format(msg=message.text.encode("utf-8")))
        if not message.text == "/pics":
            continue
        origin = message.chat.id if "chat" in message else message.from_peer.id
        if "reply_to_message" in message:
            name = message.reply_to_message.from_peer.first_name
            peer = message.reply_to_message.from_peer.id
            photos = bot.get_user_profile_photos(peer).photos
            if len(photos) == 0:
                bot.send_message(origin, "No images.")
                continue
            for x in reversed(photos):
                biggest_image = max(x, key=lambda p: p.file_size) # get the biggest image.
                bot.send_photo(origin, biggest_image.file_id, caption="{name}".format(name=name,
                                                w=biggest_image.width, h=biggest_image.height) )
        else:
            bot.send_message(origin, "Please reply to some message to select a user.")
        # end if
    # end for
#end while