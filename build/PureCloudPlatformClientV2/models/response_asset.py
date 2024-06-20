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
    from . import Division
    from . import DomainEntityRef

class ResponseAsset(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ResponseAsset - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'Division',
            'content_length': 'int',
            'content_location': 'str',
            'content_type': 'str',
            'date_created': 'datetime',
            'created_by': 'DomainEntityRef',
            'date_modified': 'datetime',
            'modified_by': 'DomainEntityRef',
            'responses': 'list[DomainEntityRef]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'content_length': 'contentLength',
            'content_location': 'contentLocation',
            'content_type': 'contentType',
            'date_created': 'dateCreated',
            'created_by': 'createdBy',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'responses': 'responses',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._content_length = None
        self._content_location = None
        self._content_type = None
        self._date_created = None
        self._created_by = None
        self._date_modified = None
        self._modified_by = None
        self._responses = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this ResponseAsset.
        The globally unique identifier for the object.

        :return: The id of this ResponseAsset.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ResponseAsset.
        The globally unique identifier for the object.

        :param id: The id of this ResponseAsset.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this ResponseAsset.


        :return: The name of this ResponseAsset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ResponseAsset.


        :param name: The name of this ResponseAsset.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this ResponseAsset.
        The division to which this entity belongs.

        :return: The division of this ResponseAsset.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this ResponseAsset.
        The division to which this entity belongs.

        :param division: The division of this ResponseAsset.
        :type: Division
        """
        

        self._division = division

    @property
    def content_length(self) -> int:
        """
        Gets the content_length of this ResponseAsset.
        response asset size in bytes

        :return: The content_length of this ResponseAsset.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length: int) -> None:
        """
        Sets the content_length of this ResponseAsset.
        response asset size in bytes

        :param content_length: The content_length of this ResponseAsset.
        :type: int
        """
        

        self._content_length = content_length

    @property
    def content_location(self) -> str:
        """
        Gets the content_location of this ResponseAsset.
        response asset location.

        :return: The content_location of this ResponseAsset.
        :rtype: str
        """
        return self._content_location

    @content_location.setter
    def content_location(self, content_location: str) -> None:
        """
        Sets the content_location of this ResponseAsset.
        response asset location.

        :param content_location: The content_location of this ResponseAsset.
        :type: str
        """
        

        self._content_location = content_location

    @property
    def content_type(self) -> str:
        """
        Gets the content_type of this ResponseAsset.
        MIME type of response asset

        :return: The content_type of this ResponseAsset.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        """
        Sets the content_type of this ResponseAsset.
        MIME type of response asset

        :param content_type: The content_type of this ResponseAsset.
        :type: str
        """
        

        self._content_type = content_type

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this ResponseAsset.
        Created date of the response asset. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this ResponseAsset.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this ResponseAsset.
        Created date of the response asset. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this ResponseAsset.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def created_by(self) -> 'DomainEntityRef':
        """
        Gets the created_by of this ResponseAsset.
        User who created the response asset

        :return: The created_by of this ResponseAsset.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'DomainEntityRef') -> None:
        """
        Sets the created_by of this ResponseAsset.
        User who created the response asset

        :param created_by: The created_by of this ResponseAsset.
        :type: DomainEntityRef
        """
        

        self._created_by = created_by

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this ResponseAsset.
        Last modified date of the response asset. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this ResponseAsset.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this ResponseAsset.
        Last modified date of the response asset. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this ResponseAsset.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> 'DomainEntityRef':
        """
        Gets the modified_by of this ResponseAsset.
        User who last modified the response asset

        :return: The modified_by of this ResponseAsset.
        :rtype: DomainEntityRef
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'DomainEntityRef') -> None:
        """
        Sets the modified_by of this ResponseAsset.
        User who last modified the response asset

        :param modified_by: The modified_by of this ResponseAsset.
        :type: DomainEntityRef
        """
        

        self._modified_by = modified_by

    @property
    def responses(self) -> List['DomainEntityRef']:
        """
        Gets the responses of this ResponseAsset.
        Canned responses actively using this asset

        :return: The responses of this ResponseAsset.
        :rtype: list[DomainEntityRef]
        """
        return self._responses

    @responses.setter
    def responses(self, responses: List['DomainEntityRef']) -> None:
        """
        Sets the responses of this ResponseAsset.
        Canned responses actively using this asset

        :param responses: The responses of this ResponseAsset.
        :type: list[DomainEntityRef]
        """
        

        self._responses = responses

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this ResponseAsset.
        The URI for this object

        :return: The self_uri of this ResponseAsset.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this ResponseAsset.
        The URI for this object

        :param self_uri: The self_uri of this ResponseAsset.
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

