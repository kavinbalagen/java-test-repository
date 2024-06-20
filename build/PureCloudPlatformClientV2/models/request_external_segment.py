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


class RequestExternalSegment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        RequestExternalSegment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'source': 'source'
        }

        self._id = None
        self._name = None
        self._source = None

    @property
    def id(self) -> str:
        """
        Gets the id of this RequestExternalSegment.
        Identifier for the external segment in the system where it originates from.

        :return: The id of this RequestExternalSegment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this RequestExternalSegment.
        Identifier for the external segment in the system where it originates from.

        :param id: The id of this RequestExternalSegment.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this RequestExternalSegment.
        Name for the external segment in the system where it originates from.

        :return: The name of this RequestExternalSegment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this RequestExternalSegment.
        Name for the external segment in the system where it originates from.

        :param name: The name of this RequestExternalSegment.
        :type: str
        """
        

        self._name = name

    @property
    def source(self) -> str:
        """
        Gets the source of this RequestExternalSegment.
        The external system where the segment originates from.

        :return: The source of this RequestExternalSegment.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        """
        Sets the source of this RequestExternalSegment.
        The external system where the segment originates from.

        :param source: The source of this RequestExternalSegment.
        :type: str
        """
        if isinstance(source, int):
            source = str(source)
        allowed_values = ["AdobeExperiencePlatform", "Custom"]
        if source.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for source -> " + source)
            self._source = "outdated_sdk_version"
        else:
            self._source = source

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

