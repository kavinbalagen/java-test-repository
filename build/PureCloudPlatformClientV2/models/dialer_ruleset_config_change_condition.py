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
    from . import DialerRulesetConfigChangeContactColumnToDataActionFieldMapping
    from . import DialerRulesetConfigChangeDataActionConditionPredicate
    from . import DialerRulesetConfigChangeUriReference

class DialerRulesetConfigChangeCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerRulesetConfigChangeCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_action': 'DialerRulesetConfigChangeUriReference',
            'additional_properties': 'dict(str, object)',
            'type': 'str',
            'inverted': 'bool',
            'attribute_name': 'str',
            'value': 'str',
            'value_type': 'str',
            'operator': 'str',
            'codes': 'list[str]',
            'property_type': 'str',
            'pcProperty': 'str',
            'data_not_found_resolution': 'bool',
            'contact_id_field': 'str',
            'call_analysis_result_field': 'str',
            'agent_wrapup_field': 'str',
            'contact_column_to_data_action_field_mappings': 'list[DialerRulesetConfigChangeContactColumnToDataActionFieldMapping]',
            'predicates': 'list[DialerRulesetConfigChangeDataActionConditionPredicate]'
        }

        self.attribute_map = {
            'data_action': 'dataAction',
            'additional_properties': 'additionalProperties',
            'type': 'type',
            'inverted': 'inverted',
            'attribute_name': 'attributeName',
            'value': 'value',
            'value_type': 'valueType',
            'operator': 'operator',
            'codes': 'codes',
            'property_type': 'propertyType',
            'pcProperty': 'property',
            'data_not_found_resolution': 'dataNotFoundResolution',
            'contact_id_field': 'contactIdField',
            'call_analysis_result_field': 'callAnalysisResultField',
            'agent_wrapup_field': 'agentWrapupField',
            'contact_column_to_data_action_field_mappings': 'contactColumnToDataActionFieldMappings',
            'predicates': 'predicates'
        }

        self._data_action = None
        self._additional_properties = None
        self._type = None
        self._inverted = None
        self._attribute_name = None
        self._value = None
        self._value_type = None
        self._operator = None
        self._codes = None
        self._property_type = None
        self._pcProperty = None
        self._data_not_found_resolution = None
        self._contact_id_field = None
        self._call_analysis_result_field = None
        self._agent_wrapup_field = None
        self._contact_column_to_data_action_field_mappings = None
        self._predicates = None

    @property
    def data_action(self) -> 'DialerRulesetConfigChangeUriReference':
        """
        Gets the data_action of this DialerRulesetConfigChangeCondition.
        A UriReference for a resource

        :return: The data_action of this DialerRulesetConfigChangeCondition.
        :rtype: DialerRulesetConfigChangeUriReference
        """
        return self._data_action

    @data_action.setter
    def data_action(self, data_action: 'DialerRulesetConfigChangeUriReference') -> None:
        """
        Sets the data_action of this DialerRulesetConfigChangeCondition.
        A UriReference for a resource

        :param data_action: The data_action of this DialerRulesetConfigChangeCondition.
        :type: DialerRulesetConfigChangeUriReference
        """
        

        self._data_action = data_action

    @property
    def additional_properties(self) -> Dict[str, object]:
        """
        Gets the additional_properties of this DialerRulesetConfigChangeCondition.


        :return: The additional_properties of this DialerRulesetConfigChangeCondition.
        :rtype: dict(str, object)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties: Dict[str, object]) -> None:
        """
        Sets the additional_properties of this DialerRulesetConfigChangeCondition.


        :param additional_properties: The additional_properties of this DialerRulesetConfigChangeCondition.
        :type: dict(str, object)
        """
        

        self._additional_properties = additional_properties

    @property
    def type(self) -> str:
        """
        Gets the type of this DialerRulesetConfigChangeCondition.
        The type of the condition

        :return: The type of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this DialerRulesetConfigChangeCondition.
        The type of the condition

        :param type: The type of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._type = type

    @property
    def inverted(self) -> bool:
        """
        Gets the inverted of this DialerRulesetConfigChangeCondition.
        Indicates whether to evaluate for the opposite of the stated condition; default is false

        :return: The inverted of this DialerRulesetConfigChangeCondition.
        :rtype: bool
        """
        return self._inverted

    @inverted.setter
    def inverted(self, inverted: bool) -> None:
        """
        Sets the inverted of this DialerRulesetConfigChangeCondition.
        Indicates whether to evaluate for the opposite of the stated condition; default is false

        :param inverted: The inverted of this DialerRulesetConfigChangeCondition.
        :type: bool
        """
        

        self._inverted = inverted

    @property
    def attribute_name(self) -> str:
        """
        Gets the attribute_name of this DialerRulesetConfigChangeCondition.
        An attribute name associated with the condition (applies only to certain rule conditions)

        :return: The attribute_name of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._attribute_name

    @attribute_name.setter
    def attribute_name(self, attribute_name: str) -> None:
        """
        Sets the attribute_name of this DialerRulesetConfigChangeCondition.
        An attribute name associated with the condition (applies only to certain rule conditions)

        :param attribute_name: The attribute_name of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._attribute_name = attribute_name

    @property
    def value(self) -> str:
        """
        Gets the value of this DialerRulesetConfigChangeCondition.
        A value associated with the condition

        :return: The value of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        """
        Sets the value of this DialerRulesetConfigChangeCondition.
        A value associated with the condition

        :param value: The value of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._value = value

    @property
    def value_type(self) -> str:
        """
        Gets the value_type of this DialerRulesetConfigChangeCondition.
        Determines the type of the value associated with the condition

        :return: The value_type of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type: str) -> None:
        """
        Sets the value_type of this DialerRulesetConfigChangeCondition.
        Determines the type of the value associated with the condition

        :param value_type: The value_type of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        if isinstance(value_type, int):
            value_type = str(value_type)
        allowed_values = ["STRING", "NUMERIC", "DATETIME", "PERIOD"]
        if value_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for value_type -> " + value_type)
            self._value_type = "outdated_sdk_version"
        else:
            self._value_type = value_type

    @property
    def operator(self) -> str:
        """
        Gets the operator of this DialerRulesetConfigChangeCondition.
        An operation type for condition evaluation

        :return: The operator of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator: str) -> None:
        """
        Sets the operator of this DialerRulesetConfigChangeCondition.
        An operation type for condition evaluation

        :param operator: The operator of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        if isinstance(operator, int):
            operator = str(operator)
        allowed_values = ["EQUALS", "LESS_THAN", "LESS_THAN_EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "CONTAINS", "BEGINS_WITH", "ENDS_WITH", "BEFORE", "AFTER"]
        if operator.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for operator -> " + operator)
            self._operator = "outdated_sdk_version"
        else:
            self._operator = operator

    @property
    def codes(self) -> List[str]:
        """
        Gets the codes of this DialerRulesetConfigChangeCondition.
        List of wrap-up code identifiers (used only in conditions of type 'wrapupCondition')

        :return: The codes of this DialerRulesetConfigChangeCondition.
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes: List[str]) -> None:
        """
        Sets the codes of this DialerRulesetConfigChangeCondition.
        List of wrap-up code identifiers (used only in conditions of type 'wrapupCondition')

        :param codes: The codes of this DialerRulesetConfigChangeCondition.
        :type: list[str]
        """
        

        self._codes = codes

    @property
    def property_type(self) -> str:
        """
        Gets the property_type of this DialerRulesetConfigChangeCondition.
        Determines the type of the property associated with the condition

        :return: The property_type of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type: str) -> None:
        """
        Sets the property_type of this DialerRulesetConfigChangeCondition.
        Determines the type of the property associated with the condition

        :param property_type: The property_type of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        if isinstance(property_type, int):
            property_type = str(property_type)
        allowed_values = ["LAST_ATTEMPT_BY_COLUMN", "LAST_ATTEMPT_OVERALL", "LAST_RESULT_BY_COLUMN", "LAST_RESULT_OVERALL"]
        if property_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for property_type -> " + property_type)
            self._property_type = "outdated_sdk_version"
        else:
            self._property_type = property_type

    @property
    def pcProperty(self) -> str:
        """
        Gets the pcProperty of this DialerRulesetConfigChangeCondition.
        A value associated with the property type of this condition

        :return: The pcProperty of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._pcProperty

    @pcProperty.setter
    def pcProperty(self, pcProperty: str) -> None:
        """
        Sets the pcProperty of this DialerRulesetConfigChangeCondition.
        A value associated with the property type of this condition

        :param pcProperty: The pcProperty of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._pcProperty = pcProperty

    @property
    def data_not_found_resolution(self) -> bool:
        """
        Gets the data_not_found_resolution of this DialerRulesetConfigChangeCondition.
        The result of this condition if the data action returns a result indicating there was no data. Required for a DataActionCondition.

        :return: The data_not_found_resolution of this DialerRulesetConfigChangeCondition.
        :rtype: bool
        """
        return self._data_not_found_resolution

    @data_not_found_resolution.setter
    def data_not_found_resolution(self, data_not_found_resolution: bool) -> None:
        """
        Sets the data_not_found_resolution of this DialerRulesetConfigChangeCondition.
        The result of this condition if the data action returns a result indicating there was no data. Required for a DataActionCondition.

        :param data_not_found_resolution: The data_not_found_resolution of this DialerRulesetConfigChangeCondition.
        :type: bool
        """
        

        self._data_not_found_resolution = data_not_found_resolution

    @property
    def contact_id_field(self) -> str:
        """
        Gets the contact_id_field of this DialerRulesetConfigChangeCondition.
        The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionCondition.

        :return: The contact_id_field of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._contact_id_field

    @contact_id_field.setter
    def contact_id_field(self, contact_id_field: str) -> None:
        """
        Sets the contact_id_field of this DialerRulesetConfigChangeCondition.
        The input field from the data action that the contactId will be passed to for this condition. Valid for a dataActionCondition.

        :param contact_id_field: The contact_id_field of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._contact_id_field = contact_id_field

    @property
    def call_analysis_result_field(self) -> str:
        """
        Gets the call_analysis_result_field of this DialerRulesetConfigChangeCondition.
        The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :return: The call_analysis_result_field of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._call_analysis_result_field

    @call_analysis_result_field.setter
    def call_analysis_result_field(self, call_analysis_result_field: str) -> None:
        """
        Sets the call_analysis_result_field of this DialerRulesetConfigChangeCondition.
        The input field from the data action that the callAnalysisResult will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :param call_analysis_result_field: The call_analysis_result_field of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._call_analysis_result_field = call_analysis_result_field

    @property
    def agent_wrapup_field(self) -> str:
        """
        Gets the agent_wrapup_field of this DialerRulesetConfigChangeCondition.
        The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :return: The agent_wrapup_field of this DialerRulesetConfigChangeCondition.
        :rtype: str
        """
        return self._agent_wrapup_field

    @agent_wrapup_field.setter
    def agent_wrapup_field(self, agent_wrapup_field: str) -> None:
        """
        Sets the agent_wrapup_field of this DialerRulesetConfigChangeCondition.
        The input field from the data action that the agentWrapup will be passed to for this condition. Valid for a wrapup dataActionCondition.

        :param agent_wrapup_field: The agent_wrapup_field of this DialerRulesetConfigChangeCondition.
        :type: str
        """
        

        self._agent_wrapup_field = agent_wrapup_field

    @property
    def contact_column_to_data_action_field_mappings(self) -> List['DialerRulesetConfigChangeContactColumnToDataActionFieldMapping']:
        """
        Gets the contact_column_to_data_action_field_mappings of this DialerRulesetConfigChangeCondition.
        A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionCondition.

        :return: The contact_column_to_data_action_field_mappings of this DialerRulesetConfigChangeCondition.
        :rtype: list[DialerRulesetConfigChangeContactColumnToDataActionFieldMapping]
        """
        return self._contact_column_to_data_action_field_mappings

    @contact_column_to_data_action_field_mappings.setter
    def contact_column_to_data_action_field_mappings(self, contact_column_to_data_action_field_mappings: List['DialerRulesetConfigChangeContactColumnToDataActionFieldMapping']) -> None:
        """
        Sets the contact_column_to_data_action_field_mappings of this DialerRulesetConfigChangeCondition.
        A list of mappings defining which contact data fields will be passed to which data action input fields for this condition. Valid for a dataActionCondition.

        :param contact_column_to_data_action_field_mappings: The contact_column_to_data_action_field_mappings of this DialerRulesetConfigChangeCondition.
        :type: list[DialerRulesetConfigChangeContactColumnToDataActionFieldMapping]
        """
        

        self._contact_column_to_data_action_field_mappings = contact_column_to_data_action_field_mappings

    @property
    def predicates(self) -> List['DialerRulesetConfigChangeDataActionConditionPredicate']:
        """
        Gets the predicates of this DialerRulesetConfigChangeCondition.
        A list of predicates defining the comparisons to use for this condition. Required for a dataActionCondition.

        :return: The predicates of this DialerRulesetConfigChangeCondition.
        :rtype: list[DialerRulesetConfigChangeDataActionConditionPredicate]
        """
        return self._predicates

    @predicates.setter
    def predicates(self, predicates: List['DialerRulesetConfigChangeDataActionConditionPredicate']) -> None:
        """
        Sets the predicates of this DialerRulesetConfigChangeCondition.
        A list of predicates defining the comparisons to use for this condition. Required for a dataActionCondition.

        :param predicates: The predicates of this DialerRulesetConfigChangeCondition.
        :type: list[DialerRulesetConfigChangeDataActionConditionPredicate]
        """
        

        self._predicates = predicates

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
