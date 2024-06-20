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
    from . import AlertSummaryEntity

class AlertSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AlertSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entities': 'list[AlertSummaryEntity]',
            'conversation': 'AddressableEntityRef',
            'metric_type': 'str',
            'entities_are_team_members': 'bool'
        }

        self.attribute_map = {
            'entities': 'entities',
            'conversation': 'conversation',
            'metric_type': 'metricType',
            'entities_are_team_members': 'entitiesAreTeamMembers'
        }

        self._entities = None
        self._conversation = None
        self._metric_type = None
        self._entities_are_team_members = None

    @property
    def entities(self) -> List['AlertSummaryEntity']:
        """
        Gets the entities of this AlertSummary.
        The entities who violated the rule condition over the duration of the alert.

        :return: The entities of this AlertSummary.
        :rtype: list[AlertSummaryEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List['AlertSummaryEntity']) -> None:
        """
        Sets the entities of this AlertSummary.
        The entities who violated the rule condition over the duration of the alert.

        :param entities: The entities of this AlertSummary.
        :type: list[AlertSummaryEntity]
        """
        

        self._entities = entities

    @property
    def conversation(self) -> 'AddressableEntityRef':
        """
        Gets the conversation of this AlertSummary.
        The id of the conversation that triggered the alert.  Only used for alerts based on instance-based conversation metrics.

        :return: The conversation of this AlertSummary.
        :rtype: AddressableEntityRef
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'AddressableEntityRef') -> None:
        """
        Sets the conversation of this AlertSummary.
        The id of the conversation that triggered the alert.  Only used for alerts based on instance-based conversation metrics.

        :param conversation: The conversation of this AlertSummary.
        :type: AddressableEntityRef
        """
        

        self._conversation = conversation

    @property
    def metric_type(self) -> str:
        """
        Gets the metric_type of this AlertSummary.
        The metric type that is monitored.

        :return: The metric_type of this AlertSummary.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type: str) -> None:
        """
        Sets the metric_type of this AlertSummary.
        The metric type that is monitored.

        :param metric_type: The metric_type of this AlertSummary.
        :type: str
        """
        if isinstance(metric_type, int):
            metric_type = str(metric_type)
        allowed_values = ["Interval", "Instance"]
        if metric_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for metric_type -> " + metric_type)
            self._metric_type = "outdated_sdk_version"
        else:
            self._metric_type = metric_type

    @property
    def entities_are_team_members(self) -> bool:
        """
        Gets the entities_are_team_members of this AlertSummary.
        Flag that indicated whether or not the alert is for a rule with a condition for all members of a team.

        :return: The entities_are_team_members of this AlertSummary.
        :rtype: bool
        """
        return self._entities_are_team_members

    @entities_are_team_members.setter
    def entities_are_team_members(self, entities_are_team_members: bool) -> None:
        """
        Sets the entities_are_team_members of this AlertSummary.
        Flag that indicated whether or not the alert is for a rule with a condition for all members of a team.

        :param entities_are_team_members: The entities_are_team_members of this AlertSummary.
        :type: bool
        """
        

        self._entities_are_team_members = entities_are_team_members

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

