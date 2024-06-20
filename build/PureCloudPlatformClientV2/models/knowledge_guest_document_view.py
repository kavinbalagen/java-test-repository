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


class KnowledgeGuestDocumentView(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeGuestDocumentView - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'document_variation_id': 'str',
            'document_version_id': 'str',
            'search_id': 'str',
            'query_type': 'str',
            'surfacing_method': 'str'
        }

        self.attribute_map = {
            'document_variation_id': 'documentVariationId',
            'document_version_id': 'documentVersionId',
            'search_id': 'searchId',
            'query_type': 'queryType',
            'surfacing_method': 'surfacingMethod'
        }

        self._document_variation_id = None
        self._document_version_id = None
        self._search_id = None
        self._query_type = None
        self._surfacing_method = None

    @property
    def document_variation_id(self) -> str:
        """
        Gets the document_variation_id of this KnowledgeGuestDocumentView.
        The variation of the viewed document.

        :return: The document_variation_id of this KnowledgeGuestDocumentView.
        :rtype: str
        """
        return self._document_variation_id

    @document_variation_id.setter
    def document_variation_id(self, document_variation_id: str) -> None:
        """
        Sets the document_variation_id of this KnowledgeGuestDocumentView.
        The variation of the viewed document.

        :param document_variation_id: The document_variation_id of this KnowledgeGuestDocumentView.
        :type: str
        """
        

        self._document_variation_id = document_variation_id

    @property
    def document_version_id(self) -> str:
        """
        Gets the document_version_id of this KnowledgeGuestDocumentView.
        The version of the viewed document.

        :return: The document_version_id of this KnowledgeGuestDocumentView.
        :rtype: str
        """
        return self._document_version_id

    @document_version_id.setter
    def document_version_id(self, document_version_id: str) -> None:
        """
        Sets the document_version_id of this KnowledgeGuestDocumentView.
        The version of the viewed document.

        :param document_version_id: The document_version_id of this KnowledgeGuestDocumentView.
        :type: str
        """
        

        self._document_version_id = document_version_id

    @property
    def search_id(self) -> str:
        """
        Gets the search_id of this KnowledgeGuestDocumentView.
        The search that surfaced the viewed document.

        :return: The search_id of this KnowledgeGuestDocumentView.
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id: str) -> None:
        """
        Sets the search_id of this KnowledgeGuestDocumentView.
        The search that surfaced the viewed document.

        :param search_id: The search_id of this KnowledgeGuestDocumentView.
        :type: str
        """
        

        self._search_id = search_id

    @property
    def query_type(self) -> str:
        """
        Gets the query_type of this KnowledgeGuestDocumentView.
        The type of the query that surfaced the document.

        :return: The query_type of this KnowledgeGuestDocumentView.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type: str) -> None:
        """
        Sets the query_type of this KnowledgeGuestDocumentView.
        The type of the query that surfaced the document.

        :param query_type: The query_type of this KnowledgeGuestDocumentView.
        :type: str
        """
        if isinstance(query_type, int):
            query_type = str(query_type)
        allowed_values = ["Unknown", "Article", "AutoSearch", "Category", "ManualSearch", "Recommendation", "Suggestion"]
        if query_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_type -> " + query_type)
            self._query_type = "outdated_sdk_version"
        else:
            self._query_type = query_type

    @property
    def surfacing_method(self) -> str:
        """
        Gets the surfacing_method of this KnowledgeGuestDocumentView.
        The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.

        :return: The surfacing_method of this KnowledgeGuestDocumentView.
        :rtype: str
        """
        return self._surfacing_method

    @surfacing_method.setter
    def surfacing_method(self, surfacing_method: str) -> None:
        """
        Sets the surfacing_method of this KnowledgeGuestDocumentView.
        The method how knowledge was surfaced. Article: Full article was shown. Snippet: A snippet from the article was shown. Highlight: A highlighted answer in a snippet was shown.

        :param surfacing_method: The surfacing_method of this KnowledgeGuestDocumentView.
        :type: str
        """
        if isinstance(surfacing_method, int):
            surfacing_method = str(surfacing_method)
        allowed_values = ["Unknown", "Article", "Snippet", "Highlight"]
        if surfacing_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for surfacing_method -> " + surfacing_method)
            self._surfacing_method = "outdated_sdk_version"
        else:
            self._surfacing_method = surfacing_method

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

