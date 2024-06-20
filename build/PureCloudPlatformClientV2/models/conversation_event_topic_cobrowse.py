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
    from . import ConversationEventTopicAddress
    from . import ConversationEventTopicAfterCallWork
    from . import ConversationEventTopicQueueMediaSettings
    from . import ConversationEventTopicWrapup

class ConversationEventTopicCobrowse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationEventTopicCobrowse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'initial_state': 'str',
            'disconnect_type': 'str',
            'id': 'str',
            'pcSelf': 'ConversationEventTopicAddress',
            'room_id': 'str',
            'cobrowse_session_id': 'str',
            'cobrowse_role': 'str',
            'controlling': 'list[str]',
            'viewer_url': 'str',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'provider_event_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'wrapup': 'ConversationEventTopicWrapup',
            'after_call_work': 'ConversationEventTopicAfterCallWork',
            'after_call_work_required': 'bool',
            'queue_media_settings': 'ConversationEventTopicQueueMediaSettings'
        }

        self.attribute_map = {
            'state': 'state',
            'initial_state': 'initialState',
            'disconnect_type': 'disconnectType',
            'id': 'id',
            'pcSelf': 'self',
            'room_id': 'roomId',
            'cobrowse_session_id': 'cobrowseSessionId',
            'cobrowse_role': 'cobrowseRole',
            'controlling': 'controlling',
            'viewer_url': 'viewerUrl',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'provider_event_time': 'providerEventTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired',
            'queue_media_settings': 'queueMediaSettings'
        }

        self._state = None
        self._initial_state = None
        self._disconnect_type = None
        self._id = None
        self._pcSelf = None
        self._room_id = None
        self._cobrowse_session_id = None
        self._cobrowse_role = None
        self._controlling = None
        self._viewer_url = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._provider_event_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None
        self._queue_media_settings = None

    @property
    def state(self) -> str:
        """
        Gets the state of this ConversationEventTopicCobrowse.


        :return: The state of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this ConversationEventTopicCobrowse.


        :param state: The state of this ConversationEventTopicCobrowse.
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
        Gets the initial_state of this ConversationEventTopicCobrowse.


        :return: The initial_state of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state: str) -> None:
        """
        Sets the initial_state of this ConversationEventTopicCobrowse.


        :param initial_state: The initial_state of this ConversationEventTopicCobrowse.
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
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this ConversationEventTopicCobrowse.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this ConversationEventTopicCobrowse.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this ConversationEventTopicCobrowse.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["endpoint", "endpoint.dnd", "client", "system", "timeout", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "transfer.noanswer", "transfer.notavailable", "transfer.dnd", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def id(self) -> str:
        """
        Gets the id of this ConversationEventTopicCobrowse.
        A globally unique identifier for this communication.

        :return: The id of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationEventTopicCobrowse.
        A globally unique identifier for this communication.

        :param id: The id of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._id = id

    @property
    def pcSelf(self) -> 'ConversationEventTopicAddress':
        """
        Gets the pcSelf of this ConversationEventTopicCobrowse.
        Address and name data for a call endpoint.

        :return: The pcSelf of this ConversationEventTopicCobrowse.
        :rtype: ConversationEventTopicAddress
        """
        return self._pcSelf

    @pcSelf.setter
    def pcSelf(self, pcSelf: 'ConversationEventTopicAddress') -> None:
        """
        Sets the pcSelf of this ConversationEventTopicCobrowse.
        Address and name data for a call endpoint.

        :param pcSelf: The pcSelf of this ConversationEventTopicCobrowse.
        :type: ConversationEventTopicAddress
        """
        

        self._pcSelf = pcSelf

    @property
    def room_id(self) -> str:
        """
        Gets the room_id of this ConversationEventTopicCobrowse.
        The room id for the chat.

        :return: The room_id of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id: str) -> None:
        """
        Sets the room_id of this ConversationEventTopicCobrowse.
        The room id for the chat.

        :param room_id: The room_id of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._room_id = room_id

    @property
    def cobrowse_session_id(self) -> str:
        """
        Gets the cobrowse_session_id of this ConversationEventTopicCobrowse.
        The co-browse session ID.

        :return: The cobrowse_session_id of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._cobrowse_session_id

    @cobrowse_session_id.setter
    def cobrowse_session_id(self, cobrowse_session_id: str) -> None:
        """
        Sets the cobrowse_session_id of this ConversationEventTopicCobrowse.
        The co-browse session ID.

        :param cobrowse_session_id: The cobrowse_session_id of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._cobrowse_session_id = cobrowse_session_id

    @property
    def cobrowse_role(self) -> str:
        """
        Gets the cobrowse_role of this ConversationEventTopicCobrowse.
        This value identifies the role of the co-browse client within the co-browse session (a client is a sharer or a viewer).

        :return: The cobrowse_role of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._cobrowse_role

    @cobrowse_role.setter
    def cobrowse_role(self, cobrowse_role: str) -> None:
        """
        Sets the cobrowse_role of this ConversationEventTopicCobrowse.
        This value identifies the role of the co-browse client within the co-browse session (a client is a sharer or a viewer).

        :param cobrowse_role: The cobrowse_role of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._cobrowse_role = cobrowse_role

    @property
    def controlling(self) -> List[str]:
        """
        Gets the controlling of this ConversationEventTopicCobrowse.
        ID of co-browse participants for which this client has been granted control (list is empty if this client cannot control any shared pages).

        :return: The controlling of this ConversationEventTopicCobrowse.
        :rtype: list[str]
        """
        return self._controlling

    @controlling.setter
    def controlling(self, controlling: List[str]) -> None:
        """
        Sets the controlling of this ConversationEventTopicCobrowse.
        ID of co-browse participants for which this client has been granted control (list is empty if this client cannot control any shared pages).

        :param controlling: The controlling of this ConversationEventTopicCobrowse.
        :type: list[str]
        """
        

        self._controlling = controlling

    @property
    def viewer_url(self) -> str:
        """
        Gets the viewer_url of this ConversationEventTopicCobrowse.
        The URL that can be used to open co-browse session in web browser.

        :return: The viewer_url of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._viewer_url

    @viewer_url.setter
    def viewer_url(self, viewer_url: str) -> None:
        """
        Sets the viewer_url of this ConversationEventTopicCobrowse.
        The URL that can be used to open co-browse session in web browser.

        :param viewer_url: The viewer_url of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._viewer_url = viewer_url

    @property
    def provider(self) -> str:
        """
        Gets the provider of this ConversationEventTopicCobrowse.
        The source provider of the co-browse communication.

        :return: The provider of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this ConversationEventTopicCobrowse.
        The source provider of the co-browse communication.

        :param provider: The provider of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._provider = provider

    @property
    def script_id(self) -> str:
        """
        Gets the script_id of this ConversationEventTopicCobrowse.
        The UUID of the script to use.

        :return: The script_id of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: str) -> None:
        """
        Sets the script_id of this ConversationEventTopicCobrowse.
        The UUID of the script to use.

        :param script_id: The script_id of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._script_id = script_id

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this ConversationEventTopicCobrowse.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this ConversationEventTopicCobrowse.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this ConversationEventTopicCobrowse.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this ConversationEventTopicCobrowse.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def provider_event_time(self) -> datetime:
        """
        Gets the provider_event_time of this ConversationEventTopicCobrowse.
        The time when the provider event which triggered this conversation update happened in the corrected provider clock (milliseconds since 1970-01-01 00:00:00 UTC).

        :return: The provider_event_time of this ConversationEventTopicCobrowse.
        :rtype: datetime
        """
        return self._provider_event_time

    @provider_event_time.setter
    def provider_event_time(self, provider_event_time: datetime) -> None:
        """
        Sets the provider_event_time of this ConversationEventTopicCobrowse.
        The time when the provider event which triggered this conversation update happened in the corrected provider clock (milliseconds since 1970-01-01 00:00:00 UTC).

        :param provider_event_time: The provider_event_time of this ConversationEventTopicCobrowse.
        :type: datetime
        """
        

        self._provider_event_time = provider_event_time

    @property
    def connected_time(self) -> datetime:
        """
        Gets the connected_time of this ConversationEventTopicCobrowse.
        The timestamp when this communication was connected in the cloud clock.

        :return: The connected_time of this ConversationEventTopicCobrowse.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time: datetime) -> None:
        """
        Sets the connected_time of this ConversationEventTopicCobrowse.
        The timestamp when this communication was connected in the cloud clock.

        :param connected_time: The connected_time of this ConversationEventTopicCobrowse.
        :type: datetime
        """
        

        self._connected_time = connected_time

    @property
    def disconnected_time(self) -> datetime:
        """
        Gets the disconnected_time of this ConversationEventTopicCobrowse.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :return: The disconnected_time of this ConversationEventTopicCobrowse.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time: datetime) -> None:
        """
        Sets the disconnected_time of this ConversationEventTopicCobrowse.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :param disconnected_time: The disconnected_time of this ConversationEventTopicCobrowse.
        :type: datetime
        """
        

        self._disconnected_time = disconnected_time

    @property
    def wrapup(self) -> 'ConversationEventTopicWrapup':
        """
        Gets the wrapup of this ConversationEventTopicCobrowse.
        Call wrap up or disposition data.

        :return: The wrapup of this ConversationEventTopicCobrowse.
        :rtype: ConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'ConversationEventTopicWrapup') -> None:
        """
        Sets the wrapup of this ConversationEventTopicCobrowse.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this ConversationEventTopicCobrowse.
        :type: ConversationEventTopicWrapup
        """
        

        self._wrapup = wrapup

    @property
    def after_call_work(self) -> 'ConversationEventTopicAfterCallWork':
        """
        Gets the after_call_work of this ConversationEventTopicCobrowse.
        A communication's after-call work data.

        :return: The after_call_work of this ConversationEventTopicCobrowse.
        :rtype: ConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work: 'ConversationEventTopicAfterCallWork') -> None:
        """
        Sets the after_call_work of this ConversationEventTopicCobrowse.
        A communication's after-call work data.

        :param after_call_work: The after_call_work of this ConversationEventTopicCobrowse.
        :type: ConversationEventTopicAfterCallWork
        """
        

        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self) -> bool:
        """
        Gets the after_call_work_required of this ConversationEventTopicCobrowse.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this ConversationEventTopicCobrowse.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required: bool) -> None:
        """
        Sets the after_call_work_required of this ConversationEventTopicCobrowse.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this ConversationEventTopicCobrowse.
        :type: bool
        """
        

        self._after_call_work_required = after_call_work_required

    @property
    def queue_media_settings(self) -> 'ConversationEventTopicQueueMediaSettings':
        """
        Gets the queue_media_settings of this ConversationEventTopicCobrowse.
        Represents the queue setting for this media.

        :return: The queue_media_settings of this ConversationEventTopicCobrowse.
        :rtype: ConversationEventTopicQueueMediaSettings
        """
        return self._queue_media_settings

    @queue_media_settings.setter
    def queue_media_settings(self, queue_media_settings: 'ConversationEventTopicQueueMediaSettings') -> None:
        """
        Sets the queue_media_settings of this ConversationEventTopicCobrowse.
        Represents the queue setting for this media.

        :param queue_media_settings: The queue_media_settings of this ConversationEventTopicCobrowse.
        :type: ConversationEventTopicQueueMediaSettings
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

