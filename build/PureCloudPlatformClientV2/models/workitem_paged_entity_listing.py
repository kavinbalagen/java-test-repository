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
    from . import Workitem

class WorkitemPagedEntityListing(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkitemPagedEntityListing - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'entities': 'list[Workitem]',
            'page_size': 'int',
            'page_number': 'int'
        }

        self.attribute_map = {
            'entities': 'entities',
            'page_size': 'pageSize',
            'page_number': 'pageNumber'
        }

        self._entities = None
        self._page_size = None
        self._page_number = None

    @property
    def entities(self) -> List['Workitem']:
        """
        Gets the entities of this WorkitemPagedEntityListing.


        :return: The entities of this WorkitemPagedEntityListing.
        :rtype: list[Workitem]
        """
        return self._entities

    @entities.setter
    def entities(self, entities: List['Workitem']) -> None:
        """
        Sets the entities of this WorkitemPagedEntityListing.


        :param entities: The entities of this WorkitemPagedEntityListing.
        :type: list[Workitem]
        """
        

        self._entities = entities

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this WorkitemPagedEntityListing.
        The total page size requested

        :return: The page_size of this WorkitemPagedEntityListing.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this WorkitemPagedEntityListing.
        The total page size requested

        :param page_size: The page_size of this WorkitemPagedEntityListing.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this WorkitemPagedEntityListing.
        The page number requested

        :return: The page_number of this WorkitemPagedEntityListing.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this WorkitemPagedEntityListing.
        The page number requested

        :param page_number: The page_number of this WorkitemPagedEntityListing.
        :type: int
        """
        

        self._page_number = page_number

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

