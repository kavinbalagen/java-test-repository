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
    from . import User

class InteractionStatsRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        InteractionStatsRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'dimension': 'str',
            'dimension_value': 'str',
            'metric': 'str',
            'media_type': 'str',
            'numeric_range': 'str',
            'statistic': 'str',
            'value': 'float',
            'enabled': 'bool',
            'in_alarm': 'bool',
            'notification_users': 'list[User]',
            'alert_types': 'list[str]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'dimension': 'dimension',
            'dimension_value': 'dimensionValue',
            'metric': 'metric',
            'media_type': 'mediaType',
            'numeric_range': 'numericRange',
            'statistic': 'statistic',
            'value': 'value',
            'enabled': 'enabled',
            'in_alarm': 'inAlarm',
            'notification_users': 'notificationUsers',
            'alert_types': 'alertTypes',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._dimension = None
        self._dimension_value = None
        self._metric = None
        self._media_type = None
        self._numeric_range = None
        self._statistic = None
        self._value = None
        self._enabled = None
        self._in_alarm = None
        self._notification_users = None
        self._alert_types = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this InteractionStatsRule.
        The globally unique identifier for the object.

        :return: The id of this InteractionStatsRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this InteractionStatsRule.
        The globally unique identifier for the object.

        :param id: The id of this InteractionStatsRule.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this InteractionStatsRule.
        Name of the rule

        :return: The name of this InteractionStatsRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this InteractionStatsRule.
        Name of the rule

        :param name: The name of this InteractionStatsRule.
        :type: str
        """
        

        self._name = name

    @property
    def dimension(self) -> str:
        """
        Gets the dimension of this InteractionStatsRule.
        The dimension of concern.

        :return: The dimension of this InteractionStatsRule.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: str) -> None:
        """
        Sets the dimension of this InteractionStatsRule.
        The dimension of concern.

        :param dimension: The dimension of this InteractionStatsRule.
        :type: str
        """
        if isinstance(dimension, int):
            dimension = str(dimension)
        allowed_values = ["queueId", "userId"]
        if dimension.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for dimension -> " + dimension)
            self._dimension = "outdated_sdk_version"
        else:
            self._dimension = dimension

    @property
    def dimension_value(self) -> str:
        """
        Gets the dimension_value of this InteractionStatsRule.
        The value of the dimension.

        :return: The dimension_value of this InteractionStatsRule.
        :rtype: str
        """
        return self._dimension_value

    @dimension_value.setter
    def dimension_value(self, dimension_value: str) -> None:
        """
        Sets the dimension_value of this InteractionStatsRule.
        The value of the dimension.

        :param dimension_value: The dimension_value of this InteractionStatsRule.
        :type: str
        """
        

        self._dimension_value = dimension_value

    @property
    def metric(self) -> str:
        """
        Gets the metric of this InteractionStatsRule.
        The metric to be assessed.

        :return: The metric of this InteractionStatsRule.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric: str) -> None:
        """
        Sets the metric of this InteractionStatsRule.
        The metric to be assessed.

        :param metric: The metric of this InteractionStatsRule.
        :type: str
        """
        if isinstance(metric, int):
            metric = str(metric)
        allowed_values = ["tAbandon", "tAnswered", "tTalk", "nOffered", "tHandle", "nTransferred", "oServiceLevel", "tWait", "tHeld", "tAcw"]
        if metric.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for metric -> " + metric)
            self._metric = "outdated_sdk_version"
        else:
            self._metric = metric

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this InteractionStatsRule.
        The media type.

        :return: The media_type of this InteractionStatsRule.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this InteractionStatsRule.
        The media type.

        :param media_type: The media_type of this InteractionStatsRule.
        :type: str
        """
        if isinstance(media_type, int):
            media_type = str(media_type)
        allowed_values = ["voice", "chat", "email", "callback", "message"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def numeric_range(self) -> str:
        """
        Gets the numeric_range of this InteractionStatsRule.
        The comparison descriptor used against the metric's value.

        :return: The numeric_range of this InteractionStatsRule.
        :rtype: str
        """
        return self._numeric_range

    @numeric_range.setter
    def numeric_range(self, numeric_range: str) -> None:
        """
        Sets the numeric_range of this InteractionStatsRule.
        The comparison descriptor used against the metric's value.

        :param numeric_range: The numeric_range of this InteractionStatsRule.
        :type: str
        """
        if isinstance(numeric_range, int):
            numeric_range = str(numeric_range)
        allowed_values = ["gt", "gte", "lt", "lte", "eq", "ne"]
        if numeric_range.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for numeric_range -> " + numeric_range)
            self._numeric_range = "outdated_sdk_version"
        else:
            self._numeric_range = numeric_range

    @property
    def statistic(self) -> str:
        """
        Gets the statistic of this InteractionStatsRule.
        The statistic of concern for the metric.

        :return: The statistic of this InteractionStatsRule.
        :rtype: str
        """
        return self._statistic

    @statistic.setter
    def statistic(self, statistic: str) -> None:
        """
        Sets the statistic of this InteractionStatsRule.
        The statistic of concern for the metric.

        :param statistic: The statistic of this InteractionStatsRule.
        :type: str
        """
        if isinstance(statistic, int):
            statistic = str(statistic)
        allowed_values = ["count", "min", "ratio", "max"]
        if statistic.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for statistic -> " + statistic)
            self._statistic = "outdated_sdk_version"
        else:
            self._statistic = statistic

    @property
    def value(self) -> float:
        """
        Gets the value of this InteractionStatsRule.
        The threshold value.

        :return: The value of this InteractionStatsRule.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        """
        Sets the value of this InteractionStatsRule.
        The threshold value.

        :param value: The value of this InteractionStatsRule.
        :type: float
        """
        

        self._value = value

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this InteractionStatsRule.
        Indicates if the rule is enabled.

        :return: The enabled of this InteractionStatsRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this InteractionStatsRule.
        Indicates if the rule is enabled.

        :param enabled: The enabled of this InteractionStatsRule.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def in_alarm(self) -> bool:
        """
        Gets the in_alarm of this InteractionStatsRule.
        Indicates if the rule is in alarm state.

        :return: The in_alarm of this InteractionStatsRule.
        :rtype: bool
        """
        return self._in_alarm

    @in_alarm.setter
    def in_alarm(self, in_alarm: bool) -> None:
        """
        Sets the in_alarm of this InteractionStatsRule.
        Indicates if the rule is in alarm state.

        :param in_alarm: The in_alarm of this InteractionStatsRule.
        :type: bool
        """
        

        self._in_alarm = in_alarm

    @property
    def notification_users(self) -> List['User']:
        """
        Gets the notification_users of this InteractionStatsRule.
        The ids of users who will be notified of alarm state change.

        :return: The notification_users of this InteractionStatsRule.
        :rtype: list[User]
        """
        return self._notification_users

    @notification_users.setter
    def notification_users(self, notification_users: List['User']) -> None:
        """
        Sets the notification_users of this InteractionStatsRule.
        The ids of users who will be notified of alarm state change.

        :param notification_users: The notification_users of this InteractionStatsRule.
        :type: list[User]
        """
        

        self._notification_users = notification_users

    @property
    def alert_types(self) -> List[str]:
        """
        Gets the alert_types of this InteractionStatsRule.
        A collection of notification methods.

        :return: The alert_types of this InteractionStatsRule.
        :rtype: list[str]
        """
        return self._alert_types

    @alert_types.setter
    def alert_types(self, alert_types: List[str]) -> None:
        """
        Sets the alert_types of this InteractionStatsRule.
        A collection of notification methods.

        :param alert_types: The alert_types of this InteractionStatsRule.
        :type: list[str]
        """
        

        self._alert_types = alert_types

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this InteractionStatsRule.
        The URI for this object

        :return: The self_uri of this InteractionStatsRule.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this InteractionStatsRule.
        The URI for this object

        :param self_uri: The self_uri of this InteractionStatsRule.
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

