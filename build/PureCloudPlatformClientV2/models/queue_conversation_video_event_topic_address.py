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


class QueueConversationVideoEventTopicAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationVideoEventTopicAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'name_raw': 'str',
            'address_normalized': 'str',
            'address_raw': 'str',
            'address_displayable': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'name_raw': 'nameRaw',
            'address_normalized': 'addressNormalized',
            'address_raw': 'addressRaw',
            'address_displayable': 'addressDisplayable'
        }

        self._name = None
        self._name_raw = None
        self._address_normalized = None
        self._address_raw = None
        self._address_displayable = None

    @property
    def name(self) -> str:
        """
        Gets the name of this QueueConversationVideoEventTopicAddress.
        This will be nameRaw if present, or a locality lookup of the address field otherwise.

        :return: The name of this QueueConversationVideoEventTopicAddress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this QueueConversationVideoEventTopicAddress.
        This will be nameRaw if present, or a locality lookup of the address field otherwise.

        :param name: The name of this QueueConversationVideoEventTopicAddress.
        :type: str
        """
        

        self._name = name

    @property
    def name_raw(self) -> str:
        """
        Gets the name_raw of this QueueConversationVideoEventTopicAddress.
        The name as close to the bits on the wire as possible.

        :return: The name_raw of this QueueConversationVideoEventTopicAddress.
        :rtype: str
        """
        return self._name_raw

    @name_raw.setter
    def name_raw(self, name_raw: str) -> None:
        """
        Sets the name_raw of this QueueConversationVideoEventTopicAddress.
        The name as close to the bits on the wire as possible.

        :param name_raw: The name_raw of this QueueConversationVideoEventTopicAddress.
        :type: str
        """
        

        self._name_raw = name_raw

    @property
    def address_normalized(self) -> str:
        """
        Gets the address_normalized of this QueueConversationVideoEventTopicAddress.
        The normalized address. This field is acquired from the Address Normalization Table.  The addressRaw could have gone through some transformations, such as only using the numeric portion, before being run through the Address Normalization Table.

        :return: The address_normalized of this QueueConversationVideoEventTopicAddress.
        :rtype: str
        """
        return self._address_normalized

    @address_normalized.setter
    def address_normalized(self, address_normalized: str) -> None:
        """
        Sets the address_normalized of this QueueConversationVideoEventTopicAddress.
        The normalized address. This field is acquired from the Address Normalization Table.  The addressRaw could have gone through some transformations, such as only using the numeric portion, before being run through the Address Normalization Table.

        :param address_normalized: The address_normalized of this QueueConversationVideoEventTopicAddress.
        :type: str
        """
        

        self._address_normalized = address_normalized

    @property
    def address_raw(self) -> str:
        """
        Gets the address_raw of this QueueConversationVideoEventTopicAddress.
        The address as close to the bits on the wire as possible.

        :return: The address_raw of this QueueConversationVideoEventTopicAddress.
        :rtype: str
        """
        return self._address_raw

    @address_raw.setter
    def address_raw(self, address_raw: str) -> None:
        """
        Sets the address_raw of this QueueConversationVideoEventTopicAddress.
        The address as close to the bits on the wire as possible.

        :param address_raw: The address_raw of this QueueConversationVideoEventTopicAddress.
        :type: str
        """
        

        self._address_raw = address_raw

    @property
    def address_displayable(self) -> str:
        """
        Gets the address_displayable of this QueueConversationVideoEventTopicAddress.
        The displayable address. This field is acquired from the Address Normalization Table.  The addressRaw could have gone through some transformations, such as only using the numeric portion, before being run through the Address Normalization Table.

        :return: The address_displayable of this QueueConversationVideoEventTopicAddress.
        :rtype: str
        """
        return self._address_displayable

    @address_displayable.setter
    def address_displayable(self, address_displayable: str) -> None:
        """
        Sets the address_displayable of this QueueConversationVideoEventTopicAddress.
        The displayable address. This field is acquired from the Address Normalization Table.  The addressRaw could have gone through some transformations, such as only using the numeric portion, before being run through the Address Normalization Table.

        :param address_displayable: The address_displayable of this QueueConversationVideoEventTopicAddress.
        :type: str
        """
        

        self._address_displayable = address_displayable

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
