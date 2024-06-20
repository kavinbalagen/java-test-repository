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
    from . import AddressableEntityRef
    from . import CategoryResponse
    from . import DocumentVariation
    from . import KnowledgeBaseReference
    from . import KnowledgeDocumentAlternative
    from . import LabelResponse
    from . import UserReference

class KnowledgeDocumentResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeDocumentResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'visible': 'bool',
            'alternatives': 'list[KnowledgeDocumentAlternative]',
            'state': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'date_imported': 'datetime',
            'last_published_version_number': 'int',
            'date_published': 'datetime',
            'created_by': 'UserReference',
            'modified_by': 'UserReference',
            'document_version': 'AddressableEntityRef',
            'category': 'CategoryResponse',
            'labels': 'list[LabelResponse]',
            'knowledge_base': 'KnowledgeBaseReference',
            'external_id': 'str',
            'source': 'AddressableEntityRef',
            'readonly': 'bool',
            'variations': 'list[DocumentVariation]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'visible': 'visible',
            'alternatives': 'alternatives',
            'state': 'state',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'date_imported': 'dateImported',
            'last_published_version_number': 'lastPublishedVersionNumber',
            'date_published': 'datePublished',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'document_version': 'documentVersion',
            'category': 'category',
            'labels': 'labels',
            'knowledge_base': 'knowledgeBase',
            'external_id': 'externalId',
            'source': 'source',
            'readonly': 'readonly',
            'variations': 'variations',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._title = None
        self._visible = None
        self._alternatives = None
        self._state = None
        self._date_created = None
        self._date_modified = None
        self._date_imported = None
        self._last_published_version_number = None
        self._date_published = None
        self._created_by = None
        self._modified_by = None
        self._document_version = None
        self._category = None
        self._labels = None
        self._knowledge_base = None
        self._external_id = None
        self._source = None
        self._readonly = None
        self._variations = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this KnowledgeDocumentResponse.
        The globally unique identifier for the object.

        :return: The id of this KnowledgeDocumentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this KnowledgeDocumentResponse.
        The globally unique identifier for the object.

        :param id: The id of this KnowledgeDocumentResponse.
        :type: str
        """
        

        self._id = id

    @property
    def title(self) -> str:
        """
        Gets the title of this KnowledgeDocumentResponse.
        Document title, having a limit of 500 words.

        :return: The title of this KnowledgeDocumentResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        """
        Sets the title of this KnowledgeDocumentResponse.
        Document title, having a limit of 500 words.

        :param title: The title of this KnowledgeDocumentResponse.
        :type: str
        """
        

        self._title = title

    @property
    def visible(self) -> bool:
        """
        Gets the visible of this KnowledgeDocumentResponse.
        Indicates if the knowledge document should be included in search results.

        :return: The visible of this KnowledgeDocumentResponse.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible: bool) -> None:
        """
        Sets the visible of this KnowledgeDocumentResponse.
        Indicates if the knowledge document should be included in search results.

        :param visible: The visible of this KnowledgeDocumentResponse.
        :type: bool
        """
        

        self._visible = visible

    @property
    def alternatives(self) -> List['KnowledgeDocumentAlternative']:
        """
        Gets the alternatives of this KnowledgeDocumentResponse.
        List of alternate phrases related to the title which improves search results.

        :return: The alternatives of this KnowledgeDocumentResponse.
        :rtype: list[KnowledgeDocumentAlternative]
        """
        return self._alternatives

    @alternatives.setter
    def alternatives(self, alternatives: List['KnowledgeDocumentAlternative']) -> None:
        """
        Sets the alternatives of this KnowledgeDocumentResponse.
        List of alternate phrases related to the title which improves search results.

        :param alternatives: The alternatives of this KnowledgeDocumentResponse.
        :type: list[KnowledgeDocumentAlternative]
        """
        

        self._alternatives = alternatives

    @property
    def state(self) -> str:
        """
        Gets the state of this KnowledgeDocumentResponse.
        State of the document.

        :return: The state of this KnowledgeDocumentResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this KnowledgeDocumentResponse.
        State of the document.

        :param state: The state of this KnowledgeDocumentResponse.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Draft", "Published", "Archived"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this KnowledgeDocumentResponse.
        Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this KnowledgeDocumentResponse.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this KnowledgeDocumentResponse.
        Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this KnowledgeDocumentResponse.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this KnowledgeDocumentResponse.
        Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this KnowledgeDocumentResponse.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this KnowledgeDocumentResponse.
        Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this KnowledgeDocumentResponse.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def date_imported(self) -> datetime:
        """
        Gets the date_imported of this KnowledgeDocumentResponse.
        Document import date-time, or null if was not imported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_imported of this KnowledgeDocumentResponse.
        :rtype: datetime
        """
        return self._date_imported

    @date_imported.setter
    def date_imported(self, date_imported: datetime) -> None:
        """
        Sets the date_imported of this KnowledgeDocumentResponse.
        Document import date-time, or null if was not imported. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_imported: The date_imported of this KnowledgeDocumentResponse.
        :type: datetime
        """
        

        self._date_imported = date_imported

    @property
    def last_published_version_number(self) -> int:
        """
        Gets the last_published_version_number of this KnowledgeDocumentResponse.
        The last published version number of the document.

        :return: The last_published_version_number of this KnowledgeDocumentResponse.
        :rtype: int
        """
        return self._last_published_version_number

    @last_published_version_number.setter
    def last_published_version_number(self, last_published_version_number: int) -> None:
        """
        Sets the last_published_version_number of this KnowledgeDocumentResponse.
        The last published version number of the document.

        :param last_published_version_number: The last_published_version_number of this KnowledgeDocumentResponse.
        :type: int
        """
        

        self._last_published_version_number = last_published_version_number

    @property
    def date_published(self) -> datetime:
        """
        Gets the date_published of this KnowledgeDocumentResponse.
        The date on which the document was last published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_published of this KnowledgeDocumentResponse.
        :rtype: datetime
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published: datetime) -> None:
        """
        Sets the date_published of this KnowledgeDocumentResponse.
        The date on which the document was last published. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_published: The date_published of this KnowledgeDocumentResponse.
        :type: datetime
        """
        

        self._date_published = date_published

    @property
    def created_by(self) -> 'UserReference':
        """
        Gets the created_by of this KnowledgeDocumentResponse.
        The user who created the document.

        :return: The created_by of this KnowledgeDocumentResponse.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'UserReference') -> None:
        """
        Sets the created_by of this KnowledgeDocumentResponse.
        The user who created the document.

        :param created_by: The created_by of this KnowledgeDocumentResponse.
        :type: UserReference
        """
        

        self._created_by = created_by

    @property
    def modified_by(self) -> 'UserReference':
        """
        Gets the modified_by of this KnowledgeDocumentResponse.
        The user who modified the document.

        :return: The modified_by of this KnowledgeDocumentResponse.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'UserReference') -> None:
        """
        Sets the modified_by of this KnowledgeDocumentResponse.
        The user who modified the document.

        :param modified_by: The modified_by of this KnowledgeDocumentResponse.
        :type: UserReference
        """
        

        self._modified_by = modified_by

    @property
    def document_version(self) -> 'AddressableEntityRef':
        """
        Gets the document_version of this KnowledgeDocumentResponse.
        The version of the document.

        :return: The document_version of this KnowledgeDocumentResponse.
        :rtype: AddressableEntityRef
        """
        return self._document_version

    @document_version.setter
    def document_version(self, document_version: 'AddressableEntityRef') -> None:
        """
        Sets the document_version of this KnowledgeDocumentResponse.
        The version of the document.

        :param document_version: The document_version of this KnowledgeDocumentResponse.
        :type: AddressableEntityRef
        """
        

        self._document_version = document_version

    @property
    def category(self) -> 'CategoryResponse':
        """
        Gets the category of this KnowledgeDocumentResponse.
        The reference to category associated with the document.

        :return: The category of this KnowledgeDocumentResponse.
        :rtype: CategoryResponse
        """
        return self._category

    @category.setter
    def category(self, category: 'CategoryResponse') -> None:
        """
        Sets the category of this KnowledgeDocumentResponse.
        The reference to category associated with the document.

        :param category: The category of this KnowledgeDocumentResponse.
        :type: CategoryResponse
        """
        

        self._category = category

    @property
    def labels(self) -> List['LabelResponse']:
        """
        Gets the labels of this KnowledgeDocumentResponse.
        The references to labels associated with the document.

        :return: The labels of this KnowledgeDocumentResponse.
        :rtype: list[LabelResponse]
        """
        return self._labels

    @labels.setter
    def labels(self, labels: List['LabelResponse']) -> None:
        """
        Sets the labels of this KnowledgeDocumentResponse.
        The references to labels associated with the document.

        :param labels: The labels of this KnowledgeDocumentResponse.
        :type: list[LabelResponse]
        """
        

        self._labels = labels

    @property
    def knowledge_base(self) -> 'KnowledgeBaseReference':
        """
        Gets the knowledge_base of this KnowledgeDocumentResponse.
        Knowledge base to which the document belongs to.

        :return: The knowledge_base of this KnowledgeDocumentResponse.
        :rtype: KnowledgeBaseReference
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base: 'KnowledgeBaseReference') -> None:
        """
        Sets the knowledge_base of this KnowledgeDocumentResponse.
        Knowledge base to which the document belongs to.

        :param knowledge_base: The knowledge_base of this KnowledgeDocumentResponse.
        :type: KnowledgeBaseReference
        """
        

        self._knowledge_base = knowledge_base

    @property
    def external_id(self) -> str:
        """
        Gets the external_id of this KnowledgeDocumentResponse.
        The reference to external id associated with the document.

        :return: The external_id of this KnowledgeDocumentResponse.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id: str) -> None:
        """
        Sets the external_id of this KnowledgeDocumentResponse.
        The reference to external id associated with the document.

        :param external_id: The external_id of this KnowledgeDocumentResponse.
        :type: str
        """
        

        self._external_id = external_id

    @property
    def source(self) -> 'AddressableEntityRef':
        """
        Gets the source of this KnowledgeDocumentResponse.
        The reference to source associated with the document.

        :return: The source of this KnowledgeDocumentResponse.
        :rtype: AddressableEntityRef
        """
        return self._source

    @source.setter
    def source(self, source: 'AddressableEntityRef') -> None:
        """
        Sets the source of this KnowledgeDocumentResponse.
        The reference to source associated with the document.

        :param source: The source of this KnowledgeDocumentResponse.
        :type: AddressableEntityRef
        """
        

        self._source = source

    @property
    def readonly(self) -> bool:
        """
        Gets the readonly of this KnowledgeDocumentResponse.
        Whether the document is read-only.

        :return: The readonly of this KnowledgeDocumentResponse.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly: bool) -> None:
        """
        Sets the readonly of this KnowledgeDocumentResponse.
        Whether the document is read-only.

        :param readonly: The readonly of this KnowledgeDocumentResponse.
        :type: bool
        """
        

        self._readonly = readonly

    @property
    def variations(self) -> List['DocumentVariation']:
        """
        Gets the variations of this KnowledgeDocumentResponse.
        Variations of the document.

        :return: The variations of this KnowledgeDocumentResponse.
        :rtype: list[DocumentVariation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations: List['DocumentVariation']) -> None:
        """
        Sets the variations of this KnowledgeDocumentResponse.
        Variations of the document.

        :param variations: The variations of this KnowledgeDocumentResponse.
        :type: list[DocumentVariation]
        """
        

        self._variations = variations

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this KnowledgeDocumentResponse.
        The URI for this object

        :return: The self_uri of this KnowledgeDocumentResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this KnowledgeDocumentResponse.
        The URI for this object

        :param self_uri: The self_uri of this KnowledgeDocumentResponse.
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
