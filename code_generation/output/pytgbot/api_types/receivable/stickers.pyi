# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable import Result

__author__ = 'luckydonald'


class StickerSet(Result):
    """
    This object represents a sticker set.

    https://core.telegram.org/bots/api#stickerset


    Parameters:

    :param name: Sticker set name
    :type  name: str|unicode

    :param title: Sticker set title
    :type  title: str|unicode

    :param is_animated: True, if the sticker set contains animated stickers
    :type  is_animated: bool

    :param contains_masks: True, if the sticker set contains masks
    :type  contains_masks: bool

    :param stickers: List of all set stickers
    :type  stickers: list of pytgbot.api_types.receivable.media.Sticker


    Optional keyword parameters:

    :param thumb: Optional. Sticker set thumbnail in the .WEBP or .TGS format
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    name: str
    title: str
    is_animated: bool
    contains_masks: bool
    stickers: List[Sticker]
    thumb: PhotoSize
# end class StickerSet

class MaskPosition(Result):
    """
    This object describes the position on faces where a mask should be placed by default.

    https://core.telegram.org/bots/api#maskposition


    Parameters:

    :param point: The part of the face relative to which the mask should be placed. One of "forehead", "eyes", "mouth", or "chin".
    :type  point: str|unicode

    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    :type  x_shift: float

    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    :type  y_shift: float

    :param scale: Mask scaling coefficient. For example, 2.0 means double size.
    :type  scale: float


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    point: str
    x_shift: float
    y_shift: float
    scale: float
# end class MaskPosition
