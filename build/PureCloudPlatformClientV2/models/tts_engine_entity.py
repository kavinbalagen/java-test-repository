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
    from . import TtsVoiceEntity

class TtsEngineEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TtsEngineEntity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'languages': 'list[str]',
            'output_formats': 'list[str]',
            'voices': 'list[TtsVoiceEntity]',
            'is_default': 'bool',
            'is_secure': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'languages': 'languages',
            'output_formats': 'outputFormats',
            'voices': 'voices',
            'is_default': 'isDefault',
            'is_secure': 'isSecure',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._languages = None
        self._output_formats = None
        self._voices = None
        self._is_default = None
        self._is_secure = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this TtsEngineEntity.
        The globally unique identifier for the object.

        :return: The id of this TtsEngineEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this TtsEngineEntity.
        The globally unique identifier for the object.

        :param id: The id of this TtsEngineEntity.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this TtsEngineEntity.


        :return: The name of this TtsEngineEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this TtsEngineEntity.


        :param name: The name of this TtsEngineEntity.
        :type: str
        """
        

        self._name = name

    @property
    def languages(self) -> List[str]:
        """
        Gets the languages of this TtsEngineEntity.
        The set of languages the TTS engine supports

        :return: The languages of this TtsEngineEntity.
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages: List[str]) -> None:
        """
        Sets the languages of this TtsEngineEntity.
        The set of languages the TTS engine supports

        :param languages: The languages of this TtsEngineEntity.
        :type: list[str]
        """
        

        self._languages = languages

    @property
    def output_formats(self) -> List[str]:
        """
        Gets the output_formats of this TtsEngineEntity.
        The set of output formats the TTS engine can produce

        :return: The output_formats of this TtsEngineEntity.
        :rtype: list[str]
        """
        return self._output_formats

    @output_formats.setter
    def output_formats(self, output_formats: List[str]) -> None:
        """
        Sets the output_formats of this TtsEngineEntity.
        The set of output formats the TTS engine can produce

        :param output_formats: The output_formats of this TtsEngineEntity.
        :type: list[str]
        """
        

        self._output_formats = output_formats

    @property
    def voices(self) -> List['TtsVoiceEntity']:
        """
        Gets the voices of this TtsEngineEntity.
        The set of voices the TTS engine supports

        :return: The voices of this TtsEngineEntity.
        :rtype: list[TtsVoiceEntity]
        """
        return self._voices

    @voices.setter
    def voices(self, voices: List['TtsVoiceEntity']) -> None:
        """
        Sets the voices of this TtsEngineEntity.
        The set of voices the TTS engine supports

        :param voices: The voices of this TtsEngineEntity.
        :type: list[TtsVoiceEntity]
        """
        

        self._voices = voices

    @property
    def is_default(self) -> bool:
        """
        Gets the is_default of this TtsEngineEntity.
        The TTS engine is the global default engine

        :return: The is_default of this TtsEngineEntity.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default: bool) -> None:
        """
        Sets the is_default of this TtsEngineEntity.
        The TTS engine is the global default engine

        :param is_default: The is_default of this TtsEngineEntity.
        :type: bool
        """
        

        self._is_default = is_default

    @property
    def is_secure(self) -> bool:
        """
        Gets the is_secure of this TtsEngineEntity.
        The TTS engine can be used in a secure call flow

        :return: The is_secure of this TtsEngineEntity.
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure: bool) -> None:
        """
        Sets the is_secure of this TtsEngineEntity.
        The TTS engine can be used in a secure call flow

        :param is_secure: The is_secure of this TtsEngineEntity.
        :type: bool
        """
        

        self._is_secure = is_secure

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this TtsEngineEntity.
        The URI for this object

        :return: The self_uri of this TtsEngineEntity.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this TtsEngineEntity.
        The URI for this object

        :param self_uri: The self_uri of this TtsEngineEntity.
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
