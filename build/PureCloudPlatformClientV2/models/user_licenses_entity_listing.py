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
    from . import UserLicenses

class UserLicensesEntityListing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UserLicensesEntityListing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entities': 'list[UserLicenses]',
            'page_size': 'int',
            'page_number': 'int',
            'total': 'int',
            'page_count': 'int'
        }

        self.attribute_map = {
            'entities': 'entities',
            'page_size': 'pageSize',
            'page_number': 'pageNumber',
            'total': 'total',
            'page_count': 'pageCount'
        }

        self._entities = None
        self._page_size = None
        self._page_number = None
        self._total = None
        self._page_count = None

    @property
    def entities(self) -> List['UserLicenses']:
        """
        Gets the entities of this UserLicensesEntityListing.


        :return: The entities of this UserLicensesEntityListing.
        :rtype: list[UserLicenses]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List['UserLicenses']) -> None:
        """
        Sets the entities of this UserLicensesEntityListing.


        :param entities: The entities of this UserLicensesEntityListing.
        :type: list[UserLicenses]
        """
        

        self._entities = entities

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this UserLicensesEntityListing.


        :return: The page_size of this UserLicensesEntityListing.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this UserLicensesEntityListing.


        :param page_size: The page_size of this UserLicensesEntityListing.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this UserLicensesEntityListing.


        :return: The page_number of this UserLicensesEntityListing.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this UserLicensesEntityListing.


        :param page_number: The page_number of this UserLicensesEntityListing.
        :type: int
        """
        

        self._page_number = page_number

    @property
    def total(self) -> int:
        """
        Gets the total of this UserLicensesEntityListing.


        :return: The total of this UserLicensesEntityListing.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int) -> None:
        """
        Sets the total of this UserLicensesEntityListing.


        :param total: The total of this UserLicensesEntityListing.
        :type: int
        """
        

        self._total = total

    @property
    def page_count(self) -> int:
        """
        Gets the page_count of this UserLicensesEntityListing.


        :return: The page_count of this UserLicensesEntityListing.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count: int) -> None:
        """
        Sets the page_count of this UserLicensesEntityListing.


        :param page_count: The page_count of this UserLicensesEntityListing.
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

