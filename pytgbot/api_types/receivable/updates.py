# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging

from . import Receivable

__author__ = 'luckydonald'
logger = logging.getLogger(__name__)


class UpdateType(Receivable):
    pass


class Update(Receivable):
    """
    This object represents an incoming update. Only one of the optional parameters can be present in any given update.

    https://core.telegram.org/bots/api#update
    """
    def __init__(self, update_id, message=None, edited_message=None, inline_query=None, chosen_inline_result=None, callback_query=None):
        """
        This object represents an incoming update.Only one of the optional parameters can be present in any given update.

        https://core.telegram.org/bots/api#update


        Parameters:

        :param update_id: The update‘s unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you’re using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order.
        :type  update_id: int


        Optional keyword parameters:

        :keyword message: Optional. New incoming message of any kind — text, photo, sticker, etc.
        :type    message: Message

        :keyword edited_message: Optional. New version of a message that is known to the bot and was edited
        :type    edited_message: Message

        :keyword inline_query: Optional. New incoming inline query
        :type    inline_query: pytgbot.api_types.receivable.inline.InlineQuery

        :keyword chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their chat partner.
        :type    chosen_inline_result: pytgbot.api_types.receivable.inline.ChosenInlineResult

        :keyword callback_query: Optional. New incoming callback query
        :type    callback_query: CallbackQuery
        """
        super(Update, self).__init__()
        from ..receivable.inline import InlineQuery
        from ..receivable.inline import ChosenInlineResult

        assert(update_id is not None)
        assert(isinstance(update_id, int))
        self.update_id = update_id

        assert(message is None or isinstance(message, Message))
        self.message = message

        assert(edited_message is None or isinstance(edited_message, Message))
        self.edited_message = edited_message

        assert(inline_query is None or isinstance(inline_query, InlineQuery))
        self.inline_query = inline_query

        assert(chosen_inline_result is None or isinstance(chosen_inline_result, ChosenInlineResult))
        self.chosen_inline_result = chosen_inline_result

        assert(callback_query is None or isinstance(callback_query, CallbackQuery))
        self.callback_query = callback_query
    # end def __init__

    def to_array(self):
        """
        Serializes this Update to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Update, self).to_array()
        array['update_id'] = int(self.update_id)  # type int
        if self.message is not None:
            array['message'] = self.message.to_array()  # type Message
        if self.edited_message is not None:
            array['edited_message'] = self.edited_message.to_array()  # type Message
        if self.inline_query is not None:
            array['inline_query'] = self.inline_query.to_array()  # type InlineQuery
        if self.chosen_inline_result is not None:
            array['chosen_inline_result'] = self.chosen_inline_result.to_array()  # type ChosenInlineResult
        if self.callback_query is not None:
            array['callback_query'] = self.callback_query.to_array()  # type CallbackQuery
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Update from a given dictionary.

        :return: new Update instance.
        :rtype: Update
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from ..receivable.inline import InlineQuery
        from ..receivable.inline import ChosenInlineResult

        data = {}
        data['update_id'] = int(array.get('update_id'))
        data['message'] = Message.from_array(array.get('message')) if array.get('message') is not None else None
        data['edited_message'] = Message.from_array(array.get('edited_message')) if array.get('edited_message') is not None else None
        data['inline_query'] = InlineQuery.from_array(array.get('inline_query')) if array.get('inline_query') is not None else None
        data['chosen_inline_result'] = ChosenInlineResult.from_array(array.get('chosen_inline_result')) if array.get('chosen_inline_result') is not None else None
        data['callback_query'] = CallbackQuery.from_array(array.get('callback_query')) if array.get('callback_query') is not None else None
        return Update(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(update_instance)`
        """
        return "Update(update_id={self.update_id!r}, message={self.message!r}, edited_message={self.edited_message!r}, inline_query={self.inline_query!r}, chosen_inline_result={self.chosen_inline_result!r}, callback_query={self.callback_query!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in update_instance`
        """
        return key in ["update_id", "message", "edited_message", "inline_query", "chosen_inline_result", "callback_query"]
    # end def __contains__
# end class Update


class Message(UpdateType):
    """
    This object represents a message.

    https://core.telegram.org/bots/api#message
    """
    def __init__(self, message_id, date, chat, from_peer=None, forward_from=None, forward_from_chat=None, forward_date=None, reply_to_message=None, edit_date=None, text=None, entities=None, audio=None, document=None, game=None, photo=None, sticker=None, video=None, voice=None, caption=None, contact=None, location=None, venue=None, new_chat_member=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None, migrate_from_chat_id=None, pinned_message=None):
        """
        This object represents a message.

        https://core.telegram.org/bots/api#message


        Parameters:

        :param message_id: Unique message identifier
        :type  message_id: int

        :param date: Date the message was sent in Unix time
        :type  date: int

        :param chat: Conversation the message belongs to
        :type  chat: pytgbot.api_types.receivable.peer.Chat


        Optional keyword parameters:

        :keyword from_peer: Optional. Sender, can be empty for messages sent to channels
        :type    from_peer: pytgbot.api_types.receivable.peer.User

        :keyword forward_from: Optional. For forwarded messages, sender of the original message
        :type    forward_from: pytgbot.api_types.receivable.peer.User

        :keyword forward_from_chat: Optional. For messages forwarded from a channel, information about the original channel
        :type    forward_from_chat: pytgbot.api_types.receivable.peer.Chat

        :keyword forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
        :type    forward_date: int

        :keyword reply_to_message: Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
        :type    reply_to_message: Message

        :keyword edit_date: Optional. Date the message was last edited in Unix time
        :type    edit_date: int

        :keyword text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters.
        :type    text: str

        :keyword entities: Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
        :type    entities: list of pytgbot.api_types.receivable.media.MessageEntity

        :keyword audio: Optional. Message is an audio file, information about the file
        :type    audio: pytgbot.api_types.receivable.media.Audio

        :keyword document: Optional. Message is a general file, information about the file
        :type    document: pytgbot.api_types.receivable.media.Document

        :keyword game: Optional. Message is a game, information about the game. More about games »
        :type    game: pytgbot.api_types.receivable.media.Game

        :keyword photo: Optional. Message is a photo, available sizes of the photo
        :type    photo: list of pytgbot.api_types.receivable.media.PhotoSize

        :keyword sticker: Optional. Message is a sticker, information about the sticker
        :type    sticker: pytgbot.api_types.receivable.media.Sticker

        :keyword video: Optional. Message is a video, information about the video
        :type    video: pytgbot.api_types.receivable.media.Video

        :keyword voice: Optional. Message is a voice message, information about the file
        :type    voice: pytgbot.api_types.receivable.media.Voice

        :keyword caption: Optional. Caption for the document, photo or video, 0-200 characters
        :type    caption: str

        :keyword contact: Optional. Message is a shared contact, information about the contact
        :type    contact: pytgbot.api_types.receivable.media.Contact

        :keyword location: Optional. Message is a shared location, information about the location
        :type    location: pytgbot.api_types.receivable.media.Location

        :keyword venue: Optional. Message is a venue, information about the venue
        :type    venue: pytgbot.api_types.receivable.media.Venue

        :keyword new_chat_member: Optional. A new member was added to the group, information about them (this member may be the bot itself)
        :type    new_chat_member: pytgbot.api_types.receivable.peer.User

        :keyword left_chat_member: Optional. A member was removed from the group, information about them (this member may be the bot itself)
        :type    left_chat_member: pytgbot.api_types.receivable.peer.User

        :keyword new_chat_title: Optional. A chat title was changed to this value
        :type    new_chat_title: str

        :keyword new_chat_photo: Optional. A chat photo was change to this value
        :type    new_chat_photo: list of pytgbot.api_types.receivable.media.PhotoSize

        :keyword delete_chat_photo: Optional. Service message: the chat photo was deleted
        :type    delete_chat_photo: bool

        :keyword group_chat_created: Optional. Service message: the group has been created
        :type    group_chat_created: bool

        :keyword supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can‘t be received in a message coming through updates, because bot can’t be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
        :type    supergroup_chat_created: bool

        :keyword channel_chat_created: Optional. Service message: the channel has been created. This field can‘t be received in a message coming through updates, because bot can’t be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
        :type    channel_chat_created: bool

        :keyword migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type    migrate_to_chat_id: int

        :keyword migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type    migrate_from_chat_id: int

        :keyword pinned_message: Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it is itself a reply.
        :type    pinned_message: Message
        """
        super(Message, self).__init__()

        from ..receivable.peer import User, Chat
        from ..receivable.media import Audio, Contact, Document, Game, Location, Sticker, Venue, Video, Voice

        assert(message_id is not None)
        assert(isinstance(message_id, int))
        self.message_id = message_id

        assert(date is not None)
        assert(isinstance(date, int))
        self.date = date

        assert(chat is not None)
        assert(isinstance(chat, Chat))
        self.chat = chat

        assert(from_peer is None or isinstance(from_peer, User))
        self.from_peer = from_peer

        assert(forward_from is None or isinstance(forward_from, User))
        self.forward_from = forward_from

        assert(forward_from_chat is None or isinstance(forward_from_chat, Chat))
        self.forward_from_chat = forward_from_chat

        assert(forward_date is None or isinstance(forward_date, int))
        self.forward_date = forward_date

        assert(reply_to_message is None or isinstance(reply_to_message, Message))
        self.reply_to_message = reply_to_message

        assert(edit_date is None or isinstance(edit_date, int))
        self.edit_date = edit_date

        assert(text is None or isinstance(text, str))
        self.text = text

        assert(entities is None or isinstance(entities, (list, tuple)))  # list of MessageEntity
        self.entities = entities

        assert(audio is None or isinstance(audio, Audio))
        self.audio = audio

        assert(document is None or isinstance(document, Document))
        self.document = document

        assert(game is None or isinstance(game, Game))
        self.game = game

        assert(photo is None or isinstance(photo, (list, tuple)))  # list of PhotoSize
        self.photo = photo

        assert(sticker is None or isinstance(sticker, Sticker))
        self.sticker = sticker

        assert(video is None or isinstance(video, Video))
        self.video = video

        assert(voice is None or isinstance(voice, Voice))
        self.voice = voice

        assert(caption is None or isinstance(caption, str))
        self.caption = caption

        assert(contact is None or isinstance(contact, Contact))
        self.contact = contact

        assert(location is None or isinstance(location, Location))
        self.location = location

        assert(venue is None or isinstance(venue, Venue))
        self.venue = venue

        assert(new_chat_member is None or isinstance(new_chat_member, User))
        self.new_chat_member = new_chat_member

        assert(left_chat_member is None or isinstance(left_chat_member, User))
        self.left_chat_member = left_chat_member

        assert(new_chat_title is None or isinstance(new_chat_title, str))
        self.new_chat_title = new_chat_title

        assert(new_chat_photo is None or isinstance(new_chat_photo, (list, tuple)))  # list of PhotoSize
        self.new_chat_photo = new_chat_photo

        assert(delete_chat_photo is None or delete_chat_photo == True)
        self.delete_chat_photo = delete_chat_photo

        assert(group_chat_created is None or group_chat_created == True)
        self.group_chat_created = group_chat_created

        assert(supergroup_chat_created is None or supergroup_chat_created == True)
        self.supergroup_chat_created = supergroup_chat_created

        assert(channel_chat_created is None or channel_chat_created == True)
        self.channel_chat_created = channel_chat_created

        assert(migrate_to_chat_id is None or isinstance(migrate_to_chat_id, int))
        self.migrate_to_chat_id = migrate_to_chat_id

        assert(migrate_from_chat_id is None or isinstance(migrate_from_chat_id, int))
        self.migrate_from_chat_id = migrate_from_chat_id

        assert(pinned_message is None or isinstance(pinned_message, Message))
        self.pinned_message = pinned_message
    # end def __init__

    def to_array(self):
        """
        Serializes this Message to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(Message, self).to_array()
        array['message_id'] = int(self.message_id)  # type int
        array['date'] = int(self.date)  # type int
        array['chat'] = self.chat.to_array()  # type Chat
        if self.from_peer is not None:
            array['from'] = self.from_peer.to_array()  # type User
        if self.forward_from is not None:
            array['forward_from'] = self.forward_from.to_array()  # type User
        if self.forward_from_chat is not None:
            array['forward_from_chat'] = self.forward_from_chat.to_array()  # type Chat
        if self.forward_date is not None:
            array['forward_date'] = int(self.forward_date)  # type int
        if self.reply_to_message is not None:
            array['reply_to_message'] = self.reply_to_message.to_array()  # type Message
        if self.edit_date is not None:
            array['edit_date'] = int(self.edit_date)  # type int
        if self.text is not None:
            array['text'] = str(self.text)  # type str
        if self.entities is not None:
            array['entities'] = self._as_array(self.entities)  # type list of MessageEntity
        if self.audio is not None:
            array['audio'] = self.audio.to_array()  # type Audio
        if self.document is not None:
            array['document'] = self.document.to_array()  # type Document
        if self.game is not None:
            array['game'] = self.game.to_array()  # type Game
        if self.photo is not None:
            array['photo'] = self._as_array(self.photo)  # type list of PhotoSize
        if self.sticker is not None:
            array['sticker'] = self.sticker.to_array()  # type Sticker
        if self.video is not None:
            array['video'] = self.video.to_array()  # type Video
        if self.voice is not None:
            array['voice'] = self.voice.to_array()  # type Voice
        if self.caption is not None:
            array['caption'] = str(self.caption)  # type str
        if self.contact is not None:
            array['contact'] = self.contact.to_array()  # type Contact
        if self.location is not None:
            array['location'] = self.location.to_array()  # type Location
        if self.venue is not None:
            array['venue'] = self.venue.to_array()  # type Venue
        if self.new_chat_member is not None:
            array['new_chat_member'] = self.new_chat_member.to_array()  # type User
        if self.left_chat_member is not None:
            array['left_chat_member'] = self.left_chat_member.to_array()  # type User
        if self.new_chat_title is not None:
            array['new_chat_title'] = str(self.new_chat_title)  # type str
        if self.new_chat_photo is not None:
            array['new_chat_photo'] = self._as_array(self.new_chat_photo)  # type list of PhotoSize
        if self.delete_chat_photo is not None:
            array['delete_chat_photo'] = bool(self.delete_chat_photo)  # type bool
        if self.group_chat_created is not None:
            array['group_chat_created'] = bool(self.group_chat_created)  # type bool
        if self.supergroup_chat_created is not None:
            array['supergroup_chat_created'] = bool(self.supergroup_chat_created)  # type bool
        if self.channel_chat_created is not None:
            array['channel_chat_created'] = bool(self.channel_chat_created)  # type bool
        if self.migrate_to_chat_id is not None:
            array['migrate_to_chat_id'] = int(self.migrate_to_chat_id)  # type int
        if self.migrate_from_chat_id is not None:
            array['migrate_from_chat_id'] = int(self.migrate_from_chat_id)  # type int
        if self.pinned_message is not None:
            array['pinned_message'] = self.pinned_message.to_array()  # type Message
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new Message from a given dictionary.

        :return: new Message instance.
        :rtype: Message
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from ..receivable.peer import User, Chat
        from ..receivable.media import Audio, Sticker, Video, Voice, Contact, Location, Venue, Document, MessageEntity, PhotoSize

        data = {}
        data['message_id'] = int(array.get('message_id'))
        data['date'] = int(array.get('date'))
        data['chat'] = Chat.from_array(array.get('chat'))
        data['from_peer'] = User.from_array(array.get('from')) if array.get('from') is not None else None
        data['forward_from'] = User.from_array(array.get('forward_from')) if array.get('forward_from') is not None else None
        data['forward_from_chat'] = Chat.from_array(array.get('forward_from_chat')) if array.get('forward_from_chat') is not None else None
        data['forward_date'] = int(array.get('forward_date')) if array.get('forward_date') is not None else None
        data['reply_to_message'] = Message.from_array(array.get('reply_to_message')) if array.get('reply_to_message') is not None else None
        data['edit_date'] = int(array.get('edit_date')) if array.get('edit_date') is not None else None
        data['text'] = str(array.get('text')) if array.get('text') is not None else None
        data['entities'] = MessageEntity.from_array_list(array.get('entities'), list_level=1) if array.get('entities') is not None else None
        data['audio'] = Audio.from_array(array.get('audio')) if array.get('audio') is not None else None
        data['document'] = Document.from_array(array.get('document')) if array.get('document') is not None else None
        data['game'] = Game.from_array(array.get('game')) if array.get('game') is not None else None
        data['photo'] = PhotoSize.from_array_list(array.get('photo'), list_level=1) if array.get('photo') is not None else None
        data['sticker'] = Sticker.from_array(array.get('sticker')) if array.get('sticker') is not None else None
        data['video'] = Video.from_array(array.get('video')) if array.get('video') is not None else None
        data['voice'] = Voice.from_array(array.get('voice')) if array.get('voice') is not None else None
        data['caption'] = str(array.get('caption')) if array.get('caption') is not None else None
        data['contact'] = Contact.from_array(array.get('contact')) if array.get('contact') is not None else None
        data['location'] = Location.from_array(array.get('location')) if array.get('location') is not None else None
        data['venue'] = Venue.from_array(array.get('venue')) if array.get('venue') is not None else None
        data['new_chat_member'] = User.from_array(array.get('new_chat_member')) if array.get('new_chat_member') is not None else None
        data['left_chat_member'] = User.from_array(array.get('left_chat_member')) if array.get('left_chat_member') is not None else None
        data['new_chat_title'] = str(array.get('new_chat_title')) if array.get('new_chat_title') is not None else None
        data['new_chat_photo'] = PhotoSize.from_array_list(array.get('new_chat_photo'), list_level=1) if array.get('new_chat_photo') is not None else None
        data['delete_chat_photo'] = bool(array.get('delete_chat_photo')) if array.get('delete_chat_photo') is not None else None
        data['group_chat_created'] = bool(array.get('group_chat_created')) if array.get('group_chat_created') is not None else None
        data['supergroup_chat_created'] = bool(array.get('supergroup_chat_created')) if array.get('supergroup_chat_created') is not None else None
        data['channel_chat_created'] = bool(array.get('channel_chat_created')) if array.get('channel_chat_created') is not None else None
        data['migrate_to_chat_id'] = int(array.get('migrate_to_chat_id')) if array.get('migrate_to_chat_id') is not None else None
        data['migrate_from_chat_id'] = int(array.get('migrate_from_chat_id')) if array.get('migrate_from_chat_id') is not None else None
        data['pinned_message'] = Message.from_array(array.get('pinned_message')) if array.get('pinned_message') is not None else None
        return Message(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(message_instance)`
        """
        return "Message(message_id={self.message_id!r}, date={self.date!r}, chat={self.chat!r}, from_peer={self.from_peer!r}, forward_from={self.forward_from!r}, forward_from_chat={self.forward_from_chat!r}, forward_date={self.forward_date!r}, reply_to_message={self.reply_to_message!r}, edit_date={self.edit_date!r}, text={self.text!r}, entities={self.entities!r}, audio={self.audio!r}, document={self.document!r}, game={self.game!r}, photo={self.photo!r}, sticker={self.sticker!r}, video={self.video!r}, voice={self.voice!r}, caption={self.caption!r}, contact={self.contact!r}, location={self.location!r}, venue={self.venue!r}, new_chat_member={self.new_chat_member!r}, left_chat_member={self.left_chat_member!r}, new_chat_title={self.new_chat_title!r}, new_chat_photo={self.new_chat_photo!r}, delete_chat_photo={self.delete_chat_photo!r}, group_chat_created={self.group_chat_created!r}, supergroup_chat_created={self.supergroup_chat_created!r}, channel_chat_created={self.channel_chat_created!r}, migrate_to_chat_id={self.migrate_to_chat_id!r}, migrate_from_chat_id={self.migrate_from_chat_id!r}, pinned_message={self.pinned_message!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in message_instance`
        """
        return key in ["message_id", "date", "chat", "from_peer", "forward_from", "forward_from_chat", "forward_date", "reply_to_message", "edit_date", "text", "entities", "audio", "document", "game", "photo", "sticker", "video", "voice", "caption", "contact", "location", "venue", "new_chat_member", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message"]
    # end def __contains__
# end class Message


class CallbackQuery(UpdateType):
    """
    This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

    NOTE: After the user presses an inline button, Telegram clients will display a progress bar until you call answerCallbackQuery. It is, therefore, necessary to react by calling answerCallbackQuery even if no notification to the user is needed (e.g., without specifying any of the optional parameters).

    https://core.telegram.org/bots/api#callbackquery
    """
    def __init__(self, id, from_peer, chat_instance, message=None, inline_message_id=None, data=None, game_short_name=None):
        """
        This object represents an incoming callback query from a callback button in an inline keyboard. If the button that originated the query was attached to a message sent by the bot, the field message will be present. If the button was attached to a message sent via the bot (in inline mode), the field inline_message_id will be present. Exactly one of the fields data or game_short_name will be present.

        NOTE: After the user presses an inline button, Telegram clients will display a progress bar until you call answerCallbackQuery. It is, therefore, necessary to react by calling answerCallbackQuery even if no notification to the user is needed (e.g., without specifying any of the optional parameters).
    
        https://core.telegram.org/bots/api#callbackquery


        Parameters:

        :param id: Unique identifier for this query
        :type  id: str

        :param from_peer: Sender
        :type  from_peer: pytgbot.api_types.receivable.peer.User

        :param chat_instance: Identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in games.
        :type  chat_instance: str


        Optional keyword parameters:

        :keyword message: Optional. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
        :type    message: pytgbot.api_types.receivable.updates.Message

        :keyword inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated the query
        :type    inline_message_id: str
        
        :keyword data: Optional. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
        :type    data: str
        
        :keyword game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for the game
        :type    game_short_name: str
        """
        super(CallbackQuery, self).__init__()

        from ..receivable.peer import User

        assert(id is not None)
        assert(isinstance(id, str))
        self.id = id

        assert(from_peer is not None)
        assert(isinstance(from_peer, User))
        self.from_peer = from_peer

        assert(chat_instance is not None)
        assert(isinstance(chat_instance, str))
        self.chat_instance = chat_instance

        assert(message is None or isinstance(message, Message))
        self.message = message

        assert(inline_message_id is None or isinstance(inline_message_id, str))
        self.inline_message_id = inline_message_id
        
        assert(data is None or isinstance(data, str))
        self.data = data
        
        assert(game_short_name is None or isinstance(game_short_name, str))
        self.game_short_name = game_short_name
    # end def __init__

    def to_array(self):
        """
        Serializes this CallbackQuery to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(CallbackQuery, self).to_array()
        array['id'] = str(self.id)  # type str
        array['from'] = self.from_peer.to_array()  # type User
        array['chat_instance'] = str(self.chat_instance)  # type str
        if self.message is not None:
            array['message'] = self.message.to_array()  # type Message
        if self.inline_message_id is not None:
            array['inline_message_id'] = str(self.inline_message_id)  # type str
        if self.data is not None:
            array['data'] = str(self.data)  # type str
        if self.game_short_name is not None:
            array['game_short_name'] = str(self.game_short_name)  # type str
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new CallbackQuery from a given dictionary.

        :return: new CallbackQuery instance.
        :rtype: CallbackQuery
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))

        from ..receivable.peer import User

        data = {}
        data['id'] = str(array.get('id'))
        data['from_peer'] = User.from_array(array.get('from'))
        data['chat_instance'] = str(array.get('chat_instance'))
        data['message'] = Message.from_array(array.get('message')) if array.get('message') is not None else None
        data['inline_message_id'] = str(array.get('inline_message_id')) if array.get('inline_message_id') is not None else None
        data['data'] = str(array.get('data')) if array.get('data') is not None else None
        data['game_short_name'] = str(array.get('game_short_name')) if array.get('game_short_name') is not None else None
        return CallbackQuery(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(callbackquery_instance)`
        """
        return "CallbackQuery(id={self.id!r}, from_peer={self.from_peer!r}, chat_instance={self.chat_instance!r}, message={self.message!r}, inline_message_id={self.inline_message_id!r}, data={self.data!r}, game_short_name={self.game_short_name!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in callbackquery_instance`
        """
        return key in ["id", "from_peer", "chat_instance", "message", "inline_message_id", "data", "game_short_name"]
    # end def __contains__
# end class CallbackQuery



class ResponseParameters(Receivable):
    """
    Contains information about why a request was unsuccessfull.

    https://core.telegram.org/bots/api#responseparameters
    """
    def __init__(self, migrate_to_chat_id=None, retry_after=None):
        """
        Contains information about why a request was unsuccessfull.
    
        https://core.telegram.org/bots/api#responseparameters

        Optional keyword parameters:
        
        :keyword migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier. This number may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier.
        :type    migrate_to_chat_id: int
        
        :keyword retry_after: Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
        :type    retry_after: int
        """
        super(ResponseParameters, self).__init__()
        assert(migrate_to_chat_id is None or isinstance(migrate_to_chat_id, int))
        self.migrate_to_chat_id = migrate_to_chat_id
        
        assert(retry_after is None or isinstance(retry_after, int))
        self.retry_after = retry_after
    # end def __init__

    def to_array(self):
        """
        Serializes this ResponseParameters to a dictionary.

        :return: dictionary repesentation of this object.
        :rtype: dict
        """
        array = super(ResponseParameters, self).to_array()
        if self.migrate_to_chat_id is not None:
            array['migrate_to_chat_id'] = int(self.migrate_to_chat_id)  # type int
        if self.retry_after is not None:
            array['retry_after'] = int(self.retry_after)  # type int
        return array
    # end def to_array

    @staticmethod
    def from_array(array):
        """
        Deserializes a new ResponseParameters from a given dictionary.

        :return: new ResponseParameters instance.
        :rtype: ResponseParameters
        """
        if array is None or not array:
            return None
        # end if
        assert(isinstance(array, dict))
        
        data = {}
        data['migrate_to_chat_id'] = int(array.get('migrate_to_chat_id')) if array.get('migrate_to_chat_id') is not None else None
        data['retry_after'] = int(array.get('retry_after')) if array.get('retry_after') is not None else None
        return ResponseParameters(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(responseparameters_instance)`
        """
        return "ResponseParameters(migrate_to_chat_id={self.migrate_to_chat_id!r}, retry_after={self.retry_after!r})".format(self=self)
    # end def __str__

    def __contains__(self, key):
        """
        Implements `"key" in responseparameters_instance`
        """
        return key in ["migrate_to_chat_id", "retry_after"]
    # end def __contains__
# end class ResponseParameters

