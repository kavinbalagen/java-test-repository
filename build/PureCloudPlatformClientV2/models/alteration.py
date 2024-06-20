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


class Alteration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Alteration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'start': 'str',
            'end': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'start': 'start',
            'end': 'end'
        }

        self._type = None
        self._start = None
        self._end = None

    @property
    def type(self) -> str:
        """
        Gets the type of this Alteration.
        Range type (Exclusion: used to exclude a specific time within the recurrence. Inclusion: used to include a specific time within the recurrence which will execute in addition to the normal recurrence. If both an exclusion and inclusion are specified, the inclusion will take precedence over the exclusion.)

        :return: The type of this Alteration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Alteration.
        Range type (Exclusion: used to exclude a specific time within the recurrence. Inclusion: used to include a specific time within the recurrence which will execute in addition to the normal recurrence. If both an exclusion and inclusion are specified, the inclusion will take precedence over the exclusion.)

        :param type: The type of this Alteration.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Exclusion", "Inclusion"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def start(self) -> str:
        """
        Gets the start of this Alteration.
        The start date of an alteration range as an ISO-8601 string

        :return: The start of this Alteration.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start: str) -> None:
        """
        Sets the start of this Alteration.
        The start date of an alteration range as an ISO-8601 string

        :param start: The start of this Alteration.
        :type: str
        """
        

        self._start = start

    @property
    def end(self) -> str:
        """
        Gets the end of this Alteration.
        The end date of an alteration range as an ISO-8601 string

        :return: The end of this Alteration.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end: str) -> None:
        """
        Sets the end of this Alteration.
        The end date of an alteration range as an ISO-8601 string

        :param end: The end of this Alteration.
        :type: str
        """
        

        self._end = end

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

