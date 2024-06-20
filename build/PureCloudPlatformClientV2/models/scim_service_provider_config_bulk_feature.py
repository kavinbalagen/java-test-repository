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


class ScimServiceProviderConfigBulkFeature(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ScimServiceProviderConfigBulkFeature - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'supported': 'bool',
            'max_operations': 'int',
            'max_payload_size': 'int'
        }

        self.attribute_map = {
            'supported': 'supported',
            'max_operations': 'maxOperations',
            'max_payload_size': 'maxPayloadSize'
        }

        self._supported = None
        self._max_operations = None
        self._max_payload_size = None

    @property
    def supported(self) -> bool:
        """
        Gets the supported of this ScimServiceProviderConfigBulkFeature.
        Indicates whether configuration options are supported.

        :return: The supported of this ScimServiceProviderConfigBulkFeature.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported: bool) -> None:
        """
        Sets the supported of this ScimServiceProviderConfigBulkFeature.
        Indicates whether configuration options are supported.

        :param supported: The supported of this ScimServiceProviderConfigBulkFeature.
        :type: bool
        """
        

        self._supported = supported

    @property
    def max_operations(self) -> int:
        """
        Gets the max_operations of this ScimServiceProviderConfigBulkFeature.
        The maximum number of operations for each bulk request.

        :return: The max_operations of this ScimServiceProviderConfigBulkFeature.
        :rtype: int
        """
        return self._max_operations

    @max_operations.setter
    def max_operations(self, max_operations: int) -> None:
        """
        Sets the max_operations of this ScimServiceProviderConfigBulkFeature.
        The maximum number of operations for each bulk request.

        :param max_operations: The max_operations of this ScimServiceProviderConfigBulkFeature.
        :type: int
        """
        

        self._max_operations = max_operations

    @property
    def max_payload_size(self) -> int:
        """
        Gets the max_payload_size of this ScimServiceProviderConfigBulkFeature.
        The maximum payload size.

        :return: The max_payload_size of this ScimServiceProviderConfigBulkFeature.
        :rtype: int
        """
        return self._max_payload_size

    @max_payload_size.setter
    def max_payload_size(self, max_payload_size: int) -> None:
        """
        Sets the max_payload_size of this ScimServiceProviderConfigBulkFeature.
        The maximum payload size.

        :param max_payload_size: The max_payload_size of this ScimServiceProviderConfigBulkFeature.
        :type: int
        """
        

        self._max_payload_size = max_payload_size

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

