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


class SuggestSearchCriteria(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SuggestSearchCriteria - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_value': 'str',
            'values': 'list[str]',
            'start_value': 'str',
            'value': 'str',
            'operator': 'str',
            'group': 'list[SuggestSearchCriteria]',
            'date_format': 'str',
            'fields': 'list[str]'
        }

        self.attribute_map = {
            'end_value': 'endValue',
            'values': 'values',
            'start_value': 'startValue',
            'value': 'value',
            'operator': 'operator',
            'group': 'group',
            'date_format': 'dateFormat',
            'fields': 'fields'
        }

        self._end_value = None
        self._values = None
        self._start_value = None
        self._value = None
        self._operator = None
        self._group = None
        self._date_format = None
        self._fields = None

    @property
    def end_value(self) -> str:
        """
        Gets the end_value of this SuggestSearchCriteria.
        The end value of the range. This field is used for range search types.

        :return: The end_value of this SuggestSearchCriteria.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value: str) -> None:
        """
        Sets the end_value of this SuggestSearchCriteria.
        The end value of the range. This field is used for range search types.

        :param end_value: The end_value of this SuggestSearchCriteria.
        :type: str
        """
        

        self._end_value = end_value

    @property
    def values(self) -> List[str]:
        """
        Gets the values of this SuggestSearchCriteria.
        A list of values for the search to match against

        :return: The values of this SuggestSearchCriteria.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values: List[str]) -> None:
        """
        Sets the values of this SuggestSearchCriteria.
        A list of values for the search to match against

        :param values: The values of this SuggestSearchCriteria.
        :type: list[str]
        """
        

        self._values = values

    @property
    def start_value(self) -> str:
        """
        Gets the start_value of this SuggestSearchCriteria.
        The start value of the range. This field is used for range search types.

        :return: The start_value of this SuggestSearchCriteria.
        :rtype: str
        """
        return self._start_value

    @start_value.setter
    def start_value(self, start_value: str) -> None:
        """
        Sets the start_value of this SuggestSearchCriteria.
        The start value of the range. This field is used for range search types.

        :param start_value: The start_value of this SuggestSearchCriteria.
        :type: str
        """
        

        self._start_value = start_value

    @property
    def value(self) -> str:
        """
        Gets the value of this SuggestSearchCriteria.
        A value for the search to match against

        :return: The value of this SuggestSearchCriteria.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this SuggestSearchCriteria.
        A value for the search to match against

        :param value: The value of this SuggestSearchCriteria.
        :type: str
        """
        

        self._value = value

    @property
    def operator(self) -> str:
        """
        Gets the operator of this SuggestSearchCriteria.
        How to apply this search criteria against other criteria

        :return: The operator of this SuggestSearchCriteria.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this SuggestSearchCriteria.
        How to apply this search criteria against other criteria

        :param operator: The operator of this SuggestSearchCriteria.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["AND", "OR", "NOT"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def group(self) -> List['SuggestSearchCriteria']:
        """
        Gets the group of this SuggestSearchCriteria.
        Groups multiple conditions

        :return: The group of this SuggestSearchCriteria.
        :rtype: list[SuggestSearchCriteria]
        """
        return self._group

    @group.setter
    def group(self, group: List['SuggestSearchCriteria']) -> None:
        """
        Sets the group of this SuggestSearchCriteria.
        Groups multiple conditions

        :param group: The group of this SuggestSearchCriteria.
        :type: list[SuggestSearchCriteria]
        """
        

        self._group = group

    @property
    def date_format(self) -> str:
        """
        Gets the date_format of this SuggestSearchCriteria.
        Set date format for criteria values when using date range search type.  Supports Java date format syntax, example yyyy-MM-dd'T'HH:mm:ss.SSSX.

        :return: The date_format of this SuggestSearchCriteria.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format: str) -> None:
        """
        Sets the date_format of this SuggestSearchCriteria.
        Set date format for criteria values when using date range search type.  Supports Java date format syntax, example yyyy-MM-dd'T'HH:mm:ss.SSSX.

        :param date_format: The date_format of this SuggestSearchCriteria.
        :type: str
        """
        

        self._date_format = date_format

    @property
    def fields(self) -> List[str]:
        """
        Gets the fields of this SuggestSearchCriteria.
        Field names to search against

        :return: The fields of this SuggestSearchCriteria.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields: List[str]) -> None:
        """
        Sets the fields of this SuggestSearchCriteria.
        Field names to search against

        :param fields: The fields of this SuggestSearchCriteria.
        :type: list[str]
        """
        

        self._fields = fields

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
