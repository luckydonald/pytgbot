# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
__author__ = 'luckydonald'


class TgBotApiObject(object):
    """
    Base class for every api object class.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self):
        self._raw = None
        super(TgBotApiObject, self).__init__()
    # end def __init__

    def to_array(self):
        array = dict()
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        if not array:
            return None
        return {}
    # end def

    # # # # # # # # # # # # # #
    # helper functions below #
    # # # # # # # # # # # # #

    @classmethod
    def from_array_list(cls, result, list_level):
        """
        Tries to parse the `result` as type given in `required_type`, while traversing into lists as often as specified in `list_level`.

        :param cls: Type as what it should be parsed as. Can be any class extending :class:`TgBotApiObject`.
                    E.g. If you call `Class.from_array_list`, it will automatically be set to `Class`.
        :type  cls: class
    ,    :param result: The result to parse
    ,    :param list_level: "list of" * list_level
        :type  list_level: int
    ,    :return: the result as `required_type` type
        """
        return from_array_list(cls, result, list_level, is_builtin=False)  # the one below, not itself. Yes, same name...
    # end def from_array_list

    @staticmethod
    def _builtin_from_array_list(required_type, value, list_level):
        """
        Helper method to make :func:`from_array_list` available to all classes extending this,
        without the need for additional imports.

        :param required_type: Type as what it should be parsed as. Any builtin.
        :param value: The result to parse
        :param list_level: "list of" * list_level
        :return:
        """
        return from_array_list(required_type, value, list_level, is_builtin=True)
    # end def _builtin_from_array_list

    @staticmethod
    def _as_array(obj):
        """
        Helper method to make :func:`as_array` available to all classes extending this,
        without the need for additional imports.
        """
        return as_array(obj)
    # end def

    def __setattr__(self, key, value):
        """
        Remove `self._raw` if any other value is set.
        """
        super(TgBotApiObject, self).__setattr__(key, value)
        if not key.startswith('_') and hasattr(self, '_raw') and self._raw is not None:
            self._raw = None
        # end if
    # end def
# end class TgBotApiObject
