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
    from . import AddressableEntityRef
    from . import DivisionReference
    from . import InsightsTrendMetricItem
    from . import InsightsTrendTotalItem
    from . import WorkdayPeriod

class InsightsTrend(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        InsightsTrend - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'performance_profile': 'AddressableEntityRef',
            'division': 'DivisionReference',
            'granularity': 'str',
            'comparative_period': 'WorkdayPeriod',
            'primary_period': 'WorkdayPeriod',
            'entities': 'list[InsightsTrendMetricItem]',
            'total': 'InsightsTrendTotalItem'
        }

        self.attribute_map = {
            'performance_profile': 'performanceProfile',
            'division': 'division',
            'granularity': 'granularity',
            'comparative_period': 'comparativePeriod',
            'primary_period': 'primaryPeriod',
            'entities': 'entities',
            'total': 'total'
        }

        self._performance_profile = None
        self._division = None
        self._granularity = None
        self._comparative_period = None
        self._primary_period = None
        self._entities = None
        self._total = None

    @property
    def performance_profile(self) -> 'AddressableEntityRef':
        """
        Gets the performance_profile of this InsightsTrend.
        The performance profile

        :return: The performance_profile of this InsightsTrend.
        :rtype: AddressableEntityRef
        """
        return self._performance_profile

    @performance_profile.setter
    def performance_profile(self, performance_profile: 'AddressableEntityRef') -> None:
        """
        Sets the performance_profile of this InsightsTrend.
        The performance profile

        :param performance_profile: The performance_profile of this InsightsTrend.
        :type: AddressableEntityRef
        """
        

        self._performance_profile = performance_profile

    @property
    def division(self) -> 'DivisionReference':
        """
        Gets the division of this InsightsTrend.
        The division

        :return: The division of this InsightsTrend.
        :rtype: DivisionReference
        """
        return self._division

    @division.setter
    def division(self, division: 'DivisionReference') -> None:
        """
        Sets the division of this InsightsTrend.
        The division

        :param division: The division of this InsightsTrend.
        :type: DivisionReference
        """
        

        self._division = division

    @property
    def granularity(self) -> str:
        """
        Gets the granularity of this InsightsTrend.
        Granularity

        :return: The granularity of this InsightsTrend.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity: str) -> None:
        """
        Sets the granularity of this InsightsTrend.
        Granularity

        :param granularity: The granularity of this InsightsTrend.
        :type: str
        """
        if isinstance(granularity, int):
            granularity = str(granularity)
        allowed_values = ["Daily", "Weekly", "Monthly"]
        if granularity.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for granularity -> " + granularity)
            self._granularity = "outdated_sdk_version"
        else:
            self._granularity = granularity

    @property
    def comparative_period(self) -> 'WorkdayPeriod':
        """
        Gets the comparative_period of this InsightsTrend.
        The comparative period work day date range

        :return: The comparative_period of this InsightsTrend.
        :rtype: WorkdayPeriod
        """
        return self._comparative_period

    @comparative_period.setter
    def comparative_period(self, comparative_period: 'WorkdayPeriod') -> None:
        """
        Sets the comparative_period of this InsightsTrend.
        The comparative period work day date range

        :param comparative_period: The comparative_period of this InsightsTrend.
        :type: WorkdayPeriod
        """
        

        self._comparative_period = comparative_period

    @property
    def primary_period(self) -> 'WorkdayPeriod':
        """
        Gets the primary_period of this InsightsTrend.
        The primary period work day date range

        :return: The primary_period of this InsightsTrend.
        :rtype: WorkdayPeriod
        """
        return self._primary_period

    @primary_period.setter
    def primary_period(self, primary_period: 'WorkdayPeriod') -> None:
        """
        Sets the primary_period of this InsightsTrend.
        The primary period work day date range

        :param primary_period: The primary_period of this InsightsTrend.
        :type: WorkdayPeriod
        """
        

        self._primary_period = primary_period

    @property
    def entities(self) -> List['InsightsTrendMetricItem']:
        """
        Gets the entities of this InsightsTrend.
        The list of insights trend for each metric

        :return: The entities of this InsightsTrend.
        :rtype: list[InsightsTrendMetricItem]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List['InsightsTrendMetricItem']) -> None:
        """
        Sets the entities of this InsightsTrend.
        The list of insights trend for each metric

        :param entities: The entities of this InsightsTrend.
        :type: list[InsightsTrendMetricItem]
        """
        

        self._entities = entities

    @property
    def total(self) -> 'InsightsTrendTotalItem':
        """
        Gets the total of this InsightsTrend.
        The insights trend in total

        :return: The total of this InsightsTrend.
        :rtype: InsightsTrendTotalItem
        """
        return self._total

    @total.setter
    def total(self, total: 'InsightsTrendTotalItem') -> None:
        """
        Sets the total of this InsightsTrend.
        The insights trend in total

        :param total: The total of this InsightsTrend.
        :type: InsightsTrendTotalItem
        """
        

        self._total = total

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

