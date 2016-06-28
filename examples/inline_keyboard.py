# -*- coding: utf-8 -*-
from pytgbot import Bot
from pytgbot.api_types.receivable.media import PhotoSize
from pytgbot.api_types.receivable.updates import Message
from pytgbot.api_types.sendable.reply_markup import InlineKeyboardButton, InlineKeyboardMarkup
from pytgbot.exceptions import TgApiException
import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)

from somewhere import API_KEY  # just set the key manually.
# API_KEY = "1231412:adLsIfTsTsLfEfPdIdPwdwIoSaBgEuSzTwszPdOaNdYs"

photo_cache = {}  # stores the images.

# get a bot instance
bot = Bot(API_KEY, return_python_objects=True)


def main():
    last_update_id = -1

    while True:
        # loop forever.
        try:
            updates = bot.get_updates(limit=100, offset=last_update_id+1, poll_timeout=30, error_as_empty=True)
            for update in updates:
                last_update_id = update.update_id
                if not (update.message and "/start" in update.message.text) and not update.callback_query:
                    continue
                if update.message:
                    print("got message: {msg}".format(msg=update.message))
                    origin, peer_id = get_sender_infos(update.message)
                    current_image = 0
                    photos = cache_peer_images(peer_id, force=True)
                    result_image, markup = generate_page(current_image, peer_id, photos)

                    result = bot.send_message(
                        origin,
                        "Profile pic {num}:\n{w}x{h}, {size}".format(
                            num=current_image, w=result_image.width, h=result_image.height, size=result_image.file_size
                        ),
                        disable_web_page_preview=False,
                        reply_markup=markup
                    )
                    print(result)
                else:
                    # callback_query.message is the original message the bot sent
                    peer_id, current_image, do_submit = update.callback_query.data.split(";")
                    peer_id, current_image = int(peer_id), int(current_image)  # str -> int
                    do_submit = do_submit == "True"  # str -> bool
                    photos = cache_peer_images(peer_id)
                    result_image, markup = generate_page(current_image, peer_id, photos)
                    assert isinstance(result_image, PhotoSize)
                    if do_submit:
                        result = bot.send_photo(chat_id=update.callback_query.message.chat.id, photo=result_image.file_id)
                    else:
                        result = bot.edit_message_text(
                            "Profile pic {num}\n{w}x{h}, {size}B".format(
                                num=current_image, w=result_image.width, h=result_image.height, size=result_image.file_size
                            ),
                            chat_id=update.callback_query.message.chat.id,
                            message_id=update.callback_query.message.message_id,
                            disable_web_page_preview=False,
                            reply_markup=markup
                        )
                    # end if
                    print(result)
                # end if
            # end for
        except TgApiException:
            logger.exception()
        # end try
    # end while
# end def main


def cache_peer_images(peer_id, force=False):
    if not force and peer_id in photo_cache:
        return photo_cache[peer_id]
    photos = bot.get_user_profile_photos(peer_id).photos
    photo_cache[peer_id] = []
    for photo in photos:
        photo_cache[peer_id].append(
            max(photo, key=lambda p: p.file_size)  # get the biggest image.
        )
    return photos
# end def


def get_sender_infos(message):
    assert isinstance(message, Message)
    peer_id = message.from_peer.id
    origin = message.chat.id if message.chat else message.from_peer.id
    return origin, peer_id


# noinspection PyTypeChecker
def generate_page(current_image, peer_id, photos):
    buttons = [[], []]  # 2 rows
    # first button row
    if current_image > 0:
        buttons[0].append(InlineKeyboardButton(
            "<<", callback_data="{peer_id};{next_pos};False".format(peer_id=peer_id, next_pos=current_image-1)
        ))
    # end if
    if current_image < len(photos)-1:
        buttons[0].append(InlineKeyboardButton(
            ">>", callback_data="{peer_id};{next_pos};False".format(peer_id=peer_id, next_pos=current_image + 1)
        ))
    # end if
    # second button row
    buttons[1].append(InlineKeyboardButton(
        "send", callback_data="{peer_id};{curr_pos};True".format(peer_id=peer_id, curr_pos=current_image)
    ))
    markup = InlineKeyboardMarkup(buttons)
    result_image = photo_cache[peer_id][current_image]
    return result_image, markup

if __name__ == '__main__':
    main()
# end if