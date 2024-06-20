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
    from . import WfmBuScheduleTopicSchedulerMessageSeverityCount

class WfmBuScheduleTopicBuScheduleGenerationResultSummary(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmBuScheduleTopicBuScheduleGenerationResultSummary - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'failed': 'bool',
            'run_id': 'str',
            'message_count': 'int',
            'message_severity_counts': 'list[WfmBuScheduleTopicSchedulerMessageSeverityCount]'
        }

        self.attribute_map = {
            'failed': 'failed',
            'run_id': 'runId',
            'message_count': 'messageCount',
            'message_severity_counts': 'messageSeverityCounts'
        }

        self._failed = None
        self._run_id = None
        self._message_count = None
        self._message_severity_counts = None

    @property
    def failed(self) -> bool:
        """
        Gets the failed of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :return: The failed of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed: bool) -> None:
        """
        Sets the failed of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :param failed: The failed of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :type: bool
        """
        

        self._failed = failed

    @property
    def run_id(self) -> str:
        """
        Gets the run_id of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :return: The run_id of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id: str) -> None:
        """
        Sets the run_id of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :param run_id: The run_id of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :type: str
        """
        

        self._run_id = run_id

    @property
    def message_count(self) -> int:
        """
        Gets the message_count of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :return: The message_count of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count: int) -> None:
        """
        Sets the message_count of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :param message_count: The message_count of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :type: int
        """
        

        self._message_count = message_count

    @property
    def message_severity_counts(self) -> List['WfmBuScheduleTopicSchedulerMessageSeverityCount']:
        """
        Gets the message_severity_counts of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :return: The message_severity_counts of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :rtype: list[WfmBuScheduleTopicSchedulerMessageSeverityCount]
        """
        return self._message_severity_counts

    @message_severity_counts.setter
    def message_severity_counts(self, message_severity_counts: List['WfmBuScheduleTopicSchedulerMessageSeverityCount']) -> None:
        """
        Sets the message_severity_counts of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.


        :param message_severity_counts: The message_severity_counts of this WfmBuScheduleTopicBuScheduleGenerationResultSummary.
        :type: list[WfmBuScheduleTopicSchedulerMessageSeverityCount]
        """
        

        self._message_severity_counts = message_severity_counts

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

