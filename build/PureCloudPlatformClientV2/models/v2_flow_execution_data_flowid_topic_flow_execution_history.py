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
    from . import V2FlowExecutionDataFlowidTopicExecution
    from . import V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo
    from . import V2FlowExecutionDataFlowidTopicInvokingContext

class V2FlowExecutionDataFlowidTopicFlowExecutionHistory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        V2FlowExecutionDataFlowidTopicFlowExecutionHistory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'execution_id': 'str',
            'conversation_id': 'str',
            'division_id': 'str',
            'end_date_time': 'datetime',
            'endpoint': 'str',
            'errors': 'list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]',
            'execution': 'list[V2FlowExecutionDataFlowidTopicExecution]',
            'flow_exit_reason': 'str',
            'flow_id': 'str',
            'flow_is_debug': 'bool',
            'execution_items_truncated': 'bool',
            'flow_type': 'str',
            'flow_version': 'str',
            'message_type': 'str',
            'invoking_context': 'V2FlowExecutionDataFlowidTopicInvokingContext',
            'start_date_time': 'datetime',
            'warnings': 'list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]'
        }

        self.attribute_map = {
            'execution_id': 'executionId',
            'conversation_id': 'conversationId',
            'division_id': 'divisionId',
            'end_date_time': 'endDateTime',
            'endpoint': 'endpoint',
            'errors': 'errors',
            'execution': 'execution',
            'flow_exit_reason': 'flowExitReason',
            'flow_id': 'flowId',
            'flow_is_debug': 'flowIsDebug',
            'execution_items_truncated': 'executionItemsTruncated',
            'flow_type': 'flowType',
            'flow_version': 'flowVersion',
            'message_type': 'messageType',
            'invoking_context': 'invokingContext',
            'start_date_time': 'startDateTime',
            'warnings': 'warnings'
        }

        self._execution_id = None
        self._conversation_id = None
        self._division_id = None
        self._end_date_time = None
        self._endpoint = None
        self._errors = None
        self._execution = None
        self._flow_exit_reason = None
        self._flow_id = None
        self._flow_is_debug = None
        self._execution_items_truncated = None
        self._flow_type = None
        self._flow_version = None
        self._message_type = None
        self._invoking_context = None
        self._start_date_time = None
        self._warnings = None

    @property
    def execution_id(self) -> str:
        """
        Gets the execution_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The execution identifier which represents this unique instance of the flow that ran.

        :return: The execution_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id: str) -> None:
        """
        Sets the execution_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The execution identifier which represents this unique instance of the flow that ran.

        :param execution_id: The execution_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._execution_id = execution_id

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The Genesys Cloud conversation identifier associated with this flow instance execution data.

        :return: The conversation_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The Genesys Cloud conversation identifier associated with this flow instance execution data.

        :param conversation_id: The conversation_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def division_id(self) -> str:
        """
        Gets the division_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The division identifier for the division associated with the flow for this flow instance.

        :return: The division_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._division_id

    @division_id.setter
    def division_id(self, division_id: str) -> None:
        """
        Sets the division_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The division identifier for the division associated with the flow for this flow instance.

        :param division_id: The division_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._division_id = division_id

    @property
    def end_date_time(self) -> datetime:
        """
        Gets the end_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The end date time for this flow instance execution data.

        :return: The end_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time: datetime) -> None:
        """
        Sets the end_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The end date time for this flow instance execution data.

        :param end_date_time: The end_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: datetime
        """
        

        self._end_date_time = end_date_time

    @property
    def endpoint(self) -> str:
        """
        Gets the endpoint of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The public endpoint a user can use to retrieve the full historical log from the service.

        :return: The endpoint of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str) -> None:
        """
        Sets the endpoint of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The public endpoint a user can use to retrieve the full historical log from the service.

        :param endpoint: The endpoint of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._endpoint = endpoint

    @property
    def errors(self) -> List['V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo']:
        """
        Gets the errors of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If the flow invoked error handling, an array of errors.

        :return: The errors of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List['V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo']) -> None:
        """
        Sets the errors of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If the flow invoked error handling, an array of errors.

        :param errors: The errors of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]
        """
        

        self._errors = errors

    @property
    def execution(self) -> List['V2FlowExecutionDataFlowidTopicExecution']:
        """
        Gets the execution of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        An array of execution items that describe what happened when an Architect flow action container ran such as a flow, task, state or bot.

        :return: The execution of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: list[V2FlowExecutionDataFlowidTopicExecution]
        """
        return self._execution

    @execution.setter
    def execution(self, execution: List['V2FlowExecutionDataFlowidTopicExecution']) -> None:
        """
        Sets the execution of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        An array of execution items that describe what happened when an Architect flow action container ran such as a flow, task, state or bot.

        :param execution: The execution of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: list[V2FlowExecutionDataFlowidTopicExecution]
        """
        

        self._execution = execution

    @property
    def flow_exit_reason(self) -> str:
        """
        Gets the flow_exit_reason of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        Provides information about why a flow ended.

        :return: The flow_exit_reason of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._flow_exit_reason

    @flow_exit_reason.setter
    def flow_exit_reason(self, flow_exit_reason: str) -> None:
        """
        Sets the flow_exit_reason of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        Provides information about why a flow ended.

        :param flow_exit_reason: The flow_exit_reason of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._flow_exit_reason = flow_exit_reason

    @property
    def flow_id(self) -> str:
        """
        Gets the flow_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The flow identifier for this flow instance execution data.  This is the identifier of the flow configuration that users load up in Architect.

        :return: The flow_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id: str) -> None:
        """
        Sets the flow_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The flow identifier for this flow instance execution data.  This is the identifier of the flow configuration that users load up in Architect.

        :param flow_id: The flow_id of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._flow_id = flow_id

    @property
    def flow_is_debug(self) -> bool:
        """
        Gets the flow_is_debug of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        Whether the flow that ran for this flow instance execution data was in debug mode.

        :return: The flow_is_debug of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: bool
        """
        return self._flow_is_debug

    @flow_is_debug.setter
    def flow_is_debug(self, flow_is_debug: bool) -> None:
        """
        Sets the flow_is_debug of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        Whether the flow that ran for this flow instance execution data was in debug mode.

        :param flow_is_debug: The flow_is_debug of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: bool
        """
        

        self._flow_is_debug = flow_is_debug

    @property
    def execution_items_truncated(self) -> bool:
        """
        Gets the execution_items_truncated of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If true, the execution items in this event have been truncated to be deliverable.

        :return: The execution_items_truncated of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: bool
        """
        return self._execution_items_truncated

    @execution_items_truncated.setter
    def execution_items_truncated(self, execution_items_truncated: bool) -> None:
        """
        Sets the execution_items_truncated of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If true, the execution items in this event have been truncated to be deliverable.

        :param execution_items_truncated: The execution_items_truncated of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: bool
        """
        

        self._execution_items_truncated = execution_items_truncated

    @property
    def flow_type(self) -> str:
        """
        Gets the flow_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The flow type of the Architect flow that was run.

        :return: The flow_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._flow_type

    @flow_type.setter
    def flow_type(self, flow_type: str) -> None:
        """
        Sets the flow_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The flow type of the Architect flow that was run.

        :param flow_type: The flow_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._flow_type = flow_type

    @property
    def flow_version(self) -> str:
        """
        Gets the flow_version of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The version of the flow for this flow instance execution data. Typically this is a numeric value like 1.0 represented as a string but can also be 'debug'

        :return: The flow_version of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._flow_version

    @flow_version.setter
    def flow_version(self, flow_version: str) -> None:
        """
        Sets the flow_version of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The version of the flow for this flow instance execution data. Typically this is a numeric value like 1.0 represented as a string but can also be 'debug'

        :param flow_version: The flow_version of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        

        self._flow_version = flow_version

    @property
    def message_type(self) -> str:
        """
        Gets the message_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If applicable, the type of message platform from which the message originated.

        :return: The message_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type: str) -> None:
        """
        Sets the message_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If applicable, the type of message platform from which the message originated.

        :param message_type: The message_type of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: str
        """
        if isinstance(message_type, int):
            message_type = str(message_type)
        allowed_values = ["unknown", "sms", "twitter", "facebook", "instagram", "line", "whatsapp", "webmessaging", "open"]
        if message_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for message_type -> " + message_type)
            self._message_type = "outdated_sdk_version"
        else:
            self._message_type = message_type

    @property
    def invoking_context(self) -> 'V2FlowExecutionDataFlowidTopicInvokingContext':
        """
        Gets the invoking_context of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.


        :return: The invoking_context of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: V2FlowExecutionDataFlowidTopicInvokingContext
        """
        return self._invoking_context

    @invoking_context.setter
    def invoking_context(self, invoking_context: 'V2FlowExecutionDataFlowidTopicInvokingContext') -> None:
        """
        Sets the invoking_context of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.


        :param invoking_context: The invoking_context of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: V2FlowExecutionDataFlowidTopicInvokingContext
        """
        

        self._invoking_context = invoking_context

    @property
    def start_date_time(self) -> datetime:
        """
        Gets the start_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The start date time for this flow instance execution data.

        :return: The start_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time: datetime) -> None:
        """
        Sets the start_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        The start date time for this flow instance execution data.

        :param start_date_time: The start_date_time of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: datetime
        """
        

        self._start_date_time = start_date_time

    @property
    def warnings(self) -> List['V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo']:
        """
        Gets the warnings of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If the flow encountered a warning during execution, this is an array of the warnings.

        :return: The warnings of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :rtype: list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings: List['V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo']) -> None:
        """
        Sets the warnings of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        If the flow encountered a warning during execution, this is an array of the warnings.

        :param warnings: The warnings of this V2FlowExecutionDataFlowidTopicFlowExecutionHistory.
        :type: list[V2FlowExecutionDataFlowidTopicFlowErrorWarningInfo]
        """
        

        self._warnings = warnings

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

