import unittest
from base64 import b64decode
from pytgbot.api_types.sendable.files import InputFile
from pytgbot.api_types.sendable.files import InputFileFromURL, InputFileUseUrl
from pytgbot.api_types.sendable.files import InputFileUseFileID
from pytgbot.api_types.sendable.files import InputFileFromDisk
from pytgbot.api_types.sendable.files import InputFileFromBlob

IMG = "https://derpicdn.net/img/view/2017/5/16/1438309.png"
IMG_FILENAME = '1438309.png'
IMG_MIME = 'image/png'
FILE_ID = 'AwADBAADbXXXXXXXXXXXGBdhD2l6XX'
FORM_VALUE = 'pony'
OS_FILE = __file__
OS_FILE_NAME = 'test_files.py'
OS_FILE_MIME = 'text/x-python'

BLOB = b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAABAlBMVEUAAADlcXHnb2/ZRUXkcnLmcnLkcnLfXl7TLy/l'
    b'cnLeW1vlcnLjcnLmc3PbTk7idHTmc3PwkV/vkWHvlWrwmm3ynm/2qW78umr9wmrriHb2rnv9v2L+y3//wGL/uFH+yn78'
    b'wn7ofHT/uE3/xG3pgnX/ulTyoHnmd3T/pyXvnSLtnCXzpjP/t03/vl/3sXzxnnnvlXjunSTvnyT/qiT9piT+piX+piXr'
    b'miTmlyPvozL+piX+piX/pib9piTwnST/uE//vFr/pyb+pyX+pib+piX2oSX9pSb+pyb/pyf/pSX/pib9pyT/pSb+pyb/'
    b'qSfzpTL9pyT2pzL/pib4qTP6qTH4rj920d5MAAAAVnRSTlMATYjWffD+///U/+XCUv9YvmaQpK+2rJyT//+A/31h////'
    b'Wv//////S6vD4v//////uJQ5jNr+////87pymv///2vQ4MP/esg0UjyTNqpc/4X/X//N9yBRhkgAAAHYSURBVHgBYqA1'
    b'GAWMTMzMTIxka2dhZWMHcD4XBxAEMAgAc8a6u2v/LZ57Xuz8E8A0DZyOsokFwDZNG4AlGzj4PIAjNBcAHhNuXCF5ePB9'
    b'PATCCfGHrQBFKBGUSBgxlFgYCZREGCmUVBgZlEwYOZRcGAWUQhhlhT9VyT2o8afmHjTtX4Wq7YTRD+OED0zj0AtjXtpx'
    b'xds6tsvMPbhQUlcJCkMxFIazkMEdUpyDu7vtfy24hYbOvd/7+euN/f0F4on7PBEP/P3FLALJVDrDzt9FNpfP57KX+Z/D'
    b'mUKxRAbKFaBaqzM7l92Lw1yvVdFotshbE8AjwLHIIxGIxPgeuGi0vY6Ou84twNzt9Ryn1+sy3wId3DT69MMAMiC9AkCT'
    b'VEOYBjAixQgvYz0wBjzOYQKbANxPo2EXaNCXFj7pAcDjFKa2gSlJsA2AhJl9YCYCSQhVLVCFkBSBuX1gLgILCB0t0IGw'
    b'IME+QFLFNjDUvuSXsRYY49OSvtgGVvRlbRdokovoawHlGQgTm0CZFAPzQIVUDePAglRJ08CGfujjacsuWzzt6KeJSWBJ'
    b'HiZeAX2v/xv37LLXzl8xb3gGDvSv2RDAkV2OAIYlMtFer88LCcUAIb6+tgw0AaMAAGw2K1yqbj5cAAAAAElFTkSuQmCC'
)
BLOB_MIME = 'image/png'
BLOB_NAME_UNKNOWN = 'file.unknown'
BLOB_NAME_PNG = 'file.png'
BLOB_NAME1 = 'example.png'
BLOB_NAME2 = 'example.blob'


class FilesTest(unittest.TestCase):
    def test_InputFileFromURL(self):
        f = InputFileFromURL(IMG)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileFromURL)
        self.assertEqual(f.url, IMG)
        self.assertEqual(f.name, IMG_FILENAME)
        self.assertEqual(f.mime, IMG_MIME)
        self.assertEqual(f.get_request_files(FORM_VALUE), {FORM_VALUE: (IMG_FILENAME, f.blob, IMG_MIME)})
    # end def


