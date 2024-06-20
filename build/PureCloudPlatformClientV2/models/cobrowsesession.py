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
    from . import Address
    from . import AfterCallWork
    from . import Segment
    from . import Wrapup

class Cobrowsesession(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Cobrowsesession - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'initial_state': 'str',
            'id': 'str',
            'disconnect_type': 'str',
            'pcSelf': 'Address',
            'cobrowse_session_id': 'str',
            'cobrowse_role': 'str',
            'controlling': 'list[str]',
            'viewer_url': 'str',
            'provider_event_time': 'datetime',
            'start_alerting_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'provider': 'str',
            'peer_id': 'str',
            'segments': 'list[Segment]',
            'wrapup': 'Wrapup',
            'after_call_work': 'AfterCallWork',
            'after_call_work_required': 'bool'
        }

        self.attribute_map = {
            'state': 'state',
            'initial_state': 'initialState',
            'id': 'id',
            'disconnect_type': 'disconnectType',
            'pcSelf': 'self',
            'cobrowse_session_id': 'cobrowseSessionId',
            'cobrowse_role': 'cobrowseRole',
            'controlling': 'controlling',
            'viewer_url': 'viewerUrl',
            'provider_event_time': 'providerEventTime',
            'start_alerting_time': 'startAlertingTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'provider': 'provider',
            'peer_id': 'peerId',
            'segments': 'segments',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired'
        }

        self._state = None
        self._initial_state = None
        self._id = None
        self._disconnect_type = None
        self._pcSelf = None
        self._cobrowse_session_id = None
        self._cobrowse_role = None
        self._controlling = None
        self._viewer_url = None
        self._provider_event_time = None
        self._start_alerting_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._provider = None
        self._peer_id = None
        self._segments = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None

    @property
    def state(self) -> str:
        """
        Gets the state of this Cobrowsesession.
        The connection state of this communication.

        :return: The state of this Cobrowsesession.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this Cobrowsesession.
        The connection state of this communication.

        :param state: The state of this Cobrowsesession.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "scheduled", "none"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def initial_state(self) -> str:
        """
        Gets the initial_state of this Cobrowsesession.
        The initial connection state of this communication.

        :return: The initial_state of this Cobrowsesession.
        :rtype: str
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state: str) -> None:
        """
        Sets the initial_state of this Cobrowsesession.
        The initial connection state of this communication.

        :param initial_state: The initial_state of this Cobrowsesession.
        :type: str
        """
        if isinstance(initial_state, int):
            initial_state = str(initial_state)
        allowed_values = ["alerting", "dialing", "contacting", "offering", "connected", "disconnected", "terminated", "scheduled", "none"]
        if initial_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for initial_state -> " + initial_state)
            self._initial_state = "outdated_sdk_version"
        else:
            self._initial_state = initial_state

    @property
    def id(self) -> str:
        """
        Gets the id of this Cobrowsesession.
        A globally unique identifier for this communication.

        :return: The id of this Cobrowsesession.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Cobrowsesession.
        A globally unique identifier for this communication.

        :param id: The id of this Cobrowsesession.
        :type: str
        """
        

        self._id = id

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this Cobrowsesession.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this Cobrowsesession.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this Cobrowsesession.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this Cobrowsesession.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["endpoint", "client", "system", "timeout", "transfer", "transfer.conference", "transfer.consult", "transfer.forward", "transport.failure", "error", "peer", "other", "spam", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def pcSelf(self) -> 'Address':
        """
        Gets the pcSelf of this Cobrowsesession.
        Address and name data for a call endpoint.

        :return: The pcSelf of this Cobrowsesession.
        :rtype: Address
        """
        return self._pcSelf

    @pcSelf.setter
    def pcSelf(self, pcSelf: 'Address') -> None:
        """
        Sets the pcSelf of this Cobrowsesession.
        Address and name data for a call endpoint.

        :param pcSelf: The pcSelf of this Cobrowsesession.
        :type: Address
        """
        

        self._pcSelf = pcSelf

    @property
    def cobrowse_session_id(self) -> str:
        """
        Gets the cobrowse_session_id of this Cobrowsesession.
        The co-browse session ID.

        :return: The cobrowse_session_id of this Cobrowsesession.
        :rtype: str
        """
        return self._cobrowse_session_id

    @cobrowse_session_id.setter
    def cobrowse_session_id(self, cobrowse_session_id: str) -> None:
        """
        Sets the cobrowse_session_id of this Cobrowsesession.
        The co-browse session ID.

        :param cobrowse_session_id: The cobrowse_session_id of this Cobrowsesession.
        :type: str
        """
        

        self._cobrowse_session_id = cobrowse_session_id

    @property
    def cobrowse_role(self) -> str:
        """
        Gets the cobrowse_role of this Cobrowsesession.
        This value identifies the role of the co-browse client within the co-browse session (a client is a sharer or a viewer).

        :return: The cobrowse_role of this Cobrowsesession.
        :rtype: str
        """
        return self._cobrowse_role

    @cobrowse_role.setter
    def cobrowse_role(self, cobrowse_role: str) -> None:
        """
        Sets the cobrowse_role of this Cobrowsesession.
        This value identifies the role of the co-browse client within the co-browse session (a client is a sharer or a viewer).

        :param cobrowse_role: The cobrowse_role of this Cobrowsesession.
        :type: str
        """
        

        self._cobrowse_role = cobrowse_role

    @property
    def controlling(self) -> List[str]:
        """
        Gets the controlling of this Cobrowsesession.
        ID of co-browse participants for which this client has been granted control (list is empty if this client cannot control any shared pages).

        :return: The controlling of this Cobrowsesession.
        :rtype: list[str]
        """
        return self._controlling

    @controlling.setter
    def controlling(self, controlling: List[str]) -> None:
        """
        Sets the controlling of this Cobrowsesession.
        ID of co-browse participants for which this client has been granted control (list is empty if this client cannot control any shared pages).

        :param controlling: The controlling of this Cobrowsesession.
        :type: list[str]
        """
        

        self._controlling = controlling

    @property
    def viewer_url(self) -> str:
        """
        Gets the viewer_url of this Cobrowsesession.
        The URL that can be used to open co-browse session in web browser.

        :return: The viewer_url of this Cobrowsesession.
        :rtype: str
        """
        return self._viewer_url

    @viewer_url.setter
    def viewer_url(self, viewer_url: str) -> None:
        """
        Sets the viewer_url of this Cobrowsesession.
        The URL that can be used to open co-browse session in web browser.

        :param viewer_url: The viewer_url of this Cobrowsesession.
        :type: str
        """
        

        self._viewer_url = viewer_url

    @property
    def provider_event_time(self) -> datetime:
        """
        Gets the provider_event_time of this Cobrowsesession.
        The time when the provider event which triggered this conversation update happened in the corrected provider clock (milliseconds since 1970-01-01 00:00:00 UTC). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The provider_event_time of this Cobrowsesession.
        :rtype: datetime
        """
        return self._provider_event_time

    @provider_event_time.setter
    def provider_event_time(self, provider_event_time: datetime) -> None:
        """
        Sets the provider_event_time of this Cobrowsesession.
        The time when the provider event which triggered this conversation update happened in the corrected provider clock (milliseconds since 1970-01-01 00:00:00 UTC). Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param provider_event_time: The provider_event_time of this Cobrowsesession.
        :type: datetime
        """
        

        self._provider_event_time = provider_event_time

    @property
    def start_alerting_time(self) -> datetime:
        """
        Gets the start_alerting_time of this Cobrowsesession.
        The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_alerting_time of this Cobrowsesession.
        :rtype: datetime
        """
        return self._start_alerting_time

    @start_alerting_time.setter
    def start_alerting_time(self, start_alerting_time: datetime) -> None:
        """
        Sets the start_alerting_time of this Cobrowsesession.
        The timestamp the communication has when it is first put into an alerting state. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_alerting_time: The start_alerting_time of this Cobrowsesession.
        :type: datetime
        """
        

        self._start_alerting_time = start_alerting_time

    @property
    def connected_time(self) -> datetime:
        """
        Gets the connected_time of this Cobrowsesession.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The connected_time of this Cobrowsesession.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time: datetime) -> None:
        """
        Sets the connected_time of this Cobrowsesession.
        The timestamp when this communication was connected in the cloud clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param connected_time: The connected_time of this Cobrowsesession.
        :type: datetime
        """
        

        self._connected_time = connected_time

    @property
    def disconnected_time(self) -> datetime:
        """
        Gets the disconnected_time of this Cobrowsesession.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The disconnected_time of this Cobrowsesession.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time: datetime) -> None:
        """
        Sets the disconnected_time of this Cobrowsesession.
        The timestamp when this communication disconnected from the conversation in the provider clock. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param disconnected_time: The disconnected_time of this Cobrowsesession.
        :type: datetime
        """
        

        self._disconnected_time = disconnected_time

    @property
    def provider(self) -> str:
        """
        Gets the provider of this Cobrowsesession.
        The source provider for the co-browse session.

        :return: The provider of this Cobrowsesession.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this Cobrowsesession.
        The source provider for the co-browse session.

        :param provider: The provider of this Cobrowsesession.
        :type: str
        """
        

        self._provider = provider

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this Cobrowsesession.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this Cobrowsesession.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this Cobrowsesession.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this Cobrowsesession.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def segments(self) -> List['Segment']:
        """
        Gets the segments of this Cobrowsesession.
        The time line of the participant's call, divided into activity segments.

        :return: The segments of this Cobrowsesession.
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments: List['Segment']) -> None:
        """
        Sets the segments of this Cobrowsesession.
        The time line of the participant's call, divided into activity segments.

        :param segments: The segments of this Cobrowsesession.
        :type: list[Segment]
        """
        

        self._segments = segments

    @property
    def wrapup(self) -> 'Wrapup':
        """
        Gets the wrapup of this Cobrowsesession.
        Call wrap up or disposition data.

        :return: The wrapup of this Cobrowsesession.
        :rtype: Wrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'Wrapup') -> None:
        """
        Sets the wrapup of this Cobrowsesession.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this Cobrowsesession.
        :type: Wrapup
        """
        

        self._wrapup = wrapup

    @property
    def after_call_work(self) -> 'AfterCallWork':
        """
        Gets the after_call_work of this Cobrowsesession.
        After-call work for the communication.

        :return: The after_call_work of this Cobrowsesession.
        :rtype: AfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work: 'AfterCallWork') -> None:
        """
        Sets the after_call_work of this Cobrowsesession.
        After-call work for the communication.

        :param after_call_work: The after_call_work of this Cobrowsesession.
        :type: AfterCallWork
        """
        

        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self) -> bool:
        """
        Gets the after_call_work_required of this Cobrowsesession.
        Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this Cobrowsesession.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required: bool) -> None:
        """
        Sets the after_call_work_required of this Cobrowsesession.
        Indicates if after-call work is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this Cobrowsesession.
        :type: bool
        """
        

        self._after_call_work_required = after_call_work_required

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

