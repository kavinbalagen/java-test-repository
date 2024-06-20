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
    from . import LexV2Slot

class LexV2Intent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LexV2Intent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'intent_name': 'str',
            'description': 'str',
            'slots': 'dict(str, LexV2Slot)',
            'intent_id': 'str'
        }

        self.attribute_map = {
            'intent_name': 'intentName',
            'description': 'description',
            'slots': 'slots',
            'intent_id': 'intentId'
        }

        self._intent_name = None
        self._description = None
        self._slots = None
        self._intent_id = None

    @property
    def intent_name(self) -> str:
        """
        Gets the intent_name of this LexV2Intent.
        The intent name

        :return: The intent_name of this LexV2Intent.
        :rtype: str
        """
        return self._intent_name

    @intent_name.setter
    def intent_name(self, intent_name: str) -> None:
        """
        Sets the intent_name of this LexV2Intent.
        The intent name

        :param intent_name: The intent_name of this LexV2Intent.
        :type: str
        """
        

        self._intent_name = intent_name

    @property
    def description(self) -> str:
        """
        Gets the description of this LexV2Intent.
        A description of the intent

        :return: The description of this LexV2Intent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this LexV2Intent.
        A description of the intent

        :param description: The description of this LexV2Intent.
        :type: str
        """
        

        self._description = description

    @property
    def slots(self) -> Dict[str, 'LexV2Slot']:
        """
        Gets the slots of this LexV2Intent.
        An object mapping slot names to Slot objects

        :return: The slots of this LexV2Intent.
        :rtype: dict(str, LexV2Slot)
        """
        return self._slots

    @slots.setter
    def slots(self, slots: Dict[str, 'LexV2Slot']) -> None:
        """
        Sets the slots of this LexV2Intent.
        An object mapping slot names to Slot objects

        :param slots: The slots of this LexV2Intent.
        :type: dict(str, LexV2Slot)
        """
        

        self._slots = slots

    @property
    def intent_id(self) -> str:
        """
        Gets the intent_id of this LexV2Intent.
        The intent id

        :return: The intent_id of this LexV2Intent.
        :rtype: str
        """
        return self._intent_id

    @intent_id.setter
    def intent_id(self, intent_id: str) -> None:
        """
        Sets the intent_id of this LexV2Intent.
        The intent id

        :param intent_id: The intent_id of this LexV2Intent.
        :type: str
        """
        

        self._intent_id = intent_id

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

