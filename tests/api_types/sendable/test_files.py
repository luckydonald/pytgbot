import unittest
from pytgbot.api_types.sendable.files import InputFileFromURL


class FilesTest(unittest.TestCase):
    def test_InputFileFromURL(self):
        i = InputFileFromURL("https://derpicdn.net/img/view/2017/5/16/1438309.png")
        self.assertEqual(i.file_url, "https://derpicdn.net/img/view/2017/5/16/1438309.png")
        self.assertEqual(i.file_name, '1438309.png')
        self.assertEqual(i.file_mime, 'image/png')
        self.assertEqual(i.get_request_files('pony'), {'pony': ('1438309.png', i.file_blob, 'image/png')})
    # end def




if __name__ == '__main__':
    unittest.main()
