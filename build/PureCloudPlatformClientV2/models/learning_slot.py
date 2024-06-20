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


class LearningSlot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LearningSlot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date_start': 'datetime',
            'length_in_minutes': 'int',
            'staffing_difference': 'float',
            'difference_rating': 'str'
        }

        self.attribute_map = {
            'date_start': 'dateStart',
            'length_in_minutes': 'lengthInMinutes',
            'staffing_difference': 'staffingDifference',
            'difference_rating': 'differenceRating'
        }

        self._date_start = None
        self._length_in_minutes = None
        self._staffing_difference = None
        self._difference_rating = None

    @property
    def date_start(self) -> datetime:
        """
        Gets the date_start of this LearningSlot.
        Start date and time of scheduled Learning activity slot. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_start of this LearningSlot.
        :rtype: datetime
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: datetime) -> None:
        """
        Sets the date_start of this LearningSlot.
        Start date and time of scheduled Learning activity slot. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_start: The date_start of this LearningSlot.
        :type: datetime
        """
        

        self._date_start = date_start

    @property
    def length_in_minutes(self) -> int:
        """
        Gets the length_in_minutes of this LearningSlot.
        Length of Learning activity slot in minutes

        :return: The length_in_minutes of this LearningSlot.
        :rtype: int
        """
        return self._length_in_minutes

    @length_in_minutes.setter
    def length_in_minutes(self, length_in_minutes: int) -> None:
        """
        Sets the length_in_minutes of this LearningSlot.
        Length of Learning activity slot in minutes

        :param length_in_minutes: The length_in_minutes of this LearningSlot.
        :type: int
        """
        

        self._length_in_minutes = length_in_minutes

    @property
    def staffing_difference(self) -> float:
        """
        Gets the staffing_difference of this LearningSlot.
        Difference between scheduled and forecast headcount for this slot after scheduling the Learning activity

        :return: The staffing_difference of this LearningSlot.
        :rtype: float
        """
        return self._staffing_difference

    @staffing_difference.setter
    def staffing_difference(self, staffing_difference: float) -> None:
        """
        Sets the staffing_difference of this LearningSlot.
        Difference between scheduled and forecast headcount for this slot after scheduling the Learning activity

        :param staffing_difference: The staffing_difference of this LearningSlot.
        :type: float
        """
        

        self._staffing_difference = staffing_difference

    @property
    def difference_rating(self) -> str:
        """
        Gets the difference_rating of this LearningSlot.
        Rating based on the staffing difference for scheduled slot

        :return: The difference_rating of this LearningSlot.
        :rtype: str
        """
        return self._difference_rating

    @difference_rating.setter
    def difference_rating(self, difference_rating: str) -> None:
        """
        Sets the difference_rating of this LearningSlot.
        Rating based on the staffing difference for scheduled slot

        :param difference_rating: The difference_rating of this LearningSlot.
        :type: str
        """
        if isinstance(difference_rating, int):
            difference_rating = str(difference_rating)
        allowed_values = ["Poor", "Neutral", "Good"]
        if difference_rating.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for difference_rating -> " + difference_rating)
            self._difference_rating = "outdated_sdk_version"
        else:
            self._difference_rating = difference_rating

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

