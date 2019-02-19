# -*- coding: utf-8 -*-
from abc import abstractmethod
from luckydonaldUtils.logger import logging
from luckydonaldUtils.exceptions import assert_type_or_raise
from os import path as os_path
import requests

try:  # python 2:
    # noinspection PyCompatibility
    from urlparse import urlparse
except ImportError:  # python 3:
    # noinspection PyCompatibility
    from urllib.parse import urlparse
# end try


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
    def __new__(cls, *outer_args, file_id=None, path=None, url=None, blob=None, mime=None, **outer_kwargs):
        """
        Simply calls :meth:`InputFile.factory` to produce a fitting subclass.
        """
        # https://stackoverflow.com/a/5953974/3423324#using-a-class-new-method-as-a-factory
        if cls is InputFile:
            # not a subclass
            # make a subclass
            outer_kwargs.update({
                'file_id': file_id,
                'path': path,
                'url': url,
                'blob': blob,
                'mime': mime,
                'create_instance': False,
            })
            clazz, args, kwargs = cls.factory(*outer_args, **outer_kwargs)
            if clazz is str:
                return args[0]  # for string we return only the string.
            # end if
            return super(InputFile, cls).__new__(clazz)
        else:
            # already is subclass
            # proceed in the usual __new__ creation
            return super(InputFile, cls).__new__(cls)
        # end if
    # end def

    def __init__(self, *args, name="file.unknown", mime=None, **kwargs):
        super(InputFile, self).__init__()
        if not name:
            raise ValueError("Cannot have empty name (name argument).")
        # end
        if not name:
            raise ValueError("Cannot have empty mime (mime argument).")
        # end

        self.name = name
        self.mime = mime
        self._size = None
    # end def

    @abstractmethod
    def get_request_files(self, var_name):
        """
        Returns a dictionary containing attachments as `{var_name: ('foo.png', open('foo.png', 'rb'), 'image/png')}`.
        For the format of thoses tuples see the requests docs:
        http://docs.python-requests.org/en/master/user/advanced/#post-multiple-multipart-encoded-files

        Used by :py:func:`~pytgbot.bot.Bot._do_fileupload`.

        :param var_name: The variable name we want to send the file as.
        :type  var_name: str

        :return: A dictionary, containing attachments how they are needed by the requests library.
        :rtype: dict
        """
        raise NotImplementedError('Your sub-class should implement this.')
    # end def

    def get_input_media_referenced_files(self, var_name):
        """
        Generates a tuple with the value for the json/url argument and a dictionary for the multipart file upload.
        Will return something which might be similar to
        `('attach://{var_name}', {var_name: ('foo.png', open('foo.png', 'rb'), 'image/png')})`

        or in the case of the :class:`InputFileUseFileID` class, just
        `('AwADBAADbXXXXXXXXXXXGBdhD2l6_XX', None)`

        :param var_name: name used to reference the file.
        :type  var_name: str

        :return: tuple of (file_id, dict)
        :rtype: tuple
        """
        # file to be uploaded
        string = 'attach://{name}'.format(name=var_name)
        return string, self.get_request_files(var_name)
    # end def

    @abstractmethod
    def _calculate_size(self):
        """
        Calculates the filesize in bytes.
        Used by :py:func:`~pytgbot.api_types.sendable.files.InputFile.size`.

        :return: Filesize in bytes
        :rtype: int
        """
        raise NotImplementedError('Your sub-class should implement this.')
    # end def

    @property
    def size(self):
        if not self._size:
            self._size = self._calculate_size()
        # end def
        return self._size
    # end def

    # noinspection PyShadowingNames
    @classmethod
    def factory(
            cls, file_id=None, path=None, url=None, blob=None, mime=None,
            prefer_local_download=True, prefer_str=False, create_instance=True
    ):
        """
        Creates a new InputFile subclass instance fitting the given parameters.

        :param prefer_local_download: If `True`, we download the file and send it to telegram. This is the default.
                                      If `False`, we send Telegram just the URL, and they'll try to download it.
        :type  prefer_local_download: bool

        :param prefer_str: Return just the `str` instead of a `InputFileUseFileID` or `InputFileUseUrl` object.
        :type  prefer_str: bool

        :param create_instance: If we should return a instance ready to use (default),
                                or the building parts being a tuple of `(class, args_tuple, kwargs_dict)`.
                                Setting this to `False` is probably only ever required for internal usage
                                by the :class:`InputFile` constructor which uses this very factory.
        :type  create_instance: bool


        :returns: if `create_instance=True` it returns a instance of some InputFile subclass or a string,
                  if `create_instance=False` it returns a tuple of the needed class, args and kwargs needed
                  to create a instance.
        :rtype: InputFile|InputFileFromBlob|InputFileFromDisk|InputFileFromURL|str|tuple
        """
        if create_instance:
            clazz, args, kwargs = cls.factory(
                file_id=file_id,
                path=path,
                url=url,
                blob=blob,
                mime=mime,
                create_instance=False,
            )
            return clazz(*args, **kwargs)
        if file_id:
            if prefer_str:
                assert_type_or_raise(file_id, str, parameter_name='file_id')
                return str, (file_id,), dict()
            # end if
            return InputFileUseFileID, (file_id,), dict()
        if blob:
            name = "file"
            suffix = ".blob"
            if path:
                name = os_path.basename(os_path.normpath(path))  # http://stackoverflow.com/a/3925147/3423324#last-part
                name, suffix = os_path.splitext(name)  # http://stackoverflow.com/a/541394/3423324#extension
            elif url:
                # http://stackoverflow.com/a/18727481/3423324#how-to-extract-a-filename-from-a-url
                url = urlparse(url)
                name = os_path.basename(url.path)
                name, suffix = os_path.splitext(name)
            # end if
            if mime:
                import mimetypes
                suffix = mimetypes.guess_extension(mime)
                suffix = '.jpg' if suffix == '.jpe' else suffix  # .jpe -> .jpg
            # end if
            if not suffix or not suffix.strip().lstrip("."):
                logger.debug("suffix was empty. Using '.blob'")
                suffix = ".blob"
            # end if
            name = "{filename}{suffix}".format(filename=name, suffix=suffix)
            return InputFileFromBlob, (blob,), dict(name=name, mime=mime)
        if path:
            return InputFileFromDisk, (path,), dict(mime=mime)
        if url:
            if prefer_local_download:
                return InputFileFromURL, (url,), dict(mime=mime)
            # end if
            # else -> so we wanna let telegram handle it
            if prefer_str:
                assert_type_or_raise(url, str, parameter_name='url')
                return str, (url,), dict()
            # end if
            return InputFileUseUrl, (url,), dict()

        # end if
        raise ValueError('Could not find a matching subclass. You might need to do it manually instead.')
    # end def
