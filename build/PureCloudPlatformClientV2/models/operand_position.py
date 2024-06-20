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


class OperandPosition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OperandPosition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'starting_position_value': 'int',
            'starting_position_direction': 'str',
            'ending_position_value': 'int',
            'ending_position_direction': 'str'
        }

        self.attribute_map = {
            'starting_position_value': 'startingPositionValue',
            'starting_position_direction': 'startingPositionDirection',
            'ending_position_value': 'endingPositionValue',
            'ending_position_direction': 'endingPositionDirection'
        }

        self._starting_position_value = None
        self._starting_position_direction = None
        self._ending_position_value = None
        self._ending_position_direction = None

    @property
    def starting_position_value(self) -> int:
        """
        Gets the starting_position_value of this OperandPosition.
        Defines starting point of a position range - number of seconds or words from the start or from the end of the interaction

        :return: The starting_position_value of this OperandPosition.
        :rtype: int
        """
        return self._starting_position_value

    @starting_position_value.setter
    def starting_position_value(self, starting_position_value: int) -> None:
        """
        Sets the starting_position_value of this OperandPosition.
        Defines starting point of a position range - number of seconds or words from the start or from the end of the interaction

        :param starting_position_value: The starting_position_value of this OperandPosition.
        :type: int
        """
        

        self._starting_position_value = starting_position_value

    @property
    def starting_position_direction(self) -> str:
        """
        Gets the starting_position_direction of this OperandPosition.
        Dictates starting position directionality

        :return: The starting_position_direction of this OperandPosition.
        :rtype: str
        """
        return self._starting_position_direction

    @starting_position_direction.setter
    def starting_position_direction(self, starting_position_direction: str) -> None:
        """
        Sets the starting_position_direction of this OperandPosition.
        Dictates starting position directionality

        :param starting_position_direction: The starting_position_direction of this OperandPosition.
        :type: str
        """
        if isinstance(starting_position_direction, int):
            starting_position_direction = str(starting_position_direction)
        allowed_values = ["FromStart", "FromEnd"]
        if starting_position_direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for starting_position_direction -> " + starting_position_direction)
            self._starting_position_direction = "outdated_sdk_version"
        else:
            self._starting_position_direction = starting_position_direction

    @property
    def ending_position_value(self) -> int:
        """
        Gets the ending_position_value of this OperandPosition.
        Defines ending point of a position range - number of seconds or words from the start or from the end of the interaction

        :return: The ending_position_value of this OperandPosition.
        :rtype: int
        """
        return self._ending_position_value

    @ending_position_value.setter
    def ending_position_value(self, ending_position_value: int) -> None:
        """
        Sets the ending_position_value of this OperandPosition.
        Defines ending point of a position range - number of seconds or words from the start or from the end of the interaction

        :param ending_position_value: The ending_position_value of this OperandPosition.
        :type: int
        """
        

        self._ending_position_value = ending_position_value

    @property
    def ending_position_direction(self) -> str:
        """
        Gets the ending_position_direction of this OperandPosition.
        Dictates ending position directionality

        :return: The ending_position_direction of this OperandPosition.
        :rtype: str
        """
        return self._ending_position_direction

    @ending_position_direction.setter
    def ending_position_direction(self, ending_position_direction: str) -> None:
        """
        Sets the ending_position_direction of this OperandPosition.
        Dictates ending position directionality

        :param ending_position_direction: The ending_position_direction of this OperandPosition.
        :type: str
        """
        if isinstance(ending_position_direction, int):
            ending_position_direction = str(ending_position_direction)
        allowed_values = ["FromStart", "FromEnd"]
        if ending_position_direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for ending_position_direction -> " + ending_position_direction)
            self._ending_position_direction = "outdated_sdk_version"
        else:
            self._ending_position_direction = ending_position_direction

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

