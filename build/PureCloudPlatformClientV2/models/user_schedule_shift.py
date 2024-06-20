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
    from . import UserScheduleActivity
    from . import WeekScheduleReference

class UserScheduleShift(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UserScheduleShift - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'week_schedule': 'WeekScheduleReference',
            'id': 'str',
            'start_date': 'datetime',
            'length_in_minutes': 'int',
            'activities': 'list[UserScheduleActivity]',
            'delete': 'bool',
            'manually_edited': 'bool'
        }

        self.attribute_map = {
            'week_schedule': 'weekSchedule',
            'id': 'id',
            'start_date': 'startDate',
            'length_in_minutes': 'lengthInMinutes',
            'activities': 'activities',
            'delete': 'delete',
            'manually_edited': 'manuallyEdited'
        }

        self._week_schedule = None
        self._id = None
        self._start_date = None
        self._length_in_minutes = None
        self._activities = None
        self._delete = None
        self._manually_edited = None

    @property
    def week_schedule(self) -> 'WeekScheduleReference':
        """
        Gets the week_schedule of this UserScheduleShift.
        The schedule to which this shift belongs

        :return: The week_schedule of this UserScheduleShift.
        :rtype: WeekScheduleReference
        """
        return self._week_schedule

    @week_schedule.setter
    def week_schedule(self, week_schedule: 'WeekScheduleReference') -> None:
        """
        Sets the week_schedule of this UserScheduleShift.
        The schedule to which this shift belongs

        :param week_schedule: The week_schedule of this UserScheduleShift.
        :type: WeekScheduleReference
        """
        

        self._week_schedule = week_schedule

    @property
    def id(self) -> str:
        """
        Gets the id of this UserScheduleShift.
        ID of the schedule shift. This is only for the case of updating and deleting an existing shift

        :return: The id of this UserScheduleShift.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this UserScheduleShift.
        ID of the schedule shift. This is only for the case of updating and deleting an existing shift

        :param id: The id of this UserScheduleShift.
        :type: str
        """
        

        self._id = id

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this UserScheduleShift.
        Start time in UTC for this shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The start_date of this UserScheduleShift.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this UserScheduleShift.
        Start time in UTC for this shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param start_date: The start_date of this UserScheduleShift.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def length_in_minutes(self) -> int:
        """
        Gets the length_in_minutes of this UserScheduleShift.
        Length of this shift in minutes

        :return: The length_in_minutes of this UserScheduleShift.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes: int) -> None:
        """
        Sets the length_in_minutes of this UserScheduleShift.
        Length of this shift in minutes

        :param length_in_minutes: The length_in_minutes of this UserScheduleShift.
        :type: int
        """
        

        self._length_in_minutes = length_in_minutes

    @property
    def activities(self) -> List['UserScheduleActivity']:
        """
        Gets the activities of this UserScheduleShift.
        List of activities in this shift

        :return: The activities of this UserScheduleShift.
        :rtype: list[UserScheduleActivity]
        """
        return self._activities

    @activities.setter
    def activities(self, activities: List['UserScheduleActivity']) -> None:
        """
        Sets the activities of this UserScheduleShift.
        List of activities in this shift

        :param activities: The activities of this UserScheduleShift.
        :type: list[UserScheduleActivity]
        """
        

        self._activities = activities

    @property
    def delete(self) -> bool:
        """
        Gets the delete of this UserScheduleShift.
        If marked true for updating this schedule shift, it will be deleted

        :return: The delete of this UserScheduleShift.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete: bool) -> None:
        """
        Sets the delete of this UserScheduleShift.
        If marked true for updating this schedule shift, it will be deleted

        :param delete: The delete of this UserScheduleShift.
        :type: bool
        """
        

        self._delete = delete

    @property
    def manually_edited(self) -> bool:
        """
        Gets the manually_edited of this UserScheduleShift.
        Whether the shift was set as manually edited

        :return: The manually_edited of this UserScheduleShift.
        :rtype: bool
        """
        return self._manually_edited

    @manually_edited.setter
    def manually_edited(self, manually_edited: bool) -> None:
        """
        Sets the manually_edited of this UserScheduleShift.
        Whether the shift was set as manually edited

        :param manually_edited: The manually_edited of this UserScheduleShift.
        :type: bool
        """
        

        self._manually_edited = manually_edited

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

