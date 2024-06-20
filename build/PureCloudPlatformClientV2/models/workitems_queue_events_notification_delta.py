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


class WorkitemsQueueEventsNotificationDelta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkitemsQueueEventsNotificationDelta - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'op': 'str',
            'field': 'str',
            'old_value': 'str',
            'new_value': 'str'
        }

        self.attribute_map = {
            'op': 'op',
            'field': 'field',
            'old_value': 'oldValue',
            'new_value': 'newValue'
        }

        self._op = None
        self._field = None
        self._old_value = None
        self._new_value = None

    @property
    def op(self) -> str:
        """
        Gets the op of this WorkitemsQueueEventsNotificationDelta.


        :return: The op of this WorkitemsQueueEventsNotificationDelta.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op: str) -> None:
        """
        Sets the op of this WorkitemsQueueEventsNotificationDelta.


        :param op: The op of this WorkitemsQueueEventsNotificationDelta.
        :type: str
        """
        if isinstance(op, int):
            op = str(op)
        allowed_values = ["add", "remove", "replace", "unknown"]
        if op.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for op -> " + op)
            self._op = "outdated_sdk_version"
        else:
            self._op = op

    @property
    def field(self) -> str:
        """
        Gets the field of this WorkitemsQueueEventsNotificationDelta.


        :return: The field of this WorkitemsQueueEventsNotificationDelta.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field: str) -> None:
        """
        Sets the field of this WorkitemsQueueEventsNotificationDelta.


        :param field: The field of this WorkitemsQueueEventsNotificationDelta.
        :type: str
        """
        

        self._field = field

    @property
    def old_value(self) -> str:
        """
        Gets the old_value of this WorkitemsQueueEventsNotificationDelta.


        :return: The old_value of this WorkitemsQueueEventsNotificationDelta.
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value: str) -> None:
        """
        Sets the old_value of this WorkitemsQueueEventsNotificationDelta.


        :param old_value: The old_value of this WorkitemsQueueEventsNotificationDelta.
        :type: str
        """
        

        self._old_value = old_value

    @property
    def new_value(self) -> str:
        """
        Gets the new_value of this WorkitemsQueueEventsNotificationDelta.


        :return: The new_value of this WorkitemsQueueEventsNotificationDelta.
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value: str) -> None:
        """
        Sets the new_value of this WorkitemsQueueEventsNotificationDelta.


        :param new_value: The new_value of this WorkitemsQueueEventsNotificationDelta.
        :type: str
        """
        

        self._new_value = new_value

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

