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
    from . import ConfusionDetails
    from . import OutlierInfo

class FlowHealthUtterance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowHealthUtterance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'text': 'str',
            'issue_count': 'int',
            'language': 'str',
            'static_validation_results': 'list[str]',
            'outlier_info': 'OutlierInfo',
            'confusion_info': 'ConfusionDetails',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'issue_count': 'issueCount',
            'language': 'language',
            'static_validation_results': 'staticValidationResults',
            'outlier_info': 'outlierInfo',
            'confusion_info': 'confusionInfo',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._text = None
        self._issue_count = None
        self._language = None
        self._static_validation_results = None
        self._outlier_info = None
        self._confusion_info = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this FlowHealthUtterance.
        The globally unique identifier for the object.

        :return: The id of this FlowHealthUtterance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this FlowHealthUtterance.
        The globally unique identifier for the object.

        :param id: The id of this FlowHealthUtterance.
        :type: str
        """
        

        self._id = id

    @property
    def text(self) -> str:
        """
        Gets the text of this FlowHealthUtterance.
        Utterance Text.

        :return: The text of this FlowHealthUtterance.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        """
        Sets the text of this FlowHealthUtterance.
        Utterance Text.

        :param text: The text of this FlowHealthUtterance.
        :type: str
        """
        

        self._text = text

    @property
    def issue_count(self) -> int:
        """
        Gets the issue_count of this FlowHealthUtterance.
        Number of issues found for this utterance.

        :return: The issue_count of this FlowHealthUtterance.
        :rtype: int
        """
        return self._issue_count

    @issue_count.setter
    def issue_count(self, issue_count: int) -> None:
        """
        Sets the issue_count of this FlowHealthUtterance.
        Number of issues found for this utterance.

        :param issue_count: The issue_count of this FlowHealthUtterance.
        :type: int
        """
        

        self._issue_count = issue_count

    @property
    def language(self) -> str:
        """
        Gets the language of this FlowHealthUtterance.
        Language provided for this utterance's health.

        :return: The language of this FlowHealthUtterance.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this FlowHealthUtterance.
        Language provided for this utterance's health.

        :param language: The language of this FlowHealthUtterance.
        :type: str
        """
        if isinstance(language, int):
            language = str(language)
        allowed_values = ["en-us", "en-gb", "en-au", "en-za", "en-nz", "en-ie", "fr-ca", "fr-fr", "es-us", "es-es", "es-mx", "de-de", "it-it", "pt-br", "pt-pt", "nl-nl"]
        if language.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for language -> " + language)
            self._language = "outdated_sdk_version"
        else:
            self._language = language

    @property
    def static_validation_results(self) -> List[str]:
        """
        Gets the static_validation_results of this FlowHealthUtterance.
        Validation results for the utterance.

        :return: The static_validation_results of this FlowHealthUtterance.
        :rtype: list[str]
        """
        return self._static_validation_results

    @static_validation_results.setter
    def static_validation_results(self, static_validation_results: List[str]) -> None:
        """
        Sets the static_validation_results of this FlowHealthUtterance.
        Validation results for the utterance.

        :param static_validation_results: The static_validation_results of this FlowHealthUtterance.
        :type: list[str]
        """
        

        self._static_validation_results = static_validation_results

    @property
    def outlier_info(self) -> 'OutlierInfo':
        """
        Gets the outlier_info of this FlowHealthUtterance.
        Details about this utterance being an outlier or not.

        :return: The outlier_info of this FlowHealthUtterance.
        :rtype: OutlierInfo
        """
        return self._outlier_info

    @outlier_info.setter
    def outlier_info(self, outlier_info: 'OutlierInfo') -> None:
        """
        Sets the outlier_info of this FlowHealthUtterance.
        Details about this utterance being an outlier or not.

        :param outlier_info: The outlier_info of this FlowHealthUtterance.
        :type: OutlierInfo
        """
        

        self._outlier_info = outlier_info

    @property
    def confusion_info(self) -> 'ConfusionDetails':
        """
        Gets the confusion_info of this FlowHealthUtterance.
        Confusion details with other utterances.

        :return: The confusion_info of this FlowHealthUtterance.
        :rtype: ConfusionDetails
        """
        return self._confusion_info

    @confusion_info.setter
    def confusion_info(self, confusion_info: 'ConfusionDetails') -> None:
        """
        Sets the confusion_info of this FlowHealthUtterance.
        Confusion details with other utterances.

        :param confusion_info: The confusion_info of this FlowHealthUtterance.
        :type: ConfusionDetails
        """
        

        self._confusion_info = confusion_info

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this FlowHealthUtterance.
        The URI for this object

        :return: The self_uri of this FlowHealthUtterance.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this FlowHealthUtterance.
        The URI for this object

        :param self_uri: The self_uri of this FlowHealthUtterance.
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

