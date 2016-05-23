# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type
from . import Sendable

__author__ = 'luckydonald'

import logging

logger = logging.getLogger(__name__)

class Button(Sendable):
    def __init__(self):
        super(Button, self).__init__()

class ReplyMarkup(Sendable):
    def __init__(self):
        super(ReplyMarkup, self).__init__()
# end class


class KeyboardButton (Button):
    """
    This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields are mutually exclusive.
    Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#keyboardbutton
    """
    def __init__(self, text, request_contact = None, request_location = None):
        """
        This object represents one button of the reply keyboard. For simple text buttons String can be used instead of this object to specify text of the button. Optional fields are mutually exclusive.
        Note: request_contact and request_location options will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#keyboardbutton


        Parameters:

        :param text: Text of the button. If none of the optional fields are used, it will be sent to the bot as a message when the button is pressed
        :type  text:  str


        Optional keyword parameters:

        :keyword request_contact: Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only
        :type    request_contact:  bool

        :keyword request_location: Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only
        :type    request_location:  bool
        """
        super(KeyboardButton, self).__init__()

        assert(text is not None)
        assert(isinstance(text, unicode_type))  # unicode on python 2, str on python 3
        self.text = text

        assert(request_contact is None or isinstance(request_contact, bool))
        self.request_contact = request_contact

        assert(request_location is None or isinstance(request_location, bool))
        self.request_location = request_location
    # end def __init__

    def to_array(self):
        array = super(KeyboardButton, self).to_array()
        array["text"] = self.text
        if self.request_contact is not None:
            array["request_contact"] = self.request_contact
        if self.request_location is not None:
            array["request_location"] = self.request_location
        return array
    # end def to_array
# end class KeyboardButton


class InlineKeyboardButton (Button):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """
    def __init__(self, text, url = None, callback_data = None, switch_inline_query = None):
        """
        This object represents one button of an inline keyboard. You must use exactly one of the optional fields.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

        https://core.telegram.org/bots/api#inlinekeyboardbutton


        Parameters:

        :param text: Label text on the button
        :type  text:  str


        Optional keyword parameters:

        :keyword url: Optional. HTTP url to be opened when button is pressed
        :type    url:  str

        :keyword callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed, 1-64 bytes
        :type    callback_data:  str

        :keyword switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot‘s username and the specified inline query in the input field. Can be empty, in which case just the bot’s username will be inserted.Note: This offers an easy way for users to start using your bot in inline mode when they are currently in a private chat with it. Especially useful when combined with switch_pm… actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
        :type    switch_inline_query:  str
        """
        super(InlineKeyboardButton, self).__init__()

        assert(text is not None)
        assert(isinstance(text, unicode_type))  # unicode on python 2, str on python 3
        self.text = text

        assert(url is None or isinstance(url, unicode_type))  # unicode on python 2, str on python 3
        self.url = url

        assert(callback_data is None or isinstance(callback_data, unicode_type))  # unicode on python 2, str on python 3
        self.callback_data = callback_data

        assert(switch_inline_query is None or isinstance(switch_inline_query, unicode_type))  # unicode on python 2, str on python 3
        self.switch_inline_query = switch_inline_query
    # end def __init__

    def to_array(self):
        array = super(InlineKeyboardButton, self).to_array()
        array["text"] = self.text
        if self.url is not None:
            array["url"] = self.url
        if self.callback_data is not None:
            array["callback_data"] = self.callback_data
        if self.switch_inline_query is not None:
            array["switch_inline_query"] = self.switch_inline_query
        return array
    # end def to_array
# end class InlineKeyboardButton


class ReplyKeyboardMarkup(ReplyMarkup):
    """
    This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    https://core.telegram.org/bots/api#replykeyboardmarkup
    """
    def __init__(self, buttons, resize_keyboard=False, one_time_keyboard=False, selective=False):
        """
        This object represents a custom keyboard with reply options.
        
        https://core.telegram.org/bots/api#replykeyboardmarkup


        Parameters:

        :param buttons: Array of button rows, each represented by an Array of Strings (aka. 2D Array of button Strings)
        :type  buttons: list of (list of KeyboardButton)


        Optional keyword parameters:

        :keyword resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to false, in which case the custom keyboard is always of the same height as the app's standard keyboard.
        :type    resize_keyboard: bool

        :keyword one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. Defaults to false.
        :type    one_time_keyboard: bool

        :keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
                            Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
        :type    selective: bool
        """
        super(ReplyKeyboardMarkup, self).__init__()
        assert(buttons is not None)
        assert(isinstance(buttons, (list, tuple)))  # Array of Array of KeyboardButton
        self.keyboard = buttons
        assert(resize_keyboard is None or isinstance(resize_keyboard, bool))
        self.resize_keyboard = resize_keyboard
        assert(one_time_keyboard is None or isinstance(one_time_keyboard, bool))
        self.one_time_keyboard = one_time_keyboard
        assert(selective is None or isinstance(selective, bool))
        self.selective = selective
    pass

    def to_array(self):
        array = super(ReplyKeyboardMarkup, self).to_array()
        array["keyboard"] = self.keyboard
        if self.resize_keyboard is not None:
            array["resize_keyboard"] = self.resize_keyboard
        if self.one_time_keyboard is not None:
            array["one_time_keyboard"] = self.one_time_keyboard
        if self.selective is not None:
            array["selective"] = self.selective
        return array
    # end def to_array


class ReplyKeyboardHide(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will hide the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardhide
    """
    def __init__(self, selective = False):
        """
        Upon receiving a message with this object, Telegram clients will hide the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

        https://core.telegram.org/bots/api#replykeyboardhide


        Optional keyword parameters:

        :keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
                            Example: A user requests to change the bot‘s language, bot replies to the request with a keyboard to select the new language. Other users in the group don’t see the keyboard.
        :type    selective: bool
        """
        super(ReplyKeyboardHide, self).__init__()
        self.hide_keyboard = True
        self.selective = selective
    # end def __init__

    def to_array(self):
        array = super(ReplyKeyboardHide, self).to_array()
        array["hide_keyboard"] = self.hide_keyboard
        if self.selective is not None:
            array["selective"] = self.selective
        return array
    # end def to_array
