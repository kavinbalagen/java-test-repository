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


class CreateEmailRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreateEmailRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue_id': 'str',
            'flow_id': 'str',
            'provider': 'str',
            'skill_ids': 'list[str]',
            'language_id': 'str',
            'priority': 'int',
            'attributes': 'dict(str, str)',
            'to_address': 'str',
            'to_name': 'str',
            'from_address': 'str',
            'from_name': 'str',
            'subject': 'str',
            'direction': 'str',
            'html_body': 'str',
            'text_body': 'str',
            'external_contact_id': 'str'
        }

        self.attribute_map = {
            'queue_id': 'queueId',
            'flow_id': 'flowId',
            'provider': 'provider',
            'skill_ids': 'skillIds',
            'language_id': 'languageId',
            'priority': 'priority',
            'attributes': 'attributes',
            'to_address': 'toAddress',
            'to_name': 'toName',
            'from_address': 'fromAddress',
            'from_name': 'fromName',
            'subject': 'subject',
            'direction': 'direction',
            'html_body': 'htmlBody',
            'text_body': 'textBody',
            'external_contact_id': 'externalContactId'
        }

        self._queue_id = None
        self._flow_id = None
        self._provider = None
        self._skill_ids = None
        self._language_id = None
        self._priority = None
        self._attributes = None
        self._to_address = None
        self._to_name = None
        self._from_address = None
        self._from_name = None
        self._subject = None
        self._direction = None
        self._html_body = None
        self._text_body = None
        self._external_contact_id = None

    @property
    def queue_id(self) -> str:
        """
        Gets the queue_id of this CreateEmailRequest.
        The ID of the queue to use for routing the email conversation. This field is mutually exclusive with flowId

        :return: The queue_id of this CreateEmailRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: str) -> None:
        """
        Sets the queue_id of this CreateEmailRequest.
        The ID of the queue to use for routing the email conversation. This field is mutually exclusive with flowId

        :param queue_id: The queue_id of this CreateEmailRequest.
        :type: str
        """
        

        self._queue_id = queue_id

    @property
    def flow_id(self) -> str:
        """
        Gets the flow_id of this CreateEmailRequest.
        The ID of the flow to use for routing email conversation. This field is mutually exclusive with queueId

        :return: The flow_id of this CreateEmailRequest.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id: str) -> None:
        """
        Sets the flow_id of this CreateEmailRequest.
        The ID of the flow to use for routing email conversation. This field is mutually exclusive with queueId

        :param flow_id: The flow_id of this CreateEmailRequest.
        :type: str
        """
        

        self._flow_id = flow_id

    @property
    def provider(self) -> str:
        """
        Gets the provider of this CreateEmailRequest.
        The name of the provider that is sourcing the emails. The Provider \"PureCloud Email\" is reserved for native emails.

        :return: The provider of this CreateEmailRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this CreateEmailRequest.
        The name of the provider that is sourcing the emails. The Provider \"PureCloud Email\" is reserved for native emails.

        :param provider: The provider of this CreateEmailRequest.
        :type: str
        """
        

        self._provider = provider

    @property
    def skill_ids(self) -> List[str]:
        """
        Gets the skill_ids of this CreateEmailRequest.
        The list of skill ID's to use for routing.

        :return: The skill_ids of this CreateEmailRequest.
        :rtype: list[str]
        """
        return self._skill_ids

    @skill_ids.setter
    def skill_ids(self, skill_ids: List[str]) -> None:
        """
        Sets the skill_ids of this CreateEmailRequest.
        The list of skill ID's to use for routing.

        :param skill_ids: The skill_ids of this CreateEmailRequest.
        :type: list[str]
        """
        

        self._skill_ids = skill_ids

    @property
    def language_id(self) -> str:
        """
        Gets the language_id of this CreateEmailRequest.
        The ID of the language to use for routing.

        :return: The language_id of this CreateEmailRequest.
        :rtype: str
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id: str) -> None:
        """
        Sets the language_id of this CreateEmailRequest.
        The ID of the language to use for routing.

        :param language_id: The language_id of this CreateEmailRequest.
        :type: str
        """
        

        self._language_id = language_id

    @property
    def priority(self) -> int:
        """
        Gets the priority of this CreateEmailRequest.
        The priority to assign to the conversation for routing.

        :return: The priority of this CreateEmailRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority: int) -> None:
        """
        Sets the priority of this CreateEmailRequest.
        The priority to assign to the conversation for routing.

        :param priority: The priority of this CreateEmailRequest.
        :type: int
        """
        

        self._priority = priority

    @property
    def attributes(self) -> Dict[str, str]:
        """
        Gets the attributes of this CreateEmailRequest.
        The list of attributes to associate with the customer participant.

        :return: The attributes of this CreateEmailRequest.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: Dict[str, str]) -> None:
        """
        Sets the attributes of this CreateEmailRequest.
        The list of attributes to associate with the customer participant.

        :param attributes: The attributes of this CreateEmailRequest.
        :type: dict(str, str)
        """
        

        self._attributes = attributes

    @property
    def to_address(self) -> str:
        """
        Gets the to_address of this CreateEmailRequest.
        The email address of the recipient of the email.

        :return: The to_address of this CreateEmailRequest.
        :rtype: str
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address: str) -> None:
        """
        Sets the to_address of this CreateEmailRequest.
        The email address of the recipient of the email.

        :param to_address: The to_address of this CreateEmailRequest.
        :type: str
        """
        

        self._to_address = to_address

    @property
    def to_name(self) -> str:
        """
        Gets the to_name of this CreateEmailRequest.
        The name of the recipient of the email.

        :return: The to_name of this CreateEmailRequest.
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name: str) -> None:
        """
        Sets the to_name of this CreateEmailRequest.
        The name of the recipient of the email.

        :param to_name: The to_name of this CreateEmailRequest.
        :type: str
        """
        

        self._to_name = to_name

    @property
    def from_address(self) -> str:
        """
        Gets the from_address of this CreateEmailRequest.
        The email address of the sender of the email.

        :return: The from_address of this CreateEmailRequest.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address: str) -> None:
        """
        Sets the from_address of this CreateEmailRequest.
        The email address of the sender of the email.

        :param from_address: The from_address of this CreateEmailRequest.
        :type: str
        """
        

        self._from_address = from_address

    @property
    def from_name(self) -> str:
        """
        Gets the from_name of this CreateEmailRequest.
        The name of the sender of the email.

        :return: The from_name of this CreateEmailRequest.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name: str) -> None:
        """
        Sets the from_name of this CreateEmailRequest.
        The name of the sender of the email.

        :param from_name: The from_name of this CreateEmailRequest.
        :type: str
        """
        

        self._from_name = from_name

    @property
    def subject(self) -> str:
        """
        Gets the subject of this CreateEmailRequest.
        The subject of the email

        :return: The subject of this CreateEmailRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this CreateEmailRequest.
        The subject of the email

        :param subject: The subject of this CreateEmailRequest.
        :type: str
        """
        

        self._subject = subject

    @property
    def direction(self) -> str:
        """
        Gets the direction of this CreateEmailRequest.
        Specify OUTBOUND to send an email on behalf of a queue, or INBOUND to create an external conversation. An external conversation is one where the provider is not PureCloud based.

        :return: The direction of this CreateEmailRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this CreateEmailRequest.
        Specify OUTBOUND to send an email on behalf of a queue, or INBOUND to create an external conversation. An external conversation is one where the provider is not PureCloud based.

        :param direction: The direction of this CreateEmailRequest.
        :type: str
        """
        if isinstance(direction, int):
            direction = str(direction)
        allowed_values = ["OUTBOUND", "INBOUND"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def html_body(self) -> str:
        """
        Gets the html_body of this CreateEmailRequest.
        An HTML body content of the email.

        :return: The html_body of this CreateEmailRequest.
        :rtype: str
        """
        return self._html_body

    @html_body.setter
    def html_body(self, html_body: str) -> None:
        """
        Sets the html_body of this CreateEmailRequest.
        An HTML body content of the email.

        :param html_body: The html_body of this CreateEmailRequest.
        :type: str
        """
        

        self._html_body = html_body

    @property
    def text_body(self) -> str:
        """
        Gets the text_body of this CreateEmailRequest.
        A text body content of the email.

        :return: The text_body of this CreateEmailRequest.
        :rtype: str
        """
        return self._text_body

    @text_body.setter
    def text_body(self, text_body: str) -> None:
        """
        Sets the text_body of this CreateEmailRequest.
        A text body content of the email.

        :param text_body: The text_body of this CreateEmailRequest.
        :type: str
        """
        

        self._text_body = text_body

    @property
    def external_contact_id(self) -> str:
        """
        Gets the external_contact_id of this CreateEmailRequest.
        The external contact with which the email should be associated. This field is only valid for OUTBOUND email.

        :return: The external_contact_id of this CreateEmailRequest.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id: str) -> None:
        """
        Sets the external_contact_id of this CreateEmailRequest.
        The external contact with which the email should be associated. This field is only valid for OUTBOUND email.

        :param external_contact_id: The external_contact_id of this CreateEmailRequest.
        :type: str
        """
        

        self._external_contact_id = external_contact_id

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

