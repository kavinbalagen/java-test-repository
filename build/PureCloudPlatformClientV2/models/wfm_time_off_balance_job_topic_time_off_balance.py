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


class WfmTimeOffBalanceJobTopicTimeOffBalance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmTimeOffBalanceJobTopicTimeOffBalance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_code_id': 'str',
            'hris_time_off_type_id': 'str',
            'hris_time_off_type_secondary_id': 'str',
            'start_date': 'datetime',
            'balance_minutes_per_day': 'list[int]'
        }

        self.attribute_map = {
            'activity_code_id': 'activityCodeId',
            'hris_time_off_type_id': 'hrisTimeOffTypeId',
            'hris_time_off_type_secondary_id': 'hrisTimeOffTypeSecondaryId',
            'start_date': 'startDate',
            'balance_minutes_per_day': 'balanceMinutesPerDay'
        }

        self._activity_code_id = None
        self._hris_time_off_type_id = None
        self._hris_time_off_type_secondary_id = None
        self._start_date = None
        self._balance_minutes_per_day = None

    @property
    def activity_code_id(self) -> str:
        """
        Gets the activity_code_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :return: The activity_code_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :rtype: str
        """
        return self._activity_code_id

    @activity_code_id.setter
    def activity_code_id(self, activity_code_id: str) -> None:
        """
        Sets the activity_code_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :param activity_code_id: The activity_code_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :type: str
        """
        

        self._activity_code_id = activity_code_id

    @property
    def hris_time_off_type_id(self) -> str:
        """
        Gets the hris_time_off_type_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :return: The hris_time_off_type_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :rtype: str
        """
        return self._hris_time_off_type_id

    @hris_time_off_type_id.setter
    def hris_time_off_type_id(self, hris_time_off_type_id: str) -> None:
        """
        Sets the hris_time_off_type_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :param hris_time_off_type_id: The hris_time_off_type_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :type: str
        """
        

        self._hris_time_off_type_id = hris_time_off_type_id

    @property
    def hris_time_off_type_secondary_id(self) -> str:
        """
        Gets the hris_time_off_type_secondary_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :return: The hris_time_off_type_secondary_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :rtype: str
        """
        return self._hris_time_off_type_secondary_id

    @hris_time_off_type_secondary_id.setter
    def hris_time_off_type_secondary_id(self, hris_time_off_type_secondary_id: str) -> None:
        """
        Sets the hris_time_off_type_secondary_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :param hris_time_off_type_secondary_id: The hris_time_off_type_secondary_id of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :type: str
        """
        

        self._hris_time_off_type_secondary_id = hris_time_off_type_secondary_id

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :return: The start_date of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :param start_date: The start_date of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def balance_minutes_per_day(self) -> List[int]:
        """
        Gets the balance_minutes_per_day of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :return: The balance_minutes_per_day of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :rtype: list[int]
        """
        return self._balance_minutes_per_day

    @balance_minutes_per_day.setter
    def balance_minutes_per_day(self, balance_minutes_per_day: List[int]) -> None:
        """
        Sets the balance_minutes_per_day of this WfmTimeOffBalanceJobTopicTimeOffBalance.


        :param balance_minutes_per_day: The balance_minutes_per_day of this WfmTimeOffBalanceJobTopicTimeOffBalance.
        :type: list[int]
        """
        

        self._balance_minutes_per_day = balance_minutes_per_day

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

