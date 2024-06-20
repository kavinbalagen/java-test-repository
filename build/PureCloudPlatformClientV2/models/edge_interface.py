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
    from . import DomainEntityRef

class EdgeInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EdgeInterface - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'ip_address': 'str',
            'name': 'str',
            'mac_address': 'str',
            'if_name': 'str',
            'endpoints': 'list[DomainEntityRef]',
            'line_types': 'list[str]',
            'address_family_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'ip_address': 'ipAddress',
            'name': 'name',
            'mac_address': 'macAddress',
            'if_name': 'ifName',
            'endpoints': 'endpoints',
            'line_types': 'lineTypes',
            'address_family_id': 'addressFamilyId'
        }

        self._type = None
        self._ip_address = None
        self._name = None
        self._mac_address = None
        self._if_name = None
        self._endpoints = None
        self._line_types = None
        self._address_family_id = None

    @property
    def type(self) -> str:
        """
        Gets the type of this EdgeInterface.


        :return: The type of this EdgeInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this EdgeInterface.


        :param type: The type of this EdgeInterface.
        :type: str
        """
        

        self._type = type

    @property
    def ip_address(self) -> str:
        """
        Gets the ip_address of this EdgeInterface.


        :return: The ip_address of this EdgeInterface.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str) -> None:
        """
        Sets the ip_address of this EdgeInterface.


        :param ip_address: The ip_address of this EdgeInterface.
        :type: str
        """
        

        self._ip_address = ip_address

    @property
    def name(self) -> str:
        """
        Gets the name of this EdgeInterface.


        :return: The name of this EdgeInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this EdgeInterface.


        :param name: The name of this EdgeInterface.
        :type: str
        """
        

        self._name = name

    @property
    def mac_address(self) -> str:
        """
        Gets the mac_address of this EdgeInterface.


        :return: The mac_address of this EdgeInterface.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address: str) -> None:
        """
        Sets the mac_address of this EdgeInterface.


        :param mac_address: The mac_address of this EdgeInterface.
        :type: str
        """
        

        self._mac_address = mac_address

    @property
    def if_name(self) -> str:
        """
        Gets the if_name of this EdgeInterface.


        :return: The if_name of this EdgeInterface.
        :rtype: str
        """
        return self._if_name

    @if_name.setter
    def if_name(self, if_name: str) -> None:
        """
        Sets the if_name of this EdgeInterface.


        :param if_name: The if_name of this EdgeInterface.
        :type: str
        """
        

        self._if_name = if_name

    @property
    def endpoints(self) -> List['DomainEntityRef']:
        """
        Gets the endpoints of this EdgeInterface.


        :return: The endpoints of this EdgeInterface.
        :rtype: list[DomainEntityRef]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints: List['DomainEntityRef']) -> None:
        """
        Sets the endpoints of this EdgeInterface.


        :param endpoints: The endpoints of this EdgeInterface.
        :type: list[DomainEntityRef]
        """
        

        self._endpoints = endpoints

    @property
    def line_types(self) -> List[str]:
        """
        Gets the line_types of this EdgeInterface.


        :return: The line_types of this EdgeInterface.
        :rtype: list[str]
        """
        return self._line_types

    @line_types.setter
    def line_types(self, line_types: List[str]) -> None:
        """
        Sets the line_types of this EdgeInterface.


        :param line_types: The line_types of this EdgeInterface.
        :type: list[str]
        """
        

        self._line_types = line_types

    @property
    def address_family_id(self) -> str:
        """
        Gets the address_family_id of this EdgeInterface.


        :return: The address_family_id of this EdgeInterface.
        :rtype: str
        """
        return self._address_family_id

    @address_family_id.setter
    def address_family_id(self, address_family_id: str) -> None:
        """
        Sets the address_family_id of this EdgeInterface.


        :param address_family_id: The address_family_id of this EdgeInterface.
        :type: str
        """
        

        self._address_family_id = address_family_id

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

