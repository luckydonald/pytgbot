# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from json import dumps

from pytgbot import Bot
from pytgbot.exceptions import TgApiException
from pytgbot.api_types.sendable.inline import InlineQueryResultArticle, InlineQueryResultGif, InlineQueryResultPhoto
from pytgbot.api_types.sendable.inline import InputTextMessageContent

from luckydonaldUtils.logger import logging
from luckydonaldUtils.download import get_json


__author__ = 'luckydonald'
VERSION = "v0.3.0"

try:
    from urllib import quote  # python 2
except ImportError:
    from urllib.parse import quote  # python 3
# end tray
logger = logging.getLogger(__name__)

from somewhere import API_KEY  # so I don't upload them to github :D
# Just remove the line, and add API_KEY="..."


def main():
    # get you bot instance.
    bot = Bot(API_KEY)

    my_info=bot.get_me()
    print("Information about myself: {info}".format(info=my_info))
    last_update_id = 0
    mlfw = MLFW(bot)
    while True:
        # loop forever.
        for update in bot.get_updates(limit=100, offset=last_update_id+1, error_as_empty=True):
            last_update_id = update.update_id
            print(update)
            if not update.inline_query:
                continue
            inline_query_id = update.inline_query.id
            query_obj = update.inline_query
            query = query_obj.query
            print(query)
            print(query_obj)
            mlfw.search(query, inline_query_id, offset=query_obj.offset)
        # end for
    # end while
# end def main


class MLFW(object):
    root = "http://mylittlefacewhen.com/"
    tag_search = "http://mylittlefacewhen.com/api/v2/tag/"
    tag_info = "http://mylittlefacewhen.com/api/v2/face/"
    error_image = "http://www.iconsdb.com/icons/preview/red/warning-xxl.png"

    def __init__(self, bot):
        super(MLFW, self).__init__()
        self.bot = bot

    def search(self, string, inline_query_id, offset):
        if not string:  # nothing entered.
            string = "littlepip"
        results = []
        next_offset=None
        if offset is None or len(str(offset).strip()) < 1:
            offset = 0
        else:
            offset = int(offset)
        valid_tag_names = []
        for string_part in string.split(","):
            string_part = string_part.strip()
            valid_tag_obj = get_json(self.tag_search, params=dict(format="json", name__startswith=string_part, limit=1))
            if "error" in valid_tag_obj:
                error_message = InlineQueryResultArticle(
                    id="404e:"+string,
                    title=u"\"{tag}\" not found.".format(tag=string),
                    input_message_content=InputTextMessageContent(string),
                    description=valid_tag_obj.error, thumb_url=self.error_image
                )
                try:
                    self.bot.answer_inline_query(inline_query_id, [error_message])
                except TgApiException:
                    logger.exception("Answering query failed.")
                return
            for tag_obj in valid_tag_obj.objects:
                valid_tag_names.append(tag_obj.name)
        if len(valid_tag_names) == 0:
            result = InlineQueryResultArticle(
                    id="404t:"+string,
                    title=u"\"{tag}\" not found.".format(tag=string),
                    input_message_content=InputTextMessageContent(string),
                    description="No similar tag found.",
                    thumb_url=self.error_image
            )
            try:
                self.bot.answer_inline_query(inline_query_id, result)
            except TgApiException:
                logger.exception("Answering query failed.")
            return
        print ("tags: {}".format(valid_tag_names))
        print("offset: {}".format(offset))
        images_of_tag = get_json(self.tag_info, params=dict(search=dumps(valid_tag_names), format="json", limit=10, offset=offset))
        print(images_of_tag)
        if images_of_tag.meta.total_count < 1 or len(images_of_tag.objects) < 1:
            error_message = InlineQueryResultArticle(
                id="404i:"+string,
                title=u"\"{tag}\" not found.".format(tag=string),
                input_message_content=InputTextMessageContent(string),
                description="Search results no images.",
                thumb_url=self.error_image
            )
            try:
                self.bot.answer_inline_query(inline_query_id, [error_message])
            except TgApiException:
                logger.exception("Answering query failed.")
            return
        if images_of_tag.meta.next:
            next_offset = offset+10
        for img in images_of_tag.objects:
            # image = self.root + tag.objects[0].resizes.small
            image_full = self.root + img.image
            image_small = image_full
            if "resizes" in img and "small" in img.resizes:
                image_small = self.root + img.resizes.small
            if "thumbnails" in img:
                if "png" in img.thumbnails:
                    image_small = self.root + img.thumbnails.png
                elif "jpg" in img.thumbnails:
                    image_small = self.root + img.thumbnails.jpg
            image_gif = self.root + img.thumbnails.gif if "gif" in img.thumbnails else None
            tag_total_count = images_of_tag.meta.total_count
            id = "mlfw-{id}".format(id=img.id)
            if not id:
                logger.error("NO ID: {}".format(img))
                continue
            logger.debug("id: {id}".format(id=id))
            # results.append(InlineQueryResultArticle(id=id, thumb_url=image_small, title=u"{tag}".format(tag=img.title), message_text=image_full, description=img.description))
            if image_gif:
                results.append(InlineQueryResultGif(id=id, title=img.title, gif_url=image_full, thumb_url=image_small, caption=self.str_to_caption(string)))
            else:
                results.append(InlineQueryResultPhoto(id=id, title=img.title, photo_url=image_full, thumb_url=image_small, caption=self.str_to_caption(string)))
        for res in results:
            logger.debug(res.to_array())
        logger.debug("next_offset=" + str(next_offset))
        try:
            self.bot.answer_inline_query(inline_query_id, results, cache_time=300, next_offset=next_offset)
        except TgApiException:
            logger.exception("Answering query failed.")
        # end try
    # end def

    def str_to_caption(self, search_string):
        return "#{search}".format(search=search_string.strip().lower().replace(" ", "_"))
    # end def str_to_caption
# end class

if __name__ == '__main__':
    main()