# -*- coding: utf-8 -*-
from . import Sendable



class LabeledPrice(Sendable):
    """
    This object represents a portion of the price for goods or services.

    https://core.telegram.org/bots/api#labeledprice
    """
    def __init__(self, label, amount):
        """
        This object represents a portion of the price for goods or services.
    
        https://core.telegram.org/bots/api#labeledprice


        Parameters:
        
        :param label: Portion label
        :type  label: str
        
        :param amount: Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        :type  amount: int
        """
        super(LabeledPrice, self).__init__()
        assert(label is not None)
        assert(isinstance(label, str))
        self.label = label
        
        assert(amount is not None)
        assert(isinstance(amount, int))
        self.amount = amount
    # end def __init__

    def to_array(self):
        """
        Serializes this LabeledPrice to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(LabeledPrice, self).to_array()
        array['label'] = str(self.label)  # type str
        array['amount'] = int(self.amount)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new LabeledPrice from a given dictionary.

        :return: new LabeledPrice instance.
        :rtype: LabeledPrice
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        data = {}
        data['label'] = str(array.get('label'))
        data['amount'] = int(array.get('amount'))
        return LabeledPrice(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(labeledprice_instance)`
        """
        return "LabeledPrice(label={self.label!r}, amount={self.amount!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in labeledprice_instance`
        """
        return key in ["label", "amount"]
    # end def __contains__
# end class LabeledPrice



class ShippingOption(Sendable):
    """
    This object represents one shipping option.

    https://core.telegram.org/bots/api#shippingoption
    """
    def __init__(self, id, title, prices):
        """
        This object represents one shipping option.
    
        https://core.telegram.org/bots/api#shippingoption


        Parameters:
        
        :param id: Shipping option identifier
        :type  id: str
        
        :param title: Option title
        :type  title: str
        
        :param prices: List of price portions
        :type  prices: list of pytgbot.api_types.sendable.payments.LabeledPrice
        """
        super(ShippingOption, self).__init__()

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id
        
        assert(title is not None)
        assert(isinstance(title, str))
        self.title = title
        
        assert(prices is not None)
        assert(isinstance(prices, list))
        self.prices = prices
    # end def __init__

    def to_array(self):
        """
        Serializes this ShippingOption to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ShippingOption, self).to_array()
        array['id'] = str(self.id)  # type str
        array['title'] = str(self.title)  # type str
        array['prices'] = self._as_array(self.prices)  # type list of LabeledPrice
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ShippingOption from a given dictionary.

        :return: new ShippingOption instance.
        :rtype: ShippingOption
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))


        data = {}
        data['id'] = str(array.get('id'))
        data['title'] = str(array.get('title'))
        data['prices'] = LabeledPrice.from_array_list(array.get('prices'), list_level=1)
        return ShippingOption(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(shippingoption_instance)`
        """
        return "ShippingOption(id={self.id!r}, title={self.title!r}, prices={self.prices!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in shippingoption_instance`
        """
        return key in ["id", "title", "prices"]
    # end def __contains__
# end class ShippingOption

