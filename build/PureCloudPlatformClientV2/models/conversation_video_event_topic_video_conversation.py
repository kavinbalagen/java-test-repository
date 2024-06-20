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
    from . import ConversationVideoEventTopicVideoMediaParticipant

class ConversationVideoEventTopicVideoConversation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationVideoEventTopicVideoConversation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'participants': 'list[ConversationVideoEventTopicVideoMediaParticipant]',
            'other_media_uris': 'list[str]',
            'address': 'str',
            'utilization_label_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'participants': 'participants',
            'other_media_uris': 'otherMediaUris',
            'address': 'address',
            'utilization_label_id': 'utilizationLabelId'
        }

        self._id = None
        self._name = None
        self._participants = None
        self._other_media_uris = None
        self._address = None
        self._utilization_label_id = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ConversationVideoEventTopicVideoConversation.


        :return: The id of this ConversationVideoEventTopicVideoConversation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationVideoEventTopicVideoConversation.


        :param id: The id of this ConversationVideoEventTopicVideoConversation.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ConversationVideoEventTopicVideoConversation.


        :return: The name of this ConversationVideoEventTopicVideoConversation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ConversationVideoEventTopicVideoConversation.


        :param name: The name of this ConversationVideoEventTopicVideoConversation.
        :type: str
        """
        

        self._name = name

    @property
    def participants(self) -> List['ConversationVideoEventTopicVideoMediaParticipant']:
        """
        Gets the participants of this ConversationVideoEventTopicVideoConversation.


        :return: The participants of this ConversationVideoEventTopicVideoConversation.
        :rtype: list[ConversationVideoEventTopicVideoMediaParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants: List['ConversationVideoEventTopicVideoMediaParticipant']) -> None:
        """
        Sets the participants of this ConversationVideoEventTopicVideoConversation.


        :param participants: The participants of this ConversationVideoEventTopicVideoConversation.
        :type: list[ConversationVideoEventTopicVideoMediaParticipant]
        """
        

        self._participants = participants

    @property
    def other_media_uris(self) -> List[str]:
        """
        Gets the other_media_uris of this ConversationVideoEventTopicVideoConversation.


        :return: The other_media_uris of this ConversationVideoEventTopicVideoConversation.
        :rtype: list[str]
        """
        return self._other_media_uris

    @other_media_uris.setter
    def other_media_uris(self, other_media_uris: List[str]) -> None:
        """
        Sets the other_media_uris of this ConversationVideoEventTopicVideoConversation.


        :param other_media_uris: The other_media_uris of this ConversationVideoEventTopicVideoConversation.
        :type: list[str]
        """
        

        self._other_media_uris = other_media_uris

    @property
    def address(self) -> str:
        """
        Gets the address of this ConversationVideoEventTopicVideoConversation.


        :return: The address of this ConversationVideoEventTopicVideoConversation.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Sets the address of this ConversationVideoEventTopicVideoConversation.


        :param address: The address of this ConversationVideoEventTopicVideoConversation.
        :type: str
        """
        

        self._address = address

    @property
    def utilization_label_id(self) -> str:
        """
        Gets the utilization_label_id of this ConversationVideoEventTopicVideoConversation.


        :return: The utilization_label_id of this ConversationVideoEventTopicVideoConversation.
        :rtype: str
        """
        return self._utilization_label_id

    @utilization_label_id.setter
    def utilization_label_id(self, utilization_label_id: str) -> None:
        """
        Sets the utilization_label_id of this ConversationVideoEventTopicVideoConversation.


        :param utilization_label_id: The utilization_label_id of this ConversationVideoEventTopicVideoConversation.
        :type: str
        """
        

        self._utilization_label_id = utilization_label_id

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

