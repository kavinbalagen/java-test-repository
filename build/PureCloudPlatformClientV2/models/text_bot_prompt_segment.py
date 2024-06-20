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
    from . import Format
    from . import MessageContent

class TextBotPromptSegment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TextBotPromptSegment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'text': 'str',
            'type': 'str',
            'format': 'Format',
            'content': 'list[MessageContent]'
        }

        self.attribute_map = {
            'text': 'text',
            'type': 'type',
            'format': 'format',
            'content': 'content'
        }

        self._text = None
        self._type = None
        self._format = None
        self._content = None

    @property
    def text(self) -> str:
        """
        Gets the text of this TextBotPromptSegment.
        The text of this prompt segment.

        :return: The text of this TextBotPromptSegment.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        """
        Sets the text of this TextBotPromptSegment.
        The text of this prompt segment.

        :param text: The text of this TextBotPromptSegment.
        :type: str
        """
        

        self._text = text

    @property
    def type(self) -> str:
        """
        Gets the type of this TextBotPromptSegment.
        The segment type which describes any semantics about the 'text' and also indicates which other field might include additional relevant info.

        :return: The type of this TextBotPromptSegment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this TextBotPromptSegment.
        The segment type which describes any semantics about the 'text' and also indicates which other field might include additional relevant info.

        :param type: The type of this TextBotPromptSegment.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Text", "RichMedia"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def format(self) -> 'Format':
        """
        Gets the format of this TextBotPromptSegment.
        Additional details describing the segment’s contents, which the client should honour where possible.

        :return: The format of this TextBotPromptSegment.
        :rtype: Format
        """
        return self._format

    @format.setter
    def format(self, format: 'Format') -> None:
        """
        Sets the format of this TextBotPromptSegment.
        Additional details describing the segment’s contents, which the client should honour where possible.

        :param format: The format of this TextBotPromptSegment.
        :type: Format
        """
        

        self._format = format

    @property
    def content(self) -> List['MessageContent']:
        """
        Gets the content of this TextBotPromptSegment.
        Details to display Rich Media content. This is only populated when the segment 'type' is 'Rich Media'.

        :return: The content of this TextBotPromptSegment.
        :rtype: list[MessageContent]
        """
        return self._content

    @content.setter
    def content(self, content: List['MessageContent']) -> None:
        """
        Sets the content of this TextBotPromptSegment.
        Details to display Rich Media content. This is only populated when the segment 'type' is 'Rich Media'.

        :param content: The content of this TextBotPromptSegment.
        :type: list[MessageContent]
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

