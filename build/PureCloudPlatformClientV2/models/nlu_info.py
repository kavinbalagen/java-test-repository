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
    from . import Intent
    from . import NluDomainVersion

class NluInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        NluInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'domain': 'AddressableEntityRef',
            'version': 'NluDomainVersion',
            'intents': 'list[Intent]',
            'engine_version': 'str',
            'nlu_data': 'NluDomainVersion'
        }

        self.attribute_map = {
            'domain': 'domain',
            'version': 'version',
            'intents': 'intents',
            'engine_version': 'engineVersion',
            'nlu_data': 'nluData'
        }

        self._domain = None
        self._version = None
        self._intents = None
        self._engine_version = None
        self._nlu_data = None

    @property
    def domain(self) -> 'AddressableEntityRef':
        """
        Gets the domain of this NluInfo.


        :return: The domain of this NluInfo.
        :rtype: AddressableEntityRef
        """
        return self._domain

    @domain.setter
    def domain(self, domain: 'AddressableEntityRef') -> None:
        """
        Sets the domain of this NluInfo.


        :param domain: The domain of this NluInfo.
        :type: AddressableEntityRef
        """
        

        self._domain = domain

    @property
    def version(self) -> 'NluDomainVersion':
        """
        Gets the version of this NluInfo.


        :return: The version of this NluInfo.
        :rtype: NluDomainVersion
        """
        return self._version

    @version.setter
    def version(self, version: 'NluDomainVersion') -> None:
        """
        Sets the version of this NluInfo.


        :param version: The version of this NluInfo.
        :type: NluDomainVersion
        """
        

        self._version = version

    @property
    def intents(self) -> List['Intent']:
        """
        Gets the intents of this NluInfo.


        :return: The intents of this NluInfo.
        :rtype: list[Intent]
        """
        return self._intents

    @intents.setter
    def intents(self, intents: List['Intent']) -> None:
        """
        Sets the intents of this NluInfo.


        :param intents: The intents of this NluInfo.
        :type: list[Intent]
        """
        

        self._intents = intents

    @property
    def engine_version(self) -> str:
        """
        Gets the engine_version of this NluInfo.


        :return: The engine_version of this NluInfo.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version: str) -> None:
        """
        Sets the engine_version of this NluInfo.


        :param engine_version: The engine_version of this NluInfo.
        :type: str
        """
        

        self._engine_version = engine_version

    @property
    def nlu_data(self) -> 'NluDomainVersion':
        """
        Gets the nlu_data of this NluInfo.


        :return: The nlu_data of this NluInfo.
        :rtype: NluDomainVersion
        """
        return self._nlu_data

    @nlu_data.setter
    def nlu_data(self, nlu_data: 'NluDomainVersion') -> None:
        """
        Sets the nlu_data of this NluInfo.


        :param nlu_data: The nlu_data of this NluInfo.
        :type: NluDomainVersion
        """
        

        self._nlu_data = nlu_data

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

