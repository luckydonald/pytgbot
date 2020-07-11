# -*- coding: utf-8 -*-

import re

from datetime import timedelta, datetime
from DictObject import DictObject

from luckydonaldUtils.logger import logging

from ..exceptions import TgApiParseException, TgApiException, TgApiTypeError
from .bot import BotBase


__author__ = 'luckydonald'
__all__ = ["SyncBot", "Bot"]

logger = logging.getLogger(__name__)


class SyncBot(BotBase):
    def get_updates(self, offset=None, limit=100, poll_timeout=0, allowed_updates=None, request_timeout=None, delta=timedelta(milliseconds=100), error_as_empty=False):
        """
        Use this method to receive incoming updates using long polling. An Array of Update objects is returned.

        You can choose to set `error_as_empty` to `True` or `False`.
        If `error_as_empty` is set to `True`, it will log that exception as warning, and fake an empty result,
        intended for use in for loops. In case of such error (and only in such case) it contains an "exception" field.
        Ìt will look like this: `{"result": [], "exception": e}`
        This is useful if you want to use a for loop, but ignore Network related burps.

        If `error_as_empty` is set to `False` however, all `requests.RequestException` exceptions are normally raised.

        :keyword offset: (Optional)	Identifier of the first update to be returned.
                 Must be greater by one than the highest among the identifiers of previously received updates.
                 By default, updates starting with the earliest unconfirmed update are returned.
                 An update is considered confirmed as soon as :func:`get_updates` is called with
                 an offset higher than its `update_id`.
        :type offset: int

        :param limit: Limits the number of updates to be retrieved. Values between 1—100 are accepted. Defaults to 100
        :type  limit: int

        :param poll_timeout: Timeout in seconds for long polling, e.g. how long we want to wait maximum.
                               Defaults to 0, i.e. usual short polling.
        :type  poll_timeout: int

        :param allowed_updates: List the types of updates you want your bot to receive.
                                  For example, specify [“message”, “edited_channel_post”, “callback_query”] to only
                                  receive updates of these types. See Update for a complete list of available update
                                  types. Specify an empty list to receive all updates regardless of type (default).
                                  If not specified, the previous setting will be used. Please note that this parameter
                                  doesn't affect updates created before the call to the get_updates,
                                  so unwanted updates may be received for a short period of time.
        :type allowed_updates: list of str


        :param request_timeout: Timeout of the request. Not the long polling server side timeout.
                                  If not specified, it is set to `poll_timeout`+2.
        :type request_timeout: int

        :param delta: Wait minimal 'delta' seconds, between requests. Useful in a loop.
        :type  delta: datetime.

        :param error_as_empty: If errors which subclasses `requests.RequestException` will be logged but not raised.
                 Instead the returned DictObject will contain an "exception" field containing the exception occured,
                 the "result" field will be an empty list `[]`. Defaults to `False`.
        :type  error_as_empty: bool


        Returns:

        :return: An Array of Update objects is returned,
                 or an empty array if there was an requests.RequestException and error_as_empty is set to True.
        :rtype: list of pytgbot.api_types.receivable.updates.Update
        """
        from time import sleep
        import requests

        assert(offset is None or isinstance(offset, int))
        assert(limit is None or isinstance(limit, int))
        assert(poll_timeout is None or isinstance(poll_timeout, int))
        assert(allowed_updates is None or isinstance(allowed_updates, list))
        if poll_timeout and not request_timeout is None:
            request_timeout = poll_timeout + 2
        # end if

        if delta.total_seconds() > poll_timeout:
            now = datetime.now()
            if self._last_update - now < delta:
                wait = ((now - self._last_update) - delta).total_seconds()  # can be 0.2
                wait = 0 if wait < 0 else wait
                if wait != 0:
                    logger.debug("Sleeping {i} seconds.".format(i=wait))
                # end if
                sleep(wait)
            # end if
        # end if
        self._last_update = datetime.now()
        use_long_polling = poll_timeout != 0
        try:
            result = self.do(
                "getUpdates", offset=offset, limit=limit, timeout=poll_timeout, allowed_updates=allowed_updates,
                use_long_polling=use_long_polling, request_timeout=request_timeout
            )
            if self.return_python_objects:
                logger.debug("Trying to parse {data}".format(data=repr(result)))
                from pytgbot.api_types.receivable.updates import Update
                try:
                    return Update.from_array_list(result, list_level=1)
                except TgApiParseException:
                    logger.debug("Failed parsing as api_type Update", exc_info=True)
                # end try
                # no valid parsing so far
                raise TgApiParseException("Could not parse result.")  # See debug log for details!
            # end if return_python_objects
            return result
        except (requests.RequestException, TgApiException) as e:
            if error_as_empty:
                if not isinstance(e, requests.exceptions.Timeout) or not use_long_polling:
                    logger.warn(
                        "Network related error happened in get_updates(), but will be ignored: " + str(e),
                        exc_info=True
                    )
                # end if
                self._last_update = datetime.now()
                return DictObject(result=[], exception=e)
            else:
                raise
            # end if
        # end try
    # end def get_updates

    def do(self, command, files=None, use_long_polling=False, request_timeout=None, **query):
        """
        Send a request to the api.

        If the bot is set to return the json objects, it will look like this:

        ```json
        {
            "ok": bool,
            "result": {...},
            # optionally present:
            "description": "human-readable description of the result",
            "error_code": int
        }
        ```

        :param command: The Url command parameter
        :type  command: str

        :param request_timeout: When the request should time out. Default: `None`
        :type  request_timeout: int

        :param files: if it needs to send files.

        :param use_long_polling: if it should use long polling. Default: `False`
                                (see http://docs.python-requests.org/en/latest/api/#requests.Response.iter_content)
        :type  use_long_polling: bool

        :param query: all the other `**kwargs` will get json encoded.

        :return: The json response from the server, or, if `self.return_python_objects` is `True`, a parsed return type.
        :rtype:  DictObject.DictObject | pytgbot.api_types.receivable.Receivable
        """
        import requests

        url, params = self._prepare_request(command, query)
        logger.debug('Sending sync request to url {url!r} with params: {params!r}'.format(url=url, params=params))
        r = requests.post(
            url, params=params, files=files, stream=use_long_polling,
            verify=True,  # No self signed certificates. Telegram should be trustworthy anyway...
            timeout=request_timeout
        )
        json = r.json()
        return self._postprocess_request(r.request, response=r, json=json)
    # end def do

    def _do_fileupload(self, file_param_name, value, _command=None, _file_is_optional=False, **kwargs):
        """
        :param file_param_name: For what field the file should be uploaded.
        :type  file_param_name: str

        :param value: File to send. You can either pass a file_id as String to resend a file
                      file that is already on the Telegram servers, or upload a new file,
                      specifying the file path as :class:`pytgbot.api_types.sendable.files.InputFile`.
                      If `_file_is_optional` is set to `True`, it can also be set to `None`.
        :type  value: pytgbot.api_types.sendable.files.InputFile | str | None

        :param _command: Overwrite the command to be send.
                         Default is to convert `file_param_name` to camel case (`"voice_note"` -> `"sendVoiceNote"`)
        :type  _command: str|None

        :param _file_is_optional: If the file (`value`) is allowed to be None.
        :type  _file_is_optional: bool

        :param kwargs: will get json encoded.

        :return: The json response from the server, or, if `self.return_python_objects` is `True`, a parsed return type.
        :rtype: DictObject.DictObject | pytgbot.api_types.receivable.Receivable

        :raises TgApiTypeError, TgApiParseException, TgApiServerException: Everything from :meth:`Bot.do`, and :class:`TgApiTypeError`
        """
        from ..api_types.sendable.files import InputFile
        from luckydonaldUtils.encoding import unicode_type
        from luckydonaldUtils.encoding import to_native as n

        if value is None and _file_is_optional:
            # Is None but set optional, so do nothing.
            pass
        elif isinstance(value, str):
            kwargs[file_param_name] = str(value)
        elif isinstance(value, unicode_type):
            kwargs[file_param_name] = n(value)
        elif isinstance(value, InputFile):
            files = value.get_request_files(file_param_name)
            if "files" in kwargs and kwargs["files"]:
                # already are some files there, merge them.
                assert isinstance(kwargs["files"], dict), \
                    'The files should be of type dict, but are of type {}.'.format(type(kwargs["files"]))
                for key in files.keys():
                    assert key not in kwargs["files"], '{key} would be overwritten!'
                    kwargs["files"][key] = files[key]
                # end for
            else:
                # no files so far
                kwargs["files"] = files
            # end if
        else:
            raise TgApiTypeError("Parameter {key} is not type (str, {text_type}, {input_file_type}), but type {type}".format(
                key=file_param_name, type=type(value), input_file_type=InputFile, text_type=unicode_type))
        # end if
        if not _command:
            # command as camelCase  # "voice_note" -> "sendVoiceNote"  # https://stackoverflow.com/a/10984923/3423324
            command = re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), "send_" + file_param_name)
        else:
            command = _command
        # end def
        return self.do(command, **kwargs)
    # end def _do_fileupload
# end class Bot

Bot = SyncBot
