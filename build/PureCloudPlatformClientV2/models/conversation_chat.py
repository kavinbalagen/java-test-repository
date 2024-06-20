# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import AfterCallWork
    from . import ConversationQueueMediaSettings
    from . import JourneyContext
    from . import Segment
    from . import Wrapup

class ConversationChat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationChat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'initial_state': 'str',
            'id': 'str',
            'room_id': 'str',
            'recording_id': 'str',
            'segments': 'list[Segment]',
            'held': 'bool',
            'direction': 'str',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'start_alerting_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'avatar_image_url': 'str',
            'journey_context': 'JourneyContext',
            'wrapup': 'Wrapup',
            'after_call_work': 'AfterCallWork',
            'after_call_work_required': 'bool',
            'queue_media_settings': 'ConversationQueueMediaSettings'
        }

        self.attribute_map = {
            'state': 'state',
            'initial_state': 'initialState',
            'id': 'id',
            'room_id': 'roomId',
            'recording_id': 'recordingId',
            'segments': 'segments',
            'held': 'held',
            'direction': 'direction',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'start_alerting_time': 'startAlertingTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'avatar_image_url': 'avatarImageUrl',
            'journey_context': 'journeyContext',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'queue_media_settings': 'queueMediaSettings'
        }

        self._state = None
        self._initial_state = None
        self._id = None
        self._room_id = None
        self._recording_id = None
        self._segments = None
        self._held = None
        self._direction = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._start_alerting_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._avatar_image_url = None
        self._journey_context = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._queue_media_settings = None

    @property
    def state(self) -> str:
        """
        Gets the state of this ConversationChat.
        The connection state of this communication.

        :return: The state of this ConversationChat.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this ConversationChat.
        The connection state of this communication.

        :param state: The state of this ConversationChat.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def initial_state(self) -> str:
        """
        Gets the initial_state of this ConversationChat.
        The initial connection state of this communication.

        :return: The initial_state of this ConversationChat.
        :rtype: str
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state: str) -> None:
        """
        Sets the initial_state of this ConversationChat.
        The initial connection state of this communication.

        :param initial_state: The initial_state of this ConversationChat.
        :type: str
        """
        if isinstance(initial_state, int):
            initial_state = str(initial_state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "none"]
        if initial_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for initial_state -> " + initial_state)
            self._initial_state = "outdated_sdk_version"
        else:
            self._initial_state = initial_state

    @property
    def id(self) -> str:
        """
        Gets the id of this ConversationChat.
        A globally unique identifier for this communication.

        :return: The id of this ConversationChat.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationChat.
        A globally unique identifier for this communication.

        :param id: The id of this ConversationChat.
        :type: str
        """
        

        self._id = id

    @property
    def room_id(self) -> str:
        """
        Gets the room_id of this ConversationChat.
        The room id for the chat.

        :return: The room_id of this ConversationChat.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id: str) -> None:
        """
        Sets the room_id of this ConversationChat.
        The room id for the chat.

        :param room_id: The room_id of this ConversationChat.
        :type: str
        """
        

        self._room_id = room_id

    @property
    def recording_id(self) -> str:
        """
        Gets the recording_id of this ConversationChat.
        A globally unique identifier for the recording associated with this chat.

        :return: The recording_id of this ConversationChat.
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id: str) -> None:
        """
        Sets the recording_id of this ConversationChat.
        A globally unique identifier for the recording associated with this chat.

        :param recording_id: The recording_id of this ConversationChat.
        :type: str
        """
        

        self._recording_id = recording_id

    @property
    def segments(self) -> List['Segment']:
        """
        Gets the segments of this ConversationChat.
        The time line of the participant's chat, divided into activity segments.

        :return: The segments of this ConversationChat.
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments: List['Segment']) -> None:
        """
        Sets the segments of this ConversationChat.
        The time line of the participant's chat, divided into activity segments.

        :param segments: The segments of this ConversationChat.
        :type: list[Segment]
        """
        

        self._segments = segments

    @property
    def held(self) -> bool:
        """
        Gets the held of this ConversationChat.
        True if this call is held and the person on this side hears silence.

        :return: The held of this ConversationChat.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held: bool) -> None:
        """
        Sets the held of this ConversationChat.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this ConversationChat.
        :type: bool
        """
        

        self._held = held

    @property
    def direction(self) -> str:
        """
        Gets the direction of this ConversationChat.
        The direction of the chat

        :return: The direction of this ConversationChat.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this ConversationChat.
        The direction of the chat

        :param direction: The direction of this ConversationChat.
        :type: str
        """
        if isinstance(direction, int):
            direction = str(direction)
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this ConversationChat.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this ConversationChat.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this ConversationChat.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this ConversationChat.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["endpoint", "client", "system", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "error", "peer", "other", "uncallable", "timeout"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def start_hold_time(self) -> datetime:
        """
        Gets the start_hold_time of this ConversationChat.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_hold_time of this ConversationChat.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time: datetime) -> None:
        """
        Sets the start_hold_time of this ConversationChat.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_hold_time: The start_hold_time of this ConversationChat.
        :type: datetime
        """
        

        self._start_hold_time = start_hold_time

    @property
    def start_alerting_time(self) -> datetime:
        """
        Gets the start_alerting_time of this ConversationChat.
        The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_alerting_time of this ConversationChat.
        :rtype: datetime
        """
        return self._start_alerting_time

    @start_alerting_time.setter
    def start_alerting_time(self, start_alerting_time: datetime) -> None:
        """
        Sets the start_alerting_time of this ConversationChat.
        The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_alerting_time: The start_alerting_time of this ConversationChat.
        :type: datetime
        """
        

        self._start_alerting_time = start_alerting_time

    @property
    def connected_time(self) -> datetime:
        """
        Gets the connected_time of this ConversationChat.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The connected_time of this ConversationChat.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time: datetime) -> None:
        """
        Sets the connected_time of this ConversationChat.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param connected_time: The connected_time of this ConversationChat.
        :type: datetime
        """
        

        self._connected_time = connected_time

    @property
    def disconnected_time(self) -> datetime:
        """
        Gets the disconnected_time of this ConversationChat.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The disconnected_time of this ConversationChat.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time: datetime) -> None:
        """
        Sets the disconnected_time of this ConversationChat.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param disconnected_time: The disconnected_time of this ConversationChat.
        :type: datetime
        """
        

        self._disconnected_time = disconnected_time

    @property
    def provider(self) -> str:
        """
        Gets the provider of this ConversationChat.
        The source provider for the email.

        :return: The provider of this ConversationChat.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this ConversationChat.
        The source provider for the email.

        :param provider: The provider of this ConversationChat.
        :type: str
        """
        

        self._provider = provider

    @property
    def script_id(self) -> str:
        """
        Gets the script_id of this ConversationChat.
        The UUID of the script to use.

        :return: The script_id of this ConversationChat.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: str) -> None:
        """
        Sets the script_id of this ConversationChat.
        The UUID of the script to use.

        :param script_id: The script_id of this ConversationChat.
        :type: str
        """
        

        self._script_id = script_id

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this ConversationChat.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this ConversationChat.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this ConversationChat.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this ConversationChat.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def avatar_image_url(self) -> str:
        """
        Gets the avatar_image_url of this ConversationChat.
        If available, the URI to the avatar image of this communication.

        :return: The avatar_image_url of this ConversationChat.
        :rtype: str
        """
        return self._avatar_image_url

    @avatar_image_url.setter
    def avatar_image_url(self, avatar_image_url: str) -> None:
        """
        Sets the avatar_image_url of this ConversationChat.
        If available, the URI to the avatar image of this communication.

        :param avatar_image_url: The avatar_image_url of this ConversationChat.
        :type: str
        """
        

        self._avatar_image_url = avatar_image_url

    @property
    def journey_context(self) -> 'JourneyContext':
        """
        Gets the journey_context of this ConversationChat.
        A subset of the Journey System's data relevant to a part of a conversation (for external linkage and internal usage/context).

        :return: The journey_context of this ConversationChat.
        :rtype: JourneyContext
        """
        return self._journey_context

    @journey_context.setter
    def journey_context(self, journey_context: 'JourneyContext') -> None:
        """
        Sets the journey_context of this ConversationChat.
        A subset of the Journey System's data relevant to a part of a conversation (for external linkage and internal usage/context).

        :param journey_context: The journey_context of this ConversationChat.
        :type: JourneyContext
        """
        

        self._journey_context = journey_context

    @property
    def wrapup(self) -> 'Wrapup':
        """
        Gets the wrapup of this ConversationChat.
        Call wrap up or disposition data.

        :return: The wrapup of this ConversationChat.
        :rtype: Wrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'Wrapup') -> None:
        """
        Sets the wrapup of this ConversationChat.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this ConversationChat.
        :type: Wrapup
        """
        

        self._wrapup = wrapup

    @property
    def after_call_work(self) -> 'AfterCallWork':
        """
        Gets the after_call_work of this ConversationChat.
        After-call work for the communication.

        :return: The after_call_work of this ConversationChat.
        :rtype: AfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work: 'AfterCallWork') -> None:
        """
        Sets the after_call_work of this ConversationChat.
        After-call work for the communication.

        :param after_call_work: The after_call_work of this ConversationChat.
        :type: AfterCallWork
        """
        

        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self) -> bool:
        """
        Gets the after_call_work_required of this ConversationChat.
        Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this ConversationChat.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required: bool) -> None:
        """
        Sets the after_call_work_required of this ConversationChat.
        Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this ConversationChat.
        :type: bool
        """
        

        self._after_call_work_required = after_call_work_required

    @property
    def queue_media_settings(self) -> 'ConversationQueueMediaSettings':
        """
        Gets the queue_media_settings of this ConversationChat.
        Represents the queue settings for this media type.

        :return: The queue_media_settings of this ConversationChat.
        :rtype: ConversationQueueMediaSettings
        """
        return self._queue_media_settings

    @queue_media_settings.setter
    def queue_media_settings(self, queue_media_settings: 'ConversationQueueMediaSettings') -> None:
        """
        Sets the queue_media_settings of this ConversationChat.
        Represents the queue settings for this media type.

        :param queue_media_settings: The queue_media_settings of this ConversationChat.
        :type: ConversationQueueMediaSettings
        """
        

        self._queue_media_settings = queue_media_settings

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

