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
    from . import LearningAssignment

class LearningAssignmentsDomainEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LearningAssignmentsDomainEntity - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entities': 'list[LearningAssignment]',
            'page_size': 'int',
            'page_number': 'int',
            'total': 'int',
            'previous_uri': 'str',
            'last_uri': 'str',
            'first_uri': 'str',
            'self_uri': 'str',
            'next_uri': 'str',
            'page_count': 'int'
        }

        self.attribute_map = {
            'entities': 'entities',
            'page_size': 'pageSize',
            'page_number': 'pageNumber',
            'total': 'total',
            'previous_uri': 'previousUri',
            'last_uri': 'lastUri',
            'first_uri': 'firstUri',
            'self_uri': 'selfUri',
            'next_uri': 'nextUri',
            'page_count': 'pageCount'
        }

        self._entities = None
        self._page_size = None
        self._page_number = None
        self._total = None
        self._previous_uri = None
        self._last_uri = None
        self._first_uri = None
        self._self_uri = None
        self._next_uri = None
        self._page_count = None

    @property
    def entities(self) -> List['LearningAssignment']:
        """
        Gets the entities of this LearningAssignmentsDomainEntity.


        :return: The entities of this LearningAssignmentsDomainEntity.
        :rtype: list[LearningAssignment]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List['LearningAssignment']) -> None:
        """
        Sets the entities of this LearningAssignmentsDomainEntity.


        :param entities: The entities of this LearningAssignmentsDomainEntity.
        :type: list[LearningAssignment]
        """
        

        self._entities = entities

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this LearningAssignmentsDomainEntity.


        :return: The page_size of this LearningAssignmentsDomainEntity.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this LearningAssignmentsDomainEntity.


        :param page_size: The page_size of this LearningAssignmentsDomainEntity.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this LearningAssignmentsDomainEntity.


        :return: The page_number of this LearningAssignmentsDomainEntity.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this LearningAssignmentsDomainEntity.


        :param page_number: The page_number of this LearningAssignmentsDomainEntity.
        :type: int
        """
        

        self._page_number = page_number

    @property
    def total(self) -> int:
        """
        Gets the total of this LearningAssignmentsDomainEntity.


        :return: The total of this LearningAssignmentsDomainEntity.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int) -> None:
        """
        Sets the total of this LearningAssignmentsDomainEntity.


        :param total: The total of this LearningAssignmentsDomainEntity.
        :type: int
        """
        

        self._total = total

    @property
    def previous_uri(self) -> str:
        """
        Gets the previous_uri of this LearningAssignmentsDomainEntity.


        :return: The previous_uri of this LearningAssignmentsDomainEntity.
        :rtype: str
        """
        return self._previous_uri

    @previous_uri.setter
    def previous_uri(self, previous_uri: str) -> None:
        """
        Sets the previous_uri of this LearningAssignmentsDomainEntity.


        :param previous_uri: The previous_uri of this LearningAssignmentsDomainEntity.
        :type: str
        """
        

        self._previous_uri = previous_uri

    @property
    def last_uri(self) -> str:
        """
        Gets the last_uri of this LearningAssignmentsDomainEntity.


        :return: The last_uri of this LearningAssignmentsDomainEntity.
        :rtype: str
        """
        return self._last_uri

    @last_uri.setter
    def last_uri(self, last_uri: str) -> None:
        """
        Sets the last_uri of this LearningAssignmentsDomainEntity.


        :param last_uri: The last_uri of this LearningAssignmentsDomainEntity.
        :type: str
        """
        

        self._last_uri = last_uri

    @property
    def first_uri(self) -> str:
        """
        Gets the first_uri of this LearningAssignmentsDomainEntity.


        :return: The first_uri of this LearningAssignmentsDomainEntity.
        :rtype: str
        """
        return self._first_uri

    @first_uri.setter
    def first_uri(self, first_uri: str) -> None:
        """
        Sets the first_uri of this LearningAssignmentsDomainEntity.


        :param first_uri: The first_uri of this LearningAssignmentsDomainEntity.
        :type: str
        """
        

        self._first_uri = first_uri

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this LearningAssignmentsDomainEntity.


        :return: The self_uri of this LearningAssignmentsDomainEntity.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this LearningAssignmentsDomainEntity.


        :param self_uri: The self_uri of this LearningAssignmentsDomainEntity.
        :type: str
        """
        

        self._self_uri = self_uri

    @property
    def next_uri(self) -> str:
        """
        Gets the next_uri of this LearningAssignmentsDomainEntity.


        :return: The next_uri of this LearningAssignmentsDomainEntity.
        :rtype: str
        """
        return self._next_uri

    @next_uri.setter
    def next_uri(self, next_uri: str) -> None:
        """
        Sets the next_uri of this LearningAssignmentsDomainEntity.


        :param next_uri: The next_uri of this LearningAssignmentsDomainEntity.
        :type: str
        """
        

        self._next_uri = next_uri

    @property
    def page_count(self) -> int:
        """
        Gets the page_count of this LearningAssignmentsDomainEntity.


        :return: The page_count of this LearningAssignmentsDomainEntity.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count: int) -> None:
        """
        Sets the page_count of this LearningAssignmentsDomainEntity.


        :param page_count: The page_count of this LearningAssignmentsDomainEntity.
        :type: int
        """
        

        self._page_count = page_count

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

