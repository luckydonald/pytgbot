# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from None import object
from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.reply_markup import Button
from pytgbot.api_types.sendable.reply_markup import ReplyMarkup

__author__ = 'luckydonald'


class Button(object):
    
# end class Button

class ReplyMarkup(object):
    
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
    keyboard: List[List[KeyboardButton]]
    resize_keyboard: bool
    one_time_keyboard: bool
    selective: bool
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
    text: str
    request_contact: bool
    request_location: bool
    request_poll: KeyboardButtonPollType
# end class KeyboardButton

class KeyboardButtonPollType(Button):
    """
    This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    https://core.telegram.org/bots/api#keyboardbuttonpolltype

    Optional keyword parameters:
    
    :param type: Optional. If quiz is passed, the user will be allowed to create only polls in the quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    :type  type: str|unicode
    """
    type: str
# end class KeyboardButtonPollType

class ReplyKeyboardRemove(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the user presses a button (see ReplyKeyboardMarkup).

    https://core.telegram.org/bots/api#replykeyboardremove
    

    Parameters:
    
    :param remove_keyboard: Requests clients to remove the custom keyboard (user will not be able to summon this keyboard; if you want to hide the keyboard from sight but keep it accessible, use one_time_keyboard in ReplyKeyboardMarkup)
    :type  remove_keyboard: bool
    

    Optional keyword parameters:
    
    :param selective: Optional. Use this parameter if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    :type  selective: bool
    """
    remove_keyboard: bool
    selective: bool
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
    inline_keyboard: List[List[InlineKeyboardButton]]
# end class InlineKeyboardMarkup

class InlineKeyboardButton(Button):
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
    text: str
    url: str
    login_url: LoginUrl
    callback_data: str
    switch_inline_query: str
    switch_inline_query_current_chat: str
    callback_game: CallbackGame
    pay: bool
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
    url: str
    forward_text: str
    bot_username: str
    request_write_access: bool
# end class LoginUrl

class ForceReply(ReplyMarkup):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and mentions). There could be two ways to create a new poll:

    Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2). May be appealing for hardcore users but lacks modern day polish.
    Guide the user through a step-by-step process. 'Please send me your question', 'Cool, now let's add the first answer option', 'Great. Keep adding answer options, then send /done when you're ready'.

    The last option is definitely more attractive. And if you use ForceReply in your bot's questions, it will receive the user's answers even if it only receives replies, commands and mentions — without any extra work for the user.

    https://core.telegram.org/bots/api#forcereply
    

    Parameters:
    
    :param force_reply: Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    :type  force_reply: bool
    

    Optional keyword parameters:
    
    :param selective: Optional. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
    :type  selective: bool
    """
    force_reply: bool
    selective: bool
# end class ForceReply
