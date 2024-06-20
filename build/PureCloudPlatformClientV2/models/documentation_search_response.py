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
    from . import DocumentationResult

class DocumentationSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DocumentationSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int',
            'page_count': 'int',
            'page_size': 'int',
            'page_number': 'int',
            'previous_page': 'str',
            'current_page': 'str',
            'next_page': 'str',
            'types': 'list[str]',
            'results': 'list[DocumentationResult]'
        }

        self.attribute_map = {
            'total': 'total',
            'page_count': 'pageCount',
            'page_size': 'pageSize',
            'page_number': 'pageNumber',
            'previous_page': 'previousPage',
            'current_page': 'currentPage',
            'next_page': 'nextPage',
            'types': 'types',
            'results': 'results'
        }

        self._total = None
        self._page_count = None
        self._page_size = None
        self._page_number = None
        self._previous_page = None
        self._current_page = None
        self._next_page = None
        self._types = None
        self._results = None

    @property
    def total(self) -> int:
        """
        Gets the total of this DocumentationSearchResponse.
        The total number of results found

        :return: The total of this DocumentationSearchResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int) -> None:
        """
        Sets the total of this DocumentationSearchResponse.
        The total number of results found

        :param total: The total of this DocumentationSearchResponse.
        :type: int
        """
        

        self._total = total

    @property
    def page_count(self) -> int:
        """
        Gets the page_count of this DocumentationSearchResponse.
        The total number of pages

        :return: The page_count of this DocumentationSearchResponse.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count: int) -> None:
        """
        Sets the page_count of this DocumentationSearchResponse.
        The total number of pages

        :param page_count: The page_count of this DocumentationSearchResponse.
        :type: int
        """
        

        self._page_count = page_count

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this DocumentationSearchResponse.
        The current page size

        :return: The page_size of this DocumentationSearchResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this DocumentationSearchResponse.
        The current page size

        :param page_size: The page_size of this DocumentationSearchResponse.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this DocumentationSearchResponse.
        The current page number

        :return: The page_number of this DocumentationSearchResponse.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this DocumentationSearchResponse.
        The current page number

        :param page_number: The page_number of this DocumentationSearchResponse.
        :type: int
        """
        

        self._page_number = page_number

    @property
    def previous_page(self) -> str:
        """
        Gets the previous_page of this DocumentationSearchResponse.
        Q64 value for the previous page of results

        :return: The previous_page of this DocumentationSearchResponse.
        :rtype: str
        """
        return self._previous_page

    @previous_page.setter
    def previous_page(self, previous_page: str) -> None:
        """
        Sets the previous_page of this DocumentationSearchResponse.
        Q64 value for the previous page of results

        :param previous_page: The previous_page of this DocumentationSearchResponse.
        :type: str
        """
        

        self._previous_page = previous_page

    @property
    def current_page(self) -> str:
        """
        Gets the current_page of this DocumentationSearchResponse.
        Q64 value for the current page of results

        :return: The current_page of this DocumentationSearchResponse.
        :rtype: str
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page: str) -> None:
        """
        Sets the current_page of this DocumentationSearchResponse.
        Q64 value for the current page of results

        :param current_page: The current_page of this DocumentationSearchResponse.
        :type: str
        """
        

        self._current_page = current_page

    @property
    def next_page(self) -> str:
        """
        Gets the next_page of this DocumentationSearchResponse.
        Q64 value for the next page of results

        :return: The next_page of this DocumentationSearchResponse.
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page: str) -> None:
        """
        Sets the next_page of this DocumentationSearchResponse.
        Q64 value for the next page of results

        :param next_page: The next_page of this DocumentationSearchResponse.
        :type: str
        """
        

        self._next_page = next_page

    @property
    def types(self) -> List[str]:
        """
        Gets the types of this DocumentationSearchResponse.
        Resource types the search was performed against

        :return: The types of this DocumentationSearchResponse.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types: List[str]) -> None:
        """
        Sets the types of this DocumentationSearchResponse.
        Resource types the search was performed against

        :param types: The types of this DocumentationSearchResponse.
        :type: list[str]
        """
        

        self._types = types

    @property
    def results(self) -> List['DocumentationResult']:
        """
        Gets the results of this DocumentationSearchResponse.
        Search results

        :return: The results of this DocumentationSearchResponse.
        :rtype: list[DocumentationResult]
        """
        return self._results

    @results.setter
    def results(self, results: List['DocumentationResult']) -> None:
        """
        Sets the results of this DocumentationSearchResponse.
        Search results

        :param results: The results of this DocumentationSearchResponse.
        :type: list[DocumentationResult]
        """
        

        self._results = results

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

