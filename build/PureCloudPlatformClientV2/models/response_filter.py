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


class ResponseFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ResponseFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'operator': 'str',
            'values': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'operator': 'operator',
            'values': 'values'
        }

        self._name = None
        self._operator = None
        self._values = None

    @property
    def name(self) -> str:
        """
        Gets the name of this ResponseFilter.
        Field to filter on. Allowed values are 'name', 'libraryId', 'text.contentType', 'messagingTemplate' and 'responseType'

        :return: The name of this ResponseFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ResponseFilter.
        Field to filter on. Allowed values are 'name', 'libraryId', 'text.contentType', 'messagingTemplate' and 'responseType'

        :param name: The name of this ResponseFilter.
        :type: str
        """
        

        self._name = name

    @property
    def operator(self) -> str:
        """
        Gets the operator of this ResponseFilter.
        Filter operation: IN, EQUALS, NOTEQUALS.

        :return: The operator of this ResponseFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this ResponseFilter.
        Filter operation: IN, EQUALS, NOTEQUALS.

        :param operator: The operator of this ResponseFilter.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["IN", "EQUALS", "NOTEQUALS"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def values(self) -> List[str]:
        """
        Gets the values of this ResponseFilter.
        Values to filter on. If name is 'responseType' then allowed values are 'CampaignSmsTemplate', 'CampaignEmailTemplate', 'Footer' and 'Signature'

        :return: The values of this ResponseFilter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values: List[str]) -> None:
        """
        Sets the values of this ResponseFilter.
        Values to filter on. If name is 'responseType' then allowed values are 'CampaignSmsTemplate', 'CampaignEmailTemplate', 'Footer' and 'Signature'

        :param values: The values of this ResponseFilter.
        :type: list[str]
        """
        

        self._values = values

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

