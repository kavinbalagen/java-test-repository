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


class CriteriaItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CriteriaItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'operator': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'operator': 'operator',
            'value': 'value'
        }

        self._key = None
        self._operator = None
        self._value = None

    @property
    def key(self) -> str:
        """
        Gets the key of this CriteriaItem.
        The id of the criteria to be checked.

        :return: The key of this CriteriaItem.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str) -> None:
        """
        Sets the key of this CriteriaItem.
        The id of the criteria to be checked.

        :param key: The key of this CriteriaItem.
        :type: str
        """
        if isinstance(key, int):
            key = str(key)
        allowed_values = ["FlowStartDateTime", "FlowEndDateTime", "ConversationId", "FlowType", "FlowId", "FlowErrorReason", "FlowWarningReason", "FlowAlternateExecutionId", "FlowObjectExecutionId", "FlowActionId", "FlowActionType", "FlowActionOutputPathId", "FlowActionOutputPathName", "FlowActionIdOutputPathId", "FlowActionIdOutputPathName", "FlowActionTypeOutputPathId", "FlowActionTypeOutputPathName", "BotId", "BotErrorReason", "BotFlowExecutionId", "BotObjectExecutionId"]
        if key.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for key -> " + key)
            self._key = "outdated_sdk_version"
        else:
            self._key = key

    @property
    def operator(self) -> str:
        """
        Gets the operator of this CriteriaItem.
        The operator used to check on the criteria id.

        :return: The operator of this CriteriaItem.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this CriteriaItem.
        The operator used to check on the criteria id.

        :param operator: The operator of this CriteriaItem.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["eq", "gt", "gte", "lt", "lte", "not", "begins", "not_null"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def value(self) -> str:
        """
        Gets the value of this CriteriaItem.
        The target value used to query on.

        :return: The value of this CriteriaItem.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this CriteriaItem.
        The target value used to query on.

        :param value: The value of this CriteriaItem.
        :type: str
        """
        

        self._value = value

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

