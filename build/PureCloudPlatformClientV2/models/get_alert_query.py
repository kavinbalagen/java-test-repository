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


class GetAlertQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GetAlertQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rule_type': 'str',
            'query_type': 'str',
            'alert_status': 'str',
            'viewed_status': 'str',
            'page_number': 'int',
            'page_size': 'int',
            'sort_by': 'str',
            'sort_order': 'str'
        }

        self.attribute_map = {
            'rule_type': 'ruleType',
            'query_type': 'queryType',
            'alert_status': 'alertStatus',
            'viewed_status': 'viewedStatus',
            'page_number': 'pageNumber',
            'page_size': 'pageSize',
            'sort_by': 'sortBy',
            'sort_order': 'sortOrder'
        }

        self._rule_type = None
        self._query_type = None
        self._alert_status = None
        self._viewed_status = None
        self._page_number = None
        self._page_size = None
        self._sort_by = None
        self._sort_order = None

    @property
    def rule_type(self) -> str:
        """
        Gets the rule_type of this GetAlertQuery.
        The rule type of the alerts the query will return

        :return: The rule_type of this GetAlertQuery.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type: str) -> None:
        """
        Sets the rule_type of this GetAlertQuery.
        The rule type of the alerts the query will return

        :param rule_type: The rule_type of this GetAlertQuery.
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
        Gets the query_type of this GetAlertQuery.
        The type of query being performed.

        :return: The query_type of this GetAlertQuery.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type: str) -> None:
        """
        Sets the query_type of this GetAlertQuery.
        The type of query being performed.

        :param query_type: The query_type of this GetAlertQuery.
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
    def alert_status(self) -> str:
        """
        Gets the alert_status of this GetAlertQuery.
        The status of the alerts the query will return.

        :return: The alert_status of this GetAlertQuery.
        :rtype: str
        """
        return self._alert_status

    @alert_status.setter
    def alert_status(self, alert_status: str) -> None:
        """
        Sets the alert_status of this GetAlertQuery.
        The status of the alerts the query will return.

        :param alert_status: The alert_status of this GetAlertQuery.
        :type: str
        """
        if isinstance(alert_status, int):
            alert_status = str(alert_status)
        allowed_values = ["Active", "Inactive", "All"]
        if alert_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for alert_status -> " + alert_status)
            self._alert_status = "outdated_sdk_version"
        else:
            self._alert_status = alert_status

    @property
    def viewed_status(self) -> str:
        """
        Gets the viewed_status of this GetAlertQuery.
        The view status of the alerts the query will return.

        :return: The viewed_status of this GetAlertQuery.
        :rtype: str
        """
        return self._viewed_status

    @viewed_status.setter
    def viewed_status(self, viewed_status: str) -> None:
        """
        Sets the viewed_status of this GetAlertQuery.
        The view status of the alerts the query will return.

        :param viewed_status: The viewed_status of this GetAlertQuery.
        :type: str
        """
        if isinstance(viewed_status, int):
            viewed_status = str(viewed_status)
        allowed_values = ["Unread", "Read", "All"]
        if viewed_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for viewed_status -> " + viewed_status)
            self._viewed_status = "outdated_sdk_version"
        else:
            self._viewed_status = viewed_status

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this GetAlertQuery.
        The page number of the queried response

        :return: The page_number of this GetAlertQuery.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this GetAlertQuery.
        The page number of the queried response

        :param page_number: The page_number of this GetAlertQuery.
        :type: int
        """
        

        self._page_number = page_number

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this GetAlertQuery.
        The number of entities to return of the queried response.  The max is 25

        :return: The page_size of this GetAlertQuery.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this GetAlertQuery.
        The number of entities to return of the queried response.  The max is 25

        :param page_size: The page_size of this GetAlertQuery.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def sort_by(self) -> str:
        """
        Gets the sort_by of this GetAlertQuery.
        The field to sort responses by.  The accepted choices are Name and DateStart

        :return: The sort_by of this GetAlertQuery.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by: str) -> None:
        """
        Sets the sort_by of this GetAlertQuery.
        The field to sort responses by.  The accepted choices are Name and DateStart

        :param sort_by: The sort_by of this GetAlertQuery.
        :type: str
        """
        if isinstance(sort_by, int):
            sort_by = str(sort_by)
        allowed_values = ["Name", "DateStart"]
        if sort_by.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for sort_by -> " + sort_by)
            self._sort_by = "outdated_sdk_version"
        else:
            self._sort_by = sort_by

    @property
    def sort_order(self) -> str:
        """
        Gets the sort_order of this GetAlertQuery.
        The order in which response will be sorted.  The accepted choices are Asc and Desc

        :return: The sort_order of this GetAlertQuery.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order: str) -> None:
        """
        Sets the sort_order of this GetAlertQuery.
        The order in which response will be sorted.  The accepted choices are Asc and Desc

        :param sort_order: The sort_order of this GetAlertQuery.
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

