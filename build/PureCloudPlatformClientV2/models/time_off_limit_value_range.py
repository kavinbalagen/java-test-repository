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
    from . import TimeOffLimitReference
    from . import WfmVersionedEntityMetadata

class TimeOffLimitValueRange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TimeOffLimitValueRange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'time_off_limit': 'TimeOffLimitReference',
            'start_date': 'date',
            'granularity': 'str',
            'limit_minutes_per_interval': 'list[int]',
            'allocated_minutes_per_interval': 'list[int]',
            'waitlisted_minutes_per_interval': 'list[int]',
            'waitlisted_requests_per_interval': 'list[int]',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'time_off_limit': 'timeOffLimit',
            'start_date': 'startDate',
            'granularity': 'granularity',
            'limit_minutes_per_interval': 'limitMinutesPerInterval',
            'allocated_minutes_per_interval': 'allocatedMinutesPerInterval',
            'waitlisted_minutes_per_interval': 'waitlistedMinutesPerInterval',
            'waitlisted_requests_per_interval': 'waitlistedRequestsPerInterval',
            'metadata': 'metadata'
        }

        self._time_off_limit = None
        self._start_date = None
        self._granularity = None
        self._limit_minutes_per_interval = None
        self._allocated_minutes_per_interval = None
        self._waitlisted_minutes_per_interval = None
        self._waitlisted_requests_per_interval = None
        self._metadata = None

    @property
    def time_off_limit(self) -> 'TimeOffLimitReference':
        """
        Gets the time_off_limit of this TimeOffLimitValueRange.
        The ID of the time off limit

        :return: The time_off_limit of this TimeOffLimitValueRange.
        :rtype: TimeOffLimitReference
        """
        return self._time_off_limit

    @time_off_limit.setter
    def time_off_limit(self, time_off_limit: 'TimeOffLimitReference') -> None:
        """
        Sets the time_off_limit of this TimeOffLimitValueRange.
        The ID of the time off limit

        :param time_off_limit: The time_off_limit of this TimeOffLimitValueRange.
        :type: TimeOffLimitReference
        """
        

        self._time_off_limit = time_off_limit

    @property
    def start_date(self) -> date:
        """
        Gets the start_date of this TimeOffLimitValueRange.
        Start date of the requested date range, in ISO-8601 format. The end date is determined by the size of interval lists

        :return: The start_date of this TimeOffLimitValueRange.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date) -> None:
        """
        Sets the start_date of this TimeOffLimitValueRange.
        Start date of the requested date range, in ISO-8601 format. The end date is determined by the size of interval lists

        :param start_date: The start_date of this TimeOffLimitValueRange.
        :type: date
        """
        

        self._start_date = start_date

    @property
    def granularity(self) -> str:
        """
        Gets the granularity of this TimeOffLimitValueRange.
        Granularity choice for time off limit

        :return: The granularity of this TimeOffLimitValueRange.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity: str) -> None:
        """
        Sets the granularity of this TimeOffLimitValueRange.
        Granularity choice for time off limit

        :param granularity: The granularity of this TimeOffLimitValueRange.
        :type: str
        """
        if isinstance(granularity, int):
            granularity = str(granularity)
        allowed_values = ["Daily"]
        if granularity.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for granularity -> " + granularity)
            self._granularity = "outdated_sdk_version"
        else:
            self._granularity = granularity

    @property
    def limit_minutes_per_interval(self) -> List[int]:
        """
        Gets the limit_minutes_per_interval of this TimeOffLimitValueRange.
        A list of time off limit values in minutes per granularity interval

        :return: The limit_minutes_per_interval of this TimeOffLimitValueRange.
        :rtype: list[int]
        """
        return self._limit_minutes_per_interval

    @limit_minutes_per_interval.setter
    def limit_minutes_per_interval(self, limit_minutes_per_interval: List[int]) -> None:
        """
        Sets the limit_minutes_per_interval of this TimeOffLimitValueRange.
        A list of time off limit values in minutes per granularity interval

        :param limit_minutes_per_interval: The limit_minutes_per_interval of this TimeOffLimitValueRange.
        :type: list[int]
        """
        

        self._limit_minutes_per_interval = limit_minutes_per_interval

    @property
    def allocated_minutes_per_interval(self) -> List[int]:
        """
        Gets the allocated_minutes_per_interval of this TimeOffLimitValueRange.
        A list of allocated time off minutes per granularity interval

        :return: The allocated_minutes_per_interval of this TimeOffLimitValueRange.
        :rtype: list[int]
        """
        return self._allocated_minutes_per_interval

    @allocated_minutes_per_interval.setter
    def allocated_minutes_per_interval(self, allocated_minutes_per_interval: List[int]) -> None:
        """
        Sets the allocated_minutes_per_interval of this TimeOffLimitValueRange.
        A list of allocated time off minutes per granularity interval

        :param allocated_minutes_per_interval: The allocated_minutes_per_interval of this TimeOffLimitValueRange.
        :type: list[int]
        """
        

        self._allocated_minutes_per_interval = allocated_minutes_per_interval

    @property
    def waitlisted_minutes_per_interval(self) -> List[int]:
        """
        Gets the waitlisted_minutes_per_interval of this TimeOffLimitValueRange.
        A list of waitlisted time off minutes per granularity interval

        :return: The waitlisted_minutes_per_interval of this TimeOffLimitValueRange.
        :rtype: list[int]
        """
        return self._waitlisted_minutes_per_interval

    @waitlisted_minutes_per_interval.setter
    def waitlisted_minutes_per_interval(self, waitlisted_minutes_per_interval: List[int]) -> None:
        """
        Sets the waitlisted_minutes_per_interval of this TimeOffLimitValueRange.
        A list of waitlisted time off minutes per granularity interval

        :param waitlisted_minutes_per_interval: The waitlisted_minutes_per_interval of this TimeOffLimitValueRange.
        :type: list[int]
        """
        

        self._waitlisted_minutes_per_interval = waitlisted_minutes_per_interval

    @property
    def waitlisted_requests_per_interval(self) -> List[int]:
        """
        Gets the waitlisted_requests_per_interval of this TimeOffLimitValueRange.
        The current number of waitlisted time off requests for every interval per granularity

        :return: The waitlisted_requests_per_interval of this TimeOffLimitValueRange.
        :rtype: list[int]
        """
        return self._waitlisted_requests_per_interval

    @waitlisted_requests_per_interval.setter
    def waitlisted_requests_per_interval(self, waitlisted_requests_per_interval: List[int]) -> None:
        """
        Sets the waitlisted_requests_per_interval of this TimeOffLimitValueRange.
        The current number of waitlisted time off requests for every interval per granularity

        :param waitlisted_requests_per_interval: The waitlisted_requests_per_interval of this TimeOffLimitValueRange.
        :type: list[int]
        """
        

        self._waitlisted_requests_per_interval = waitlisted_requests_per_interval

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this TimeOffLimitValueRange.
        Version metadata for the time off limit

        :return: The metadata of this TimeOffLimitValueRange.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this TimeOffLimitValueRange.
        Version metadata for the time off limit

        :param metadata: The metadata of this TimeOffLimitValueRange.
        :type: WfmVersionedEntityMetadata
        """
        

        self._metadata = metadata

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

