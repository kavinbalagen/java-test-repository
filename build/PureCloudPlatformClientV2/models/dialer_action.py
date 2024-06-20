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
    from . import ContactColumnToDataActionFieldMapping
    from . import DomainEntityRef

class DialerAction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerAction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'action_type_name': 'str',
            'update_option': 'str',
            'properties': 'dict(str, str)',
            'data_action': 'DomainEntityRef',
            'contact_column_to_data_action_field_mappings': 'list[ContactColumnToDataActionFieldMapping]',
            'contact_id_field': 'str',
            'call_analysis_result_field': 'str',
            'agent_wrapup_field': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'action_type_name': 'actionTypeName',
            'update_option': 'updateOption',
            'properties': 'properties',
            'data_action': 'dataAction',
            'contact_column_to_data_action_field_mappings': 'contactColumnToDataActionFieldMappings',
            'contact_id_field': 'contactIdField',
            'call_analysis_result_field': 'callAnalysisResultField',
            'agent_wrapup_field': 'agentWrapupField'
        }

        self._type = None
        self._action_type_name = None
        self._update_option = None
        self._properties = None
        self._data_action = None
        self._contact_column_to_data_action_field_mappings = None
        self._contact_id_field = None
        self._call_analysis_result_field = None
        self._agent_wrapup_field = None

    @property
    def type(self) -> str:
        """
        Gets the type of this DialerAction.
        The type of this DialerAction.

        :return: The type of this DialerAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this DialerAction.
        The type of this DialerAction.

        :param type: The type of this DialerAction.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Action", "modifyContactAttribute", "dataActionBehavior"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def action_type_name(self) -> str:
        """
        Gets the action_type_name of this DialerAction.
        Additional type specification for this DialerAction.

        :return: The action_type_name of this DialerAction.
        :rtype: str
        """
        return self._action_type_name

    @action_type_name.setter
    def action_type_name(self, action_type_name: str) -> None:
        """
        Sets the action_type_name of this DialerAction.
        Additional type specification for this DialerAction.

        :param action_type_name: The action_type_name of this DialerAction.
        :type: str
        """
        if isinstance(action_type_name, int):
            action_type_name = str(action_type_name)
        allowed_values = ["DO_NOT_DIAL", "MODIFY_CONTACT_ATTRIBUTE", "SWITCH_TO_PREVIEW", "APPEND_NUMBER_TO_DNC_LIST", "APPEND_CUSTOM_ENTRY_TO_DNC_LIST", "SCHEDULE_CALLBACK", "CONTACT_UNCALLABLE", "NUMBER_UNCALLABLE", "SET_CALLER_ID", "SET_SKILLS", "DATA_ACTION"]
        if action_type_name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action_type_name -> " + action_type_name)
            self._action_type_name = "outdated_sdk_version"
        else:
            self._action_type_name = action_type_name

    @property
    def update_option(self) -> str:
        """
        Gets the update_option of this DialerAction.
        Specifies how a contact attribute should be updated. Required for MODIFY_CONTACT_ATTRIBUTE.

        :return: The update_option of this DialerAction.
        :rtype: str
        """
        return self._update_option

    @update_option.setter
    def update_option(self, update_option: str) -> None:
        """
        Sets the update_option of this DialerAction.
        Specifies how a contact attribute should be updated. Required for MODIFY_CONTACT_ATTRIBUTE.

        :param update_option: The update_option of this DialerAction.
        :type: str
        """
        if isinstance(update_option, int):
            update_option = str(update_option)
        allowed_values = ["SET", "INCREMENT", "DECREMENT", "CURRENT_TIME"]
        if update_option.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for update_option -> " + update_option)
            self._update_option = "outdated_sdk_version"
        else:
            self._update_option = update_option

    @property
    def properties(self) -> Dict[str, str]:
        """
        Gets the properties of this DialerAction.
        A map of key-value pairs pertinent to the DialerAction. Different types of DialerActions require different properties. MODIFY_CONTACT_ATTRIBUTE with an updateOption of SET takes a contact column as the key and accepts any value. SCHEDULE_CALLBACK takes a key 'callbackOffset' that specifies how far in the future the callback should be scheduled, in minutes. SET_CALLER_ID takes two keys: 'callerAddress', which should be the caller id phone number, and 'callerName'. For either key, you can also specify a column on the contact to get the value from. To do this, specify 'contact.Column', where 'Column' is the name of the contact column from which to get the value. SET_SKILLS takes a key 'skills' with an array of skill ids wrapped into a string (Example: {'skills': '['skillIdHere']'} ).

        :return: The properties of this DialerAction.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, str]) -> None:
        """
        Sets the properties of this DialerAction.
        A map of key-value pairs pertinent to the DialerAction. Different types of DialerActions require different properties. MODIFY_CONTACT_ATTRIBUTE with an updateOption of SET takes a contact column as the key and accepts any value. SCHEDULE_CALLBACK takes a key 'callbackOffset' that specifies how far in the future the callback should be scheduled, in minutes. SET_CALLER_ID takes two keys: 'callerAddress', which should be the caller id phone number, and 'callerName'. For either key, you can also specify a column on the contact to get the value from. To do this, specify 'contact.Column', where 'Column' is the name of the contact column from which to get the value. SET_SKILLS takes a key 'skills' with an array of skill ids wrapped into a string (Example: {'skills': '['skillIdHere']'} ).

        :param properties: The properties of this DialerAction.
        :type: dict(str, str)
        """
        

        self._properties = properties

    @property
    def data_action(self) -> 'DomainEntityRef':
        """
        Gets the data_action of this DialerAction.
        The Data Action to use for this action. Required for a dataActionBehavior.

        :return: The data_action of this DialerAction.
        :rtype: DomainEntityRef
        """
        return self._data_action

    @data_action.setter
    def data_action(self, data_action: 'DomainEntityRef') -> None:
        """
        Sets the data_action of this DialerAction.
        The Data Action to use for this action. Required for a dataActionBehavior.

        :param data_action: The data_action of this DialerAction.
        :type: DomainEntityRef
        """
        

        self._data_action = data_action

    @property
    def contact_column_to_data_action_field_mappings(self) -> List['ContactColumnToDataActionFieldMapping']:
        """
        Gets the contact_column_to_data_action_field_mappings of this DialerAction.
        A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionBehavior.

        :return: The contact_column_to_data_action_field_mappings of this DialerAction.
        :rtype: list[ContactColumnToDataActionFieldMapping]
        """
        return self._contact_column_to_data_action_field_mappings

    @contact_column_to_data_action_field_mappings.setter
    def contact_column_to_data_action_field_mappings(self, contact_column_to_data_action_field_mappings: List['ContactColumnToDataActionFieldMapping']) -> None:
        """
        Sets the contact_column_to_data_action_field_mappings of this DialerAction.
        A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionBehavior.

        :param contact_column_to_data_action_field_mappings: The contact_column_to_data_action_field_mappings of this DialerAction.
        :type: list[ContactColumnToDataActionFieldMapping]
        """
        

        self._contact_column_to_data_action_field_mappings = contact_column_to_data_action_field_mappings

    @property
    def contact_id_field(self) -> str:
        """
        Gets the contact_id_field of this DialerAction.
        The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionBehavior.

        :return: The contact_id_field of this DialerAction.
        :rtype: str
        """
        return self._contact_id_field

    @contact_id_field.setter
    def contact_id_field(self, contact_id_field: str) -> None:
        """
        Sets the contact_id_field of this DialerAction.
        The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionBehavior.

        :param contact_id_field: The contact_id_field of this DialerAction.
        :type: str
        """
        

        self._contact_id_field = contact_id_field

    @property
    def call_analysis_result_field(self) -> str:
        """
        Gets the call_analysis_result_field of this DialerAction.
        The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionBehavior.

        :return: The call_analysis_result_field of this DialerAction.
        :rtype: str
        """
        return self._call_analysis_result_field

    @call_analysis_result_field.setter
    def call_analysis_result_field(self, call_analysis_result_field: str) -> None:
        """
        Sets the call_analysis_result_field of this DialerAction.
        The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionBehavior.

        :param call_analysis_result_field: The call_analysis_result_field of this DialerAction.
        :type: str
        """
        

        self._call_analysis_result_field = call_analysis_result_field

    @property
    def agent_wrapup_field(self) -> str:
        """
        Gets the agent_wrapup_field of this DialerAction.
        The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionBehavior.

        :return: The agent_wrapup_field of this DialerAction.
        :rtype: str
        """
        return self._agent_wrapup_field

    @agent_wrapup_field.setter
    def agent_wrapup_field(self, agent_wrapup_field: str) -> None:
        """
        Sets the agent_wrapup_field of this DialerAction.
        The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionBehavior.

        :param agent_wrapup_field: The agent_wrapup_field of this DialerAction.
        :type: str
        """
        

        self._agent_wrapup_field = agent_wrapup_field

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

