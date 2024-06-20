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


class CampaignSkillStatistics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CampaignSkillStatistics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'skill_combinations': 'int',
            'eligible_skilled_agents': 'int'
        }

        self.attribute_map = {
            'skill_combinations': 'skillCombinations',
            'eligible_skilled_agents': 'eligibleSkilledAgents'
        }

        self._skill_combinations = None
        self._eligible_skilled_agents = None

    @property
    def skill_combinations(self) -> int:
        """
        Gets the skill_combinations of this CampaignSkillStatistics.
        Number of available skill combinations for the campaign

        :return: The skill_combinations of this CampaignSkillStatistics.
        :rtype: int
        """
        return self._skill_combinations

    @skill_combinations.setter
    def skill_combinations(self, skill_combinations: int) -> None:
        """
        Sets the skill_combinations of this CampaignSkillStatistics.
        Number of available skill combinations for the campaign

        :param skill_combinations: The skill_combinations of this CampaignSkillStatistics.
        :type: int
        """
        

        self._skill_combinations = skill_combinations

    @property
    def eligible_skilled_agents(self) -> int:
        """
        Gets the eligible_skilled_agents of this CampaignSkillStatistics.
        Number of eligible agents with skills for campaign

        :return: The eligible_skilled_agents of this CampaignSkillStatistics.
        :rtype: int
        """
        return self._eligible_skilled_agents

    @eligible_skilled_agents.setter
    def eligible_skilled_agents(self, eligible_skilled_agents: int) -> None:
        """
        Sets the eligible_skilled_agents of this CampaignSkillStatistics.
        Number of eligible agents with skills for campaign

        :param eligible_skilled_agents: The eligible_skilled_agents of this CampaignSkillStatistics.
        :type: int
        """
        

        self._eligible_skilled_agents = eligible_skilled_agents

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

