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


class PasswordRequirements(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PasswordRequirements - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'minimum_length': 'int',
            'minimum_digits': 'int',
            'minimum_letters': 'int',
            'minimum_upper': 'int',
            'minimum_lower': 'int',
            'minimum_specials': 'int',
            'minimum_age_seconds': 'int',
            'expiration_days': 'int'
        }

        self.attribute_map = {
            'minimum_length': 'minimumLength',
            'minimum_digits': 'minimumDigits',
            'minimum_letters': 'minimumLetters',
            'minimum_upper': 'minimumUpper',
            'minimum_lower': 'minimumLower',
            'minimum_specials': 'minimumSpecials',
            'minimum_age_seconds': 'minimumAgeSeconds',
            'expiration_days': 'expirationDays'
        }

        self._minimum_length = None
        self._minimum_digits = None
        self._minimum_letters = None
        self._minimum_upper = None
        self._minimum_lower = None
        self._minimum_specials = None
        self._minimum_age_seconds = None
        self._expiration_days = None

    @property
    def minimum_length(self) -> int:
        """
        Gets the minimum_length of this PasswordRequirements.


        :return: The minimum_length of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_length

    @minimum_length.setter
    def minimum_length(self, minimum_length: int) -> None:
        """
        Sets the minimum_length of this PasswordRequirements.


        :param minimum_length: The minimum_length of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_length = minimum_length

    @property
    def minimum_digits(self) -> int:
        """
        Gets the minimum_digits of this PasswordRequirements.


        :return: The minimum_digits of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_digits

    @minimum_digits.setter
    def minimum_digits(self, minimum_digits: int) -> None:
        """
        Sets the minimum_digits of this PasswordRequirements.


        :param minimum_digits: The minimum_digits of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_digits = minimum_digits

    @property
    def minimum_letters(self) -> int:
        """
        Gets the minimum_letters of this PasswordRequirements.


        :return: The minimum_letters of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_letters

    @minimum_letters.setter
    def minimum_letters(self, minimum_letters: int) -> None:
        """
        Sets the minimum_letters of this PasswordRequirements.


        :param minimum_letters: The minimum_letters of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_letters = minimum_letters

    @property
    def minimum_upper(self) -> int:
        """
        Gets the minimum_upper of this PasswordRequirements.


        :return: The minimum_upper of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_upper

    @minimum_upper.setter
    def minimum_upper(self, minimum_upper: int) -> None:
        """
        Sets the minimum_upper of this PasswordRequirements.


        :param minimum_upper: The minimum_upper of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_upper = minimum_upper

    @property
    def minimum_lower(self) -> int:
        """
        Gets the minimum_lower of this PasswordRequirements.


        :return: The minimum_lower of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_lower

    @minimum_lower.setter
    def minimum_lower(self, minimum_lower: int) -> None:
        """
        Sets the minimum_lower of this PasswordRequirements.


        :param minimum_lower: The minimum_lower of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_lower = minimum_lower

    @property
    def minimum_specials(self) -> int:
        """
        Gets the minimum_specials of this PasswordRequirements.


        :return: The minimum_specials of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_specials

    @minimum_specials.setter
    def minimum_specials(self, minimum_specials: int) -> None:
        """
        Sets the minimum_specials of this PasswordRequirements.


        :param minimum_specials: The minimum_specials of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_specials = minimum_specials

    @property
    def minimum_age_seconds(self) -> int:
        """
        Gets the minimum_age_seconds of this PasswordRequirements.


        :return: The minimum_age_seconds of this PasswordRequirements.
        :rtype: int
        """
        return self._minimum_age_seconds

    @minimum_age_seconds.setter
    def minimum_age_seconds(self, minimum_age_seconds: int) -> None:
        """
        Sets the minimum_age_seconds of this PasswordRequirements.


        :param minimum_age_seconds: The minimum_age_seconds of this PasswordRequirements.
        :type: int
        """
        

        self._minimum_age_seconds = minimum_age_seconds

    @property
    def expiration_days(self) -> int:
        """
        Gets the expiration_days of this PasswordRequirements.


        :return: The expiration_days of this PasswordRequirements.
        :rtype: int
        """
        return self._expiration_days

    @expiration_days.setter
    def expiration_days(self, expiration_days: int) -> None:
        """
        Sets the expiration_days of this PasswordRequirements.


        :param expiration_days: The expiration_days of this PasswordRequirements.
        :type: int
        """
        

        self._expiration_days = expiration_days

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

