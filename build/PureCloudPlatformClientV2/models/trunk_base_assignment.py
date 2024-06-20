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
    from . import TrunkBase

class TrunkBaseAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrunkBaseAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'family': 'int',
            'trunk_base': 'TrunkBase'
        }

        self.attribute_map = {
            'family': 'family',
            'trunk_base': 'trunkBase'
        }

        self._family = None
        self._trunk_base = None

    @property
    def family(self) -> int:
        """
        Gets the family of this TrunkBaseAssignment.
        The address family to use with the trunk base settings. 2=IPv4, 23=IPv6

        :return: The family of this TrunkBaseAssignment.
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family: int) -> None:
        """
        Sets the family of this TrunkBaseAssignment.
        The address family to use with the trunk base settings. 2=IPv4, 23=IPv6

        :param family: The family of this TrunkBaseAssignment.
        :type: int
        """
        

        self._family = family

    @property
    def trunk_base(self) -> 'TrunkBase':
        """
        Gets the trunk_base of this TrunkBaseAssignment.
        A trunk base settings reference.

        :return: The trunk_base of this TrunkBaseAssignment.
        :rtype: TrunkBase
        """
        return self._trunk_base

    @trunk_base.setter
    def trunk_base(self, trunk_base: 'TrunkBase') -> None:
        """
        Sets the trunk_base of this TrunkBaseAssignment.
        A trunk base settings reference.

        :param trunk_base: The trunk_base of this TrunkBaseAssignment.
        :type: TrunkBase
        """
        

        self._trunk_base = trunk_base

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
