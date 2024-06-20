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


class MinerErrorInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MinerErrorInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'code': 'str',
            'message_with_params': 'str',
            'message_params': 'dict(str, object)'
        }

        self.attribute_map = {
            'message': 'message',
            'code': 'code',
            'message_with_params': 'messageWithParams',
            'message_params': 'messageParams'
        }

        self._message = None
        self._code = None
        self._message_with_params = None
        self._message_params = None

    @property
    def message(self) -> str:
        """
        Gets the message of this MinerErrorInfo.


        :return: The message of this MinerErrorInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """
        Sets the message of this MinerErrorInfo.


        :param message: The message of this MinerErrorInfo.
        :type: str
        """
        

        self._message = message

    @property
    def code(self) -> str:
        """
        Gets the code of this MinerErrorInfo.


        :return: The code of this MinerErrorInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str) -> None:
        """
        Sets the code of this MinerErrorInfo.


        :param code: The code of this MinerErrorInfo.
        :type: str
        """
        

        self._code = code

    @property
    def message_with_params(self) -> str:
        """
        Gets the message_with_params of this MinerErrorInfo.
        Error message with params included.

        :return: The message_with_params of this MinerErrorInfo.
        :rtype: str
        """
        return self._message_with_params

    @message_with_params.setter
    def message_with_params(self, message_with_params: str) -> None:
        """
        Sets the message_with_params of this MinerErrorInfo.
        Error message with params included.

        :param message_with_params: The message_with_params of this MinerErrorInfo.
        :type: str
        """
        

        self._message_with_params = message_with_params

    @property
    def message_params(self) -> Dict[str, object]:
        """
        Gets the message_params of this MinerErrorInfo.
        Map of variables and params for the error message.

        :return: The message_params of this MinerErrorInfo.
        :rtype: dict(str, object)
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params: Dict[str, object]) -> None:
        """
        Sets the message_params of this MinerErrorInfo.
        Map of variables and params for the error message.

        :param message_params: The message_params of this MinerErrorInfo.
        :type: dict(str, object)
        """
        

        self._message_params = message_params

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

