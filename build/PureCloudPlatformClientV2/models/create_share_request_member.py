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
    from . import MemberEntity

class CreateShareRequestMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreateShareRequestMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'member_type': 'str',
            'member': 'MemberEntity'
        }

        self.attribute_map = {
            'member_type': 'memberType',
            'member': 'member'
        }

        self._member_type = None
        self._member = None

    @property
    def member_type(self) -> str:
        """
        Gets the member_type of this CreateShareRequestMember.


        :return: The member_type of this CreateShareRequestMember.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type: str) -> None:
        """
        Sets the member_type of this CreateShareRequestMember.


        :param member_type: The member_type of this CreateShareRequestMember.
        :type: str
        """
        if isinstance(member_type, int):
            member_type = str(member_type)
        allowed_values = ["USER", "GROUP", "PUBLIC"]
        if member_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for member_type -> " + member_type)
            self._member_type = "outdated_sdk_version"
        else:
            self._member_type = member_type

    @property
    def member(self) -> 'MemberEntity':
        """
        Gets the member of this CreateShareRequestMember.


        :return: The member of this CreateShareRequestMember.
        :rtype: MemberEntity
        """
        return self._member

    @member.setter
    def member(self, member: 'MemberEntity') -> None:
        """
        Sets the member of this CreateShareRequestMember.


        :param member: The member of this CreateShareRequestMember.
        :type: MemberEntity
        """
        

        self._member = member

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

