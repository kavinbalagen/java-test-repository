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


class SpeechTextAnalyticsSettingsRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SpeechTextAnalyticsSettingsRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_program_id': 'str',
            'expected_dialects': 'list[str]',
            'text_analytics_enabled': 'bool',
            'agent_empathy_enabled': 'bool'
        }

        self.attribute_map = {
            'default_program_id': 'defaultProgramId',
            'expected_dialects': 'expectedDialects',
            'text_analytics_enabled': 'textAnalyticsEnabled',
            'agent_empathy_enabled': 'agentEmpathyEnabled'
        }

        self._default_program_id = None
        self._expected_dialects = None
        self._text_analytics_enabled = None
        self._agent_empathy_enabled = None

    @property
    def default_program_id(self) -> str:
        """
        Gets the default_program_id of this SpeechTextAnalyticsSettingsRequest.
        Setting to choose name for the default program for topic detection

        :return: The default_program_id of this SpeechTextAnalyticsSettingsRequest.
        :rtype: str
        """
        return self._default_program_id

    @default_program_id.setter
    def default_program_id(self, default_program_id: str) -> None:
        """
        Sets the default_program_id of this SpeechTextAnalyticsSettingsRequest.
        Setting to choose name for the default program for topic detection

        :param default_program_id: The default_program_id of this SpeechTextAnalyticsSettingsRequest.
        :type: str
        """
        

        self._default_program_id = default_program_id

    @property
    def expected_dialects(self) -> List[str]:
        """
        Gets the expected_dialects of this SpeechTextAnalyticsSettingsRequest.
        Setting to choose expected dialects

        :return: The expected_dialects of this SpeechTextAnalyticsSettingsRequest.
        :rtype: list[str]
        """
        return self._expected_dialects

    @expected_dialects.setter
    def expected_dialects(self, expected_dialects: List[str]) -> None:
        """
        Sets the expected_dialects of this SpeechTextAnalyticsSettingsRequest.
        Setting to choose expected dialects

        :param expected_dialects: The expected_dialects of this SpeechTextAnalyticsSettingsRequest.
        :type: list[str]
        """
        

        self._expected_dialects = expected_dialects

    @property
    def text_analytics_enabled(self) -> bool:
        """
        Gets the text_analytics_enabled of this SpeechTextAnalyticsSettingsRequest.
        Setting to enable/disable text analytics

        :return: The text_analytics_enabled of this SpeechTextAnalyticsSettingsRequest.
        :rtype: bool
        """
        return self._text_analytics_enabled

    @text_analytics_enabled.setter
    def text_analytics_enabled(self, text_analytics_enabled: bool) -> None:
        """
        Sets the text_analytics_enabled of this SpeechTextAnalyticsSettingsRequest.
        Setting to enable/disable text analytics

        :param text_analytics_enabled: The text_analytics_enabled of this SpeechTextAnalyticsSettingsRequest.
        :type: bool
        """
        

        self._text_analytics_enabled = text_analytics_enabled

    @property
    def agent_empathy_enabled(self) -> bool:
        """
        Gets the agent_empathy_enabled of this SpeechTextAnalyticsSettingsRequest.
        Setting to enable/disable Agent Empathy setting

        :return: The agent_empathy_enabled of this SpeechTextAnalyticsSettingsRequest.
        :rtype: bool
        """
        return self._agent_empathy_enabled

    @agent_empathy_enabled.setter
    def agent_empathy_enabled(self, agent_empathy_enabled: bool) -> None:
        """
        Sets the agent_empathy_enabled of this SpeechTextAnalyticsSettingsRequest.
        Setting to enable/disable Agent Empathy setting

        :param agent_empathy_enabled: The agent_empathy_enabled of this SpeechTextAnalyticsSettingsRequest.
        :type: bool
        """
        

        self._agent_empathy_enabled = agent_empathy_enabled

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

