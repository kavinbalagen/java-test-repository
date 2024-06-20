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
    from . import DocumentArticle
    from . import DocumentFaq
    from . import KnowledgeBase
    from . import KnowledgeCategory

class KnowledgeSearchDocumentV1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeSearchDocumentV1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'language_code': 'str',
            'type': 'str',
            'faq': 'DocumentFaq',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'categories': 'list[KnowledgeCategory]',
            'knowledge_base': 'KnowledgeBase',
            'external_url': 'str',
            'article': 'DocumentArticle',
            'confidence': 'float',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'language_code': 'languageCode',
            'type': 'type',
            'faq': 'faq',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'categories': 'categories',
            'knowledge_base': 'knowledgeBase',
            'external_url': 'externalUrl',
            'article': 'article',
            'confidence': 'confidence',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._language_code = None
        self._type = None
        self._faq = None
        self._date_created = None
        self._date_modified = None
        self._categories = None
        self._knowledge_base = None
        self._external_url = None
        self._article = None
        self._confidence = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this KnowledgeSearchDocumentV1.
        The globally unique identifier for the object.

        :return: The id of this KnowledgeSearchDocumentV1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this KnowledgeSearchDocumentV1.
        The globally unique identifier for the object.

        :param id: The id of this KnowledgeSearchDocumentV1.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this KnowledgeSearchDocumentV1.


        :return: The name of this KnowledgeSearchDocumentV1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this KnowledgeSearchDocumentV1.


        :param name: The name of this KnowledgeSearchDocumentV1.
        :type: str
        """
        

        self._name = name

    @property
    def language_code(self) -> str:
        """
        Gets the language_code of this KnowledgeSearchDocumentV1.
        Language of the document

        :return: The language_code of this KnowledgeSearchDocumentV1.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code: str) -> None:
        """
        Sets the language_code of this KnowledgeSearchDocumentV1.
        Language of the document

        :param language_code: The language_code of this KnowledgeSearchDocumentV1.
        :type: str
        """
        if isinstance(language_code, int):
            language_code = str(language_code)
        allowed_values = ["en-US", "en-UK", "en-AU", "en-CA", "en-HK", "en-IN", "en-IE", "en-NZ", "en-PH", "en-SG", "en-ZA", "de-DE", "de-AT", "de-CH", "es-AR", "es-CO", "es-MX", "es-US", "es-ES", "fr-FR", "fr-BE", "fr-CA", "fr-CH", "pt-BR", "pt-PT", "nl-NL", "nl-BE", "it-IT", "ca-ES", "tr-TR", "sv-SE", "fi-FI", "nb-NO", "da-DK", "ja-JP", "ar-AE", "zh-CN", "zh-TW", "zh-HK", "ko-KR", "pl-PL", "hi-IN", "th-TH", "hu-HU", "vi-VN", "uk-UA"]
        if language_code.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for language_code -> " + language_code)
            self._language_code = "outdated_sdk_version"
        else:
            self._language_code = language_code

    @property
    def type(self) -> str:
        """
        Gets the type of this KnowledgeSearchDocumentV1.
        Document type

        :return: The type of this KnowledgeSearchDocumentV1.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this KnowledgeSearchDocumentV1.
        Document type

        :param type: The type of this KnowledgeSearchDocumentV1.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Faq", "Article"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def faq(self) -> 'DocumentFaq':
        """
        Gets the faq of this KnowledgeSearchDocumentV1.
        FAQ document details

        :return: The faq of this KnowledgeSearchDocumentV1.
        :rtype: DocumentFaq
        """
        return self._faq

    @faq.setter
    def faq(self, faq: 'DocumentFaq') -> None:
        """
        Sets the faq of this KnowledgeSearchDocumentV1.
        FAQ document details

        :param faq: The faq of this KnowledgeSearchDocumentV1.
        :type: DocumentFaq
        """
        

        self._faq = faq

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this KnowledgeSearchDocumentV1.
        Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this KnowledgeSearchDocumentV1.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this KnowledgeSearchDocumentV1.
        Document creation date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this KnowledgeSearchDocumentV1.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this KnowledgeSearchDocumentV1.
        Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this KnowledgeSearchDocumentV1.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this KnowledgeSearchDocumentV1.
        Document last modification date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this KnowledgeSearchDocumentV1.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def categories(self) -> List['KnowledgeCategory']:
        """
        Gets the categories of this KnowledgeSearchDocumentV1.
        Document categories

        :return: The categories of this KnowledgeSearchDocumentV1.
        :rtype: list[KnowledgeCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List['KnowledgeCategory']) -> None:
        """
        Sets the categories of this KnowledgeSearchDocumentV1.
        Document categories

        :param categories: The categories of this KnowledgeSearchDocumentV1.
        :type: list[KnowledgeCategory]
        """
        

        self._categories = categories

    @property
    def knowledge_base(self) -> 'KnowledgeBase':
        """
        Gets the knowledge_base of this KnowledgeSearchDocumentV1.
        Knowledge base which document does belong to

        :return: The knowledge_base of this KnowledgeSearchDocumentV1.
        :rtype: KnowledgeBase
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base: 'KnowledgeBase') -> None:
        """
        Sets the knowledge_base of this KnowledgeSearchDocumentV1.
        Knowledge base which document does belong to

        :param knowledge_base: The knowledge_base of this KnowledgeSearchDocumentV1.
        :type: KnowledgeBase
        """
        

        self._knowledge_base = knowledge_base

    @property
    def external_url(self) -> str:
        """
        Gets the external_url of this KnowledgeSearchDocumentV1.
        External URL to the document

        :return: The external_url of this KnowledgeSearchDocumentV1.
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url: str) -> None:
        """
        Sets the external_url of this KnowledgeSearchDocumentV1.
        External URL to the document

        :param external_url: The external_url of this KnowledgeSearchDocumentV1.
        :type: str
        """
        

        self._external_url = external_url

    @property
    def article(self) -> 'DocumentArticle':
        """
        Gets the article of this KnowledgeSearchDocumentV1.
        Article

        :return: The article of this KnowledgeSearchDocumentV1.
        :rtype: DocumentArticle
        """
        return self._article

    @article.setter
    def article(self, article: 'DocumentArticle') -> None:
        """
        Sets the article of this KnowledgeSearchDocumentV1.
        Article

        :param article: The article of this KnowledgeSearchDocumentV1.
        :type: DocumentArticle
        """
        

        self._article = article

    @property
    def confidence(self) -> float:
        """
        Gets the confidence of this KnowledgeSearchDocumentV1.
        The confidence associated with a document with respect to a search query

        :return: The confidence of this KnowledgeSearchDocumentV1.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: float) -> None:
        """
        Sets the confidence of this KnowledgeSearchDocumentV1.
        The confidence associated with a document with respect to a search query

        :param confidence: The confidence of this KnowledgeSearchDocumentV1.
        :type: float
        """
        

        self._confidence = confidence

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this KnowledgeSearchDocumentV1.
        The URI for this object

        :return: The self_uri of this KnowledgeSearchDocumentV1.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this KnowledgeSearchDocumentV1.
        The URI for this object

        :param self_uri: The self_uri of this KnowledgeSearchDocumentV1.
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
