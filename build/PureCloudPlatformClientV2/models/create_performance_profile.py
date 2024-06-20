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
    from . import ReportingInterval
    from . import WritableDivision

class CreatePerformanceProfile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreatePerformanceProfile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'WritableDivision',
            'description': 'str',
            'metric_orders': 'list[str]',
            'date_created': 'datetime',
            'reporting_intervals': 'list[ReportingInterval]',
            'active': 'bool',
            'member_count': 'int',
            'max_leaderboard_rank_size': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'description': 'description',
            'metric_orders': 'metricOrders',
            'date_created': 'dateCreated',
            'reporting_intervals': 'reportingIntervals',
            'active': 'active',
            'member_count': 'memberCount',
            'max_leaderboard_rank_size': 'maxLeaderboardRankSize',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._description = None
        self._metric_orders = None
        self._date_created = None
        self._reporting_intervals = None
        self._active = None
        self._member_count = None
        self._max_leaderboard_rank_size = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this CreatePerformanceProfile.
        The globally unique identifier for the object.

        :return: The id of this CreatePerformanceProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this CreatePerformanceProfile.
        The globally unique identifier for the object.

        :param id: The id of this CreatePerformanceProfile.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this CreatePerformanceProfile.
        A name for this performance profile

        :return: The name of this CreatePerformanceProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this CreatePerformanceProfile.
        A name for this performance profile

        :param name: The name of this CreatePerformanceProfile.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'WritableDivision':
        """
        Gets the division of this CreatePerformanceProfile.
        The associated division for this Performance Profile

        :return: The division of this CreatePerformanceProfile.
        :rtype: WritableDivision
        """
        return self._division

    @division.setter
    def division(self, division: 'WritableDivision') -> None:
        """
        Sets the division of this CreatePerformanceProfile.
        The associated division for this Performance Profile

        :param division: The division of this CreatePerformanceProfile.
        :type: WritableDivision
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this CreatePerformanceProfile.
        A description about this performance profile

        :return: The description of this CreatePerformanceProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this CreatePerformanceProfile.
        A description about this performance profile

        :param description: The description of this CreatePerformanceProfile.
        :type: str
        """
        

        self._description = description

    @property
    def metric_orders(self) -> List[str]:
        """
        Gets the metric_orders of this CreatePerformanceProfile.
        Order of the associated metrics. The list should contain valid ids for metrics

        :return: The metric_orders of this CreatePerformanceProfile.
        :rtype: list[str]
        """
        return self._metric_orders

    @metric_orders.setter
    def metric_orders(self, metric_orders: List[str]) -> None:
        """
        Sets the metric_orders of this CreatePerformanceProfile.
        Order of the associated metrics. The list should contain valid ids for metrics

        :param metric_orders: The metric_orders of this CreatePerformanceProfile.
        :type: list[str]
        """
        

        self._metric_orders = metric_orders

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this CreatePerformanceProfile.
        Creation date for this performance profile. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this CreatePerformanceProfile.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this CreatePerformanceProfile.
        Creation date for this performance profile. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this CreatePerformanceProfile.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def reporting_intervals(self) -> List['ReportingInterval']:
        """
        Gets the reporting_intervals of this CreatePerformanceProfile.
        The reporting interval periods for this performance profile

        :return: The reporting_intervals of this CreatePerformanceProfile.
        :rtype: list[ReportingInterval]
        """
        return self._reporting_intervals

    @reporting_intervals.setter
    def reporting_intervals(self, reporting_intervals: List['ReportingInterval']) -> None:
        """
        Sets the reporting_intervals of this CreatePerformanceProfile.
        The reporting interval periods for this performance profile

        :param reporting_intervals: The reporting_intervals of this CreatePerformanceProfile.
        :type: list[ReportingInterval]
        """
        

        self._reporting_intervals = reporting_intervals

    @property
    def active(self) -> bool:
        """
        Gets the active of this CreatePerformanceProfile.
        The flag for active profiles

        :return: The active of this CreatePerformanceProfile.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active: bool) -> None:
        """
        Sets the active of this CreatePerformanceProfile.
        The flag for active profiles

        :param active: The active of this CreatePerformanceProfile.
        :type: bool
        """
        

        self._active = active

    @property
    def member_count(self) -> int:
        """
        Gets the member_count of this CreatePerformanceProfile.
        The number of members in this performance profile

        :return: The member_count of this CreatePerformanceProfile.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count: int) -> None:
        """
        Sets the member_count of this CreatePerformanceProfile.
        The number of members in this performance profile

        :param member_count: The member_count of this CreatePerformanceProfile.
        :type: int
        """
        

        self._member_count = member_count

    @property
    def max_leaderboard_rank_size(self) -> int:
        """
        Gets the max_leaderboard_rank_size of this CreatePerformanceProfile.
        The maximum rank size for the leaderboard. This counts the number of ranks can be retrieved in a leaderboard queries

        :return: The max_leaderboard_rank_size of this CreatePerformanceProfile.
        :rtype: int
        """
        return self._max_leaderboard_rank_size

    @max_leaderboard_rank_size.setter
    def max_leaderboard_rank_size(self, max_leaderboard_rank_size: int) -> None:
        """
        Sets the max_leaderboard_rank_size of this CreatePerformanceProfile.
        The maximum rank size for the leaderboard. This counts the number of ranks can be retrieved in a leaderboard queries

        :param max_leaderboard_rank_size: The max_leaderboard_rank_size of this CreatePerformanceProfile.
        :type: int
        """
        

        self._max_leaderboard_rank_size = max_leaderboard_rank_size

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this CreatePerformanceProfile.
        The URI for this object

        :return: The self_uri of this CreatePerformanceProfile.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this CreatePerformanceProfile.
        The URI for this object

        :param self_uri: The self_uri of this CreatePerformanceProfile.
        :type: str
        """
        

        self._self_uri = self_uri

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

