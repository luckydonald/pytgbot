# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from pytgbot.api_types import TgBotApiObject

__author__ = 'luckydonald'
__all__ = ["inline", "media", "peer", "responses", "updates", "Receivable", "Result"]
logger = logging.getLogger(__name__)


class Receivable(TgBotApiObject):
    pass
# end class Receivable


class Result(Receivable):
    def to_array(self):
        return {}
    pass
# end class Result

class WebhookInfo(Receivable):
    """
    Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    """

    def __init__(self, url, has_custom_certificate, pending_update_count, last_error_date=None,
                 last_error_message=None):
        """
        Contains information about the current status of a webhook.

        https://core.telegram.org/bots/api#webhookinfo


        Parameters:

        :param url: Webhook URL, may be empty if webhook is not set up
        :type  url: str

        :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
        :type  has_custom_certificate: bool

        :param pending_update_count: Number of updates awaiting delivery
        :type  pending_update_count: int


        Optional keyword parameters:

        :keyword last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
        :type    last_error_date: int

        :keyword last_error_message: Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
        :type    last_error_message: str
        """
        super(WebhookInfo, self).__init__()
        assert (url is not None)
        assert (isinstance(url, str))
        self.url = url

        assert (has_custom_certificate is not None)
        assert (isinstance(has_custom_certificate, bool))
        self.has_custom_certificate = has_custom_certificate

        assert (pending_update_count is not None)
        assert (isinstance(pending_update_count, int))
        self.pending_update_count = pending_update_count

        assert (last_error_date is None or isinstance(last_error_date, int))
        self.last_error_date = last_error_date

        assert (last_error_message is None or isinstance(last_error_message, str))
        self.last_error_message = last_error_message

    # end def __init__

    def to_array(self):
        """
        Serializes this WebhookInfo to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(WebhookInfo, self).to_array()
        array['url'] = str(self.url)  # type str
        array['has_custom_certificate'] = bool(self.has_custom_certificate)  # type bool
        array['pending_update_count'] = int(self.pending_update_count)  # type int
        if self.last_error_date is not None:
            array['last_error_date'] = int(self.last_error_date)  # type int
        if self.last_error_message is not None:
            array['last_error_message'] = str(self.last_error_message)  # type str
        return array

    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new WebhookInfo from a given dictionary.

        :return: new WebhookInfo instance.
        :rtype: WebhookInfo
        """
        if array is None or not array:
            return None
        # end if
        assert (isinstance(array, dict))

        data = {}
        data['url'] = str(array.get('url'))
        data['has_custom_certificate'] = bool(array.get('has_custom_certificate'))
        data['pending_update_count'] = int(array.get('pending_update_count'))
        data['last_error_date'] = int(array.get('last_error_date')) if array.get(
            'last_error_date') is not None else None
        data['last_error_message'] = str(array.get('last_error_message')) if array.get(
            'last_error_message') is not None else None
        return WebhookInfo(**data)

    # end def from_array

    def __str__(self):
        """
        Implements `str(webhookinfo_instance)`
        """
        return "WebhookInfo(url={self.url!r}, has_custom_certificate={self.has_custom_certificate!r}, pending_update_count={self.pending_update_count!r}, last_error_date={self.last_error_date!r}, last_error_message={self.last_error_message!r})".format(
            self=self)

    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in webhookinfo_instance`
        """
        return key in ["url", "has_custom_certificate", "pending_update_count", "last_error_date", "last_error_message"]
        # end def __contains__
# end class WebhookInfo
