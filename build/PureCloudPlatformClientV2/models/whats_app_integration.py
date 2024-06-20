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
    from . import ErrorBody
    from . import MessagingSettingReference
    from . import SupportedContentReference
    from . import WhatsAppAvailablePhoneNumberDetailsListing

class WhatsAppIntegration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WhatsAppIntegration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'supported_content': 'SupportedContentReference',
            'messaging_setting': 'MessagingSettingReference',
            'phone_number': 'str',
            'available_phone_numbers': 'WhatsAppAvailablePhoneNumberDetailsListing',
            'status': 'str',
            'recipient': 'DomainEntityRef',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'created_by': 'DomainEntityRef',
            'modified_by': 'DomainEntityRef',
            'version': 'int',
            'activation_status_code': 'str',
            'activation_error_info': 'ErrorBody',
            'create_status': 'str',
            'create_error': 'ErrorBody',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'supported_content': 'supportedContent',
            'messaging_setting': 'messagingSetting',
            'phone_number': 'phoneNumber',
            'available_phone_numbers': 'availablePhoneNumbers',
            'status': 'status',
            'recipient': 'recipient',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'created_by': 'createdBy',
            'modified_by': 'modifiedBy',
            'version': 'version',
            'activation_status_code': 'activationStatusCode',
            'activation_error_info': 'activationErrorInfo',
            'create_status': 'createStatus',
            'create_error': 'createError',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._supported_content = None
        self._messaging_setting = None
        self._phone_number = None
        self._available_phone_numbers = None
        self._status = None
        self._recipient = None
        self._date_created = None
        self._date_modified = None
        self._created_by = None
        self._modified_by = None
        self._version = None
        self._activation_status_code = None
        self._activation_error_info = None
        self._create_status = None
        self._create_error = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WhatsAppIntegration.
        A unique Integration Id.

        :return: The id of this WhatsAppIntegration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WhatsAppIntegration.
        A unique Integration Id.

        :param id: The id of this WhatsAppIntegration.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this WhatsAppIntegration.
        The name of the WhatsApp integration.

        :return: The name of this WhatsAppIntegration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this WhatsAppIntegration.
        The name of the WhatsApp integration.

        :param name: The name of this WhatsAppIntegration.
        :type: str
        """
        

        self._name = name

    @property
    def supported_content(self) -> 'SupportedContentReference':
        """
        Gets the supported_content of this WhatsAppIntegration.
        Defines the SupportedContent profile configured for an integration

        :return: The supported_content of this WhatsAppIntegration.
        :rtype: SupportedContentReference
        """
        return self._supported_content

    @supported_content.setter
    def supported_content(self, supported_content: 'SupportedContentReference') -> None:
        """
        Sets the supported_content of this WhatsAppIntegration.
        Defines the SupportedContent profile configured for an integration

        :param supported_content: The supported_content of this WhatsAppIntegration.
        :type: SupportedContentReference
        """
        

        self._supported_content = supported_content

    @property
    def messaging_setting(self) -> 'MessagingSettingReference':
        """
        Gets the messaging_setting of this WhatsAppIntegration.


        :return: The messaging_setting of this WhatsAppIntegration.
        :rtype: MessagingSettingReference
        """
        return self._messaging_setting

    @messaging_setting.setter
    def messaging_setting(self, messaging_setting: 'MessagingSettingReference') -> None:
        """
        Sets the messaging_setting of this WhatsAppIntegration.


        :param messaging_setting: The messaging_setting of this WhatsAppIntegration.
        :type: MessagingSettingReference
        """
        

        self._messaging_setting = messaging_setting

    @property
    def phone_number(self) -> str:
        """
        Gets the phone_number of this WhatsAppIntegration.
        The phone number associated to the WhatsApp integration.

        :return: The phone_number of this WhatsAppIntegration.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str) -> None:
        """
        Sets the phone_number of this WhatsAppIntegration.
        The phone number associated to the WhatsApp integration.

        :param phone_number: The phone_number of this WhatsAppIntegration.
        :type: str
        """
        

        self._phone_number = phone_number

    @property
    def available_phone_numbers(self) -> 'WhatsAppAvailablePhoneNumberDetailsListing':
        """
        Gets the available_phone_numbers of this WhatsAppIntegration.
        The list of available WhatsApp phone numbers for this account. Please select one phone number from this list to use with the created integration.

        :return: The available_phone_numbers of this WhatsAppIntegration.
        :rtype: WhatsAppAvailablePhoneNumberDetailsListing
        """
        return self._available_phone_numbers

    @available_phone_numbers.setter
    def available_phone_numbers(self, available_phone_numbers: 'WhatsAppAvailablePhoneNumberDetailsListing') -> None:
        """
        Sets the available_phone_numbers of this WhatsAppIntegration.
        The list of available WhatsApp phone numbers for this account. Please select one phone number from this list to use with the created integration.

        :param available_phone_numbers: The available_phone_numbers of this WhatsAppIntegration.
        :type: WhatsAppAvailablePhoneNumberDetailsListing
        """
        

        self._available_phone_numbers = available_phone_numbers

    @property
    def status(self) -> str:
        """
        Gets the status of this WhatsAppIntegration.
        The status of the WhatsApp Integration

        :return: The status of this WhatsAppIntegration.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this WhatsAppIntegration.
        The status of the WhatsApp Integration

        :param status: The status of this WhatsAppIntegration.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Active", "Inactive", "Error", "Starting", "Incomplete", "Deleting", "DeletionFailed"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def recipient(self) -> 'DomainEntityRef':
        """
        Gets the recipient of this WhatsAppIntegration.
        The recipient associated to the WhatsApp Integration. This recipient is used to associate a flow to an integration

        :return: The recipient of this WhatsAppIntegration.
        :rtype: DomainEntityRef
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient: 'DomainEntityRef') -> None:
        """
        Sets the recipient of this WhatsAppIntegration.
        The recipient associated to the WhatsApp Integration. This recipient is used to associate a flow to an integration

        :param recipient: The recipient of this WhatsAppIntegration.
        :type: DomainEntityRef
        """
        

        self._recipient = recipient

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this WhatsAppIntegration.
        Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this WhatsAppIntegration.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this WhatsAppIntegration.
        Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this WhatsAppIntegration.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this WhatsAppIntegration.
        Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this WhatsAppIntegration.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this WhatsAppIntegration.
        Date this Integration was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this WhatsAppIntegration.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def created_by(self) -> 'DomainEntityRef':
        """
        Gets the created_by of this WhatsAppIntegration.
        User reference that created this Integration

        :return: The created_by of this WhatsAppIntegration.
        :rtype: DomainEntityRef
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'DomainEntityRef') -> None:
        """
        Sets the created_by of this WhatsAppIntegration.
        User reference that created this Integration

        :param created_by: The created_by of this WhatsAppIntegration.
        :type: DomainEntityRef
        """
        

        self._created_by = created_by

    @property
    def modified_by(self) -> 'DomainEntityRef':
        """
        Gets the modified_by of this WhatsAppIntegration.
        User reference that last modified this Integration

        :return: The modified_by of this WhatsAppIntegration.
        :rtype: DomainEntityRef
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'DomainEntityRef') -> None:
        """
        Sets the modified_by of this WhatsAppIntegration.
        User reference that last modified this Integration

        :param modified_by: The modified_by of this WhatsAppIntegration.
        :type: DomainEntityRef
        """
        

        self._modified_by = modified_by

    @property
    def version(self) -> int:
        """
        Gets the version of this WhatsAppIntegration.
        Version number required for updates.

        :return: The version of this WhatsAppIntegration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this WhatsAppIntegration.
        Version number required for updates.

        :param version: The version of this WhatsAppIntegration.
        :type: int
        """
        

        self._version = version

    @property
    def activation_status_code(self) -> str:
        """
        Gets the activation_status_code of this WhatsAppIntegration.
        The status code of WhatsApp Integration activation process

        :return: The activation_status_code of this WhatsAppIntegration.
        :rtype: str
        """
        return self._activation_status_code

    @activation_status_code.setter
    def activation_status_code(self, activation_status_code: str) -> None:
        """
        Sets the activation_status_code of this WhatsAppIntegration.
        The status code of WhatsApp Integration activation process

        :param activation_status_code: The activation_status_code of this WhatsAppIntegration.
        :type: str
        """
        if isinstance(activation_status_code, int):
            activation_status_code = str(activation_status_code)
        allowed_values = ["CodeSent", "WaitRequired", "ActivationFailed", "CodeConfirmed", "ConfirmationFailed", "ResendCode"]
        if activation_status_code.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for activation_status_code -> " + activation_status_code)
            self._activation_status_code = "outdated_sdk_version"
        else:
            self._activation_status_code = activation_status_code

    @property
    def activation_error_info(self) -> 'ErrorBody':
        """
        Gets the activation_error_info of this WhatsAppIntegration.
        The error information of WhatsApp Integration activation process

        :return: The activation_error_info of this WhatsAppIntegration.
        :rtype: ErrorBody
        """
        return self._activation_error_info

    @activation_error_info.setter
    def activation_error_info(self, activation_error_info: 'ErrorBody') -> None:
        """
        Sets the activation_error_info of this WhatsAppIntegration.
        The error information of WhatsApp Integration activation process

        :param activation_error_info: The activation_error_info of this WhatsAppIntegration.
        :type: ErrorBody
        """
        

        self._activation_error_info = activation_error_info

    @property
    def create_status(self) -> str:
        """
        Gets the create_status of this WhatsAppIntegration.
        Status of asynchronous create operation

        :return: The create_status of this WhatsAppIntegration.
        :rtype: str
        """
        return self._create_status

    @create_status.setter
    def create_status(self, create_status: str) -> None:
        """
        Sets the create_status of this WhatsAppIntegration.
        Status of asynchronous create operation

        :param create_status: The create_status of this WhatsAppIntegration.
        :type: str
        """
        if isinstance(create_status, int):
            create_status = str(create_status)
        allowed_values = ["Initiated", "Completed", "Error"]
        if create_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for create_status -> " + create_status)
            self._create_status = "outdated_sdk_version"
        else:
            self._create_status = create_status

    @property
    def create_error(self) -> 'ErrorBody':
        """
        Gets the create_error of this WhatsAppIntegration.
        Error information returned, if createStatus is set to Error

        :return: The create_error of this WhatsAppIntegration.
        :rtype: ErrorBody
        """
        return self._create_error

    @create_error.setter
    def create_error(self, create_error: 'ErrorBody') -> None:
        """
        Sets the create_error of this WhatsAppIntegration.
        Error information returned, if createStatus is set to Error

        :param create_error: The create_error of this WhatsAppIntegration.
        :type: ErrorBody
        """
        

        self._create_error = create_error

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this WhatsAppIntegration.
        The URI for this object

        :return: The self_uri of this WhatsAppIntegration.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this WhatsAppIntegration.
        The URI for this object

        :param self_uri: The self_uri of this WhatsAppIntegration.
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
