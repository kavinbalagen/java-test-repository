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
    from . import HomerRecord

class SipSearchResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SipSearchResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'status': 'int',
            'sid': 'str',
            'auth': 'str',
            'message': 'str',
            'data': 'list[HomerRecord]',
            'count': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'sid': 'sid',
            'auth': 'auth',
            'message': 'message',
            'data': 'data',
            'count': 'count',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._status = None
        self._sid = None
        self._auth = None
        self._message = None
        self._data = None
        self._count = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this SipSearchResult.
        The globally unique identifier for the object.

        :return: The id of this SipSearchResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this SipSearchResult.
        The globally unique identifier for the object.

        :param id: The id of this SipSearchResult.
        :type: str
        """
        

        self._id = id

    @property
    def status(self) -> int:
        """
        Gets the status of this SipSearchResult.
        Status of the search request

        :return: The status of this SipSearchResult.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int) -> None:
        """
        Sets the status of this SipSearchResult.
        Status of the search request

        :param status: The status of this SipSearchResult.
        :type: int
        """
        

        self._status = status

    @property
    def sid(self) -> str:
        """
        Gets the sid of this SipSearchResult.
        Session id associated to the search request

        :return: The sid of this SipSearchResult.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid: str) -> None:
        """
        Sets the sid of this SipSearchResult.
        Session id associated to the search request

        :param sid: The sid of this SipSearchResult.
        :type: str
        """
        

        self._sid = sid

    @property
    def auth(self) -> str:
        """
        Gets the auth of this SipSearchResult.
        Auth token used for this search request

        :return: The auth of this SipSearchResult.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth: str) -> None:
        """
        Sets the auth of this SipSearchResult.
        Auth token used for this search request

        :param auth: The auth of this SipSearchResult.
        :type: str
        """
        

        self._auth = auth

    @property
    def message(self) -> str:
        """
        Gets the message of this SipSearchResult.
        Any messages returned from homer as part of the response

        :return: The message of this SipSearchResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """
        Sets the message of this SipSearchResult.
        Any messages returned from homer as part of the response

        :param message: The message of this SipSearchResult.
        :type: str
        """
        

        self._message = message

    @property
    def data(self) -> List['HomerRecord']:
        """
        Gets the data of this SipSearchResult.
        Homer search data that is returned

        :return: The data of this SipSearchResult.
        :rtype: list[HomerRecord]
        """
        return self._data

    @data.setter
    def data(self, data: List['HomerRecord']) -> None:
        """
        Sets the data of this SipSearchResult.
        Homer search data that is returned

        :param data: The data of this SipSearchResult.
        :type: list[HomerRecord]
        """
        

        self._data = data

    @property
    def count(self) -> int:
        """
        Gets the count of this SipSearchResult.
        Number of records returned

        :return: The count of this SipSearchResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int) -> None:
        """
        Sets the count of this SipSearchResult.
        Number of records returned

        :param count: The count of this SipSearchResult.
        :type: int
        """
        

        self._count = count

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this SipSearchResult.
        The URI for this object

        :return: The self_uri of this SipSearchResult.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this SipSearchResult.
        The URI for this object

        :param self_uri: The self_uri of this SipSearchResult.
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

