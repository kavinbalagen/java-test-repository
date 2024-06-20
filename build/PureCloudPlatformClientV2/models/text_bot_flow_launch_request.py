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
    from . import TextBotChannel
    from . import TextBotFlow
    from . import TextBotInputOutputData

class TextBotFlowLaunchRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TextBotFlowLaunchRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'flow': 'TextBotFlow',
            'external_session_id': 'str',
            'conversation_id': 'str',
            'input_data': 'TextBotInputOutputData',
            'channel': 'TextBotChannel',
            'language': 'str'
        }

        self.attribute_map = {
            'flow': 'flow',
            'external_session_id': 'externalSessionId',
            'conversation_id': 'conversationId',
            'input_data': 'inputData',
            'channel': 'channel',
            'language': 'language'
        }

        self._flow = None
        self._external_session_id = None
        self._conversation_id = None
        self._input_data = None
        self._channel = None
        self._language = None

    @property
    def flow(self) -> 'TextBotFlow':
        """
        Gets the flow of this TextBotFlowLaunchRequest.
        Specifies which Bot Flow to launch.

        :return: The flow of this TextBotFlowLaunchRequest.
        :rtype: TextBotFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow: 'TextBotFlow') -> None:
        """
        Sets the flow of this TextBotFlowLaunchRequest.
        Specifies which Bot Flow to launch.

        :param flow: The flow of this TextBotFlowLaunchRequest.
        :type: TextBotFlow
        """
        

        self._flow = flow

    @property
    def external_session_id(self) -> str:
        """
        Gets the external_session_id of this TextBotFlowLaunchRequest.
        The ID of the external session that is associated with the bot flow.

        :return: The external_session_id of this TextBotFlowLaunchRequest.
        :rtype: str
        """
        return self._external_session_id

    @external_session_id.setter
    def external_session_id(self, external_session_id: str) -> None:
        """
        Sets the external_session_id of this TextBotFlowLaunchRequest.
        The ID of the external session that is associated with the bot flow.

        :param external_session_id: The external_session_id of this TextBotFlowLaunchRequest.
        :type: str
        """
        

        self._external_session_id = external_session_id

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this TextBotFlowLaunchRequest.
        A conversation ID to associate with the bot flow, if available.

        :return: The conversation_id of this TextBotFlowLaunchRequest.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this TextBotFlowLaunchRequest.
        A conversation ID to associate with the bot flow, if available.

        :param conversation_id: The conversation_id of this TextBotFlowLaunchRequest.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def input_data(self) -> 'TextBotInputOutputData':
        """
        Gets the input_data of this TextBotFlowLaunchRequest.
        Input values to the flow. Valid values are defined by the flow's input JSON schema.

        :return: The input_data of this TextBotFlowLaunchRequest.
        :rtype: TextBotInputOutputData
        """
        return self._input_data

    @input_data.setter
    def input_data(self, input_data: 'TextBotInputOutputData') -> None:
        """
        Sets the input_data of this TextBotFlowLaunchRequest.
        Input values to the flow. Valid values are defined by the flow's input JSON schema.

        :param input_data: The input_data of this TextBotFlowLaunchRequest.
        :type: TextBotInputOutputData
        """
        

        self._input_data = input_data

    @property
    def channel(self) -> 'TextBotChannel':
        """
        Gets the channel of this TextBotFlowLaunchRequest.
        Channel information relevant to the bot flow.

        :return: The channel of this TextBotFlowLaunchRequest.
        :rtype: TextBotChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel: 'TextBotChannel') -> None:
        """
        Sets the channel of this TextBotFlowLaunchRequest.
        Channel information relevant to the bot flow.

        :param channel: The channel of this TextBotFlowLaunchRequest.
        :type: TextBotChannel
        """
        

        self._channel = channel

    @property
    def language(self) -> str:
        """
        Gets the language of this TextBotFlowLaunchRequest.
        The language that the bot will use in the session. Validated against list of supported languages and if the value is omitted or is invalid, the default language will be used.

        :return: The language of this TextBotFlowLaunchRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        """
        Sets the language of this TextBotFlowLaunchRequest.
        The language that the bot will use in the session. Validated against list of supported languages and if the value is omitted or is invalid, the default language will be used.

        :param language: The language of this TextBotFlowLaunchRequest.
        :type: str
        """
        

        self._language = language

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

