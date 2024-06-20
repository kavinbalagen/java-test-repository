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
    from . import UserParam

class PolicyErrorMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PolicyErrorMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status_code': 'int',
            'user_message': 'object',
            'user_params_message': 'str',
            'error_code': 'str',
            'correlation_id': 'str',
            'user_params': 'list[UserParam]',
            'insert_date': 'datetime'
        }

        self.attribute_map = {
            'status_code': 'statusCode',
            'user_message': 'userMessage',
            'user_params_message': 'userParamsMessage',
            'error_code': 'errorCode',
            'correlation_id': 'correlationId',
            'user_params': 'userParams',
            'insert_date': 'insertDate'
        }

        self._status_code = None
        self._user_message = None
        self._user_params_message = None
        self._error_code = None
        self._correlation_id = None
        self._user_params = None
        self._insert_date = None

    @property
    def status_code(self) -> int:
        """
        Gets the status_code of this PolicyErrorMessage.


        :return: The status_code of this PolicyErrorMessage.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int) -> None:
        """
        Sets the status_code of this PolicyErrorMessage.


        :param status_code: The status_code of this PolicyErrorMessage.
        :type: int
        """
        

        self._status_code = status_code

    @property
    def user_message(self) -> object:
        """
        Gets the user_message of this PolicyErrorMessage.


        :return: The user_message of this PolicyErrorMessage.
        :rtype: object
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message: object) -> None:
        """
        Sets the user_message of this PolicyErrorMessage.


        :param user_message: The user_message of this PolicyErrorMessage.
        :type: object
        """
        

        self._user_message = user_message

    @property
    def user_params_message(self) -> str:
        """
        Gets the user_params_message of this PolicyErrorMessage.


        :return: The user_params_message of this PolicyErrorMessage.
        :rtype: str
        """
        return self._user_params_message

    @user_params_message.setter
    def user_params_message(self, user_params_message: str) -> None:
        """
        Sets the user_params_message of this PolicyErrorMessage.


        :param user_params_message: The user_params_message of this PolicyErrorMessage.
        :type: str
        """
        

        self._user_params_message = user_params_message

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this PolicyErrorMessage.


        :return: The error_code of this PolicyErrorMessage.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this PolicyErrorMessage.


        :param error_code: The error_code of this PolicyErrorMessage.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def correlation_id(self) -> str:
        """
        Gets the correlation_id of this PolicyErrorMessage.


        :return: The correlation_id of this PolicyErrorMessage.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id: str) -> None:
        """
        Sets the correlation_id of this PolicyErrorMessage.


        :param correlation_id: The correlation_id of this PolicyErrorMessage.
        :type: str
        """
        

        self._correlation_id = correlation_id

    @property
    def user_params(self) -> List['UserParam']:
        """
        Gets the user_params of this PolicyErrorMessage.


        :return: The user_params of this PolicyErrorMessage.
        :rtype: list[UserParam]
        """
        return self._user_params

    @user_params.setter
    def user_params(self, user_params: List['UserParam']) -> None:
        """
        Sets the user_params of this PolicyErrorMessage.


        :param user_params: The user_params of this PolicyErrorMessage.
        :type: list[UserParam]
        """
        

        self._user_params = user_params

    @property
    def insert_date(self) -> datetime:
        """
        Gets the insert_date of this PolicyErrorMessage.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The insert_date of this PolicyErrorMessage.
        :rtype: datetime
        """
        return self._insert_date

    @insert_date.setter
    def insert_date(self, insert_date: datetime) -> None:
        """
        Sets the insert_date of this PolicyErrorMessage.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param insert_date: The insert_date of this PolicyErrorMessage.
        :type: datetime
        """
        

        self._insert_date = insert_date

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

