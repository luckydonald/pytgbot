# -*- coding: utf-8 -*-
from . import Result
from .updates import UpdateType


class Invoice(Result):
    """
    This object contains basic information about an invoice.

    https://core.telegram.org/bots/api#invoice
    """
    def __init__(self, title, description, start_parameter, currency, total_amount):
        """
        This object contains basic information about an invoice.
    
        https://core.telegram.org/bots/api#invoice


        Parameters:
        
        :param title: Product name
        :type  title: str
        
        :param description: Product description
        :type  description: str
        
        :param start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice
        :type  start_parameter: str
        
        :param currency: Three-letter ISO 4217 currency code
        :type  currency: str
        
        :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        :type  total_amount: int
        """
        super(Invoice, self).__init__()
        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title
        
        assert(description is not None)
        assert(isinstance(description, str))
        self.description = description
        
        assert(start_parameter is not None)
        assert(isinstance(start_parameter, str))
        self.start_parameter = start_parameter
        
        assert(currency is not None)
        assert(isinstance(currency, str))
        self.currency = currency
        
        assert(total_amount is not None)
        assert(isinstance(total_amount, int))
        self.total_amount = total_amount
    # end def __init__

    def to_array(self):
        """
        Serializes this Invoice to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Invoice, self).to_array()
        array['title'] = str(self.title)  # type str
        array['description'] = str(self.description)  # type str
        array['start_parameter'] = str(self.start_parameter)  # type str
        array['currency'] = str(self.currency)  # type str
        array['total_amount'] = int(self.total_amount)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Invoice from a given dictionary.

        :return: new Invoice instance.
        :rtype: Invoice
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        data = {}
        data['title'] = str(array.get('title'))
        data['description'] = str(array.get('description'))
        data['start_parameter'] = str(array.get('start_parameter'))
        data['currency'] = str(array.get('currency'))
        data['total_amount'] = int(array.get('total_amount'))
        return Invoice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(invoice_instance)`
        """
        return "Invoice(title={self.title!r}, description={self.description!r}, start_parameter={self.start_parameter!r}, currency={self.currency!r}, total_amount={self.total_amount!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in invoice_instance`
        """
        return key in ["title", "description", "start_parameter", "currency", "total_amount"]
    # end def __contains__
# end class Invoice



class ShippingAddress(Result):
    """
    This object represents a shipping address.

    https://core.telegram.org/bots/api#shippingaddress
    """
    def __init__(self, country_code, state, city, street_line1, street_line2, post_code):
        """
        This object represents a shipping address.
    
        https://core.telegram.org/bots/api#shippingaddress


        Parameters:
        
        :param country_code: ISO 3166-1 alpha-2 country code
        :type  country_code: str
        
        :param state: State, if applicable
        :type  state: str
        
        :param city: City
        :type  city: str
        
        :param street_line1: First line for the address
        :type  street_line1: str
        
        :param street_line2: Second line for the address
        :type  street_line2: str
        
        :param post_code: Address post code
        :type  post_code: str
        """
        super(ShippingAddress, self).__init__()
        assert(country_code is not None)
        assert(isinstance(country_code, str))
        self.country_code = country_code
        
        assert(state is not None)
        assert(isinstance(state, str))
        self.state = state
        
        assert(city is not None)
        assert(isinstance(city, str))
        self.city = city
        
        assert(street_line1 is not None)
        assert(isinstance(street_line1, str))
        self.street_line1 = street_line1
        
        assert(street_line2 is not None)
        assert(isinstance(street_line2, str))
        self.street_line2 = street_line2
        
        assert(post_code is not None)
        assert(isinstance(post_code, str))
        self.post_code = post_code
    # end def __init__

    def to_array(self):
        """
        Serializes this ShippingAddress to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ShippingAddress, self).to_array()
        array['country_code'] = str(self.country_code)  # type str
        array['state'] = str(self.state)  # type str
        array['city'] = str(self.city)  # type str
        array['street_line1'] = str(self.street_line1)  # type str
        array['street_line2'] = str(self.street_line2)  # type str
        array['post_code'] = str(self.post_code)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ShippingAddress from a given dictionary.

        :return: new ShippingAddress instance.
        :rtype: ShippingAddress
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        data = {}
        data['country_code'] = str(array.get('country_code'))
        data['state'] = str(array.get('state'))
        data['city'] = str(array.get('city'))
        data['street_line1'] = str(array.get('street_line1'))
        data['street_line2'] = str(array.get('street_line2'))
        data['post_code'] = str(array.get('post_code'))
        return ShippingAddress(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(shippingaddress_instance)`
        """
        return "ShippingAddress(country_code={self.country_code!r}, state={self.state!r}, city={self.city!r}, street_line1={self.street_line1!r}, street_line2={self.street_line2!r}, post_code={self.post_code!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in shippingaddress_instance`
        """
        return key in ["country_code", "state", "city", "street_line1", "street_line2", "post_code"]
    # end def __contains__
# end class ShippingAddress



class OrderInfo(Result):
    """
    This object represents information about an order.

    https://core.telegram.org/bots/api#orderinfo
    """
    def __init__(self, name=None, phone_number=None, email=None, shipping_address=None):
        """
        This object represents information about an order.
    
        https://core.telegram.org/bots/api#orderinfo

        Optional keyword parameters:
        
        :keyword name: Optional. User name
        :type    name: str
        
        :keyword phone_number: Optional. User's phone number
        :type    phone_number: str
        
        :keyword email: Optional. User email
        :type    email: str
        
        :keyword shipping_address: Optional. User shipping address
        :type    shipping_address: pytgbot.api_types.receivable.payments.ShippingAddress
        """
        super(OrderInfo, self).__init__()

        assert(name is None or isinstance(name, str))
        self.name = name
        
        assert(phone_number is None or isinstance(phone_number, str))
        self.phone_number = phone_number
        
        assert(email is None or isinstance(email, str))
        self.email = email
        
        assert(shipping_address is None or isinstance(shipping_address, ShippingAddress))
        self.shipping_address = shipping_address
    # end def __init__

    def to_array(self):
        """
        Serializes this OrderInfo to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(OrderInfo, self).to_array()
        if self.name is not None:
            array['name'] = str(self.name)  # type str
        if self.phone_number is not None:
            array['phone_number'] = str(self.phone_number)  # type str
        if self.email is not None:
            array['email'] = str(self.email)  # type str
        if self.shipping_address is not None:
            array['shipping_address'] = self.shipping_address.to_array()  # type ShippingAddress
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new OrderInfo from a given dictionary.

        :return: new OrderInfo instance.
        :rtype: OrderInfo
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        data = {}
        data['name'] = str(array.get('name')) if array.get('name') is not None else None
        data['phone_number'] = str(array.get('phone_number')) if array.get('phone_number') is not None else None
        data['email'] = str(array.get('email')) if array.get('email') is not None else None
        data['shipping_address'] = ShippingAddress.from_array(array.get('shipping_address')) if array.get('shipping_address') is not None else None
        return OrderInfo(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(orderinfo_instance)`
        """
        return "OrderInfo(name={self.name!r}, phone_number={self.phone_number!r}, email={self.email!r}, shipping_address={self.shipping_address!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in orderinfo_instance`
        """
        return key in ["name", "phone_number", "email", "shipping_address"]
    # end def __contains__
# end class OrderInfo



class SuccessfulPayment(Result):
    """
    This object contains basic information about a successful payment.

    https://core.telegram.org/bots/api#successfulpayment
    """
    def __init__(self, currency, total_amount, invoice_payload, telegram_payment_charge_id, provider_payment_charge_id, shipping_option_id=None, order_info=None):
        """
        This object contains basic information about a successful payment.
    
        https://core.telegram.org/bots/api#successfulpayment


        Parameters:
        
        :param currency: Three-letter ISO 4217 currency code
        :type  currency: str
        
        :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        :type  total_amount: int
        
        :param invoice_payload: Bot specified invoice payload
        :type  invoice_payload: str
        
        :param telegram_payment_charge_id: Telegram payment identifier
        :type  telegram_payment_charge_id: str
        
        :param provider_payment_charge_id: Provider payment identifier
        :type  provider_payment_charge_id: str
        

        Optional keyword parameters:
        
        :keyword shipping_option_id: Optional. Identifier of the shipping option chosen by the user
        :type    shipping_option_id: str
        
        :keyword order_info: Optional. Order info provided by the user
        :type    order_info: pytgbot.api_types.receivable.payments.OrderInfo
        """
        super(SuccessfulPayment, self).__init__()

        assert(currency is not None)
        assert(isinstance(currency, str))
        self.currency = currency
        
        assert(total_amount is not None)
        assert(isinstance(total_amount, int))
        self.total_amount = total_amount
        
        assert(invoice_payload is not None)
        assert(isinstance(invoice_payload, str))
        self.invoice_payload = invoice_payload
        
        assert(telegram_payment_charge_id is not None)
        assert(isinstance(telegram_payment_charge_id, str))
        self.telegram_payment_charge_id = telegram_payment_charge_id
        
        assert(provider_payment_charge_id is not None)
        assert(isinstance(provider_payment_charge_id, str))
        self.provider_payment_charge_id = provider_payment_charge_id
        
        assert(shipping_option_id is None or isinstance(shipping_option_id, str))
        self.shipping_option_id = shipping_option_id
        
        assert(order_info is None or isinstance(order_info, OrderInfo))
        self.order_info = order_info
    # end def __init__

    def to_array(self):
        """
        Serializes this SuccessfulPayment to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(SuccessfulPayment, self).to_array()
        array['currency'] = str(self.currency)  # type str
        array['total_amount'] = int(self.total_amount)  # type int
        array['invoice_payload'] = str(self.invoice_payload)  # type str
        array['telegram_payment_charge_id'] = str(self.telegram_payment_charge_id)  # type str
        array['provider_payment_charge_id'] = str(self.provider_payment_charge_id)  # type str
        if self.shipping_option_id is not None:
            array['shipping_option_id'] = str(self.shipping_option_id)  # type str
        if self.order_info is not None:
            array['order_info'] = self.order_info.to_array()  # type OrderInfo
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new SuccessfulPayment from a given dictionary.

        :return: new SuccessfulPayment instance.
        :rtype: SuccessfulPayment
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        data = {}
        data['currency'] = str(array.get('currency'))
        data['total_amount'] = int(array.get('total_amount'))
        data['invoice_payload'] = str(array.get('invoice_payload'))
        data['telegram_payment_charge_id'] = str(array.get('telegram_payment_charge_id'))
        data['provider_payment_charge_id'] = str(array.get('provider_payment_charge_id'))
        data['shipping_option_id'] = str(array.get('shipping_option_id')) if array.get('shipping_option_id') is not None else None
        data['order_info'] = OrderInfo.from_array(array.get('order_info')) if array.get('order_info') is not None else None
        return SuccessfulPayment(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(successfulpayment_instance)`
        """
        return "SuccessfulPayment(currency={self.currency!r}, total_amount={self.total_amount!r}, invoice_payload={self.invoice_payload!r}, telegram_payment_charge_id={self.telegram_payment_charge_id!r}, provider_payment_charge_id={self.provider_payment_charge_id!r}, shipping_option_id={self.shipping_option_id!r}, order_info={self.order_info!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in successfulpayment_instance`
        """
        return key in ["currency", "total_amount", "invoice_payload", "telegram_payment_charge_id", "provider_payment_charge_id", "shipping_option_id", "order_info"]
    # end def __contains__
# end class SuccessfulPayment



class ShippingQuery(UpdateType):
    """
    This object contains information about an incoming shipping query.

    https://core.telegram.org/bots/api#shippingquery
    """
    def __init__(self, id, from_peer, invoice_payload, shipping_address):
        """
        This object contains information about an incoming shipping query.
    
        https://core.telegram.org/bots/api#shippingquery


        Parameters:
        
        :param id: Unique query identifier
        :type  id: str
        
        :param from_peer: User who sent the query
        :type  from_peer: pytgbot.api_types.receivable.peer.User
        
        :param invoice_payload: Bot specified invoice payload
        :type  invoice_payload: str
        
        :param shipping_address: User specified shipping address
        :type  shipping_address: pytgbot.api_types.receivable.payments.ShippingAddress
        """
        super(ShippingQuery, self).__init__()
        from pytgbot.api_types.receivable.peer import User
        
        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id
        
        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer
        
        assert(invoice_payload is not None)
        assert(isinstance(invoice_payload, str))
        self.invoice_payload = invoice_payload
        
        assert(shipping_address is not None)
        assert(isinstance(shipping_address, ShippingAddress))
        self.shipping_address = shipping_address
    # end def __init__

    def to_array(self):
        """
        Serializes this ShippingQuery to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ShippingQuery, self).to_array()
        array['id'] = str(self.id)  # type str
        array['from'] = self.from_peer.to_array()  # type User
        array['invoice_payload'] = str(self.invoice_payload)  # type str
        array['shipping_address'] = self.shipping_address.to_array()  # type ShippingAddress
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ShippingQuery from a given dictionary.

        :return: new ShippingQuery instance.
        :rtype: ShippingQuery
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        from pytgbot.api_types.receivable.peer import User
        
        data = {}
        data['id'] = str(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['invoice_payload'] = str(array.get('invoice_payload'))
        data['shipping_address'] = ShippingAddress.from_array(array.get('shipping_address'))
        return ShippingQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(shippingquery_instance)`
        """
        return "ShippingQuery(id={self.id!r}, from_peer={self.from_peer!r}, invoice_payload={self.invoice_payload!r}, shipping_address={self.shipping_address!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in shippingquery_instance`
        """
        return key in ["id", "from_peer", "invoice_payload", "shipping_address"]
    # end def __contains__
# end class ShippingQuery



class PreCheckoutQuery(UpdateType):
    """
    This object contains information about an incoming pre-checkout query.

    https://core.telegram.org/bots/api#precheckoutquery
    """
    def __init__(self, id, from_peer, currency, total_amount, invoice_payload, shipping_option_id=None, order_info=None):
        """
        This object contains information about an incoming pre-checkout query.
    
        https://core.telegram.org/bots/api#precheckoutquery


        Parameters:
        
        :param id: Unique query identifier
        :type  id: str
        
        :param from_peer: User who sent the query
        :type  from_peer: pytgbot.api_types.receivable.peer.User
        
        :param currency: Three-letter ISO 4217 currency code
        :type  currency: str
        
        :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        :type  total_amount: int
        
        :param invoice_payload: Bot specified invoice payload
        :type  invoice_payload: str
        

        Optional keyword parameters:
        
        :keyword shipping_option_id: Optional. Identifier of the shipping option chosen by the user
        :type    shipping_option_id: str
        
        :keyword order_info: Optional. Order info provided by the user
        :type    order_info: pytgbot.api_types.receivable.payments.OrderInfo
        """
        super(PreCheckoutQuery, self).__init__()
        from pytgbot.api_types.receivable.peer import User
        
        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id
        
        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer
        
        assert(currency is not None)
        assert(isinstance(currency, str))
        self.currency = currency
        
        assert(total_amount is not None)
        assert(isinstance(total_amount, int))
        self.total_amount = total_amount
        
        assert(invoice_payload is not None)
        assert(isinstance(invoice_payload, str))
        self.invoice_payload = invoice_payload
        
        assert(shipping_option_id is None or isinstance(shipping_option_id, str))
        self.shipping_option_id = shipping_option_id
        
        assert(order_info is None or isinstance(order_info, OrderInfo))
        self.order_info = order_info
    # end def __init__

    def to_array(self):
        """
        Serializes this PreCheckoutQuery to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(PreCheckoutQuery, self).to_array()
        array['id'] = str(self.id)  # type str
        array['from'] = self.from_peer.to_array()  # type User
        array['currency'] = str(self.currency)  # type str
        array['total_amount'] = int(self.total_amount)  # type int
        array['invoice_payload'] = str(self.invoice_payload)  # type str
        if self.shipping_option_id is not None:
            array['shipping_option_id'] = str(self.shipping_option_id)  # type str
        if self.order_info is not None:
            array['order_info'] = self.order_info.to_array()  # type OrderInfo
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new PreCheckoutQuery from a given dictionary.

        :return: new PreCheckoutQuery instance.
        :rtype: PreCheckoutQuery
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        from pytgbot.api_types.receivable.peer import User
        
        data = {}
        data['id'] = str(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['currency'] = str(array.get('currency'))
        data['total_amount'] = int(array.get('total_amount'))
        data['invoice_payload'] = str(array.get('invoice_payload'))
        data['shipping_option_id'] = str(array.get('shipping_option_id')) if array.get('shipping_option_id') is not None else None
        data['order_info'] = OrderInfo.from_array(array.get('order_info')) if array.get('order_info') is not None else None
        return PreCheckoutQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(precheckoutquery_instance)`
        """
        return "PreCheckoutQuery(id={self.id!r}, from_peer={self.from_peer!r}, currency={self.currency!r}, total_amount={self.total_amount!r}, invoice_payload={self.invoice_payload!r}, shipping_option_id={self.shipping_option_id!r}, order_info={self.order_info!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in precheckoutquery_instance`
        """
        return key in ["id", "from_peer", "currency", "total_amount", "invoice_payload", "shipping_option_id", "order_info"]
    # end def __contains__
# end class PreCheckoutQuery

