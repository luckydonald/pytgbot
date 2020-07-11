# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class TgApiException(Exception):
    """
    Base Class for all exceptions.
    """
    pass
# end class TgApiException


class TgApiResponseException(TgApiException):
    """
    Server responded something, but that can't be parsed as json.
    Contains the `response`, and also direct access to the `status_code` of that response.
    """
    def __init__(self, message, response=None, exception=None):
        """
        :param message: The message of the exception
        :type  message: str

        :param response: The failed response
        :type  response: requests.Response

        :param exception: The exception which occured when parsing the json.
        :type  exception:
        """
        super(TgApiResponseException, self).__init__(message)
        self.response = response
        self.exception = exception
    # end def

    @property
    def status_code(self):
        return self.response.status_code if self.response is not None else None
    # end def

    def __str__(self):
        return "{msg} [{code}] {e_type}({e_text!r})".format(
            code=self.status_code, e_type=self.exception.__class__.__name__,
            e_text=self.exception.args[0] if len(self.exception.args) == 1 else self.exception.args,
            msg=self.args[0] if len(self.args) == 1 else self.args,
        )
    # end def

    def __repr__(self):
        return "{cls}({msg!r}, response={r!r}, exception={e!r})".format(
            cls=self.__class__.__name__, r=self.response, e=self.exception,
            msg=self.args[0] if len(self.args) == 1 else self.args,
        )
    # end def
# end class


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
