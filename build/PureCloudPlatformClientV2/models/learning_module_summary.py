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


class LearningModuleSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LearningModuleSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'assigned_count': 'int',
            'completed_count': 'int',
            'passed_count': 'int',
            'completed_sum': 'float'
        }

        self.attribute_map = {
            'assigned_count': 'assignedCount',
            'completed_count': 'completedCount',
            'passed_count': 'passedCount',
            'completed_sum': 'completedSum'
        }

        self._assigned_count = None
        self._completed_count = None
        self._passed_count = None
        self._completed_sum = None

    @property
    def assigned_count(self) -> int:
        """
        Gets the assigned_count of this LearningModuleSummary.
        The total number of assignments assigned for a learning module

        :return: The assigned_count of this LearningModuleSummary.
        :rtype: int
        """
        return self._assigned_count

    @assigned_count.setter
    def assigned_count(self, assigned_count: int) -> None:
        """
        Sets the assigned_count of this LearningModuleSummary.
        The total number of assignments assigned for a learning module

        :param assigned_count: The assigned_count of this LearningModuleSummary.
        :type: int
        """
        

        self._assigned_count = assigned_count

    @property
    def completed_count(self) -> int:
        """
        Gets the completed_count of this LearningModuleSummary.
        The number of assignments completed for a learning module

        :return: The completed_count of this LearningModuleSummary.
        :rtype: int
        """
        return self._completed_count

    @completed_count.setter
    def completed_count(self, completed_count: int) -> None:
        """
        Sets the completed_count of this LearningModuleSummary.
        The number of assignments completed for a learning module

        :param completed_count: The completed_count of this LearningModuleSummary.
        :type: int
        """
        

        self._completed_count = completed_count

    @property
    def passed_count(self) -> int:
        """
        Gets the passed_count of this LearningModuleSummary.
        The number of assignments passed for a learning module

        :return: The passed_count of this LearningModuleSummary.
        :rtype: int
        """
        return self._passed_count

    @passed_count.setter
    def passed_count(self, passed_count: int) -> None:
        """
        Sets the passed_count of this LearningModuleSummary.
        The number of assignments passed for a learning module

        :param passed_count: The passed_count of this LearningModuleSummary.
        :type: int
        """
        

        self._passed_count = passed_count

    @property
    def completed_sum(self) -> float:
        """
        Gets the completed_sum of this LearningModuleSummary.
        The sum of assignment scores for a learning module

        :return: The completed_sum of this LearningModuleSummary.
        :rtype: float
        """
        return self._completed_sum

    @completed_sum.setter
    def completed_sum(self, completed_sum: float) -> None:
        """
        Sets the completed_sum of this LearningModuleSummary.
        The sum of assignment scores for a learning module

        :param completed_sum: The completed_sum of this LearningModuleSummary.
        :type: float
        """
        

        self._completed_sum = completed_sum

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

