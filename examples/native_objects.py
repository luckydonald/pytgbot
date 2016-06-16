# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from pytgbot import Bot
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.updates import Update


from somewhere import API_KEY  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..."

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


def main():
    # get you bot instance.
    bot = Bot(API_KEY)
    print(bot.get_me())

    # do the update loop.
    last_update_id = 0
    while True:  # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1).result:  # for every new update
            last_update_id = update["update_id"]
            print(update)
            upd = Update.from_array(update)
            print(upd)
            result = upd.to_array()
            assert isinstance(upd, Update)
        # end for
    # end while
# end def


if __name__ == '__main__':
    main()
# end if