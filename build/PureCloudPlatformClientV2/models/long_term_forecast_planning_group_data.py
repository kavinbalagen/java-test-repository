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


class LongTermForecastPlanningGroupData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LongTermForecastPlanningGroupData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'planning_group_id': 'str',
            'offered_per_day': 'list[float]',
            'average_handle_time_seconds_per_day': 'list[float]'
        }

        self.attribute_map = {
            'planning_group_id': 'planningGroupId',
            'offered_per_day': 'offeredPerDay',
            'average_handle_time_seconds_per_day': 'averageHandleTimeSecondsPerDay'
        }

        self._planning_group_id = None
        self._offered_per_day = None
        self._average_handle_time_seconds_per_day = None

    @property
    def planning_group_id(self) -> str:
        """
        Gets the planning_group_id of this LongTermForecastPlanningGroupData.
        The ID of the planning group to which this data applies. Note this is a snapshot of the planning group at the time of forecast creation and may not correspond to the current configuration

        :return: The planning_group_id of this LongTermForecastPlanningGroupData.
        :rtype: str
        """
        return self._planning_group_id

    @planning_group_id.setter
    def planning_group_id(self, planning_group_id: str) -> None:
        """
        Sets the planning_group_id of this LongTermForecastPlanningGroupData.
        The ID of the planning group to which this data applies. Note this is a snapshot of the planning group at the time of forecast creation and may not correspond to the current configuration

        :param planning_group_id: The planning_group_id of this LongTermForecastPlanningGroupData.
        :type: str
        """
        

        self._planning_group_id = planning_group_id

    @property
    def offered_per_day(self) -> List[float]:
        """
        Gets the offered_per_day of this LongTermForecastPlanningGroupData.
        Forecast offered counts per day for this planning group

        :return: The offered_per_day of this LongTermForecastPlanningGroupData.
        :rtype: list[float]
        """
        return self._offered_per_day

    @offered_per_day.setter
    def offered_per_day(self, offered_per_day: List[float]) -> None:
        """
        Sets the offered_per_day of this LongTermForecastPlanningGroupData.
        Forecast offered counts per day for this planning group

        :param offered_per_day: The offered_per_day of this LongTermForecastPlanningGroupData.
        :type: list[float]
        """
        

        self._offered_per_day = offered_per_day

    @property
    def average_handle_time_seconds_per_day(self) -> List[float]:
        """
        Gets the average_handle_time_seconds_per_day of this LongTermForecastPlanningGroupData.
        Forecast average handle time per day in seconds

        :return: The average_handle_time_seconds_per_day of this LongTermForecastPlanningGroupData.
        :rtype: list[float]
        """
        return self._average_handle_time_seconds_per_day

    @average_handle_time_seconds_per_day.setter
    def average_handle_time_seconds_per_day(self, average_handle_time_seconds_per_day: List[float]) -> None:
        """
        Sets the average_handle_time_seconds_per_day of this LongTermForecastPlanningGroupData.
        Forecast average handle time per day in seconds

        :param average_handle_time_seconds_per_day: The average_handle_time_seconds_per_day of this LongTermForecastPlanningGroupData.
        :type: list[float]
        """
        

        self._average_handle_time_seconds_per_day = average_handle_time_seconds_per_day

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

