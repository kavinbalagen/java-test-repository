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


class QueueConversationVideoEventTopicDisconnectReason(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationVideoEventTopicDisconnectReason - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'code': 'int',
            'phrase': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'code': 'code',
            'phrase': 'phrase'
        }

        self._type = None
        self._code = None
        self._phrase = None

    @property
    def type(self) -> str:
        """
        Gets the type of this QueueConversationVideoEventTopicDisconnectReason.
        Disconnect reason protocol type.

        :return: The type of this QueueConversationVideoEventTopicDisconnectReason.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this QueueConversationVideoEventTopicDisconnectReason.
        Disconnect reason protocol type.

        :param type: The type of this QueueConversationVideoEventTopicDisconnectReason.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["q850", "sip"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def code(self) -> int:
        """
        Gets the code of this QueueConversationVideoEventTopicDisconnectReason.
        Protocol specific reason code. See the Q.850 and SIP specs.

        :return: The code of this QueueConversationVideoEventTopicDisconnectReason.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int) -> None:
        """
        Sets the code of this QueueConversationVideoEventTopicDisconnectReason.
        Protocol specific reason code. See the Q.850 and SIP specs.

        :param code: The code of this QueueConversationVideoEventTopicDisconnectReason.
        :type: int
        """
        

        self._code = code

    @property
    def phrase(self) -> str:
        """
        Gets the phrase of this QueueConversationVideoEventTopicDisconnectReason.
        Human readable English description of the disconnect reason.

        :return: The phrase of this QueueConversationVideoEventTopicDisconnectReason.
        :rtype: str
        """
        return self._phrase

    @phrase.setter
    def phrase(self, phrase: str) -> None:
        """
        Sets the phrase of this QueueConversationVideoEventTopicDisconnectReason.
        Human readable English description of the disconnect reason.

        :param phrase: The phrase of this QueueConversationVideoEventTopicDisconnectReason.
        :type: str
        """
        

        self._phrase = phrase

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

