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
    from . import TtsEngineEntity

class TtsVoiceEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TtsVoiceEntity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'gender': 'str',
            'language': 'str',
            'engine': 'TtsEngineEntity',
            'is_default': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'gender': 'gender',
            'language': 'language',
            'engine': 'engine',
            'is_default': 'isDefault',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._gender = None
        self._language = None
        self._engine = None
        self._is_default = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this TtsVoiceEntity.
        The globally unique identifier for the object.

        :return: The id of this TtsVoiceEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this TtsVoiceEntity.
        The globally unique identifier for the object.

        :param id: The id of this TtsVoiceEntity.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this TtsVoiceEntity.


        :return: The name of this TtsVoiceEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this TtsVoiceEntity.


        :param name: The name of this TtsVoiceEntity.
        :type: str
        """
        

        self._name = name

    @property
    def gender(self) -> str:
        """
        Gets the gender of this TtsVoiceEntity.
        The gender of the TTS voice

        :return: The gender of this TtsVoiceEntity.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str) -> None:
        """
        Sets the gender of this TtsVoiceEntity.
        The gender of the TTS voice

        :param gender: The gender of this TtsVoiceEntity.
        :type: str
        """
        

        self._gender = gender

    @property
    def language(self) -> str:
        """
        Gets the language of this TtsVoiceEntity.
        The language supported by the TTS voice

        :return: The language of this TtsVoiceEntity.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this TtsVoiceEntity.
        The language supported by the TTS voice

        :param language: The language of this TtsVoiceEntity.
        :type: str
        """
        

        self._language = language

    @property
    def engine(self) -> 'TtsEngineEntity':
        """
        Gets the engine of this TtsVoiceEntity.
        Ths TTS engine this voice belongs to

        :return: The engine of this TtsVoiceEntity.
        :rtype: TtsEngineEntity
        """
        return self._engine

    @engine.setter
    def engine(self, engine: 'TtsEngineEntity') -> None:
        """
        Sets the engine of this TtsVoiceEntity.
        Ths TTS engine this voice belongs to

        :param engine: The engine of this TtsVoiceEntity.
        :type: TtsEngineEntity
        """
        

        self._engine = engine

    @property
    def is_default(self) -> bool:
        """
        Gets the is_default of this TtsVoiceEntity.
        The voice is the default voice for its language

        :return: The is_default of this TtsVoiceEntity.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default: bool) -> None:
        """
        Sets the is_default of this TtsVoiceEntity.
        The voice is the default voice for its language

        :param is_default: The is_default of this TtsVoiceEntity.
        :type: bool
        """
        

        self._is_default = is_default

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this TtsVoiceEntity.
        The URI for this object

        :return: The self_uri of this TtsVoiceEntity.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this TtsVoiceEntity.
        The URI for this object

        :param self_uri: The self_uri of this TtsVoiceEntity.
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

