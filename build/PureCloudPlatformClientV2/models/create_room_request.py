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


class CreateRoomRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreateRoomRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'subject': 'str',
            'user_ids': 'list[str]'
        }

        self.attribute_map = {
            'description': 'description',
            'subject': 'subject',
            'user_ids': 'userIds'
        }

        self._description = None
        self._subject = None
        self._user_ids = None

    @property
    def description(self) -> str:
        """
        Gets the description of this CreateRoomRequest.
        Room's description

        :return: The description of this CreateRoomRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this CreateRoomRequest.
        Room's description

        :param description: The description of this CreateRoomRequest.
        :type: str
        """
        

        self._description = description

    @property
    def subject(self) -> str:
        """
        Gets the subject of this CreateRoomRequest.
        Room's subject

        :return: The subject of this CreateRoomRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this CreateRoomRequest.
        Room's subject

        :param subject: The subject of this CreateRoomRequest.
        :type: str
        """
        

        self._subject = subject

    @property
    def user_ids(self) -> List[str]:
        """
        Gets the user_ids of this CreateRoomRequest.
        Users to add to the room

        :return: The user_ids of this CreateRoomRequest.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids: List[str]) -> None:
        """
        Sets the user_ids of this CreateRoomRequest.
        Users to add to the room

        :param user_ids: The user_ids of this CreateRoomRequest.
        :type: list[str]
        """
        

        self._user_ids = user_ids

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

