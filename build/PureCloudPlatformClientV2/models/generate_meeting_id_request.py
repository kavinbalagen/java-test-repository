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


class GenerateMeetingIdRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        GenerateMeetingIdRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'conference_id': 'str',
            'ephemeral': 'bool',
            'expire_time_days': 'int'
        }

        self.attribute_map = {
            'conference_id': 'conferenceId',
            'ephemeral': 'ephemeral',
            'expire_time_days': 'expireTimeDays'
        }

        self._conference_id = None
        self._ephemeral = None
        self._expire_time_days = None

    @property
    def conference_id(self) -> str:
        """
        Gets the conference_id of this GenerateMeetingIdRequest.
        The conferenceId for which to generate a meetingId

        :return: The conference_id of this GenerateMeetingIdRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id: str) -> None:
        """
        Sets the conference_id of this GenerateMeetingIdRequest.
        The conferenceId for which to generate a meetingId

        :param conference_id: The conference_id of this GenerateMeetingIdRequest.
        :type: str
        """
        

        self._conference_id = conference_id

    @property
    def ephemeral(self) -> bool:
        """
        Gets the ephemeral of this GenerateMeetingIdRequest.
        Boolean flag for ephemeral status of the created record

        :return: The ephemeral of this GenerateMeetingIdRequest.
        :rtype: bool
        """
        return self._ephemeral

    @ephemeral.setter
    def ephemeral(self, ephemeral: bool) -> None:
        """
        Sets the ephemeral of this GenerateMeetingIdRequest.
        Boolean flag for ephemeral status of the created record

        :param ephemeral: The ephemeral of this GenerateMeetingIdRequest.
        :type: bool
        """
        

        self._ephemeral = ephemeral

    @property
    def expire_time_days(self) -> int:
        """
        Gets the expire_time_days of this GenerateMeetingIdRequest.
        Number of days the meetingId record will remain active

        :return: The expire_time_days of this GenerateMeetingIdRequest.
        :rtype: int
        """
        return self._expire_time_days

    @expire_time_days.setter
    def expire_time_days(self, expire_time_days: int) -> None:
        """
        Sets the expire_time_days of this GenerateMeetingIdRequest.
        Number of days the meetingId record will remain active

        :param expire_time_days: The expire_time_days of this GenerateMeetingIdRequest.
        :type: int
        """
        

        self._expire_time_days = expire_time_days

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

