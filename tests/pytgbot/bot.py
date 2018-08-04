from pytgbot.exceptions import TgApiServerException

from somewhere import API_KEY, TEST_CHAT
import unittest
from luckydonaldUtils.logger import logging
from pytgbot.bot import Bot
from pytgbot.api_types.receivable.media import PhotoSize
from pytgbot.api_types.receivable.updates import Message
from pytgbot.api_types.sendable.files import InputFileFromURL
from pytgbot.api_types.sendable.input_media import InputMediaPhoto
logging.add_colored_handler(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BotTest(unittest.TestCase):
    def setUp(self):
        self.bot = Bot(API_KEY)
        self.messages = []
    # end def


    def test_edit_message_media(self):
        # upload by url
        url1 = 'https://derpicdn.net/img/view/2012/1/22/1382.jpg'
        url2 = 'https://derpicdn.net/img/view/2016/2/3/1079240.png'
        #self.bot.send_photo(TEST_CHAT, url1, caption="url1")
        #self.bot.send_photo(TEST_CHAT, url2, caption="url2")

        msg = self.bot.send_photo(TEST_CHAT, url1, caption="unittest")
        self.messages.append(msg)
        print("msg 1: {!r}".format(msg))
        self.assertIsInstance(msg, Message)
        self.assertEqual(msg.caption, 'unittest')
        self.assertIn('photo', msg)
        self.assertIsInstance(msg.photo, list)

        msg_id = msg.message_id
        file_id = self._get_biggest_photo_fileid(msg)

        # edit by url
        msg2 = self.bot.edit_message_media(InputMediaPhoto(url2), TEST_CHAT, message_id=msg_id)
        self.messages.append(msg2)
        print("msg 2: {!r}".format(msg2))
        self.assertIsInstance(msg2, Message)
        self.assertIn('photo', msg2)
        self.assertIsInstance(msg2.photo, list)
        self.assertEqual(msg2.caption, None)
        file_id2 = self._get_biggest_photo_fileid(msg2)

        # edit by file_id
        msg3 = self.bot.edit_message_media(InputMediaPhoto(file_id), TEST_CHAT, message_id=msg_id)
        self.messages.append(msg3)
        print("msg 3: {!r}".format(msg3))
        self.assertIsInstance(msg3, Message)
        self.assertIn('photo', msg3)
        self.assertIsInstance(msg3.photo, list)
        file_id3 = self._get_biggest_photo_fileid(msg3)
        self.assertEqual(msg2.caption, None)
        self.assertEqual(file_id3, file_id)

        # edit by upload (url)
        msg4 = self.bot.edit_message_media(InputMediaPhoto(InputFileFromURL(url2)), TEST_CHAT, message_id=msg_id)
        self.messages.append(msg4)
        print("msg 4: {!r}".format(msg4))
        self.assertIsInstance(msg4, Message)
        self.assertIn('photo', msg4)
        self.assertIsInstance(msg4.photo, list)
        self.assertEqual(msg4.caption, None)
        file_id4 = self._get_biggest_photo_fileid(msg4)

        self.messages.append(self.bot.send_message(TEST_CHAT, 'done.'))
    # end def

    #
    # utils:
    #

    def _get_biggest_photo_fileid(self, msg):
        biggest = msg.photo[0]
        for photo in msg.photo:
            self.assertIsInstance(photo, PhotoSize)
            if photo.file_size > biggest.file_size:
                biggest = photo
            # end if
        # end for
        return biggest.file_id
    # end def

    def tearDown(self):
        if self.bot and self.messages:
            for msg in reversed(self.messages):
                try:
                    self.bot.delete_message(TEST_CHAT, msg.message_id)
                except Exception as e:
                    if (
                        isinstance(e, TgApiServerException) and e.error_code == 400 and
                        e.description == 'Bad Request: message to delete not found'
                    ):
                        logger.info('delete message fail, not found.')
                        continue
                    # end if
                    logger.debug('delete message fail.', exc_info=True)
                # end try
            # end for
        # end if
    # end def
# end class


if __name__ == '__main__':
    unittest.main()
# end def
