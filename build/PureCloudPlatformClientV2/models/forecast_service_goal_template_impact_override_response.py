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
    from . import WfmServiceGoalImpact

class ForecastServiceGoalTemplateImpactOverrideResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ForecastServiceGoalTemplateImpactOverrideResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'service_level': 'WfmServiceGoalImpact',
            'average_speed_of_answer': 'WfmServiceGoalImpact',
            'abandon_rate': 'WfmServiceGoalImpact'
        }

        self.attribute_map = {
            'service_level': 'serviceLevel',
            'average_speed_of_answer': 'averageSpeedOfAnswer',
            'abandon_rate': 'abandonRate'
        }

        self._service_level = None
        self._average_speed_of_answer = None
        self._abandon_rate = None

    @property
    def service_level(self) -> 'WfmServiceGoalImpact':
        """
        Gets the service_level of this ForecastServiceGoalTemplateImpactOverrideResponse.
        Allowed service level percent increase and decrease; undefined if the goal is not enabled

        :return: The service_level of this ForecastServiceGoalTemplateImpactOverrideResponse.
        :rtype: WfmServiceGoalImpact
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level: 'WfmServiceGoalImpact') -> None:
        """
        Sets the service_level of this ForecastServiceGoalTemplateImpactOverrideResponse.
        Allowed service level percent increase and decrease; undefined if the goal is not enabled

        :param service_level: The service_level of this ForecastServiceGoalTemplateImpactOverrideResponse.
        :type: WfmServiceGoalImpact
        """
        

        self._service_level = service_level

    @property
    def average_speed_of_answer(self) -> 'WfmServiceGoalImpact':
        """
        Gets the average_speed_of_answer of this ForecastServiceGoalTemplateImpactOverrideResponse.
        Allowed average speed of answer percent increase and decrease; undefined if the goal is not enabled

        :return: The average_speed_of_answer of this ForecastServiceGoalTemplateImpactOverrideResponse.
        :rtype: WfmServiceGoalImpact
        """
        return self._average_speed_of_answer

    @average_speed_of_answer.setter
    def average_speed_of_answer(self, average_speed_of_answer: 'WfmServiceGoalImpact') -> None:
        """
        Sets the average_speed_of_answer of this ForecastServiceGoalTemplateImpactOverrideResponse.
        Allowed average speed of answer percent increase and decrease; undefined if the goal is not enabled

        :param average_speed_of_answer: The average_speed_of_answer of this ForecastServiceGoalTemplateImpactOverrideResponse.
        :type: WfmServiceGoalImpact
        """
        

        self._average_speed_of_answer = average_speed_of_answer

    @property
    def abandon_rate(self) -> 'WfmServiceGoalImpact':
        """
        Gets the abandon_rate of this ForecastServiceGoalTemplateImpactOverrideResponse.
        Allowed abandon rate percent increase and decrease; undefined if the goal is not enabled

        :return: The abandon_rate of this ForecastServiceGoalTemplateImpactOverrideResponse.
        :rtype: WfmServiceGoalImpact
        """
        return self._abandon_rate

    @abandon_rate.setter
    def abandon_rate(self, abandon_rate: 'WfmServiceGoalImpact') -> None:
        """
        Sets the abandon_rate of this ForecastServiceGoalTemplateImpactOverrideResponse.
        Allowed abandon rate percent increase and decrease; undefined if the goal is not enabled

        :param abandon_rate: The abandon_rate of this ForecastServiceGoalTemplateImpactOverrideResponse.
        :type: WfmServiceGoalImpact
        """
        

        self._abandon_rate = abandon_rate

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

