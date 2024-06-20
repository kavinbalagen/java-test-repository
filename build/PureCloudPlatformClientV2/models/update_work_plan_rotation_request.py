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
    from . import DateRangeWithOptionalEnd
    from . import UpdateWorkPlanRotationAgentRequest
    from . import WfmVersionedEntityMetadata
    from . import WorkPlanPatternRequest

class UpdateWorkPlanRotationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UpdateWorkPlanRotationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'enabled': 'bool',
            'date_range': 'DateRangeWithOptionalEnd',
            'agents': 'list[UpdateWorkPlanRotationAgentRequest]',
            'pattern': 'WorkPlanPatternRequest',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'name': 'name',
            'enabled': 'enabled',
            'date_range': 'dateRange',
            'agents': 'agents',
            'pattern': 'pattern',
            'metadata': 'metadata'
        }

        self._name = None
        self._enabled = None
        self._date_range = None
        self._agents = None
        self._pattern = None
        self._metadata = None

    @property
    def name(self) -> str:
        """
        Gets the name of this UpdateWorkPlanRotationRequest.
        Name of this work plan rotation

        :return: The name of this UpdateWorkPlanRotationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this UpdateWorkPlanRotationRequest.
        Name of this work plan rotation

        :param name: The name of this UpdateWorkPlanRotationRequest.
        :type: str
        """
        

        self._name = name

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this UpdateWorkPlanRotationRequest.
        Whether the work plan rotation is enabled for scheduling

        :return: The enabled of this UpdateWorkPlanRotationRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this UpdateWorkPlanRotationRequest.
        Whether the work plan rotation is enabled for scheduling

        :param enabled: The enabled of this UpdateWorkPlanRotationRequest.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def date_range(self) -> 'DateRangeWithOptionalEnd':
        """
        Gets the date_range of this UpdateWorkPlanRotationRequest.
        The date range to which this work plan rotation applies

        :return: The date_range of this UpdateWorkPlanRotationRequest.
        :rtype: DateRangeWithOptionalEnd
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range: 'DateRangeWithOptionalEnd') -> None:
        """
        Sets the date_range of this UpdateWorkPlanRotationRequest.
        The date range to which this work plan rotation applies

        :param date_range: The date_range of this UpdateWorkPlanRotationRequest.
        :type: DateRangeWithOptionalEnd
        """
        

        self._date_range = date_range

    @property
    def agents(self) -> List['UpdateWorkPlanRotationAgentRequest']:
        """
        Gets the agents of this UpdateWorkPlanRotationRequest.
        Agents in this work plan rotation

        :return: The agents of this UpdateWorkPlanRotationRequest.
        :rtype: list[UpdateWorkPlanRotationAgentRequest]
        """
        return self._agents

    @agents.setter
    def agents(self, agents: List['UpdateWorkPlanRotationAgentRequest']) -> None:
        """
        Sets the agents of this UpdateWorkPlanRotationRequest.
        Agents in this work plan rotation

        :param agents: The agents of this UpdateWorkPlanRotationRequest.
        :type: list[UpdateWorkPlanRotationAgentRequest]
        """
        

        self._agents = agents

    @property
    def pattern(self) -> 'WorkPlanPatternRequest':
        """
        Gets the pattern of this UpdateWorkPlanRotationRequest.
        Pattern with list of work plan IDs that rotate on a weekly basis

        :return: The pattern of this UpdateWorkPlanRotationRequest.
        :rtype: WorkPlanPatternRequest
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern: 'WorkPlanPatternRequest') -> None:
        """
        Sets the pattern of this UpdateWorkPlanRotationRequest.
        Pattern with list of work plan IDs that rotate on a weekly basis

        :param pattern: The pattern of this UpdateWorkPlanRotationRequest.
        :type: WorkPlanPatternRequest
        """
        

        self._pattern = pattern

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this UpdateWorkPlanRotationRequest.
        Version metadata for this work plan rotation

        :return: The metadata of this UpdateWorkPlanRotationRequest.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this UpdateWorkPlanRotationRequest.
        Version metadata for this work plan rotation

        :param metadata: The metadata of this UpdateWorkPlanRotationRequest.
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
