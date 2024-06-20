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
    from . import BuAgentSchedulePublishedScheduleReference
    from . import BuAgentScheduleSearchResponse

class BuAgentSchedulesSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuAgentSchedulesSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'agent_schedules': 'list[BuAgentScheduleSearchResponse]',
            'business_unit_time_zone': 'str',
            'published_schedules': 'list[BuAgentSchedulePublishedScheduleReference]'
        }

        self.attribute_map = {
            'agent_schedules': 'agentSchedules',
            'business_unit_time_zone': 'businessUnitTimeZone',
            'published_schedules': 'publishedSchedules'
        }

        self._agent_schedules = None
        self._business_unit_time_zone = None
        self._published_schedules = None

    @property
    def agent_schedules(self) -> List['BuAgentScheduleSearchResponse']:
        """
        Gets the agent_schedules of this BuAgentSchedulesSearchResponse.
        The requested agent schedules

        :return: The agent_schedules of this BuAgentSchedulesSearchResponse.
        :rtype: list[BuAgentScheduleSearchResponse]
        """
        return self._agent_schedules

    @agent_schedules.setter
    def agent_schedules(self, agent_schedules: List['BuAgentScheduleSearchResponse']) -> None:
        """
        Sets the agent_schedules of this BuAgentSchedulesSearchResponse.
        The requested agent schedules

        :param agent_schedules: The agent_schedules of this BuAgentSchedulesSearchResponse.
        :type: list[BuAgentScheduleSearchResponse]
        """
        

        self._agent_schedules = agent_schedules

    @property
    def business_unit_time_zone(self) -> str:
        """
        Gets the business_unit_time_zone of this BuAgentSchedulesSearchResponse.
        The time zone configured for the business unit to which this schedule applies

        :return: The business_unit_time_zone of this BuAgentSchedulesSearchResponse.
        :rtype: str
        """
        return self._business_unit_time_zone

    @business_unit_time_zone.setter
    def business_unit_time_zone(self, business_unit_time_zone: str) -> None:
        """
        Sets the business_unit_time_zone of this BuAgentSchedulesSearchResponse.
        The time zone configured for the business unit to which this schedule applies

        :param business_unit_time_zone: The business_unit_time_zone of this BuAgentSchedulesSearchResponse.
        :type: str
        """
        

        self._business_unit_time_zone = business_unit_time_zone

    @property
    def published_schedules(self) -> List['BuAgentSchedulePublishedScheduleReference']:
        """
        Gets the published_schedules of this BuAgentSchedulesSearchResponse.
        References to all published week schedules overlapping the start/end date query parameters

        :return: The published_schedules of this BuAgentSchedulesSearchResponse.
        :rtype: list[BuAgentSchedulePublishedScheduleReference]
        """
        return self._published_schedules

    @published_schedules.setter
    def published_schedules(self, published_schedules: List['BuAgentSchedulePublishedScheduleReference']) -> None:
        """
        Sets the published_schedules of this BuAgentSchedulesSearchResponse.
        References to all published week schedules overlapping the start/end date query parameters

        :param published_schedules: The published_schedules of this BuAgentSchedulesSearchResponse.
        :type: list[BuAgentSchedulePublishedScheduleReference]
        """
        

        self._published_schedules = published_schedules

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
