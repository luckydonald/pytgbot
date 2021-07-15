# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Sendable

__author__ = 'luckydonald'
__all__ = [
    'BotCommand',
    'BotCommandScope',
    'BotCommandScopeDefault',
    'BotCommandScopeAllPrivateChats',
    'BotCommandScopeAllGroupChats',
    'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeChat',
    'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
]


class BotCommand(Sendable):
    """
    This object represents a bot command.

    https://core.telegram.org/bots/api#botcommand


    Parameters:

    :param command: Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    :type  command: str|unicode

    :param description: Description of the command, 3-256 characters.
    :type  description: str|unicode


    Optional keyword parameters:
    """

    def __init__(self, command, description):
        """
        This object represents a bot command.

        https://core.telegram.org/bots/api#botcommand


        Parameters:

        :param command: Text of the command, 1-32 characters. Can contain only lowercase English letters, digits and underscores.
        :type  command: str|unicode

        :param description: Description of the command, 3-256 characters.
        :type  description: str|unicode


        Optional keyword parameters:
        """
        super(BotCommand, self).__init__()
        assert_type_or_raise(command, unicode_type, parameter_name="command")
        self.command = command
        assert_type_or_raise(description, unicode_type, parameter_name="description")
        self.description = description
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommand to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommand, self).to_array()

        array['command'] = u(self.command)  # py2: type unicode, py3: type str
        array['description'] = u(self.description)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommand constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Sendable.validate_array(array)
        data['command'] = u(array.get('command'))
        data['description'] = u(array.get('description'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommand from a given dictionary.

        :return: new BotCommand instance.
        :rtype: BotCommand
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommand.validate_array(array)
        instance = BotCommand(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommand_instance)`
        """
        return "BotCommand(command={self.command!r}, description={self.description!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommand_instance)`
        """
        if self._raw:
            return "BotCommand.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommand(command={self.command!r}, description={self.description!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommand_instance`
        """
        return (
            key in ["command", "description"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommand


class BotCommandScope(Sendable):
    """
    This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

    https://core.telegram.org/bots/api#botcommandscope

    Optional keyword parameters:
    """

    def __init__(self):
        """
        This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

        https://core.telegram.org/bots/api#botcommandscope

        Optional keyword parameters:
        """
        super(BotCommandScope, self).__init__()
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScope to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScope, self).to_array()

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScope constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Sendable.validate_array(array)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScope from a given dictionary.

        :return: new BotCommandScope instance.
        :rtype: BotCommandScope
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScope.validate_array(array)
        instance = BotCommandScope(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscope_instance)`
        """
        return "BotCommandScope()".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscope_instance)`
        """
        if self._raw:
            return "BotCommandScope.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScope()".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscope_instance`
        """
        return (
            key in []
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScope


class BotCommandScopeDefault(BotCommandScope):
    """
    Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

    https://core.telegram.org/bots/api#botcommandscopedefault


    Parameters:


    Optional keyword parameters:
    """

    def __init__(self):
        """
        Represents the default scope of bot commands. Default commands are used if no commands with a narrower scope are specified for the user.

        https://core.telegram.org/bots/api#botcommandscopedefault


        Parameters:


        Optional keyword parameters:
        """
        super(BotCommandScopeDefault, self).__init__()
        self.type = 'default'
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeDefault to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeDefault, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeDefault constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always default.
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeDefault from a given dictionary.

        :return: new BotCommandScopeDefault instance.
        :rtype: BotCommandScopeDefault
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeDefault.validate_array(array)
        instance = BotCommandScopeDefault(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopedefault_instance)`
        """
        return "BotCommandScopeDefault(type={self.type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopedefault_instance)`
        """
        if self._raw:
            return "BotCommandScopeDefault.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeDefault(type={self.type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopedefault_instance`
        """
        return (
            key in ["type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeDefault


class BotCommandScopeAllPrivateChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all private chats.

    https://core.telegram.org/bots/api#botcommandscopeallprivatechats


    Parameters:


    Optional keyword parameters:
    """

    def __init__(self):
        """
        Represents the scope of bot commands, covering all private chats.

        https://core.telegram.org/bots/api#botcommandscopeallprivatechats


        Parameters:


        Optional keyword parameters:
        """
        super(BotCommandScopeAllPrivateChats, self).__init__()
        self.type = 'all_private_chats'
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeAllPrivateChats to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeAllPrivateChats, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeAllPrivateChats constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always all_private_chats.
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeAllPrivateChats from a given dictionary.

        :return: new BotCommandScopeAllPrivateChats instance.
        :rtype: BotCommandScopeAllPrivateChats
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeAllPrivateChats.validate_array(array)
        instance = BotCommandScopeAllPrivateChats(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopeallprivatechats_instance)`
        """
        return "BotCommandScopeAllPrivateChats(type={self.type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopeallprivatechats_instance)`
        """
        if self._raw:
            return "BotCommandScopeAllPrivateChats.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeAllPrivateChats(type={self.type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopeallprivatechats_instance`
        """
        return (
            key in ["type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeAllPrivateChats


class BotCommandScopeAllGroupChats(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.

    https://core.telegram.org/bots/api#botcommandscopeallgroupchats


    Parameters:


    Optional keyword parameters:
    """

    def __init__(self):
        """
        Represents the scope of bot commands, covering all group and supergroup chats.

        https://core.telegram.org/bots/api#botcommandscopeallgroupchats


        Parameters:


        Optional keyword parameters:
        """
        super(BotCommandScopeAllGroupChats, self).__init__()
        self.type = 'all_group_chats'
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeAllGroupChats to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeAllGroupChats, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeAllGroupChats constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always all_group_chats.
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeAllGroupChats from a given dictionary.

        :return: new BotCommandScopeAllGroupChats instance.
        :rtype: BotCommandScopeAllGroupChats
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeAllGroupChats.validate_array(array)
        instance = BotCommandScopeAllGroupChats(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopeallgroupchats_instance)`
        """
        return "BotCommandScopeAllGroupChats(type={self.type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopeallgroupchats_instance)`
        """
        if self._raw:
            return "BotCommandScopeAllGroupChats.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeAllGroupChats(type={self.type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopeallgroupchats_instance`
        """
        return (
            key in ["type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeAllGroupChats


class BotCommandScopeAllChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all group and supergroup chat administrators.

    https://core.telegram.org/bots/api#botcommandscopeallchatadministrators


    Parameters:


    Optional keyword parameters:
    """

    def __init__(self):
        """
        Represents the scope of bot commands, covering all group and supergroup chat administrators.

        https://core.telegram.org/bots/api#botcommandscopeallchatadministrators


        Parameters:


        Optional keyword parameters:
        """
        super(BotCommandScopeAllChatAdministrators, self).__init__()
        self.type = 'all_chat_administrators'
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeAllChatAdministrators to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeAllChatAdministrators, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeAllChatAdministrators constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always all_chat_administrators.
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeAllChatAdministrators from a given dictionary.

        :return: new BotCommandScopeAllChatAdministrators instance.
        :rtype: BotCommandScopeAllChatAdministrators
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeAllChatAdministrators.validate_array(array)
        instance = BotCommandScopeAllChatAdministrators(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopeallchatadministrators_instance)`
        """
        return "BotCommandScopeAllChatAdministrators(type={self.type!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopeallchatadministrators_instance)`
        """
        if self._raw:
            return "BotCommandScopeAllChatAdministrators.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeAllChatAdministrators(type={self.type!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopeallchatadministrators_instance`
        """
        return (
            key in ["type"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeAllChatAdministrators


class BotCommandScopeChat(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific chat.

    https://core.telegram.org/bots/api#botcommandscopechat


    Parameters:

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :type  chat_id: int | str|unicode


    Optional keyword parameters:
    """

    def __init__(self, chat_id):
        """
        Represents the scope of bot commands, covering a specific chat.

        https://core.telegram.org/bots/api#botcommandscopechat


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type  chat_id: int | str|unicode


        Optional keyword parameters:
        """
        super(BotCommandScopeChat, self).__init__()
        self.type = 'chat'
        assert_type_or_raise(chat_id, int, unicode_type, parameter_name="chat_id")
        self.chat_id = chat_id
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeChat to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeChat, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        if isinstance(self.chat_id, int):
            array['chat_id'] = int(self.chat_id)  # type int
        elif isinstance(self.chat_id, str):
            array['chat_id'] = u(self.chat_id)  # py2: type unicode, py3: type str
        else:
            raise TypeError('Unknown type, must be one of int, str.')
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeChat constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always chat.
        if isinstance(array.get('chat_id'), int):
            data['chat_id'] = int(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['chat_id'] = u(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of int, str.')
        # end if
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeChat from a given dictionary.

        :return: new BotCommandScopeChat instance.
        :rtype: BotCommandScopeChat
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeChat.validate_array(array)
        instance = BotCommandScopeChat(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopechat_instance)`
        """
        return "BotCommandScopeChat(type={self.type!r}, chat_id={self.chat_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopechat_instance)`
        """
        if self._raw:
            return "BotCommandScopeChat.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeChat(type={self.type!r}, chat_id={self.chat_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopechat_instance`
        """
        return (
            key in ["type", "chat_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeChat


class BotCommandScopeChatAdministrators(BotCommandScope):
    """
    Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

    https://core.telegram.org/bots/api#botcommandscopechatadministrators


    Parameters:

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :type  chat_id: int | str|unicode


    Optional keyword parameters:
    """

    def __init__(self, chat_id):
        """
        Represents the scope of bot commands, covering all administrators of a specific group or supergroup chat.

        https://core.telegram.org/bots/api#botcommandscopechatadministrators


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type  chat_id: int | str|unicode


        Optional keyword parameters:
        """
        super(BotCommandScopeChatAdministrators, self).__init__()
        self.type = 'chat_administrators'
        assert_type_or_raise(chat_id, int, unicode_type, parameter_name="chat_id")
        self.chat_id = chat_id
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeChatAdministrators to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeChatAdministrators, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        if isinstance(self.chat_id, int):
            array['chat_id'] = int(self.chat_id)  # type int
        elif isinstance(self.chat_id, str):
            array['chat_id'] = u(self.chat_id)  # py2: type unicode, py3: type str
        else:
            raise TypeError('Unknown type, must be one of int, str.')
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeChatAdministrators constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always chat_administrators.
        if isinstance(array.get('chat_id'), int):
            data['chat_id'] = int(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['chat_id'] = u(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of int, str.')
        # end if
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeChatAdministrators from a given dictionary.

        :return: new BotCommandScopeChatAdministrators instance.
        :rtype: BotCommandScopeChatAdministrators
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeChatAdministrators.validate_array(array)
        instance = BotCommandScopeChatAdministrators(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopechatadministrators_instance)`
        """
        return "BotCommandScopeChatAdministrators(type={self.type!r}, chat_id={self.chat_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopechatadministrators_instance)`
        """
        if self._raw:
            return "BotCommandScopeChatAdministrators.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeChatAdministrators(type={self.type!r}, chat_id={self.chat_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopechatadministrators_instance`
        """
        return (
            key in ["type", "chat_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeChatAdministrators


class BotCommandScopeChatMember(BotCommandScope):
    """
    Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

    https://core.telegram.org/bots/api#botcommandscopechatmember


    Parameters:

    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
    :type  chat_id: int | str|unicode

    :param user_id: Unique identifier of the target user
    :type  user_id: int


    Optional keyword parameters:
    """

    def __init__(self, chat_id, user_id):
        """
        Represents the scope of bot commands, covering a specific member of a group or supergroup chat.

        https://core.telegram.org/bots/api#botcommandscopechatmember


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        :type  chat_id: int | str|unicode

        :param user_id: Unique identifier of the target user
        :type  user_id: int


        Optional keyword parameters:
        """
        super(BotCommandScopeChatMember, self).__init__()
        self.type = 'chat_member'
        assert_type_or_raise(chat_id, int, unicode_type, parameter_name="chat_id")
        self.chat_id = chat_id
        assert_type_or_raise(user_id, int, parameter_name="user_id")
        self.user_id = user_id
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this BotCommandScopeChatMember to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(BotCommandScopeChatMember, self).to_array()

        array['type'] = u(self.type)  # py2: type unicode, py3: type str
        if isinstance(self.chat_id, int):
            array['chat_id'] = int(self.chat_id)  # type int
        elif isinstance(self.chat_id, str):
            array['chat_id'] = u(self.chat_id)  # py2: type unicode, py3: type str
        else:
            raise TypeError('Unknown type, must be one of int, str.')
        # end if
        array['user_id'] = int(self.user_id)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the BotCommandScopeChatMember constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = BotCommandScope.validate_array(array)
        # 'type' is always chat_member.
        if isinstance(array.get('chat_id'), int):
            data['chat_id'] = int(array.get('chat_id'))
        elif isinstance(array.get('chat_id'), str):
            data['chat_id'] = u(array.get('chat_id'))
        else:
            raise TypeError('Unknown type, must be one of int, str.')
        # end if
        data['user_id'] = int(array.get('user_id'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new BotCommandScopeChatMember from a given dictionary.

        :return: new BotCommandScopeChatMember instance.
        :rtype: BotCommandScopeChatMember
        """
        if not array:  # None or {}
            return None
        # end if

        data = BotCommandScopeChatMember.validate_array(array)
        instance = BotCommandScopeChatMember(**data)
        instance._raw = array
        return instance
    # end def from_array

    def __str__(self):
        """
        Implements `str(botcommandscopechatmember_instance)`
        """
        return "BotCommandScopeChatMember(type={self.type!r}, chat_id={self.chat_id!r}, user_id={self.user_id!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(botcommandscopechatmember_instance)`
        """
        if self._raw:
            return "BotCommandScopeChatMember.from_array({self._raw})".format(self=self)
        # end if
        return "BotCommandScopeChatMember(type={self.type!r}, chat_id={self.chat_id!r}, user_id={self.user_id!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in botcommandscopechatmember_instance`
        """
        return (
            key in ["type", "chat_id", "user_id"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class BotCommandScopeChatMember
