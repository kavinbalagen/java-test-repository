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
    from . import JourneyViewChartDisplayAttributes
    from . import JourneyViewChartGroupByAttribute
    from . import JourneyViewChartMetric

class JourneyViewChart(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneyViewChart - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'version': 'int',
            'group_by_time': 'str',
            'group_by_attributes': 'list[JourneyViewChartGroupByAttribute]',
            'metrics': 'list[JourneyViewChartMetric]',
            'display_attributes': 'JourneyViewChartDisplayAttributes',
            'group_by_max': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'version': 'version',
            'group_by_time': 'groupByTime',
            'group_by_attributes': 'groupByAttributes',
            'metrics': 'metrics',
            'display_attributes': 'displayAttributes',
            'group_by_max': 'groupByMax',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._version = None
        self._group_by_time = None
        self._group_by_attributes = None
        self._metrics = None
        self._display_attributes = None
        self._group_by_max = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this JourneyViewChart.
        The globally unique identifier for the object.

        :return: The id of this JourneyViewChart.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this JourneyViewChart.
        The globally unique identifier for the object.

        :param id: The id of this JourneyViewChart.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this JourneyViewChart.


        :return: The name of this JourneyViewChart.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this JourneyViewChart.


        :param name: The name of this JourneyViewChart.
        :type: str
        """
        

        self._name = name

    @property
    def version(self) -> int:
        """
        Gets the version of this JourneyViewChart.
        The version of the journey view chart

        :return: The version of this JourneyViewChart.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this JourneyViewChart.
        The version of the journey view chart

        :param version: The version of this JourneyViewChart.
        :type: int
        """
        

        self._version = version

    @property
    def group_by_time(self) -> str:
        """
        Gets the group_by_time of this JourneyViewChart.
        A time unit to group the metrics by. There is a limit on the number of groupBy properties which can be specified.

        :return: The group_by_time of this JourneyViewChart.
        :rtype: str
        """
        return self._group_by_time

    @group_by_time.setter
    def group_by_time(self, group_by_time: str) -> None:
        """
        Sets the group_by_time of this JourneyViewChart.
        A time unit to group the metrics by. There is a limit on the number of groupBy properties which can be specified.

        :param group_by_time: The group_by_time of this JourneyViewChart.
        :type: str
        """
        if isinstance(group_by_time, int):
            group_by_time = str(group_by_time)
        allowed_values = ["Day", "Week", "Month", "Year"]
        if group_by_time.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for group_by_time -> " + group_by_time)
            self._group_by_time = "outdated_sdk_version"
        else:
            self._group_by_time = group_by_time

    @property
    def group_by_attributes(self) -> List['JourneyViewChartGroupByAttribute']:
        """
        Gets the group_by_attributes of this JourneyViewChart.
        A list of attributes to group the metrics by. There is a limit on the number of groupBy properties which can be specified.

        :return: The group_by_attributes of this JourneyViewChart.
        :rtype: list[JourneyViewChartGroupByAttribute]
        """
        return self._group_by_attributes

    @group_by_attributes.setter
    def group_by_attributes(self, group_by_attributes: List['JourneyViewChartGroupByAttribute']) -> None:
        """
        Sets the group_by_attributes of this JourneyViewChart.
        A list of attributes to group the metrics by. There is a limit on the number of groupBy properties which can be specified.

        :param group_by_attributes: The group_by_attributes of this JourneyViewChart.
        :type: list[JourneyViewChartGroupByAttribute]
        """
        

        self._group_by_attributes = group_by_attributes

    @property
    def metrics(self) -> List['JourneyViewChartMetric']:
        """
        Gets the metrics of this JourneyViewChart.
        A list of metrics to calculate within the chart by (aka the y axis)

        :return: The metrics of this JourneyViewChart.
        :rtype: list[JourneyViewChartMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List['JourneyViewChartMetric']) -> None:
        """
        Sets the metrics of this JourneyViewChart.
        A list of metrics to calculate within the chart by (aka the y axis)

        :param metrics: The metrics of this JourneyViewChart.
        :type: list[JourneyViewChartMetric]
        """
        

        self._metrics = metrics

    @property
    def display_attributes(self) -> 'JourneyViewChartDisplayAttributes':
        """
        Gets the display_attributes of this JourneyViewChart.
        Optional display attributes for rendering the chart

        :return: The display_attributes of this JourneyViewChart.
        :rtype: JourneyViewChartDisplayAttributes
        """
        return self._display_attributes

    @display_attributes.setter
    def display_attributes(self, display_attributes: 'JourneyViewChartDisplayAttributes') -> None:
        """
        Sets the display_attributes of this JourneyViewChart.
        Optional display attributes for rendering the chart

        :param display_attributes: The display_attributes of this JourneyViewChart.
        :type: JourneyViewChartDisplayAttributes
        """
        

        self._display_attributes = display_attributes

    @property
    def group_by_max(self) -> int:
        """
        Gets the group_by_max of this JourneyViewChart.
        A maximum on the number of values being grouped by

        :return: The group_by_max of this JourneyViewChart.
        :rtype: int
        """
        return self._group_by_max

    @group_by_max.setter
    def group_by_max(self, group_by_max: int) -> None:
        """
        Sets the group_by_max of this JourneyViewChart.
        A maximum on the number of values being grouped by

        :param group_by_max: The group_by_max of this JourneyViewChart.
        :type: int
        """
        

        self._group_by_max = group_by_max

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this JourneyViewChart.
        The URI for this object

        :return: The self_uri of this JourneyViewChart.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this JourneyViewChart.
        The URI for this object

        :param self_uri: The self_uri of this JourneyViewChart.
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

