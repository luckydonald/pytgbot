# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Result

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

    def __init__(self, name, title, is_animated, contains_masks, stickers, thumb=None, _raw=None):
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
        super(StickerSet, self).__init__()
        from .media import PhotoSize
        from .media import Sticker
        
        assert_type_or_raise(name, unicode_type, parameter_name="name")
        self.name = name
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        assert_type_or_raise(is_animated, bool, parameter_name="is_animated")
        self.is_animated = is_animated
        assert_type_or_raise(contains_masks, bool, parameter_name="contains_masks")
        self.contains_masks = contains_masks
        assert_type_or_raise(stickers, list, parameter_name="stickers")
        self.stickers = stickers
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this StickerSet to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(StickerSet, self).to_array()
        
        array['name'] = u(self.name)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['is_animated'] = bool(self.is_animated)  # type bool
        array['contains_masks'] = bool(self.contains_masks)  # type bool
        array['stickers'] = self._as_array(self.stickers)  # type list of Sticker
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the StickerSet constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import PhotoSize
        from .media import Sticker
        
        data = Result.validate_array(array)
        data['name'] = u(array.get('name'))
        data['title'] = u(array.get('title'))
        data['is_animated'] = bool(array.get('is_animated'))
        data['contains_masks'] = bool(array.get('contains_masks'))
        data['stickers'] = Sticker.from_array_list(array.get('stickers'), list_level=1)
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new StickerSet from a given dictionary.

        :return: new StickerSet instance.
        :rtype: StickerSet
        """
        if not array:  # None or {}
            return None
        # end if

        data = StickerSet.validate_array(array)
        data['_raw'] = array
        return StickerSet(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(stickerset_instance)`
        """
        return "StickerSet(name={self.name!r}, title={self.title!r}, is_animated={self.is_animated!r}, contains_masks={self.contains_masks!r}, stickers={self.stickers!r}, thumb={self.thumb!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(stickerset_instance)`
        """
        if self._raw:
            return "StickerSet.from_array({self._raw})".format(self=self)
        # end if
        return "StickerSet(name={self.name!r}, title={self.title!r}, is_animated={self.is_animated!r}, contains_masks={self.contains_masks!r}, stickers={self.stickers!r}, thumb={self.thumb!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in stickerset_instance`
        """
        return (
            key in ["name", "title", "is_animated", "contains_masks", "stickers", "thumb"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
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

    def __init__(self, point, x_shift, y_shift, scale, _raw=None):
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
        super(MaskPosition, self).__init__()
        assert_type_or_raise(point, unicode_type, parameter_name="point")
        self.point = point
        assert_type_or_raise(x_shift, float, parameter_name="x_shift")
        self.x_shift = x_shift
        assert_type_or_raise(y_shift, float, parameter_name="y_shift")
        self.y_shift = y_shift
        assert_type_or_raise(scale, float, parameter_name="scale")
        self.scale = scale

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this MaskPosition to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(MaskPosition, self).to_array()
        
        array['point'] = u(self.point)  # py2: type unicode, py3: type str
        array['x_shift'] = float(self.x_shift)  # type float
        array['y_shift'] = float(self.y_shift)  # type float
        array['scale'] = float(self.scale)  # type float

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the MaskPosition constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Result.validate_array(array)
        data['point'] = u(array.get('point'))
        data['x_shift'] = float(array.get('x_shift'))
        data['y_shift'] = float(array.get('y_shift'))
        data['scale'] = float(array.get('scale'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new MaskPosition from a given dictionary.

        :return: new MaskPosition instance.
        :rtype: MaskPosition
        """
        if not array:  # None or {}
            return None
        # end if

        data = MaskPosition.validate_array(array)
        data['_raw'] = array
        return MaskPosition(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(maskposition_instance)`
        """
        return "MaskPosition(point={self.point!r}, x_shift={self.x_shift!r}, y_shift={self.y_shift!r}, scale={self.scale!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(maskposition_instance)`
        """
        if self._raw:
            return "MaskPosition.from_array({self._raw})".format(self=self)
        # end if
        return "MaskPosition(point={self.point!r}, x_shift={self.x_shift!r}, y_shift={self.y_shift!r}, scale={self.scale!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in maskposition_instance`
        """
        return (
            key in ["point", "x_shift", "y_shift", "scale"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class MaskPosition

