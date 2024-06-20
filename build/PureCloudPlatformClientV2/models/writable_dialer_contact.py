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
    from . import ContactableStatus
    from . import MessageEvaluation
    from . import PhoneNumberStatus

class WritableDialerContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WritableDialerContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'contact_list_id': 'str',
            'data': 'dict(str, str)',
            'latest_sms_evaluations': 'dict(str, MessageEvaluation)',
            'latest_email_evaluations': 'dict(str, MessageEvaluation)',
            'callable': 'bool',
            'phone_number_status': 'dict(str, PhoneNumberStatus)',
            'contactable_status': 'dict(str, ContactableStatus)',
            'date_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'contact_list_id': 'contactListId',
            'data': 'data',
            'latest_sms_evaluations': 'latestSmsEvaluations',
            'latest_email_evaluations': 'latestEmailEvaluations',
            'callable': 'callable',
            'phone_number_status': 'phoneNumberStatus',
            'contactable_status': 'contactableStatus',
            'date_created': 'dateCreated'
        }

        self._id = None
        self._contact_list_id = None
        self._data = None
        self._latest_sms_evaluations = None
        self._latest_email_evaluations = None
        self._callable = None
        self._phone_number_status = None
        self._contactable_status = None
        self._date_created = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WritableDialerContact.
        The globally unique identifier for the object.

        :return: The id of this WritableDialerContact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WritableDialerContact.
        The globally unique identifier for the object.

        :param id: The id of this WritableDialerContact.
        :type: str
        """
        

        self._id = id

    @property
    def contact_list_id(self) -> str:
        """
        Gets the contact_list_id of this WritableDialerContact.
        The identifier of the contact list containing this contact.

        :return: The contact_list_id of this WritableDialerContact.
        :rtype: str
        """
        return self._contact_list_id

    @contact_list_id.setter
    def contact_list_id(self, contact_list_id: str) -> None:
        """
        Sets the contact_list_id of this WritableDialerContact.
        The identifier of the contact list containing this contact.

        :param contact_list_id: The contact_list_id of this WritableDialerContact.
        :type: str
        """
        

        self._contact_list_id = contact_list_id

    @property
    def data(self) -> Dict[str, str]:
        """
        Gets the data of this WritableDialerContact.
        An ordered map of the contact's columns and corresponding values.

        :return: The data of this WritableDialerContact.
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data: Dict[str, str]) -> None:
        """
        Sets the data of this WritableDialerContact.
        An ordered map of the contact's columns and corresponding values.

        :param data: The data of this WritableDialerContact.
        :type: dict(str, str)
        """
        

        self._data = data

    @property
    def latest_sms_evaluations(self) -> Dict[str, 'MessageEvaluation']:
        """
        Gets the latest_sms_evaluations of this WritableDialerContact.
        A map of SMS records for the contact phone columns.

        :return: The latest_sms_evaluations of this WritableDialerContact.
        :rtype: dict(str, MessageEvaluation)
        """
        return self._latest_sms_evaluations

    @latest_sms_evaluations.setter
    def latest_sms_evaluations(self, latest_sms_evaluations: Dict[str, 'MessageEvaluation']) -> None:
        """
        Sets the latest_sms_evaluations of this WritableDialerContact.
        A map of SMS records for the contact phone columns.

        :param latest_sms_evaluations: The latest_sms_evaluations of this WritableDialerContact.
        :type: dict(str, MessageEvaluation)
        """
        

        self._latest_sms_evaluations = latest_sms_evaluations

    @property
    def latest_email_evaluations(self) -> Dict[str, 'MessageEvaluation']:
        """
        Gets the latest_email_evaluations of this WritableDialerContact.
        A map of email records for the contact email columns.

        :return: The latest_email_evaluations of this WritableDialerContact.
        :rtype: dict(str, MessageEvaluation)
        """
        return self._latest_email_evaluations

    @latest_email_evaluations.setter
    def latest_email_evaluations(self, latest_email_evaluations: Dict[str, 'MessageEvaluation']) -> None:
        """
        Sets the latest_email_evaluations of this WritableDialerContact.
        A map of email records for the contact email columns.

        :param latest_email_evaluations: The latest_email_evaluations of this WritableDialerContact.
        :type: dict(str, MessageEvaluation)
        """
        

        self._latest_email_evaluations = latest_email_evaluations

    @property
    def callable(self) -> bool:
        """
        Gets the callable of this WritableDialerContact.
        Indicates whether or not the contact can be called.

        :return: The callable of this WritableDialerContact.
        :rtype: bool
        """
        return self._callable

    @callable.setter
    def callable(self, callable: bool) -> None:
        """
        Sets the callable of this WritableDialerContact.
        Indicates whether or not the contact can be called.

        :param callable: The callable of this WritableDialerContact.
        :type: bool
        """
        

        self._callable = callable

    @property
    def phone_number_status(self) -> Dict[str, 'PhoneNumberStatus']:
        """
        Gets the phone_number_status of this WritableDialerContact.
        A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not.

        :return: The phone_number_status of this WritableDialerContact.
        :rtype: dict(str, PhoneNumberStatus)
        """
        return self._phone_number_status

    @phone_number_status.setter
    def phone_number_status(self, phone_number_status: Dict[str, 'PhoneNumberStatus']) -> None:
        """
        Sets the phone_number_status of this WritableDialerContact.
        A map of phone number columns to PhoneNumberStatuses, which indicate if the phone number is callable or not.

        :param phone_number_status: The phone_number_status of this WritableDialerContact.
        :type: dict(str, PhoneNumberStatus)
        """
        

        self._phone_number_status = phone_number_status

    @property
    def contactable_status(self) -> Dict[str, 'ContactableStatus']:
        """
        Gets the contactable_status of this WritableDialerContact.
        A map of media types (Voice, SMS and Email) to ContactableStatus, which indicates if the contact can be contacted using the specified media type.

        :return: The contactable_status of this WritableDialerContact.
        :rtype: dict(str, ContactableStatus)
        """
        return self._contactable_status

    @contactable_status.setter
    def contactable_status(self, contactable_status: Dict[str, 'ContactableStatus']) -> None:
        """
        Sets the contactable_status of this WritableDialerContact.
        A map of media types (Voice, SMS and Email) to ContactableStatus, which indicates if the contact can be contacted using the specified media type.

        :param contactable_status: The contactable_status of this WritableDialerContact.
        :type: dict(str, ContactableStatus)
        """
        

        self._contactable_status = contactable_status

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this WritableDialerContact.
        Timestamp for when the contact was added. Contacts added prior to 2023 September 1 may be missing this value. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this WritableDialerContact.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this WritableDialerContact.
        Timestamp for when the contact was added. Contacts added prior to 2023 September 1 may be missing this value. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this WritableDialerContact.
        :type: datetime
        """
        

        self._date_created = date_created

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

