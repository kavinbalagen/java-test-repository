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


class QueueConversationEventTopicErrorDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationEventTopicErrorDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'int',
            'code': 'str',
            'message': 'str',
            'message_with_params': 'str',
            'message_params': 'dict(str, str)',
            'context_id': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'code': 'code',
            'message': 'message',
            'message_with_params': 'messageWithParams',
            'message_params': 'messageParams',
            'context_id': 'contextId',
            'uri': 'uri'
        }

        self._status = None
        self._code = None
        self._message = None
        self._message_with_params = None
        self._message_params = None
        self._context_id = None
        self._uri = None

    @property
    def status(self) -> int:
        """
        Gets the status of this QueueConversationEventTopicErrorDetails.
        The HTTP status code for this message (400, 401, 403, 404, 500, etc.

        :return: The status of this QueueConversationEventTopicErrorDetails.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int) -> None:
        """
        Sets the status of this QueueConversationEventTopicErrorDetails.
        The HTTP status code for this message (400, 401, 403, 404, 500, etc.

        :param status: The status of this QueueConversationEventTopicErrorDetails.
        :type: int
        """
        

        self._status = status

    @property
    def code(self) -> str:
        """
        Gets the code of this QueueConversationEventTopicErrorDetails.
        A code unique to this error.

        :return: The code of this QueueConversationEventTopicErrorDetails.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str) -> None:
        """
        Sets the code of this QueueConversationEventTopicErrorDetails.
        A code unique to this error.

        :param code: The code of this QueueConversationEventTopicErrorDetails.
        :type: str
        """
        

        self._code = code

    @property
    def message(self) -> str:
        """
        Gets the message of this QueueConversationEventTopicErrorDetails.
        Friendly description of this error.

        :return: The message of this QueueConversationEventTopicErrorDetails.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        """
        Sets the message of this QueueConversationEventTopicErrorDetails.
        Friendly description of this error.

        :param message: The message of this QueueConversationEventTopicErrorDetails.
        :type: str
        """
        

        self._message = message

    @property
    def message_with_params(self) -> str:
        """
        Gets the message_with_params of this QueueConversationEventTopicErrorDetails.
        This is the same as message except it uses template fields for variable replacement. For instance: 'User {username} was not found'

        :return: The message_with_params of this QueueConversationEventTopicErrorDetails.
        :rtype: str
        """
        return self._message_with_params

    @message_with_params.setter
    def message_with_params(self, message_with_params: str) -> None:
        """
        Sets the message_with_params of this QueueConversationEventTopicErrorDetails.
        This is the same as message except it uses template fields for variable replacement. For instance: 'User {username} was not found'

        :param message_with_params: The message_with_params of this QueueConversationEventTopicErrorDetails.
        :type: str
        """
        

        self._message_with_params = message_with_params

    @property
    def message_params(self) -> Dict[str, str]:
        """
        Gets the message_params of this QueueConversationEventTopicErrorDetails.
        Used in conjunction with messageWithParams. These are the template parameters. For instance: UserParam.key = 'username', UserParam.value = 'john.doe'

        :return: The message_params of this QueueConversationEventTopicErrorDetails.
        :rtype: dict(str, str)
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params: Dict[str, str]) -> None:
        """
        Sets the message_params of this QueueConversationEventTopicErrorDetails.
        Used in conjunction with messageWithParams. These are the template parameters. For instance: UserParam.key = 'username', UserParam.value = 'john.doe'

        :param message_params: The message_params of this QueueConversationEventTopicErrorDetails.
        :type: dict(str, str)
        """
        

        self._message_params = message_params

    @property
    def context_id(self) -> str:
        """
        Gets the context_id of this QueueConversationEventTopicErrorDetails.
        The correlation Id or context Id for this message. If left blank the Public API will look at the HTTP response header 'ININ-Correlation-Id' instead.

        :return: The context_id of this QueueConversationEventTopicErrorDetails.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id: str) -> None:
        """
        Sets the context_id of this QueueConversationEventTopicErrorDetails.
        The correlation Id or context Id for this message. If left blank the Public API will look at the HTTP response header 'ININ-Correlation-Id' instead.

        :param context_id: The context_id of this QueueConversationEventTopicErrorDetails.
        :type: str
        """
        

        self._context_id = context_id

    @property
    def uri(self) -> str:
        """
        Gets the uri of this QueueConversationEventTopicErrorDetails.


        :return: The uri of this QueueConversationEventTopicErrorDetails.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri: str) -> None:
        """
        Sets the uri of this QueueConversationEventTopicErrorDetails.


        :param uri: The uri of this QueueConversationEventTopicErrorDetails.
        :type: str
        """
        

        self._uri = uri

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

