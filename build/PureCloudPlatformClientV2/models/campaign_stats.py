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
    from . import CampaignLinesUtilization
    from . import ConnectRate

class CampaignStats(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CampaignStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contact_rate': 'ConnectRate',
            'idle_agents': 'int',
            'effective_idle_agents': 'float',
            'adjusted_calls_per_agent': 'float',
            'outstanding_calls': 'int',
            'scheduled_calls': 'int',
            'time_zone_rescheduled_calls': 'int',
            'lines_utilization': 'CampaignLinesUtilization'
        }

        self.attribute_map = {
            'contact_rate': 'contactRate',
            'idle_agents': 'idleAgents',
            'effective_idle_agents': 'effectiveIdleAgents',
            'adjusted_calls_per_agent': 'adjustedCallsPerAgent',
            'outstanding_calls': 'outstandingCalls',
            'scheduled_calls': 'scheduledCalls',
            'time_zone_rescheduled_calls': 'timeZoneRescheduledCalls',
            'lines_utilization': 'linesUtilization'
        }

        self._contact_rate = None
        self._idle_agents = None
        self._effective_idle_agents = None
        self._adjusted_calls_per_agent = None
        self._outstanding_calls = None
        self._scheduled_calls = None
        self._time_zone_rescheduled_calls = None
        self._lines_utilization = None

    @property
    def contact_rate(self) -> 'ConnectRate':
        """
        Gets the contact_rate of this CampaignStats.
        Information regarding the campaign's connect rate

        :return: The contact_rate of this CampaignStats.
        :rtype: ConnectRate
        """
        return self._contact_rate

    @contact_rate.setter
    def contact_rate(self, contact_rate: 'ConnectRate') -> None:
        """
        Sets the contact_rate of this CampaignStats.
        Information regarding the campaign's connect rate

        :param contact_rate: The contact_rate of this CampaignStats.
        :type: ConnectRate
        """
        

        self._contact_rate = contact_rate

    @property
    def idle_agents(self) -> int:
        """
        Gets the idle_agents of this CampaignStats.
        Number of available agents not currently being utilized

        :return: The idle_agents of this CampaignStats.
        :rtype: int
        """
        return self._idle_agents

    @idle_agents.setter
    def idle_agents(self, idle_agents: int) -> None:
        """
        Sets the idle_agents of this CampaignStats.
        Number of available agents not currently being utilized

        :param idle_agents: The idle_agents of this CampaignStats.
        :type: int
        """
        

        self._idle_agents = idle_agents

    @property
    def effective_idle_agents(self) -> float:
        """
        Gets the effective_idle_agents of this CampaignStats.
        Number of effective available agents not currently being utilized

        :return: The effective_idle_agents of this CampaignStats.
        :rtype: float
        """
        return self._effective_idle_agents

    @effective_idle_agents.setter
    def effective_idle_agents(self, effective_idle_agents: float) -> None:
        """
        Sets the effective_idle_agents of this CampaignStats.
        Number of effective available agents not currently being utilized

        :param effective_idle_agents: The effective_idle_agents of this CampaignStats.
        :type: float
        """
        

        self._effective_idle_agents = effective_idle_agents

    @property
    def adjusted_calls_per_agent(self) -> float:
        """
        Gets the adjusted_calls_per_agent of this CampaignStats.
        Calls per agent adjusted by pace

        :return: The adjusted_calls_per_agent of this CampaignStats.
        :rtype: float
        """
        return self._adjusted_calls_per_agent

    @adjusted_calls_per_agent.setter
    def adjusted_calls_per_agent(self, adjusted_calls_per_agent: float) -> None:
        """
        Sets the adjusted_calls_per_agent of this CampaignStats.
        Calls per agent adjusted by pace

        :param adjusted_calls_per_agent: The adjusted_calls_per_agent of this CampaignStats.
        :type: float
        """
        

        self._adjusted_calls_per_agent = adjusted_calls_per_agent

    @property
    def outstanding_calls(self) -> int:
        """
        Gets the outstanding_calls of this CampaignStats.
        Number of campaign calls currently ongoing

        :return: The outstanding_calls of this CampaignStats.
        :rtype: int
        """
        return self._outstanding_calls

    @outstanding_calls.setter
    def outstanding_calls(self, outstanding_calls: int) -> None:
        """
        Sets the outstanding_calls of this CampaignStats.
        Number of campaign calls currently ongoing

        :param outstanding_calls: The outstanding_calls of this CampaignStats.
        :type: int
        """
        

        self._outstanding_calls = outstanding_calls

    @property
    def scheduled_calls(self) -> int:
        """
        Gets the scheduled_calls of this CampaignStats.
        Number of campaign calls currently scheduled

        :return: The scheduled_calls of this CampaignStats.
        :rtype: int
        """
        return self._scheduled_calls

    @scheduled_calls.setter
    def scheduled_calls(self, scheduled_calls: int) -> None:
        """
        Sets the scheduled_calls of this CampaignStats.
        Number of campaign calls currently scheduled

        :param scheduled_calls: The scheduled_calls of this CampaignStats.
        :type: int
        """
        

        self._scheduled_calls = scheduled_calls

    @property
    def time_zone_rescheduled_calls(self) -> int:
        """
        Gets the time_zone_rescheduled_calls of this CampaignStats.
        Number of campaign calls currently timezone rescheduled

        :return: The time_zone_rescheduled_calls of this CampaignStats.
        :rtype: int
        """
        return self._time_zone_rescheduled_calls

    @time_zone_rescheduled_calls.setter
    def time_zone_rescheduled_calls(self, time_zone_rescheduled_calls: int) -> None:
        """
        Sets the time_zone_rescheduled_calls of this CampaignStats.
        Number of campaign calls currently timezone rescheduled

        :param time_zone_rescheduled_calls: The time_zone_rescheduled_calls of this CampaignStats.
        :type: int
        """
        

        self._time_zone_rescheduled_calls = time_zone_rescheduled_calls

    @property
    def lines_utilization(self) -> 'CampaignLinesUtilization':
        """
        Gets the lines_utilization of this CampaignStats.
        Information on the campaign's lines utilization

        :return: The lines_utilization of this CampaignStats.
        :rtype: CampaignLinesUtilization
        """
        return self._lines_utilization

    @lines_utilization.setter
    def lines_utilization(self, lines_utilization: 'CampaignLinesUtilization') -> None:
        """
        Sets the lines_utilization of this CampaignStats.
        Information on the campaign's lines utilization

        :param lines_utilization: The lines_utilization of this CampaignStats.
        :type: CampaignLinesUtilization
        """
        

        self._lines_utilization = lines_utilization

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

