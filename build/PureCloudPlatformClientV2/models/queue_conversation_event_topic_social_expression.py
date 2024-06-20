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
    from . import QueueConversationEventTopicAfterCallWork
    from . import QueueConversationEventTopicWrapup

class QueueConversationEventTopicSocialExpression(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationEventTopicSocialExpression - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'state': 'str',
            'initial_state': 'str',
            'id': 'str',
            'social_media_id': 'str',
            'social_media_hub': 'str',
            'social_user_name': 'str',
            'preview_text': 'str',
            'recording_id': 'str',
            'held': 'bool',
            'provider': 'str',
            'script_id': 'str',
            'peer_id': 'str',
            'disconnect_type': 'str',
            'start_hold_time': 'datetime',
            'connected_time': 'datetime',
            'disconnected_time': 'datetime',
            'wrapup': 'QueueConversationEventTopicWrapup',
            'after_call_work': 'QueueConversationEventTopicAfterCallWork',
            'after_call_work_required': 'bool'
        }

        self.attribute_map = {
            'state': 'state',
            'initial_state': 'initialState',
            'id': 'id',
            'social_media_id': 'socialMediaId',
            'social_media_hub': 'socialMediaHub',
            'social_user_name': 'socialUserName',
            'preview_text': 'previewText',
            'recording_id': 'recordingId',
            'held': 'held',
            'provider': 'provider',
            'script_id': 'scriptId',
            'peer_id': 'peerId',
            'disconnect_type': 'disconnectType',
            'start_hold_time': 'startHoldTime',
            'connected_time': 'connectedTime',
            'disconnected_time': 'disconnectedTime',
            'wrapup': 'wrapup',
            'after_call_work': 'afterCallWork',
            'after_call_work_required': 'afterCallWorkRequired'
        }

        self._state = None
        self._initial_state = None
        self._id = None
        self._social_media_id = None
        self._social_media_hub = None
        self._social_user_name = None
        self._preview_text = None
        self._recording_id = None
        self._held = None
        self._provider = None
        self._script_id = None
        self._peer_id = None
        self._disconnect_type = None
        self._start_hold_time = None
        self._connected_time = None
        self._disconnected_time = None
        self._wrapup = None
        self._after_call_work = None
        self._after_call_work_required = None

    @property
    def state(self) -> str:
        """
        Gets the state of this QueueConversationEventTopicSocialExpression.


        :return: The state of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this QueueConversationEventTopicSocialExpression.


        :param state: The state of this QueueConversationEventTopicSocialExpression.
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
        Gets the initial_state of this QueueConversationEventTopicSocialExpression.


        :return: The initial_state of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._initial_state

    @initial_state.setter
    def initial_state(self, initial_state: str) -> None:
        """
        Sets the initial_state of this QueueConversationEventTopicSocialExpression.


        :param initial_state: The initial_state of this QueueConversationEventTopicSocialExpression.
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
        Gets the id of this QueueConversationEventTopicSocialExpression.
        A globally unique identifier for this communication.

        :return: The id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this QueueConversationEventTopicSocialExpression.
        A globally unique identifier for this communication.

        :param id: The id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._id = id

    @property
    def social_media_id(self) -> str:
        """
        Gets the social_media_id of this QueueConversationEventTopicSocialExpression.
        A globally unique identifier for the social media.

        :return: The social_media_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._social_media_id

    @social_media_id.setter
    def social_media_id(self, social_media_id: str) -> None:
        """
        Sets the social_media_id of this QueueConversationEventTopicSocialExpression.
        A globally unique identifier for the social media.

        :param social_media_id: The social_media_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._social_media_id = social_media_id

    @property
    def social_media_hub(self) -> str:
        """
        Gets the social_media_hub of this QueueConversationEventTopicSocialExpression.
        The social network of the communication

        :return: The social_media_hub of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._social_media_hub

    @social_media_hub.setter
    def social_media_hub(self, social_media_hub: str) -> None:
        """
        Sets the social_media_hub of this QueueConversationEventTopicSocialExpression.
        The social network of the communication

        :param social_media_hub: The social_media_hub of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._social_media_hub = social_media_hub

    @property
    def social_user_name(self) -> str:
        """
        Gets the social_user_name of this QueueConversationEventTopicSocialExpression.
        The social media user name of the communication

        :return: The social_user_name of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._social_user_name

    @social_user_name.setter
    def social_user_name(self, social_user_name: str) -> None:
        """
        Sets the social_user_name of this QueueConversationEventTopicSocialExpression.
        The social media user name of the communication

        :param social_user_name: The social_user_name of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._social_user_name = social_user_name

    @property
    def preview_text(self) -> str:
        """
        Gets the preview_text of this QueueConversationEventTopicSocialExpression.
        The text preview of the communication contents

        :return: The preview_text of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._preview_text

    @preview_text.setter
    def preview_text(self, preview_text: str) -> None:
        """
        Sets the preview_text of this QueueConversationEventTopicSocialExpression.
        The text preview of the communication contents

        :param preview_text: The preview_text of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._preview_text = preview_text

    @property
    def recording_id(self) -> str:
        """
        Gets the recording_id of this QueueConversationEventTopicSocialExpression.
        A globally unique identifier for the recording associated with this chat.

        :return: The recording_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id: str) -> None:
        """
        Sets the recording_id of this QueueConversationEventTopicSocialExpression.
        A globally unique identifier for the recording associated with this chat.

        :param recording_id: The recording_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._recording_id = recording_id

    @property
    def held(self) -> bool:
        """
        Gets the held of this QueueConversationEventTopicSocialExpression.
        True if this call is held and the person on this side hears silence.

        :return: The held of this QueueConversationEventTopicSocialExpression.
        :rtype: bool
        """
        return self._held

    @held.setter
    def held(self, held: bool) -> None:
        """
        Sets the held of this QueueConversationEventTopicSocialExpression.
        True if this call is held and the person on this side hears silence.

        :param held: The held of this QueueConversationEventTopicSocialExpression.
        :type: bool
        """
        

        self._held = held

    @property
    def provider(self) -> str:
        """
        Gets the provider of this QueueConversationEventTopicSocialExpression.
        The source provider of the social expression.

        :return: The provider of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this QueueConversationEventTopicSocialExpression.
        The source provider of the social expression.

        :param provider: The provider of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._provider = provider

    @property
    def script_id(self) -> str:
        """
        Gets the script_id of this QueueConversationEventTopicSocialExpression.
        The UUID of the script to use.

        :return: The script_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: str) -> None:
        """
        Sets the script_id of this QueueConversationEventTopicSocialExpression.
        The UUID of the script to use.

        :param script_id: The script_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._script_id = script_id

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this QueueConversationEventTopicSocialExpression.
        The id of the peer communication corresponding to a matching leg for this communication.

        :return: The peer_id of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this QueueConversationEventTopicSocialExpression.
        The id of the peer communication corresponding to a matching leg for this communication.

        :param peer_id: The peer_id of this QueueConversationEventTopicSocialExpression.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this QueueConversationEventTopicSocialExpression.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :return: The disconnect_type of this QueueConversationEventTopicSocialExpression.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this QueueConversationEventTopicSocialExpression.
        System defined string indicating what caused the communication to disconnect. Will be null until the communication disconnects.

        :param disconnect_type: The disconnect_type of this QueueConversationEventTopicSocialExpression.
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
    def start_hold_time(self) -> datetime:
        """
        Gets the start_hold_time of this QueueConversationEventTopicSocialExpression.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold.

        :return: The start_hold_time of this QueueConversationEventTopicSocialExpression.
        :rtype: datetime
        """
        return self._start_hold_time

    @start_hold_time.setter
    def start_hold_time(self, start_hold_time: datetime) -> None:
        """
        Sets the start_hold_time of this QueueConversationEventTopicSocialExpression.
        The timestamp the chat was placed on hold in the cloud clock if the chat is currently on hold.

        :param start_hold_time: The start_hold_time of this QueueConversationEventTopicSocialExpression.
        :type: datetime
        """
        

        self._start_hold_time = start_hold_time

    @property
    def connected_time(self) -> datetime:
        """
        Gets the connected_time of this QueueConversationEventTopicSocialExpression.
        The timestamp when this communication was connected in the cloud clock.

        :return: The connected_time of this QueueConversationEventTopicSocialExpression.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time: datetime) -> None:
        """
        Sets the connected_time of this QueueConversationEventTopicSocialExpression.
        The timestamp when this communication was connected in the cloud clock.

        :param connected_time: The connected_time of this QueueConversationEventTopicSocialExpression.
        :type: datetime
        """
        

        self._connected_time = connected_time

    @property
    def disconnected_time(self) -> datetime:
        """
        Gets the disconnected_time of this QueueConversationEventTopicSocialExpression.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :return: The disconnected_time of this QueueConversationEventTopicSocialExpression.
        :rtype: datetime
        """
        return self._disconnected_time

    @disconnected_time.setter
    def disconnected_time(self, disconnected_time: datetime) -> None:
        """
        Sets the disconnected_time of this QueueConversationEventTopicSocialExpression.
        The timestamp when this communication disconnected from the conversation in the provider clock.

        :param disconnected_time: The disconnected_time of this QueueConversationEventTopicSocialExpression.
        :type: datetime
        """
        

        self._disconnected_time = disconnected_time

    @property
    def wrapup(self) -> 'QueueConversationEventTopicWrapup':
        """
        Gets the wrapup of this QueueConversationEventTopicSocialExpression.
        Call wrap up or disposition data.

        :return: The wrapup of this QueueConversationEventTopicSocialExpression.
        :rtype: QueueConversationEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'QueueConversationEventTopicWrapup') -> None:
        """
        Sets the wrapup of this QueueConversationEventTopicSocialExpression.
        Call wrap up or disposition data.

        :param wrapup: The wrapup of this QueueConversationEventTopicSocialExpression.
        :type: QueueConversationEventTopicWrapup
        """
        

        self._wrapup = wrapup

    @property
    def after_call_work(self) -> 'QueueConversationEventTopicAfterCallWork':
        """
        Gets the after_call_work of this QueueConversationEventTopicSocialExpression.
        A communication's after-call work data.

        :return: The after_call_work of this QueueConversationEventTopicSocialExpression.
        :rtype: QueueConversationEventTopicAfterCallWork
        """
        return self._after_call_work

    @after_call_work.setter
    def after_call_work(self, after_call_work: 'QueueConversationEventTopicAfterCallWork') -> None:
        """
        Sets the after_call_work of this QueueConversationEventTopicSocialExpression.
        A communication's after-call work data.

        :param after_call_work: The after_call_work of this QueueConversationEventTopicSocialExpression.
        :type: QueueConversationEventTopicAfterCallWork
        """
        

        self._after_call_work = after_call_work

    @property
    def after_call_work_required(self) -> bool:
        """
        Gets the after_call_work_required of this QueueConversationEventTopicSocialExpression.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :return: The after_call_work_required of this QueueConversationEventTopicSocialExpression.
        :rtype: bool
        """
        return self._after_call_work_required

    @after_call_work_required.setter
    def after_call_work_required(self, after_call_work_required: bool) -> None:
        """
        Sets the after_call_work_required of this QueueConversationEventTopicSocialExpression.
        Indicates if after-call is required for a communication. Only used when the ACW Setting is Agent Requested.

        :param after_call_work_required: The after_call_work_required of this QueueConversationEventTopicSocialExpression.
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

