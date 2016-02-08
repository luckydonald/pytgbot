# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from json import dumps

__author__ = 'luckydonald'

from random import getrandbits
import logging
logger = logging.getLogger(__name__)

from somewhere import API_KEY, TEST_CHAT  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..." and TEST_CHAT = 12345

from pytgbot import Bot, u
from pytgbot.types.inline import InlineQueryResultArticle, InlineQueryResultPhoto, InlineQueryResultGif
from pytgbot.encoding import to_native as n


def main():
    # get you bot instance.
    bot = Bot(API_KEY)


    my_info=bot.get_me()
    print("Information about myself: {info}".format(info=my_info))
    last_update_id = 0
    mlfw = MLFW(bot)
    while True:
        # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1)["result"]:
            last_update_id = update["update_id"]
            print(update)
            if not "inline_query" in update:
                continue
            inline_query_id = update.inline_query.id
            query_obj = update.inline_query
            query = query_obj.query
            print (query)
            mlfw.search(query, inline_query_id, offset=query_obj.offset)



from luckydonaldUtils.download import get_json
from urllib import quote
class MLFW(object):
    root = "http://mylittlefacewhen.com/"
    tag_search = "http://mylittlefacewhen.com/api/v2/tag/"
    tag_info = "http://mylittlefacewhen.com/api/v3/face/"

    def __init__(self, bot):
        super(MLFW, self).__init__()
        self.bot = bot

    def search(self, string, inline_query_id, offset=0):
        results = []
        fo = get_json(self.tag_search, params=dict(format="json", name__startswith=string, limit=1))
        total_count = fo.meta.total_count
        if total_count <= 0:
            return []
        objects = fo.objects
        for tag_obj in objects:
            name = tag_obj.name
            print ("tag: " + name)
            tag = get_json(self.tag_info, params=dict(search=dumps([name]), format="json", limit=10, offset=0))
            print(tag)
            if tag.meta.total_count < 1 or len(tag.objects) < 1:
                continue
            for img in tag.objects:
                #image = self.root + tag.objects[0].resizes.small
                image_small = self.root + img.resizes.small
                image_gif = self.root + img.thumbnails.jpg if "gif" in img.thumbnails else None
                image_full = self.root + img.image
                tag_total_count = tag.meta.total_count
                results.append(InlineQueryResultArticle(id=img.md5[4:]+u(hex(getrandbits(64))[:4]), thumb_url=image_small, title=u"{tag}".format(tag=img.title), message_text=image_full, description=img.description))
                #if image_gif:
                    #results.append(InlineQueryResultGif(id=img.md5, title=img.title, gif_url=image_full, thumb_url=image_small, caption=img.description))
                #else:
                    #results.append(InlineQueryResultPhoto(id=img.md5, title=img.title, photo_url=image_full, thumb_url=image_small, caption=img.description))
        for res in results:
            print( res.to_array())
        success = self.bot.answer_inline_query(inline_query_id, results, cache_time=60, next_offset=10)
        print(success)
        if not success.ok:
            print ("dayum!")
        return results



if __name__ == '__main__':
    main()