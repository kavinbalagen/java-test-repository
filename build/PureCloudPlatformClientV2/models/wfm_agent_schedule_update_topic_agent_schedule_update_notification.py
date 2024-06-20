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
    from . import WfmAgentScheduleUpdateTopicAgentScheduleShiftUpdate
    from . import WfmAgentScheduleUpdateTopicUserReference

class WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'WfmAgentScheduleUpdateTopicUserReference',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'updates': 'list[WfmAgentScheduleUpdateTopicAgentScheduleShiftUpdate]'
        }

        self.attribute_map = {
            'user': 'user',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'updates': 'updates'
        }

        self._user = None
        self._start_date = None
        self._end_date = None
        self._updates = None

    @property
    def user(self) -> 'WfmAgentScheduleUpdateTopicUserReference':
        """
        Gets the user of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :return: The user of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :rtype: WfmAgentScheduleUpdateTopicUserReference
        """
        return self._user

    @user.setter
    def user(self, user: 'WfmAgentScheduleUpdateTopicUserReference') -> None:
        """
        Sets the user of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :param user: The user of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :type: WfmAgentScheduleUpdateTopicUserReference
        """
        

        self._user = user

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :return: The start_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :param start_date: The start_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def end_date(self) -> datetime:
        """
        Gets the end_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :return: The end_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime) -> None:
        """
        Sets the end_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :param end_date: The end_date of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :type: datetime
        """
        

        self._end_date = end_date

    @property
    def updates(self) -> List['WfmAgentScheduleUpdateTopicAgentScheduleShiftUpdate']:
        """
        Gets the updates of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :return: The updates of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :rtype: list[WfmAgentScheduleUpdateTopicAgentScheduleShiftUpdate]
        """
        return self._updates

    @updates.setter
    def updates(self, updates: List['WfmAgentScheduleUpdateTopicAgentScheduleShiftUpdate']) -> None:
        """
        Sets the updates of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.


        :param updates: The updates of this WfmAgentScheduleUpdateTopicAgentScheduleUpdateNotification.
        :type: list[WfmAgentScheduleUpdateTopicAgentScheduleShiftUpdate]
        """
        

        self._updates = updates

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

