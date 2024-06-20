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
    from . import PossibleWorkShiftsForWeek

class AgentPossibleWorkShiftsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AgentPossibleWorkShiftsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'week_start_date': 'date',
            'pattern': 'list[int]',
            'weekly_possible_work_shifts': 'list[PossibleWorkShiftsForWeek]',
            'scheduler_interval_length_minutes': 'int',
            'time_zone': 'str'
        }

        self.attribute_map = {
            'week_start_date': 'weekStartDate',
            'pattern': 'pattern',
            'weekly_possible_work_shifts': 'weeklyPossibleWorkShifts',
            'scheduler_interval_length_minutes': 'schedulerIntervalLengthMinutes',
            'time_zone': 'timeZone'
        }

        self._week_start_date = None
        self._pattern = None
        self._weekly_possible_work_shifts = None
        self._scheduler_interval_length_minutes = None
        self._time_zone = None

    @property
    def week_start_date(self) -> date:
        """
        Gets the week_start_date of this AgentPossibleWorkShiftsResponse.
        Start date of requested effective work plan. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The week_start_date of this AgentPossibleWorkShiftsResponse.
        :rtype: date
        """
        return self._week_start_date

    @week_start_date.setter
    def week_start_date(self, week_start_date: date) -> None:
        """
        Sets the week_start_date of this AgentPossibleWorkShiftsResponse.
        Start date of requested effective work plan. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param week_start_date: The week_start_date of this AgentPossibleWorkShiftsResponse.
        :type: date
        """
        

        self._week_start_date = week_start_date

    @property
    def pattern(self) -> List[int]:
        """
        Gets the pattern of this AgentPossibleWorkShiftsResponse.
        Each element is the ID of an effective work plan for a specific week

        :return: The pattern of this AgentPossibleWorkShiftsResponse.
        :rtype: list[int]
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern: List[int]) -> None:
        """
        Sets the pattern of this AgentPossibleWorkShiftsResponse.
        Each element is the ID of an effective work plan for a specific week

        :param pattern: The pattern of this AgentPossibleWorkShiftsResponse.
        :type: list[int]
        """
        

        self._pattern = pattern

    @property
    def weekly_possible_work_shifts(self) -> List['PossibleWorkShiftsForWeek']:
        """
        Gets the weekly_possible_work_shifts of this AgentPossibleWorkShiftsResponse.
        Each element is a weekly effective work plan that can be used for multiple weeks

        :return: The weekly_possible_work_shifts of this AgentPossibleWorkShiftsResponse.
        :rtype: list[PossibleWorkShiftsForWeek]
        """
        return self._weekly_possible_work_shifts

    @weekly_possible_work_shifts.setter
    def weekly_possible_work_shifts(self, weekly_possible_work_shifts: List['PossibleWorkShiftsForWeek']) -> None:
        """
        Sets the weekly_possible_work_shifts of this AgentPossibleWorkShiftsResponse.
        Each element is a weekly effective work plan that can be used for multiple weeks

        :param weekly_possible_work_shifts: The weekly_possible_work_shifts of this AgentPossibleWorkShiftsResponse.
        :type: list[PossibleWorkShiftsForWeek]
        """
        

        self._weekly_possible_work_shifts = weekly_possible_work_shifts

    @property
    def scheduler_interval_length_minutes(self) -> int:
        """
        Gets the scheduler_interval_length_minutes of this AgentPossibleWorkShiftsResponse.
        Number of minutes in each interval in the intervalScheduleProbabilities

        :return: The scheduler_interval_length_minutes of this AgentPossibleWorkShiftsResponse.
        :rtype: int
        """
        return self._scheduler_interval_length_minutes

    @scheduler_interval_length_minutes.setter
    def scheduler_interval_length_minutes(self, scheduler_interval_length_minutes: int) -> None:
        """
        Sets the scheduler_interval_length_minutes of this AgentPossibleWorkShiftsResponse.
        Number of minutes in each interval in the intervalScheduleProbabilities

        :param scheduler_interval_length_minutes: The scheduler_interval_length_minutes of this AgentPossibleWorkShiftsResponse.
        :type: int
        """
        

        self._scheduler_interval_length_minutes = scheduler_interval_length_minutes

    @property
    def time_zone(self) -> str:
        """
        Gets the time_zone of this AgentPossibleWorkShiftsResponse.
        The time zone of the business unit

        :return: The time_zone of this AgentPossibleWorkShiftsResponse.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone: str) -> None:
        """
        Sets the time_zone of this AgentPossibleWorkShiftsResponse.
        The time zone of the business unit

        :param time_zone: The time_zone of this AgentPossibleWorkShiftsResponse.
        :type: str
        """
        

        self._time_zone = time_zone

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

