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


class Settings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Settings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'communication_based_acw': 'bool',
            'include_non_agent_conversation_summary': 'bool',
            'allow_callback_queue_selection': 'bool',
            'callbacks_inherit_routing_from_inbound_call': 'bool',
            'complete_acw_when_agent_transitions_offline': 'bool',
            'total_active_callback': 'bool'
        }

        self.attribute_map = {
            'communication_based_acw': 'communicationBasedACW',
            'include_non_agent_conversation_summary': 'includeNonAgentConversationSummary',
            'allow_callback_queue_selection': 'allowCallbackQueueSelection',
            'callbacks_inherit_routing_from_inbound_call': 'callbacksInheritRoutingFromInboundCall',
            'complete_acw_when_agent_transitions_offline': 'completeAcwWhenAgentTransitionsOffline',
            'total_active_callback': 'totalActiveCallback'
        }

        self._communication_based_acw = None
        self._include_non_agent_conversation_summary = None
        self._allow_callback_queue_selection = None
        self._callbacks_inherit_routing_from_inbound_call = None
        self._complete_acw_when_agent_transitions_offline = None
        self._total_active_callback = None

    @property
    def communication_based_acw(self) -> bool:
        """
        Gets the communication_based_acw of this Settings.
        Communication Based ACW

        :return: The communication_based_acw of this Settings.
        :rtype: bool
        """
        return self._communication_based_acw

    @communication_based_acw.setter
    def communication_based_acw(self, communication_based_acw: bool) -> None:
        """
        Sets the communication_based_acw of this Settings.
        Communication Based ACW

        :param communication_based_acw: The communication_based_acw of this Settings.
        :type: bool
        """
        

        self._communication_based_acw = communication_based_acw

    @property
    def include_non_agent_conversation_summary(self) -> bool:
        """
        Gets the include_non_agent_conversation_summary of this Settings.
        Display communication summary

        :return: The include_non_agent_conversation_summary of this Settings.
        :rtype: bool
        """
        return self._include_non_agent_conversation_summary

    @include_non_agent_conversation_summary.setter
    def include_non_agent_conversation_summary(self, include_non_agent_conversation_summary: bool) -> None:
        """
        Sets the include_non_agent_conversation_summary of this Settings.
        Display communication summary

        :param include_non_agent_conversation_summary: The include_non_agent_conversation_summary of this Settings.
        :type: bool
        """
        

        self._include_non_agent_conversation_summary = include_non_agent_conversation_summary

    @property
    def allow_callback_queue_selection(self) -> bool:
        """
        Gets the allow_callback_queue_selection of this Settings.
        Allow Callback Queue Selection

        :return: The allow_callback_queue_selection of this Settings.
        :rtype: bool
        """
        return self._allow_callback_queue_selection

    @allow_callback_queue_selection.setter
    def allow_callback_queue_selection(self, allow_callback_queue_selection: bool) -> None:
        """
        Sets the allow_callback_queue_selection of this Settings.
        Allow Callback Queue Selection

        :param allow_callback_queue_selection: The allow_callback_queue_selection of this Settings.
        :type: bool
        """
        

        self._allow_callback_queue_selection = allow_callback_queue_selection

    @property
    def callbacks_inherit_routing_from_inbound_call(self) -> bool:
        """
        Gets the callbacks_inherit_routing_from_inbound_call of this Settings.
        Inherit callback routing data from inbound calls

        :return: The callbacks_inherit_routing_from_inbound_call of this Settings.
        :rtype: bool
        """
        return self._callbacks_inherit_routing_from_inbound_call

    @callbacks_inherit_routing_from_inbound_call.setter
    def callbacks_inherit_routing_from_inbound_call(self, callbacks_inherit_routing_from_inbound_call: bool) -> None:
        """
        Sets the callbacks_inherit_routing_from_inbound_call of this Settings.
        Inherit callback routing data from inbound calls

        :param callbacks_inherit_routing_from_inbound_call: The callbacks_inherit_routing_from_inbound_call of this Settings.
        :type: bool
        """
        

        self._callbacks_inherit_routing_from_inbound_call = callbacks_inherit_routing_from_inbound_call

    @property
    def complete_acw_when_agent_transitions_offline(self) -> bool:
        """
        Gets the complete_acw_when_agent_transitions_offline of this Settings.
        Complete ACW When Agent Transitions Offline

        :return: The complete_acw_when_agent_transitions_offline of this Settings.
        :rtype: bool
        """
        return self._complete_acw_when_agent_transitions_offline

    @complete_acw_when_agent_transitions_offline.setter
    def complete_acw_when_agent_transitions_offline(self, complete_acw_when_agent_transitions_offline: bool) -> None:
        """
        Sets the complete_acw_when_agent_transitions_offline of this Settings.
        Complete ACW When Agent Transitions Offline

        :param complete_acw_when_agent_transitions_offline: The complete_acw_when_agent_transitions_offline of this Settings.
        :type: bool
        """
        

        self._complete_acw_when_agent_transitions_offline = complete_acw_when_agent_transitions_offline

    @property
    def total_active_callback(self) -> bool:
        """
        Gets the total_active_callback of this Settings.
        Exclude the 'interacting' duration from the handle calculations of callbacks

        :return: The total_active_callback of this Settings.
        :rtype: bool
        """
        return self._total_active_callback

    @total_active_callback.setter
    def total_active_callback(self, total_active_callback: bool) -> None:
        """
        Sets the total_active_callback of this Settings.
        Exclude the 'interacting' duration from the handle calculations of callbacks

        :param total_active_callback: The total_active_callback of this Settings.
        :type: bool
        """
        

        self._total_active_callback = total_active_callback

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
