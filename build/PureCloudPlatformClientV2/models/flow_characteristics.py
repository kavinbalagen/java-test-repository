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


class FlowCharacteristics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowCharacteristics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'execution_items': 'bool',
            'execution_input_outputs': 'bool',
            'communications': 'bool',
            'event_error': 'bool',
            'event_warning': 'bool',
            'event_other': 'bool',
            'variables': 'bool',
            'names': 'bool'
        }

        self.attribute_map = {
            'execution_items': 'executionItems',
            'execution_input_outputs': 'executionInputOutputs',
            'communications': 'communications',
            'event_error': 'eventError',
            'event_warning': 'eventWarning',
            'event_other': 'eventOther',
            'variables': 'variables',
            'names': 'names'
        }

        self._execution_items = None
        self._execution_input_outputs = None
        self._communications = None
        self._event_error = None
        self._event_warning = None
        self._event_other = None
        self._variables = None
        self._names = None

    @property
    def execution_items(self) -> bool:
        """
        Gets the execution_items of this FlowCharacteristics.
        Whether to report execution data about individual actions, menus, states, tasks, etc. etc. that ran during execution of the flow.

        :return: The execution_items of this FlowCharacteristics.
        :rtype: bool
        """
        return self._execution_items

    @execution_items.setter
    def execution_items(self, execution_items: bool) -> None:
        """
        Sets the execution_items of this FlowCharacteristics.
        Whether to report execution data about individual actions, menus, states, tasks, etc. etc. that ran during execution of the flow.

        :param execution_items: The execution_items of this FlowCharacteristics.
        :type: bool
        """
        

        self._execution_items = execution_items

    @property
    def execution_input_outputs(self) -> bool:
        """
        Gets the execution_input_outputs of this FlowCharacteristics.
        Whether to report input setting input setting values and output data values for individual execution items above.  For example, if you have FlowExecutionInputOutputs and a Call Data Action ran in a flow, if FlowExecutionItems was enabled you'd see the fact a Call Data Action ran and the output path it took but nothing about which Data Action it ran, the input data sent to it at flow runtime and the data returned from it.  If you enable this characteristic, execution data will contain this additional detail.

        :return: The execution_input_outputs of this FlowCharacteristics.
        :rtype: bool
        """
        return self._execution_input_outputs

    @execution_input_outputs.setter
    def execution_input_outputs(self, execution_input_outputs: bool) -> None:
        """
        Sets the execution_input_outputs of this FlowCharacteristics.
        Whether to report input setting input setting values and output data values for individual execution items above.  For example, if you have FlowExecutionInputOutputs and a Call Data Action ran in a flow, if FlowExecutionItems was enabled you'd see the fact a Call Data Action ran and the output path it took but nothing about which Data Action it ran, the input data sent to it at flow runtime and the data returned from it.  If you enable this characteristic, execution data will contain this additional detail.

        :param execution_input_outputs: The execution_input_outputs of this FlowCharacteristics.
        :type: bool
        """
        

        self._execution_input_outputs = execution_input_outputs

    @property
    def communications(self) -> bool:
        """
        Gets the communications of this FlowCharacteristics.
        Communications are either audio or digital communications sent to or received from a participant.  An example here would be the initial greeting in an inbound call flow where it plays a greeting message to the participant.

        :return: The communications of this FlowCharacteristics.
        :rtype: bool
        """
        return self._communications

    @communications.setter
    def communications(self, communications: bool) -> None:
        """
        Sets the communications of this FlowCharacteristics.
        Communications are either audio or digital communications sent to or received from a participant.  An example here would be the initial greeting in an inbound call flow where it plays a greeting message to the participant.

        :param communications: The communications of this FlowCharacteristics.
        :type: bool
        """
        

        self._communications = communications

    @property
    def event_error(self) -> bool:
        """
        Gets the event_error of this FlowCharacteristics.
        Whether to report flow error events.

        :return: The event_error of this FlowCharacteristics.
        :rtype: bool
        """
        return self._event_error

    @event_error.setter
    def event_error(self, event_error: bool) -> None:
        """
        Sets the event_error of this FlowCharacteristics.
        Whether to report flow error events.

        :param event_error: The event_error of this FlowCharacteristics.
        :type: bool
        """
        

        self._event_error = event_error

    @property
    def event_warning(self) -> bool:
        """
        Gets the event_warning of this FlowCharacteristics.
        Whether to report flow warning events.

        :return: The event_warning of this FlowCharacteristics.
        :rtype: bool
        """
        return self._event_warning

    @event_warning.setter
    def event_warning(self, event_warning: bool) -> None:
        """
        Sets the event_warning of this FlowCharacteristics.
        Whether to report flow warning events.

        :param event_warning: The event_warning of this FlowCharacteristics.
        :type: bool
        """
        

        self._event_warning = event_warning

    @property
    def event_other(self) -> bool:
        """
        Gets the event_other of this FlowCharacteristics.
        Whether to report events other than errors or warnings such as a language change, loop event.

        :return: The event_other of this FlowCharacteristics.
        :rtype: bool
        """
        return self._event_other

    @event_other.setter
    def event_other(self, event_other: bool) -> None:
        """
        Sets the event_other of this FlowCharacteristics.
        Whether to report events other than errors or warnings such as a language change, loop event.

        :param event_other: The event_other of this FlowCharacteristics.
        :type: bool
        """
        

        self._event_other = event_other

    @property
    def variables(self) -> bool:
        """
        Gets the variables of this FlowCharacteristics.
        Whether to report assignment of values to variables in flow execution data. It's important to remember there is a difference between variable value assignments and output data from an action.  If you have a Call Digital Bot flow action in an Inbound Message flow and there is no variable bound to the Exit Reason output but FlowExecutionInputOutputs is enabled, you will still be able to see the exit reason from the digital bot flow in execution data even though it is not bound to a variable.

        :return: The variables of this FlowCharacteristics.
        :rtype: bool
        """
        return self._variables

    @variables.setter
    def variables(self, variables: bool) -> None:
        """
        Sets the variables of this FlowCharacteristics.
        Whether to report assignment of values to variables in flow execution data. It's important to remember there is a difference between variable value assignments and output data from an action.  If you have a Call Digital Bot flow action in an Inbound Message flow and there is no variable bound to the Exit Reason output but FlowExecutionInputOutputs is enabled, you will still be able to see the exit reason from the digital bot flow in execution data even though it is not bound to a variable.

        :param variables: The variables of this FlowCharacteristics.
        :type: bool
        """
        

        self._variables = variables

    @property
    def names(self) -> bool:
        """
        Gets the names of this FlowCharacteristics.
        This characteristic specifies whether or not name information should be emitted in execution data such as action, task, state or even the flow name itself.  Names are very handy from a readability standpoint but they do take up additional space in flow execution data instances.

        :return: The names of this FlowCharacteristics.
        :rtype: bool
        """
        return self._names

    @names.setter
    def names(self, names: bool) -> None:
        """
        Sets the names of this FlowCharacteristics.
        This characteristic specifies whether or not name information should be emitted in execution data such as action, task, state or even the flow name itself.  Names are very handy from a readability standpoint but they do take up additional space in flow execution data instances.

        :param names: The names of this FlowCharacteristics.
        :type: bool
        """
        

        self._names = names

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

