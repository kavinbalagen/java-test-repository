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


class AvailableMediaType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AvailableMediaType - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'media_type': 'str',
            'available_sub_types': 'list[str]'
        }

        self.attribute_map = {
            'media_type': 'mediaType',
            'available_sub_types': 'availableSubTypes'
        }

        self._media_type = None
        self._available_sub_types = None

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this AvailableMediaType.
        Name of the available media type

        :return: The media_type of this AvailableMediaType.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this AvailableMediaType.
        Name of the available media type

        :param media_type: The media_type of this AvailableMediaType.
        :type: str
        """
        

        self._media_type = media_type

    @property
    def available_sub_types(self) -> List[str]:
        """
        Gets the available_sub_types of this AvailableMediaType.
        List of available subtypes for this media type

        :return: The available_sub_types of this AvailableMediaType.
        :rtype: list[str]
        """
        return self._available_sub_types

    @available_sub_types.setter
    def available_sub_types(self, available_sub_types: List[str]) -> None:
        """
        Sets the available_sub_types of this AvailableMediaType.
        List of available subtypes for this media type

        :param available_sub_types: The available_sub_types of this AvailableMediaType.
        :type: list[str]
        """
        

        self._available_sub_types = available_sub_types

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

