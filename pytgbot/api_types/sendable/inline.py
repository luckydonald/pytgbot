# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type
from luckydonaldUtils.logger import logging

from pytgbot.api_types.sendable import Sendable

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class InputMessageContent(Sendable):
    """
    This object represents the content of a message to be sent as a result of an inline query.

    Telegram clients currently support the following 4 types:
        - InputTextMessageContent
        - InputLocationMessageContent
        - InputVenueMessageContent
        - InputContactMessageContent
    """
    pass


class InputTextMessageContent (InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    def __init__(self, message_text, parse_mode = None, disable_web_page_preview = None):
        """
        Represents the content of a text message to be sent as the result of an inline query.

        https://core.telegram.org/bots/api#inputtextmessagecontent


        Parameters:

        :param message_text: Text of the message to be sent, 1-4096 characters
        :type  message_text:  str


        Optional keyword parameters:

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool
        """
        super(InputTextMessageContent, self).__init__()

        assert(message_text is not None)
        assert(isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text

        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode

        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self):
        array = super(InputTextMessageContent, self).to_array()
        array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        return array
    # end def to_array
# end class InputTextMessageContent


class InputLocationMessageContent (InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    def __init__(self, latitude, longitude):
        """
        Represents the content of a location message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputlocationmessagecontent


        Parameters:

        :param latitude: Latitude of the location in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the location in degrees
        :type  longitude:  Float
        """
        super(InputLocationMessageContent, self).__init__()

        assert(latitude is not None)
        assert(isinstance(latitude, float))
        self.latitude = latitude

        assert(longitude is not None)
        assert(isinstance(longitude, float))
        self.longitude = longitude
    # end def __init__

    def to_array(self):
        array = super(InputLocationMessageContent, self).to_array()
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        return array
    # end def to_array
# end class InputLocationMessageContent


class InputVenueMessageContent (InputLocationMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    def __init__(self, latitude, longitude, title, address, foursquare_id=None):
        """
        Represents the content of a venue message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputvenuemessagecontent


        Parameters:

        :param latitude: Latitude of the venue in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the venue in degrees
        :type  longitude:  Float

        :param title: Name of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue, if known
        :type    foursquare_id:  str
        """
        super(InputVenueMessageContent, self).__init__(latitude=latitude, longitude=longitude)

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
        array = super(InputVenueMessageContent, self).to_array()
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
        return array
    # end def to_array
# end class InputVenueMessageContent


class InputContactMessageContent (InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    def __init__(self, phone_number, first_name, last_name=None):
        """
        Represents the content of a contact message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputcontactmessagecontent


        Parameters:

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name:  str
        """
        super(InputContactMessageContent, self).__init__()

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name
    # end def __init__

    def to_array(self):
        array = super(InputContactMessageContent, self).to_array()
        array["phone_number"] = self.phone_number
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        return array
    # end def to_array
# end class InputContactMessageContent
