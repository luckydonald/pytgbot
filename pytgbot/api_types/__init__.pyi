# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.typing import JSONType
from typing import TypeVar, Type, Union

__author__ = 'luckydonald'


class TgBotApiObject(object):
    """
    Base class for every api object class.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class TgBotApiObject


REQUIRED_TYPE = TypeVar('REQUIRED_TYPE')
def from_array_list(required_type: Type[REQUIRED_TYPE], result: JSONType, list_level: int, is_builtin: bool) -> REQUIRED_TYPE: pass

def as_array(obj: Union[TgBotApiObject, list, tuple, dict, JSONType]) -> JSONType: pass