# end class ReplyKeyboardHide


class ForceReply(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot‘s message and tapped ’Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions). There could be two ways to create a new poll:

    The last option is definitely more attractive. And if you use ForceReply in your bot‘s questions, it will receive the user’s answers even if it only receives replies, commands and mentions — without any extra work for the user.

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
        The last option is definitely more attractive. And if you use ForceReply in your bot‘s questions, it will receive the user’s answers even if it only receives replies, commands and mentions — without any extra work for the user.

        https://core.telegram.org/bots/api#forcereply


        Parameters:

        :param force_reply: Shows reply interface to the user, as if they manually selected the bot‘s message and tapped ’Reply'
        :type  force_reply:  True


        Optional keyword parameters:
        :keyword selective: Optional. Use this parameter if you want to show the keyboard to specific users only.
                            Targets:
                            1) users that are @mentioned in the text of the Message object;
                            2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
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
        array = super(ForceReply, self).to_array()
        array["force_reply"] = self.force_reply
        if self.selective is not None:
            array["selective"] = self.selective
        return array
    # end def to_array
# end class ForceReply


class InlineKeyboardMarkup(ReplyMarkup):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.

    Warning: Inline keyboards are currently being tested and are only available in one-on-one chats (i.e., user-bot or user-user in the case of inline bots).

    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will display unsupported message.

    https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """
    def __init__(self, inline_keyboard):
        """
        This object represents an inline keyboard that appears right next to the message it belongs to.

        Warning: Inline keyboards are currently being tested and are only available in one-on-one chats
                 (i.e., user-bot or user-user in the case of inline bots).

        Note: This will only work in Telegram versions released after 9 April, 2016.
              Older clients will display unsupported message.

        https://core.telegram.org/bots/api#inlinekeyboardmarkup


        Parameters:

        :param inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects.
        :type  inline_keyboard: list of list of InlineKeyboardButton
        """
        super(InlineKeyboardMarkup, self).__init__()

        assert(inline_keyboard is not None)
        assert(isinstance(inline_keyboard, (list, tuple)))  # Array of Array of InlineKeyboardButton
        self.inline_keyboard = inline_keyboard
    # end def __init__

    def to_array(self):
        array = super(InlineKeyboardMarkup, self).to_array()
        array["inline_keyboard"] = self.inline_keyboard
        return array
    # end def to_array
# end class InlineKeyboardMarkup