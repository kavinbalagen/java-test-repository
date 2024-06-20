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


class WfmHistoricalAdherenceBulkItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmHistoricalAdherenceBulkItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'management_unit_id': 'str',
            'start_date': 'datetime',
            'end_date': 'datetime',
            'user_ids': 'list[str]',
            'include_exceptions': 'bool',
            'include_actuals': 'bool'
        }

        self.attribute_map = {
            'management_unit_id': 'managementUnitId',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'user_ids': 'userIds',
            'include_exceptions': 'includeExceptions',
            'include_actuals': 'includeActuals'
        }

        self._management_unit_id = None
        self._start_date = None
        self._end_date = None
        self._user_ids = None
        self._include_exceptions = None
        self._include_actuals = None

    @property
    def management_unit_id(self) -> str:
        """
        Gets the management_unit_id of this WfmHistoricalAdherenceBulkItem.
        The ID of the management unit to query

        :return: The management_unit_id of this WfmHistoricalAdherenceBulkItem.
        :rtype: str
        """
        return self._management_unit_id

    @management_unit_id.setter
    def management_unit_id(self, management_unit_id: str) -> None:
        """
        Sets the management_unit_id of this WfmHistoricalAdherenceBulkItem.
        The ID of the management unit to query

        :param management_unit_id: The management_unit_id of this WfmHistoricalAdherenceBulkItem.
        :type: str
        """
        

        self._management_unit_id = management_unit_id

    @property
    def start_date(self) -> datetime:
        """
        Gets the start_date of this WfmHistoricalAdherenceBulkItem.
        Beginning of the date range to query in ISO-8601 format

        :return: The start_date of this WfmHistoricalAdherenceBulkItem.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: datetime) -> None:
        """
        Sets the start_date of this WfmHistoricalAdherenceBulkItem.
        Beginning of the date range to query in ISO-8601 format

        :param start_date: The start_date of this WfmHistoricalAdherenceBulkItem.
        :type: datetime
        """
        

        self._start_date = start_date

    @property
    def end_date(self) -> datetime:
        """
        Gets the end_date of this WfmHistoricalAdherenceBulkItem.
        End of the date range to query in ISO-8601 format

        :return: The end_date of this WfmHistoricalAdherenceBulkItem.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: datetime) -> None:
        """
        Sets the end_date of this WfmHistoricalAdherenceBulkItem.
        End of the date range to query in ISO-8601 format

        :param end_date: The end_date of this WfmHistoricalAdherenceBulkItem.
        :type: datetime
        """
        

        self._end_date = end_date

    @property
    def user_ids(self) -> List[str]:
        """
        Gets the user_ids of this WfmHistoricalAdherenceBulkItem.
        The IDs of the users to query. If not included, will query every user in the management unit

        :return: The user_ids of this WfmHistoricalAdherenceBulkItem.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids: List[str]) -> None:
        """
        Sets the user_ids of this WfmHistoricalAdherenceBulkItem.
        The IDs of the users to query. If not included, will query every user in the management unit

        :param user_ids: The user_ids of this WfmHistoricalAdherenceBulkItem.
        :type: list[str]
        """
        

        self._user_ids = user_ids

    @property
    def include_exceptions(self) -> bool:
        """
        Gets the include_exceptions of this WfmHistoricalAdherenceBulkItem.
        Whether user exceptions should be returned as part of the results. Defaults to false if not specified.

        :return: The include_exceptions of this WfmHistoricalAdherenceBulkItem.
        :rtype: bool
        """
        return self._include_exceptions

    @include_exceptions.setter
    def include_exceptions(self, include_exceptions: bool) -> None:
        """
        Sets the include_exceptions of this WfmHistoricalAdherenceBulkItem.
        Whether user exceptions should be returned as part of the results. Defaults to false if not specified.

        :param include_exceptions: The include_exceptions of this WfmHistoricalAdherenceBulkItem.
        :type: bool
        """
        

        self._include_exceptions = include_exceptions

    @property
    def include_actuals(self) -> bool:
        """
        Gets the include_actuals of this WfmHistoricalAdherenceBulkItem.
        Whether user actual activities should be returned as part of the results. Defaults to false if not specified.

        :return: The include_actuals of this WfmHistoricalAdherenceBulkItem.
        :rtype: bool
        """
        return self._include_actuals

    @include_actuals.setter
    def include_actuals(self, include_actuals: bool) -> None:
        """
        Sets the include_actuals of this WfmHistoricalAdherenceBulkItem.
        Whether user actual activities should be returned as part of the results. Defaults to false if not specified.

        :param include_actuals: The include_actuals of this WfmHistoricalAdherenceBulkItem.
        :type: bool
        """
        

        self._include_actuals = include_actuals

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

