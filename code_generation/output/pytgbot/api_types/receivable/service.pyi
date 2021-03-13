# -*- coding: utf-8 -*-
from luckydonaldUtils.exceptions import assert_type_or_raise
from luckydonaldUtils.encoding import unicode_type, to_unicode as u
from typing import Any, Union, List
from pytgbot.api_types.receivable.service import ServiceMessage

__author__ = 'luckydonald'


class ServiceMessage(ServiceMessage):
    """
    parent class for all service messages, those are not directly media related special attributes of the Message object.

    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
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
    traveler: User
    watcher: User
    distance: int
# end class ProximityAlertTriggered

class MessageAutoDeleteTimerChanged(ServiceMessage):
    """
    This object represents a service message about a change in auto-delete timer settings.

    https://core.telegram.org/bots/api#messageautodeletetimerchanged


    Parameters:

    :param message_auto_delete_time: New auto-delete time for messages in the chat
    :type  message_auto_delete_time: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    message_auto_delete_time: int
# end class MessageAutoDeleteTimerChanged

class VoiceChatEnded(ServiceMessage):
    """
    This object represents a service message about a voice chat ended in the chat.

    https://core.telegram.org/bots/api#voicechatended


    Parameters:

    :param duration: Voice chat duration; in seconds
    :type  duration: int


    Optional keyword parameters:

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    duration: int
# end class VoiceChatEnded

class VoiceChatParticipantsInvited(ServiceMessage):
    """
    This object represents a service message about new members invited to a voice chat.

    https://core.telegram.org/bots/api#voicechatparticipantsinvited

    Optional keyword parameters:

    :param users: Optional. New members that were invited to the voice chat
    :type  users: list of pytgbot.api_types.receivable.peer.User

    :param _raw: Optional. Original data this object was generated from. Could be `None`.
    :type  _raw: None | dict
    """
    users: List[User]
# end class VoiceChatParticipantsInvited
