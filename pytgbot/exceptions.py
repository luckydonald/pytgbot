# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class TgApiException(BaseException):
    """
    Base Class for all exceptions.
    """
    pass
# end class TgApiException


class TgApiServerException(TgApiException):
    """
    Raised if the api returns "ok" == false
    """
    def __init__(self, error_code=None, response=None, description=None, request=None):
        super(TgApiServerException, self).__init__(description)
        self.error_code = error_code
        self.response = response
        self.description = description
        self.request=request
    # end def __init__

    def __str__(self, *args, **kwargs):
        return "TgApiServerException(error_code={self.error_code!r}, response={self.response!r}, " \
               "description={self.description!r}, request={self.request!r})".format(self=self)
    # end def __str__
# end class TgApiException


class TgApiParseException(TgApiException):
    """
    Raised if something did go wrong with parsing.
    E.g. a missing key, an unexpected value, etc.
    """
    pass


class TgApiTypeError(TgApiException, TypeError):
    """ Raised where a TypeError is needed"""
    pass