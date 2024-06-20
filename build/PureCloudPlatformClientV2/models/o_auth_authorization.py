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
    from . import DomainEntityRef
    from . import OAuthClient

class OAuthAuthorization(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OAuthAuthorization - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client': 'OAuthClient',
            'scope': 'list[str]',
            'roles': 'list[str]',
            'resource_owner': 'DomainEntityRef',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'created_by': 'DomainEntityRef',
            'modified_by': 'DomainEntityRef',
            'pending': 'bool',
            'state': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'client': 'client',
            'scope': 'scope',
            'roles': 'roles',
            'resource_owner': 'resourceOwner',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'pending': 'pending',
            'state': 'state',
            'self_uri': 'selfUri'
        }

        self._client = None
        self._scope = None
        self._roles = None
        self._resource_owner = None
        self._date_created = None
        self._date_modified = None
        self._created_by = None
        self._modified_by = None
        self._pending = None
        self._state = None
        self._self_uri = None

    @property
    def client(self) -> 'OAuthClient':
        """
        Gets the client of this OAuthAuthorization.


        :return: The client of this OAuthAuthorization.
        :rtype: OAuthClient
        """
        return self._client

    @client.setter
    def client(self, client: 'OAuthClient') -> None:
        """
        Sets the client of this OAuthAuthorization.


        :param client: The client of this OAuthAuthorization.
        :type: OAuthClient
        """
        

        self._client = client

    @property
    def scope(self) -> List[str]:
        """
        Gets the scope of this OAuthAuthorization.


        :return: The scope of this OAuthAuthorization.
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope: List[str]) -> None:
        """
        Sets the scope of this OAuthAuthorization.


        :param scope: The scope of this OAuthAuthorization.
        :type: list[str]
        """
        

        self._scope = scope

    @property
    def roles(self) -> List[str]:
        """
        Gets the roles of this OAuthAuthorization.


        :return: The roles of this OAuthAuthorization.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles: List[str]) -> None:
        """
        Sets the roles of this OAuthAuthorization.


        :param roles: The roles of this OAuthAuthorization.
        :type: list[str]
        """
        

        self._roles = roles

    @property
    def resource_owner(self) -> 'DomainEntityRef':
        """
        Gets the resource_owner of this OAuthAuthorization.


        :return: The resource_owner of this OAuthAuthorization.
        :rtype: DomainEntityRef
        """
        return self._resource_owner

    @resource_owner.setter
    def resource_owner(self, resource_owner: 'DomainEntityRef') -> None:
        """
        Sets the resource_owner of this OAuthAuthorization.


        :param resource_owner: The resource_owner of this OAuthAuthorization.
        :type: DomainEntityRef
        """
        

        self._resource_owner = resource_owner

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this OAuthAuthorization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this OAuthAuthorization.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this OAuthAuthorization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this OAuthAuthorization.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this OAuthAuthorization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this OAuthAuthorization.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this OAuthAuthorization.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this OAuthAuthorization.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def created_by(self) -> 'DomainEntityRef':
        """
        Gets the created_by of this OAuthAuthorization.


        :return: The created_by of this OAuthAuthorization.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'DomainEntityRef') -> None:
        """
        Sets the created_by of this OAuthAuthorization.


        :param created_by: The created_by of this OAuthAuthorization.
        :type: DomainEntityRef
        """
        

        self._created_by = created_by

    @property
    def modified_by(self) -> 'DomainEntityRef':
        """
        Gets the modified_by of this OAuthAuthorization.


        :return: The modified_by of this OAuthAuthorization.
        :rtype: DomainEntityRef
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'DomainEntityRef') -> None:
        """
        Sets the modified_by of this OAuthAuthorization.


        :param modified_by: The modified_by of this OAuthAuthorization.
        :type: DomainEntityRef
        """
        

        self._modified_by = modified_by

    @property
    def pending(self) -> bool:
        """
        Gets the pending of this OAuthAuthorization.


        :return: The pending of this OAuthAuthorization.
        :rtype: bool
        """
        return self._pending

    @pending.setter
    def pending(self, pending: bool) -> None:
        """
        Sets the pending of this OAuthAuthorization.


        :param pending: The pending of this OAuthAuthorization.
        :type: bool
        """
        

        self._pending = pending

    @property
    def state(self) -> str:
        """
        Gets the state of this OAuthAuthorization.


        :return: The state of this OAuthAuthorization.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this OAuthAuthorization.


        :param state: The state of this OAuthAuthorization.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Unauthorized", "Requested", "Authorized", "Revoked"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this OAuthAuthorization.
        The URI for this object

        :return: The self_uri of this OAuthAuthorization.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this OAuthAuthorization.
        The URI for this object

        :param self_uri: The self_uri of this OAuthAuthorization.
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

