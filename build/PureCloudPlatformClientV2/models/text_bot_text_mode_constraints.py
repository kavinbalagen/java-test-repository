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


class TextBotTextModeConstraints(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TextBotTextModeConstraints - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'language_preferences': 'list[str]',
            'no_input_timeout_milliseconds': 'int'
        }

        self.attribute_map = {
            'language_preferences': 'languagePreferences',
            'no_input_timeout_milliseconds': 'noInputTimeoutMilliseconds'
        }

        self._language_preferences = None
        self._no_input_timeout_milliseconds = None

    @property
    def language_preferences(self) -> List[str]:
        """
        Gets the language_preferences of this TextBotTextModeConstraints.
        The list of language preferences by their ISO language code.

        :return: The language_preferences of this TextBotTextModeConstraints.
        :rtype: list[str]
        """
        return self._language_preferences

    @language_preferences.setter
    def language_preferences(self, language_preferences: List[str]) -> None:
        """
        Sets the language_preferences of this TextBotTextModeConstraints.
        The list of language preferences by their ISO language code.

        :param language_preferences: The language_preferences of this TextBotTextModeConstraints.
        :type: list[str]
        """
        

        self._language_preferences = language_preferences

    @property
    def no_input_timeout_milliseconds(self) -> int:
        """
        Gets the no_input_timeout_milliseconds of this TextBotTextModeConstraints.
        The amount of time, in milliseconds, before the client should send the 'NoInput' event  to trigger the \"no input\" bot response and handling on digital channels.  Note: This optional field will only be returned for 'Digital Bot Flow' turns.

        :return: The no_input_timeout_milliseconds of this TextBotTextModeConstraints.
        :rtype: int
        """
        return self._no_input_timeout_milliseconds

    @no_input_timeout_milliseconds.setter
    def no_input_timeout_milliseconds(self, no_input_timeout_milliseconds: int) -> None:
        """
        Sets the no_input_timeout_milliseconds of this TextBotTextModeConstraints.
        The amount of time, in milliseconds, before the client should send the 'NoInput' event  to trigger the \"no input\" bot response and handling on digital channels.  Note: This optional field will only be returned for 'Digital Bot Flow' turns.

        :param no_input_timeout_milliseconds: The no_input_timeout_milliseconds of this TextBotTextModeConstraints.
        :type: int
        """
        

        self._no_input_timeout_milliseconds = no_input_timeout_milliseconds

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

