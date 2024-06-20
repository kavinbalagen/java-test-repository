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


class WorkbinQuerySort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkbinQuerySort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'ascending': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'ascending': 'ascending'
        }

        self._name = None
        self._ascending = None

    @property
    def name(self) -> str:
        """
        Gets the name of this WorkbinQuerySort.
        Specify an attribute for sorting. It's possible to use an attribute both for sorting and in the query at the same time, but these restrictions apply: Only the operators EQ, LT, LTE, GT, GTE, BETWEEN and BEGINS_WITH are supported and the attribute can't be present in more than one filter.

        :return: The name of this WorkbinQuerySort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this WorkbinQuerySort.
        Specify an attribute for sorting. It's possible to use an attribute both for sorting and in the query at the same time, but these restrictions apply: Only the operators EQ, LT, LTE, GT, GTE, BETWEEN and BEGINS_WITH are supported and the attribute can't be present in more than one filter.

        :param name: The name of this WorkbinQuerySort.
        :type: str
        """
        if isinstance(name, int):
            name = str(name)
        allowed_values = ["dateModified", "name"]
        if name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for name -> " + name)
            self._name = "outdated_sdk_version"
        else:
            self._name = name

    @property
    def ascending(self) -> bool:
        """
        Gets the ascending of this WorkbinQuerySort.
        Sort Ascending

        :return: The ascending of this WorkbinQuerySort.
        :rtype: bool
        """
        return self._ascending

    @ascending.setter
    def ascending(self, ascending: bool) -> None:
        """
        Sets the ascending of this WorkbinQuerySort.
        Sort Ascending

        :param ascending: The ascending of this WorkbinQuerySort.
        :type: bool
        """
        

        self._ascending = ascending

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

