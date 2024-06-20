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
    from . import TranscriptAggregateQueryFilter
    from . import TranscriptAggregationView

class TranscriptAsyncAggregationQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TranscriptAsyncAggregationQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interval': 'str',
            'granularity': 'str',
            'time_zone': 'str',
            'group_by': 'list[str]',
            'filter': 'TranscriptAggregateQueryFilter',
            'metrics': 'list[str]',
            'flatten_multivalued_dimensions': 'bool',
            'views': 'list[TranscriptAggregationView]',
            'alternate_time_dimension': 'str',
            'page_size': 'int'
        }

        self.attribute_map = {
            'interval': 'interval',
            'granularity': 'granularity',
            'time_zone': 'timeZone',
            'group_by': 'groupBy',
            'filter': 'filter',
            'metrics': 'metrics',
            'flatten_multivalued_dimensions': 'flattenMultivaluedDimensions',
            'views': 'views',
            'alternate_time_dimension': 'alternateTimeDimension',
            'page_size': 'pageSize'
        }

        self._interval = None
        self._granularity = None
        self._time_zone = None
        self._group_by = None
        self._filter = None
        self._metrics = None
        self._flatten_multivalued_dimensions = None
        self._views = None
        self._alternate_time_dimension = None
        self._page_size = None

    @property
    def interval(self) -> str:
        """
        Gets the interval of this TranscriptAsyncAggregationQuery.
        Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :return: The interval of this TranscriptAsyncAggregationQuery.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval: str) -> None:
        """
        Sets the interval of this TranscriptAsyncAggregationQuery.
        Behaves like one clause in a SQL WHERE. Specifies the date and time range of data being queried. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss

        :param interval: The interval of this TranscriptAsyncAggregationQuery.
        :type: str
        """
        

        self._interval = interval

    @property
    def granularity(self) -> str:
        """
        Gets the granularity of this TranscriptAsyncAggregationQuery.
        Granularity aggregates metrics into subpartitions within the time interval specified. The default granularity is the same duration as the interval. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :return: The granularity of this TranscriptAsyncAggregationQuery.
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity: str) -> None:
        """
        Sets the granularity of this TranscriptAsyncAggregationQuery.
        Granularity aggregates metrics into subpartitions within the time interval specified. The default granularity is the same duration as the interval. Periods are represented as an ISO-8601 string. For example: P1D or P1DT12H

        :param granularity: The granularity of this TranscriptAsyncAggregationQuery.
        :type: str
        """
        

        self._granularity = granularity

    @property
    def time_zone(self) -> str:
        """
        Gets the time_zone of this TranscriptAsyncAggregationQuery.
        Time zone context used to calculate response intervals (this allows resolving DST changes). The interval offset is used even when timeZone is specified. Default is UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :return: The time_zone of this TranscriptAsyncAggregationQuery.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone: str) -> None:
        """
        Sets the time_zone of this TranscriptAsyncAggregationQuery.
        Time zone context used to calculate response intervals (this allows resolving DST changes). The interval offset is used even when timeZone is specified. Default is UTC. Time zones are represented as a string of the zone name as found in the IANA time zone database. For example: UTC, Etc/UTC, or Europe/London

        :param time_zone: The time_zone of this TranscriptAsyncAggregationQuery.
        :type: str
        """
        

        self._time_zone = time_zone

    @property
    def group_by(self) -> List[str]:
        """
        Gets the group_by of this TranscriptAsyncAggregationQuery.
        Behaves like a SQL GROUPBY. Allows for multiple levels of grouping as a list of dimensions. Partitions resulting aggregate computations into distinct named subgroups rather than across the entire result set as if it were one group.

        :return: The group_by of this TranscriptAsyncAggregationQuery.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by: List[str]) -> None:
        """
        Sets the group_by of this TranscriptAsyncAggregationQuery.
        Behaves like a SQL GROUPBY. Allows for multiple levels of grouping as a list of dimensions. Partitions resulting aggregate computations into distinct named subgroups rather than across the entire result set as if it were one group.

        :param group_by: The group_by of this TranscriptAsyncAggregationQuery.
        :type: list[str]
        """
        

        self._group_by = group_by

    @property
    def filter(self) -> 'TranscriptAggregateQueryFilter':
        """
        Gets the filter of this TranscriptAsyncAggregationQuery.
        Behaves like a SQL WHERE clause. This is ANDed with the interval parameter. Expresses boolean logical predicates as well as dimensional filters

        :return: The filter of this TranscriptAsyncAggregationQuery.
        :rtype: TranscriptAggregateQueryFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter: 'TranscriptAggregateQueryFilter') -> None:
        """
        Sets the filter of this TranscriptAsyncAggregationQuery.
        Behaves like a SQL WHERE clause. This is ANDed with the interval parameter. Expresses boolean logical predicates as well as dimensional filters

        :param filter: The filter of this TranscriptAsyncAggregationQuery.
        :type: TranscriptAggregateQueryFilter
        """
        

        self._filter = filter

    @property
    def metrics(self) -> List[str]:
        """
        Gets the metrics of this TranscriptAsyncAggregationQuery.
        Behaves like a SQL SELECT clause. Only named metrics will be retrieved.

        :return: The metrics of this TranscriptAsyncAggregationQuery.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List[str]) -> None:
        """
        Sets the metrics of this TranscriptAsyncAggregationQuery.
        Behaves like a SQL SELECT clause. Only named metrics will be retrieved.

        :param metrics: The metrics of this TranscriptAsyncAggregationQuery.
        :type: list[str]
        """
        

        self._metrics = metrics

    @property
    def flatten_multivalued_dimensions(self) -> bool:
        """
        Gets the flatten_multivalued_dimensions of this TranscriptAsyncAggregationQuery.
        Flattens any multivalued dimensions used in response groups (e.g. ['a','b','c']->'a,b,c')

        :return: The flatten_multivalued_dimensions of this TranscriptAsyncAggregationQuery.
        :rtype: bool
        """
        return self._flatten_multivalued_dimensions

    @flatten_multivalued_dimensions.setter
    def flatten_multivalued_dimensions(self, flatten_multivalued_dimensions: bool) -> None:
        """
        Sets the flatten_multivalued_dimensions of this TranscriptAsyncAggregationQuery.
        Flattens any multivalued dimensions used in response groups (e.g. ['a','b','c']->'a,b,c')

        :param flatten_multivalued_dimensions: The flatten_multivalued_dimensions of this TranscriptAsyncAggregationQuery.
        :type: bool
        """
        

        self._flatten_multivalued_dimensions = flatten_multivalued_dimensions

    @property
    def views(self) -> List['TranscriptAggregationView']:
        """
        Gets the views of this TranscriptAsyncAggregationQuery.
        Custom derived metric views

        :return: The views of this TranscriptAsyncAggregationQuery.
        :rtype: list[TranscriptAggregationView]
        """
        return self._views

    @views.setter
    def views(self, views: List['TranscriptAggregationView']) -> None:
        """
        Sets the views of this TranscriptAsyncAggregationQuery.
        Custom derived metric views

        :param views: The views of this TranscriptAsyncAggregationQuery.
        :type: list[TranscriptAggregationView]
        """
        

        self._views = views

    @property
    def alternate_time_dimension(self) -> str:
        """
        Gets the alternate_time_dimension of this TranscriptAsyncAggregationQuery.
        Dimension to use as the alternative timestamp for data in the aggregate.  Choosing \"eventTime\" uses the actual time of the data event.

        :return: The alternate_time_dimension of this TranscriptAsyncAggregationQuery.
        :rtype: str
        """
        return self._alternate_time_dimension

    @alternate_time_dimension.setter
    def alternate_time_dimension(self, alternate_time_dimension: str) -> None:
        """
        Sets the alternate_time_dimension of this TranscriptAsyncAggregationQuery.
        Dimension to use as the alternative timestamp for data in the aggregate.  Choosing \"eventTime\" uses the actual time of the data event.

        :param alternate_time_dimension: The alternate_time_dimension of this TranscriptAsyncAggregationQuery.
        :type: str
        """
        if isinstance(alternate_time_dimension, int):
            alternate_time_dimension = str(alternate_time_dimension)
        allowed_values = ["eventTime"]
        if alternate_time_dimension.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for alternate_time_dimension -> " + alternate_time_dimension)
            self._alternate_time_dimension = "outdated_sdk_version"
        else:
            self._alternate_time_dimension = alternate_time_dimension

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this TranscriptAsyncAggregationQuery.
        The number of results per page

        :return: The page_size of this TranscriptAsyncAggregationQuery.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this TranscriptAsyncAggregationQuery.
        The number of results per page

        :param page_size: The page_size of this TranscriptAsyncAggregationQuery.
        :type: int
        """
        

        self._page_size = page_size

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

