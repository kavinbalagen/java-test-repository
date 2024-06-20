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
    from . import V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo

class V2FlowExecutionDataFlowidTopicExecution(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        V2FlowExecutionDataFlowidTopicExecution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'object_type': 'str',
            'object_id': 'str',
            'output_path_id': 'str',
            'execution_id': 'str',
            'start_date_time': 'datetime',
            'error': 'V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo',
            'warning': 'V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo',
            'language_tag': 'str'
        }

        self.attribute_map = {
            'object_type': 'objectType',
            'object_id': 'objectId',
            'output_path_id': 'outputPathId',
            'execution_id': 'executionId',
            'start_date_time': 'startDateTime',
            'error': 'error',
            'warning': 'warning',
            'language_tag': 'languageTag'
        }

        self._object_type = None
        self._object_id = None
        self._output_path_id = None
        self._execution_id = None
        self._start_date_time = None
        self._error = None
        self._warning = None
        self._language_tag = None

    @property
    def object_type(self) -> str:
        """
        Gets the object_type of this V2FlowExecutionDataFlowidTopicExecution.
        The type of executionItem that was executed.

        :return: The object_type of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type: str) -> None:
        """
        Sets the object_type of this V2FlowExecutionDataFlowidTopicExecution.
        The type of executionItem that was executed.

        :param object_type: The object_type of this V2FlowExecutionDataFlowidTopicExecution.
        :type: str
        """
        

        self._object_type = object_type

    @property
    def object_id(self) -> str:
        """
        Gets the object_id of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the actionId, menuId or taskId for the executionItem.

        :return: The object_id of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id: str) -> None:
        """
        Sets the object_id of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the actionId, menuId or taskId for the executionItem.

        :param object_id: The object_id of this V2FlowExecutionDataFlowidTopicExecution.
        :type: str
        """
        

        self._object_id = object_id

    @property
    def output_path_id(self) -> str:
        """
        Gets the output_path_id of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the identifier of the OutputPath that was taken.

        :return: The output_path_id of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: str
        """
        return self._output_path_id

    @output_path_id.setter
    def output_path_id(self, output_path_id: str) -> None:
        """
        Sets the output_path_id of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the identifier of the OutputPath that was taken.

        :param output_path_id: The output_path_id of this V2FlowExecutionDataFlowidTopicExecution.
        :type: str
        """
        

        self._output_path_id = output_path_id

    @property
    def execution_id(self) -> str:
        """
        Gets the execution_id of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the executionId for the executionItem.

        :return: The execution_id of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id: str) -> None:
        """
        Sets the execution_id of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the executionId for the executionItem.

        :param execution_id: The execution_id of this V2FlowExecutionDataFlowidTopicExecution.
        :type: str
        """
        

        self._execution_id = execution_id

    @property
    def start_date_time(self) -> datetime:
        """
        Gets the start_date_time of this V2FlowExecutionDataFlowidTopicExecution.
        This is the starting time of the executionItem.

        :return: The start_date_time of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time: datetime) -> None:
        """
        Sets the start_date_time of this V2FlowExecutionDataFlowidTopicExecution.
        This is the starting time of the executionItem.

        :param start_date_time: The start_date_time of this V2FlowExecutionDataFlowidTopicExecution.
        :type: datetime
        """
        

        self._start_date_time = start_date_time

    @property
    def error(self) -> 'V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo':
        """
        Gets the error of this V2FlowExecutionDataFlowidTopicExecution.
        Event generated when a Flow's Execution History is received and logged.

        :return: The error of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo
        """
        return self._error

    @error.setter
    def error(self, error: 'V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo') -> None:
        """
        Sets the error of this V2FlowExecutionDataFlowidTopicExecution.
        Event generated when a Flow's Execution History is received and logged.

        :param error: The error of this V2FlowExecutionDataFlowidTopicExecution.
        :type: V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo
        """
        

        self._error = error

    @property
    def warning(self) -> 'V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo':
        """
        Gets the warning of this V2FlowExecutionDataFlowidTopicExecution.
        Event generated when a Flow's Execution History is received and logged.

        :return: The warning of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo
        """
        return self._warning

    @warning.setter
    def warning(self, warning: 'V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo') -> None:
        """
        Sets the warning of this V2FlowExecutionDataFlowidTopicExecution.
        Event generated when a Flow's Execution History is received and logged.

        :param warning: The warning of this V2FlowExecutionDataFlowidTopicExecution.
        :type: V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo
        """
        

        self._warning = warning

    @property
    def language_tag(self) -> str:
        """
        Gets the language_tag of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the language tag associated set by the execution.

        :return: The language_tag of this V2FlowExecutionDataFlowidTopicExecution.
        :rtype: str
        """
        return self._language_tag

    @language_tag.setter
    def language_tag(self, language_tag: str) -> None:
        """
        Sets the language_tag of this V2FlowExecutionDataFlowidTopicExecution.
        If applicable, the language tag associated set by the execution.

        :param language_tag: The language_tag of this V2FlowExecutionDataFlowidTopicExecution.
        :type: str
        """
        

        self._language_tag = language_tag

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

