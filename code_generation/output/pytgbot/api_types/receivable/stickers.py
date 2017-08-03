# -*- coding: utf-8 -*-
from . import updates
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from pytgbot.api_types.receivable import Result
from pytgbot.api_types.receivable.media import Media



class Sticker(Media):
    """
    This object represents a sticker.

    https://core.telegram.org/bots/api#sticker
    

    Parameters:
    
    :param file_id: Unique identifier for this file
    :type  file_id: str|unicode
    
    :param width: Sticker width
    :type  width: int
    
    :param height: Sticker height
    :type  height: int
    

    Optional keyword parameters:
    
    :param thumb: Optional. Sticker thumbnail in the .webp or .jpg format
    :type  thumb: pytgbot.api_types.receivable.media.PhotoSize
    
    :param emoji: Optional. Emoji associated with the sticker
    :type  emoji: str|unicode
    
    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :type  set_name: str|unicode
    
    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :type  mask_position: pytgbot.api_types.receivable.stickers.MaskPosition
    
    :param file_size: Optional. File size
    :type  file_size: int
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, file_id, width, height, thumb=None, emoji=None, set_name=None, mask_position=None, file_size=None, _raw=None):
        """
        This object represents a sticker.
    
        https://core.telegram.org/bots/api#sticker
        
    
        Parameters:
        
        :param file_id: Unique identifier for this file
        :type  file_id: str|unicode
        
        :param width: Sticker width
        :type  width: int
        
        :param height: Sticker height
        :type  height: int
        
    
        Optional keyword parameters:
        
        :param thumb: Optional. Sticker thumbnail in the .webp or .jpg format
        :type  thumb: pytgbot.api_types.receivable.media.PhotoSize
        
        :param emoji: Optional. Emoji associated with the sticker
        :type  emoji: str|unicode
        
        :param set_name: Optional. Name of the sticker set to which the sticker belongs
        :type  set_name: str|unicode
        
        :param mask_position: Optional. For mask stickers, the position where the mask should be placed
        :type  mask_position: pytgbot.api_types.receivable.stickers.MaskPosition
        
        :param file_size: Optional. File size
        :type  file_size: int
        
        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Sticker, self).__init__()
        from pytgbot.api_types.receivable.media import PhotoSize
        from pytgbot.api_types.receivable.stickers import MaskPosition
        
        assert_type_or_raise(file_id, unicode_type, parameter_name="file_id")
        self.file_id = file_id
        
        assert_type_or_raise(width, int, parameter_name="width")
        self.width = width
        
        assert_type_or_raise(height, int, parameter_name="height")
        self.height = height
        
        assert_type_or_raise(thumb, None, PhotoSize, parameter_name="thumb")
        self.thumb = thumb
        
        assert_type_or_raise(emoji, None, unicode_type, parameter_name="emoji")
        self.emoji = emoji
        
        assert_type_or_raise(set_name, None, unicode_type, parameter_name="set_name")
        self.set_name = set_name
        
        assert_type_or_raise(mask_position, None, MaskPosition, parameter_name="mask_position")
        self.mask_position = mask_position
        
        assert_type_or_raise(file_size, None, int, parameter_name="file_size")
        self.file_size = file_size

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this Sticker to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(Sticker, self).to_array()
        array['file_id'] = u(self.file_id)  # py2: type unicode, py3: type str
        array['width'] = int(self.width)  # type int
        array['height'] = int(self.height)  # type int
        if self.thumb is not None:
            array['thumb'] = self.thumb.to_array()  # type PhotoSize
        if self.emoji is not None:
            array['emoji'] = u(self.emoji)  # py2: type unicode, py3: type str
        if self.set_name is not None:
            array['set_name'] = u(self.set_name)  # py2: type unicode, py3: type str
        if self.mask_position is not None:
            array['mask_position'] = self.mask_position.to_array()  # type MaskPosition
        if self.file_size is not None:
            array['file_size'] = int(self.file_size)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Sticker from a given dictionary.

        :return: new Sticker instance.
        :rtype: Sticker
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.receivable.media import PhotoSize
        from pytgbot.api_types.receivable.stickers import MaskPosition
        

        data = {}
        data['file_id'] = u(array.get('file_id'))
        data['width'] = int(array.get('width'))
        data['height'] = int(array.get('height'))
        data['thumb'] = PhotoSize.from_array(array.get('thumb')) if array.get('thumb') is not None else None
        data['emoji'] = u(array.get('emoji')) if array.get('emoji') is not None else None
        data['set_name'] = u(array.get('set_name')) if array.get('set_name') is not None else None
        data['mask_position'] = MaskPosition.from_array(array.get('mask_position')) if array.get('mask_position') is not None else None
        data['file_size'] = int(array.get('file_size')) if array.get('file_size') is not None else None
        data['_raw'] = array
        return Sticker(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(sticker_instance)`
        """
        return "Sticker(file_id={self.file_id!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, emoji={self.emoji!r}, set_name={self.set_name!r}, mask_position={self.mask_position!r}, file_size={self.file_size!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(sticker_instance)`
        """
        if self._raw:
            return "Sticker.from_array({self._raw})".format(self=self)
        # end if
        return "Sticker(file_id={self.file_id!r}, width={self.width!r}, height={self.height!r}, thumb={self.thumb!r}, emoji={self.emoji!r}, set_name={self.set_name!r}, mask_position={self.mask_position!r}, file_size={self.file_size!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in sticker_instance`
        """
        return key in ["file_id", "width", "height", "thumb", "emoji", "set_name", "mask_position", "file_size"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class Sticker



class StickerSet(Result):
    """
    This object represents a sticker set.

    https://core.telegram.org/bots/api#stickerset
    

    Parameters:
    
    :param name: Sticker set name
    :type  name: str|unicode
    
    :param title: Sticker set title
    :type  title: str|unicode
    
    :param contains_masks: True, if the sticker set contains masks
    :type  contains_masks: bool
    
    :param stickers: List of all set stickers
    :type  stickers: list of pytgbot.api_types.receivable.stickers.Sticker
    

    Optional keyword parameters:
    
    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, name, title, contains_masks, stickers, _raw=None):
        """
        This object represents a sticker set.
    
        https://core.telegram.org/bots/api#stickerset
        
    
        Parameters:
        
        :param name: Sticker set name
        :type  name: str|unicode
        
        :param title: Sticker set title
        :type  title: str|unicode
        
        :param contains_masks: True, if the sticker set contains masks
        :type  contains_masks: bool
        
        :param stickers: List of all set stickers
        :type  stickers: list of pytgbot.api_types.receivable.stickers.Sticker
        
    
        Optional keyword parameters:
        
        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(StickerSet, self).__init__()
        from pytgbot.api_types.receivable.stickers import Sticker
        
        assert_type_or_raise(name, unicode_type, parameter_name="name")
        self.name = name
        
        assert_type_or_raise(title, unicode_type, parameter_name="title")
        self.title = title
        
        assert_type_or_raise(contains_masks, bool, parameter_name="contains_masks")
        self.contains_masks = contains_masks
        
        assert_type_or_raise(stickers, list, parameter_name="stickers")
        self.stickers = stickers

        self._raw = _raw
    # end def __init__

    def to_array(self):
        """
        Serializes this StickerSet to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(StickerSet, self).to_array()
        array['name'] = u(self.name)  # py2: type unicode, py3: type str
        array['title'] = u(self.title)  # py2: type unicode, py3: type str
        array['contains_masks'] = bool(self.contains_masks)  # type bool
        array['stickers'] = self._as_array(self.stickers)  # type list of Sticker
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new StickerSet from a given dictionary.

        :return: new StickerSet instance.
        :rtype: StickerSet
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")
        from pytgbot.api_types.receivable.stickers import Sticker
        

        data = {}
        data['name'] = u(array.get('name'))
        data['title'] = u(array.get('title'))
        data['contains_masks'] = bool(array.get('contains_masks'))
        data['stickers'] = Sticker.from_array_list(array.get('stickers'), list_level=1)
        data['_raw'] = array
        return StickerSet(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(stickerset_instance)`
        """
        return "StickerSet(name={self.name!r}, title={self.title!r}, contains_masks={self.contains_masks!r}, stickers={self.stickers!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(stickerset_instance)`
        """
        if self._raw:
            return "StickerSet.from_array({self._raw})".format(self=self)
        # end if
        return "StickerSet(name={self.name!r}, title={self.title!r}, contains_masks={self.contains_masks!r}, stickers={self.stickers!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in stickerset_instance`
        """
        return key in ["name", "title", "contains_masks", "stickers"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class StickerSet



class MaskPosition(Result):
    """
    This object describes the position on faces where a mask should be placed by default.

    https://core.telegram.org/bots/api#maskposition
    

    Parameters:
    
    :param point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
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
        
        :param point: The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
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

    def to_array(self):
        """
        Serializes this MaskPosition to a dictionary.

        :return: dictionary representation of this object.
        :rtype: dict
        """
        array = super(MaskPosition, self).to_array()
        array['point'] = u(self.point)  # py2: type unicode, py3: type str
        array['x_shift'] = float(self.x_shift)  # type float
        array['y_shift'] = float(self.y_shift)  # type float
        array['scale'] = float(self.scale)  # type float
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new MaskPosition from a given dictionary.

        :return: new MaskPosition instance.
        :rtype: MaskPosition
        """
        if array is None or not array:
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = {}
        data['point'] = u(array.get('point'))
        data['x_shift'] = float(array.get('x_shift'))
        data['y_shift'] = float(array.get('y_shift'))
        data['scale'] = float(array.get('scale'))
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
        return key in ["point", "x_shift", "y_shift", "scale"] and hasattr(self, key) and getattr(self, key)
    # end def __contains__
# end class MaskPosition

