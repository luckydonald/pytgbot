# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type

from pytgbot.api_types import as_array
from . import Sendable
import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)


class Button(Sendable):
    def __init__(self):
        super(Button, self).__init__()
    # end def __init__
# end class Button


class ReplyMarkup(Sendable):
    def __init__(self):
        super(ReplyMarkup, self).__init__()
    # end def __init__
# end class ReplyMarkup


class ReplyKeyboardMarkup(ReplyMarkup):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    https://core.telegram.org/bots/api#replykeyboardmarkup
    """
    def __init__(self, keyboard, resize_keyboard=False, one_time_keyboard=False, selective=None):
        """
        This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

        https://core.telegram.org/bots/api#replykeyboardmarkup


        Parameters:

        :param keyboard: Array of button rows, each represented by an Array of KeyboardButton objects
        :type  keyboard: list of list of KeyboardButton


        Optional keyword parameters:

        :keyword resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g.,
                                  make the keyboard smaller if there are just two rows of buttons).
                                  Defaults to false, in which case the custom keyboard is always of the same height as
                                  the app's standard keyboard.
        :type    resize_keyboard: bool

        :keyword one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used.
                                    The keyboard will still be available, but clients will automatically display the
                                    usual letter-keyboard in the chat – the user can press a special button in the input
                                    field to see the custom keyboard again. Defaults to false.
        :type    one_time_keyboard: bool

        :keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only.
                            Targets: 1) users that are @mentioned in the text of the Message object;
                                     2) if the bot's message is a reply (has reply_to_message_id),
                                     sender of the original message.
                            Example: A user requests to change the bot‘s language,
                                    bot replies to the request with a keyboard to select the new language.
                                    Other users in the group don’t see the keyboard.
        :type    selective: bool
        """
        super(ReplyKeyboardMarkup, self).__init__()

        assert(keyboard is not None)
        assert(isinstance(keyboard, list))
        self.keyboard = keyboard

        assert(resize_keyboard is None or isinstance(resize_keyboard, bool))
        self.resize_keyboard = resize_keyboard

        assert(one_time_keyboard is None or isinstance(one_time_keyboard, bool))
        self.one_time_keyboard = one_time_keyboard

        assert(selective is None or isinstance(selective, bool))
        self.selective = selective
    # end def __init__

    def to_array(self):
        """
        Serializes this ReplyKeyboardMarkup to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ReplyKeyboardMarkup, self).to_array()
        array['keyboard'] = self._as_array(self.keyboard)  # type list of list of KeyboardButton
        if self.resize_keyboard is not None:
            array['resize_keyboard'] = bool(self.resize_keyboard)  # type bool
        if self.one_time_keyboard is not None:
            array['one_time_keyboard'] = bool(self.one_time_keyboard)  # type bool
        if self.selective is not None:
            array['selective'] = bool(self.selective)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ReplyKeyboardMarkup from a given dictionary.

        :return: new ReplyKeyboardMarkup instance.
        :rtype: ReplyKeyboardMarkup
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['keyboard'] = KeyboardButton.from_array_list(array.get('keyboard'), list_level=2)
        data['resize_keyboard'] = bool(array.get('resize_keyboard')) if array.get('resize_keyboard') is not None else None
        data['one_time_keyboard'] = bool(array.get('one_time_keyboard')) if array.get('one_time_keyboard') is not None else None
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None
        return ReplyKeyboardMarkup(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(replykeyboardmarkup_instance)`
        """
        return "ReplyKeyboardMarkup(keyboard={self.keyboard!r}, resize_keyboard={self.resize_keyboard!r}, one_time_keyboard={self.one_time_keyboard!r}, selective={self.selective!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in replykeyboardmarkup_instance`
        """
        return key in ["keyboard", "resize_keyboard", "one_time_keyboard", "selective"]
    # end def __contains__
# end class ReplyKeyboardMarkup


class KeyboardButton(Button):
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this
    object to specify text of the button. Optional fields are mutually exclusive.

    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016.
          Older clients will ignore them.

    https://core.telegram.org/bots/api#keyboardbutton
    """
    def __init__(self, text, request_contact=None, request_location=None):
        """
        This object represents one button of the reply keyboard. For simple text buttons String can be used instead of
        this object to specify text of the button. Optional fields are mutually exclusive.

        Note: request_contact and request_location options will only work in Telegram
              versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#keyboardbutton


        Parameters:

        :param text: Text of the button. If none of the optional fields are used,
                     it will be sent to the bot as a message when the button is pressed
        :type  text: str


        Optional keyword parameters:

        :keyword request_contact: Optional. If True, the user's phone number will be sent as a contact when the button
                                  is pressed. Available in private chats only
        :type    request_contact: bool

        :keyword request_location: Optional. If True, the user's current location will be sent when the button is
                                   pressed. Available in private chats only
        :type    request_location: bool
        """
        super(KeyboardButton, self).__init__()
        assert(text is not None)
        assert(isinstance(text, str))
        self.text = text

        assert(request_contact is None or isinstance(request_contact, bool))
        self.request_contact = request_contact

        assert(request_location is None or isinstance(request_location, bool))
        self.request_location = request_location
    # end def __init__

    def to_array(self):
        """
        Serializes this KeyboardButton to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(KeyboardButton, self).to_array()
        array['text'] = str(self.text)  # type str
        if self.request_contact is not None:
            array['request_contact'] = bool(self.request_contact)  # type bool
        if self.request_location is not None:
            array['request_location'] = bool(self.request_location)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new KeyboardButton from a given dictionary.

        :return: new KeyboardButton instance.
        :rtype: KeyboardButton
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['text'] = str(array.get('text'))
        data['request_contact'] = bool(array.get('request_contact')) if array.get('request_contact') is not None else None
        data['request_location'] = bool(array.get('request_location')) if array.get('request_location') is not None else None
        return KeyboardButton(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(keyboardbutton_instance)`
        """
        return "KeyboardButton(text={self.text!r}, request_contact={self.request_contact!r}, request_location={self.request_location!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in keyboardbutton_instance`
        """
        return key in ["text", "request_contact", "request_location"]
    # end def __contains__
# end class KeyboardButton


class ReplyKeyboardHide(ReplyMarkup):
    """
    Upon receiving a message with this object,
    Telegram clients will hide the current custom keyboard and display the default letter-keyboard.
    By default, custom keyboards are displayed until a new keyboard is sent by a bot.
    An exception is made for one-time keyboards that are hidden immediately after the user presses a button
    (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardhide
    """
    def __init__(self, selective=False):
        """
        Upon receiving a message with this object,
        Telegram clients will hide the current custom keyboard and display the default letter-keyboard.
        By default, custom keyboards are displayed until a new keyboard is sent by a bot.
        An exception is made for one-time keyboards that are hidden immediately after the user presses a button
        (see ReplyKeyboardMarkup).

        https://core.telegram.org/bots/api#replykeyboardhide


        Parameters:

        Optional keyword parameters:

        :keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only.
                            Targets: 1) users that are @mentioned in the text of the Message object;
                                     2) if the bot's message is a reply (has reply_to_message_id),
                                        sender of the original message.
                            Example: A user requests to change the bot‘s language,
                                     bot replies to the request with a keyboard to select the new language.
                                     Other users in the group don’t see the keyboard.
                            Example: A user votes in a poll, bot returns confirmation message in reply to the vote and
                                     hides keyboard for that user, while still showing the keyboard with poll options to
                                     users who haven't voted yet.
        :type    selective: bool
        """
        super(ReplyKeyboardHide, self).__init__()
        self.hide_keyboard = True

        assert(selective is None or isinstance(selective, bool))
        self.selective = selective
    # end def __init__

    def to_array(self):
        """
        Serializes this ReplyKeyboardHide to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ReplyKeyboardHide, self).to_array()
        array['hide_keyboard'] = bool(self.hide_keyboard)  # type bool
        if self.selective is not None:
            array['selective'] = bool(self.selective)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ReplyKeyboardHide from a given dictionary.

        :return: new ReplyKeyboardHide instance.
        :rtype: ReplyKeyboardHide
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None
        return ReplyKeyboardHide(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(replykeyboardhide_instance)`
        """
        return "ReplyKeyboardHide(hide_keyboard={self.hide_keyboard!r}, selective={self.selective!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in replykeyboardhide_instance`
        """
        return key in ["hide_keyboard", "selective"]
    # end def __contains__
# end class ReplyKeyboardHide


class InlineKeyboardMarkup(ReplyMarkup):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.

    Warning: Inline keyboards are currently being tested and are not available in channels yet.
         For now, feel free to use them in one-on-one chats or groups.

    Note: This will only work in Telegram versions released after 9 April, 2016.
          Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """
    def __init__(self, inline_keyboard):
        """
        This object represents an inline keyboard that appears right next to the message it belongs to.

        Warning: Inline keyboards are currently being tested and are not available in channels yet.
             For now, feel free to use them in one-on-one chats or groups.

        Note: This will only work in Telegram versions released after 9 April, 2016.
              Older clients will display unsupported message.

        https://core.telegram.org/bots/api#inlinekeyboardmarkup


        Parameters:

        :param inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects
        :type  inline_keyboard: list of list of InlineKeyboardButton
        """
        super(InlineKeyboardMarkup, self).__init__()

        assert(inline_keyboard is not None)
        assert(isinstance(inline_keyboard, list))
        self.inline_keyboard = inline_keyboard
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineKeyboardMarkup to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineKeyboardMarkup, self).to_array()
        array['inline_keyboard'] = self._as_array(self.inline_keyboard)  # type list of list of InlineKeyboardButton
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineKeyboardMarkup from a given dictionary.

        :return: new InlineKeyboardMarkup instance.
        :rtype: InlineKeyboardMarkup
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['inline_keyboard'] = InlineKeyboardButton.from_array_list(array.get('inline_keyboard'), list_level=2)
        return InlineKeyboardMarkup(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinekeyboardmarkup_instance)`
        """
        return "InlineKeyboardMarkup(inline_keyboard={self.inline_keyboard!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinekeyboardmarkup_instance`
        """
        return key in ["inline_keyboard"]
    # end def __contains__
# end class InlineKeyboardMarkup


class InlineKeyboardButton(Button):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    Note: This will only work in Telegram versions released after 9 April, 2016.
          Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """
    def __init__(self, text, url=None, callback_data=None, switch_inline_query=None, switch_inline_query_current_chat=None, callback_game=None):
        """
        This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

        Note: This will only work in Telegram versions released after 9 April, 2016.
              Older clients will display unsupported message.

        https://core.telegram.org/bots/api#inlinekeyboardbutton


        Parameters:

        :param text: Label text on the button
        :type  text: str


        Optional keyword parameters:

        :keyword url: Optional. HTTP url to be opened when button is pressed
        :type    url: str

        :keyword callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed,
                                1-64 bytes
        :type    callback_data: str

        :keyword switch_inline_query: Optional. If set,
                                      pressing the button will prompt the user to select one of their chats,
                                      open that chat and insert the bot‘s username and the specified
                                      inline query in the input field. Can be empty, in which case just the bot’s
                                      username will be inserted.
                                      Note:  This offers an easy way for users to start using your bot in inline mode
                                             when they are currently in a private chat with it.
                                             Especially useful when combined with switch_pm… action – in this case the
                                             user will be automatically returned to the chat they switched from,
                                             skipping the chat selection screen.
        :type    switch_inline_query: str
        
        :keyword switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot‘s username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot’s username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
        :type    switch_inline_query_current_chat: str
        
        :keyword callback_game: Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
        :type    callback_game: pytgbot.api_types.receivable.updates.CallbackGame
        """
        super(InlineKeyboardButton, self).__init__()
        from pytgbot.api_types.receivable.updates import CallbackGame

        assert(text is not None)
        assert(isinstance(text, str))
        self.text = text

        assert(url is None or isinstance(url, str))
        self.url = url

        assert(callback_data is None or isinstance(callback_data, str))
        self.callback_data = callback_data

        assert(switch_inline_query is None or isinstance(switch_inline_query, str))
        self.switch_inline_query = switch_inline_query
        
        assert(switch_inline_query_current_chat is None or isinstance(switch_inline_query_current_chat, str))
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        
        assert(callback_game is None or isinstance(callback_game, CallbackGame))
        self.callback_game = callback_game
    # end def __init__

    def to_array(self):
        """
        Serializes this InlineKeyboardButton to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(InlineKeyboardButton, self).to_array()
        array['text'] = str(self.text)  # type str
        if self.url is not None:
            array['url'] = str(self.url)  # type str
        if self.callback_data is not None:
            array['callback_data'] = str(self.callback_data)  # type str
        if self.switch_inline_query is not None:
            array['switch_inline_query'] = str(self.switch_inline_query)  # type str
        if self.switch_inline_query_current_chat is not None:
            array['switch_inline_query_current_chat'] = str(self.switch_inline_query_current_chat)  # type str
        if self.callback_game is not None:
            array['callback_game'] = self.callback_game.to_array()  # type CallbackGame
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new InlineKeyboardButton from a given dictionary.

        :return: new InlineKeyboardButton instance.
        :rtype: InlineKeyboardButton
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        from pytgbot.api_types.receivable.updates import CallbackGame

        data = {}
        data['text'] = str(array.get('text'))
        data['url'] = str(array.get('url')) if array.get('url') is not None else None
        data['callback_data'] = str(array.get('callback_data')) if array.get('callback_data') is not None else None
        data['switch_inline_query'] = str(array.get('switch_inline_query')) if array.get('switch_inline_query') is not None else None
        data['switch_inline_query_current_chat'] = str(array.get('switch_inline_query_current_chat')) if array.get('switch_inline_query_current_chat') is not None else None
        data['callback_game'] = CallbackGame.from_array(array.get('callback_game')) if array.get('callback_game') is not None else None
        return InlineKeyboardButton(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(inlinekeyboardbutton_instance)`
        """
        return "InlineKeyboardButton(text={self.text!r}, url={self.url!r}, callback_data={self.callback_data!r}, switch_inline_query={self.switch_inline_query!r}, switch_inline_query_current_chat={self.switch_inline_query_current_chat!r}, callback_game={self.callback_game!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in inlinekeyboardbutton_instance`
        """
        return key in ["text", "url", "callback_data", "switch_inline_query", "switch_inline_query_current_chat", "callback_game"]
    # end def __contains__
# end class InlineKeyboardButton


class ForceReply(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user
    (act as if the user has selected the bot‘s message and tapped ’Reply').
    This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice
    privacy mode.

    Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions).
             There could be two ways to create a new poll:
             1) Explain the user how to send a command with parameters (e.g. `/newpoll question answer1 answer2`).
                May be appealing for hardcore users but lacks modern day polish.
             2) Guide the user through a step-by-step process. ‘Please send me your question’,
                ‘Cool, now let’s add the first answer option‘,
                ’Great. Keep adding answer options, then send `/done` when you‘re ready’.
    The last option is definitely more attractive. And if you use ForceReply in your bot‘s questions,
    it will receive the user’s answers even if it only receives replies, commands and mentions
    — without any extra work for the user.

    https://core.telegram.org/bots/api#forcereply
    """
    def __init__(self, selective=False):
        """
        Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as
        if the user has selected the bot‘s message and tapped ’Reply').
        This can be extremely useful if you want to
        create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

        Example:
        A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions).
        There could be two ways to create a new poll:
         - Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2).
           May be appealing for hardcore users but lacks modern day polish.
         - Guide the user through a step-by-step process. ‘Please send me your question’,
           ‘Cool, now let’s add the first answer option‘,
           ’Great. Keep adding answer options, then send /done when you‘re ready’.
        The last option is definitely more attractive. And if you use ForceReply in your bot‘s questions,
        it will receive the user’s answers even if it only receives replies, commands and mentions
        — without any extra work for the user.

        https://core.telegram.org/bots/api#forcereply


        Parameters:

        Optional keyword parameters:
        :keyword selective: Optional. Use this parameter if you want to show the keyboard to/force reply from specific users only.
                            Targets: 1) users that are @mentioned in the text of the Message object;
                                     2) if the bot's message is a reply (has reply_to_message_id),
                                        sender of the original message.
                            Example:
                            A user requests to change the bot‘s language, bot replies to the request with a keyboard to
                            select the new language. Other users in the group don’t see the keyboard.
        :type    selective: bool
        """
        super(ForceReply, self).__init__()
        self.force_reply = True
        self.selective = selective
    # end def __init__

    def to_array(self):
        """
        Serializes this ForceReply to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ForceReply, self).to_array()
        array['force_reply'] = bool(self.force_reply)  # type bool
        if self.selective is not None:
            array['selective'] = bool(self.selective)  # type bool
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ForceReply from a given dictionary.

        :return: new ForceReply instance.
        :rtype: ForceReply
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        data = {}
        data['selective'] = bool(array.get('selective')) if array.get('selective') is not None else None
        return ForceReply(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(forcereply_instance)`
        """
        return "ForceReply(force_reply={self.force_reply!r}, selective={self.selective!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in forcereply_instance`
        """
        return key in ["force_reply", "selective"]
    # end def __contains__
# end class ForceReply
