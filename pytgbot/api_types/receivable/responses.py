# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result

__author__ = 'luckydonald'


class MessageId(Result):
    """
    This object represents a unique message identifier.

    https://core.telegram.org/bots/api#messageid
    

    Parameters:
    
    :param message_id: Unique message identifier
    :type  message_id: int
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, message_id, _raw=None):
        """
        This object represents a unique message identifier.

        https://core.telegram.org/bots/api#messageid
        

        Parameters:
        
        :param message_id: Unique message identifier
        :type  message_id: int
        

        Optional keyword parameters:
        
        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(MessageId, self).__init__()
        assert_type_or_raise(message_id, int, parameter_name="message_id")
        self.message_id = message_id

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this MessageId to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(MessageId, self).to_array()
        
        array['message_id'] = int(self.message_id)  # type int

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the MessageId constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['message_id'] = int(array.get('message_id'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new MessageId from a given dictionary.

        :return: new MessageId instance.
        :rtype: MessageId
        """
        if not array:  # None or {}
            return None
        # end if

        data = MessageId.validate_array(array)
        data['_raw'] = array
        return MessageId(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(messageid_instance)`
        """
        return "MessageId(message_id={self.message_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(messageid_instance)`
        """
        if self._raw:
            return "MessageId.from_array({self._raw})".format(self=self)
        # end if
        return "MessageId(message_id={self.message_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in messageid_instance`
        """
        return (
            key in ["message_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class MessageId

