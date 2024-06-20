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
    from . import ApiUsageRow
    from . import Cursors

class ApiUsageQueryResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ApiUsageQueryResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'results': 'list[ApiUsageRow]',
            'query_status': 'str',
            'cursors': 'Cursors'
        }

        self.attribute_map = {
            'results': 'results',
            'query_status': 'queryStatus',
            'cursors': 'cursors'
        }

        self._results = None
        self._query_status = None
        self._cursors = None

    @property
    def results(self) -> List['ApiUsageRow']:
        """
        Gets the results of this ApiUsageQueryResult.
        Query results

        :return: The results of this ApiUsageQueryResult.
        :rtype: list[ApiUsageRow]
        """
        return self._results

    @results.setter
    def results(self, results: List['ApiUsageRow']) -> None:
        """
        Sets the results of this ApiUsageQueryResult.
        Query results

        :param results: The results of this ApiUsageQueryResult.
        :type: list[ApiUsageRow]
        """
        

        self._results = results

    @property
    def query_status(self) -> str:
        """
        Gets the query_status of this ApiUsageQueryResult.
        Query status

        :return: The query_status of this ApiUsageQueryResult.
        :rtype: str
        """
        return self._query_status

    @query_status.setter
    def query_status(self, query_status: str) -> None:
        """
        Sets the query_status of this ApiUsageQueryResult.
        Query status

        :param query_status: The query_status of this ApiUsageQueryResult.
        :type: str
        """
        if isinstance(query_status, int):
            query_status = str(query_status)
        allowed_values = ["Complete", "Failed", "Running"]
        if query_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_status -> " + query_status)
            self._query_status = "outdated_sdk_version"
        else:
            self._query_status = query_status

    @property
    def cursors(self) -> 'Cursors':
        """
        Gets the cursors of this ApiUsageQueryResult.
        Cursor tokens to be used for navigating paginated results

        :return: The cursors of this ApiUsageQueryResult.
        :rtype: Cursors
        """
        return self._cursors

    @cursors.setter
    def cursors(self, cursors: 'Cursors') -> None:
        """
        Sets the cursors of this ApiUsageQueryResult.
        Cursor tokens to be used for navigating paginated results

        :param cursors: The cursors of this ApiUsageQueryResult.
        :type: Cursors
        """
        

        self._cursors = cursors

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

