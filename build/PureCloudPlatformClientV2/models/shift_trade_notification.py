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

class ShiftTradeNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ShiftTradeNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'week_date': 'str',
            'trade_id': 'str',
            'one_sided': 'bool',
            'new_state': 'str',
            'initiating_user': 'UserReference',
            'initiating_shift_date': 'datetime',
            'receiving_user': 'UserReference',
            'receiving_shift_date': 'datetime'
        }

        self.attribute_map = {
            'week_date': 'weekDate',
            'trade_id': 'tradeId',
            'one_sided': 'oneSided',
            'new_state': 'newState',
            'initiating_user': 'initiatingUser',
            'initiating_shift_date': 'initiatingShiftDate',
            'receiving_user': 'receivingUser',
            'receiving_shift_date': 'receivingShiftDate'
        }

        self._week_date = None
        self._trade_id = None
        self._one_sided = None
        self._new_state = None
        self._initiating_user = None
        self._initiating_shift_date = None
        self._receiving_user = None
        self._receiving_shift_date = None

    @property
    def week_date(self) -> str:
        """
        Gets the week_date of this ShiftTradeNotification.
        The start date of the schedule with which this trade is associated

        :return: The week_date of this ShiftTradeNotification.
        :rtype: str
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date: str) -> None:
        """
        Sets the week_date of this ShiftTradeNotification.
        The start date of the schedule with which this trade is associated

        :param week_date: The week_date of this ShiftTradeNotification.
        :type: str
        """
        

        self._week_date = week_date

    @property
    def trade_id(self) -> str:
        """
        Gets the trade_id of this ShiftTradeNotification.
        The ID of the shift trade

        :return: The trade_id of this ShiftTradeNotification.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id: str) -> None:
        """
        Sets the trade_id of this ShiftTradeNotification.
        The ID of the shift trade

        :param trade_id: The trade_id of this ShiftTradeNotification.
        :type: str
        """
        

        self._trade_id = trade_id

    @property
    def one_sided(self) -> bool:
        """
        Gets the one_sided of this ShiftTradeNotification.
        Whether this is a one sided shift trade

        :return: The one_sided of this ShiftTradeNotification.
        :rtype: bool
        """
        return self._one_sided

    @one_sided.setter
    def one_sided(self, one_sided: bool) -> None:
        """
        Sets the one_sided of this ShiftTradeNotification.
        Whether this is a one sided shift trade

        :param one_sided: The one_sided of this ShiftTradeNotification.
        :type: bool
        """
        

        self._one_sided = one_sided

    @property
    def new_state(self) -> str:
        """
        Gets the new_state of this ShiftTradeNotification.
        The new state of the shift trade, null if there was no change

        :return: The new_state of this ShiftTradeNotification.
        :rtype: str
        """
        return self._new_state

    @new_state.setter
    def new_state(self, new_state: str) -> None:
        """
        Sets the new_state of this ShiftTradeNotification.
        The new state of the shift trade, null if there was no change

        :param new_state: The new_state of this ShiftTradeNotification.
        :type: str
        """
        if isinstance(new_state, int):
            new_state = str(new_state)
        allowed_values = ["Unmatched", "Matched", "Approved", "Denied", "Expired", "Canceled"]
        if new_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for new_state -> " + new_state)
            self._new_state = "outdated_sdk_version"
        else:
            self._new_state = new_state

    @property
    def initiating_user(self) -> 'UserReference':
        """
        Gets the initiating_user of this ShiftTradeNotification.
        The user who initiated the shift trade

        :return: The initiating_user of this ShiftTradeNotification.
        :rtype: UserReference
        """
        return self._initiating_user

    @initiating_user.setter
    def initiating_user(self, initiating_user: 'UserReference') -> None:
        """
        Sets the initiating_user of this ShiftTradeNotification.
        The user who initiated the shift trade

        :param initiating_user: The initiating_user of this ShiftTradeNotification.
        :type: UserReference
        """
        

        self._initiating_user = initiating_user

    @property
    def initiating_shift_date(self) -> datetime:
        """
        Gets the initiating_shift_date of this ShiftTradeNotification.
        The start date and time of the initiating shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The initiating_shift_date of this ShiftTradeNotification.
        :rtype: datetime
        """
        return self._initiating_shift_date

    @initiating_shift_date.setter
    def initiating_shift_date(self, initiating_shift_date: datetime) -> None:
        """
        Sets the initiating_shift_date of this ShiftTradeNotification.
        The start date and time of the initiating shift. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param initiating_shift_date: The initiating_shift_date of this ShiftTradeNotification.
        :type: datetime
        """
        

        self._initiating_shift_date = initiating_shift_date

    @property
    def receiving_user(self) -> 'UserReference':
        """
        Gets the receiving_user of this ShiftTradeNotification.
        The user on the receiving side of this shift trade (null if not matched)

        :return: The receiving_user of this ShiftTradeNotification.
        :rtype: UserReference
        """
        return self._receiving_user

    @receiving_user.setter
    def receiving_user(self, receiving_user: 'UserReference') -> None:
        """
        Sets the receiving_user of this ShiftTradeNotification.
        The user on the receiving side of this shift trade (null if not matched)

        :param receiving_user: The receiving_user of this ShiftTradeNotification.
        :type: UserReference
        """
        

        self._receiving_user = receiving_user

    @property
    def receiving_shift_date(self) -> datetime:
        """
        Gets the receiving_shift_date of this ShiftTradeNotification.
        The start date and time of the receiving shift (null if not matched or if one-sided. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The receiving_shift_date of this ShiftTradeNotification.
        :rtype: datetime
        """
        return self._receiving_shift_date

    @receiving_shift_date.setter
    def receiving_shift_date(self, receiving_shift_date: datetime) -> None:
        """
        Sets the receiving_shift_date of this ShiftTradeNotification.
        The start date and time of the receiving shift (null if not matched or if one-sided. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param receiving_shift_date: The receiving_shift_date of this ShiftTradeNotification.
        :type: datetime
        """
        

        self._receiving_shift_date = receiving_shift_date

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

