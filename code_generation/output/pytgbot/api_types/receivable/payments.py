# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result
from .updates import UpdateType

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

    def __init__(self, title, description, start_parameter, currency, total_amount, _raw=None):
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
        super(Invoice, self).__init__()
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(description, unicode_type, parameter_name="description")
        self.description = description
        assert_type_or_raise(start_parameter, unicode_type, parameter_name="start_parameter")
        self.start_parameter = start_parameter
        assert_type_or_raise(currency, unicode_type, parameter_name="currency")
        self.currency = currency
        assert_type_or_raise(total_amount, int, parameter_name="total_amount")
        self.total_amount = total_amount

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Invoice to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Invoice, self).to_array()
        
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['description'] = u(self.description)  # py2: type unicode, py3: type str
        array['start_parameter'] = u(self.start_parameter)  # py2: type unicode, py3: type str
        array['currency'] = u(self.currency)  # py2: type unicode, py3: type str
        array['total_amount'] = int(self.total_amount)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Invoice constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['title'] = u(array.get('title'))
        data['description'] = u(array.get('description'))
        data['start_parameter'] = u(array.get('start_parameter'))
        data['currency'] = u(array.get('currency'))
        data['total_amount'] = int(array.get('total_amount'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Invoice from a given dictionary.

        :return: new Invoice instance.
        :rtype: Invoice
        """
        if not array:  # None or {}
            return None
        # end if

        data = Invoice.validate_array(array)
        data['_raw'] = array
        return Invoice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(invoice_instance)`
        """
        return "Invoice(title={self.title!r}, description={self.description!r}, start_parameter={self.start_parameter!r}, currency={self.currency!r}, total_amount={self.total_amount!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(invoice_instance)`
        """
        if self._raw:
            return "Invoice.from_array({self._raw})".format(self=self)
        # end if
        return "Invoice(title={self.title!r}, description={self.description!r}, start_parameter={self.start_parameter!r}, currency={self.currency!r}, total_amount={self.total_amount!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in invoice_instance`
        """
        return (
            key in ["title", "description", "start_parameter", "currency", "total_amount"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, country_code, state, city, street_line1, street_line2, post_code, _raw=None):
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
        super(ShippingAddress, self).__init__()
        assert_type_or_raise(country_code, unicode_type, parameter_name="country_code")
        self.country_code = country_code
        assert_type_or_raise(state, unicode_type, parameter_name="state")
        self.state = state
        assert_type_or_raise(city, unicode_type, parameter_name="city")
        self.city = city
        assert_type_or_raise(street_line1, unicode_type, parameter_name="street_line1")
        self.street_line1 = street_line1
        assert_type_or_raise(street_line2, unicode_type, parameter_name="street_line2")
        self.street_line2 = street_line2
        assert_type_or_raise(post_code, unicode_type, parameter_name="post_code")
        self.post_code = post_code

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ShippingAddress to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ShippingAddress, self).to_array()
        
        array['country_code'] = u(self.country_code)  # py2: type unicode, py3: type str
        array['state'] = u(self.state)  # py2: type unicode, py3: type str
        array['city'] = u(self.city)  # py2: type unicode, py3: type str
        array['street_line1'] = u(self.street_line1)  # py2: type unicode, py3: type str
        array['street_line2'] = u(self.street_line2)  # py2: type unicode, py3: type str
        array['post_code'] = u(self.post_code)  # py2: type unicode, py3: type str

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ShippingAddress constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['country_code'] = u(array.get('country_code'))
        data['state'] = u(array.get('state'))
        data['city'] = u(array.get('city'))
        data['street_line1'] = u(array.get('street_line1'))
        data['street_line2'] = u(array.get('street_line2'))
        data['post_code'] = u(array.get('post_code'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ShippingAddress from a given dictionary.

        :return: new ShippingAddress instance.
        :rtype: ShippingAddress
        """
        if not array:  # None or {}
            return None
        # end if

        data = ShippingAddress.validate_array(array)
        data['_raw'] = array
        return ShippingAddress(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(shippingaddress_instance)`
        """
        return "ShippingAddress(country_code={self.country_code!r}, state={self.state!r}, city={self.city!r}, street_line1={self.street_line1!r}, street_line2={self.street_line2!r}, post_code={self.post_code!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(shippingaddress_instance)`
        """
        if self._raw:
            return "ShippingAddress.from_array({self._raw})".format(self=self)
        # end if
        return "ShippingAddress(country_code={self.country_code!r}, state={self.state!r}, city={self.city!r}, street_line1={self.street_line1!r}, street_line2={self.street_line2!r}, post_code={self.post_code!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in shippingaddress_instance`
        """
        return (
            key in ["country_code", "state", "city", "street_line1", "street_line2", "post_code"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, name=None, phone_number=None, email=None, shipping_address=None, _raw=None):
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
        super(OrderInfo, self).__init__()
        
        assert_type_or_raise(name, None, unicode_type, parameter_name="name")
        self.name = name
        assert_type_or_raise(phone_number, None, unicode_type, parameter_name="phone_number")
        self.phone_number = phone_number
        assert_type_or_raise(email, None, unicode_type, parameter_name="email")
        self.email = email
        assert_type_or_raise(shipping_address, None, ShippingAddress, parameter_name="shipping_address")
        self.shipping_address = shipping_address

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this OrderInfo to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(OrderInfo, self).to_array()
        
        if self.name is not None:
            array['name'] = u(self.name)  # py2: type unicode, py3: type str
        # end if
        if self.phone_number is not None:
            array['phone_number'] = u(self.phone_number)  # py2: type unicode, py3: type str
        # end if
        if self.email is not None:
            array['email'] = u(self.email)  # py2: type unicode, py3: type str
        # end if
        if self.shipping_address is not None:
            array['shipping_address'] = self.shipping_address.to_array()  # type ShippingAddress
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the OrderInfo constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        
        data = Result.validate_array(array)
        data['name'] = u(array.get('name')) if array.get('name') is not None else None
        data['phone_number'] = u(array.get('phone_number')) if array.get('phone_number') is not None else None
        data['email'] = u(array.get('email')) if array.get('email') is not None else None
        data['shipping_address'] = ShippingAddress.from_array(array.get('shipping_address')) if array.get('shipping_address') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new OrderInfo from a given dictionary.

        :return: new OrderInfo instance.
        :rtype: OrderInfo
        """
        if not array:  # None or {}
            return None
        # end if

        data = OrderInfo.validate_array(array)
        data['_raw'] = array
        return OrderInfo(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(orderinfo_instance)`
        """
        return "OrderInfo(name={self.name!r}, phone_number={self.phone_number!r}, email={self.email!r}, shipping_address={self.shipping_address!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(orderinfo_instance)`
        """
        if self._raw:
            return "OrderInfo.from_array({self._raw})".format(self=self)
        # end if
        return "OrderInfo(name={self.name!r}, phone_number={self.phone_number!r}, email={self.email!r}, shipping_address={self.shipping_address!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in orderinfo_instance`
        """
        return (
            key in ["name", "phone_number", "email", "shipping_address"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, currency, total_amount, invoice_payload, telegram_payment_charge_id, provider_payment_charge_id, shipping_option_id=None, order_info=None, _raw=None):
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
        super(SuccessfulPayment, self).__init__()
        
        assert_type_or_raise(currency, unicode_type, parameter_name="currency")
        self.currency = currency
        assert_type_or_raise(total_amount, int, parameter_name="total_amount")
        self.total_amount = total_amount
        assert_type_or_raise(invoice_payload, unicode_type, parameter_name="invoice_payload")
        self.invoice_payload = invoice_payload
        assert_type_or_raise(telegram_payment_charge_id, unicode_type, parameter_name="telegram_payment_charge_id")
        self.telegram_payment_charge_id = telegram_payment_charge_id
        assert_type_or_raise(provider_payment_charge_id, unicode_type, parameter_name="provider_payment_charge_id")
        self.provider_payment_charge_id = provider_payment_charge_id
        assert_type_or_raise(shipping_option_id, None, unicode_type, parameter_name="shipping_option_id")
        self.shipping_option_id = shipping_option_id
        assert_type_or_raise(order_info, None, OrderInfo, parameter_name="order_info")
        self.order_info = order_info

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this SuccessfulPayment to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(SuccessfulPayment, self).to_array()
        
        array['currency'] = u(self.currency)  # py2: type unicode, py3: type str
        array['total_amount'] = int(self.total_amount)  # type int
        array['invoice_payload'] = u(self.invoice_payload)  # py2: type unicode, py3: type str
        array['telegram_payment_charge_id'] = u(self.telegram_payment_charge_id)  # py2: type unicode, py3: type str
        array['provider_payment_charge_id'] = u(self.provider_payment_charge_id)  # py2: type unicode, py3: type str
        if self.shipping_option_id is not None:
            array['shipping_option_id'] = u(self.shipping_option_id)  # py2: type unicode, py3: type str
        # end if
        if self.order_info is not None:
            array['order_info'] = self.order_info.to_array()  # type OrderInfo
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the SuccessfulPayment constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        
        data = Result.validate_array(array)
        data['currency'] = u(array.get('currency'))
        data['total_amount'] = int(array.get('total_amount'))
        data['invoice_payload'] = u(array.get('invoice_payload'))
        data['telegram_payment_charge_id'] = u(array.get('telegram_payment_charge_id'))
        data['provider_payment_charge_id'] = u(array.get('provider_payment_charge_id'))
        data['shipping_option_id'] = u(array.get('shipping_option_id')) if array.get('shipping_option_id') is not None else None
        data['order_info'] = OrderInfo.from_array(array.get('order_info')) if array.get('order_info') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new SuccessfulPayment from a given dictionary.

        :return: new SuccessfulPayment instance.
        :rtype: SuccessfulPayment
        """
        if not array:  # None or {}
            return None
        # end if

        data = SuccessfulPayment.validate_array(array)
        data['_raw'] = array
        return SuccessfulPayment(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(successfulpayment_instance)`
        """
        return "SuccessfulPayment(currency={self.currency!r}, total_amount={self.total_amount!r}, invoice_payload={self.invoice_payload!r}, telegram_payment_charge_id={self.telegram_payment_charge_id!r}, provider_payment_charge_id={self.provider_payment_charge_id!r}, shipping_option_id={self.shipping_option_id!r}, order_info={self.order_info!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(successfulpayment_instance)`
        """
        if self._raw:
            return "SuccessfulPayment.from_array({self._raw})".format(self=self)
        # end if
        return "SuccessfulPayment(currency={self.currency!r}, total_amount={self.total_amount!r}, invoice_payload={self.invoice_payload!r}, telegram_payment_charge_id={self.telegram_payment_charge_id!r}, provider_payment_charge_id={self.provider_payment_charge_id!r}, shipping_option_id={self.shipping_option_id!r}, order_info={self.order_info!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in successfulpayment_instance`
        """
        return (
            key in ["currency", "total_amount", "invoice_payload", "telegram_payment_charge_id", "provider_payment_charge_id", "shipping_option_id", "order_info"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, id, from_peer, invoice_payload, shipping_address, _raw=None):
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
        super(ShippingQuery, self).__init__()
        from .peer import User
        
        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(invoice_payload, unicode_type, parameter_name="invoice_payload")
        self.invoice_payload = invoice_payload
        assert_type_or_raise(shipping_address, ShippingAddress, parameter_name="shipping_address")
        self.shipping_address = shipping_address

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ShippingQuery to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ShippingQuery, self).to_array()
        
        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['from'] = self.from_peer.to_array()  # type User
        array['invoice_payload'] = u(self.invoice_payload)  # py2: type unicode, py3: type str
        array['shipping_address'] = self.shipping_address.to_array()  # type ShippingAddress

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ShippingQuery constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User
        
        data = UpdateType.validate_array(array)
        data['id'] = u(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['invoice_payload'] = u(array.get('invoice_payload'))
        data['shipping_address'] = ShippingAddress.from_array(array.get('shipping_address'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ShippingQuery from a given dictionary.

        :return: new ShippingQuery instance.
        :rtype: ShippingQuery
        """
        if not array:  # None or {}
            return None
        # end if

        data = ShippingQuery.validate_array(array)
        data['_raw'] = array
        return ShippingQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(shippingquery_instance)`
        """
        return "ShippingQuery(id={self.id!r}, from_peer={self.from_peer!r}, invoice_payload={self.invoice_payload!r}, shipping_address={self.shipping_address!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(shippingquery_instance)`
        """
        if self._raw:
            return "ShippingQuery.from_array({self._raw})".format(self=self)
        # end if
        return "ShippingQuery(id={self.id!r}, from_peer={self.from_peer!r}, invoice_payload={self.invoice_payload!r}, shipping_address={self.shipping_address!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in shippingquery_instance`
        """
        return (
            key in ["id", "from_peer", "invoice_payload", "shipping_address"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, id, from_peer, currency, total_amount, invoice_payload, shipping_option_id=None, order_info=None, _raw=None):
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
        super(PreCheckoutQuery, self).__init__()
        from .peer import User
        
        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(currency, unicode_type, parameter_name="currency")
        self.currency = currency
        assert_type_or_raise(total_amount, int, parameter_name="total_amount")
        self.total_amount = total_amount
        assert_type_or_raise(invoice_payload, unicode_type, parameter_name="invoice_payload")
        self.invoice_payload = invoice_payload
        assert_type_or_raise(shipping_option_id, None, unicode_type, parameter_name="shipping_option_id")
        self.shipping_option_id = shipping_option_id
        assert_type_or_raise(order_info, None, OrderInfo, parameter_name="order_info")
        self.order_info = order_info

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this PreCheckoutQuery to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(PreCheckoutQuery, self).to_array()
        
        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['from'] = self.from_peer.to_array()  # type User
        array['currency'] = u(self.currency)  # py2: type unicode, py3: type str
        array['total_amount'] = int(self.total_amount)  # type int
        array['invoice_payload'] = u(self.invoice_payload)  # py2: type unicode, py3: type str
        if self.shipping_option_id is not None:
            array['shipping_option_id'] = u(self.shipping_option_id)  # py2: type unicode, py3: type str
        # end if
        if self.order_info is not None:
            array['order_info'] = self.order_info.to_array()  # type OrderInfo
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the PreCheckoutQuery constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User
        
        data = UpdateType.validate_array(array)
        data['id'] = u(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['currency'] = u(array.get('currency'))
        data['total_amount'] = int(array.get('total_amount'))
        data['invoice_payload'] = u(array.get('invoice_payload'))
        data['shipping_option_id'] = u(array.get('shipping_option_id')) if array.get('shipping_option_id') is not None else None
        data['order_info'] = OrderInfo.from_array(array.get('order_info')) if array.get('order_info') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new PreCheckoutQuery from a given dictionary.

        :return: new PreCheckoutQuery instance.
        :rtype: PreCheckoutQuery
        """
        if not array:  # None or {}
            return None
        # end if

        data = PreCheckoutQuery.validate_array(array)
        data['_raw'] = array
        return PreCheckoutQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(precheckoutquery_instance)`
        """
        return "PreCheckoutQuery(id={self.id!r}, from_peer={self.from_peer!r}, currency={self.currency!r}, total_amount={self.total_amount!r}, invoice_payload={self.invoice_payload!r}, shipping_option_id={self.shipping_option_id!r}, order_info={self.order_info!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(precheckoutquery_instance)`
        """
        if self._raw:
            return "PreCheckoutQuery.from_array({self._raw})".format(self=self)
        # end if
        return "PreCheckoutQuery(id={self.id!r}, from_peer={self.from_peer!r}, currency={self.currency!r}, total_amount={self.total_amount!r}, invoice_payload={self.invoice_payload!r}, shipping_option_id={self.shipping_option_id!r}, order_info={self.order_info!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in precheckoutquery_instance`
        """
        return (
            key in ["id", "from_peer", "currency", "total_amount", "invoice_payload", "shipping_option_id", "order_info"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class PreCheckoutQuery