# end class InputFile


class BaseInputFileUse(InputFile):
    def get_request_files(self, var_name):
        """
        Returns a dictionary containing attachments as `{var_name: ('foo.png', open('foo.png', 'rb'), 'image/png')}`.
        - Just in this case it's an empty :class:`dict` as we don't have any files to send.

        Used by :py:func:`~pytgbot.bot.Bot._do_fileupload`.
        :param var_name: The variable name we want to send the file as.
        :return: An empty dictionary, `{}`
        """
        return dict()
    # end def
# end def


class InputFileUseFileID(BaseInputFileUse):
    def __init__(self, file_id, **kwargs):
        super(InputFileUseFileID, self).__init__(**kwargs)
        assert_type_or_raise(file_id, str, 'file_id')
        self.file_id = file_id
    # end def

    def get_input_media_referenced_files(self, var_name):
        """
        Generates a tuple with the value for the json/url argument and a empty dictionary for the multipart file part.
        Empty, because we have no files to send.

        Will return something which might be similar to `('AwADBAADbXXXXXXXXXXXGBdhD2l6_XX', None)`.

        :param var_name: unused field name.
        :type  var_name: str

        :return: tuple of (file_id, None)
        :rtype: tuple
        """
        return self.file_id, None
    # end def
# end class


class InputFileUseUrl(BaseInputFileUse):
    def __init__(self, url, **kwargs):
        super(InputFileUseUrl, self).__init__(**kwargs)
        assert_type_or_raise(url, str, 'url')
        self.url = url
    # end def

    def get_input_media_referenced_files(self, var_name):
        """
        Generates a tuple with the value for the json/url argument and a empty dictionary for the multipart file part.
        Empty, because we have no files to send.

        Will return something which might be similar to `('http://.../foo.png', None)`.

        :param var_name: unused field name.
        :type  var_name: str

        :return: tuple of (file_id, None)
        :rtype: tuple
        """
        return self.url, None
    # end def
