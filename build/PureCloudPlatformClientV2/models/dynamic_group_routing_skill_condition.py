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
    from . import DynamicGroupSkillCondition

class DynamicGroupRoutingSkillCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DynamicGroupRoutingSkillCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'routing_skill': 'str',
            'comparator': 'str',
            'proficiency': 'int',
            'child_conditions': 'list[DynamicGroupSkillCondition]'
        }

        self.attribute_map = {
            'routing_skill': 'routingSkill',
            'comparator': 'comparator',
            'proficiency': 'proficiency',
            'child_conditions': 'childConditions'
        }

        self._routing_skill = None
        self._comparator = None
        self._proficiency = None
        self._child_conditions = None

    @property
    def routing_skill(self) -> str:
        """
        Gets the routing_skill of this DynamicGroupRoutingSkillCondition.
        The routing skill to be used in the skill condition query

        :return: The routing_skill of this DynamicGroupRoutingSkillCondition.
        :rtype: str
        """
        return self._routing_skill

    @routing_skill.setter
    def routing_skill(self, routing_skill: str) -> None:
        """
        Sets the routing_skill of this DynamicGroupRoutingSkillCondition.
        The routing skill to be used in the skill condition query

        :param routing_skill: The routing_skill of this DynamicGroupRoutingSkillCondition.
        :type: str
        """
        

        self._routing_skill = routing_skill

    @property
    def comparator(self) -> str:
        """
        Gets the comparator of this DynamicGroupRoutingSkillCondition.
        Comparator that will be applied to the proficiency

        :return: The comparator of this DynamicGroupRoutingSkillCondition.
        :rtype: str
        """
        return self._comparator

    @comparator.setter
    def comparator(self, comparator: str) -> None:
        """
        Sets the comparator of this DynamicGroupRoutingSkillCondition.
        Comparator that will be applied to the proficiency

        :param comparator: The comparator of this DynamicGroupRoutingSkillCondition.
        :type: str
        """
        if isinstance(comparator, int):
            comparator = str(comparator)
        allowed_values = ["EqualTo", "NotEqualTo", "LessThan", "GreaterThan", "GreaterThanOrEqualTo", "LessThanOrEqualTo"]
        if comparator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for comparator -> " + comparator)
            self._comparator = "outdated_sdk_version"
        else:
            self._comparator = comparator

    @property
    def proficiency(self) -> int:
        """
        Gets the proficiency of this DynamicGroupRoutingSkillCondition.
        The skill proficiency that will be used for the routing skill. Integer range 0-5

        :return: The proficiency of this DynamicGroupRoutingSkillCondition.
        :rtype: int
        """
        return self._proficiency

    @proficiency.setter
    def proficiency(self, proficiency: int) -> None:
        """
        Sets the proficiency of this DynamicGroupRoutingSkillCondition.
        The skill proficiency that will be used for the routing skill. Integer range 0-5

        :param proficiency: The proficiency of this DynamicGroupRoutingSkillCondition.
        :type: int
        """
        

        self._proficiency = proficiency

    @property
    def child_conditions(self) -> List['DynamicGroupSkillCondition']:
        """
        Gets the child_conditions of this DynamicGroupRoutingSkillCondition.
        Nested conditions to be applied to this skill condition

        :return: The child_conditions of this DynamicGroupRoutingSkillCondition.
        :rtype: list[DynamicGroupSkillCondition]
        """
        return self._child_conditions

    @child_conditions.setter
    def child_conditions(self, child_conditions: List['DynamicGroupSkillCondition']) -> None:
        """
        Sets the child_conditions of this DynamicGroupRoutingSkillCondition.
        Nested conditions to be applied to this skill condition

        :param child_conditions: The child_conditions of this DynamicGroupRoutingSkillCondition.
        :type: list[DynamicGroupSkillCondition]
        """
        

        self._child_conditions = child_conditions

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

