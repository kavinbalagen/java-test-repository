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
    from . import DomainEntityRef

class DIDNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DIDNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'number': 'str',
            'assigned': 'bool',
            'did_pool': 'AddressableEntityRef',
            'owner': 'DomainEntityRef',
            'owner_type': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'number': 'number',
            'assigned': 'assigned',
            'did_pool': 'didPool',
            'owner': 'owner',
            'owner_type': 'ownerType',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._number = None
        self._assigned = None
        self._did_pool = None
        self._owner = None
        self._owner_type = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this DIDNumber.
        The globally unique identifier for the object.

        :return: The id of this DIDNumber.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DIDNumber.
        The globally unique identifier for the object.

        :param id: The id of this DIDNumber.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DIDNumber.


        :return: The name of this DIDNumber.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DIDNumber.


        :param name: The name of this DIDNumber.
        :type: str
        """
        

        self._name = name

    @property
    def number(self) -> str:
        """
        Gets the number of this DIDNumber.
        The number of the DID formatted as E164.

        :return: The number of this DIDNumber.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number: str) -> None:
        """
        Sets the number of this DIDNumber.
        The number of the DID formatted as E164.

        :param number: The number of this DIDNumber.
        :type: str
        """
        

        self._number = number

    @property
    def assigned(self) -> bool:
        """
        Gets the assigned of this DIDNumber.
        True if this DID is assigned to an entity.  False otherwise.

        :return: The assigned of this DIDNumber.
        :rtype: bool
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned: bool) -> None:
        """
        Sets the assigned of this DIDNumber.
        True if this DID is assigned to an entity.  False otherwise.

        :param assigned: The assigned of this DIDNumber.
        :type: bool
        """
        

        self._assigned = assigned

    @property
    def did_pool(self) -> 'AddressableEntityRef':
        """
        Gets the did_pool of this DIDNumber.
        A Uri reference to the DID Pool this DID is a part of.

        :return: The did_pool of this DIDNumber.
        :rtype: AddressableEntityRef
        """
        return self._did_pool

    @did_pool.setter
    def did_pool(self, did_pool: 'AddressableEntityRef') -> None:
        """
        Sets the did_pool of this DIDNumber.
        A Uri reference to the DID Pool this DID is a part of.

        :param did_pool: The did_pool of this DIDNumber.
        :type: AddressableEntityRef
        """
        

        self._did_pool = did_pool

    @property
    def owner(self) -> 'DomainEntityRef':
        """
        Gets the owner of this DIDNumber.
        A Uri reference to the owner of this DID.  The owner's type can be found in ownerType.  If the DID is unassigned, this will be NULL.

        :return: The owner of this DIDNumber.
        :rtype: DomainEntityRef
        """
        return self._owner

    @owner.setter
    def owner(self, owner: 'DomainEntityRef') -> None:
        """
        Sets the owner of this DIDNumber.
        A Uri reference to the owner of this DID.  The owner's type can be found in ownerType.  If the DID is unassigned, this will be NULL.

        :param owner: The owner of this DIDNumber.
        :type: DomainEntityRef
        """
        

        self._owner = owner

    @property
    def owner_type(self) -> str:
        """
        Gets the owner_type of this DIDNumber.
        The type of the entity that owns this DID.  If the DID is unassigned, this will be NULL.

        :return: The owner_type of this DIDNumber.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type: str) -> None:
        """
        Sets the owner_type of this DIDNumber.
        The type of the entity that owns this DID.  If the DID is unassigned, this will be NULL.

        :param owner_type: The owner_type of this DIDNumber.
        :type: str
        """
        if isinstance(owner_type, int):
            owner_type = str(owner_type)
        allowed_values = ["USER", "PHONE", "IVR_CONFIG", "GROUP"]
        if owner_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for owner_type -> " + owner_type)
            self._owner_type = "outdated_sdk_version"
        else:
            self._owner_type = owner_type

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this DIDNumber.
        The URI for this object

        :return: The self_uri of this DIDNumber.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this DIDNumber.
        The URI for this object

        :param self_uri: The self_uri of this DIDNumber.
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

