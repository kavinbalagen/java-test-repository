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
    from . import BuAgentScheduleHistoryChangeMetadata
    from . import BuAgentScheduleHistoryDeletedChange
    from . import BuAgentScheduleShift
    from . import BuFullDayTimeOffMarker

class BuAgentScheduleHistoryChange(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuAgentScheduleHistoryChange - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metadata': 'BuAgentScheduleHistoryChangeMetadata',
            'shifts': 'list[BuAgentScheduleShift]',
            'full_day_time_off_markers': 'list[BuFullDayTimeOffMarker]',
            'deletes': 'BuAgentScheduleHistoryDeletedChange'
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'shifts': 'shifts',
            'full_day_time_off_markers': 'fullDayTimeOffMarkers',
            'deletes': 'deletes'
        }

        self._metadata = None
        self._shifts = None
        self._full_day_time_off_markers = None
        self._deletes = None

    @property
    def metadata(self) -> 'BuAgentScheduleHistoryChangeMetadata':
        """
        Gets the metadata of this BuAgentScheduleHistoryChange.
        The metadata of the change, including who and when the change was made

        :return: The metadata of this BuAgentScheduleHistoryChange.
        :rtype: BuAgentScheduleHistoryChangeMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'BuAgentScheduleHistoryChangeMetadata') -> None:
        """
        Sets the metadata of this BuAgentScheduleHistoryChange.
        The metadata of the change, including who and when the change was made

        :param metadata: The metadata of this BuAgentScheduleHistoryChange.
        :type: BuAgentScheduleHistoryChangeMetadata
        """
        

        self._metadata = metadata

    @property
    def shifts(self) -> List['BuAgentScheduleShift']:
        """
        Gets the shifts of this BuAgentScheduleHistoryChange.
        The list of changed shifts

        :return: The shifts of this BuAgentScheduleHistoryChange.
        :rtype: list[BuAgentScheduleShift]
        """
        return self._shifts

    @shifts.setter
    def shifts(self, shifts: List['BuAgentScheduleShift']) -> None:
        """
        Sets the shifts of this BuAgentScheduleHistoryChange.
        The list of changed shifts

        :param shifts: The shifts of this BuAgentScheduleHistoryChange.
        :type: list[BuAgentScheduleShift]
        """
        

        self._shifts = shifts

    @property
    def full_day_time_off_markers(self) -> List['BuFullDayTimeOffMarker']:
        """
        Gets the full_day_time_off_markers of this BuAgentScheduleHistoryChange.
        The list of changed full day time off markers

        :return: The full_day_time_off_markers of this BuAgentScheduleHistoryChange.
        :rtype: list[BuFullDayTimeOffMarker]
        """
        return self._full_day_time_off_markers

    @full_day_time_off_markers.setter
    def full_day_time_off_markers(self, full_day_time_off_markers: List['BuFullDayTimeOffMarker']) -> None:
        """
        Sets the full_day_time_off_markers of this BuAgentScheduleHistoryChange.
        The list of changed full day time off markers

        :param full_day_time_off_markers: The full_day_time_off_markers of this BuAgentScheduleHistoryChange.
        :type: list[BuFullDayTimeOffMarker]
        """
        

        self._full_day_time_off_markers = full_day_time_off_markers

    @property
    def deletes(self) -> 'BuAgentScheduleHistoryDeletedChange':
        """
        Gets the deletes of this BuAgentScheduleHistoryChange.
        The deleted shifts, full day time off markers, or the entire agent schedule

        :return: The deletes of this BuAgentScheduleHistoryChange.
        :rtype: BuAgentScheduleHistoryDeletedChange
        """
        return self._deletes

    @deletes.setter
    def deletes(self, deletes: 'BuAgentScheduleHistoryDeletedChange') -> None:
        """
        Sets the deletes of this BuAgentScheduleHistoryChange.
        The deleted shifts, full day time off markers, or the entire agent schedule

        :param deletes: The deletes of this BuAgentScheduleHistoryChange.
        :type: BuAgentScheduleHistoryDeletedChange
        """
        

        self._deletes = deletes

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

