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
    from . import NumericRange

class ActionAggregateQueryPredicate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ActionAggregateQueryPredicate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'dimension': 'str',
            'operator': 'str',
            'value': 'str',
            'range': 'NumericRange'
        }

        self.attribute_map = {
            'type': 'type',
            'dimension': 'dimension',
            'operator': 'operator',
            'value': 'value',
            'range': 'range'
        }

        self._type = None
        self._dimension = None
        self._operator = None
        self._value = None
        self._range = None

    @property
    def type(self) -> str:
        """
        Gets the type of this ActionAggregateQueryPredicate.
        Optional type, can usually be inferred

        :return: The type of this ActionAggregateQueryPredicate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this ActionAggregateQueryPredicate.
        Optional type, can usually be inferred

        :param type: The type of this ActionAggregateQueryPredicate.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["dimension", "property", "metric"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def dimension(self) -> str:
        """
        Gets the dimension of this ActionAggregateQueryPredicate.
        Left hand side for dimension predicates

        :return: The dimension of this ActionAggregateQueryPredicate.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: str) -> None:
        """
        Sets the dimension of this ActionAggregateQueryPredicate.
        Left hand side for dimension predicates

        :param dimension: The dimension of this ActionAggregateQueryPredicate.
        :type: str
        """
        if isinstance(dimension, int):
            dimension = str(dimension)
        allowed_values = ["actionCategory", "actionId", "actionName", "correlationId", "errorType", "integrationId", "integrationName", "responseStatus"]
        if dimension.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for dimension -> " + dimension)
            self._dimension = "outdated_sdk_version"
        else:
            self._dimension = dimension

    @property
    def operator(self) -> str:
        """
        Gets the operator of this ActionAggregateQueryPredicate.
        Optional operator, default is matches

        :return: The operator of this ActionAggregateQueryPredicate.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this ActionAggregateQueryPredicate.
        Optional operator, default is matches

        :param operator: The operator of this ActionAggregateQueryPredicate.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["matches", "exists", "notExists"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def value(self) -> str:
        """
        Gets the value of this ActionAggregateQueryPredicate.
        Right hand side for dimension predicates

        :return: The value of this ActionAggregateQueryPredicate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this ActionAggregateQueryPredicate.
        Right hand side for dimension predicates

        :param value: The value of this ActionAggregateQueryPredicate.
        :type: str
        """
        

        self._value = value

    @property
    def range(self) -> 'NumericRange':
        """
        Gets the range of this ActionAggregateQueryPredicate.
        Right hand side for dimension predicates

        :return: The range of this ActionAggregateQueryPredicate.
        :rtype: NumericRange
        """
        return self._range

    @range.setter
    def range(self, range: 'NumericRange') -> None:
        """
        Sets the range of this ActionAggregateQueryPredicate.
        Right hand side for dimension predicates

        :param range: The range of this ActionAggregateQueryPredicate.
        :type: NumericRange
        """
        

        self._range = range

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

