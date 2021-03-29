# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.updates import UpdateType

__author__ = 'luckydonald'


class Invoice(Result):
    """
    This object contains basic information about an invoice.

    https://core.telegram.org/bots/api#invoice


    Parameters:

    :param title: Product name
    :type  title: str|unicode

    :param description: Product description
    :type  description: str|unicode

    :param start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice
    :type  start_parameter: str|unicode

    :param currency: Three-letter ISO 4217 currency code
    :type  currency: str|unicode

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type  total_amount: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int
# end class Invoice

class ShippingAddress(Result):
    """
    This object represents a shipping address.

    https://core.telegram.org/bots/api#shippingaddress


    Parameters:

    :param country_code: ISO 3166-1 alpha-2 country code
    :type  country_code: str|unicode

    :param state: State, if applicable
    :type  state: str|unicode

    :param city: City
    :type  city: str|unicode

    :param street_line1: First line for the address
    :type  street_line1: str|unicode

    :param street_line2: Second line for the address
    :type  street_line2: str|unicode

    :param post_code: Address post code
    :type  post_code: str|unicode


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str
# end class ShippingAddress

class OrderInfo(Result):
    """
    This object represents information about an order.

    https://core.telegram.org/bots/api#orderinfo

    Optional keyword parameters:

    :param name: Optional. User name
    :type  name: str|unicode

    :param phone_number: Optional. User's phone number
    :type  phone_number: str|unicode

    :param email: Optional. User email
    :type  email: str|unicode

    :param shipping_address: Optional. User shipping address
    :type  shipping_address: pytgbot.api_types.receivable.payments.ShippingAddress

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    name: str
    phone_number: str
    email: str
    shipping_address: ShippingAddress
# end class OrderInfo

class SuccessfulPayment(Result):
    """
    This object contains basic information about a successful payment.

    https://core.telegram.org/bots/api#successfulpayment


    Parameters:

    :param currency: Three-letter ISO 4217 currency code
    :type  currency: str|unicode

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type  total_amount: int

    :param invoice_payload: Bot specified invoice payload
    :type  invoice_payload: str|unicode

    :param telegram_payment_charge_id: Telegram payment identifier
    :type  telegram_payment_charge_id: str|unicode

    :param provider_payment_charge_id: Provider payment identifier
    :type  provider_payment_charge_id: str|unicode


    Optional keyword parameters:

    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :type  shipping_option_id: str|unicode

    :param order_info: Optional. Order info provided by the user
    :type  order_info: pytgbot.api_types.receivable.payments.OrderInfo

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    shipping_option_id: str
    order_info: OrderInfo
# end class SuccessfulPayment

class ShippingQuery(UpdateType):
    """
    This object contains information about an incoming shipping query.

    https://core.telegram.org/bots/api#shippingquery


    Parameters:

    :param id: Unique query identifier
    :type  id: str|unicode

    :param from_peer: User who sent the query
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param invoice_payload: Bot specified invoice payload
    :type  invoice_payload: str|unicode

    :param shipping_address: User specified shipping address
    :type  shipping_address: pytgbot.api_types.receivable.payments.ShippingAddress


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    id: str
    from_peer: User
    invoice_payload: str
    shipping_address: ShippingAddress
# end class ShippingQuery

class PreCheckoutQuery(UpdateType):
    """
    This object contains information about an incoming pre-checkout query.

    https://core.telegram.org/bots/api#precheckoutquery


    Parameters:

    :param id: Unique query identifier
    :type  id: str|unicode

    :param from_peer: User who sent the query
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param currency: Three-letter ISO 4217 currency code
    :type  currency: str|unicode

    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    :type  total_amount: int

    :param invoice_payload: Bot specified invoice payload
    :type  invoice_payload: str|unicode


    Optional keyword parameters:

    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :type  shipping_option_id: str|unicode

    :param order_info: Optional. Order info provided by the user
    :type  order_info: pytgbot.api_types.receivable.payments.OrderInfo

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    id: str
    from_peer: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: OrderInfo
# end class PreCheckoutQuery
