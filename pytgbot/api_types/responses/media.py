# -*- coding: utf-8 -*-
import Result as Result
from luckydonaldUtils.encoding import unicode_type
from luckydonaldUtils.logger import logging

from pytgbot.api_types.receivable import Receivable

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class Media(Receivable):
    pass


class Voice(Media):
    """
    This object represents a voice note.

    https://core.telegram.org/bots/api#voice
    """
    def __init__(self, file_id, duration, mime_type = None, file_size = None):
        """
        This object represents a voice note.

        https://core.telegram.org/bots/api#voice


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id:  str

        :param duration: Duration of the audio in seconds as defined by sender
        :type  duration:  int


        Optional keyword parameters:

        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type:  str

        :keyword file_size: Optional. File size
        :type    file_size:  int
        """
        super(Voice, self).__init__(id)

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        assert(duration is not None)
        assert(isinstance(duration, int))
        self.duration = duration

        assert(mime_type is None or isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        array = super(Voice, self).to_array()
        array["file_id"] = self.file_id
        array["duration"] = self.duration
        if self.mime_type is not None:
            array["mime_type"] = self.mime_type
        if self.file_size is not None:
            array["file_size"] = self.file_size
        return array
    # end def to_array
# end class Voice

class Contact(object):
    """
    This object represents a phone contact.

    https://core.telegram.org/bots/api#contact
    """
    def __init__(self, phone_number, first_name, last_name = None, user_id = None):
        """
        This object represents a phone contact.

        https://core.telegram.org/bots/api#contact


        Parameters:

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name:  str

        :keyword user_id: Optional. Contact's user identifier in Telegram
        :type    user_id:  int
        """
        super(Contact, self).__init__(id)

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name

        assert(user_id is None or isinstance(user_id, int))
        self.user_id = user_id
    # end def __init__

    def to_array(self):
        array = super(Contact, self).to_array()
        array["phone_number"] = self.phone_number
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        if self.user_id is not None:
            array["user_id"] = self.user_id
        return array
    # end def to_array
# end class Contact

class Location (Receivable):
    """
    This object represents a point on the map.

    https://core.telegram.org/bots/api#location
    """
    def __init__(self, longitude, latitude):
        """
        This object represents a point on the map.

        https://core.telegram.org/bots/api#location


        Parameters:

        :param longitude: Longitude as defined by sender
        :type  longitude:  Float

        :param latitude: Latitude as defined by sender
        :type  latitude:  Float
        """
        super(Location, self).__init__(id)

        self.longitude = longitude

        self.latitude = latitude
    # end def __init__

    def to_array(self):
        array = super(Location, self).to_array()
        array["longitude"] = self.longitude
        array["latitude"] = self.latitude
        return array
    # end def to_array
# end class Location

class Venue (object):
    """
    This object represents a venue.

    https://core.telegram.org/bots/api#venue
    """
    def __init__(self, location, title, address, foursquare_id = None):
        """
        This object represents a venue.

        https://core.telegram.org/bots/api#venue


        Parameters:

        :param location: Venue location
        :type  location:  Location

        :param title: Name of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue
        :type    foursquare_id:  str
        """
        super(Venue, self).__init__(id)

        self.location = location

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(address is not None)
        assert(isinstance(address, unicode_type))  # unicode on python 2, str on python 3
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, unicode_type))  # unicode on python 2, str on python 3
        self.foursquare_id = foursquare_id
    # end def __init__

    def to_array(self):
        array = super(Venue, self).to_array()
        array["location"] = self.location
        array["title"] = self.title
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
        return array
    # end def to_array
# end class Venue


