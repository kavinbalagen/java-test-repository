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


class SplittingInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SplittingInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'criteria': 'str',
            'criteria_value': 'str',
            'create_remainder_contact_list': 'bool',
            'use_waterfall_rule': 'bool'
        }

        self.attribute_map = {
            'criteria': 'criteria',
            'criteria_value': 'criteriaValue',
            'create_remainder_contact_list': 'createRemainderContactList',
            'use_waterfall_rule': 'useWaterfallRule'
        }

        self._criteria = None
        self._criteria_value = None
        self._create_remainder_contact_list = None
        self._use_waterfall_rule = None

    @property
    def criteria(self) -> str:
        """
        Gets the criteria of this SplittingInformation.
        The splitting criteria type

        :return: The criteria of this SplittingInformation.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: str) -> None:
        """
        Sets the criteria of this SplittingInformation.
        The splitting criteria type

        :param criteria: The criteria of this SplittingInformation.
        :type: str
        """
        if isinstance(criteria, int):
            criteria = str(criteria)
        allowed_values = ["Percentage", "Quantity", "Column", "Custom"]
        if criteria.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for criteria -> " + criteria)
            self._criteria = "outdated_sdk_version"
        else:
            self._criteria = criteria

    @property
    def criteria_value(self) -> str:
        """
        Gets the criteria_value of this SplittingInformation.
        The criteria value for the specified criteria type

        :return: The criteria_value of this SplittingInformation.
        :rtype: str
        """
        return self._criteria_value

    @criteria_value.setter
    def criteria_value(self, criteria_value: str) -> None:
        """
        Sets the criteria_value of this SplittingInformation.
        The criteria value for the specified criteria type

        :param criteria_value: The criteria_value of this SplittingInformation.
        :type: str
        """
        

        self._criteria_value = criteria_value

    @property
    def create_remainder_contact_list(self) -> bool:
        """
        Gets the create_remainder_contact_list of this SplittingInformation.
        Whether to create remainder contact list

        :return: The create_remainder_contact_list of this SplittingInformation.
        :rtype: bool
        """
        return self._create_remainder_contact_list

    @create_remainder_contact_list.setter
    def create_remainder_contact_list(self, create_remainder_contact_list: bool) -> None:
        """
        Sets the create_remainder_contact_list of this SplittingInformation.
        Whether to create remainder contact list

        :param create_remainder_contact_list: The create_remainder_contact_list of this SplittingInformation.
        :type: bool
        """
        

        self._create_remainder_contact_list = create_remainder_contact_list

    @property
    def use_waterfall_rule(self) -> bool:
        """
        Gets the use_waterfall_rule of this SplittingInformation.
        Whether to use waterfall rule

        :return: The use_waterfall_rule of this SplittingInformation.
        :rtype: bool
        """
        return self._use_waterfall_rule

    @use_waterfall_rule.setter
    def use_waterfall_rule(self, use_waterfall_rule: bool) -> None:
        """
        Sets the use_waterfall_rule of this SplittingInformation.
        Whether to use waterfall rule

        :param use_waterfall_rule: The use_waterfall_rule of this SplittingInformation.
        :type: bool
        """
        

        self._use_waterfall_rule = use_waterfall_rule

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

