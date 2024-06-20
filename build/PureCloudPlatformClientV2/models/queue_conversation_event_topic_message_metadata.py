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
    from . import QueueConversationEventTopicMessageMetadataContent
    from . import QueueConversationEventTopicMessageMetadataEvent

class QueueConversationEventTopicMessageMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationEventTopicMessageMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'events': 'list[QueueConversationEventTopicMessageMetadataEvent]',
            'content': 'list[QueueConversationEventTopicMessageMetadataContent]'
        }

        self.attribute_map = {
            'type': 'type',
            'events': 'events',
            'content': 'content'
        }

        self._type = None
        self._events = None
        self._content = None

    @property
    def type(self) -> str:
        """
        Gets the type of this QueueConversationEventTopicMessageMetadata.
        Message type.

        :return: The type of this QueueConversationEventTopicMessageMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this QueueConversationEventTopicMessageMetadata.
        Message type.

        :param type: The type of this QueueConversationEventTopicMessageMetadata.
        :type: str
        """
        

        self._type = type

    @property
    def events(self) -> List['QueueConversationEventTopicMessageMetadataEvent']:
        """
        Gets the events of this QueueConversationEventTopicMessageMetadata.
        List of message events, if any

        :return: The events of this QueueConversationEventTopicMessageMetadata.
        :rtype: list[QueueConversationEventTopicMessageMetadataEvent]
        """
        return self._events

    @events.setter
    def events(self, events: List['QueueConversationEventTopicMessageMetadataEvent']) -> None:
        """
        Sets the events of this QueueConversationEventTopicMessageMetadata.
        List of message events, if any

        :param events: The events of this QueueConversationEventTopicMessageMetadata.
        :type: list[QueueConversationEventTopicMessageMetadataEvent]
        """
        

        self._events = events

    @property
    def content(self) -> List['QueueConversationEventTopicMessageMetadataContent']:
        """
        Gets the content of this QueueConversationEventTopicMessageMetadata.
        List of message content, if any

        :return: The content of this QueueConversationEventTopicMessageMetadata.
        :rtype: list[QueueConversationEventTopicMessageMetadataContent]
        """
        return self._content

    @content.setter
    def content(self, content: List['QueueConversationEventTopicMessageMetadataContent']) -> None:
        """
        Sets the content of this QueueConversationEventTopicMessageMetadata.
        List of message content, if any

        :param content: The content of this QueueConversationEventTopicMessageMetadata.
        :type: list[QueueConversationEventTopicMessageMetadataContent]
        """
        

        self._content = content

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

