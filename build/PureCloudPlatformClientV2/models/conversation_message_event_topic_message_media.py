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


class ConversationMessageEventTopicMessageMedia(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationMessageEventTopicMessageMedia - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'media_type': 'str',
            'content_length_bytes': 'int',
            'name': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'media_type': 'mediaType',
            'content_length_bytes': 'contentLengthBytes',
            'name': 'name',
            'id': 'id'
        }

        self._url = None
        self._media_type = None
        self._content_length_bytes = None
        self._name = None
        self._id = None

    @property
    def url(self) -> str:
        """
        Gets the url of this ConversationMessageEventTopicMessageMedia.
        The location of the media, useful for retrieving it

        :return: The url of this ConversationMessageEventTopicMessageMedia.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        """
        Sets the url of this ConversationMessageEventTopicMessageMedia.
        The location of the media, useful for retrieving it

        :param url: The url of this ConversationMessageEventTopicMessageMedia.
        :type: str
        """
        

        self._url = url

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this ConversationMessageEventTopicMessageMedia.
        The optional internet media type of the the media object.  If null then the media type should be dictated by the url

        :return: The media_type of this ConversationMessageEventTopicMessageMedia.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this ConversationMessageEventTopicMessageMedia.
        The optional internet media type of the the media object.  If null then the media type should be dictated by the url

        :param media_type: The media_type of this ConversationMessageEventTopicMessageMedia.
        :type: str
        """
        

        self._media_type = media_type

    @property
    def content_length_bytes(self) -> int:
        """
        Gets the content_length_bytes of this ConversationMessageEventTopicMessageMedia.
        The optional content length of the the media object, in bytes.

        :return: The content_length_bytes of this ConversationMessageEventTopicMessageMedia.
        :rtype: int
        """
        return self._content_length_bytes

    @content_length_bytes.setter
    def content_length_bytes(self, content_length_bytes: int) -> None:
        """
        Sets the content_length_bytes of this ConversationMessageEventTopicMessageMedia.
        The optional content length of the the media object, in bytes.

        :param content_length_bytes: The content_length_bytes of this ConversationMessageEventTopicMessageMedia.
        :type: int
        """
        

        self._content_length_bytes = content_length_bytes

    @property
    def name(self) -> str:
        """
        Gets the name of this ConversationMessageEventTopicMessageMedia.
        The optional name of the the media object.

        :return: The name of this ConversationMessageEventTopicMessageMedia.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this ConversationMessageEventTopicMessageMedia.
        The optional name of the the media object.

        :param name: The name of this ConversationMessageEventTopicMessageMedia.
        :type: str
        """
        

        self._name = name

    @property
    def id(self) -> str:
        """
        Gets the id of this ConversationMessageEventTopicMessageMedia.
        The optional id of the the media object.

        :return: The id of this ConversationMessageEventTopicMessageMedia.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationMessageEventTopicMessageMedia.
        The optional id of the the media object.

        :param id: The id of this ConversationMessageEventTopicMessageMedia.
        :type: str
        """
        

        self._id = id

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

