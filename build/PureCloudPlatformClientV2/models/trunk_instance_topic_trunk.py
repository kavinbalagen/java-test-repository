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
    from . import TrunkInstanceTopicTrunkConnectedStatus
    from . import TrunkInstanceTopicTrunkMetricsNetworkTypeIp
    from . import TrunkInstanceTopicTrunkMetricsOptions
    from . import TrunkInstanceTopicTrunkMetricsRegisters

class TrunkInstanceTopicTrunk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrunkInstanceTopicTrunk - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'connected_status': 'TrunkInstanceTopicTrunkConnectedStatus',
            'options_status': 'list[TrunkInstanceTopicTrunkMetricsOptions]',
            'registers_status': 'list[TrunkInstanceTopicTrunkMetricsRegisters]',
            'ip_status': 'TrunkInstanceTopicTrunkMetricsNetworkTypeIp'
        }

        self.attribute_map = {
            'id': 'id',
            'connected_status': 'connectedStatus',
            'options_status': 'optionsStatus',
            'registers_status': 'registersStatus',
            'ip_status': 'ipStatus'
        }

        self._id = None
        self._connected_status = None
        self._options_status = None
        self._registers_status = None
        self._ip_status = None

    @property
    def id(self) -> str:
        """
        Gets the id of this TrunkInstanceTopicTrunk.


        :return: The id of this TrunkInstanceTopicTrunk.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this TrunkInstanceTopicTrunk.


        :param id: The id of this TrunkInstanceTopicTrunk.
        :type: str
        """
        

        self._id = id

    @property
    def connected_status(self) -> 'TrunkInstanceTopicTrunkConnectedStatus':
        """
        Gets the connected_status of this TrunkInstanceTopicTrunk.


        :return: The connected_status of this TrunkInstanceTopicTrunk.
        :rtype: TrunkInstanceTopicTrunkConnectedStatus
        """
        return self._connected_status

    @connected_status.setter
    def connected_status(self, connected_status: 'TrunkInstanceTopicTrunkConnectedStatus') -> None:
        """
        Sets the connected_status of this TrunkInstanceTopicTrunk.


        :param connected_status: The connected_status of this TrunkInstanceTopicTrunk.
        :type: TrunkInstanceTopicTrunkConnectedStatus
        """
        

        self._connected_status = connected_status

    @property
    def options_status(self) -> List['TrunkInstanceTopicTrunkMetricsOptions']:
        """
        Gets the options_status of this TrunkInstanceTopicTrunk.


        :return: The options_status of this TrunkInstanceTopicTrunk.
        :rtype: list[TrunkInstanceTopicTrunkMetricsOptions]
        """
        return self._options_status

    @options_status.setter
    def options_status(self, options_status: List['TrunkInstanceTopicTrunkMetricsOptions']) -> None:
        """
        Sets the options_status of this TrunkInstanceTopicTrunk.


        :param options_status: The options_status of this TrunkInstanceTopicTrunk.
        :type: list[TrunkInstanceTopicTrunkMetricsOptions]
        """
        

        self._options_status = options_status

    @property
    def registers_status(self) -> List['TrunkInstanceTopicTrunkMetricsRegisters']:
        """
        Gets the registers_status of this TrunkInstanceTopicTrunk.


        :return: The registers_status of this TrunkInstanceTopicTrunk.
        :rtype: list[TrunkInstanceTopicTrunkMetricsRegisters]
        """
        return self._registers_status

    @registers_status.setter
    def registers_status(self, registers_status: List['TrunkInstanceTopicTrunkMetricsRegisters']) -> None:
        """
        Sets the registers_status of this TrunkInstanceTopicTrunk.


        :param registers_status: The registers_status of this TrunkInstanceTopicTrunk.
        :type: list[TrunkInstanceTopicTrunkMetricsRegisters]
        """
        

        self._registers_status = registers_status

    @property
    def ip_status(self) -> 'TrunkInstanceTopicTrunkMetricsNetworkTypeIp':
        """
        Gets the ip_status of this TrunkInstanceTopicTrunk.


        :return: The ip_status of this TrunkInstanceTopicTrunk.
        :rtype: TrunkInstanceTopicTrunkMetricsNetworkTypeIp
        """
        return self._ip_status

    @ip_status.setter
    def ip_status(self, ip_status: 'TrunkInstanceTopicTrunkMetricsNetworkTypeIp') -> None:
        """
        Sets the ip_status of this TrunkInstanceTopicTrunk.


        :param ip_status: The ip_status of this TrunkInstanceTopicTrunk.
        :type: TrunkInstanceTopicTrunkMetricsNetworkTypeIp
        """
        

        self._ip_status = ip_status

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

