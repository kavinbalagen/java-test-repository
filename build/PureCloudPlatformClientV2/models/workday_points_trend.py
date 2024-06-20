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
    from . import UserReference
    from . import WorkdayPointsTrendItem

class WorkdayPointsTrend(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkdayPointsTrend - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date_start_workday': 'date',
            'date_end_workday': 'date',
            'user': 'UserReference',
            'day_of_week': 'str',
            'average_points': 'float',
            'trend': 'list[WorkdayPointsTrendItem]'
        }

        self.attribute_map = {
            'date_start_workday': 'dateStartWorkday',
            'date_end_workday': 'dateEndWorkday',
            'user': 'user',
            'day_of_week': 'dayOfWeek',
            'average_points': 'averagePoints',
            'trend': 'trend'
        }

        self._date_start_workday = None
        self._date_end_workday = None
        self._user = None
        self._day_of_week = None
        self._average_points = None
        self._trend = None

    @property
    def date_start_workday(self) -> date:
        """
        Gets the date_start_workday of this WorkdayPointsTrend.
        The start workday for the query range for the gamification points trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The date_start_workday of this WorkdayPointsTrend.
        :rtype: date
        """
        return self._date_start_workday

    @date_start_workday.setter
    def date_start_workday(self, date_start_workday: date) -> None:
        """
        Sets the date_start_workday of this WorkdayPointsTrend.
        The start workday for the query range for the gamification points trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param date_start_workday: The date_start_workday of this WorkdayPointsTrend.
        :type: date
        """
        

        self._date_start_workday = date_start_workday

    @property
    def date_end_workday(self) -> date:
        """
        Gets the date_end_workday of this WorkdayPointsTrend.
        The end workday for the query range for the gamification points trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The date_end_workday of this WorkdayPointsTrend.
        :rtype: date
        """
        return self._date_end_workday

    @date_end_workday.setter
    def date_end_workday(self, date_end_workday: date) -> None:
        """
        Sets the date_end_workday of this WorkdayPointsTrend.
        The end workday for the query range for the gamification points trend. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param date_end_workday: The date_end_workday of this WorkdayPointsTrend.
        :type: date
        """
        

        self._date_end_workday = date_end_workday

    @property
    def user(self) -> 'UserReference':
        """
        Gets the user of this WorkdayPointsTrend.
        The targeted user for the query

        :return: The user of this WorkdayPointsTrend.
        :rtype: UserReference
        """
        return self._user

    @user.setter
    def user(self, user: 'UserReference') -> None:
        """
        Sets the user of this WorkdayPointsTrend.
        The targeted user for the query

        :param user: The user of this WorkdayPointsTrend.
        :type: UserReference
        """
        

        self._user = user

    @property
    def day_of_week(self) -> str:
        """
        Gets the day_of_week of this WorkdayPointsTrend.
        Aggregated for same day comparison

        :return: The day_of_week of this WorkdayPointsTrend.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week: str) -> None:
        """
        Sets the day_of_week of this WorkdayPointsTrend.
        Aggregated for same day comparison

        :param day_of_week: The day_of_week of this WorkdayPointsTrend.
        :type: str
        """
        if isinstance(day_of_week, int):
            day_of_week = str(day_of_week)
        allowed_values = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if day_of_week.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for day_of_week -> " + day_of_week)
            self._day_of_week = "outdated_sdk_version"
        else:
            self._day_of_week = day_of_week

    @property
    def average_points(self) -> float:
        """
        Gets the average_points of this WorkdayPointsTrend.
        The total average points

        :return: The average_points of this WorkdayPointsTrend.
        :rtype: float
        """
        return self._average_points

    @average_points.setter
    def average_points(self, average_points: float) -> None:
        """
        Sets the average_points of this WorkdayPointsTrend.
        The total average points

        :param average_points: The average_points of this WorkdayPointsTrend.
        :type: float
        """
        

        self._average_points = average_points

    @property
    def trend(self) -> List['WorkdayPointsTrendItem']:
        """
        Gets the trend of this WorkdayPointsTrend.
        Daily points trends

        :return: The trend of this WorkdayPointsTrend.
        :rtype: list[WorkdayPointsTrendItem]
        """
        return self._trend

    @trend.setter
    def trend(self, trend: List['WorkdayPointsTrendItem']) -> None:
        """
        Sets the trend of this WorkdayPointsTrend.
        Daily points trends

        :param trend: The trend of this WorkdayPointsTrend.
        :type: list[WorkdayPointsTrendItem]
        """
        

        self._trend = trend

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

