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
    from . import DomainEntityRef
    from . import SmsPhoneNumberRef

class SmsConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SmsConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message_column': 'str',
            'phone_column': 'str',
            'sender_sms_phone_number': 'SmsPhoneNumberRef',
            'content_template': 'DomainEntityRef'
        }

        self.attribute_map = {
            'message_column': 'messageColumn',
            'phone_column': 'phoneColumn',
            'sender_sms_phone_number': 'senderSmsPhoneNumber',
            'content_template': 'contentTemplate'
        }

        self._message_column = None
        self._phone_column = None
        self._sender_sms_phone_number = None
        self._content_template = None

    @property
    def message_column(self) -> str:
        """
        Gets the message_column of this SmsConfig.
        The Contact List column specifying the message to send to the contact.

        :return: The message_column of this SmsConfig.
        :rtype: str
        """
        return self._message_column

    @message_column.setter
    def message_column(self, message_column: str) -> None:
        """
        Sets the message_column of this SmsConfig.
        The Contact List column specifying the message to send to the contact.

        :param message_column: The message_column of this SmsConfig.
        :type: str
        """
        

        self._message_column = message_column

    @property
    def phone_column(self) -> str:
        """
        Gets the phone_column of this SmsConfig.
        The Contact List column specifying the phone number to send a message to.

        :return: The phone_column of this SmsConfig.
        :rtype: str
        """
        return self._phone_column

    @phone_column.setter
    def phone_column(self, phone_column: str) -> None:
        """
        Sets the phone_column of this SmsConfig.
        The Contact List column specifying the phone number to send a message to.

        :param phone_column: The phone_column of this SmsConfig.
        :type: str
        """
        

        self._phone_column = phone_column

    @property
    def sender_sms_phone_number(self) -> 'SmsPhoneNumberRef':
        """
        Gets the sender_sms_phone_number of this SmsConfig.
        A reference to the SMS Phone Number that will be used as the sender of a message.

        :return: The sender_sms_phone_number of this SmsConfig.
        :rtype: SmsPhoneNumberRef
        """
        return self._sender_sms_phone_number

    @sender_sms_phone_number.setter
    def sender_sms_phone_number(self, sender_sms_phone_number: 'SmsPhoneNumberRef') -> None:
        """
        Sets the sender_sms_phone_number of this SmsConfig.
        A reference to the SMS Phone Number that will be used as the sender of a message.

        :param sender_sms_phone_number: The sender_sms_phone_number of this SmsConfig.
        :type: SmsPhoneNumberRef
        """
        

        self._sender_sms_phone_number = sender_sms_phone_number

    @property
    def content_template(self) -> 'DomainEntityRef':
        """
        Gets the content_template of this SmsConfig.
        The content template used to formulate the message to send to the contact.

        :return: The content_template of this SmsConfig.
        :rtype: DomainEntityRef
        """
        return self._content_template

    @content_template.setter
    def content_template(self, content_template: 'DomainEntityRef') -> None:
        """
        Sets the content_template of this SmsConfig.
        The content template used to formulate the message to send to the contact.

        :param content_template: The content_template of this SmsConfig.
        :type: DomainEntityRef
        """
        

        self._content_template = content_template

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

