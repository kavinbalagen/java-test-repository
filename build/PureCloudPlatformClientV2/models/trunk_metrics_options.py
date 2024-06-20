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
    from . import TrunkErrorInfo

class TrunkMetricsOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrunkMetricsOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'proxy_address': 'str',
            'option_state': 'bool',
            'option_state_time': 'datetime',
            'error_info': 'TrunkErrorInfo'
        }

        self.attribute_map = {
            'proxy_address': 'proxyAddress',
            'option_state': 'optionState',
            'option_state_time': 'optionStateTime',
            'error_info': 'errorInfo'
        }

        self._proxy_address = None
        self._option_state = None
        self._option_state_time = None
        self._error_info = None

    @property
    def proxy_address(self) -> str:
        """
        Gets the proxy_address of this TrunkMetricsOptions.
        Server proxy address that this options array element represents.

        :return: The proxy_address of this TrunkMetricsOptions.
        :rtype: str
        """
        return self._proxy_address

    @proxy_address.setter
    def proxy_address(self, proxy_address: str) -> None:
        """
        Sets the proxy_address of this TrunkMetricsOptions.
        Server proxy address that this options array element represents.

        :param proxy_address: The proxy_address of this TrunkMetricsOptions.
        :type: str
        """
        

        self._proxy_address = proxy_address

    @property
    def option_state(self) -> bool:
        """
        Gets the option_state of this TrunkMetricsOptions.


        :return: The option_state of this TrunkMetricsOptions.
        :rtype: bool
        """
        return self._option_state

    @option_state.setter
    def option_state(self, option_state: bool) -> None:
        """
        Sets the option_state of this TrunkMetricsOptions.


        :param option_state: The option_state of this TrunkMetricsOptions.
        :type: bool
        """
        

        self._option_state = option_state

    @property
    def option_state_time(self) -> datetime:
        """
        Gets the option_state_time of this TrunkMetricsOptions.
        ISO 8601 format UTC absolute date & time of the last change of the option state.

        :return: The option_state_time of this TrunkMetricsOptions.
        :rtype: datetime
        """
        return self._option_state_time

    @option_state_time.setter
    def option_state_time(self, option_state_time: datetime) -> None:
        """
        Sets the option_state_time of this TrunkMetricsOptions.
        ISO 8601 format UTC absolute date & time of the last change of the option state.

        :param option_state_time: The option_state_time of this TrunkMetricsOptions.
        :type: datetime
        """
        

        self._option_state_time = option_state_time

    @property
    def error_info(self) -> 'TrunkErrorInfo':
        """
        Gets the error_info of this TrunkMetricsOptions.


        :return: The error_info of this TrunkMetricsOptions.
        :rtype: TrunkErrorInfo
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info: 'TrunkErrorInfo') -> None:
        """
        Sets the error_info of this TrunkMetricsOptions.


        :param error_info: The error_info of this TrunkMetricsOptions.
        :type: TrunkErrorInfo
        """
        

        self._error_info = error_info

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
