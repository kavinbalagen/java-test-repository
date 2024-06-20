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
    from . import FlowCharacteristics

class FlowLogLevelCharacteristicsDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowLogLevelCharacteristicsDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'minimum_level': 'str',
            'depends_on': 'FlowCharacteristics'
        }

        self.attribute_map = {
            'id': 'id',
            'minimum_level': 'minimumLevel',
            'depends_on': 'dependsOn'
        }

        self._id = None
        self._minimum_level = None
        self._depends_on = None

    @property
    def id(self) -> str:
        """
        Gets the id of this FlowLogLevelCharacteristicsDefinition.
        The globally unique identifier for the object.

        :return: The id of this FlowLogLevelCharacteristicsDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this FlowLogLevelCharacteristicsDefinition.
        The globally unique identifier for the object.

        :param id: The id of this FlowLogLevelCharacteristicsDefinition.
        :type: str
        """
        

        self._id = id

    @property
    def minimum_level(self) -> str:
        """
        Gets the minimum_level of this FlowLogLevelCharacteristicsDefinition.
        The minimum level required for this characteristic to be enabled.

        :return: The minimum_level of this FlowLogLevelCharacteristicsDefinition.
        :rtype: str
        """
        return self._minimum_level

    @minimum_level.setter
    def minimum_level(self, minimum_level: str) -> None:
        """
        Sets the minimum_level of this FlowLogLevelCharacteristicsDefinition.
        The minimum level required for this characteristic to be enabled.

        :param minimum_level: The minimum_level of this FlowLogLevelCharacteristicsDefinition.
        :type: str
        """
        if isinstance(minimum_level, int):
            minimum_level = str(minimum_level)
        allowed_values = ["Unknown", "Disabled", "Base", "Notes", "VerboseNotes", "All"]
        if minimum_level.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for minimum_level -> " + minimum_level)
            self._minimum_level = "outdated_sdk_version"
        else:
            self._minimum_level = minimum_level

    @property
    def depends_on(self) -> 'FlowCharacteristics':
        """
        Gets the depends_on of this FlowLogLevelCharacteristicsDefinition.
        If set, this is the id of the characteristic that this one depends on and it must be enabled for this to be enabled.

        :return: The depends_on of this FlowLogLevelCharacteristicsDefinition.
        :rtype: FlowCharacteristics
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on: 'FlowCharacteristics') -> None:
        """
        Sets the depends_on of this FlowLogLevelCharacteristicsDefinition.
        If set, this is the id of the characteristic that this one depends on and it must be enabled for this to be enabled.

        :param depends_on: The depends_on of this FlowLogLevelCharacteristicsDefinition.
        :type: FlowCharacteristics
        """
        

        self._depends_on = depends_on

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

