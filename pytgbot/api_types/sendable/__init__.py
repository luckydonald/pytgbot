# -*- coding: utf-8 -*-
from os import path
import requests
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["inline", "reply_markup", "Sendable", "InputFile", "InputFileFromURL", "InputFileFromDisk"]
logger = logging.getLogger(__name__)


class Sendable(TgBotApiObject):
    def __init__(self):
        super(Sendable, self).__init__()
    # end def __init__
# end class


class InputFile(object):
    def __init__(self, file_blob, file_name=None, file_mime=None):
        super(InputFile, self).__init__()
        self.file_blob = file_blob
        self.file_name = file_name if file_name else None
        self.file_mime = file_mime if file_mime else None
    # end def __init__

    def get_request_files(self, var_name):
        return {var_name: (self.file_name, self.file_blob, self.file_mime)}
    # end def get_request_files
# end class InputFile


class InputFileFromDisk(InputFile):
    def __init__(self, file_path, file_name=None, file_mime=None):
        super(InputFile, self).__init__()
        self.file_path = file_path
        self.file_name = file_name if file_name else path.basename(file_path)
        self.file_mime = file_mime if file_mime else None
    # end def __init__

    def get_request_files(self, var_name):
        return {var_name: (self.file_name, open(self.file_path, 'rb'), self.file_mime)}
    # end def get_request_files
# end class InputFileFromDisk


class InputFileFromURL(InputFile):
    def __init__(self, file_url, file_name=None, file_mime=None):
        super(InputFileFromURL, self).__init__(None, file_name, file_mime)
        self.file_url = file_url
        self.file = requests.get(file_url)
        self.file_name = file_name if file_name else None
        self.file_mime = file_mime if file_mime else None
        self.url_to_name_and_mime()
    # end def __init__

    def __str__(self):
        file_size = len(self.file.content)
        return (
            "{clazz_name!s}("
             "file_url={self.file_url!r}, file_name={self.file_name!r}, file_mime={self.file_mime!r}, "
            "file_size={file_size}"
        ).format(clazz_name=self.__class__.__name__, file_size=file_size, self=self)
    # end def __str__

    def url_to_name_and_mime(self):
        if not self.file_name:
            import os  # http://stackoverflow.com/a/18727481/3423324
            try:  # python 2:
                from urlparse import urlparse
            except ImportError:  # python 3:
                from urllib.parse import urlparse
            # end try
            path_part = urlparse(self.file_url).path
            self.file_name = os.path.basename(path_part)
        # end if
        if not self.file_mime:
            import magic  # pip install python-magic
            self.file_mime = magic.from_buffer(requests.get(self.file_url).content, mime=True)
        # end if
    # end def



    def get_request_files(self, var_name):
        return {var_name: (self.file_name, self.file.content, self.file_mime)}
    # end def get_request_files
# end class InputFileFromURL
