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


class MessageEvaluation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MessageEvaluation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'contact_column': 'str',
            'contact_address': 'str',
            'message_type': 'str',
            'wrapup_code_id': 'str',
            'timestamp': 'datetime'
        }

        self.attribute_map = {
            'contact_column': 'contactColumn',
            'contact_address': 'contactAddress',
            'message_type': 'messageType',
            'wrapup_code_id': 'wrapupCodeId',
            'timestamp': 'timestamp'
        }

        self._contact_column = None
        self._contact_address = None
        self._message_type = None
        self._wrapup_code_id = None
        self._timestamp = None

    @property
    def contact_column(self) -> str:
        """
        Gets the contact_column of this MessageEvaluation.
        The name of the contact column that was wrapped up

        :return: The contact_column of this MessageEvaluation.
        :rtype: str
        """
        return self._contact_column

    @contact_column.setter
    def contact_column(self, contact_column: str) -> None:
        """
        Sets the contact_column of this MessageEvaluation.
        The name of the contact column that was wrapped up

        :param contact_column: The contact_column of this MessageEvaluation.
        :type: str
        """
        

        self._contact_column = contact_column

    @property
    def contact_address(self) -> str:
        """
        Gets the contact_address of this MessageEvaluation.
        The address (phone or email) that was wrapped up

        :return: The contact_address of this MessageEvaluation.
        :rtype: str
        """
        return self._contact_address

    @contact_address.setter
    def contact_address(self, contact_address: str) -> None:
        """
        Sets the contact_address of this MessageEvaluation.
        The address (phone or email) that was wrapped up

        :param contact_address: The contact_address of this MessageEvaluation.
        :type: str
        """
        

        self._contact_address = contact_address

    @property
    def message_type(self) -> str:
        """
        Gets the message_type of this MessageEvaluation.
        The type of message sent

        :return: The message_type of this MessageEvaluation.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type: str) -> None:
        """
        Sets the message_type of this MessageEvaluation.
        The type of message sent

        :param message_type: The message_type of this MessageEvaluation.
        :type: str
        """
        if isinstance(message_type, int):
            message_type = str(message_type)
        allowed_values = ["Sms", "Email"]
        if message_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for message_type -> " + message_type)
            self._message_type = "outdated_sdk_version"
        else:
            self._message_type = message_type

    @property
    def wrapup_code_id(self) -> str:
        """
        Gets the wrapup_code_id of this MessageEvaluation.
        The id of the wrap-up code

        :return: The wrapup_code_id of this MessageEvaluation.
        :rtype: str
        """
        return self._wrapup_code_id

    @wrapup_code_id.setter
    def wrapup_code_id(self, wrapup_code_id: str) -> None:
        """
        Sets the wrapup_code_id of this MessageEvaluation.
        The id of the wrap-up code

        :param wrapup_code_id: The wrapup_code_id of this MessageEvaluation.
        :type: str
        """
        

        self._wrapup_code_id = wrapup_code_id

    @property
    def timestamp(self) -> datetime:
        """
        Gets the timestamp of this MessageEvaluation.
        The time that the wrap-up was applied. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The timestamp of this MessageEvaluation.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime) -> None:
        """
        Sets the timestamp of this MessageEvaluation.
        The time that the wrap-up was applied. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param timestamp: The timestamp of this MessageEvaluation.
        :type: datetime
        """
        

        self._timestamp = timestamp

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
