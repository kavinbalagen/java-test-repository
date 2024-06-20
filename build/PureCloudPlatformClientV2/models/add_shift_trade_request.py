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


class AddShiftTradeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AddShiftTradeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'schedule_id': 'str',
            'initiating_shift_id': 'str',
            'receiving_user_id': 'str',
            'expiration': 'datetime',
            'acceptable_intervals': 'list[str]'
        }

        self.attribute_map = {
            'schedule_id': 'scheduleId',
            'initiating_shift_id': 'initiatingShiftId',
            'receiving_user_id': 'receivingUserId',
            'expiration': 'expiration',
            'acceptable_intervals': 'acceptableIntervals'
        }

        self._schedule_id = None
        self._initiating_shift_id = None
        self._receiving_user_id = None
        self._expiration = None
        self._acceptable_intervals = None

    @property
    def schedule_id(self) -> str:
        """
        Gets the schedule_id of this AddShiftTradeRequest.
        The ID of the schedule to which the initiating and receiving shifts belong

        :return: The schedule_id of this AddShiftTradeRequest.
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id: str) -> None:
        """
        Sets the schedule_id of this AddShiftTradeRequest.
        The ID of the schedule to which the initiating and receiving shifts belong

        :param schedule_id: The schedule_id of this AddShiftTradeRequest.
        :type: str
        """
        

        self._schedule_id = schedule_id

    @property
    def initiating_shift_id(self) -> str:
        """
        Gets the initiating_shift_id of this AddShiftTradeRequest.
        The ID of the shift that the initiating user wants to give up

        :return: The initiating_shift_id of this AddShiftTradeRequest.
        :rtype: str
        """
        return self._initiating_shift_id

    @initiating_shift_id.setter
    def initiating_shift_id(self, initiating_shift_id: str) -> None:
        """
        Sets the initiating_shift_id of this AddShiftTradeRequest.
        The ID of the shift that the initiating user wants to give up

        :param initiating_shift_id: The initiating_shift_id of this AddShiftTradeRequest.
        :type: str
        """
        

        self._initiating_shift_id = initiating_shift_id

    @property
    def receiving_user_id(self) -> str:
        """
        Gets the receiving_user_id of this AddShiftTradeRequest.
        The ID of the user to whom to send the request (for use in direct trade requests)

        :return: The receiving_user_id of this AddShiftTradeRequest.
        :rtype: str
        """
        return self._receiving_user_id

    @receiving_user_id.setter
    def receiving_user_id(self, receiving_user_id: str) -> None:
        """
        Sets the receiving_user_id of this AddShiftTradeRequest.
        The ID of the user to whom to send the request (for use in direct trade requests)

        :param receiving_user_id: The receiving_user_id of this AddShiftTradeRequest.
        :type: str
        """
        

        self._receiving_user_id = receiving_user_id

    @property
    def expiration(self) -> datetime:
        """
        Gets the expiration of this AddShiftTradeRequest.
        When this shift trade request should expire. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The expiration of this AddShiftTradeRequest.
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration: datetime) -> None:
        """
        Sets the expiration of this AddShiftTradeRequest.
        When this shift trade request should expire. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param expiration: The expiration of this AddShiftTradeRequest.
        :type: datetime
        """
        

        self._expiration = expiration

    @property
    def acceptable_intervals(self) -> List[str]:
        """
        Gets the acceptable_intervals of this AddShiftTradeRequest.
        The acceptable intervals the initiating user is willing to accept in trade.  Empty indicates the user is giving up the shift. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The acceptable_intervals of this AddShiftTradeRequest.
        :rtype: list[str]
        """
        return self._acceptable_intervals

    @acceptable_intervals.setter
    def acceptable_intervals(self, acceptable_intervals: List[str]) -> None:
        """
        Sets the acceptable_intervals of this AddShiftTradeRequest.
        The acceptable intervals the initiating user is willing to accept in trade.  Empty indicates the user is giving up the shift. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param acceptable_intervals: The acceptable_intervals of this AddShiftTradeRequest.
        :type: list[str]
        """
        

        self._acceptable_intervals = acceptable_intervals

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

