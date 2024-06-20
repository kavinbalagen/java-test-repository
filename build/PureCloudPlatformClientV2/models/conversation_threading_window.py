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
    from . import ConversationThreadingWindowSetting

class ConversationThreadingWindow(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationThreadingWindow - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'settings': 'list[ConversationThreadingWindowSetting]',
            'default_timeout_minutes': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'settings': 'settings',
            'default_timeout_minutes': 'defaultTimeoutMinutes'
        }

        self._id = None
        self._settings = None
        self._default_timeout_minutes = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ConversationThreadingWindow.
        The globally unique identifier for the object.

        :return: The id of this ConversationThreadingWindow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationThreadingWindow.
        The globally unique identifier for the object.

        :param id: The id of this ConversationThreadingWindow.
        :type: str
        """
        

        self._id = id

    @property
    def settings(self) -> List['ConversationThreadingWindowSetting']:
        """
        Gets the settings of this ConversationThreadingWindow.
        The conversation threading window timeout (Minutes) for each messaging type

        :return: The settings of this ConversationThreadingWindow.
        :rtype: list[ConversationThreadingWindowSetting]
        """
        return self._settings

    @settings.setter
    def settings(self, settings: List['ConversationThreadingWindowSetting']) -> None:
        """
        Sets the settings of this ConversationThreadingWindow.
        The conversation threading window timeout (Minutes) for each messaging type

        :param settings: The settings of this ConversationThreadingWindow.
        :type: list[ConversationThreadingWindowSetting]
        """
        

        self._settings = settings

    @property
    def default_timeout_minutes(self) -> int:
        """
        Gets the default_timeout_minutes of this ConversationThreadingWindow.
        The default conversation threading window timeout (Minutes)

        :return: The default_timeout_minutes of this ConversationThreadingWindow.
        :rtype: int
        """
        return self._default_timeout_minutes

    @default_timeout_minutes.setter
    def default_timeout_minutes(self, default_timeout_minutes: int) -> None:
        """
        Sets the default_timeout_minutes of this ConversationThreadingWindow.
        The default conversation threading window timeout (Minutes)

        :param default_timeout_minutes: The default_timeout_minutes of this ConversationThreadingWindow.
        :type: int
        """
        

        self._default_timeout_minutes = default_timeout_minutes

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

