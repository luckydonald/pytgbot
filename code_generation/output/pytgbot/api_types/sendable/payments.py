# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

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

    def __init__(self, label, amount):
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
        super(LabeledPrice, self).__init__()
        assert_type_or_raise(label, unicode_type, parameter_name="label")
        self.label = label
        assert_type_or_raise(amount, int, parameter_name="amount")
        self.amount = amount
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this LabeledPrice to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(LabeledPrice, self).to_array()
        
        array['label'] = u(self.label)  # py2: type unicode, py3: type str
        array['amount'] = int(self.amount)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the LabeledPrice constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Sendable.validate_array(array)
        data['label'] = u(array.get('label'))
        data['amount'] = int(array.get('amount'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new LabeledPrice from a given dictionary.

        :return: new LabeledPrice instance.
        :rtype: LabeledPrice
        """
        if not array:  # None or {}
            return None
        # end if

        data = LabeledPrice.validate_array(array)
        instance = LabeledPrice(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(labeledprice_instance)`
        """
        return "LabeledPrice(label={self.label!r}, amount={self.amount!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(labeledprice_instance)`
        """
        if self._raw:
            return "LabeledPrice.from_array({self._raw})".format(self=self)
        # end if
        return "LabeledPrice(label={self.label!r}, amount={self.amount!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in labeledprice_instance`
        """
        return (
            key in ["label", "amount"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, id, title, prices):
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
        super(ShippingOption, self).__init__()
        
        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(prices, list, parameter_name="prices")
        self.prices = prices
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ShippingOption to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ShippingOption, self).to_array()
        
        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['prices'] = self._as_array(self.prices)  # type list of LabeledPrice

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ShippingOption constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        
        data = Sendable.validate_array(array)
        data['id'] = u(array.get('id'))
        data['title'] = u(array.get('title'))
        data['prices'] = LabeledPrice.from_array_list(array.get('prices'), list_level=1)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ShippingOption from a given dictionary.

        :return: new ShippingOption instance.
        :rtype: ShippingOption
        """
        if not array:  # None or {}
            return None
        # end if

        data = ShippingOption.validate_array(array)
        instance = ShippingOption(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(shippingoption_instance)`
        """
        return "ShippingOption(id={self.id!r}, title={self.title!r}, prices={self.prices!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(shippingoption_instance)`
        """
        if self._raw:
            return "ShippingOption.from_array({self._raw})".format(self=self)
        # end if
        return "ShippingOption(id={self.id!r}, title={self.title!r}, prices={self.prices!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in shippingoption_instance`
        """
        return (
            key in ["id", "title", "prices"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ShippingOption

