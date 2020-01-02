# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.sendable import Sendable

__author__ = 'luckydonald'


class LabeledPrice(Sendable):
    """
    This object represents a portion of the price for goods or services.

    https://core.telegram.org/bots/api#labeledprice
    

    Parameters:
    
    :param label: Portion label
    :type  label: str|unicode
    
    :param amount: Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type  amount: int
    

    Optional keyword parameters:
    """
    label: str
    amount: int
# end class LabeledPrice

class ShippingOption(Sendable):
    """
    This object represents one shipping option.

    https://core.telegram.org/bots/api#shippingoption
    

    Parameters:
    
    :param id: Shipping option identifier
    :type  id: str|unicode
    
    :param title: Option title
    :type  title: str|unicode
    
    :param prices: List of price portions
    :type  prices: list of pytgbot.api_types.sendable.payments.LabeledPrice
    

    Optional keyword parameters:
    """
    id: str
    title: str
    prices: List[LabeledPrice]
# end class ShippingOption
