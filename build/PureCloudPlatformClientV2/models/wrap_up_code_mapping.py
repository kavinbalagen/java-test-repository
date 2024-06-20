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


class WrapUpCodeMapping(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WrapUpCodeMapping - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'default_set': 'list[str]',
            'mapping': 'dict(str, list[str])',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'default_set': 'defaultSet',
            'mapping': 'mapping',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._default_set = None
        self._mapping = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WrapUpCodeMapping.
        The globally unique identifier for the object.

        :return: The id of this WrapUpCodeMapping.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WrapUpCodeMapping.
        The globally unique identifier for the object.

        :param id: The id of this WrapUpCodeMapping.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this WrapUpCodeMapping.


        :return: The name of this WrapUpCodeMapping.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this WrapUpCodeMapping.


        :param name: The name of this WrapUpCodeMapping.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this WrapUpCodeMapping.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this WrapUpCodeMapping.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this WrapUpCodeMapping.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this WrapUpCodeMapping.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this WrapUpCodeMapping.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this WrapUpCodeMapping.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this WrapUpCodeMapping.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this WrapUpCodeMapping.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this WrapUpCodeMapping.
        Required for updates, must match the version number of the most recent update

        :return: The version of this WrapUpCodeMapping.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this WrapUpCodeMapping.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this WrapUpCodeMapping.
        :type: int
        """
        

        self._version = version

    @property
    def default_set(self) -> List[str]:
        """
        Gets the default_set of this WrapUpCodeMapping.
        The default set of wrap-up flags. These will be used if there is no entry for a given wrap-up code in the mapping.

        :return: The default_set of this WrapUpCodeMapping.
        :rtype: list[str]
        """
        return self._default_set

    @default_set.setter
    def default_set(self, default_set: List[str]) -> None:
        """
        Sets the default_set of this WrapUpCodeMapping.
        The default set of wrap-up flags. These will be used if there is no entry for a given wrap-up code in the mapping.

        :param default_set: The default_set of this WrapUpCodeMapping.
        :type: list[str]
        """
        

        self._default_set = default_set

    @property
    def mapping(self) -> List[str]:
        """
        Gets the mapping of this WrapUpCodeMapping.
        A map from wrap-up code identifiers to a set of wrap-up flags.

        :return: The mapping of this WrapUpCodeMapping.
        :rtype: dict(str, list[str])
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping: List[str]) -> None:
        """
        Sets the mapping of this WrapUpCodeMapping.
        A map from wrap-up code identifiers to a set of wrap-up flags.

        :param mapping: The mapping of this WrapUpCodeMapping.
        :type: dict(str, list[str])
        """
        

        self._mapping = mapping

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this WrapUpCodeMapping.
        The URI for this object

        :return: The self_uri of this WrapUpCodeMapping.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this WrapUpCodeMapping.
        The URI for this object

        :param self_uri: The self_uri of this WrapUpCodeMapping.
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
