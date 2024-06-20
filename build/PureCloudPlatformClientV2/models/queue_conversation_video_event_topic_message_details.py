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
    from . import QueueConversationVideoEventTopicErrorDetails
    from . import QueueConversationVideoEventTopicMessageMedia
    from . import QueueConversationVideoEventTopicMessageMetadata
    from . import QueueConversationVideoEventTopicMessageSticker

class QueueConversationVideoEventTopicMessageDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationVideoEventTopicMessageDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message_id': 'str',
            'message_time': 'datetime',
            'message_status': 'str',
            'message_segment_count': 'int',
            'media': 'list[QueueConversationVideoEventTopicMessageMedia]',
            'error_info': 'QueueConversationVideoEventTopicErrorDetails',
            'stickers': 'list[QueueConversationVideoEventTopicMessageSticker]',
            'message_metadata': 'QueueConversationVideoEventTopicMessageMetadata'
        }

        self.attribute_map = {
            'message_id': 'messageId',
            'message_time': 'messageTime',
            'message_status': 'messageStatus',
            'message_segment_count': 'messageSegmentCount',
            'media': 'media',
            'error_info': 'errorInfo',
            'stickers': 'stickers',
            'message_metadata': 'messageMetadata'
        }

        self._message_id = None
        self._message_time = None
        self._message_status = None
        self._message_segment_count = None
        self._media = None
        self._error_info = None
        self._stickers = None
        self._message_metadata = None

    @property
    def message_id(self) -> str:
        """
        Gets the message_id of this QueueConversationVideoEventTopicMessageDetails.
        UUID identifying the message media.

        :return: The message_id of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: str) -> None:
        """
        Sets the message_id of this QueueConversationVideoEventTopicMessageDetails.
        UUID identifying the message media.

        :param message_id: The message_id of this QueueConversationVideoEventTopicMessageDetails.
        :type: str
        """
        

        self._message_id = message_id

    @property
    def message_time(self) -> datetime:
        """
        Gets the message_time of this QueueConversationVideoEventTopicMessageDetails.
        The time when the message was sent or received.

        :return: The message_time of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: datetime
        """
        return self._message_time

    @message_time.setter
    def message_time(self, message_time: datetime) -> None:
        """
        Sets the message_time of this QueueConversationVideoEventTopicMessageDetails.
        The time when the message was sent or received.

        :param message_time: The message_time of this QueueConversationVideoEventTopicMessageDetails.
        :type: datetime
        """
        

        self._message_time = message_time

    @property
    def message_status(self) -> str:
        """
        Gets the message_status of this QueueConversationVideoEventTopicMessageDetails.
        Indicates the delivery status of the message.

        :return: The message_status of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: str
        """
        return self._message_status

    @message_status.setter
    def message_status(self, message_status: str) -> None:
        """
        Sets the message_status of this QueueConversationVideoEventTopicMessageDetails.
        Indicates the delivery status of the message.

        :param message_status: The message_status of this QueueConversationVideoEventTopicMessageDetails.
        :type: str
        """
        if isinstance(message_status, int):
            message_status = str(message_status)
        allowed_values = ["queued", "sent", "failed", "received", "delivery-success", "delivery-failed", "read", "removed", "published"]
        if message_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for message_status -> " + message_status)
            self._message_status = "outdated_sdk_version"
        else:
            self._message_status = message_status

    @property
    def message_segment_count(self) -> int:
        """
        Gets the message_segment_count of this QueueConversationVideoEventTopicMessageDetails.
        The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits.

        :return: The message_segment_count of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: int
        """
        return self._message_segment_count

    @message_segment_count.setter
    def message_segment_count(self, message_segment_count: int) -> None:
        """
        Sets the message_segment_count of this QueueConversationVideoEventTopicMessageDetails.
        The message segment count, greater than 1 if the message content was split into multiple parts for this message type, e.g. SMS character limits.

        :param message_segment_count: The message_segment_count of this QueueConversationVideoEventTopicMessageDetails.
        :type: int
        """
        

        self._message_segment_count = message_segment_count

    @property
    def media(self) -> List['QueueConversationVideoEventTopicMessageMedia']:
        """
        Gets the media of this QueueConversationVideoEventTopicMessageDetails.
        The media (images, files, etc) associated with this message, if any

        :return: The media of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: list[QueueConversationVideoEventTopicMessageMedia]
        """
        return self._media

    @media.setter
    def media(self, media: List['QueueConversationVideoEventTopicMessageMedia']) -> None:
        """
        Sets the media of this QueueConversationVideoEventTopicMessageDetails.
        The media (images, files, etc) associated with this message, if any

        :param media: The media of this QueueConversationVideoEventTopicMessageDetails.
        :type: list[QueueConversationVideoEventTopicMessageMedia]
        """
        

        self._media = media

    @property
    def error_info(self) -> 'QueueConversationVideoEventTopicErrorDetails':
        """
        Gets the error_info of this QueueConversationVideoEventTopicMessageDetails.
        Detailed information about an error response.

        :return: The error_info of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: QueueConversationVideoEventTopicErrorDetails
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info: 'QueueConversationVideoEventTopicErrorDetails') -> None:
        """
        Sets the error_info of this QueueConversationVideoEventTopicMessageDetails.
        Detailed information about an error response.

        :param error_info: The error_info of this QueueConversationVideoEventTopicMessageDetails.
        :type: QueueConversationVideoEventTopicErrorDetails
        """
        

        self._error_info = error_info

    @property
    def stickers(self) -> List['QueueConversationVideoEventTopicMessageSticker']:
        """
        Gets the stickers of this QueueConversationVideoEventTopicMessageDetails.
        A list of stickers included in the message

        :return: The stickers of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: list[QueueConversationVideoEventTopicMessageSticker]
        """
        return self._stickers

    @stickers.setter
    def stickers(self, stickers: List['QueueConversationVideoEventTopicMessageSticker']) -> None:
        """
        Sets the stickers of this QueueConversationVideoEventTopicMessageDetails.
        A list of stickers included in the message

        :param stickers: The stickers of this QueueConversationVideoEventTopicMessageDetails.
        :type: list[QueueConversationVideoEventTopicMessageSticker]
        """
        

        self._stickers = stickers

    @property
    def message_metadata(self) -> 'QueueConversationVideoEventTopicMessageMetadata':
        """
        Gets the message_metadata of this QueueConversationVideoEventTopicMessageDetails.


        :return: The message_metadata of this QueueConversationVideoEventTopicMessageDetails.
        :rtype: QueueConversationVideoEventTopicMessageMetadata
        """
        return self._message_metadata

    @message_metadata.setter
    def message_metadata(self, message_metadata: 'QueueConversationVideoEventTopicMessageMetadata') -> None:
        """
        Sets the message_metadata of this QueueConversationVideoEventTopicMessageDetails.


        :param message_metadata: The message_metadata of this QueueConversationVideoEventTopicMessageDetails.
        :type: QueueConversationVideoEventTopicMessageMetadata
        """
        

        self._message_metadata = message_metadata

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

