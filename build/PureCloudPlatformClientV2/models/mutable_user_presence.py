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
    from . import PresenceDefinition

class MutableUserPresence(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MutableUserPresence - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'source': 'str',
            'source_id': 'str',
            'primary': 'bool',
            'presence_definition': 'PresenceDefinition',
            'message': 'str',
            'modified_date': 'datetime',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'source': 'source',
            'source_id': 'sourceId',
            'primary': 'primary',
            'presence_definition': 'presenceDefinition',
            'message': 'message',
            'modified_date': 'modifiedDate',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._source = None
        self._source_id = None
        self._primary = None
        self._presence_definition = None
        self._message = None
        self._modified_date = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this MutableUserPresence.
        The user's id

        :return: The id of this MutableUserPresence.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this MutableUserPresence.
        The user's id

        :param id: The id of this MutableUserPresence.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this MutableUserPresence.


        :return: The name of this MutableUserPresence.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this MutableUserPresence.


        :param name: The name of this MutableUserPresence.
        :type: str
        """
        

        self._name = name

    @property
    def source(self) -> str:
        """
        Gets the source of this MutableUserPresence.
        Deprecated - The sourceID field should be used as a replacement.

        :return: The source of this MutableUserPresence.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str) -> None:
        """
        Sets the source of this MutableUserPresence.
        Deprecated - The sourceID field should be used as a replacement.

        :param source: The source of this MutableUserPresence.
        :type: str
        """
        

        self._source = source

    @property
    def source_id(self) -> str:
        """
        Gets the source_id of this MutableUserPresence.
        Represents the ID of a registered source

        :return: The source_id of this MutableUserPresence.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id: str) -> None:
        """
        Sets the source_id of this MutableUserPresence.
        Represents the ID of a registered source

        :param source_id: The source_id of this MutableUserPresence.
        :type: str
        """
        

        self._source_id = source_id

    @property
    def primary(self) -> bool:
        """
        Gets the primary of this MutableUserPresence.
        A boolean used to tell whether or not to set this presence source as the primary on a PATCH

        :return: The primary of this MutableUserPresence.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary: bool) -> None:
        """
        Sets the primary of this MutableUserPresence.
        A boolean used to tell whether or not to set this presence source as the primary on a PATCH

        :param primary: The primary of this MutableUserPresence.
        :type: bool
        """
        

        self._primary = primary

    @property
    def presence_definition(self) -> 'PresenceDefinition':
        """
        Gets the presence_definition of this MutableUserPresence.


        :return: The presence_definition of this MutableUserPresence.
        :rtype: PresenceDefinition
        """
        return self._presence_definition

    @presence_definition.setter
    def presence_definition(self, presence_definition: 'PresenceDefinition') -> None:
        """
        Sets the presence_definition of this MutableUserPresence.


        :param presence_definition: The presence_definition of this MutableUserPresence.
        :type: PresenceDefinition
        """
        

        self._presence_definition = presence_definition

    @property
    def message(self) -> str:
        """
        Gets the message of this MutableUserPresence.


        :return: The message of this MutableUserPresence.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """
        Sets the message of this MutableUserPresence.


        :param message: The message of this MutableUserPresence.
        :type: str
        """
        

        self._message = message

    @property
    def modified_date(self) -> datetime:
        """
        Gets the modified_date of this MutableUserPresence.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modified_date of this MutableUserPresence.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date: datetime) -> None:
        """
        Sets the modified_date of this MutableUserPresence.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modified_date: The modified_date of this MutableUserPresence.
        :type: datetime
        """
        

        self._modified_date = modified_date

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this MutableUserPresence.
        The URI for this object

        :return: The self_uri of this MutableUserPresence.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this MutableUserPresence.
        The URI for this object

        :param self_uri: The self_uri of this MutableUserPresence.
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

