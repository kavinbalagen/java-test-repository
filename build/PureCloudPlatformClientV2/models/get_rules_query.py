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


class GetRulesQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GetRulesQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rule_type': 'str',
            'query_type': 'str',
            'enabled_type': 'str',
            'page_number': 'int',
            'page_size': 'int',
            'sort_by': 'str',
            'sort_order': 'str',
            'rule_name': 'str',
            'name_search_type': 'str'
        }

        self.attribute_map = {
            'rule_type': 'ruleType',
            'query_type': 'queryType',
            'enabled_type': 'enabledType',
            'page_number': 'pageNumber',
            'page_size': 'pageSize',
            'sort_by': 'sortBy',
            'sort_order': 'sortOrder',
            'rule_name': 'ruleName',
            'name_search_type': 'nameSearchType'
        }

        self._rule_type = None
        self._query_type = None
        self._enabled_type = None
        self._page_number = None
        self._page_size = None
        self._sort_by = None
        self._sort_order = None
        self._rule_name = None
        self._name_search_type = None

    @property
    def rule_type(self) -> str:
        """
        Gets the rule_type of this GetRulesQuery.
        The rule type of the alerts the query will return

        :return: The rule_type of this GetRulesQuery.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type: str) -> None:
        """
        Sets the rule_type of this GetRulesQuery.
        The rule type of the alerts the query will return

        :param rule_type: The rule_type of this GetRulesQuery.
        :type: str
        """
        if isinstance(rule_type, int):
            rule_type = str(rule_type)
        allowed_values = ["Conversation", "Presence", "All"]
        if rule_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for rule_type -> " + rule_type)
            self._rule_type = "outdated_sdk_version"
        else:
            self._rule_type = rule_type

    @property
    def query_type(self) -> str:
        """
        Gets the query_type of this GetRulesQuery.
        The type of query being performed.

        :return: The query_type of this GetRulesQuery.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type: str) -> None:
        """
        Sets the query_type of this GetRulesQuery.
        The type of query being performed.

        :param query_type: The query_type of this GetRulesQuery.
        :type: str
        """
        if isinstance(query_type, int):
            query_type = str(query_type)
        allowed_values = ["Info", "Count"]
        if query_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_type -> " + query_type)
            self._query_type = "outdated_sdk_version"
        else:
            self._query_type = query_type

    @property
    def enabled_type(self) -> str:
        """
        Gets the enabled_type of this GetRulesQuery.
        The state of the rule the query will return.  The accepted choices are Enabled, Disabled, or All

        :return: The enabled_type of this GetRulesQuery.
        :rtype: str
        """
        return self._enabled_type

    @enabled_type.setter
    def enabled_type(self, enabled_type: str) -> None:
        """
        Sets the enabled_type of this GetRulesQuery.
        The state of the rule the query will return.  The accepted choices are Enabled, Disabled, or All

        :param enabled_type: The enabled_type of this GetRulesQuery.
        :type: str
        """
        if isinstance(enabled_type, int):
            enabled_type = str(enabled_type)
        allowed_values = ["Enabled", "Disabled", "All"]
        if enabled_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for enabled_type -> " + enabled_type)
            self._enabled_type = "outdated_sdk_version"
        else:
            self._enabled_type = enabled_type

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this GetRulesQuery.
        The page number of the queried response

        :return: The page_number of this GetRulesQuery.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this GetRulesQuery.
        The page number of the queried response

        :param page_number: The page_number of this GetRulesQuery.
        :type: int
        """
        

        self._page_number = page_number

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this GetRulesQuery.
        The number of entities to return of the queried response.  The max is 25

        :return: The page_size of this GetRulesQuery.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this GetRulesQuery.
        The number of entities to return of the queried response.  The max is 25

        :param page_size: The page_size of this GetRulesQuery.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def sort_by(self) -> str:
        """
        Gets the sort_by of this GetRulesQuery.
        The field to sort responses by.  The accepted choices are Name and DateStart

        :return: The sort_by of this GetRulesQuery.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by: str) -> None:
        """
        Sets the sort_by of this GetRulesQuery.
        The field to sort responses by.  The accepted choices are Name and DateStart

        :param sort_by: The sort_by of this GetRulesQuery.
        :type: str
        """
        if isinstance(sort_by, int):
            sort_by = str(sort_by)
        allowed_values = ["Name", "DateCreated"]
        if sort_by.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for sort_by -> " + sort_by)
            self._sort_by = "outdated_sdk_version"
        else:
            self._sort_by = sort_by

    @property
    def sort_order(self) -> str:
        """
        Gets the sort_order of this GetRulesQuery.
        The order in which response will be sorted.  The accepted choices are Asc and Desc

        :return: The sort_order of this GetRulesQuery.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order: str) -> None:
        """
        Sets the sort_order of this GetRulesQuery.
        The order in which response will be sorted.  The accepted choices are Asc and Desc

        :param sort_order: The sort_order of this GetRulesQuery.
        :type: str
        """
        if isinstance(sort_order, int):
            sort_order = str(sort_order)
        allowed_values = ["Asc", "Desc"]
        if sort_order.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for sort_order -> " + sort_order)
            self._sort_order = "outdated_sdk_version"
        else:
            self._sort_order = sort_order

    @property
    def rule_name(self) -> str:
        """
        Gets the rule_name of this GetRulesQuery.
        The name of the rule being queries.

        :return: The rule_name of this GetRulesQuery.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name: str) -> None:
        """
        Sets the rule_name of this GetRulesQuery.
        The name of the rule being queries.

        :param rule_name: The rule_name of this GetRulesQuery.
        :type: str
        """
        

        self._rule_name = rule_name

    @property
    def name_search_type(self) -> str:
        """
        Gets the name_search_type of this GetRulesQuery.
        Specifies how strict the name search needs to be. Expected values are Exact and Contains if querying by name.

        :return: The name_search_type of this GetRulesQuery.
        :rtype: str
        """
        return self._name_search_type

    @name_search_type.setter
    def name_search_type(self, name_search_type: str) -> None:
        """
        Sets the name_search_type of this GetRulesQuery.
        Specifies how strict the name search needs to be. Expected values are Exact and Contains if querying by name.

        :param name_search_type: The name_search_type of this GetRulesQuery.
        :type: str
        """
        if isinstance(name_search_type, int):
            name_search_type = str(name_search_type)
        allowed_values = ["Exact", "Contains", "Unknown"]
        if name_search_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for name_search_type -> " + name_search_type)
            self._name_search_type = "outdated_sdk_version"
        else:
            self._name_search_type = name_search_type

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

