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

class WebhookInfo(updates.WebhookInfo, db.Entity):
    """
    Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo
    """
    url = pony.Required(str)
    has_custom_certificate = pony.Required(bool)
    pending_update_count = pony.Required(int)
    last_error_date = pony.Optional(int)
    last_error_message = pony.Optional(str)
# end class WebhookInfo
