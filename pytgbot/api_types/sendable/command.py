# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

__author__ = 'luckydonald'


class BotCommand(Sendable):
    """
    This object represents a bot command.

    https://core.telegram.org/bots/api#botcommand
    

    Parameters:
    
    :param command: Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    :type  command: str|unicode
    
    :param description: Description of the command, 3-256 characters.
    :type  description: str|unicode
    

    Optional keyword parameters:
    """

    def __init__(self, command, description):
        """
        This object represents a bot command.

        https://core.telegram.org/bots/api#botcommand
        

        Parameters:
        
        :param command: Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
        :type  command: str|unicode
        
        :param description: Description of the command, 3-256 characters.
        :type  description: str|unicode
        

        Optional keyword parameters:
        """
        super(BotCommand, self).__init__()
        assert_type_or_raise(command, unicode_type, parameter_name="command")
        self.command = command
        assert_type_or_raise(description, unicode_type, parameter_name="description")
        self.description = description
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommand to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommand, self).to_array()
        
        array['command'] = u(self.command)  # py2: type unicode, py3: type str
        array['description'] = u(self.description)  # py2: type unicode, py3: type str

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommand constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Sendable.validate_array(array)
        data['command'] = u(array.get('command'))
        data['description'] = u(array.get('description'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommand from a given dictionary.

        :return: new BotCommand instance.
        :rtype: BotCommand
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommand.validate_array(array)
        instance = BotCommand(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommand_instance)`
        """
        return "BotCommand(command={self.command!r}, description={self.description!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommand_instance)`
        """
        if self._raw:
            return "BotCommand.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommand(command={self.command!r}, description={self.description!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommand_instance`
        """
        return (
            key in ["command", "description"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommand

