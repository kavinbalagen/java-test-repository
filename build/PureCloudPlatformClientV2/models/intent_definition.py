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
    from . import AdditionalLanguagesIntent
    from . import NamedEntityTypeBinding
    from . import NluUtterance

class IntentDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        IntentDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'entity_type_bindings': 'list[NamedEntityTypeBinding]',
            'entity_name_references': 'list[str]',
            'utterances': 'list[NluUtterance]',
            'additional_languages': 'dict(str, AdditionalLanguagesIntent)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'entity_type_bindings': 'entityTypeBindings',
            'entity_name_references': 'entityNameReferences',
            'utterances': 'utterances',
            'additional_languages': 'additionalLanguages'
        }

        self._id = None
        self._name = None
        self._entity_type_bindings = None
        self._entity_name_references = None
        self._utterances = None
        self._additional_languages = None

    @property
    def id(self) -> str:
        """
        Gets the id of this IntentDefinition.
        ID of the intent.

        :return: The id of this IntentDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this IntentDefinition.
        ID of the intent.

        :param id: The id of this IntentDefinition.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this IntentDefinition.
        The name of the intent.

        :return: The name of this IntentDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this IntentDefinition.
        The name of the intent.

        :param name: The name of this IntentDefinition.
        :type: str
        """
        

        self._name = name

    @property
    def entity_type_bindings(self) -> List['NamedEntityTypeBinding']:
        """
        Gets the entity_type_bindings of this IntentDefinition.
        The bindings for the named entity types used in this intent.This field is mutually exclusive with entityNameReferences and entities

        :return: The entity_type_bindings of this IntentDefinition.
        :rtype: list[NamedEntityTypeBinding]
        """
        return self._entity_type_bindings

    @entity_type_bindings.setter
    def entity_type_bindings(self, entity_type_bindings: List['NamedEntityTypeBinding']) -> None:
        """
        Sets the entity_type_bindings of this IntentDefinition.
        The bindings for the named entity types used in this intent.This field is mutually exclusive with entityNameReferences and entities

        :param entity_type_bindings: The entity_type_bindings of this IntentDefinition.
        :type: list[NamedEntityTypeBinding]
        """
        

        self._entity_type_bindings = entity_type_bindings

    @property
    def entity_name_references(self) -> List[str]:
        """
        Gets the entity_name_references of this IntentDefinition.
        The references for the named entity used in this intent.This field is mutually exclusive with entityTypeBindings

        :return: The entity_name_references of this IntentDefinition.
        :rtype: list[str]
        """
        return self._entity_name_references

    @entity_name_references.setter
    def entity_name_references(self, entity_name_references: List[str]) -> None:
        """
        Sets the entity_name_references of this IntentDefinition.
        The references for the named entity used in this intent.This field is mutually exclusive with entityTypeBindings

        :param entity_name_references: The entity_name_references of this IntentDefinition.
        :type: list[str]
        """
        

        self._entity_name_references = entity_name_references

    @property
    def utterances(self) -> List['NluUtterance']:
        """
        Gets the utterances of this IntentDefinition.
        The utterances that act as training phrases for the intent.

        :return: The utterances of this IntentDefinition.
        :rtype: list[NluUtterance]
        """
        return self._utterances

    @utterances.setter
    def utterances(self, utterances: List['NluUtterance']) -> None:
        """
        Sets the utterances of this IntentDefinition.
        The utterances that act as training phrases for the intent.

        :param utterances: The utterances of this IntentDefinition.
        :type: list[NluUtterance]
        """
        

        self._utterances = utterances

    @property
    def additional_languages(self) -> Dict[str, 'AdditionalLanguagesIntent']:
        """
        Gets the additional_languages of this IntentDefinition.
        Additional languages for intents

        :return: The additional_languages of this IntentDefinition.
        :rtype: dict(str, AdditionalLanguagesIntent)
        """
        return self._additional_languages

    @additional_languages.setter
    def additional_languages(self, additional_languages: Dict[str, 'AdditionalLanguagesIntent']) -> None:
        """
        Sets the additional_languages of this IntentDefinition.
        Additional languages for intents

        :param additional_languages: The additional_languages of this IntentDefinition.
        :type: dict(str, AdditionalLanguagesIntent)
        """
        

        self._additional_languages = additional_languages

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