class FilesFactoryTest(unittest.TestCase):
    def test_url(self):
        f = InputFile(url=IMG)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileFromURL)
        self.assertEqual(f.url, IMG)
        self.assertEqual(f.name, IMG_FILENAME)
        self.assertEqual(f.mime, IMG_MIME)
        self.assertEqual(f.get_request_files(FORM_VALUE), {FORM_VALUE: (IMG_FILENAME, f.blob, IMG_MIME)})
    # end def

    def test_url_str(self):
        f = InputFile(url=IMG, prefer_str=True)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileFromURL)
        self.assertEqual(f.url, IMG)
        self.assertEqual(f.name, IMG_FILENAME)
        self.assertEqual(f.mime, IMG_MIME)
        self.assertEqual(f.get_request_files(FORM_VALUE), {FORM_VALUE: (IMG_FILENAME, f.blob, IMG_MIME)})
    # end def

    def test_url_tg(self):
        f = InputFile(url=IMG, prefer_local_download=False)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileUseUrl)
        self.assertEqual(f.url, IMG)
        self.assertEqual(f.get_request_files(FORM_VALUE), {})
    # end def

    def test_url_tg_str(self):
        f = InputFile(url=IMG, prefer_local_download=False, prefer_str=True)
        self.assertIsInstance(f, str)
        self.assertEqual(f, IMG)
    # end def

    def test_file_id(self):
        f = InputFile(file_id=FILE_ID)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileUseFileID)
        self.assertEqual(f.file_id, FILE_ID)
        self.assertEqual(f.get_request_files(FORM_VALUE), {})
    # end def

    def test_file_id_str(self):
        f = InputFile(file_id=FILE_ID, prefer_str=True)
        self.assertIsInstance(f, str)
        self.assertEqual(f, FILE_ID)
    # end def

    def test_file_disk(self):
        f = InputFile(path=OS_FILE)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileFromDisk)
        self.assertEqual(f.name, OS_FILE_NAME)
        self.assertEqual(f.mime, OS_FILE_MIME)
        request_files = f.get_request_files(FORM_VALUE)
        # tuple(FORM_VALUE, {FORM_VALUE: (OS_FILE_NAME, os.open(...), OS_FILE_MIME)})
        # we can't compare the os.open result with anything,
        # so we need to manually compare the whole array.
        self.assertIn(FORM_VALUE, request_files, msg='key exist')
        self.assertListEqual(list(request_files.keys()), [FORM_VALUE], msg='key(s) correct')
        self.assertIsInstance(request_files[FORM_VALUE], tuple, msg='dict contains tuple')
        self.assertEqual(len(request_files[FORM_VALUE]), 3, msg='tuple has 3 elements')
        self.assertEqual(request_files[FORM_VALUE][0], OS_FILE_NAME, msg='first tuple element is correct filename')
        self.assertEqual(request_files[FORM_VALUE][1].name, OS_FILE, msg='second tuple element is probably opened file. We confirm only correct name.')
        self.assertEqual(request_files[FORM_VALUE][2], OS_FILE_MIME, msg='third tuple element is correct mime')
    # end def

    def test_file_blob(self):
        f = InputFile(blob=BLOB)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileFromBlob)
        self.assertEqual(f.name, BLOB_NAME_UNKNOWN)
        self.assertEqual(f.mime, BLOB_MIME)
        self.assertEqual(f.blob, BLOB)
        self.assertEqual(f.get_request_files(FORM_VALUE), {FORM_VALUE: (BLOB_NAME_UNKNOWN, BLOB, BLOB_MIME)})
    # end def

    def test_file_blob(self):
        f = InputFile(blob=BLOB)
        self.assertIsInstance(f, InputFile)
        self.assertIsInstance(f, InputFileFromBlob)
        self.assertEqual(f.name, BLOB_NAME_UNKNOWN)
        self.assertEqual(f.mime, BLOB_MIME)
        self.assertEqual(f.blob, BLOB)
        self.assertEqual(f.get_request_files(FORM_VALUE), {FORM_VALUE: (BLOB_NAME_UNKNOWN, BLOB, BLOB_MIME)})
    # end def





if __name__ == '__main__':
    unittest.main()
