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


class Device(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Device - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'type': 'str',
            'is_mobile': 'bool',
            'screen_height': 'int',
            'screen_width': 'int',
            'screen_density': 'int',
            'fingerprint': 'str',
            'os_family': 'str',
            'os_version': 'str',
            'manufacturer': 'str'
        }

        self.attribute_map = {
            'category': 'category',
            'type': 'type',
            'is_mobile': 'isMobile',
            'screen_height': 'screenHeight',
            'screen_width': 'screenWidth',
            'screen_density': 'screenDensity',
            'fingerprint': 'fingerprint',
            'os_family': 'osFamily',
            'os_version': 'osVersion',
            'manufacturer': 'manufacturer'
        }

        self._category = None
        self._type = None
        self._is_mobile = None
        self._screen_height = None
        self._screen_width = None
        self._screen_density = None
        self._fingerprint = None
        self._os_family = None
        self._os_version = None
        self._manufacturer = None

    @property
    def category(self) -> str:
        """
        Gets the category of this Device.
        Device category.

        :return: The category of this Device.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Sets the category of this Device.
        Device category.

        :param category: The category of this Device.
        :type: str
        """
        if isinstance(category, int):
            category = str(category)
        allowed_values = ["desktop", "mobile", "tablet", "other"]
        if category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for category -> " + category)
            self._category = "outdated_sdk_version"
        else:
            self._category = category

    @property
    def type(self) -> str:
        """
        Gets the type of this Device.
        Device type (e.g. iPad, iPhone, Other).

        :return: The type of this Device.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this Device.
        Device type (e.g. iPad, iPhone, Other).

        :param type: The type of this Device.
        :type: str
        """
        

        self._type = type

    @property
    def is_mobile(self) -> bool:
        """
        Gets the is_mobile of this Device.
        Flag that is true for mobile devices.

        :return: The is_mobile of this Device.
        :rtype: bool
        """
        return self._is_mobile

    @is_mobile.setter
    def is_mobile(self, is_mobile: bool) -> None:
        """
        Sets the is_mobile of this Device.
        Flag that is true for mobile devices.

        :param is_mobile: The is_mobile of this Device.
        :type: bool
        """
        

        self._is_mobile = is_mobile

    @property
    def screen_height(self) -> int:
        """
        Gets the screen_height of this Device.
        Device's screen height.

        :return: The screen_height of this Device.
        :rtype: int
        """
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height: int) -> None:
        """
        Sets the screen_height of this Device.
        Device's screen height.

        :param screen_height: The screen_height of this Device.
        :type: int
        """
        

        self._screen_height = screen_height

    @property
    def screen_width(self) -> int:
        """
        Gets the screen_width of this Device.
        Device's screen width.

        :return: The screen_width of this Device.
        :rtype: int
        """
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width: int) -> None:
        """
        Sets the screen_width of this Device.
        Device's screen width.

        :param screen_width: The screen_width of this Device.
        :type: int
        """
        

        self._screen_width = screen_width

    @property
    def screen_density(self) -> int:
        """
        Gets the screen_density of this Device.
        Device's screen density, measured as a scale factor where a value of 1 represents a baseline 1:1 ratio of pixels to logical (device-independent) pixels.

        :return: The screen_density of this Device.
        :rtype: int
        """
        return self._screen_density

    @screen_density.setter
    def screen_density(self, screen_density: int) -> None:
        """
        Sets the screen_density of this Device.
        Device's screen density, measured as a scale factor where a value of 1 represents a baseline 1:1 ratio of pixels to logical (device-independent) pixels.

        :param screen_density: The screen_density of this Device.
        :type: int
        """
        

        self._screen_density = screen_density

    @property
    def fingerprint(self) -> str:
        """
        Gets the fingerprint of this Device.
        Fingerprint generated by looking at the individual device features.

        :return: The fingerprint of this Device.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint: str) -> None:
        """
        Sets the fingerprint of this Device.
        Fingerprint generated by looking at the individual device features.

        :param fingerprint: The fingerprint of this Device.
        :type: str
        """
        

        self._fingerprint = fingerprint

    @property
    def os_family(self) -> str:
        """
        Gets the os_family of this Device.
        Operating system family.

        :return: The os_family of this Device.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family: str) -> None:
        """
        Sets the os_family of this Device.
        Operating system family.

        :param os_family: The os_family of this Device.
        :type: str
        """
        

        self._os_family = os_family

    @property
    def os_version(self) -> str:
        """
        Gets the os_version of this Device.
        Operating system version.

        :return: The os_version of this Device.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version: str) -> None:
        """
        Sets the os_version of this Device.
        Operating system version.

        :param os_version: The os_version of this Device.
        :type: str
        """
        

        self._os_version = os_version

    @property
    def manufacturer(self) -> str:
        """
        Gets the manufacturer of this Device.
        Manufacturer of the device.

        :return: The manufacturer of this Device.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str) -> None:
        """
        Sets the manufacturer of this Device.
        Manufacturer of the device.

        :param manufacturer: The manufacturer of this Device.
        :type: str
        """
        

        self._manufacturer = manufacturer

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

