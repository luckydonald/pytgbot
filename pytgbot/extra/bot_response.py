# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
from luckydonaldUtils.encoding import to_native as n

from pytgbot import Bot

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class ResponseBot(Bot):
    """
    A :class:`Bot` subclass, not instantly sending responses, but instead returning them.
    Useful for replying responses to an open Webhook connection.
    """
    def __init__(self, api_key):
        super(ResponseBot, self).__init__(api_key, return_python_objects=True)
    # end def

    def do(self, command, files=None, use_long_polling=False, request_timeout=None, **query):
        """
        Return the request params we would send to the api.
        """
        url, params = self._prepare_request(command, query)
        return {
            "url": url, "params": params, "files": files, "stream": use_long_polling,
            "verify": True,  # No self signed certificates. Telegram should be trustworthy anyway...
            "timeout": request_timeout
        }
    # end def
# end class