# end class


class InputFileFromBlob(InputFile):
    def __init__(self, blob, name="file.unknown", mime=None, **kwargs):
        if not blob:
            raise ValueError("The file content (blob argument) is required to be non-empty.")
        # end if
        if not name:
            raise ValueError("Cannot have empty name (name argument).")
        # end

        if not mime:
            mime = self.mime_from_blob(blob)
        # end if

        self.blob = blob
        super(InputFileFromBlob, self).__init__(name=name, mime=mime, **kwargs)
    # end def

    @staticmethod
    def mime_from_blob(blob):
        """
        Calculates the mime type from the given blob
        :return:
        """
        import magic  # pip install python-magic
        return magic.from_buffer(blob, mime=True)
    # end def

    def get_request_files(self, var_name):
        return {var_name: (self.name, self.blob, self.mime)}
    # end def get_request_files

    def _calculate_size(self):
        return len(self.blob)
    # end def

# end class InputFile


class InputFileFromDisk(InputFile):
    def __init__(self, path, name=None, mime=None, **kwargs):
        if not path:
            raise ValueError("The file path (path argument) is required to be non-empty.")
        # end if

        name = name if name else os_path.basename(path)

        if not mime:
            mime = self.mime_from_file(path)
        # end if

        self.path = path
        super(InputFileFromDisk, self).__init__(name=name, mime=mime, **kwargs)
    # end def __init__

    @staticmethod
    def mime_from_file(path):
        """
        Calculates the mime type from the given path
        :return:
        """
        import magic  # pip install python-magic
        return magic.from_file(path, mime=True)
    # end def

    def get_request_files(self, var_name):
        return {var_name: (self.name, open(self.path, 'rb'), self.mime)}
    # end def

    def _calculate_size(self):
        from os import stat
        return stat(self.path).st_size
    # end def
# end class


class InputFileFromURL(InputFile):
    def __init__(self, url, name=None, mime=None, **kwargs):
        if not url:
            raise ValueError("The url (url argument) is required to be non-empty.")
        # end if

        # BLOB
        request = requests.get(url)
        if not request.status_code == 200:
            raise ValueError("Status code of request wasn't 200, but {!r}".format(request.status_code))
        # end if
        blob = request.content

        # NAME
        if name:
            name = name
        else:
            name = self.name_from_url(url)
        # end if

        # MIME
        if mime:
            mime = mime
        else:
            mime = InputFileFromBlob.mime_from_blob(blob)
        # end if
        self.url = url
        self.request = request
        self.blob = blob
        super(InputFileFromURL, self).__init__(name=name, mime=mime, **kwargs)
    # end def

    def __str__(self):
        file_size = len(self.blob)
        return (
            "{clazz_name!s}("
            "url={self.url!r}, name={self.name!r}, mime={self.mime!r}, "
            "size={file_size})"
        ).format(clazz_name=self.__class__.__name__, file_size=file_size, self=self)
    # end def __str__

    @staticmethod
    def name_from_url(url):
        """
        Cuts a name from an url
        :return: Filename
        :rtype: str
        """
        path_part = urlparse(url).path
        return os_path.basename(path_part)
        # end if
    # end def

    def get_request_files(self, var_name):
        return {var_name: (self.name, self.blob, self.mime)}
    # end def get_request_files

    def _calculate_size(self):
        return len(self.blob)
    # end def
# end class InputFileFromURL
