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
    from . import FlowHealthIntentInfo
    from . import FlowHealthVersionInfo
    from . import LocaleInfo

class FlowHealth(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowHealth - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flow_version_info': 'FlowHealthVersionInfo',
            'language_info': 'dict(str, LocaleInfo)',
            'intents': 'list[FlowHealthIntentInfo]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'flow_version_info': 'flowVersionInfo',
            'language_info': 'languageInfo',
            'intents': 'intents',
            'self_uri': 'selfUri'
        }

        self._flow_version_info = None
        self._language_info = None
        self._intents = None
        self._self_uri = None

    @property
    def flow_version_info(self) -> 'FlowHealthVersionInfo':
        """
        Gets the flow_version_info of this FlowHealth.
        Info about given flow version.

        :return: The flow_version_info of this FlowHealth.
        :rtype: FlowHealthVersionInfo
        """
        return self._flow_version_info

    @flow_version_info.setter
    def flow_version_info(self, flow_version_info: 'FlowHealthVersionInfo') -> None:
        """
        Sets the flow_version_info of this FlowHealth.
        Info about given flow version.

        :param flow_version_info: The flow_version_info of this FlowHealth.
        :type: FlowHealthVersionInfo
        """
        

        self._flow_version_info = flow_version_info

    @property
    def language_info(self) -> Dict[str, 'LocaleInfo']:
        """
        Gets the language_info of this FlowHealth.
        Each language's status about its health computation.

        :return: The language_info of this FlowHealth.
        :rtype: dict(str, LocaleInfo)
        """
        return self._language_info

    @language_info.setter
    def language_info(self, language_info: Dict[str, 'LocaleInfo']) -> None:
        """
        Sets the language_info of this FlowHealth.
        Each language's status about its health computation.

        :param language_info: The language_info of this FlowHealth.
        :type: dict(str, LocaleInfo)
        """
        

        self._language_info = language_info

    @property
    def intents(self) -> List['FlowHealthIntentInfo']:
        """
        Gets the intents of this FlowHealth.
        Health metrics information for the intents.

        :return: The intents of this FlowHealth.
        :rtype: list[FlowHealthIntentInfo]
        """
        return self._intents

    @intents.setter
    def intents(self, intents: List['FlowHealthIntentInfo']) -> None:
        """
        Sets the intents of this FlowHealth.
        Health metrics information for the intents.

        :param intents: The intents of this FlowHealth.
        :type: list[FlowHealthIntentInfo]
        """
        

        self._intents = intents

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this FlowHealth.
        The URI for this object

        :return: The self_uri of this FlowHealth.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this FlowHealth.
        The URI for this object

        :param self_uri: The self_uri of this FlowHealth.
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

