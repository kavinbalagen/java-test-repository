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


class CommunicationEndedEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CommunicationEndedEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_id': 'str',
            'event_date_time': 'datetime',
            'conversation_id': 'str',
            'communication_id': 'str',
            'disconnect_type': 'str',
            'destination_conversation_id': 'str'
        }

        self.attribute_map = {
            'event_id': 'eventId',
            'event_date_time': 'eventDateTime',
            'conversation_id': 'conversationId',
            'communication_id': 'communicationId',
            'disconnect_type': 'disconnectType',
            'destination_conversation_id': 'destinationConversationId'
        }

        self._event_id = None
        self._event_date_time = None
        self._conversation_id = None
        self._communication_id = None
        self._disconnect_type = None
        self._destination_conversation_id = None

    @property
    def event_id(self) -> str:
        """
        Gets the event_id of this CommunicationEndedEvent.
        A unique (V4 UUID) eventId for this event

        :return: The event_id of this CommunicationEndedEvent.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id: str) -> None:
        """
        Sets the event_id of this CommunicationEndedEvent.
        A unique (V4 UUID) eventId for this event

        :param event_id: The event_id of this CommunicationEndedEvent.
        :type: str
        """
        

        self._event_id = event_id

    @property
    def event_date_time(self) -> datetime:
        """
        Gets the event_date_time of this CommunicationEndedEvent.
        A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The event_date_time of this CommunicationEndedEvent.
        :rtype: datetime
        """
        return self._event_date_time

    @event_date_time.setter
    def event_date_time(self, event_date_time: datetime) -> None:
        """
        Sets the event_date_time of this CommunicationEndedEvent.
        A Date Time representing the time this event occurred. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param event_date_time: The event_date_time of this CommunicationEndedEvent.
        :type: datetime
        """
        

        self._event_date_time = event_date_time

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this CommunicationEndedEvent.
        A unique Id (V4 UUID) identifying this conversation

        :return: The conversation_id of this CommunicationEndedEvent.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this CommunicationEndedEvent.
        A unique Id (V4 UUID) identifying this conversation

        :param conversation_id: The conversation_id of this CommunicationEndedEvent.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def communication_id(self) -> str:
        """
        Gets the communication_id of this CommunicationEndedEvent.
        A unique Id (V4 UUID) identifying this communication

        :return: The communication_id of this CommunicationEndedEvent.
        :rtype: str
        """
        return self._communication_id

    @communication_id.setter
    def communication_id(self, communication_id: str) -> None:
        """
        Sets the communication_id of this CommunicationEndedEvent.
        A unique Id (V4 UUID) identifying this communication

        :param communication_id: The communication_id of this CommunicationEndedEvent.
        :type: str
        """
        

        self._communication_id = communication_id

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this CommunicationEndedEvent.
        Indicates how this communication was ended.

        :return: The disconnect_type of this CommunicationEndedEvent.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this CommunicationEndedEvent.
        Indicates how this communication was ended.

        :param disconnect_type: The disconnect_type of this CommunicationEndedEvent.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["Error", "Peer", "Self", "System", "Transfer", "TransferACD", "TransferConference", "TransferConsult", "TransferUser"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def destination_conversation_id(self) -> str:
        """
        Gets the destination_conversation_id of this CommunicationEndedEvent.
        The id (V4 UUID) of the conversation that the communication is being moved to when conversations are merged.

        :return: The destination_conversation_id of this CommunicationEndedEvent.
        :rtype: str
        """
        return self._destination_conversation_id

    @destination_conversation_id.setter
    def destination_conversation_id(self, destination_conversation_id: str) -> None:
        """
        Sets the destination_conversation_id of this CommunicationEndedEvent.
        The id (V4 UUID) of the conversation that the communication is being moved to when conversations are merged.

        :param destination_conversation_id: The destination_conversation_id of this CommunicationEndedEvent.
        :type: str
        """
        

        self._destination_conversation_id = destination_conversation_id

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

