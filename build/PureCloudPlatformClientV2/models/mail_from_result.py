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
    from . import Record

class MailFromResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MailFromResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'records': 'list[Record]',
            'mail_from_domain': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'records': 'records',
            'mail_from_domain': 'mailFromDomain'
        }

        self._status = None
        self._records = None
        self._mail_from_domain = None

    @property
    def status(self) -> str:
        """
        Gets the status of this MailFromResult.
        The verification status.

        :return: The status of this MailFromResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this MailFromResult.
        The verification status.

        :param status: The status of this MailFromResult.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["FAILED", "PENDING", "VERIFIED", "UNKNOWN"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def records(self) -> List['Record']:
        """
        Gets the records of this MailFromResult.
        The list of DNS records that pertain that need to exist for verification.

        :return: The records of this MailFromResult.
        :rtype: list[Record]
        """
        return self._records

    @records.setter
    def records(self, records: List['Record']) -> None:
        """
        Sets the records of this MailFromResult.
        The list of DNS records that pertain that need to exist for verification.

        :param records: The records of this MailFromResult.
        :type: list[Record]
        """
        

        self._records = records

    @property
    def mail_from_domain(self) -> str:
        """
        Gets the mail_from_domain of this MailFromResult.
        The custom MAIL FROM domain.

        :return: The mail_from_domain of this MailFromResult.
        :rtype: str
        """
        return self._mail_from_domain

    @mail_from_domain.setter
    def mail_from_domain(self, mail_from_domain: str) -> None:
        """
        Sets the mail_from_domain of this MailFromResult.
        The custom MAIL FROM domain.

        :param mail_from_domain: The mail_from_domain of this MailFromResult.
        :type: str
        """
        

        self._mail_from_domain = mail_from_domain

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

