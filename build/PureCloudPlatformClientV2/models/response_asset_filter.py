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


class ResponseAssetFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ResponseAssetFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'end_value': 'str',
            'values': 'list[str]',
            'start_value': 'str',
            'fields': 'list[str]',
            'value': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'end_value': 'endValue',
            'values': 'values',
            'start_value': 'startValue',
            'fields': 'fields',
            'value': 'value',
            'type': 'type'
        }

        self._end_value = None
        self._values = None
        self._start_value = None
        self._fields = None
        self._value = None
        self._type = None

    @property
    def end_value(self) -> str:
        """
        Gets the end_value of this ResponseAssetFilter.
        The end value of the range. This field is used for range search types. Accepts numbers and date in ISO8601 format

        :return: The end_value of this ResponseAssetFilter.
        :rtype: str
        """
        return self._end_value

    @end_value.setter
    def end_value(self, end_value: str) -> None:
        """
        Sets the end_value of this ResponseAssetFilter.
        The end value of the range. This field is used for range search types. Accepts numbers and date in ISO8601 format

        :param end_value: The end_value of this ResponseAssetFilter.
        :type: str
        """
        

        self._end_value = end_value

    @property
    def values(self) -> List[str]:
        """
        Gets the values of this ResponseAssetFilter.
        A list of values for the search to match against

        :return: The values of this ResponseAssetFilter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values: List[str]) -> None:
        """
        Sets the values of this ResponseAssetFilter.
        A list of values for the search to match against

        :param values: The values of this ResponseAssetFilter.
        :type: list[str]
        """
        

        self._values = values

    @property
    def start_value(self) -> str:
        """
        Gets the start_value of this ResponseAssetFilter.
        The start value of the range. This field is used for range search types. Accepts numbers and date in ISO8601 format

        :return: The start_value of this ResponseAssetFilter.
        :rtype: str
        """
        return self._start_value

    @start_value.setter
    def start_value(self, start_value: str) -> None:
        """
        Sets the start_value of this ResponseAssetFilter.
        The start value of the range. This field is used for range search types. Accepts numbers and date in ISO8601 format

        :param start_value: The start_value of this ResponseAssetFilter.
        :type: str
        """
        

        self._start_value = start_value

    @property
    def fields(self) -> List[str]:
        """
        Gets the fields of this ResponseAssetFilter.
        Field name to search against. Allowed Values: divisionId, name, contentLength, contentType, dateCreated

        :return: The fields of this ResponseAssetFilter.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields: List[str]) -> None:
        """
        Sets the fields of this ResponseAssetFilter.
        Field name to search against. Allowed Values: divisionId, name, contentLength, contentType, dateCreated

        :param fields: The fields of this ResponseAssetFilter.
        :type: list[str]
        """
        

        self._fields = fields

    @property
    def value(self) -> str:
        """
        Gets the value of this ResponseAssetFilter.
        A value for the search to match against

        :return: The value of this ResponseAssetFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this ResponseAssetFilter.
        A value for the search to match against

        :param value: The value of this ResponseAssetFilter.
        :type: str
        """
        

        self._value = value

    @property
    def type(self) -> str:
        """
        Gets the type of this ResponseAssetFilter.
        How to apply this search criteria against other criteria. Filter type supported for each field:- name:[STARTS_WITH, TERM], divisionId:[TERM, TERMS], contentLength:[RANGE, GREATER_THAN_EQUAL_TO, LESS_THAN_EQUAL_TO], contentType:[STARTS_WITH, TERM] dateCreated:[DATE_RANGE]

        :return: The type of this ResponseAssetFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this ResponseAssetFilter.
        How to apply this search criteria against other criteria. Filter type supported for each field:- name:[STARTS_WITH, TERM], divisionId:[TERM, TERMS], contentLength:[RANGE, GREATER_THAN_EQUAL_TO, LESS_THAN_EQUAL_TO], contentType:[STARTS_WITH, TERM] dateCreated:[DATE_RANGE]

        :param type: The type of this ResponseAssetFilter.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["TERM", "TERMS", "STARTS_WITH", "RANGE", "GREATER_THAN_EQUAL_TO", "LESS_THAN_EQUAL_TO", "DATE_RANGE"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

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

