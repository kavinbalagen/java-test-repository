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
    from . import EngineIntegration

class ProgramTranscriptionEngine(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ProgramTranscriptionEngine - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'engine': 'str',
            'dialects': 'list[str]',
            'engine_integration': 'EngineIntegration'
        }

        self.attribute_map = {
            'engine': 'engine',
            'dialects': 'dialects',
            'engine_integration': 'engineIntegration'
        }

        self._engine = None
        self._dialects = None
        self._engine_integration = None

    @property
    def engine(self) -> str:
        """
        Gets the engine of this ProgramTranscriptionEngine.


        :return: The engine of this ProgramTranscriptionEngine.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine: str) -> None:
        """
        Sets the engine of this ProgramTranscriptionEngine.


        :param engine: The engine of this ProgramTranscriptionEngine.
        :type: str
        """
        if isinstance(engine, int):
            engine = str(engine)
        allowed_values = ["Genesys", "GenesysExtended", "TranscriptionConnector"]
        if engine.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for engine -> " + engine)
            self._engine = "outdated_sdk_version"
        else:
            self._engine = engine

    @property
    def dialects(self) -> List[str]:
        """
        Gets the dialects of this ProgramTranscriptionEngine.


        :return: The dialects of this ProgramTranscriptionEngine.
        :rtype: list[str]
        """
        return self._dialects

    @dialects.setter
    def dialects(self, dialects: List[str]) -> None:
        """
        Sets the dialects of this ProgramTranscriptionEngine.


        :param dialects: The dialects of this ProgramTranscriptionEngine.
        :type: list[str]
        """
        

        self._dialects = dialects

    @property
    def engine_integration(self) -> 'EngineIntegration':
        """
        Gets the engine_integration of this ProgramTranscriptionEngine.


        :return: The engine_integration of this ProgramTranscriptionEngine.
        :rtype: EngineIntegration
        """
        return self._engine_integration

    @engine_integration.setter
    def engine_integration(self, engine_integration: 'EngineIntegration') -> None:
        """
        Sets the engine_integration of this ProgramTranscriptionEngine.


        :param engine_integration: The engine_integration of this ProgramTranscriptionEngine.
        :type: EngineIntegration
        """
        

        self._engine_integration = engine_integration

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

