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
    from . import MessagingSettingRequestReference
    from . import SupportedContentReference

class OpenIntegrationUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OpenIntegrationUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'supported_content': 'SupportedContentReference',
            'messaging_setting': 'MessagingSettingRequestReference',
            'outbound_notification_webhook_url': 'str',
            'outbound_notification_webhook_signature_secret_token': 'str',
            'webhook_headers': 'dict(str, str)',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'supported_content': 'supportedContent',
            'messaging_setting': 'messagingSetting',
            'outbound_notification_webhook_url': 'outboundNotificationWebhookUrl',
            'outbound_notification_webhook_signature_secret_token': 'outboundNotificationWebhookSignatureSecretToken',
            'webhook_headers': 'webhookHeaders',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._supported_content = None
        self._messaging_setting = None
        self._outbound_notification_webhook_url = None
        self._outbound_notification_webhook_signature_secret_token = None
        self._webhook_headers = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this OpenIntegrationUpdateRequest.
        The globally unique identifier for the object.

        :return: The id of this OpenIntegrationUpdateRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this OpenIntegrationUpdateRequest.
        The globally unique identifier for the object.

        :param id: The id of this OpenIntegrationUpdateRequest.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this OpenIntegrationUpdateRequest.
        The name of the Open messaging integration.

        :return: The name of this OpenIntegrationUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this OpenIntegrationUpdateRequest.
        The name of the Open messaging integration.

        :param name: The name of this OpenIntegrationUpdateRequest.
        :type: str
        """
        

        self._name = name

    @property
    def supported_content(self) -> 'SupportedContentReference':
        """
        Gets the supported_content of this OpenIntegrationUpdateRequest.
        Defines the SupportedContent profile configured for an integration

        :return: The supported_content of this OpenIntegrationUpdateRequest.
        :rtype: SupportedContentReference
        """
        return self._supported_content

    @supported_content.setter
    def supported_content(self, supported_content: 'SupportedContentReference') -> None:
        """
        Sets the supported_content of this OpenIntegrationUpdateRequest.
        Defines the SupportedContent profile configured for an integration

        :param supported_content: The supported_content of this OpenIntegrationUpdateRequest.
        :type: SupportedContentReference
        """
        

        self._supported_content = supported_content

    @property
    def messaging_setting(self) -> 'MessagingSettingRequestReference':
        """
        Gets the messaging_setting of this OpenIntegrationUpdateRequest.
        Defines the message settings to be applied for this integration

        :return: The messaging_setting of this OpenIntegrationUpdateRequest.
        :rtype: MessagingSettingRequestReference
        """
        return self._messaging_setting

    @messaging_setting.setter
    def messaging_setting(self, messaging_setting: 'MessagingSettingRequestReference') -> None:
        """
        Sets the messaging_setting of this OpenIntegrationUpdateRequest.
        Defines the message settings to be applied for this integration

        :param messaging_setting: The messaging_setting of this OpenIntegrationUpdateRequest.
        :type: MessagingSettingRequestReference
        """
        

        self._messaging_setting = messaging_setting

    @property
    def outbound_notification_webhook_url(self) -> str:
        """
        Gets the outbound_notification_webhook_url of this OpenIntegrationUpdateRequest.
        The outbound notification webhook URL for the Open messaging integration.

        :return: The outbound_notification_webhook_url of this OpenIntegrationUpdateRequest.
        :rtype: str
        """
        return self._outbound_notification_webhook_url

    @outbound_notification_webhook_url.setter
    def outbound_notification_webhook_url(self, outbound_notification_webhook_url: str) -> None:
        """
        Sets the outbound_notification_webhook_url of this OpenIntegrationUpdateRequest.
        The outbound notification webhook URL for the Open messaging integration.

        :param outbound_notification_webhook_url: The outbound_notification_webhook_url of this OpenIntegrationUpdateRequest.
        :type: str
        """
        

        self._outbound_notification_webhook_url = outbound_notification_webhook_url

    @property
    def outbound_notification_webhook_signature_secret_token(self) -> str:
        """
        Gets the outbound_notification_webhook_signature_secret_token of this OpenIntegrationUpdateRequest.
        The outbound notification webhook signature secret token.

        :return: The outbound_notification_webhook_signature_secret_token of this OpenIntegrationUpdateRequest.
        :rtype: str
        """
        return self._outbound_notification_webhook_signature_secret_token

    @outbound_notification_webhook_signature_secret_token.setter
    def outbound_notification_webhook_signature_secret_token(self, outbound_notification_webhook_signature_secret_token: str) -> None:
        """
        Sets the outbound_notification_webhook_signature_secret_token of this OpenIntegrationUpdateRequest.
        The outbound notification webhook signature secret token.

        :param outbound_notification_webhook_signature_secret_token: The outbound_notification_webhook_signature_secret_token of this OpenIntegrationUpdateRequest.
        :type: str
        """
        

        self._outbound_notification_webhook_signature_secret_token = outbound_notification_webhook_signature_secret_token

    @property
    def webhook_headers(self) -> Dict[str, str]:
        """
        Gets the webhook_headers of this OpenIntegrationUpdateRequest.
        The user specified headers for the Open messaging integration.

        :return: The webhook_headers of this OpenIntegrationUpdateRequest.
        :rtype: dict(str, str)
        """
        return self._webhook_headers

    @webhook_headers.setter
    def webhook_headers(self, webhook_headers: Dict[str, str]) -> None:
        """
        Sets the webhook_headers of this OpenIntegrationUpdateRequest.
        The user specified headers for the Open messaging integration.

        :param webhook_headers: The webhook_headers of this OpenIntegrationUpdateRequest.
        :type: dict(str, str)
        """
        

        self._webhook_headers = webhook_headers

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this OpenIntegrationUpdateRequest.
        The URI for this object

        :return: The self_uri of this OpenIntegrationUpdateRequest.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this OpenIntegrationUpdateRequest.
        The URI for this object

        :param self_uri: The self_uri of this OpenIntegrationUpdateRequest.
        :type: str
        """
        

        self._self_uri = self_uri

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

