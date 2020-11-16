# -*- coding: utf-8 -*-
import logging
from json import dumps as _json_dumps
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
# NOTE: `from . import receivable` import at the bottom of this file

__author__ = 'luckydonald'
# __all__ = ["sendable", "receivable", "TgBotApiObject", "as_array", "from_array_list"]
# __all__ = ["receivable", "TgBotApiObject", "as_array", "from_array_list"]
logger = logging.getLogger(__name__)


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
    def validate_array(array):
        """
        Builds a new array with valid values for the {{ clazz.clazz }} constructor.

        :return: new array with valid values
        :rtype: dict
        """
        return {}
    # end def

    @staticmethod
    def from_array(array):
        if not array:
            return None
        return TgBotApiObject()
    # end def from_array

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

        :param result: The result to parse

        :param list_level: "list of" * list_level
        :type  list_level: int

        :return: the result as `required_type` type
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
# end class


# # # # # # #
# Functions #
# # # # # # #


def from_array_list(required_type, result, list_level, is_builtin):
    """
    Tries to parse the `result` as type given in `required_type`, while traversing into lists as often as specified in `list_level`.

    :param required_type: What it should be parsed as
    :type  required_type: class

    :param result: The result to parse

    :param list_level: "list of" * list_level
    :type  list_level: int

    :param is_builtin: if it is a builtin python type like :class:`int`, :class:`bool`, etc.
    :type  is_builtin: bool

    :return: the result as `required_type` type
    """
    logger.debug("Trying parsing as {type}, list_level={list_level}, is_builtin={is_builtin}".format(
        type=required_type.__name__, list_level=list_level, is_builtin=is_builtin
    ))
    if list_level > 0:
        assert isinstance(result, (list, tuple))
        return [from_array_list(required_type, obj, list_level-1, is_builtin) for obj in result]
    # end if
    if is_builtin:
        if isinstance(result, required_type):
            logger.debug("Already is correct type.")
            return required_type(result)
        elif isinstance(required_type, unicode_type):  # handle str, so emojis work for py2.
            return u(result)
        else:
            import ast
            logger.warn("Trying parsing with ast.literal_eval()...")
            return ast.literal_eval(str(result))  # raises ValueError if it could not parse
        # end if
    else:
        return required_type.from_array(result)
    # end if
# end def _parse_builtin_type


def as_array(obj):
    """
    Creates an json-like representation of a variable, supporting types with a `.to_array()` function.

    :rtype: dict|list|str|int|float|bool|None
    """
    if hasattr(obj, "to_array"):
        return obj.to_array()
    elif isinstance(obj, (list, tuple)):
        return [as_array(x) for x in obj]
    elif isinstance(obj, dict):
        return {key:as_array(obj[key]) for key in obj.keys()}
    else:
        _json_dumps(obj)  # raises error if is wrong json
        return obj
    # end if
# end def


from . import receivable  # bottom of file so TgBotApiObject is already defined.
