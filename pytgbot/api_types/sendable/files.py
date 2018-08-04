# -*- coding: utf-8 -*-
from abc import abstractmethod
from luckydonaldUtils.logger import logging
from os import path
import requests


__author__ = 'luckydonald'
__all__ = ["InputFile", "InputFileFromURL", "InputFileFromDisk", "InputFileFromBlob"]
logger = logging.getLogger(__name__)


class InputFile(object):
    """
    This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

    https://core.telegram.org/bots/api#inputfile


    Sending Files:

    There are three ways to send files (photos, stickers, audio, media, etc.):

        1. If the file is already stored somewhere on the Telegram servers, you don't need to reupload it:
           Each file object has a `file_id` field, simply pass this `file_id` as a `str` parameter
           instead of uploading as :class:`InputFile`. There are no size limits for files resend this way.

        2. Provide Telegram with an HTTP URL (:class:`str`) for the file to be sent, instead of any :class:`InputFile`.
           Telegram will download and send the file. 5 MB max size for photos and 20 MB max for other types of content.

        3. Post the file using multipart/form-data in the usual way that files are uploaded via the browser.
           This is what any :class:`InputFile` (subclass) does automatically,
           when send by the bot via the :py:func:`~pytgbot.bot.Bot._do_fileupload` method.
           10 MB max size for photos, 50 MB for other files.

    https://core.telegram.org/bots/api#sending-files
    """
    def __init__(self, file_blob=None, file_name="file.unknown", file_mime=None):
        super(InputFile, self).__init__()
        if file_blob:
            logger.warning("Deprecated! Use a InputFileFromBlob from pytgbot.api_types.sendable.files instead!")
        # end if
        if not file_name:
            raise ValueError("Cannot have empty name (file_name argument).")
        # end

        self.file_blob = file_blob
        self.file_name = file_name
        if file_mime:
            self.file_mime = file_mime
        elif self.file_blob:
            self.file_mime = None
            self.update_mime_from_blob()
        # end if
    # end def

    def update_mime_from_blob(self):
        """
        Calculates the mime type from self.file_blob
        :return:
        """
        logger.warning("Deprecated! Use a InputFileFromBlob from pytgbot.api_types.sendable.files instead!")
        if not self.file_mime:
            import magic  # pip install python-magic
            self.file_mime = magic.from_buffer(self.file_blob, mime=True)
        # end if
    # end def

    @abstractmethod
    def get_request_files(self, var_name):
        """
        Used by :py:func:`~pytgbot.bot.Bot._do_fileupload`.
        :param var_name: The variable name we want to send the file as.
        :return:
        """
        raise NotImplementedError('Your subclass should implement this.')
        if not self.file_blob:
            logger.warning("Deprecated! Use a InputFileFromBlob from pytgbot.api_types.sendable.files instead!")
            raise DeprecationWarning("Deprecated! Use a InputFileFromBlob from pytgbot.api_types.sendable.files instead! I cannot work without file blob. Please use one of the classes overriding this funcion.")
        return {var_name: (self.file_name, self.file_blob, self.file_mime)}
    # end def get_request_files
# end class InputFile


class InputFileFromBlob(InputFile):
    def __init__(self, file_blob, file_name="file.unknown", file_mime=None):
        if not file_blob:
            raise ValueError("The file content (file_blob argument) is required to be non-empty.")
        # end if
        if not file_name:
            raise ValueError("Cannot have empty name (file_name argument).")
        # end

        self.file_blob = file_blob
        self.file_name = file_name
        if file_mime:
            self.file_mime = file_mime
        else:
            self.file_mime = None
            self.update_mime_from_blob()
        # end if

        super(InputFileFromBlob, self).__init__(file_name=file_name, file_mime=file_mime)
    # end def

    def update_mime_from_blob(self):
        """
        Calculates the mime type from self.file_blob
        :return:
        """
        if not self.file_mime:
            import magic  # pip install python-magic
            self.file_mime = magic.from_buffer(self.file_blob, mime=True)
        # end if
    # end def

    def get_request_files(self, var_name):
        return {var_name: (self.file_name, self.file_blob, self.file_mime)}
    # end def get_request_files
# end class InputFile


class InputFileFromDisk(InputFile):
    def __init__(self, file_path, file_name=None, file_mime=None):
        self.file_path = file_path
        self.file_name = file_name if file_name else path.basename(file_path)
        if file_mime:
            self.file_mime = file_mime
        else:  # can't use super.update_mime_from_blob() because we have no blob.
            import magic  # pip install python-magic
            self.file_mime = magic.from_file(self.file_path, mime=True)
        # end if file_mime
        super(InputFileFromDisk, self).__init__(file_name=self.file_name, file_mime=self.file_mime)
    # end def __init__

    def get_request_files(self, var_name):
        return {var_name: (self.file_name, open(self.file_path, 'rb'), self.file_mime)}
    # end def get_request_files
# end class InputFileFromDisk


class InputFileFromURL(InputFile):
    def __init__(self, file_url, file_name=None, file_mime=None):
        # URL
        self.file_url = file_url

        # BLOB
        self.update_blob_from_url()

        # NAME
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = None
            self.update_name_from_url()
        # end if

        # MIME
        if file_mime:
            self.file_mime = file_mime
        else:
            self.file_mime = None
            self.update_mime_from_blob()
        # end if
        super(InputFileFromURL, self).__init__(self.file_blob, self.file_name, self.file_mime)
    # end def __init__

    def __str__(self):
        file_size = len(self.file_blob)
        return (
            "{clazz_name!s}("
             "file_url={self.file_url!r}, file_name={self.file_name!r}, file_mime={self.file_mime!r}, "
            "file_size={file_size}"
        ).format(clazz_name=self.__class__.__name__, file_size=file_size, self=self)
    # end def __str__

    def update_blob_from_url(self):
        """
        Loads the file from the url to self.file and self.file_blob
        :return:
        """
        self.file = requests.get(self.file_url)
        self.file_blob = self.file.content
    # end def

    def update_name_from_url(self):
        """
        Cuts a name from an url
        :return:
        """
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
    # end def

    def get_request_files(self, var_name):
        return {var_name: (self.file_name, self.file_blob, self.file_mime)}
    # end def get_request_files
# end class InputFileFromURL
