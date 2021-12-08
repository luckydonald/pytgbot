# -*- coding: utf-8 -*-
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from luckydonaldUtils.exceptions import assert_type_or_raise
from . import Receivable

__author__ = 'luckydonald'
__all__ = [
    'ServiceMessage',
    'ProximityAlertTriggered',
    'MessageAutoDeleteTimerChanged',
    'VoiceChatScheduled',
    'VoiceChatStarted',
    'VoiceChatEnded',
    'VoiceChatParticipantsInvited',
]


class ServiceMessage(Receivable):
    """
    parent class for all service messages, those are not directly media related special attributes of the Message object.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    pass
# end class ServiceMessage


class ProximityAlertTriggered(ServiceMessage):
    """
    This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    https://core.telegram.org/bots/api#proximityalerttriggered


    Parameters:

    :param traveler: User that triggered the alert
    :type  traveler: pytgbot.api_types.receivable.peer.User

    :param watcher: User that set the alert
    :type  watcher: pytgbot.api_types.receivable.peer.User

    :param distance: The distance between the users
    :type  distance: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, traveler, watcher, distance, _raw=None):
        """
        This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

        https://core.telegram.org/bots/api#proximityalerttriggered


        Parameters:

        :param traveler: User that triggered the alert
        :type  traveler: pytgbot.api_types.receivable.peer.User

        :param watcher: User that set the alert
        :type  watcher: pytgbot.api_types.receivable.peer.User

        :param distance: The distance between the users
        :type  distance: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(ProximityAlertTriggered, self).__init__()
        from .peer import User
        assert_type_or_raise(traveler, User, parameter_name="traveler")
        self.traveler = traveler
        assert_type_or_raise(watcher, User, parameter_name="watcher")
        self.watcher = watcher
        assert_type_or_raise(distance, int, parameter_name="distance")
        self.distance = distance

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this ProximityAlertTriggered to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        from .peer import User
        array = super(ProximityAlertTriggered, self).to_array()

        array['traveler'] = self.traveler.to_array()  # type User
        array['watcher'] = self.watcher.to_array()  # type User
        array['distance'] = int(self.distance)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the ProximityAlertTriggered constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User
        data = ServiceMessage.validate_array(array)
        data['traveler'] = User.from_array(array.get('traveler'))
        data['watcher'] = User.from_array(array.get('watcher'))
        data['distance'] = int(array.get('distance'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new ProximityAlertTriggered from a given dictionary.

        :return: new ProximityAlertTriggered instance.
        :rtype: ProximityAlertTriggered
        """
        if not array:  # None or {}
            return None
        # end if

        data = ProximityAlertTriggered.validate_array(array)
        data['_raw'] = array
        return ProximityAlertTriggered(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(proximityalerttriggered_instance)`
        """
        return "ProximityAlertTriggered(traveler={self.traveler!r}, watcher={self.watcher!r}, distance={self.distance!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(proximityalerttriggered_instance)`
        """
        if self._raw:
            return "ProximityAlertTriggered.from_array({self._raw})".format(self=self)
        # end if
        return "ProximityAlertTriggered(traveler={self.traveler!r}, watcher={self.watcher!r}, distance={self.distance!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in proximityalerttriggered_instance`
        """
        return (
            key in ["traveler", "watcher", "distance"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class ProximityAlertTriggered


class MessageAutoDeleteTimerChanged(ServiceMessage):
    """
    This object represents a service message about a change in auto-delete timer settings.

    https://core.telegram.org/bots/api#messageautodeletetimerchanged


    Parameters:

    :param message_auto_delete_time: New auto-delete time for messages in the chat; in seconds
    :type  message_auto_delete_time: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, message_auto_delete_time, _raw=None):
        """
        This object represents a service message about a change in auto-delete timer settings.

        https://core.telegram.org/bots/api#messageautodeletetimerchanged


        Parameters:

        :param message_auto_delete_time: New auto-delete time for messages in the chat; in seconds
        :type  message_auto_delete_time: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(MessageAutoDeleteTimerChanged, self).__init__()
        assert_type_or_raise(message_auto_delete_time, int, parameter_name="message_auto_delete_time")
        self.message_auto_delete_time = message_auto_delete_time

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this MessageAutoDeleteTimerChanged to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(MessageAutoDeleteTimerChanged, self).to_array()

        array['message_auto_delete_time'] = int(self.message_auto_delete_time)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the MessageAutoDeleteTimerChanged constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ServiceMessage.validate_array(array)
        data['message_auto_delete_time'] = int(array.get('message_auto_delete_time'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new MessageAutoDeleteTimerChanged from a given dictionary.

        :return: new MessageAutoDeleteTimerChanged instance.
        :rtype: MessageAutoDeleteTimerChanged
        """
        if not array:  # None or {}
            return None
        # end if

        data = MessageAutoDeleteTimerChanged.validate_array(array)
        data['_raw'] = array
        return MessageAutoDeleteTimerChanged(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(messageautodeletetimerchanged_instance)`
        """
        return "MessageAutoDeleteTimerChanged(message_auto_delete_time={self.message_auto_delete_time!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(messageautodeletetimerchanged_instance)`
        """
        if self._raw:
            return "MessageAutoDeleteTimerChanged.from_array({self._raw})".format(self=self)
        # end if
        return "MessageAutoDeleteTimerChanged(message_auto_delete_time={self.message_auto_delete_time!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in messageautodeletetimerchanged_instance`
        """
        return (
            key in ["message_auto_delete_time"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class MessageAutoDeleteTimerChanged


class VoiceChatScheduled(ServiceMessage):
    """
    This object represents a service message about a voice chat scheduled in the chat.

    https://core.telegram.org/bots/api#voicechatscheduled


    Parameters:

    :param start_date: Point in time (Unix timestamp) when the voice chat is supposed to be started by a chat administrator
    :type  start_date: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, start_date, _raw=None):
        """
        This object represents a service message about a voice chat scheduled in the chat.

        https://core.telegram.org/bots/api#voicechatscheduled


        Parameters:

        :param start_date: Point in time (Unix timestamp) when the voice chat is supposed to be started by a chat administrator
        :type  start_date: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(VoiceChatScheduled, self).__init__()
        assert_type_or_raise(start_date, int, parameter_name="start_date")
        self.start_date = start_date

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this VoiceChatScheduled to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(VoiceChatScheduled, self).to_array()

        array['start_date'] = int(self.start_date)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VoiceChatScheduled constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ServiceMessage.validate_array(array)
        data['start_date'] = int(array.get('start_date'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VoiceChatScheduled from a given dictionary.

        :return: new VoiceChatScheduled instance.
        :rtype: VoiceChatScheduled
        """
        if not array:  # None or {}
            return None
        # end if

        data = VoiceChatScheduled.validate_array(array)
        data['_raw'] = array
        return VoiceChatScheduled(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voicechatscheduled_instance)`
        """
        return "VoiceChatScheduled(start_date={self.start_date!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(voicechatscheduled_instance)`
        """
        if self._raw:
            return "VoiceChatScheduled.from_array({self._raw})".format(self=self)
        # end if
        return "VoiceChatScheduled(start_date={self.start_date!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in voicechatscheduled_instance`
        """
        return (
            key in ["start_date"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VoiceChatScheduled


class VoiceChatStarted(ServiceMessage):
    """
    This object represents a service message about a voice chat started in the chat. Currently holds no information.

    https://core.telegram.org/bots/api#voicechatstarted

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, _raw=None):
        """
        This object represents a service message about a voice chat started in the chat. Currently holds no information.

        https://core.telegram.org/bots/api#voicechatstarted

        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(VoiceChatStarted, self).__init__()

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this VoiceChatStarted to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(VoiceChatStarted, self).to_array()

        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VoiceChatStarted constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ServiceMessage.validate_array(array)
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VoiceChatStarted from a given dictionary.

        :return: new VoiceChatStarted instance.
        :rtype: VoiceChatStarted
        """
        if not array:  # None or {}
            return None
        # end if

        data = VoiceChatStarted.validate_array(array)
        data['_raw'] = array
        return VoiceChatStarted(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voicechatstarted_instance)`
        """
        return "VoiceChatStarted()".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(voicechatstarted_instance)`
        """
        if self._raw:
            return "VoiceChatStarted.from_array({self._raw})".format(self=self)
        # end if
        return "VoiceChatStarted()".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in voicechatstarted_instance`
        """
        return (
            key in []
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VoiceChatStarted


class VoiceChatEnded(ServiceMessage):
    """
    This object represents a service message about a voice chat ended in the chat.

    https://core.telegram.org/bots/api#voicechatended


    Parameters:

    :param duration: Voice chat duration in seconds
    :type  duration: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, duration, _raw=None):
        """
        This object represents a service message about a voice chat ended in the chat.

        https://core.telegram.org/bots/api#voicechatended


        Parameters:

        :param duration: Voice chat duration in seconds
        :type  duration: int


        Optional keyword parameters:

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(VoiceChatEnded, self).__init__()
        assert_type_or_raise(duration, int, parameter_name="duration")
        self.duration = duration

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this VoiceChatEnded to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        array = super(VoiceChatEnded, self).to_array()

        array['duration'] = int(self.duration)  # type int
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VoiceChatEnded constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        data = ServiceMessage.validate_array(array)
        data['duration'] = int(array.get('duration'))
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VoiceChatEnded from a given dictionary.

        :return: new VoiceChatEnded instance.
        :rtype: VoiceChatEnded
        """
        if not array:  # None or {}
            return None
        # end if

        data = VoiceChatEnded.validate_array(array)
        data['_raw'] = array
        return VoiceChatEnded(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voicechatended_instance)`
        """
        return "VoiceChatEnded(duration={self.duration!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(voicechatended_instance)`
        """
        if self._raw:
            return "VoiceChatEnded.from_array({self._raw})".format(self=self)
        # end if
        return "VoiceChatEnded(duration={self.duration!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in voicechatended_instance`
        """
        return (
            key in ["duration"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VoiceChatEnded


class VoiceChatParticipantsInvited(ServiceMessage):
    """
    This object represents a service message about new members invited to a voice chat.

    https://core.telegram.org/bots/api#voicechatparticipantsinvited

    Optional keyword parameters:

    :param users: Optional. New members that were invited to the voice chat.
    :type  users: list of pytgbot.api_types.receivable.peer.User

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """

    def __init__(self, users=None, _raw=None):
        """
        This object represents a service message about new members invited to a voice chat.

        https://core.telegram.org/bots/api#voicechatparticipantsinvited

        Optional keyword parameters:

        :param users: Optional. New members that were invited to the voice chat.
        :type  users: list of pytgbot.api_types.receivable.peer.User

        :param _raw: Optional. Original data this object was generated from. Could be `None`.
        :type  _raw: None | dict
        """
        super(VoiceChatParticipantsInvited, self).__init__()
        from .peer import User
        assert_type_or_raise(users, None, list, parameter_name="users")
        self.users = users

        self._raw = _raw
    # end def __init__

    def to_array(self, prefer_original=False):
        """
        Serializes this VoiceChatParticipantsInvited to a dictionary.

        :param prefer_original: If we should return the data this was constructed with if available. If it's not available, it will be constructed normally from the data of the object.
        :type  prefer_original: bool

        :return: dictionary representation of this object.
        :rtype: dict
        """
        if prefer_original and self._raw:
            return self._raw
        # end if

        from .peer import User
        array = super(VoiceChatParticipantsInvited, self).to_array()

        if self.users is not None:
            array['users'] = self._as_array(self.users)  # type list of User
        # end if
        return array
    # end def to_array

    @staticmethod
    def validate_array(array):
        """
        Builds a new array with valid values for the VoiceChatParticipantsInvited constructor.

        :return: new array with valid values
        :rtype: dict
        """
        assert_type_or_raise(array, dict, parameter_name="array")
        from .peer import User
        data = ServiceMessage.validate_array(array)
        data['users'] = User.from_array_list(array.get('users'), list_level=1) if array.get('users') is not None else None
        return data
    # end def validate_array

    @staticmethod
    def from_array(array):
        """
        Deserialize a new VoiceChatParticipantsInvited from a given dictionary.

        :return: new VoiceChatParticipantsInvited instance.
        :rtype: VoiceChatParticipantsInvited
        """
        if not array:  # None or {}
            return None
        # end if

        data = VoiceChatParticipantsInvited.validate_array(array)
        data['_raw'] = array
        return VoiceChatParticipantsInvited(**data)
    # end def from_array

    def __str__(self):
        """
        Implements `str(voicechatparticipantsinvited_instance)`
        """
        return "VoiceChatParticipantsInvited(users={self.users!r})".format(self=self)
    # end def __str__

    def __repr__(self):
        """
        Implements `repr(voicechatparticipantsinvited_instance)`
        """
        if self._raw:
            return "VoiceChatParticipantsInvited.from_array({self._raw})".format(self=self)
        # end if
        return "VoiceChatParticipantsInvited(users={self.users!r})".format(self=self)
    # end def __repr__

    def __contains__(self, key):
        """
        Implements `"key" in voicechatparticipantsinvited_instance`
        """
        return (
            key in ["users"]
            and hasattr(self, key)
            and bool(getattr(self, key, None))
        )
    # end def __contains__
# end class VoiceChatParticipantsInvited
