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
    from . import KnowledgeDocumentGuestSearchResult

class KnowledgeDocumentGuestSearch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeDocumentGuestSearch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'query': 'str',
            'page_size': 'int',
            'page_number': 'int',
            'search_id': 'str',
            'total': 'int',
            'page_count': 'int',
            'query_type': 'str',
            'session_id': 'str',
            'results': 'list[KnowledgeDocumentGuestSearchResult]'
        }

        self.attribute_map = {
            'query': 'query',
            'page_size': 'pageSize',
            'page_number': 'pageNumber',
            'search_id': 'searchId',
            'total': 'total',
            'page_count': 'pageCount',
            'query_type': 'queryType',
            'session_id': 'sessionId',
            'results': 'results'
        }

        self._query = None
        self._page_size = None
        self._page_number = None
        self._search_id = None
        self._total = None
        self._page_count = None
        self._query_type = None
        self._session_id = None
        self._results = None

    @property
    def query(self) -> str:
        """
        Gets the query of this KnowledgeDocumentGuestSearch.
        Query to search content in the knowledge base. Maximum of 30 records per query can be fetched.

        :return: The query of this KnowledgeDocumentGuestSearch.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query: str) -> None:
        """
        Sets the query of this KnowledgeDocumentGuestSearch.
        Query to search content in the knowledge base. Maximum of 30 records per query can be fetched.

        :param query: The query of this KnowledgeDocumentGuestSearch.
        :type: str
        """
        
        if len(query) > 2147483647:
            raise ValueError("Invalid value for `query`, length must be less than `2147483647`")

        if len(query) < 3:
            raise ValueError("Invalid value for `query`, length must be greater than or equal to `3`")


        self._query = query

    @property
    def page_size(self) -> int:
        """
        Gets the page_size of this KnowledgeDocumentGuestSearch.
        Page size of the returned results.

        :return: The page_size of this KnowledgeDocumentGuestSearch.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size: int) -> None:
        """
        Sets the page_size of this KnowledgeDocumentGuestSearch.
        Page size of the returned results.

        :param page_size: The page_size of this KnowledgeDocumentGuestSearch.
        :type: int
        """
        

        self._page_size = page_size

    @property
    def page_number(self) -> int:
        """
        Gets the page_number of this KnowledgeDocumentGuestSearch.
        Page number of the returned results.

        :return: The page_number of this KnowledgeDocumentGuestSearch.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int) -> None:
        """
        Sets the page_number of this KnowledgeDocumentGuestSearch.
        Page number of the returned results.

        :param page_number: The page_number of this KnowledgeDocumentGuestSearch.
        :type: int
        """
        

        self._page_number = page_number

    @property
    def search_id(self) -> str:
        """
        Gets the search_id of this KnowledgeDocumentGuestSearch.
        The globally unique identifier for the search.

        :return: The search_id of this KnowledgeDocumentGuestSearch.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str) -> None:
        """
        Sets the search_id of this KnowledgeDocumentGuestSearch.
        The globally unique identifier for the search.

        :param search_id: The search_id of this KnowledgeDocumentGuestSearch.
        :type: str
        """
        

        self._search_id = search_id

    @property
    def total(self) -> int:
        """
        Gets the total of this KnowledgeDocumentGuestSearch.
        The total number of documents matching the query.

        :return: The total of this KnowledgeDocumentGuestSearch.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int) -> None:
        """
        Sets the total of this KnowledgeDocumentGuestSearch.
        The total number of documents matching the query.

        :param total: The total of this KnowledgeDocumentGuestSearch.
        :type: int
        """
        

        self._total = total

    @property
    def page_count(self) -> int:
        """
        Gets the page_count of this KnowledgeDocumentGuestSearch.
        Number of pages returned in the result calculated according to the pageSize and the total

        :return: The page_count of this KnowledgeDocumentGuestSearch.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count: int) -> None:
        """
        Sets the page_count of this KnowledgeDocumentGuestSearch.
        Number of pages returned in the result calculated according to the pageSize and the total

        :param page_count: The page_count of this KnowledgeDocumentGuestSearch.
        :type: int
        """
        

        self._page_count = page_count

    @property
    def query_type(self) -> str:
        """
        Gets the query_type of this KnowledgeDocumentGuestSearch.
        The type of the query that initiates the search.

        :return: The query_type of this KnowledgeDocumentGuestSearch.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type: str) -> None:
        """
        Sets the query_type of this KnowledgeDocumentGuestSearch.
        The type of the query that initiates the search.

        :param query_type: The query_type of this KnowledgeDocumentGuestSearch.
        :type: str
        """
        if isinstance(query_type, int):
            query_type = str(query_type)
        allowed_values = ["AutoSearch", "ManualSearch", "Suggestion"]
        if query_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_type -> " + query_type)
            self._query_type = "outdated_sdk_version"
        else:
            self._query_type = query_type

    @property
    def session_id(self) -> str:
        """
        Gets the session_id of this KnowledgeDocumentGuestSearch.
        Session ID of the search.

        :return: The session_id of this KnowledgeDocumentGuestSearch.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str) -> None:
        """
        Sets the session_id of this KnowledgeDocumentGuestSearch.
        Session ID of the search.

        :param session_id: The session_id of this KnowledgeDocumentGuestSearch.
        :type: str
        """
        

        self._session_id = session_id

    @property
    def results(self) -> List['KnowledgeDocumentGuestSearchResult']:
        """
        Gets the results of this KnowledgeDocumentGuestSearch.
        Documents that matched the search query.

        :return: The results of this KnowledgeDocumentGuestSearch.
        :rtype: list[KnowledgeDocumentGuestSearchResult]
        """
        return self._results

    @results.setter
    def results(self, results: List['KnowledgeDocumentGuestSearchResult']) -> None:
        """
        Sets the results of this KnowledgeDocumentGuestSearch.
        Documents that matched the search query.

        :param results: The results of this KnowledgeDocumentGuestSearch.
        :type: list[KnowledgeDocumentGuestSearchResult]
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

