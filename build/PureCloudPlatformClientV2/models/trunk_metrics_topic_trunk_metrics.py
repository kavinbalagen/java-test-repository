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
    from . import TrunkMetricsTopicTrunkMetricsCalls
    from . import TrunkMetricsTopicTrunkMetricsQoS
    from . import TrunkMetricsTopicUriReference

class TrunkMetricsTopicTrunkMetrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrunkMetricsTopicTrunkMetrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'calls': 'TrunkMetricsTopicTrunkMetricsCalls',
            'event_time': 'datetime',
            'qos': 'TrunkMetricsTopicTrunkMetricsQoS',
            'trunk': 'TrunkMetricsTopicUriReference'
        }

        self.attribute_map = {
            'calls': 'calls',
            'event_time': 'eventTime',
            'qos': 'qos',
            'trunk': 'trunk'
        }

        self._calls = None
        self._event_time = None
        self._qos = None
        self._trunk = None

    @property
    def calls(self) -> 'TrunkMetricsTopicTrunkMetricsCalls':
        """
        Gets the calls of this TrunkMetricsTopicTrunkMetrics.


        :return: The calls of this TrunkMetricsTopicTrunkMetrics.
        :rtype: TrunkMetricsTopicTrunkMetricsCalls
        """
        return self._calls

    @calls.setter
    def calls(self, calls: 'TrunkMetricsTopicTrunkMetricsCalls') -> None:
        """
        Sets the calls of this TrunkMetricsTopicTrunkMetrics.


        :param calls: The calls of this TrunkMetricsTopicTrunkMetrics.
        :type: TrunkMetricsTopicTrunkMetricsCalls
        """
        

        self._calls = calls

    @property
    def event_time(self) -> datetime:
        """
        Gets the event_time of this TrunkMetricsTopicTrunkMetrics.


        :return: The event_time of this TrunkMetricsTopicTrunkMetrics.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: datetime) -> None:
        """
        Sets the event_time of this TrunkMetricsTopicTrunkMetrics.


        :param event_time: The event_time of this TrunkMetricsTopicTrunkMetrics.
        :type: datetime
        """
        

        self._event_time = event_time

    @property
    def qos(self) -> 'TrunkMetricsTopicTrunkMetricsQoS':
        """
        Gets the qos of this TrunkMetricsTopicTrunkMetrics.


        :return: The qos of this TrunkMetricsTopicTrunkMetrics.
        :rtype: TrunkMetricsTopicTrunkMetricsQoS
        """
        return self._qos

    @qos.setter
    def qos(self, qos: 'TrunkMetricsTopicTrunkMetricsQoS') -> None:
        """
        Sets the qos of this TrunkMetricsTopicTrunkMetrics.


        :param qos: The qos of this TrunkMetricsTopicTrunkMetrics.
        :type: TrunkMetricsTopicTrunkMetricsQoS
        """
        

        self._qos = qos

    @property
    def trunk(self) -> 'TrunkMetricsTopicUriReference':
        """
        Gets the trunk of this TrunkMetricsTopicTrunkMetrics.


        :return: The trunk of this TrunkMetricsTopicTrunkMetrics.
        :rtype: TrunkMetricsTopicUriReference
        """
        return self._trunk

    @trunk.setter
    def trunk(self, trunk: 'TrunkMetricsTopicUriReference') -> None:
        """
        Sets the trunk of this TrunkMetricsTopicTrunkMetrics.


        :param trunk: The trunk of this TrunkMetricsTopicTrunkMetrics.
        :type: TrunkMetricsTopicUriReference
        """
        

        self._trunk = trunk

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

