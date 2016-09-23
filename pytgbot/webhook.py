# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot.bot import Bot
from pytgbot.exceptions import TgApiServerException, TgApiParseException

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Webhook(Bot):
    """
    Subclass of Bot, will be returned of a sucessful webhook setting.
    Differs with the normal Bot class, as the sending function stores the result to send,
    so you can actually get that and return the data on your incomming message.
    """

    stored_request = None

    def _prepare_request(self, command, query):
        """
        :param command: The Url command parameter
        :type  command: str

        :param query: will get json encoded.
        :type  query: dict

        :return:
        """
        from luckydonaldUtils.encoding import to_native as n
        from pytgbot.api_types.sendable import Sendable
        from pytgbot.api_types import as_array
        from DictObject import DictObject
        import json

        params = {}
        for key in query.keys():
            element = query[key]
            if element is not None:
                if isinstance(element, Sendable):
                    params[key] = json.dumps(as_array(element))
                else:
                    params[key] = element
        url = self._base_url.format(api_key=n(self.api_key), command=n(command))
        return DictObject(url=url, params=params)
    # end def

    def _do_request(self, url, params=None, files=None, use_long_polling=None, request_timeout=None):
        """

        :param url: The complete url to send to
        :type  url: str

        :keyword params: Parameter for that connection

        :keyword files: Optional files parameters

        :keyword use_long_polling: if it should use long polling.
                                (see http://docs.python-requests.org/en/latest/api/#requests.Response.iter_content)
        :type    use_long_polling: bool

        :keyword request_timeout: When the request should time out.
        :type    request_timeout: int

        :return: json data received
        :rtype: DictObject.DictObject
        """
        import requests
        r = requests.post(url, params=params, files=files, stream=use_long_polling,
                          verify=True, timeout=request_timeout)
        # No self signed certificates. Telegram should be trustworthy anyway...
        from DictObject import DictObject
        try:
            logger.debug("Response: {}".format(r.json()))
            json_data = DictObject.objectify(r.json())
        except Exception:
            logger.exception("Parsing answer failed.\nRequest: {r!s}\nContent: {r.content}".format(r=r))
            raise
        # end if
        json_data["response"] = r  # TODO: does this failes on json lists? Does TG does that?
        return json_data
    # end def

    def _process_response(self, json_data):
        # TG should always return an dict, with at least a status or something.
        if self.return_python_objects:
            if json_data.ok != True:
                raise TgApiServerException(
                    error_code=json_data.error_code if "error_code" in json_data else None,
                    response=json_data.response if "response" in json_data else None,
                    description=json_data.description if "description" in json_data else None,
                    request=r.request
                )
            # end if not ok
            if "result" not in json_data:
                raise TgApiParseException('Key "result" is missing.')
            # end if no result
            return json_data.result
        # end if return_python_objects
        return json_data
    # end def

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

        :keyword request_timeout: When the request should time out.
        :type    request_timeout: int

        :keyword files: if it needs to send files.

        :keyword use_long_polling: if it should use long polling.
                                (see http://docs.python-requests.org/en/latest/api/#requests.Response.iter_content)
        :type    use_long_polling: bool

        :param query: will get json encoded.

        :return: The json response from the server, or, if `self.return_python_objects` is `True`, a parsed return type.
        :rtype: DictObject.DictObject | pytgbot.api_types.receivable.Receivable
        """
        params = self._prepare_request(command, query)
        r = self._do_request(
            params.url, params=params.params,
            files=files, stream=use_long_polling,  timeout=request_timeout
        )
        return self._process_response(r)






    # end def do
