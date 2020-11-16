# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
__author__ = 'luckydonald'


class Result(object):
    """
    Base class for every api object class.

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
# end class Result
