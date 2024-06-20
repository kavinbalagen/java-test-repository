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


class ExternalMetricDefinitionUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ExternalMetricDefinitionUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'precision': 'int',
            'default_objective_type': 'str',
            'enabled': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'precision': 'precision',
            'default_objective_type': 'defaultObjectiveType',
            'enabled': 'enabled'
        }

        self._name = None
        self._precision = None
        self._default_objective_type = None
        self._enabled = None

    @property
    def name(self) -> str:
        """
        Gets the name of this ExternalMetricDefinitionUpdateRequest.
        The name of the External Metric Definition

        :return: The name of this ExternalMetricDefinitionUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ExternalMetricDefinitionUpdateRequest.
        The name of the External Metric Definition

        :param name: The name of this ExternalMetricDefinitionUpdateRequest.
        :type: str
        """
        

        self._name = name

    @property
    def precision(self) -> int:
        """
        Gets the precision of this ExternalMetricDefinitionUpdateRequest.
        The decimal precision of the External Metric Definition. Must be at least 0 and at most 5

        :return: The precision of this ExternalMetricDefinitionUpdateRequest.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision: int) -> None:
        """
        Sets the precision of this ExternalMetricDefinitionUpdateRequest.
        The decimal precision of the External Metric Definition. Must be at least 0 and at most 5

        :param precision: The precision of this ExternalMetricDefinitionUpdateRequest.
        :type: int
        """
        
        if precision > 5:
            raise ValueError("Invalid value for `precision`, must be a value less than or equal to `5`")

        if precision < 0:
            raise ValueError("Invalid value for `precision`, must be a value greater than or equal to `0`")


        self._precision = precision

    @property
    def default_objective_type(self) -> str:
        """
        Gets the default_objective_type of this ExternalMetricDefinitionUpdateRequest.
        The default objective type of the External Metric Definition

        :return: The default_objective_type of this ExternalMetricDefinitionUpdateRequest.
        :rtype: str
        """
        return self._default_objective_type

    @default_objective_type.setter
    def default_objective_type(self, default_objective_type: str) -> None:
        """
        Sets the default_objective_type of this ExternalMetricDefinitionUpdateRequest.
        The default objective type of the External Metric Definition

        :param default_objective_type: The default_objective_type of this ExternalMetricDefinitionUpdateRequest.
        :type: str
        """
        if isinstance(default_objective_type, int):
            default_objective_type = str(default_objective_type)
        allowed_values = ["HigherIsBetter", "LowerIsBetter", "TargetArea"]
        if default_objective_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for default_objective_type -> " + default_objective_type)
            self._default_objective_type = "outdated_sdk_version"
        else:
            self._default_objective_type = default_objective_type

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this ExternalMetricDefinitionUpdateRequest.
        True if the External Metric Definition is enabled

        :return: The enabled of this ExternalMetricDefinitionUpdateRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this ExternalMetricDefinitionUpdateRequest.
        True if the External Metric Definition is enabled

        :param enabled: The enabled of this ExternalMetricDefinitionUpdateRequest.
        :type: bool
        """
        

        self._enabled = enabled

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

