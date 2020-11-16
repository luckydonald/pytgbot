# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Receivable

__author__ = 'luckydonald'


class UpdateType(Receivable):
    """
    All extending classes are an property of the Update type.
    Like Message: Update.message

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    pass
# end class UpdateType


class CallbackGame(UpdateType):
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.

    https://core.telegram.org/bots/api#callbackgame

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, _raw=None):
        """
        A placeholder, currently holds no information. Use BotFather to set up your game.

        https://core.telegram.org/bots/api#callbackgame

        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(CallbackGame, self).__init__()


        self._raw = _raw
    # end def __init__

    def to_array(self):
        return {}
    # end def

    @staticmethod
    def validate_array(array):
        return {}
    # end def

    @staticmethod
    def from_array(array):
        """
        Deserialize a new CallbackGame from a given dictionary.

        :return: new CallbackGame instance.
        :rtype: CallbackGame
        """
        if not array:  # None or {}
            return None
        # end if

        data = CallbackGame.validate_array(array)
        data['_raw'] = array
        return CallbackGame(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(callbackgame_instance)`
        """
        return "CallbackGame()".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(callbackgame_instance)`
        """
        if self._raw:
            return "CallbackGame.from_array({self._raw})".format(self=self)
        # end if
        return "CallbackGame()".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in callbackgame_instance`
        """
        return (
            key in []
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class CallbackGame


class Update(Receivable):
    """
    This object represents an incoming update.At most one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update


    Parameters:

    :param update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    :type  update_id: int


    Optional keyword parameters:

    :param message: Optional. New incoming message of any kind — text, photo, sticker, etc.
    :type  message: pytgbot.api_types.receivable.updates.Message

    :param edited_message: Optional. New version of a message that is known to the bot and was edited
    :type  edited_message: pytgbot.api_types.receivable.updates.Message

    :param channel_post: Optional. New incoming channel post of any kind — text, photo, sticker, etc.
    :type  channel_post: pytgbot.api_types.receivable.updates.Message

    :param edited_channel_post: Optional. New version of a channel post that is known to the bot and was edited
    :type  edited_channel_post: pytgbot.api_types.receivable.updates.Message

    :param inline_query: Optional. New incoming inline query
    :type  inline_query: pytgbot.api_types.receivable.inline.InlineQuery

    :param chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
    :type  chosen_inline_result: pytgbot.api_types.receivable.inline.ChosenInlineResult

    :param callback_query: Optional. New incoming callback query
    :type  callback_query: pytgbot.api_types.receivable.updates.CallbackQuery

    :param shipping_query: Optional. New incoming shipping query. Only for invoices with flexible price
    :type  shipping_query: pytgbot.api_types.receivable.payments.ShippingQuery

    :param pre_checkout_query: Optional. New incoming pre-checkout query. Contains full information about checkout
    :type  pre_checkout_query: pytgbot.api_types.receivable.payments.PreCheckoutQuery

    :param poll: Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
    :type  poll: pytgbot.api_types.receivable.media.Poll

    :param poll_answer: Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    :type  poll_answer: pytgbot.api_types.receivable.media.PollAnswer

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, update_id, message=None, edited_message=None, channel_post=None, edited_channel_post=None, inline_query=None, chosen_inline_result=None, callback_query=None, shipping_query=None, pre_checkout_query=None, poll=None, poll_answer=None, _raw=None):
        """
        This object represents an incoming update.At most one of the optional parameters can be present in any given update.

        https://core.telegram.org/bots/api#update


        Parameters:

        :param update_id: The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
        :type  update_id: int


        Optional keyword parameters:

        :param message: Optional. New incoming message of any kind — text, photo, sticker, etc.
        :type  message: pytgbot.api_types.receivable.updates.Message

        :param edited_message: Optional. New version of a message that is known to the bot and was edited
        :type  edited_message: pytgbot.api_types.receivable.updates.Message

        :param channel_post: Optional. New incoming channel post of any kind — text, photo, sticker, etc.
        :type  channel_post: pytgbot.api_types.receivable.updates.Message

        :param edited_channel_post: Optional. New version of a channel post that is known to the bot and was edited
        :type  edited_channel_post: pytgbot.api_types.receivable.updates.Message

        :param inline_query: Optional. New incoming inline query
        :type  inline_query: pytgbot.api_types.receivable.inline.InlineQuery

        :param chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.
        :type  chosen_inline_result: pytgbot.api_types.receivable.inline.ChosenInlineResult

        :param callback_query: Optional. New incoming callback query
        :type  callback_query: pytgbot.api_types.receivable.updates.CallbackQuery

        :param shipping_query: Optional. New incoming shipping query. Only for invoices with flexible price
        :type  shipping_query: pytgbot.api_types.receivable.payments.ShippingQuery

        :param pre_checkout_query: Optional. New incoming pre-checkout query. Contains full information about checkout
        :type  pre_checkout_query: pytgbot.api_types.receivable.payments.PreCheckoutQuery

        :param poll: Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
        :type  poll: pytgbot.api_types.receivable.media.Poll

        :param poll_answer: Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
        :type  poll_answer: pytgbot.api_types.receivable.media.PollAnswer

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Update, self).__init__()
        from .inline import ChosenInlineResult
        from .inline import InlineQuery
        from .media import Poll
        from .media import PollAnswer
        from .payments import PreCheckoutQuery
        from .payments import ShippingQuery

        assert_type_or_raise(update_id, int, parameter_name="update_id")
        self.update_id = update_id
        assert_type_or_raise(message, None, Message, parameter_name="message")
        self.message = message
        assert_type_or_raise(edited_message, None, Message, parameter_name="edited_message")
        self.edited_message = edited_message
        assert_type_or_raise(channel_post, None, Message, parameter_name="channel_post")
        self.channel_post = channel_post
        assert_type_or_raise(edited_channel_post, None, Message, parameter_name="edited_channel_post")
        self.edited_channel_post = edited_channel_post
        assert_type_or_raise(inline_query, None, InlineQuery, parameter_name="inline_query")
        self.inline_query = inline_query
        assert_type_or_raise(chosen_inline_result, None, ChosenInlineResult, parameter_name="chosen_inline_result")
        self.chosen_inline_result = chosen_inline_result
        assert_type_or_raise(callback_query, None, CallbackQuery, parameter_name="callback_query")
        self.callback_query = callback_query
        assert_type_or_raise(shipping_query, None, ShippingQuery, parameter_name="shipping_query")
        self.shipping_query = shipping_query
        assert_type_or_raise(pre_checkout_query, None, PreCheckoutQuery, parameter_name="pre_checkout_query")
        self.pre_checkout_query = pre_checkout_query
        assert_type_or_raise(poll, None, Poll, parameter_name="poll")
        self.poll = poll
        assert_type_or_raise(poll_answer, None, PollAnswer, parameter_name="poll_answer")
        self.poll_answer = poll_answer

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Update to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Update, self).to_array()

        array['update_id'] = int(self.update_id)  # type int
        if self.message is not None:
            array['message'] = self.message.to_array()  # type Message
        # end if
        if self.edited_message is not None:
            array['edited_message'] = self.edited_message.to_array()  # type Message
        # end if
        if self.channel_post is not None:
            array['channel_post'] = self.channel_post.to_array()  # type Message
        # end if
        if self.edited_channel_post is not None:
            array['edited_channel_post'] = self.edited_channel_post.to_array()  # type Message
        # end if
        if self.inline_query is not None:
            array['inline_query'] = self.inline_query.to_array()  # type InlineQuery
        # end if
        if self.chosen_inline_result is not None:
            array['chosen_inline_result'] = self.chosen_inline_result.to_array()  # type ChosenInlineResult
        # end if
        if self.callback_query is not None:
            array['callback_query'] = self.callback_query.to_array()  # type CallbackQuery
        # end if
        if self.shipping_query is not None:
            array['shipping_query'] = self.shipping_query.to_array()  # type ShippingQuery
        # end if
        if self.pre_checkout_query is not None:
            array['pre_checkout_query'] = self.pre_checkout_query.to_array()  # type PreCheckoutQuery
        # end if
        if self.poll is not None:
            array['poll'] = self.poll.to_array()  # type Poll
        # end if
        if self.poll_answer is not None:
            array['poll_answer'] = self.poll_answer.to_array()  # type PollAnswer
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Update constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .inline import ChosenInlineResult
        from .inline import InlineQuery
        from .media import Poll
        from .media import PollAnswer
        from .payments import PreCheckoutQuery
        from .payments import ShippingQuery

        data = Receivable.validate_array(array)
        data['update_id'] = int(array.get('update_id'))
        data['message'] = Message.from_array(array.get('message')) if array.get('message') is not None else None
        data['edited_message'] = Message.from_array(array.get('edited_message')) if array.get('edited_message') is not None else None
        data['channel_post'] = Message.from_array(array.get('channel_post')) if array.get('channel_post') is not None else None
        data['edited_channel_post'] = Message.from_array(array.get('edited_channel_post')) if array.get('edited_channel_post') is not None else None
        data['inline_query'] = InlineQuery.from_array(array.get('inline_query')) if array.get('inline_query') is not None else None
        data['chosen_inline_result'] = ChosenInlineResult.from_array(array.get('chosen_inline_result')) if array.get('chosen_inline_result') is not None else None
        data['callback_query'] = CallbackQuery.from_array(array.get('callback_query')) if array.get('callback_query') is not None else None
        data['shipping_query'] = ShippingQuery.from_array(array.get('shipping_query')) if array.get('shipping_query') is not None else None
        data['pre_checkout_query'] = PreCheckoutQuery.from_array(array.get('pre_checkout_query')) if array.get('pre_checkout_query') is not None else None
        data['poll'] = Poll.from_array(array.get('poll')) if array.get('poll') is not None else None
        data['poll_answer'] = PollAnswer.from_array(array.get('poll_answer')) if array.get('poll_answer') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Update from a given dictionary.

        :return: new Update instance.
        :rtype: Update
        """
        if not array:  # None or {}
            return None
        # end if

        data = Update.validate_array(array)
        data['_raw'] = array
        return Update(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(update_instance)`
        """
        return "Update(update_id={self.update_id!r}, message={self.message!r}, edited_message={self.edited_message!r}, channel_post={self.channel_post!r}, edited_channel_post={self.edited_channel_post!r}, inline_query={self.inline_query!r}, chosen_inline_result={self.chosen_inline_result!r}, callback_query={self.callback_query!r}, shipping_query={self.shipping_query!r}, pre_checkout_query={self.pre_checkout_query!r}, poll={self.poll!r}, poll_answer={self.poll_answer!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(update_instance)`
        """
        if self._raw:
            return "Update.from_array({self._raw})".format(self=self)
        # end if
        return "Update(update_id={self.update_id!r}, message={self.message!r}, edited_message={self.edited_message!r}, channel_post={self.channel_post!r}, edited_channel_post={self.edited_channel_post!r}, inline_query={self.inline_query!r}, chosen_inline_result={self.chosen_inline_result!r}, callback_query={self.callback_query!r}, shipping_query={self.shipping_query!r}, pre_checkout_query={self.pre_checkout_query!r}, poll={self.poll!r}, poll_answer={self.poll_answer!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in update_instance`
        """
        return (
            key in ["update_id", "message", "edited_message", "channel_post", "edited_channel_post", "inline_query", "chosen_inline_result", "callback_query", "shipping_query", "pre_checkout_query", "poll", "poll_answer"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Update


class WebhookInfo(Receivable):
    """
    Contains information about the current status of a webhook.

    https://core.telegram.org/bots/api#webhookinfo


    Parameters:

    :param url: Webhook URL, may be empty if webhook is not set up
    :type  url: str|unicode

    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    :type  has_custom_certificate: bool

    :param pending_update_count: Number of updates awaiting delivery
    :type  pending_update_count: int


    Optional keyword parameters:

    :param ip_address: Optional. Currently used webhook IP address
    :type  ip_address: str|unicode

    :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
    :type  last_error_date: int

    :param last_error_message: Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    :type  last_error_message: str|unicode

    :param max_connections: Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    :type  max_connections: int

    :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update types
    :type  allowed_updates: list of str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, url, has_custom_certificate, pending_update_count, ip_address=None, last_error_date=None, last_error_message=None, max_connections=None, allowed_updates=None, _raw=None):
        """
        Contains information about the current status of a webhook.

        https://core.telegram.org/bots/api#webhookinfo


        Parameters:

        :param url: Webhook URL, may be empty if webhook is not set up
        :type  url: str|unicode

        :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
        :type  has_custom_certificate: bool

        :param pending_update_count: Number of updates awaiting delivery
        :type  pending_update_count: int


        Optional keyword parameters:

        :param ip_address: Optional. Currently used webhook IP address
        :type  ip_address: str|unicode

        :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver an update via webhook
        :type  last_error_date: int

        :param last_error_message: Optional. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
        :type  last_error_message: str|unicode

        :param max_connections: Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
        :type  max_connections: int

        :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update types
        :type  allowed_updates: list of str|unicode

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(WebhookInfo, self).__init__()
        assert_type_or_raise(url, unicode_type, parameter_name="url")
        self.url = url
        assert_type_or_raise(has_custom_certificate, bool, parameter_name="has_custom_certificate")
        self.has_custom_certificate = has_custom_certificate
        assert_type_or_raise(pending_update_count, int, parameter_name="pending_update_count")
        self.pending_update_count = pending_update_count
        assert_type_or_raise(ip_address, None, unicode_type, parameter_name="ip_address")
        self.ip_address = ip_address
        assert_type_or_raise(last_error_date, None, int, parameter_name="last_error_date")
        self.last_error_date = last_error_date
        assert_type_or_raise(last_error_message, None, unicode_type, parameter_name="last_error_message")
        self.last_error_message = last_error_message
        assert_type_or_raise(max_connections, None, int, parameter_name="max_connections")
        self.max_connections = max_connections
        assert_type_or_raise(allowed_updates, None, list, parameter_name="allowed_updates")
        self.allowed_updates = allowed_updates

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this WebhookInfo to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(WebhookInfo, self).to_array()

        array['url'] = u(self.url)  # py2: type unicode, py3: type str
        array['has_custom_certificate'] = bool(self.has_custom_certificate)  # type bool
        array['pending_update_count'] = int(self.pending_update_count)  # type int
        if self.ip_address is not None:
            array['ip_address'] = u(self.ip_address)  # py2: type unicode, py3: type str
        # end if
        if self.last_error_date is not None:
            array['last_error_date'] = int(self.last_error_date)  # type int
        # end if
        if self.last_error_message is not None:
            array['last_error_message'] = u(self.last_error_message)  # py2: type unicode, py3: type str
        # end if
        if self.max_connections is not None:
            array['max_connections'] = int(self.max_connections)  # type int
        # end if
        if self.allowed_updates is not None:
            array['allowed_updates'] = self._as_array(self.allowed_updates)  # type list of str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the WebhookInfo constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Receivable.validate_array(array)
        data['url'] = u(array.get('url'))
        data['has_custom_certificate'] = bool(array.get('has_custom_certificate'))
        data['pending_update_count'] = int(array.get('pending_update_count'))
        data['ip_address'] = u(array.get('ip_address')) if array.get('ip_address') is not None else None
        data['last_error_date'] = int(array.get('last_error_date')) if array.get('last_error_date') is not None else None
        data['last_error_message'] = u(array.get('last_error_message')) if array.get('last_error_message') is not None else None
        data['max_connections'] = int(array.get('max_connections')) if array.get('max_connections') is not None else None
        data['allowed_updates'] = WebhookInfo._builtin_from_array_list(required_type=unicode_type, value=array.get('allowed_updates'), list_level=1) if array.get('allowed_updates') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new WebhookInfo from a given dictionary.

        :return: new WebhookInfo instance.
        :rtype: WebhookInfo
        """
        if not array:  # None or {}
            return None
        # end if

        data = WebhookInfo.validate_array(array)
        data['_raw'] = array
        return WebhookInfo(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(webhookinfo_instance)`
        """
        return "WebhookInfo(url={self.url!r}, has_custom_certificate={self.has_custom_certificate!r}, pending_update_count={self.pending_update_count!r}, ip_address={self.ip_address!r}, last_error_date={self.last_error_date!r}, last_error_message={self.last_error_message!r}, max_connections={self.max_connections!r}, allowed_updates={self.allowed_updates!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(webhookinfo_instance)`
        """
        if self._raw:
            return "WebhookInfo.from_array({self._raw})".format(self=self)
        # end if
        return "WebhookInfo(url={self.url!r}, has_custom_certificate={self.has_custom_certificate!r}, pending_update_count={self.pending_update_count!r}, ip_address={self.ip_address!r}, last_error_date={self.last_error_date!r}, last_error_message={self.last_error_message!r}, max_connections={self.max_connections!r}, allowed_updates={self.allowed_updates!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in webhookinfo_instance`
        """
        return (
            key in ["url", "has_custom_certificate", "pending_update_count", "ip_address", "last_error_date", "last_error_message", "max_connections", "allowed_updates"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class WebhookInfo


class Message(UpdateType):
    """
    This object represents a message.

    https://core.telegram.org/bots/api#message


    Parameters:

    :param message_id: Unique message identifier inside this chat
    :type  message_id: int

    :param date: Date the message was sent in Unix time
    :type  date: int

    :param chat: Conversation the message belongs to
    :type  chat: pytgbot.api_types.receivable.peer.Chat


    Optional keyword parameters:

    :param from_peer: Optional. Sender, empty for messages sent to channels
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group
    :type  sender_chat: pytgbot.api_types.receivable.peer.Chat

    :param forward_from: Optional. For forwarded messages, sender of the original message
    :type  forward_from: pytgbot.api_types.receivable.peer.User

    :param forward_from_chat: Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
    :type  forward_from_chat: pytgbot.api_types.receivable.peer.Chat

    :param forward_from_message_id: Optional. For messages forwarded from channels, identifier of the original message in the channel
    :type  forward_from_message_id: int

    :param forward_signature: Optional. For messages forwarded from channels, signature of the post author if present
    :type  forward_signature: str|unicode

    :param forward_sender_name: Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    :type  forward_sender_name: str|unicode

    :param forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
    :type  forward_date: int

    :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    :type  reply_to_message: pytgbot.api_types.receivable.updates.Message

    :param via_bot: Optional. Bot through which the message was sent
    :type  via_bot: pytgbot.api_types.receivable.peer.User

    :param edit_date: Optional. Date the message was last edited in Unix time
    :type  edit_date: int

    :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
    :type  media_group_id: str|unicode

    :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
    :type  author_signature: str|unicode

    :param text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    :type  text: str|unicode

    :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    :type  entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param animation: Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
    :type  animation: pytgbot.api_types.receivable.media.Animation

    :param audio: Optional. Message is an audio file, information about the file
    :type  audio: pytgbot.api_types.receivable.media.Audio

    :param document: Optional. Message is a general file, information about the file
    :type  document: pytgbot.api_types.receivable.media.Document

    :param photo: Optional. Message is a photo, available sizes of the photo
    :type  photo: list of pytgbot.api_types.receivable.media.PhotoSize

    :param sticker: Optional. Message is a sticker, information about the sticker
    :type  sticker: pytgbot.api_types.receivable.media.Sticker

    :param video: Optional. Message is a video, information about the video
    :type  video: pytgbot.api_types.receivable.media.Video

    :param video_note: Optional. Message is a video note, information about the video message
    :type  video_note: pytgbot.api_types.receivable.media.VideoNote

    :param voice: Optional. Message is a voice message, information about the file
    :type  voice: pytgbot.api_types.receivable.media.Voice

    :param caption: Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    :type  caption: str|unicode

    :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

    :param contact: Optional. Message is a shared contact, information about the contact
    :type  contact: pytgbot.api_types.receivable.media.Contact

    :param dice: Optional. Message is a dice with random value from 1 to 6
    :type  dice: pytgbot.api_types.receivable.media.Dice

    :param game: Optional. Message is a game, information about the game. More about games »
    :type  game: pytgbot.api_types.receivable.media.Game

    :param poll: Optional. Message is a native poll, information about the poll
    :type  poll: pytgbot.api_types.receivable.media.Poll

    :param venue: Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    :type  venue: pytgbot.api_types.receivable.media.Venue

    :param location: Optional. Message is a shared location, information about the location
    :type  location: pytgbot.api_types.receivable.media.Location

    :param new_chat_members: Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    :type  new_chat_members: list of pytgbot.api_types.receivable.peer.User

    :param left_chat_member: Optional. A member was removed from the group, information about them (this member may be the bot itself)
    :type  left_chat_member: pytgbot.api_types.receivable.peer.User

    :param new_chat_title: Optional. A chat title was changed to this value
    :type  new_chat_title: str|unicode

    :param new_chat_photo: Optional. A chat photo was change to this value
    :type  new_chat_photo: list of pytgbot.api_types.receivable.media.PhotoSize

    :param delete_chat_photo: Optional. Service message: the chat photo was deleted
    :type  delete_chat_photo: bool

    :param group_chat_created: Optional. Service message: the group has been created
    :type  group_chat_created: bool

    :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    :type  supergroup_chat_created: bool

    :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    :type  channel_chat_created: bool

    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  migrate_to_chat_id: int

    :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  migrate_from_chat_id: int

    :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
    :type  pinned_message: pytgbot.api_types.receivable.updates.Message

    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
    :type  invoice: pytgbot.api_types.receivable.payments.Invoice

    :param successful_payment: Optional. Message is a service message about a successful payment, information about the payment. More about payments »
    :type  successful_payment: pytgbot.api_types.receivable.payments.SuccessfulPayment

    :param connected_website: Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
    :type  connected_website: str|unicode

    :param passport_data: Optional. Telegram Passport data
    :type  passport_data: pytgbot.api_types.receivable.passport.PassportData

    :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    :type  proximity_alert_triggered: pytgbot.api_types.receivable.media.ProximityAlertTriggered

    :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, message_id, date, chat, from_peer=None, sender_chat=None, forward_from=None, forward_from_chat=None, forward_from_message_id=None, forward_signature=None, forward_sender_name=None, forward_date=None, reply_to_message=None, via_bot=None, edit_date=None, media_group_id=None, author_signature=None, text=None, entities=None, animation=None, audio=None, document=None, photo=None, sticker=None, video=None, video_note=None, voice=None, caption=None, caption_entities=None, contact=None, dice=None, game=None, poll=None, venue=None, location=None, new_chat_members=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None, migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None, connected_website=None, passport_data=None, proximity_alert_triggered=None, reply_markup=None, _raw=None):
        """
        This object represents a message.

        https://core.telegram.org/bots/api#message


        Parameters:

        :param message_id: Unique message identifier inside this chat
        :type  message_id: int

        :param date: Date the message was sent in Unix time
        :type  date: int

        :param chat: Conversation the message belongs to
        :type  chat: pytgbot.api_types.receivable.peer.Chat


        Optional keyword parameters:

        :param from_peer: Optional. Sender, empty for messages sent to channels
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group
        :type  sender_chat: pytgbot.api_types.receivable.peer.Chat

        :param forward_from: Optional. For forwarded messages, sender of the original message
        :type  forward_from: pytgbot.api_types.receivable.peer.User

        :param forward_from_chat: Optional. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
        :type  forward_from_chat: pytgbot.api_types.receivable.peer.Chat

        :param forward_from_message_id: Optional. For messages forwarded from channels, identifier of the original message in the channel
        :type  forward_from_message_id: int

        :param forward_signature: Optional. For messages forwarded from channels, signature of the post author if present
        :type  forward_signature: str|unicode

        :param forward_sender_name: Optional. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
        :type  forward_sender_name: str|unicode

        :param forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
        :type  forward_date: int

        :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        :type  reply_to_message: pytgbot.api_types.receivable.updates.Message

        :param via_bot: Optional. Bot through which the message was sent
        :type  via_bot: pytgbot.api_types.receivable.peer.User

        :param edit_date: Optional. Date the message was last edited in Unix time
        :type  edit_date: int

        :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
        :type  media_group_id: str|unicode

        :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
        :type  author_signature: str|unicode

        :param text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
        :type  text: str|unicode

        :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
        :type  entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :param animation: Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set
        :type  animation: pytgbot.api_types.receivable.media.Animation

        :param audio: Optional. Message is an audio file, information about the file
        :type  audio: pytgbot.api_types.receivable.media.Audio

        :param document: Optional. Message is a general file, information about the file
        :type  document: pytgbot.api_types.receivable.media.Document

        :param photo: Optional. Message is a photo, available sizes of the photo
        :type  photo: list of pytgbot.api_types.receivable.media.PhotoSize

        :param sticker: Optional. Message is a sticker, information about the sticker
        :type  sticker: pytgbot.api_types.receivable.media.Sticker

        :param video: Optional. Message is a video, information about the video
        :type  video: pytgbot.api_types.receivable.media.Video

        :param video_note: Optional. Message is a video note, information about the video message
        :type  video_note: pytgbot.api_types.receivable.media.VideoNote

        :param voice: Optional. Message is a voice message, information about the file
        :type  voice: pytgbot.api_types.receivable.media.Voice

        :param caption: Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
        :type  caption: str|unicode

        :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
        :type  caption_entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :param contact: Optional. Message is a shared contact, information about the contact
        :type  contact: pytgbot.api_types.receivable.media.Contact

        :param dice: Optional. Message is a dice with random value from 1 to 6
        :type  dice: pytgbot.api_types.receivable.media.Dice

        :param game: Optional. Message is a game, information about the game. More about games »
        :type  game: pytgbot.api_types.receivable.media.Game

        :param poll: Optional. Message is a native poll, information about the poll
        :type  poll: pytgbot.api_types.receivable.media.Poll

        :param venue: Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
        :type  venue: pytgbot.api_types.receivable.media.Venue

        :param location: Optional. Message is a shared location, information about the location
        :type  location: pytgbot.api_types.receivable.media.Location

        :param new_chat_members: Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
        :type  new_chat_members: list of pytgbot.api_types.receivable.peer.User

        :param left_chat_member: Optional. A member was removed from the group, information about them (this member may be the bot itself)
        :type  left_chat_member: pytgbot.api_types.receivable.peer.User

        :param new_chat_title: Optional. A chat title was changed to this value
        :type  new_chat_title: str|unicode

        :param new_chat_photo: Optional. A chat photo was change to this value
        :type  new_chat_photo: list of pytgbot.api_types.receivable.media.PhotoSize

        :param delete_chat_photo: Optional. Service message: the chat photo was deleted
        :type  delete_chat_photo: bool

        :param group_chat_created: Optional. Service message: the group has been created
        :type  group_chat_created: bool

        :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
        :type  supergroup_chat_created: bool

        :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
        :type  channel_chat_created: bool

        :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type  migrate_to_chat_id: int

        :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type  migrate_from_chat_id: int

        :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
        :type  pinned_message: pytgbot.api_types.receivable.updates.Message

        :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More about payments »
        :type  invoice: pytgbot.api_types.receivable.payments.Invoice

        :param successful_payment: Optional. Message is a service message about a successful payment, information about the payment. More about payments »
        :type  successful_payment: pytgbot.api_types.receivable.payments.SuccessfulPayment

        :param connected_website: Optional. The domain name of the website on which the user has logged in. More about Telegram Login »
        :type  connected_website: str|unicode

        :param passport_data: Optional. Telegram Passport data
        :type  passport_data: pytgbot.api_types.receivable.passport.PassportData

        :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
        :type  proximity_alert_triggered: pytgbot.api_types.receivable.media.ProximityAlertTriggered

        :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
        :type  reply_markup: pytgbot.api_types.sendable.reply_markup.InlineKeyboardMarkup

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(Message, self).__init__()
        from .media import Animation
        from .media import Audio
        from .media import Contact
        from .media import Dice
        from .media import Document
        from .media import Game
        from .media import Location
        from .media import MessageEntity
        from .media import PhotoSize
        from .media import Poll
        from .media import ProximityAlertTriggered
        from .media import Sticker
        from .media import Venue
        from .media import Video
        from .media import VideoNote
        from .media import Voice
        from .passport import PassportData
        from .payments import Invoice
        from .payments import SuccessfulPayment
        from .peer import Chat
        from .peer import User
        from ..sendable.reply_markup import InlineKeyboardMarkup

        assert_type_or_raise(message_id, int, parameter_name="message_id")
        self.message_id = message_id
        assert_type_or_raise(date, int, parameter_name="date")
        self.date = date
        assert_type_or_raise(chat, Chat, parameter_name="chat")
        self.chat = chat
        assert_type_or_raise(from_peer, None, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(sender_chat, None, Chat, parameter_name="sender_chat")
        self.sender_chat = sender_chat
        assert_type_or_raise(forward_from, None, User, parameter_name="forward_from")
        self.forward_from = forward_from
        assert_type_or_raise(forward_from_chat, None, Chat, parameter_name="forward_from_chat")
        self.forward_from_chat = forward_from_chat
        assert_type_or_raise(forward_from_message_id, None, int, parameter_name="forward_from_message_id")
        self.forward_from_message_id = forward_from_message_id
        assert_type_or_raise(forward_signature, None, unicode_type, parameter_name="forward_signature")
        self.forward_signature = forward_signature
        assert_type_or_raise(forward_sender_name, None, unicode_type, parameter_name="forward_sender_name")
        self.forward_sender_name = forward_sender_name
        assert_type_or_raise(forward_date, None, int, parameter_name="forward_date")
        self.forward_date = forward_date
        assert_type_or_raise(reply_to_message, None, Message, parameter_name="reply_to_message")
        self.reply_to_message = reply_to_message
        assert_type_or_raise(via_bot, None, User, parameter_name="via_bot")
        self.via_bot = via_bot
        assert_type_or_raise(edit_date, None, int, parameter_name="edit_date")
        self.edit_date = edit_date
        assert_type_or_raise(media_group_id, None, unicode_type, parameter_name="media_group_id")
        self.media_group_id = media_group_id
        assert_type_or_raise(author_signature, None, unicode_type, parameter_name="author_signature")
        self.author_signature = author_signature
        assert_type_or_raise(text, None, unicode_type, parameter_name="text")
        self.text = text
        assert_type_or_raise(entities, None, list, parameter_name="entities")
        self.entities = entities
        assert_type_or_raise(animation, None, Animation, parameter_name="animation")
        self.animation = animation
        assert_type_or_raise(audio, None, Audio, parameter_name="audio")
        self.audio = audio
        assert_type_or_raise(document, None, Document, parameter_name="document")
        self.document = document
        assert_type_or_raise(photo, None, list, parameter_name="photo")
        self.photo = photo
        assert_type_or_raise(sticker, None, Sticker, parameter_name="sticker")
        self.sticker = sticker
        assert_type_or_raise(video, None, Video, parameter_name="video")
        self.video = video
        assert_type_or_raise(video_note, None, VideoNote, parameter_name="video_note")
        self.video_note = video_note
        assert_type_or_raise(voice, None, Voice, parameter_name="voice")
        self.voice = voice
        assert_type_or_raise(caption, None, unicode_type, parameter_name="caption")
        self.caption = caption
        assert_type_or_raise(caption_entities, None, list, parameter_name="caption_entities")
        self.caption_entities = caption_entities
        assert_type_or_raise(contact, None, Contact, parameter_name="contact")
        self.contact = contact
        assert_type_or_raise(dice, None, Dice, parameter_name="dice")
        self.dice = dice
        assert_type_or_raise(game, None, Game, parameter_name="game")
        self.game = game
        assert_type_or_raise(poll, None, Poll, parameter_name="poll")
        self.poll = poll
        assert_type_or_raise(venue, None, Venue, parameter_name="venue")
        self.venue = venue
        assert_type_or_raise(location, None, Location, parameter_name="location")
        self.location = location
        assert_type_or_raise(new_chat_members, None, list, parameter_name="new_chat_members")
        self.new_chat_members = new_chat_members
        assert_type_or_raise(left_chat_member, None, User, parameter_name="left_chat_member")
        self.left_chat_member = left_chat_member
        assert_type_or_raise(new_chat_title, None, unicode_type, parameter_name="new_chat_title")
        self.new_chat_title = new_chat_title
        assert_type_or_raise(new_chat_photo, None, list, parameter_name="new_chat_photo")
        self.new_chat_photo = new_chat_photo
        assert_type_or_raise(delete_chat_photo, None, bool, parameter_name="delete_chat_photo")
        self.delete_chat_photo = delete_chat_photo
        assert_type_or_raise(group_chat_created, None, bool, parameter_name="group_chat_created")
        self.group_chat_created = group_chat_created
        assert_type_or_raise(supergroup_chat_created, None, bool, parameter_name="supergroup_chat_created")
        self.supergroup_chat_created = supergroup_chat_created
        assert_type_or_raise(channel_chat_created, None, bool, parameter_name="channel_chat_created")
        self.channel_chat_created = channel_chat_created
        assert_type_or_raise(migrate_to_chat_id, None, int, parameter_name="migrate_to_chat_id")
        self.migrate_to_chat_id = migrate_to_chat_id
        assert_type_or_raise(migrate_from_chat_id, None, int, parameter_name="migrate_from_chat_id")
        self.migrate_from_chat_id = migrate_from_chat_id
        assert_type_or_raise(pinned_message, None, Message, parameter_name="pinned_message")
        self.pinned_message = pinned_message
        assert_type_or_raise(invoice, None, Invoice, parameter_name="invoice")
        self.invoice = invoice
        assert_type_or_raise(successful_payment, None, SuccessfulPayment, parameter_name="successful_payment")
        self.successful_payment = successful_payment
        assert_type_or_raise(connected_website, None, unicode_type, parameter_name="connected_website")
        self.connected_website = connected_website
        assert_type_or_raise(passport_data, None, PassportData, parameter_name="passport_data")
        self.passport_data = passport_data
        assert_type_or_raise(proximity_alert_triggered, None, ProximityAlertTriggered, parameter_name="proximity_alert_triggered")
        self.proximity_alert_triggered = proximity_alert_triggered
        assert_type_or_raise(reply_markup, None, InlineKeyboardMarkup, parameter_name="reply_markup")
        self.reply_markup = reply_markup

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this Message to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(Message, self).to_array()

        array['message_id'] = int(self.message_id)  # type int
        array['date'] = int(self.date)  # type int
        array['chat'] = self.chat.to_array()  # type Chat
        if self.from_peer is not None:
            array['from'] = self.from_peer.to_array()  # type User
        # end if
        if self.sender_chat is not None:
            array['sender_chat'] = self.sender_chat.to_array()  # type Chat
        # end if
        if self.forward_from is not None:
            array['forward_from'] = self.forward_from.to_array()  # type User
        # end if
        if self.forward_from_chat is not None:
            array['forward_from_chat'] = self.forward_from_chat.to_array()  # type Chat
        # end if
        if self.forward_from_message_id is not None:
            array['forward_from_message_id'] = int(self.forward_from_message_id)  # type int
        # end if
        if self.forward_signature is not None:
            array['forward_signature'] = u(self.forward_signature)  # py2: type unicode, py3: type str
        # end if
        if self.forward_sender_name is not None:
            array['forward_sender_name'] = u(self.forward_sender_name)  # py2: type unicode, py3: type str
        # end if
        if self.forward_date is not None:
            array['forward_date'] = int(self.forward_date)  # type int
        # end if
        if self.reply_to_message is not None:
            array['reply_to_message'] = self.reply_to_message.to_array()  # type Message
        # end if
        if self.via_bot is not None:
            array['via_bot'] = self.via_bot.to_array()  # type User
        # end if
        if self.edit_date is not None:
            array['edit_date'] = int(self.edit_date)  # type int
        # end if
        if self.media_group_id is not None:
            array['media_group_id'] = u(self.media_group_id)  # py2: type unicode, py3: type str
        # end if
        if self.author_signature is not None:
            array['author_signature'] = u(self.author_signature)  # py2: type unicode, py3: type str
        # end if
        if self.text is not None:
            array['text'] = u(self.text)  # py2: type unicode, py3: type str
        # end if
        if self.entities is not None:
            array['entities'] = self._as_array(self.entities)  # type list of MessageEntity
        # end if
        if self.animation is not None:
            array['animation'] = self.animation.to_array()  # type Animation
        # end if
        if self.audio is not None:
            array['audio'] = self.audio.to_array()  # type Audio
        # end if
        if self.document is not None:
            array['document'] = self.document.to_array()  # type Document
        # end if
        if self.photo is not None:
            array['photo'] = self._as_array(self.photo)  # type list of PhotoSize
        # end if
        if self.sticker is not None:
            array['sticker'] = self.sticker.to_array()  # type Sticker
        # end if
        if self.video is not None:
            array['video'] = self.video.to_array()  # type Video
        # end if
        if self.video_note is not None:
            array['video_note'] = self.video_note.to_array()  # type VideoNote
        # end if
        if self.voice is not None:
            array['voice'] = self.voice.to_array()  # type Voice
        # end if
        if self.caption is not None:
            array['caption'] = u(self.caption)  # py2: type unicode, py3: type str
        # end if
        if self.caption_entities is not None:
            array['caption_entities'] = self._as_array(self.caption_entities)  # type list of MessageEntity
        # end if
        if self.contact is not None:
            array['contact'] = self.contact.to_array()  # type Contact
        # end if
        if self.dice is not None:
            array['dice'] = self.dice.to_array()  # type Dice
        # end if
        if self.game is not None:
            array['game'] = self.game.to_array()  # type Game
        # end if
        if self.poll is not None:
            array['poll'] = self.poll.to_array()  # type Poll
        # end if
        if self.venue is not None:
            array['venue'] = self.venue.to_array()  # type Venue
        # end if
        if self.location is not None:
            array['location'] = self.location.to_array()  # type Location
        # end if
        if self.new_chat_members is not None:
            array['new_chat_members'] = self._as_array(self.new_chat_members)  # type list of User
        # end if
        if self.left_chat_member is not None:
            array['left_chat_member'] = self.left_chat_member.to_array()  # type User
        # end if
        if self.new_chat_title is not None:
            array['new_chat_title'] = u(self.new_chat_title)  # py2: type unicode, py3: type str
        # end if
        if self.new_chat_photo is not None:
            array['new_chat_photo'] = self._as_array(self.new_chat_photo)  # type list of PhotoSize
        # end if
        if self.delete_chat_photo is not None:
            array['delete_chat_photo'] = bool(self.delete_chat_photo)  # type bool
        # end if
        if self.group_chat_created is not None:
            array['group_chat_created'] = bool(self.group_chat_created)  # type bool
        # end if
        if self.supergroup_chat_created is not None:
            array['supergroup_chat_created'] = bool(self.supergroup_chat_created)  # type bool
        # end if
        if self.channel_chat_created is not None:
            array['channel_chat_created'] = bool(self.channel_chat_created)  # type bool
        # end if
        if self.migrate_to_chat_id is not None:
            array['migrate_to_chat_id'] = int(self.migrate_to_chat_id)  # type int
        # end if
        if self.migrate_from_chat_id is not None:
            array['migrate_from_chat_id'] = int(self.migrate_from_chat_id)  # type int
        # end if
        if self.pinned_message is not None:
            array['pinned_message'] = self.pinned_message.to_array()  # type Message
        # end if
        if self.invoice is not None:
            array['invoice'] = self.invoice.to_array()  # type Invoice
        # end if
        if self.successful_payment is not None:
            array['successful_payment'] = self.successful_payment.to_array()  # type SuccessfulPayment
        # end if
        if self.connected_website is not None:
            array['connected_website'] = u(self.connected_website)  # py2: type unicode, py3: type str
        # end if
        if self.passport_data is not None:
            array['passport_data'] = self.passport_data.to_array()  # type PassportData
        # end if
        if self.proximity_alert_triggered is not None:
            array['proximity_alert_triggered'] = self.proximity_alert_triggered.to_array()  # type ProximityAlertTriggered
        # end if
        if self.reply_markup is not None:
            array['reply_markup'] = self.reply_markup.to_array()  # type InlineKeyboardMarkup
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the Message constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .media import Animation
        from .media import Audio
        from .media import Contact
        from .media import Dice
        from .media import Document
        from .media import Game
        from .media import Location
        from .media import MessageEntity
        from .media import PhotoSize
        from .media import Poll
        from .media import ProximityAlertTriggered
        from .media import Sticker
        from .media import Venue
        from .media import Video
        from .media import VideoNote
        from .media import Voice
        from .passport import PassportData
        from .payments import Invoice
        from .payments import SuccessfulPayment
        from .peer import Chat
        from .peer import User
        from ..sendable.reply_markup import InlineKeyboardMarkup

        data = UpdateType.validate_array(array)
        data['message_id'] = int(array.get('message_id'))
        data['date'] = int(array.get('date'))
        data['chat'] = Chat.from_array(array.get('chat'))
        data['from_peer'] = User.from_array(array.get('from')) if array.get('from') is not None else None
        data['sender_chat'] = Chat.from_array(array.get('sender_chat')) if array.get('sender_chat') is not None else None
        data['forward_from'] = User.from_array(array.get('forward_from')) if array.get('forward_from') is not None else None
        data['forward_from_chat'] = Chat.from_array(array.get('forward_from_chat')) if array.get('forward_from_chat') is not None else None
        data['forward_from_message_id'] = int(array.get('forward_from_message_id')) if array.get('forward_from_message_id') is not None else None
        data['forward_signature'] = u(array.get('forward_signature')) if array.get('forward_signature') is not None else None
        data['forward_sender_name'] = u(array.get('forward_sender_name')) if array.get('forward_sender_name') is not None else None
        data['forward_date'] = int(array.get('forward_date')) if array.get('forward_date') is not None else None
        data['reply_to_message'] = Message.from_array(array.get('reply_to_message')) if array.get('reply_to_message') is not None else None
        data['via_bot'] = User.from_array(array.get('via_bot')) if array.get('via_bot') is not None else None
        data['edit_date'] = int(array.get('edit_date')) if array.get('edit_date') is not None else None
        data['media_group_id'] = u(array.get('media_group_id')) if array.get('media_group_id') is not None else None
        data['author_signature'] = u(array.get('author_signature')) if array.get('author_signature') is not None else None
        data['text'] = u(array.get('text')) if array.get('text') is not None else None
        data['entities'] = MessageEntity.from_array_list(array.get('entities'), list_level=1) if array.get('entities') is not None else None
        data['animation'] = Animation.from_array(array.get('animation')) if array.get('animation') is not None else None
        data['audio'] = Audio.from_array(array.get('audio')) if array.get('audio') is not None else None
        data['document'] = Document.from_array(array.get('document')) if array.get('document') is not None else None
        data['photo'] = PhotoSize.from_array_list(array.get('photo'), list_level=1) if array.get('photo') is not None else None
        data['sticker'] = Sticker.from_array(array.get('sticker')) if array.get('sticker') is not None else None
        data['video'] = Video.from_array(array.get('video')) if array.get('video') is not None else None
        data['video_note'] = VideoNote.from_array(array.get('video_note')) if array.get('video_note') is not None else None
        data['voice'] = Voice.from_array(array.get('voice')) if array.get('voice') is not None else None
        data['caption'] = u(array.get('caption')) if array.get('caption') is not None else None
        data['caption_entities'] = MessageEntity.from_array_list(array.get('caption_entities'), list_level=1) if array.get('caption_entities') is not None else None
        data['contact'] = Contact.from_array(array.get('contact')) if array.get('contact') is not None else None
        data['dice'] = Dice.from_array(array.get('dice')) if array.get('dice') is not None else None
        data['game'] = Game.from_array(array.get('game')) if array.get('game') is not None else None
        data['poll'] = Poll.from_array(array.get('poll')) if array.get('poll') is not None else None
        data['venue'] = Venue.from_array(array.get('venue')) if array.get('venue') is not None else None
        data['location'] = Location.from_array(array.get('location')) if array.get('location') is not None else None
        data['new_chat_members'] = User.from_array_list(array.get('new_chat_members'), list_level=1) if array.get('new_chat_members') is not None else None
        data['left_chat_member'] = User.from_array(array.get('left_chat_member')) if array.get('left_chat_member') is not None else None
        data['new_chat_title'] = u(array.get('new_chat_title')) if array.get('new_chat_title') is not None else None
        data['new_chat_photo'] = PhotoSize.from_array_list(array.get('new_chat_photo'), list_level=1) if array.get('new_chat_photo') is not None else None
        data['delete_chat_photo'] = bool(array.get('delete_chat_photo')) if array.get('delete_chat_photo') is not None else None
        data['group_chat_created'] = bool(array.get('group_chat_created')) if array.get('group_chat_created') is not None else None
        data['supergroup_chat_created'] = bool(array.get('supergroup_chat_created')) if array.get('supergroup_chat_created') is not None else None
        data['channel_chat_created'] = bool(array.get('channel_chat_created')) if array.get('channel_chat_created') is not None else None
        data['migrate_to_chat_id'] = int(array.get('migrate_to_chat_id')) if array.get('migrate_to_chat_id') is not None else None
        data['migrate_from_chat_id'] = int(array.get('migrate_from_chat_id')) if array.get('migrate_from_chat_id') is not None else None
        data['pinned_message'] = Message.from_array(array.get('pinned_message')) if array.get('pinned_message') is not None else None
        data['invoice'] = Invoice.from_array(array.get('invoice')) if array.get('invoice') is not None else None
        data['successful_payment'] = SuccessfulPayment.from_array(array.get('successful_payment')) if array.get('successful_payment') is not None else None
        data['connected_website'] = u(array.get('connected_website')) if array.get('connected_website') is not None else None
        data['passport_data'] = PassportData.from_array(array.get('passport_data')) if array.get('passport_data') is not None else None
        data['proximity_alert_triggered'] = ProximityAlertTriggered.from_array(array.get('proximity_alert_triggered')) if array.get('proximity_alert_triggered') is not None else None
        data['reply_markup'] = InlineKeyboardMarkup.from_array(array.get('reply_markup')) if array.get('reply_markup') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new Message from a given dictionary.

        :return: new Message instance.
        :rtype: Message
        """
        if not array:  # None or {}
            return None
        # end if

        data = Message.validate_array(array)
        data['_raw'] = array
        return Message(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(message_instance)`
        """
        return "Message(message_id={self.message_id!r}, date={self.date!r}, chat={self.chat!r}, from_peer={self.from_peer!r}, sender_chat={self.sender_chat!r}, forward_from={self.forward_from!r}, forward_from_chat={self.forward_from_chat!r}, forward_from_message_id={self.forward_from_message_id!r}, forward_signature={self.forward_signature!r}, forward_sender_name={self.forward_sender_name!r}, forward_date={self.forward_date!r}, reply_to_message={self.reply_to_message!r}, via_bot={self.via_bot!r}, edit_date={self.edit_date!r}, media_group_id={self.media_group_id!r}, author_signature={self.author_signature!r}, text={self.text!r}, entities={self.entities!r}, animation={self.animation!r}, audio={self.audio!r}, document={self.document!r}, photo={self.photo!r}, sticker={self.sticker!r}, video={self.video!r}, video_note={self.video_note!r}, voice={self.voice!r}, caption={self.caption!r}, caption_entities={self.caption_entities!r}, contact={self.contact!r}, dice={self.dice!r}, game={self.game!r}, poll={self.poll!r}, venue={self.venue!r}, location={self.location!r}, new_chat_members={self.new_chat_members!r}, left_chat_member={self.left_chat_member!r}, new_chat_title={self.new_chat_title!r}, new_chat_photo={self.new_chat_photo!r}, delete_chat_photo={self.delete_chat_photo!r}, group_chat_created={self.group_chat_created!r}, supergroup_chat_created={self.supergroup_chat_created!r}, channel_chat_created={self.channel_chat_created!r}, migrate_to_chat_id={self.migrate_to_chat_id!r}, migrate_from_chat_id={self.migrate_from_chat_id!r}, pinned_message={self.pinned_message!r}, invoice={self.invoice!r}, successful_payment={self.successful_payment!r}, connected_website={self.connected_website!r}, passport_data={self.passport_data!r}, proximity_alert_triggered={self.proximity_alert_triggered!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(message_instance)`
        """
        if self._raw:
            return "Message.from_array({self._raw})".format(self=self)
        # end if
        return "Message(message_id={self.message_id!r}, date={self.date!r}, chat={self.chat!r}, from_peer={self.from_peer!r}, sender_chat={self.sender_chat!r}, forward_from={self.forward_from!r}, forward_from_chat={self.forward_from_chat!r}, forward_from_message_id={self.forward_from_message_id!r}, forward_signature={self.forward_signature!r}, forward_sender_name={self.forward_sender_name!r}, forward_date={self.forward_date!r}, reply_to_message={self.reply_to_message!r}, via_bot={self.via_bot!r}, edit_date={self.edit_date!r}, media_group_id={self.media_group_id!r}, author_signature={self.author_signature!r}, text={self.text!r}, entities={self.entities!r}, animation={self.animation!r}, audio={self.audio!r}, document={self.document!r}, photo={self.photo!r}, sticker={self.sticker!r}, video={self.video!r}, video_note={self.video_note!r}, voice={self.voice!r}, caption={self.caption!r}, caption_entities={self.caption_entities!r}, contact={self.contact!r}, dice={self.dice!r}, game={self.game!r}, poll={self.poll!r}, venue={self.venue!r}, location={self.location!r}, new_chat_members={self.new_chat_members!r}, left_chat_member={self.left_chat_member!r}, new_chat_title={self.new_chat_title!r}, new_chat_photo={self.new_chat_photo!r}, delete_chat_photo={self.delete_chat_photo!r}, group_chat_created={self.group_chat_created!r}, supergroup_chat_created={self.supergroup_chat_created!r}, channel_chat_created={self.channel_chat_created!r}, migrate_to_chat_id={self.migrate_to_chat_id!r}, migrate_from_chat_id={self.migrate_from_chat_id!r}, pinned_message={self.pinned_message!r}, invoice={self.invoice!r}, successful_payment={self.successful_payment!r}, connected_website={self.connected_website!r}, passport_data={self.passport_data!r}, proximity_alert_triggered={self.proximity_alert_triggered!r}, reply_markup={self.reply_markup!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in message_instance`
        """
        return (
            key in ["message_id", "date", "chat", "from_peer", "sender_chat", "forward_from", "forward_from_chat", "forward_from_message_id", "forward_signature", "forward_sender_name", "forward_date", "reply_to_message", "via_bot", "edit_date", "media_group_id", "author_signature", "text", "entities", "animation", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "caption", "caption_entities", "contact", "dice", "game", "poll", "venue", "location", "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message", "invoice", "successful_payment", "connected_website", "passport_data", "proximity_alert_triggered", "reply_markup"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class Message


class CallbackQuery(UpdateType):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    NOTE: After the user presses a callback button, Telegram clients will display a progress bar until you call answerCallbackQuery. It is, therefore, necessary to react by calling answerCallbackQuery even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

    https://core.telegram.org/bots/api#callbackquery


    Parameters:

    :param id: Unique identifier for this query
    :type  id: str|unicode

    :param from_peer: Sender
    :type  from_peer: pytgbot.api_types.receivable.peer.User

    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
    :type  chat_instance: str|unicode


    Optional keyword parameters:

    :param message: Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    :type  message: pytgbot.api_types.receivable.updates.Message

    :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
    :type  inline_message_id: str|unicode

    :param data: Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
    :type  data: str|unicode

    :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game
    :type  game_short_name: str|unicode

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, id, from_peer, chat_instance, message=None, inline_message_id=None, data=None, game_short_name=None, _raw=None):
        """
        This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

        NOTE: After the user presses a callback button, Telegram clients will display a progress bar until you call answerCallbackQuery. It is, therefore, necessary to react by calling answerCallbackQuery even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

        https://core.telegram.org/bots/api#callbackquery


        Parameters:

        :param id: Unique identifier for this query
        :type  id: str|unicode

        :param from_peer: Sender
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
        :type  chat_instance: str|unicode


        Optional keyword parameters:

        :param message: Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
        :type  message: pytgbot.api_types.receivable.updates.Message

        :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the query.
        :type  inline_message_id: str|unicode

        :param data: Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
        :type  data: str|unicode

        :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game
        :type  game_short_name: str|unicode

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(CallbackQuery, self).__init__()
        from .peer import User

        assert_type_or_raise(id, unicode_type, parameter_name="id")
        self.id = id
        assert_type_or_raise(from_peer, User, parameter_name="from_peer")
        self.from_peer = from_peer
        assert_type_or_raise(chat_instance, unicode_type, parameter_name="chat_instance")
        self.chat_instance = chat_instance
        assert_type_or_raise(message, None, Message, parameter_name="message")
        self.message = message
        assert_type_or_raise(inline_message_id, None, unicode_type, parameter_name="inline_message_id")
        self.inline_message_id = inline_message_id
        assert_type_or_raise(data, None, unicode_type, parameter_name="data")
        self.data = data
        assert_type_or_raise(game_short_name, None, unicode_type, parameter_name="game_short_name")
        self.game_short_name = game_short_name

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this CallbackQuery to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(CallbackQuery, self).to_array()

        array['id'] = u(self.id)  # py2: type unicode, py3: type str
        array['from'] = self.from_peer.to_array()  # type User
        array['chat_instance'] = u(self.chat_instance)  # py2: type unicode, py3: type str
        if self.message is not None:
            array['message'] = self.message.to_array()  # type Message
        # end if
        if self.inline_message_id is not None:
            array['inline_message_id'] = u(self.inline_message_id)  # py2: type unicode, py3: type str
        # end if
        if self.data is not None:
            array['data'] = u(self.data)  # py2: type unicode, py3: type str
        # end if
        if self.game_short_name is not None:
            array['game_short_name'] = u(self.game_short_name)  # py2: type unicode, py3: type str
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the CallbackQuery constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User

        data = UpdateType.validate_array(array)
        data['id'] = u(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['chat_instance'] = u(array.get('chat_instance'))
        data['message'] = Message.from_array(array.get('message')) if array.get('message') is not None else None
        data['inline_message_id'] = u(array.get('inline_message_id')) if array.get('inline_message_id') is not None else None
        data['data'] = u(array.get('data')) if array.get('data') is not None else None
        data['game_short_name'] = u(array.get('game_short_name')) if array.get('game_short_name') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new CallbackQuery from a given dictionary.

        :return: new CallbackQuery instance.
        :rtype: CallbackQuery
        """
        if not array:  # None or {}
            return None
        # end if

        data = CallbackQuery.validate_array(array)
        data['_raw'] = array
        return CallbackQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(callbackquery_instance)`
        """
        return "CallbackQuery(id={self.id!r}, from_peer={self.from_peer!r}, chat_instance={self.chat_instance!r}, message={self.message!r}, inline_message_id={self.inline_message_id!r}, data={self.data!r}, game_short_name={self.game_short_name!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(callbackquery_instance)`
        """
        if self._raw:
            return "CallbackQuery.from_array({self._raw})".format(self=self)
        # end if
        return "CallbackQuery(id={self.id!r}, from_peer={self.from_peer!r}, chat_instance={self.chat_instance!r}, message={self.message!r}, inline_message_id={self.inline_message_id!r}, data={self.data!r}, game_short_name={self.game_short_name!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in callbackquery_instance`
        """
        return (
            key in ["id", "from_peer", "chat_instance", "message", "inline_message_id", "data", "game_short_name"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class CallbackQuery


class ResponseParameters(Receivable):
    """
    Contains information about why a request was unsuccessful.

    https://core.telegram.org/bots/api#responseparameters

    Optional keyword parameters:

    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
    :type  migrate_to_chat_id: int

    :param retry_after: Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    :type  retry_after: int

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, migrate_to_chat_id=None, retry_after=None, _raw=None):
        """
        Contains information about why a request was unsuccessful.

        https://core.telegram.org/bots/api#responseparameters

        Optional keyword parameters:

        :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type  migrate_to_chat_id: int

        :param retry_after: Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
        :type  retry_after: int

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ResponseParameters, self).__init__()
        assert_type_or_raise(migrate_to_chat_id, None, int, parameter_name="migrate_to_chat_id")
        self.migrate_to_chat_id = migrate_to_chat_id
        assert_type_or_raise(retry_after, None, int, parameter_name="retry_after")
        self.retry_after = retry_after

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ResponseParameters to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(ResponseParameters, self).to_array()

        if self.migrate_to_chat_id is not None:
            array['migrate_to_chat_id'] = int(self.migrate_to_chat_id)  # type int
        # end if
        if self.retry_after is not None:
            array['retry_after'] = int(self.retry_after)  # type int
        # end if

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ResponseParameters constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = Receivable.validate_array(array)
        data['migrate_to_chat_id'] = int(array.get('migrate_to_chat_id')) if array.get('migrate_to_chat_id') is not None else None
        data['retry_after'] = int(array.get('retry_after')) if array.get('retry_after') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ResponseParameters from a given dictionary.

        :return: new ResponseParameters instance.
        :rtype: ResponseParameters
        """
        if not array:  # None or {}
            return None
        # end if

        data = ResponseParameters.validate_array(array)
        data['_raw'] = array
        return ResponseParameters(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(responseparameters_instance)`
        """
        return "ResponseParameters(migrate_to_chat_id={self.migrate_to_chat_id!r}, retry_after={self.retry_after!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(responseparameters_instance)`
        """
        if self._raw:
            return "ResponseParameters.from_array({self._raw})".format(self=self)
        # end if
        return "ResponseParameters(migrate_to_chat_id={self.migrate_to_chat_id!r}, retry_after={self.retry_after!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in responseparameters_instance`
        """
        return (
            key in ["migrate_to_chat_id", "retry_after"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ResponseParameters

