# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

__author__ = 'luckydonald'


class Button(Sendable):
    """
    Class for grouping KeyboardButton, KeyboardButtonPollType and InlineKeyboardButton.

    Optional keyword parameters:
    """

    def __init__(self):
        super(Button, self).__init__()
    # end def __init__
# end class Button


class ReplyMarkup(Sendable):
    """
    Class for grouping ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup and ForceReply.

    Optional keyword parameters:
    """

    def __init__(self):
        super(ReplyMarkup, self).__init__()
    # end def __init__
# end class ReplyMarkup


class ReplyKeyboardMarkup(ReplyMarkup):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    https://core.telegram.org/bots/api#replykeyboardmarkup


    Parameters:

    :param keyboard: Array of button rows, each represented by an Array of KeyboardButton objects
    :type  keyboard: list of list of pytgbot.api_types.sendable.reply_markup.KeyboardButton


    Optional keyword parameters:

    :param resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    :type  resize_keyboard: bool

    :param one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
    :type  one_time_keyboard: bool

    :param selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    :type  selective: bool
    """

    def __init__(self, keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
        """
        This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

        https://core.telegram.org/bots/api#replykeyboardmarkup


        Parameters:

        :param keyboard: Array of button rows, each represented by an Array of KeyboardButton objects
        :type  keyboard: list of list of pytgbot.api_types.sendable.reply_markup.KeyboardButton


        Optional keyword parameters:

        :param resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
        :type  resize_keyboard: bool

        :param one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to false.
        :type  one_time_keyboard: bool

        :param selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
        :type  selective: bool
        """
        super(ReplyKeyboardMarkup, self).__init__()

        assert_type_or_raise(keyboard, list, parameter_name="keyboard")
        self.keyboard = keyboard
        assert_type_or_raise(resize_keyboard, None, bool, parameter_name="resize_keyboard")
        self.resize_keyboard = resize_keyboard
        assert_type_or_raise(one_time_keyboard, None, bool, parameter_name="one_time_keyboard")
        self.one_time_keyboard = one_time_keyboard
        assert_type_or_raise(selective, None, bool, parameter_name="selective")
        self.selective = selective
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ReplyKeyboardMarkup to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ReplyKeyboardMarkup, self).to_array()

        array['keyboard'] = self._as_array(self.keyboard)  # type list of list of KeyboardButton
        if self.resize_keyboard is not None:
            array['resize_keyboard'] = bool(self.resize_keyboard)  # type bool
        # end if
        if self.one_time_keyboard is not None:
            array['one_time_keyboard'] = bool(self.one_time_keyboard)  # type bool
        # end if
        if self.selective is not None:
            array['selective'] = bool(self.selective)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ReplyKeyboardMarkup constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = ReplyMarkup.validate_array(array)
        data['keyboard'] = KeyboardButton.from_array_list(array.get('keyboard'), list_level=2)
        data['resize_keyboard'] = bool(array.get('resize_keyboard')) if array.get('resize_keyboard') is not None else None
        data['one_time_keyboard'] = bool(array.get('one_time_keyboard')) if array.get('one_time_keyboard') is not None else None
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ReplyKeyboardMarkup from a given dictionary.

        :return: new ReplyKeyboardMarkup instance.
        :rtype: ReplyKeyboardMarkup
        """
        if not array:  # None or {}
            return None
        # end if

        data = ReplyKeyboardMarkup.validate_array(array)
        instance = ReplyKeyboardMarkup(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(replykeyboardmarkup_instance)`
        """
        return "ReplyKeyboardMarkup(keyboard={self.keyboard!r}, resize_keyboard={self.resize_keyboard!r}, one_time_keyboard={self.one_time_keyboard!r}, selective={self.selective!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(replykeyboardmarkup_instance)`
        """
        if self._raw:
            return "ReplyKeyboardMarkup.from_array({self._raw})".format(self=self)
        # end if
        return "ReplyKeyboardMarkup(keyboard={self.keyboard!r}, resize_keyboard={self.resize_keyboard!r}, one_time_keyboard={self.one_time_keyboard!r}, selective={self.selective!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in replykeyboardmarkup_instance`
        """
        return (
            key in ["keyboard", "resize_keyboard", "one_time_keyboard", "selective"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ReplyKeyboardMarkup


class KeyboardButton(Button):
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#keyboardbutton


    Parameters:

    :param text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    :type  text: str|unicode


    Optional keyword parameters:

    :param request_contact: Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
    :type  request_contact: bool

    :param request_location: Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
    :type  request_location: bool

    :param request_poll: Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
    :type  request_poll: pytgbot.api_types.sendable.reply_markup.KeyboardButtonPollType
    """

    def __init__(self, text, request_contact=None, request_location=None, request_poll=None):
        """
        This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields request_contact, request_location, and request_poll are mutually exclusive.
        Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.Note: request_poll option will only work in Telegram versions released after 23 January, 2020. Older clients will display unsupported message.

        https://core.telegram.org/bots/api#keyboardbutton


        Parameters:

        :param text: Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
        :type  text: str|unicode


        Optional keyword parameters:

        :param request_contact: Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
        :type  request_contact: bool

        :param request_location: Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
        :type  request_location: bool

        :param request_poll: Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only
        :type  request_poll: pytgbot.api_types.sendable.reply_markup.KeyboardButtonPollType
        """
        super(KeyboardButton, self).__init__()

        assert_type_or_raise(text, unicode_type, parameter_name="text")
        self.text = text
        assert_type_or_raise(request_contact, None, bool, parameter_name="request_contact")
        self.request_contact = request_contact
        assert_type_or_raise(request_location, None, bool, parameter_name="request_location")
        self.request_location = request_location
        assert_type_or_raise(request_poll, None, KeyboardButtonPollType, parameter_name="request_poll")
        self.request_poll = request_poll
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this KeyboardButton to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(KeyboardButton, self).to_array()

        array['text'] = u(self.text)  # py2: type unicode, py3: type str
        if self.request_contact is not None:
            array['request_contact'] = bool(self.request_contact)  # type bool
        # end if
        if self.request_location is not None:
            array['request_location'] = bool(self.request_location)  # type bool
        # end if
        if self.request_poll is not None:
            array['request_poll'] = self.request_poll.to_array()  # type KeyboardButtonPollType
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the KeyboardButton constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = Button.validate_array(array)
        data['text'] = u(array.get('text'))
        data['request_contact'] = bool(array.get('request_contact')) if array.get('request_contact') is not None else None
        data['request_location'] = bool(array.get('request_location')) if array.get('request_location') is not None else None
        data['request_poll'] = KeyboardButtonPollType.from_array(array.get('request_poll')) if array.get('request_poll') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new KeyboardButton from a given dictionary.

        :return: new KeyboardButton instance.
        :rtype: KeyboardButton
        """
        if not array:  # None or {}
            return None
        # end if

        data = KeyboardButton.validate_array(array)
        instance = KeyboardButton(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(keyboardbutton_instance)`
        """
        return "KeyboardButton(text={self.text!r}, request_contact={self.request_contact!r}, request_location={self.request_location!r}, request_poll={self.request_poll!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(keyboardbutton_instance)`
        """
        if self._raw:
            return "KeyboardButton.from_array({self._raw})".format(self=self)
        # end if
        return "KeyboardButton(text={self.text!r}, request_contact={self.request_contact!r}, request_location={self.request_location!r}, request_poll={self.request_poll!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in keyboardbutton_instance`
        """
        return (
            key in ["text", "request_contact", "request_location", "request_poll"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class KeyboardButton


class KeyboardButtonPollType(Button):
    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    https://core.telegram.org/bots/api#keyboardbuttonpolltype

    Optional keyword parameters:

    :param type: Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    :type  type: str|unicode
    """

    def __init__(self, type=None):
        """
        This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

        https://core.telegram.org/bots/api#keyboardbuttonpolltype

        Optional keyword parameters:

        :param type: Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
        :type  type: str|unicode
        """
        super(KeyboardButtonPollType, self).__init__()
        assert_type_or_raise(type, None, unicode_type, parameter_name="type")
        self.type = type
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this KeyboardButtonPollType to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(KeyboardButtonPollType, self).to_array()

        if self.type is not None:
            array['type'] = u(self.type)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the KeyboardButtonPollType constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Button.validate_array(array)
        data['type'] = u(array.get('type')) if array.get('type') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new KeyboardButtonPollType from a given dictionary.

        :return: new KeyboardButtonPollType instance.
        :rtype: KeyboardButtonPollType
        """
        if not array:  # None or {}
            return None
        # end if

        data = KeyboardButtonPollType.validate_array(array)
        instance = KeyboardButtonPollType(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(keyboardbuttonpolltype_instance)`
        """
        return "KeyboardButtonPollType(type={self.type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(keyboardbuttonpolltype_instance)`
        """
        if self._raw:
            return "KeyboardButtonPollType.from_array({self._raw})".format(self=self)
        # end if
        return "KeyboardButtonPollType(type={self.type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in keyboardbuttonpolltype_instance`
        """
        return (
            key in ["type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class KeyboardButtonPollType


class ReplyKeyboardRemove(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardremove


    Parameters:


    Optional keyword parameters:

    :param selective: Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    :type  selective: bool
    """

    def __init__(self, selective=None):
        """
        Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

        https://core.telegram.org/bots/api#replykeyboardremove


        Parameters:


        Optional keyword parameters:

        :param selective: Optional. Use this parameter if you want to remove the keyboard for specific users only.
                          Targets: 1) users that are @mentioned in the text of the Message object;
                                   2) if the bot's message is a reply (has reply_to_message_id),
                                      sender of the original message.
                          Example: A user requests to change the bot's language,
                                   bot replies to the request with a keyboard to select the new language.
                                   Other users in the group don't see the keyboard.
                          Example: A user votes in a poll, bot returns confirmation message in reply to the vote and
                                   removes keyboard for that user, while still showing the keyboard with poll options to
                                   users who haven't voted yet.
        :type  selective: bool
        """
        super(ReplyKeyboardRemove, self).__init__()
        self.remove_keyboard = True
        assert_type_or_raise(selective, None, bool, parameter_name="selective")
        self.selective = selective
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ReplyKeyboardRemove to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ReplyKeyboardRemove, self).to_array()

        array['remove_keyboard'] = bool(self.remove_keyboard)  # type bool
        if self.selective is not None:
            array['selective'] = bool(self.selective)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ReplyKeyboardRemove constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ReplyMarkup.validate_array(array)
        data['remove_keyboard'] = bool(array.get('remove_keyboard'))
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ReplyKeyboardRemove from a given dictionary.

        :return: new ReplyKeyboardRemove instance.
        :rtype: ReplyKeyboardRemove
        """
        if not array:  # None or {}
            return None
        # end if
        assert_type_or_raise(array, dict, parameter_name="array")

        data = ReplyKeyboardRemove.validate_array(array)
        assert (bool(array.get('remove_keyboard')) == True)
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None

        instance = ReplyKeyboardRemove(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(replykeyboardremove_instance)`
        """
        return "ReplyKeyboardRemove(remove_keyboard={self.remove_keyboard!r}, selective={self.selective!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(replykeyboardremove_instance)`
        """
        if self._raw:
            return "ReplyKeyboardRemove.from_array({self._raw})".format(self=self)
        # end if
        return "ReplyKeyboardRemove(remove_keyboard={self.remove_keyboard!r}, selective={self.selective!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in replykeyboardremove_instance`
        """
        return (
            key in ["remove_keyboard", "selective"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ReplyKeyboardRemove


class InlineKeyboardMarkup(ReplyMarkup):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardmarkup


    Parameters:

    :param inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects
    :type  inline_keyboard: list of list of pytgbot.api_types.sendable.reply_markup.InlineKeyboardButton


    Optional keyword parameters:
    """

    def __init__(self, inline_keyboard):
        """
        This object represents an inline keyboard that appears right next to the message it belongs to.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

        https://core.telegram.org/bots/api#inlinekeyboardmarkup


        Parameters:

        :param inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects
        :type  inline_keyboard: list of list of pytgbot.api_types.sendable.reply_markup.InlineKeyboardButton


        Optional keyword parameters:
        """
        super(InlineKeyboardMarkup, self).__init__()

        assert_type_or_raise(inline_keyboard, list, parameter_name="inline_keyboard")
        self.inline_keyboard = inline_keyboard
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineKeyboardMarkup to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineKeyboardMarkup, self).to_array()

        array['inline_keyboard'] = self._as_array(self.inline_keyboard)  # type list of list of InlineKeyboardButton

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineKeyboardMarkup constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")

        data = ReplyMarkup.validate_array(array)
        data['inline_keyboard'] = InlineKeyboardButton.from_array_list(array.get('inline_keyboard'), list_level=2)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineKeyboardMarkup from a given dictionary.

        :return: new InlineKeyboardMarkup instance.
        :rtype: InlineKeyboardMarkup
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineKeyboardMarkup.validate_array(array)
        instance = InlineKeyboardMarkup(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinekeyboardmarkup_instance)`
        """
        return "InlineKeyboardMarkup(inline_keyboard={self.inline_keyboard!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinekeyboardmarkup_instance)`
        """
        if self._raw:
            return "InlineKeyboardMarkup.from_array({self._raw})".format(self=self)
        # end if
        return "InlineKeyboardMarkup(inline_keyboard={self.inline_keyboard!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinekeyboardmarkup_instance`
        """
        return (
            key in ["inline_keyboard"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineKeyboardMarkup


class InlineKeyboardButton(Button):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Note: This will only work in Telegram versions released after 9 April, 2016.
          Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardbutton


    Parameters:

    :param text: Label text on the button
    :type  text: str|unicode


    Optional keyword parameters:

    :param url: Optional. HTTP or tg:// url to be opened when button is pressed
    :type  url: str|unicode

    :param login_url: Optional. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
    :type  login_url: pytgbot.api_types.sendable.reply_markup.LoginUrl

    :param callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
    :type  callback_data: str|unicode

    :param switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    :type  switch_inline_query: str|unicode

    :param switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
    :type  switch_inline_query_current_chat: str|unicode

    :param callback_game: Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
    :type  callback_game: pytgbot.api_types.receivable.updates.CallbackGame

    :param pay: Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row.
    :type  pay: bool
    """

    def __init__(self, text, url=None, login_url=None, callback_data=None, switch_inline_query=None, switch_inline_query_current_chat=None, callback_game=None, pay=None):
        """
        This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

        https://core.telegram.org/bots/api#inlinekeyboardbutton


        Parameters:

        :param text: Label text on the button
        :type  text: str|unicode


        Optional keyword parameters:

        :param url: Optional. HTTP or tg:// url to be opened when button is pressed
        :type  url: str|unicode

        :param login_url: Optional. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
        :type  login_url: pytgbot.api_types.sendable.reply_markup.LoginUrl

        :param callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
        :type  callback_data: str|unicode

        :param switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
        :type  switch_inline_query: str|unicode

        :param switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
        :type  switch_inline_query_current_chat: str|unicode

        :param callback_game: Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
        :type  callback_game: pytgbot.api_types.receivable.updates.CallbackGame

        :param pay: Optional. Specify True, to send a Pay button.NOTE: This type of button must always be the first button in the first row.
        :type  pay: bool
        """
        super(InlineKeyboardButton, self).__init__()
        from ..receivable.updates import CallbackGame

        assert_type_or_raise(text, unicode_type, parameter_name="text")
        self.text = text
        assert_type_or_raise(url, None, unicode_type, parameter_name="url")
        self.url = url
        assert_type_or_raise(login_url, None, LoginUrl, parameter_name="login_url")
        self.login_url = login_url
        assert_type_or_raise(callback_data, None, unicode_type, parameter_name="callback_data")
        self.callback_data = callback_data
        assert_type_or_raise(switch_inline_query, None, unicode_type, parameter_name="switch_inline_query")
        self.switch_inline_query = switch_inline_query
        assert_type_or_raise(switch_inline_query_current_chat, None, unicode_type, parameter_name="switch_inline_query_current_chat")
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        assert_type_or_raise(callback_game, None, CallbackGame, parameter_name="callback_game")
        self.callback_game = callback_game
        assert_type_or_raise(pay, None, bool, parameter_name="pay")
        self.pay = pay
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this InlineKeyboardButton to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(InlineKeyboardButton, self).to_array()

        array['text'] = u(self.text)  # py2: type unicode, py3: type str
        if self.url is not None:
            array['url'] = u(self.url)  # py2: type unicode, py3: type str
        # end if
        if self.login_url is not None:
            array['login_url'] = self.login_url.to_array()  # type LoginUrl
        # end if
        if self.callback_data is not None:
            array['callback_data'] = u(self.callback_data)  # py2: type unicode, py3: type str
        # end if
        if self.switch_inline_query is not None:
            array['switch_inline_query'] = u(self.switch_inline_query)  # py2: type unicode, py3: type str
        # end if
        if self.switch_inline_query_current_chat is not None:
            array['switch_inline_query_current_chat'] = u(self.switch_inline_query_current_chat)  # py2: type unicode, py3: type str
        # end if
        if self.callback_game is not None:
            array['callback_game'] = self.callback_game.to_array()  # type CallbackGame
        # end if
        if self.pay is not None:
            array['pay'] = bool(self.pay)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the InlineKeyboardButton constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from ..receivable.updates import CallbackGame

        data = Button.validate_array(array)
        data['text'] = u(array.get('text'))
        data['url'] = u(array.get('url')) if array.get('url') is not None else None
        data['login_url'] = LoginUrl.from_array(array.get('login_url')) if array.get('login_url') is not None else None
        data['callback_data'] = u(array.get('callback_data')) if array.get('callback_data') is not None else None
        data['switch_inline_query'] = u(array.get('switch_inline_query')) if array.get('switch_inline_query') is not None else None
        data['switch_inline_query_current_chat'] = u(array.get('switch_inline_query_current_chat')) if array.get('switch_inline_query_current_chat') is not None else None
        data['callback_game'] = CallbackGame.from_array(array.get('callback_game')) if array.get('callback_game') is not None else None
        data['pay'] = bool(array.get('pay')) if array.get('pay') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new InlineKeyboardButton from a given dictionary.

        :return: new InlineKeyboardButton instance.
        :rtype: InlineKeyboardButton
        """
        if not array:  # None or {}
            return None
        # end if

        data = InlineKeyboardButton.validate_array(array)
        instance = InlineKeyboardButton(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinekeyboardbutton_instance)`
        """
        return "InlineKeyboardButton(text={self.text!r}, url={self.url!r}, login_url={self.login_url!r}, callback_data={self.callback_data!r}, switch_inline_query={self.switch_inline_query!r}, switch_inline_query_current_chat={self.switch_inline_query_current_chat!r}, callback_game={self.callback_game!r}, pay={self.pay!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(inlinekeyboardbutton_instance)`
        """
        if self._raw:
            return "InlineKeyboardButton.from_array({self._raw})".format(self=self)
        # end if
        return "InlineKeyboardButton(text={self.text!r}, url={self.url!r}, login_url={self.login_url!r}, callback_data={self.callback_data!r}, switch_inline_query={self.switch_inline_query!r}, switch_inline_query_current_chat={self.switch_inline_query_current_chat!r}, callback_game={self.callback_game!r}, pay={self.pay!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in inlinekeyboardbutton_instance`
        """
        return (
            key in ["text", "url", "login_url", "callback_data", "switch_inline_query", "switch_inline_query_current_chat", "callback_game", "pay"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class InlineKeyboardButton


class LoginUrl(Sendable):
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
    Telegram apps support these buttons as of version 5.7.

    Sample bot: @discussbot

    https://core.telegram.org/bots/api#loginurl


    Parameters:

    :param url: An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
    :type  url: str|unicode


    Optional keyword parameters:

    :param forward_text: Optional. New text of the button in forwarded messages.
    :type  forward_text: str|unicode

    :param bot_username: Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
    :type  bot_username: str|unicode

    :param request_write_access: Optional. Pass True to request the permission for your bot to send messages to the user.
    :type  request_write_access: bool
    """

    def __init__(self, url, forward_text=None, bot_username=None, request_write_access=None):
        """
        This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:
        Telegram apps support these buttons as of version 5.7.

        Sample bot: @discussbot

        https://core.telegram.org/bots/api#loginurl


        Parameters:

        :param url: An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.
        :type  url: str|unicode


        Optional keyword parameters:

        :param forward_text: Optional. New text of the button in forwarded messages.
        :type  forward_text: str|unicode

        :param bot_username: Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.
        :type  bot_username: str|unicode

        :param request_write_access: Optional. Pass True to request the permission for your bot to send messages to the user.
        :type  request_write_access: bool
        """
        super(LoginUrl, self).__init__()
        assert_type_or_raise(url, unicode_type, parameter_name="url")
        self.url = url
        assert_type_or_raise(forward_text, None, unicode_type, parameter_name="forward_text")
        self.forward_text = forward_text
        assert_type_or_raise(bot_username, None, unicode_type, parameter_name="bot_username")
        self.bot_username = bot_username
        assert_type_or_raise(request_write_access, None, bool, parameter_name="request_write_access")
        self.request_write_access = request_write_access
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this LoginUrl to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(LoginUrl, self).to_array()

        array['url'] = u(self.url)  # py2: type unicode, py3: type str
        if self.forward_text is not None:
            array['forward_text'] = u(self.forward_text)  # py2: type unicode, py3: type str
        # end if
        if self.bot_username is not None:
            array['bot_username'] = u(self.bot_username)  # py2: type unicode, py3: type str
        # end if
        if self.request_write_access is not None:
            array['request_write_access'] = bool(self.request_write_access)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the LoginUrl constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Sendable.validate_array(array)
        data['url'] = u(array.get('url'))
        data['forward_text'] = u(array.get('forward_text')) if array.get('forward_text') is not None else None
        data['bot_username'] = u(array.get('bot_username')) if array.get('bot_username') is not None else None
        data['request_write_access'] = bool(array.get('request_write_access')) if array.get('request_write_access') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new LoginUrl from a given dictionary.

        :return: new LoginUrl instance.
        :rtype: LoginUrl
        """
        if not array:  # None or {}
            return None
        # end if

        data = LoginUrl.validate_array(array)
        instance = LoginUrl(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(loginurl_instance)`
        """
        return "LoginUrl(url={self.url!r}, forward_text={self.forward_text!r}, bot_username={self.bot_username!r}, request_write_access={self.request_write_access!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(loginurl_instance)`
        """
        if self._raw:
            return "LoginUrl.from_array({self._raw})".format(self=self)
        # end if
        return "LoginUrl(url={self.url!r}, forward_text={self.forward_text!r}, bot_username={self.bot_username!r}, request_write_access={self.request_write_access!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in loginurl_instance`
        """
        return (
            key in ["url", "forward_text", "bot_username", "request_write_access"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class LoginUrl


class ForceReply(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user
    (act as if the user has selected the bot's message and tapped 'Reply').
    This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice
    privacy mode.

    Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions).
             There could be two ways to create a new poll:
             1) Explain the user how to send a command with parameters (e.g. `/newpoll question answer1 answer2`).
                May be appealing for hardcore users but lacks modern day polish.
             2) Guide the user through a step-by-step process. 'Please send me your question',
                'Cool, now let's add the first answer option',
                'Great. Keep adding answer options, then send `/done` when you're ready'.
    The last option is definitely more attractive. And if you use ForceReply in your bot's questions,
    it will receive the user's answers even if it only receives replies, commands and mentions
    — without any extra work for the user.

    https://core.telegram.org/bots/api#forcereply


    Parameters:


    Optional keyword parameters:

    :param selective: Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    :type  selective: bool
    """

    def __init__(self, selective=None):
        """
        Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as
        if the user has selected the bot's message and tapped 'Reply').
        This can be extremely useful if you want to
        create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

        Example:
        A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions).
        There could be two ways to create a new poll:
         - Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2).
           May be appealing for hardcore users but lacks modern day polish.
         - Guide the user through a step-by-step process. 'Please send me your question',
           'Cool, now let's add the first answer option',
           'Great. Keep adding answer options, then send /done when you're ready'.
        The last option is definitely more attractive. And if you use ForceReply in your bot's questions,
        it will receive the user's answers even if it only receives replies, commands and mentions
        — without any extra work for the user.

        https://core.telegram.org/bots/api#forcereply


        Parameters:


        Optional keyword parameters:
        :param selective: Optional. Use this parameter if you want to show the keyboard to/force reply from specific users only.
                          Targets: 1) users that are @mentioned in the text of the Message object;
                                   2) if the bot's message is a reply (has reply_to_message_id),
                                      sender of the original message.
                          Example:
                          A user requests to change the bot's language, bot replies to the request with a keyboard to
                          select the new language. Other users in the group don't see the keyboard.
        :type  selective: bool
        """
        super(ForceReply, self).__init__()
        self.force_reply = True
        assert_type_or_raise(selective, None, bool, parameter_name="selective")
        self.selective = selective
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ForceReply to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ForceReply, self).to_array()

        array['force_reply'] = bool(self.force_reply)  # type bool
        if self.selective is not None:
            array['selective'] = bool(self.selective)  # type bool
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ForceReply constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ReplyMarkup.validate_array(array)
        data['force_reply'] = bool(array.get('force_reply'))
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ForceReply from a given dictionary.

        :return: new ForceReply instance.
        :rtype: ForceReply
        """
        if not array:  # None or {}
            return None
        # end if

        data = ForceReply.validate_array(array)
        assert(bool(array.get('force_reply')) == True)
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None

        instance = ForceReply(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(forcereply_instance)`
        """
        return "ForceReply(force_reply={self.force_reply!r}, selective={self.selective!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(forcereply_instance)`
        """
        if self._raw:
            return "ForceReply.from_array({self._raw})".format(self=self)
        # end if
        return "ForceReply(force_reply={self.force_reply!r}, selective={self.selective!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in forcereply_instance`
        """
        return (
            key in ["force_reply", "selective"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ForceReply

