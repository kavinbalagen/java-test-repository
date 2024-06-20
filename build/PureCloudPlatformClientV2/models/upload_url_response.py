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


class UploadUrlResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        UploadUrlResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'upload_key': 'str',
            'headers': 'dict(str, str)'
        }

        self.attribute_map = {
            'url': 'url',
            'upload_key': 'uploadKey',
            'headers': 'headers'
        }

        self._url = None
        self._upload_key = None
        self._headers = None

    @property
    def url(self) -> str:
        """
        Gets the url of this UploadUrlResponse.
        Presigned URL to PUT the file to

        :return: The url of this UploadUrlResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        """
        Sets the url of this UploadUrlResponse.
        Presigned URL to PUT the file to

        :param url: The url of this UploadUrlResponse.
        :type: str
        """
        

        self._url = url

    @property
    def upload_key(self) -> str:
        """
        Gets the upload_key of this UploadUrlResponse.
        Key that identifies the file in the storage including the file name

        :return: The upload_key of this UploadUrlResponse.
        :rtype: str
        """
        return self._upload_key

    @upload_key.setter
    def upload_key(self, upload_key: str) -> None:
        """
        Sets the upload_key of this UploadUrlResponse.
        Key that identifies the file in the storage including the file name

        :param upload_key: The upload_key of this UploadUrlResponse.
        :type: str
        """
        

        self._upload_key = upload_key

    @property
    def headers(self) -> Dict[str, str]:
        """
        Gets the headers of this UploadUrlResponse.
        Required headers when uploading a file through PUT request to the URL

        :return: The headers of this UploadUrlResponse.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers: Dict[str, str]) -> None:
        """
        Sets the headers of this UploadUrlResponse.
        Required headers when uploading a file through PUT request to the URL

        :param headers: The headers of this UploadUrlResponse.
        :type: dict(str, str)
        """
        

        self._headers = headers

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

