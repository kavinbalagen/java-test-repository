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


class AcwDetailEventTopicAfterCallWorkEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AcwDetailEventTopicAfterCallWorkEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_time': 'int',
            'conversation_id': 'str',
            'participant_id': 'str',
            'session_id': 'str',
            'media_type': 'str',
            'provider': 'str',
            'direction': 'str',
            'ani': 'str',
            'dnis': 'str',
            'address_to': 'str',
            'address_from': 'str',
            'callback_user_name': 'str',
            'callback_numbers': 'list[str]',
            'callback_scheduled_time': 'int',
            'subject': 'str',
            'message_type': 'str',
            'user_id': 'str',
            'queue_id': 'str',
            'wrapup_code': 'str',
            'wrapup_notes': 'str',
            'wrapup_duration_ms': 'int',
            'conversation_external_contact_ids': 'list[str]',
            'conversation_external_organization_ids': 'list[str]'
        }

        self.attribute_map = {
            'event_time': 'eventTime',
            'conversation_id': 'conversationId',
            'participant_id': 'participantId',
            'session_id': 'sessionId',
            'media_type': 'mediaType',
            'provider': 'provider',
            'direction': 'direction',
            'ani': 'ani',
            'dnis': 'dnis',
            'address_to': 'addressTo',
            'address_from': 'addressFrom',
            'callback_user_name': 'callbackUserName',
            'callback_numbers': 'callbackNumbers',
            'callback_scheduled_time': 'callbackScheduledTime',
            'subject': 'subject',
            'message_type': 'messageType',
            'user_id': 'userId',
            'queue_id': 'queueId',
            'wrapup_code': 'wrapupCode',
            'wrapup_notes': 'wrapupNotes',
            'wrapup_duration_ms': 'wrapupDurationMs',
            'conversation_external_contact_ids': 'conversationExternalContactIds',
            'conversation_external_organization_ids': 'conversationExternalOrganizationIds'
        }

        self._event_time = None
        self._conversation_id = None
        self._participant_id = None
        self._session_id = None
        self._media_type = None
        self._provider = None
        self._direction = None
        self._ani = None
        self._dnis = None
        self._address_to = None
        self._address_from = None
        self._callback_user_name = None
        self._callback_numbers = None
        self._callback_scheduled_time = None
        self._subject = None
        self._message_type = None
        self._user_id = None
        self._queue_id = None
        self._wrapup_code = None
        self._wrapup_notes = None
        self._wrapup_duration_ms = None
        self._conversation_external_contact_ids = None
        self._conversation_external_organization_ids = None

    @property
    def event_time(self) -> int:
        """
        Gets the event_time of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The event_time of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: int) -> None:
        """
        Sets the event_time of this AcwDetailEventTopicAfterCallWorkEvent.


        :param event_time: The event_time of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: int
        """
        

        self._event_time = event_time

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The conversation_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :param conversation_id: The conversation_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def participant_id(self) -> str:
        """
        Gets the participant_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The participant_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id: str) -> None:
        """
        Sets the participant_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :param participant_id: The participant_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._participant_id = participant_id

    @property
    def session_id(self) -> str:
        """
        Gets the session_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The session_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str) -> None:
        """
        Sets the session_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :param session_id: The session_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._session_id = session_id

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The media_type of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this AcwDetailEventTopicAfterCallWorkEvent.


        :param media_type: The media_type of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        if isinstance(media_type, int):
            media_type = str(media_type)
        allowed_values = ["UNKNOWN", "VOICE", "CHAT", "EMAIL", "CALLBACK", "COBROWSE", "VIDEO", "SCREENSHARE", "MESSAGE"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def provider(self) -> str:
        """
        Gets the provider of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The provider of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider: str) -> None:
        """
        Sets the provider of this AcwDetailEventTopicAfterCallWorkEvent.


        :param provider: The provider of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._provider = provider

    @property
    def direction(self) -> str:
        """
        Gets the direction of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The direction of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this AcwDetailEventTopicAfterCallWorkEvent.


        :param direction: The direction of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        if isinstance(direction, int):
            direction = str(direction)
        allowed_values = ["UNKNOWN", "INBOUND", "OUTBOUND"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def ani(self) -> str:
        """
        Gets the ani of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The ani of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._ani

    @ani.setter
    def ani(self, ani: str) -> None:
        """
        Sets the ani of this AcwDetailEventTopicAfterCallWorkEvent.


        :param ani: The ani of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._ani = ani

    @property
    def dnis(self) -> str:
        """
        Gets the dnis of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The dnis of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._dnis

    @dnis.setter
    def dnis(self, dnis: str) -> None:
        """
        Sets the dnis of this AcwDetailEventTopicAfterCallWorkEvent.


        :param dnis: The dnis of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._dnis = dnis

    @property
    def address_to(self) -> str:
        """
        Gets the address_to of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The address_to of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._address_to

    @address_to.setter
    def address_to(self, address_to: str) -> None:
        """
        Sets the address_to of this AcwDetailEventTopicAfterCallWorkEvent.


        :param address_to: The address_to of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._address_to = address_to

    @property
    def address_from(self) -> str:
        """
        Gets the address_from of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The address_from of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._address_from

    @address_from.setter
    def address_from(self, address_from: str) -> None:
        """
        Sets the address_from of this AcwDetailEventTopicAfterCallWorkEvent.


        :param address_from: The address_from of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._address_from = address_from

    @property
    def callback_user_name(self) -> str:
        """
        Gets the callback_user_name of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The callback_user_name of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._callback_user_name

    @callback_user_name.setter
    def callback_user_name(self, callback_user_name: str) -> None:
        """
        Sets the callback_user_name of this AcwDetailEventTopicAfterCallWorkEvent.


        :param callback_user_name: The callback_user_name of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._callback_user_name = callback_user_name

    @property
    def callback_numbers(self) -> List[str]:
        """
        Gets the callback_numbers of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The callback_numbers of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: list[str]
        """
        return self._callback_numbers

    @callback_numbers.setter
    def callback_numbers(self, callback_numbers: List[str]) -> None:
        """
        Sets the callback_numbers of this AcwDetailEventTopicAfterCallWorkEvent.


        :param callback_numbers: The callback_numbers of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: list[str]
        """
        

        self._callback_numbers = callback_numbers

    @property
    def callback_scheduled_time(self) -> int:
        """
        Gets the callback_scheduled_time of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The callback_scheduled_time of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: int
        """
        return self._callback_scheduled_time

    @callback_scheduled_time.setter
    def callback_scheduled_time(self, callback_scheduled_time: int) -> None:
        """
        Sets the callback_scheduled_time of this AcwDetailEventTopicAfterCallWorkEvent.


        :param callback_scheduled_time: The callback_scheduled_time of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: int
        """
        

        self._callback_scheduled_time = callback_scheduled_time

    @property
    def subject(self) -> str:
        """
        Gets the subject of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The subject of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this AcwDetailEventTopicAfterCallWorkEvent.


        :param subject: The subject of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._subject = subject

    @property
    def message_type(self) -> str:
        """
        Gets the message_type of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The message_type of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type: str) -> None:
        """
        Sets the message_type of this AcwDetailEventTopicAfterCallWorkEvent.


        :param message_type: The message_type of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        if isinstance(message_type, int):
            message_type = str(message_type)
        allowed_values = ["UNKNOWN", "SMS", "TWITTER", "FACEBOOK", "LINE", "WHATSAPP", "WEBMESSAGING", "OPEN", "INSTAGRAM"]
        if message_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for message_type -> " + message_type)
            self._message_type = "outdated_sdk_version"
        else:
            self._message_type = message_type

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The user_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :param user_id: The user_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def queue_id(self) -> str:
        """
        Gets the queue_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The queue_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: str) -> None:
        """
        Sets the queue_id of this AcwDetailEventTopicAfterCallWorkEvent.


        :param queue_id: The queue_id of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._queue_id = queue_id

    @property
    def wrapup_code(self) -> str:
        """
        Gets the wrapup_code of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The wrapup_code of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._wrapup_code

    @wrapup_code.setter
    def wrapup_code(self, wrapup_code: str) -> None:
        """
        Sets the wrapup_code of this AcwDetailEventTopicAfterCallWorkEvent.


        :param wrapup_code: The wrapup_code of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._wrapup_code = wrapup_code

    @property
    def wrapup_notes(self) -> str:
        """
        Gets the wrapup_notes of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The wrapup_notes of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: str
        """
        return self._wrapup_notes

    @wrapup_notes.setter
    def wrapup_notes(self, wrapup_notes: str) -> None:
        """
        Sets the wrapup_notes of this AcwDetailEventTopicAfterCallWorkEvent.


        :param wrapup_notes: The wrapup_notes of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: str
        """
        

        self._wrapup_notes = wrapup_notes

    @property
    def wrapup_duration_ms(self) -> int:
        """
        Gets the wrapup_duration_ms of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The wrapup_duration_ms of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: int
        """
        return self._wrapup_duration_ms

    @wrapup_duration_ms.setter
    def wrapup_duration_ms(self, wrapup_duration_ms: int) -> None:
        """
        Sets the wrapup_duration_ms of this AcwDetailEventTopicAfterCallWorkEvent.


        :param wrapup_duration_ms: The wrapup_duration_ms of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: int
        """
        

        self._wrapup_duration_ms = wrapup_duration_ms

    @property
    def conversation_external_contact_ids(self) -> List[str]:
        """
        Gets the conversation_external_contact_ids of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The conversation_external_contact_ids of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: list[str]
        """
        return self._conversation_external_contact_ids

    @conversation_external_contact_ids.setter
    def conversation_external_contact_ids(self, conversation_external_contact_ids: List[str]) -> None:
        """
        Sets the conversation_external_contact_ids of this AcwDetailEventTopicAfterCallWorkEvent.


        :param conversation_external_contact_ids: The conversation_external_contact_ids of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: list[str]
        """
        

        self._conversation_external_contact_ids = conversation_external_contact_ids

    @property
    def conversation_external_organization_ids(self) -> List[str]:
        """
        Gets the conversation_external_organization_ids of this AcwDetailEventTopicAfterCallWorkEvent.


        :return: The conversation_external_organization_ids of this AcwDetailEventTopicAfterCallWorkEvent.
        :rtype: list[str]
        """
        return self._conversation_external_organization_ids

    @conversation_external_organization_ids.setter
    def conversation_external_organization_ids(self, conversation_external_organization_ids: List[str]) -> None:
        """
        Sets the conversation_external_organization_ids of this AcwDetailEventTopicAfterCallWorkEvent.


        :param conversation_external_organization_ids: The conversation_external_organization_ids of this AcwDetailEventTopicAfterCallWorkEvent.
        :type: list[str]
        """
        

        self._conversation_external_organization_ids = conversation_external_organization_ids

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

