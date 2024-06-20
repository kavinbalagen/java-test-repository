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


class QueueConversationScreenShareEventTopicJourneyActionMap(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationScreenShareEventTopicJourneyActionMap - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'version': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'version': 'version'
        }

        self._id = None
        self._version = None

    @property
    def id(self) -> str:
        """
        Gets the id of this QueueConversationScreenShareEventTopicJourneyActionMap.
        The ID of the actionMap in the Journey System which triggered this action

        :return: The id of this QueueConversationScreenShareEventTopicJourneyActionMap.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this QueueConversationScreenShareEventTopicJourneyActionMap.
        The ID of the actionMap in the Journey System which triggered this action

        :param id: The id of this QueueConversationScreenShareEventTopicJourneyActionMap.
        :type: str
        """
        

        self._id = id

    @property
    def version(self) -> int:
        """
        Gets the version of this QueueConversationScreenShareEventTopicJourneyActionMap.
        The version number of the actionMap in the Journey System at the time this action was triggered

        :return: The version of this QueueConversationScreenShareEventTopicJourneyActionMap.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this QueueConversationScreenShareEventTopicJourneyActionMap.
        The version number of the actionMap in the Journey System at the time this action was triggered

        :param version: The version of this QueueConversationScreenShareEventTopicJourneyActionMap.
        :type: int
        """
        

        self._version = version

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