class PhotoSize (Result):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    https://core.telegram.org/bots/api#photosize
    """
    def __init__(self, file_id, width, height, file_size = None):
        """
        This object represents one size of a photo or a file / sticker thumbnail.

        https://core.telegram.org/bots/api#photosize


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id:  str

        :param width: Photo width
        :type  width:  int

        :param height: Photo height
        :type  height:  int


        Optional keyword parameters:

        :keyword file_size: Optional. File size
        :type    file_size:  int
        """
        super(PhotoSize, self).__init__(id)

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        assert(width is not None)
        assert(isinstance(width, int))
        self.width = width

        assert(height is not None)
        assert(isinstance(height, int))
        self.height = height

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        array = super(PhotoSize, self).to_array()
        array["file_id"] = self.file_id
        array["width"] = self.width
        array["height"] = self.height
        if self.file_size is not None:
            array["file_size"] = self.file_size
        return array
    # end def to_array

class UserProfilePhotos (Result):
    """
    This object represent a user's profile pictures.

    https://core.telegram.org/bots/api#userprofilephotos
    """
    def __init__(self, total_count, photos):
        """
        This object represent a user's profile pictures.

        https://core.telegram.org/bots/api#userprofilephotos


        Parameters:

        :param total_count: Total number of profile pictures the target user has
        :type  total_count:  int

        :param photos: Requested profile pictures (in up to 4 sizes each)
        :type  photos:  Array of Array of PhotoSize
        """
        super(UserProfilePhotos, self).__init__(id)

        assert(total_count is not None)
        assert(isinstance(total_count, int))
        self.total_count = total_count

        assert(photos is not None)
        assert(isinstance(photos, (list, tuple)))  # Array of Array of PhotoSize
        self.photos = photos
    # end def __init__

    def to_array(self):
        array = super(UserProfilePhotos, self).to_array()
        array["total_count"] = self.total_count
        array["photos"] = self.photos
        return array
    # end def to_array
# end class UserProfilePhotos


class Audio (Media):
    """
    This object represents an audio file to be treated as music by the Telegram clients.

    https://core.telegram.org/bots/api#audio
    """
    def __init__(self, file_id, duration, performer = None, title = None, mime_type = None, file_size = None):
        """
        This object represents an audio file to be treated as music by the Telegram clients.

        https://core.telegram.org/bots/api#audio


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id:  str

        :param duration: Duration of the audio in seconds as defined by sender
        :type  duration:  int


        Optional keyword parameters:

        :keyword performer: Optional. Performer of the audio as defined by sender or by audio tags
        :type    performer:  str

        :keyword title: Optional. Title of the audio as defined by sender or by audio tags
        :type    title:  str

        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type:  str

        :keyword file_size: Optional. File size
        :type    file_size:  int
        """
        super(Audio, self).__init__(id)

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        assert(duration is not None)
        assert(isinstance(duration, int))
        self.duration = duration

        assert(performer is None or isinstance(performer, unicode_type))  # unicode on python 2, str on python 3
        self.performer = performer

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(mime_type is None or isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        array = super(Audio, self).to_array()
        array["file_id"] = self.file_id
        array["duration"] = self.duration
        if self.performer is not None:
            array["performer"] = self.performer
        if self.title is not None:
            array["title"] = self.title
        if self.mime_type is not None:
            array["mime_type"] = self.mime_type
        if self.file_size is not None:
            array["file_size"] = self.file_size
        return array
    # end def to_array


class Document (Media):
    """
    This object represents a general file (as opposed to photos, voice messages and audio files).

    https://core.telegram.org/bots/api#document
    """
    def __init__(self, file_id, thumb = None, file_name = None, mime_type = None, file_size = None):
        """
        This object represents a general file (as opposed to photos, voice messages and audio files).

        https://core.telegram.org/bots/api#document


        Parameters:

        :param file_id: Unique file identifier
        :type  file_id:  str


        Optional keyword parameters:

        :keyword thumb: Optional. Document thumbnail as defined by sender
        :type    thumb:  PhotoSize

        :keyword file_name: Optional. Original filename as defined by sender
        :type    file_name:  str

        :keyword mime_type: Optional. MIME type of the file as defined by sender
        :type    mime_type:  str

        :keyword file_size: Optional. File size
        :type    file_size:  int
        """
        super(Document, self).__init__(id)

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        self.thumb = thumb

        assert(file_name is None or isinstance(file_name, unicode_type))  # unicode on python 2, str on python 3
        self.file_name = file_name

        assert(mime_type is None or isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        array = super(Document, self).to_array()
        array["file_id"] = self.file_id
        if self.thumb is not None:
            array["thumb"] = self.thumb
        if self.file_name is not None:
            array["file_name"] = self.file_name
        if self.mime_type is not None:
            array["mime_type"] = self.mime_type
        if self.file_size is not None:
            array["file_size"] = self.file_size
        return array
    # end def to_array


class Sticker (Media):
    """
    This object represents a sticker.

    https://core.telegram.org/bots/api#sticker
    """
    def __init__(self, file_id, width, height, thumb = None, file_size = None):
        """
        This object represents a sticker.

        https://core.telegram.org/bots/api#sticker


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id:  str

        :param width: Sticker width
        :type  width:  int

        :param height: Sticker height
        :type  height:  int


        Optional keyword parameters:

        :keyword thumb: Optional. Sticker thumbnail in .webp or .jpg format
        :type    thumb:  PhotoSize

        :keyword file_size: Optional. File size
        :type    file_size:  int
        """
        super(Sticker, self).__init__(id)

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        assert(width is not None)
        assert(isinstance(width, int))
        self.width = width

        assert(height is not None)
        assert(isinstance(height, int))
        self.height = height

        self.thumb = thumb

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        array = super(Sticker, self).to_array()
        array["file_id"] = self.file_id
        array["width"] = self.width
        array["height"] = self.height
        if self.thumb is not None:
            array["thumb"] = self.thumb
        if self.file_size is not None:
            array["file_size"] = self.file_size
        return array
    # end def to_array


class Video (Media):
    """
    This object represents a video file.

    https://core.telegram.org/bots/api#video
    """
    def __init__(self, file_id, width, height, duration, thumb = None, mime_type = None, file_size = None):
        """
        This object represents a video file.

        https://core.telegram.org/bots/api#video


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id:  str

        :param width: Video width as defined by sender
        :type  width:  int

        :param height: Video height as defined by sender
        :type  height:  int

        :param duration: Duration of the video in seconds as defined by sender
        :type  duration:  int


        Optional keyword parameters:

        :keyword thumb: Optional. Video thumbnail
        :type    thumb:  PhotoSize

        :keyword mime_type: Optional. Mime type of a file as defined by sender
        :type    mime_type:  str

        :keyword file_size: Optional. File size
        :type    file_size:  int
        """
        super(Video, self).__init__(id)

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        assert(width is not None)
        assert(isinstance(width, int))
        self.width = width

        assert(height is not None)
        assert(isinstance(height, int))
        self.height = height

        assert(duration is not None)
        assert(isinstance(duration, int))
        self.duration = duration

        self.thumb = thumb

        assert(mime_type is None or isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size
    # end def __init__

    def to_array(self):
        array = super(Video, self).to_array()
        array["file_id"] = self.file_id
        array["width"] = self.width
        array["height"] = self.height
        array["duration"] = self.duration
        if self.thumb is not None:
            array["thumb"] = self.thumb
        if self.mime_type is not None:
            array["mime_type"] = self.mime_type
        if self.file_size is not None:
            array["file_size"] = self.file_size
        return array
    # end def to_array
# end class Video


class File (Receivable):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

    Maximum file size to download is 20 MB

    https://core.telegram.org/bots/api#file
    """
    def __init__(self, file_id, file_size=None, file_path=None):
        """
        This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

        Maximum file size to download is 20 MB

        https://core.telegram.org/bots/api#file


        Parameters:

        :param file_id: Unique identifier for this file
        :type  file_id:  str


        Optional keyword parameters:

        :keyword file_size: Optional. File size, if known
        :type    file_size:  int

        :keyword file_path: Optional. File path. Use https://api.telegram.org/file/bot<token>/<file_path> to get the file.
        :type    file_path:  str
        """
        super(File, self).__init__()

        assert(file_id is not None)
        assert(isinstance(file_id, unicode_type))  # unicode on python 2, str on python 3
        self.file_id = file_id

        assert(file_size is None or isinstance(file_size, int))
        self.file_size = file_size

        assert(file_path is None or isinstance(file_path, unicode_type))  # unicode on python 2, str on python 3
        self.file_path = file_path
    # end def __init__

    @property
    def file_url(self, api_key):
        return "https://api.telegram.org/file/bot{token}/{file_path}".format(token=api_key, file_path=self.file_path)

    def to_array(self):
        array = super(File, self).to_array()
        array["file_id"] = self.file_id
        if self.file_size is not None:
            array["file_size"] = self.file_size
        if self.file_path is not None:
            array["file_path"] = self.file_path
        return array
    # end def to_array
# end class File
