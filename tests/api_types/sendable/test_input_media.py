from pytgbot.api_types.sendable.files import InputFileFromURL
from pytgbot.api_types.sendable.input_media import InputMediaVideo
import unittest


class MyTestCase(unittest.TestCase):
    def test_InputMediaVideo_thumb_files(self):
        vid1 = 'https://derpicdn.net/img/view/2016/12/21/1322277.mp4'
        pic1 = 'https://derpicdn.net/img/2017/7/21/1491832/thumb.jpeg'
        i = InputMediaVideo(InputFileFromURL(vid1), InputFileFromURL(pic1))
        d = i.get_request_data('lel', full_data=True)
        self.assertEqual(d[0], {'type': 'video', 'thumb': 'attach://lel_thumb', 'media': 'attach://lel_media'})
        self.assertListEqual(list(d[1].keys()), ['lel_media', 'lel_thumb'])
        self.assertEqual(d[1]['lel_media'][0], '1322277.mp4', msg='Filename video')
        self.assertEqual(d[1]['lel_thumb'][0], 'thumb.jpeg', msg='Filename thumb')
    # end def
# end class


if __name__ == '__main__':
    unittest.main()
# end if
