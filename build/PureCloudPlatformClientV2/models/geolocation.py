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
    from . import LocationDefinition

class Geolocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Geolocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'primary': 'bool',
            'latitude': 'float',
            'longitude': 'float',
            'country': 'str',
            'region': 'str',
            'city': 'str',
            'locations': 'list[LocationDefinition]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'primary': 'primary',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'country': 'country',
            'region': 'region',
            'city': 'city',
            'locations': 'locations',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._type = None
        self._primary = None
        self._latitude = None
        self._longitude = None
        self._country = None
        self._region = None
        self._city = None
        self._locations = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Geolocation.
        The globally unique identifier for the object.

        :return: The id of this Geolocation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Geolocation.
        The globally unique identifier for the object.

        :param id: The id of this Geolocation.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Geolocation.


        :return: The name of this Geolocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Geolocation.


        :param name: The name of this Geolocation.
        :type: str
        """
        

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this Geolocation.
        A string used to describe the type of client the geolocation is being updated from e.g. ios, android, web, etc.

        :return: The type of this Geolocation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Geolocation.
        A string used to describe the type of client the geolocation is being updated from e.g. ios, android, web, etc.

        :param type: The type of this Geolocation.
        :type: str
        """
        

        self._type = type

    @property
    def primary(self) -> bool:
        """
        Gets the primary of this Geolocation.
        A boolean used to tell whether or not to set this geolocation client as the primary on a PATCH

        :return: The primary of this Geolocation.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary: bool) -> None:
        """
        Sets the primary of this Geolocation.
        A boolean used to tell whether or not to set this geolocation client as the primary on a PATCH

        :param primary: The primary of this Geolocation.
        :type: bool
        """
        

        self._primary = primary

    @property
    def latitude(self) -> float:
        """
        Gets the latitude of this Geolocation.


        :return: The latitude of this Geolocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        """
        Sets the latitude of this Geolocation.


        :param latitude: The latitude of this Geolocation.
        :type: float
        """
        

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """
        Gets the longitude of this Geolocation.


        :return: The longitude of this Geolocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        """
        Sets the longitude of this Geolocation.


        :param longitude: The longitude of this Geolocation.
        :type: float
        """
        

        self._longitude = longitude

    @property
    def country(self) -> str:
        """
        Gets the country of this Geolocation.


        :return: The country of this Geolocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str) -> None:
        """
        Sets the country of this Geolocation.


        :param country: The country of this Geolocation.
        :type: str
        """
        

        self._country = country

    @property
    def region(self) -> str:
        """
        Gets the region of this Geolocation.


        :return: The region of this Geolocation.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region: str) -> None:
        """
        Sets the region of this Geolocation.


        :param region: The region of this Geolocation.
        :type: str
        """
        

        self._region = region

    @property
    def city(self) -> str:
        """
        Gets the city of this Geolocation.


        :return: The city of this Geolocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str) -> None:
        """
        Sets the city of this Geolocation.


        :param city: The city of this Geolocation.
        :type: str
        """
        

        self._city = city

    @property
    def locations(self) -> List['LocationDefinition']:
        """
        Gets the locations of this Geolocation.


        :return: The locations of this Geolocation.
        :rtype: list[LocationDefinition]
        """
        return self._locations

    @locations.setter
    def locations(self, locations: List['LocationDefinition']) -> None:
        """
        Sets the locations of this Geolocation.


        :param locations: The locations of this Geolocation.
        :type: list[LocationDefinition]
        """
        

        self._locations = locations

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Geolocation.
        The URI for this object

        :return: The self_uri of this Geolocation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Geolocation.
        The URI for this object

        :param self_uri: The self_uri of this Geolocation.
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

