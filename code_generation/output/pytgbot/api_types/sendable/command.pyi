# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.sendable import Sendable
from pytgbot.api_types.sendable.command import BotCommandScope

__author__ = 'luckydonald'


class BotCommand(Sendable):
    """
    This object represents a bot command.

    https://core.telegram.org/bots/api#botcommand


    Parameters:

    :param command: Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    :type  command: str|unicode

    :param description: Description of the command; 1-256 characters.
    :type  description: str|unicode


    Optional keyword parameters:
    """
    command: str
    description: str
# end class BotCommand

class BotCommandScope(Sendable):
    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

    https://core.telegram.org/bots/api#botcommandscope

    Optional keyword parameters:
    """
# end class BotCommandScope

class BotCommandScopeDefault(BotCommandScope):
    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

    https://core.telegram.org/bots/api#botcommandscopedefault


    Parameters:

    :param type: Scope type, must be default
    :type  type: str|unicode


    Optional keyword parameters:
    """
    type: str
# end class BotCommandScopeDefault

class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all private chats.

    https://core.telegram.org/bots/api#botcommandscopeallprivatechats


    Parameters:

    :param type: Scope type, must be all_private_chats
    :type  type: str|unicode


    Optional keyword parameters:
    """
    type: str
# end class BotCommandScopeAllPrivateChats

class BotCommandScopeAllGroupChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    https://core.telegram.org/bots/api#botcommandscopeallgroupchats


    Parameters:

    :param type: Scope type, must be all_group_chats
    :type  type: str|unicode


    Optional keyword parameters:
    """
    type: str
# end class BotCommandScopeAllGroupChats

class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    https://core.telegram.org/bots/api#botcommandscopeallchatadministrators


    Parameters:

    :param type: Scope type, must be all_chat_administrators
    :type  type: str|unicode


    Optional keyword parameters:
    """
    type: str
# end class BotCommandScopeAllChatAdministrators

class BotCommandScopeChat(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific chat.

    https://core.telegram.org/bots/api#botcommandscopechat


    Parameters:

    :param type: Scope type, must be chat
    :type  type: str|unicode

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :type  chat_id: int | str|unicode


    Optional keyword parameters:
    """
    type: str
    chat_id: Union[int, str]
# end class BotCommandScopeChat

class BotCommandScopeChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    https://core.telegram.org/bots/api#botcommandscopechatadministrators


    Parameters:

    :param type: Scope type, must be chat_administrators
    :type  type: str|unicode

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :type  chat_id: int | str|unicode


    Optional keyword parameters:
    """
    type: str
    chat_id: Union[int, str]
# end class BotCommandScopeChatAdministrators

class BotCommandScopeChatMember(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

    https://core.telegram.org/bots/api#botcommandscopechatmember


    Parameters:

    :param type: Scope type, must be chat_member
    :type  type: str|unicode

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :type  chat_id: int | str|unicode

    :param user_id: Unique identifier of the target user
    :type  user_id: int


    Optional keyword parameters:
    """
    type: str
    chat_id: Union[int, str]
    user_id: int
# end class BotCommandScopeChatMember
