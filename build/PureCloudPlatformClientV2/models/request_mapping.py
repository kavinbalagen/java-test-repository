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


class RequestMapping(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        RequestMapping - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'attribute_type': 'str',
            'mapping_type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'attribute_type': 'attributeType',
            'mapping_type': 'mappingType',
            'value': 'value'
        }

        self._name = None
        self._attribute_type = None
        self._mapping_type = None
        self._value = None

    @property
    def name(self) -> str:
        """
        Gets the name of this RequestMapping.
        Name of the Integration Action Attribute to supply the value for

        :return: The name of this RequestMapping.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this RequestMapping.
        Name of the Integration Action Attribute to supply the value for

        :param name: The name of this RequestMapping.
        :type: str
        """
        

        self._name = name

    @property
    def attribute_type(self) -> str:
        """
        Gets the attribute_type of this RequestMapping.
        Type of the value supplied

        :return: The attribute_type of this RequestMapping.
        :rtype: str
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type: str) -> None:
        """
        Sets the attribute_type of this RequestMapping.
        Type of the value supplied

        :param attribute_type: The attribute_type of this RequestMapping.
        :type: str
        """
        if isinstance(attribute_type, int):
            attribute_type = str(attribute_type)
        allowed_values = ["String", "Number", "Integer", "Boolean"]
        if attribute_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for attribute_type -> " + attribute_type)
            self._attribute_type = "outdated_sdk_version"
        else:
            self._attribute_type = attribute_type

    @property
    def mapping_type(self) -> str:
        """
        Gets the mapping_type of this RequestMapping.
        Method of finding value to use with Attribute

        :return: The mapping_type of this RequestMapping.
        :rtype: str
        """
        return self._mapping_type

    @mapping_type.setter
    def mapping_type(self, mapping_type: str) -> None:
        """
        Sets the mapping_type of this RequestMapping.
        Method of finding value to use with Attribute

        :param mapping_type: The mapping_type of this RequestMapping.
        :type: str
        """
        if isinstance(mapping_type, int):
            mapping_type = str(mapping_type)
        allowed_values = ["Lookup", "HardCoded"]
        if mapping_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for mapping_type -> " + mapping_type)
            self._mapping_type = "outdated_sdk_version"
        else:
            self._mapping_type = mapping_type

    @property
    def value(self) -> str:
        """
        Gets the value of this RequestMapping.
        Value to supply for the specified Attribute

        :return: The value of this RequestMapping.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this RequestMapping.
        Value to supply for the specified Attribute

        :param value: The value of this RequestMapping.
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
