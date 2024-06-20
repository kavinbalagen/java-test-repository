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
    from . import MessagingTemplateRequest

class SendAgentlessOutboundMessageRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        SendAgentlessOutboundMessageRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'from_address': 'str',
            'to_address': 'str',
            'to_address_messenger_type': 'str',
            'text_body': 'str',
            'messaging_template': 'MessagingTemplateRequest',
            'use_existing_active_conversation': 'bool'
        }

        self.attribute_map = {
            'from_address': 'fromAddress',
            'to_address': 'toAddress',
            'to_address_messenger_type': 'toAddressMessengerType',
            'text_body': 'textBody',
            'messaging_template': 'messagingTemplate',
            'use_existing_active_conversation': 'useExistingActiveConversation'
        }

        self._from_address = None
        self._to_address = None
        self._to_address_messenger_type = None
        self._text_body = None
        self._messaging_template = None
        self._use_existing_active_conversation = None

    @property
    def from_address(self) -> str:
        """
        Gets the from_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the sender of the message. For an SMS messenger type, this must be a currently provisioned SMS phone number. For a WhatsApp messenger type use the provisioned WhatsApp integration’s ID

        :return: The from_address of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address: str) -> None:
        """
        Sets the from_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the sender of the message. For an SMS messenger type, this must be a currently provisioned SMS phone number. For a WhatsApp messenger type use the provisioned WhatsApp integration’s ID

        :param from_address: The from_address of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        

        self._from_address = from_address

    @property
    def to_address(self) -> str:
        """
        Gets the to_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234. For WhatsApp messenger type, use a WhatsApp ID of a phone number. E.g for a E.164 formatted phone number `+13175555555`, a WhatsApp ID would be 13175555555

        :return: The to_address of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address: str) -> None:
        """
        Sets the to_address of this SendAgentlessOutboundMessageRequest.
        The messaging address of the recipient of the message. For an SMS messenger type, the phone number address must be in E.164 format. E.g. +13175555555 or +34234234234. For WhatsApp messenger type, use a WhatsApp ID of a phone number. E.g for a E.164 formatted phone number `+13175555555`, a WhatsApp ID would be 13175555555

        :param to_address: The to_address of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        

        self._to_address = to_address

    @property
    def to_address_messenger_type(self) -> str:
        """
        Gets the to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        The recipient messaging address messenger type.

        :return: The to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._to_address_messenger_type

    @to_address_messenger_type.setter
    def to_address_messenger_type(self, to_address_messenger_type: str) -> None:
        """
        Sets the to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        The recipient messaging address messenger type.

        :param to_address_messenger_type: The to_address_messenger_type of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        if isinstance(to_address_messenger_type, int):
            to_address_messenger_type = str(to_address_messenger_type)
        allowed_values = ["sms", "whatsapp", "open"]
        if to_address_messenger_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for to_address_messenger_type -> " + to_address_messenger_type)
            self._to_address_messenger_type = "outdated_sdk_version"
        else:
            self._to_address_messenger_type = to_address_messenger_type

    @property
    def text_body(self) -> str:
        """
        Gets the text_body of this SendAgentlessOutboundMessageRequest.
        The text of the message to send. This field is required in the case of SMS messenger type. Maximum character counts are: SMS - 765 characters, other channels - 2000 characters.

        :return: The text_body of this SendAgentlessOutboundMessageRequest.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body: str) -> None:
        """
        Sets the text_body of this SendAgentlessOutboundMessageRequest.
        The text of the message to send. This field is required in the case of SMS messenger type. Maximum character counts are: SMS - 765 characters, other channels - 2000 characters.

        :param text_body: The text_body of this SendAgentlessOutboundMessageRequest.
        :type: str
        """
        

        self._text_body = text_body

    @property
    def messaging_template(self) -> 'MessagingTemplateRequest':
        """
        Gets the messaging_template of this SendAgentlessOutboundMessageRequest.
        The messaging template to use in the case of WhatsApp messenger type. This field is required when using WhatsApp messenger type

        :return: The messaging_template of this SendAgentlessOutboundMessageRequest.
        :rtype: MessagingTemplateRequest
        """
        return self._messaging_template

    @messaging_template.setter
    def messaging_template(self, messaging_template: 'MessagingTemplateRequest') -> None:
        """
        Sets the messaging_template of this SendAgentlessOutboundMessageRequest.
        The messaging template to use in the case of WhatsApp messenger type. This field is required when using WhatsApp messenger type

        :param messaging_template: The messaging_template of this SendAgentlessOutboundMessageRequest.
        :type: MessagingTemplateRequest
        """
        

        self._messaging_template = messaging_template

    @property
    def use_existing_active_conversation(self) -> bool:
        """
        Gets the use_existing_active_conversation of this SendAgentlessOutboundMessageRequest.
        Use an existing active conversation to send the agentless outbound message. Set this parameter to 'true' to use active conversation. Default value: false

        :return: The use_existing_active_conversation of this SendAgentlessOutboundMessageRequest.
        :rtype: bool
        """
        return self._use_existing_active_conversation

    @use_existing_active_conversation.setter
    def use_existing_active_conversation(self, use_existing_active_conversation: bool) -> None:
        """
        Sets the use_existing_active_conversation of this SendAgentlessOutboundMessageRequest.
        Use an existing active conversation to send the agentless outbound message. Set this parameter to 'true' to use active conversation. Default value: false

        :param use_existing_active_conversation: The use_existing_active_conversation of this SendAgentlessOutboundMessageRequest.
        :type: bool
        """
        

        self._use_existing_active_conversation = use_existing_active_conversation

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

