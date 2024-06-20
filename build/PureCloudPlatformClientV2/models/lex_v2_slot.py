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


class LexV2Slot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LexV2Slot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'slot_name': 'str',
            'description': 'str',
            'slot_id': 'str',
            'type': 'str',
            'slot_type_id': 'str'
        }

        self.attribute_map = {
            'slot_name': 'slotName',
            'description': 'description',
            'slot_id': 'slotId',
            'type': 'type',
            'slot_type_id': 'slotTypeId'
        }

        self._slot_name = None
        self._description = None
        self._slot_id = None
        self._type = None
        self._slot_type_id = None

    @property
    def slot_name(self) -> str:
        """
        Gets the slot_name of this LexV2Slot.
        The slot name

        :return: The slot_name of this LexV2Slot.
        :rtype: str
        """
        return self._slot_name

    @slot_name.setter
    def slot_name(self, slot_name: str) -> None:
        """
        Sets the slot_name of this LexV2Slot.
        The slot name

        :param slot_name: The slot_name of this LexV2Slot.
        :type: str
        """
        

        self._slot_name = slot_name

    @property
    def description(self) -> str:
        """
        Gets the description of this LexV2Slot.
        The slot description

        :return: The description of this LexV2Slot.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this LexV2Slot.
        The slot description

        :param description: The description of this LexV2Slot.
        :type: str
        """
        

        self._description = description

    @property
    def slot_id(self) -> str:
        """
        Gets the slot_id of this LexV2Slot.
        The slot id

        :return: The slot_id of this LexV2Slot.
        :rtype: str
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id: str) -> None:
        """
        Sets the slot_id of this LexV2Slot.
        The slot id

        :param slot_id: The slot_id of this LexV2Slot.
        :type: str
        """
        

        self._slot_id = slot_id

    @property
    def type(self) -> str:
        """
        Gets the type of this LexV2Slot.
        The slot type

        :return: The type of this LexV2Slot.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this LexV2Slot.
        The slot type

        :param type: The type of this LexV2Slot.
        :type: str
        """
        

        self._type = type

    @property
    def slot_type_id(self) -> str:
        """
        Gets the slot_type_id of this LexV2Slot.
        The slot type id

        :return: The slot_type_id of this LexV2Slot.
        :rtype: str
        """
        return self._slot_type_id

    @slot_type_id.setter
    def slot_type_id(self, slot_type_id: str) -> None:
        """
        Sets the slot_type_id of this LexV2Slot.
        The slot type id

        :param slot_type_id: The slot_type_id of this LexV2Slot.
        :type: str
        """
        

        self._slot_type_id = slot_type_id

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

