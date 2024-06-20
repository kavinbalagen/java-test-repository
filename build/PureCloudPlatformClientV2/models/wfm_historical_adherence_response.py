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
    from . import WfmHistoricalAdherenceResultWrapper

class WfmHistoricalAdherenceResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmHistoricalAdherenceResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'download_url': 'str',
            'download_result': 'WfmHistoricalAdherenceResultWrapper',
            'download_urls': 'list[str]',
            'query_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'download_url': 'downloadUrl',
            'download_result': 'downloadResult',
            'download_urls': 'downloadUrls',
            'query_state': 'queryState'
        }

        self._id = None
        self._download_url = None
        self._download_result = None
        self._download_urls = None
        self._query_state = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WfmHistoricalAdherenceResponse.
        The query ID to listen for

        :return: The id of this WfmHistoricalAdherenceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WfmHistoricalAdherenceResponse.
        The query ID to listen for

        :param id: The id of this WfmHistoricalAdherenceResponse.
        :type: str
        """
        

        self._id = id

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this WfmHistoricalAdherenceResponse.
        Deprecated. Use downloadUrls instead.

        :return: The download_url of this WfmHistoricalAdherenceResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this WfmHistoricalAdherenceResponse.
        Deprecated. Use downloadUrls instead.

        :param download_url: The download_url of this WfmHistoricalAdherenceResponse.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def download_result(self) -> 'WfmHistoricalAdherenceResultWrapper':
        """
        Gets the download_result of this WfmHistoricalAdherenceResponse.
        Result will always come via downloadUrls; however the schema is included for documentation

        :return: The download_result of this WfmHistoricalAdherenceResponse.
        :rtype: WfmHistoricalAdherenceResultWrapper
        """
        return self._download_result

    @download_result.setter
    def download_result(self, download_result: 'WfmHistoricalAdherenceResultWrapper') -> None:
        """
        Sets the download_result of this WfmHistoricalAdherenceResponse.
        Result will always come via downloadUrls; however the schema is included for documentation

        :param download_result: The download_result of this WfmHistoricalAdherenceResponse.
        :type: WfmHistoricalAdherenceResultWrapper
        """
        

        self._download_result = download_result

    @property
    def download_urls(self) -> List[str]:
        """
        Gets the download_urls of this WfmHistoricalAdherenceResponse.
        The uri list to GET the results of the Historical Adherence query. For notification purposes only

        :return: The download_urls of this WfmHistoricalAdherenceResponse.
        :rtype: list[str]
        """
        return self._download_urls

    @download_urls.setter
    def download_urls(self, download_urls: List[str]) -> None:
        """
        Sets the download_urls of this WfmHistoricalAdherenceResponse.
        The uri list to GET the results of the Historical Adherence query. For notification purposes only

        :param download_urls: The download_urls of this WfmHistoricalAdherenceResponse.
        :type: list[str]
        """
        

        self._download_urls = download_urls

    @property
    def query_state(self) -> str:
        """
        Gets the query_state of this WfmHistoricalAdherenceResponse.
        The state of the adherence query

        :return: The query_state of this WfmHistoricalAdherenceResponse.
        :rtype: str
        """
        return self._query_state

    @query_state.setter
    def query_state(self, query_state: str) -> None:
        """
        Sets the query_state of this WfmHistoricalAdherenceResponse.
        The state of the adherence query

        :param query_state: The query_state of this WfmHistoricalAdherenceResponse.
        :type: str
        """
        if isinstance(query_state, int):
            query_state = str(query_state)
        allowed_values = ["Processing", "Complete", "Error"]
        if query_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for query_state -> " + query_state)
            self._query_state = "outdated_sdk_version"
        else:
            self._query_state = query_state

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

