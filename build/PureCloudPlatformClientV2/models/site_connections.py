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
    from . import SiteConnection

class SiteConnections(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SiteConnections - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'site_connections': 'list[SiteConnection]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'site_connections': 'siteConnections',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._site_connections = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this SiteConnections.
        The globally unique identifier for the object.

        :return: The id of this SiteConnections.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this SiteConnections.
        The globally unique identifier for the object.

        :param id: The id of this SiteConnections.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this SiteConnections.


        :return: The name of this SiteConnections.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this SiteConnections.


        :param name: The name of this SiteConnections.
        :type: str
        """
        

        self._name = name

    @property
    def site_connections(self) -> List['SiteConnection']:
        """
        Gets the site_connections of this SiteConnections.
        List of site connections

        :return: The site_connections of this SiteConnections.
        :rtype: list[SiteConnection]
        """
        return self._site_connections

    @site_connections.setter
    def site_connections(self, site_connections: List['SiteConnection']) -> None:
        """
        Sets the site_connections of this SiteConnections.
        List of site connections

        :param site_connections: The site_connections of this SiteConnections.
        :type: list[SiteConnection]
        """
        

        self._site_connections = site_connections

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this SiteConnections.
        The URI for this object

        :return: The self_uri of this SiteConnections.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this SiteConnections.
        The URI for this object

        :param self_uri: The self_uri of this SiteConnections.
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

