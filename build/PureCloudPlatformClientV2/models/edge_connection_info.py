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
    from . import AddressableEntityRef

class EdgeConnectionInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EdgeConnectionInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'interface_name': 'str',
            'interface_ip_address': 'str',
            'connection_errors': 'list[str]',
            'site': 'AddressableEntityRef',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'interface_name': 'interfaceName',
            'interface_ip_address': 'interfaceIpAddress',
            'connection_errors': 'connectionErrors',
            'site': 'site',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._interface_name = None
        self._interface_ip_address = None
        self._connection_errors = None
        self._site = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this EdgeConnectionInfo.
        The globally unique identifier for the object.

        :return: The id of this EdgeConnectionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this EdgeConnectionInfo.
        The globally unique identifier for the object.

        :param id: The id of this EdgeConnectionInfo.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this EdgeConnectionInfo.


        :return: The name of this EdgeConnectionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this EdgeConnectionInfo.


        :param name: The name of this EdgeConnectionInfo.
        :type: str
        """
        

        self._name = name

    @property
    def interface_name(self) -> str:
        """
        Gets the interface_name of this EdgeConnectionInfo.
        Interface used for the connection on the edge

        :return: The interface_name of this EdgeConnectionInfo.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name: str) -> None:
        """
        Sets the interface_name of this EdgeConnectionInfo.
        Interface used for the connection on the edge

        :param interface_name: The interface_name of this EdgeConnectionInfo.
        :type: str
        """
        

        self._interface_name = interface_name

    @property
    def interface_ip_address(self) -> str:
        """
        Gets the interface_ip_address of this EdgeConnectionInfo.
        IP address of the interface

        :return: The interface_ip_address of this EdgeConnectionInfo.
        :rtype: str
        """
        return self._interface_ip_address

    @interface_ip_address.setter
    def interface_ip_address(self, interface_ip_address: str) -> None:
        """
        Sets the interface_ip_address of this EdgeConnectionInfo.
        IP address of the interface

        :param interface_ip_address: The interface_ip_address of this EdgeConnectionInfo.
        :type: str
        """
        

        self._interface_ip_address = interface_ip_address

    @property
    def connection_errors(self) -> List[str]:
        """
        Gets the connection_errors of this EdgeConnectionInfo.
        Connection errors

        :return: The connection_errors of this EdgeConnectionInfo.
        :rtype: list[str]
        """
        return self._connection_errors

    @connection_errors.setter
    def connection_errors(self, connection_errors: List[str]) -> None:
        """
        Sets the connection_errors of this EdgeConnectionInfo.
        Connection errors

        :param connection_errors: The connection_errors of this EdgeConnectionInfo.
        :type: list[str]
        """
        

        self._connection_errors = connection_errors

    @property
    def site(self) -> 'AddressableEntityRef':
        """
        Gets the site of this EdgeConnectionInfo.


        :return: The site of this EdgeConnectionInfo.
        :rtype: AddressableEntityRef
        """
        return self._site

    @site.setter
    def site(self, site: 'AddressableEntityRef') -> None:
        """
        Sets the site of this EdgeConnectionInfo.


        :param site: The site of this EdgeConnectionInfo.
        :type: AddressableEntityRef
        """
        

        self._site = site

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this EdgeConnectionInfo.
        The URI for this object

        :return: The self_uri of this EdgeConnectionInfo.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this EdgeConnectionInfo.
        The URI for this object

        :param self_uri: The self_uri of this EdgeConnectionInfo.
        :type: str
        """
        

        self._self_uri = self_uri

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

