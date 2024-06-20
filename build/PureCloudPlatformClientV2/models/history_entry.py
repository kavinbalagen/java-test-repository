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
    from . import User

class HistoryEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        HistoryEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'resource': 'str',
            'timestamp': 'datetime',
            'user': 'User',
            'client': 'DomainEntityRef',
            'version': 'str',
            'secure': 'bool'
        }

        self.attribute_map = {
            'action': 'action',
            'resource': 'resource',
            'timestamp': 'timestamp',
            'user': 'user',
            'client': 'client',
            'version': 'version',
            'secure': 'secure'
        }

        self._action = None
        self._resource = None
        self._timestamp = None
        self._user = None
        self._client = None
        self._version = None
        self._secure = None

    @property
    def action(self) -> str:
        """
        Gets the action of this HistoryEntry.
        The action performed

        :return: The action of this HistoryEntry.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str) -> None:
        """
        Sets the action of this HistoryEntry.
        The action performed

        :param action: The action of this HistoryEntry.
        :type: str
        """
        if isinstance(action, int):
            action = str(action)
        allowed_values = ["CHECKIN", "CHECKOUT", "CREATE", "DEACTIVATE", "DEBUG", "DELETE", "PUBLISH", "REVERT", "SAVE", "TRANSCODE", "UPDATE", "UPLOAD"]
        if action.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action -> " + action)
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def resource(self) -> str:
        """
        Gets the resource of this HistoryEntry.
        For actions performed not on the item itself, but on a sub-item, this field identifies the sub-item by name.  For example, for actions performed on prompt resources, this will be the prompt resource name.

        :return: The resource of this HistoryEntry.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource: str) -> None:
        """
        Sets the resource of this HistoryEntry.
        For actions performed not on the item itself, but on a sub-item, this field identifies the sub-item by name.  For example, for actions performed on prompt resources, this will be the prompt resource name.

        :param resource: The resource of this HistoryEntry.
        :type: str
        """
        

        self._resource = resource

    @property
    def timestamp(self) -> datetime:
        """
        Gets the timestamp of this HistoryEntry.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The timestamp of this HistoryEntry.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime) -> None:
        """
        Sets the timestamp of this HistoryEntry.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param timestamp: The timestamp of this HistoryEntry.
        :type: datetime
        """
        

        self._timestamp = timestamp

    @property
    def user(self) -> 'User':
        """
        Gets the user of this HistoryEntry.
        User associated with this entry.

        :return: The user of this HistoryEntry.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user: 'User') -> None:
        """
        Sets the user of this HistoryEntry.
        User associated with this entry.

        :param user: The user of this HistoryEntry.
        :type: User
        """
        

        self._user = user

    @property
    def client(self) -> 'DomainEntityRef':
        """
        Gets the client of this HistoryEntry.
        OAuth client associated with this entry.

        :return: The client of this HistoryEntry.
        :rtype: DomainEntityRef
        """
        return self._client

    @client.setter
    def client(self, client: 'DomainEntityRef') -> None:
        """
        Sets the client of this HistoryEntry.
        OAuth client associated with this entry.

        :param client: The client of this HistoryEntry.
        :type: DomainEntityRef
        """
        

        self._client = client

    @property
    def version(self) -> str:
        """
        Gets the version of this HistoryEntry.


        :return: The version of this HistoryEntry.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str) -> None:
        """
        Sets the version of this HistoryEntry.


        :param version: The version of this HistoryEntry.
        :type: str
        """
        

        self._version = version

    @property
    def secure(self) -> bool:
        """
        Gets the secure of this HistoryEntry.


        :return: The secure of this HistoryEntry.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure: bool) -> None:
        """
        Sets the secure of this HistoryEntry.


        :param secure: The secure of this HistoryEntry.
        :type: bool
        """
        

        self._secure = secure

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

