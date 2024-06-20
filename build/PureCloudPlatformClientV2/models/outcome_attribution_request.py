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
    from . import Touchpoint

class OutcomeAttributionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OutcomeAttributionRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'outcome_id': 'str',
            'external_contact_id': 'str',
            'associated_value': 'float',
            'touchpoints': 'list[Touchpoint]',
            'created_date': 'datetime'
        }

        self.attribute_map = {
            'outcome_id': 'outcomeId',
            'external_contact_id': 'externalContactId',
            'associated_value': 'associatedValue',
            'touchpoints': 'touchpoints',
            'created_date': 'createdDate'
        }

        self._outcome_id = None
        self._external_contact_id = None
        self._associated_value = None
        self._touchpoints = None
        self._created_date = None

    @property
    def outcome_id(self) -> str:
        """
        Gets the outcome_id of this OutcomeAttributionRequest.
        ID of Outcome.

        :return: The outcome_id of this OutcomeAttributionRequest.
        :rtype: str
        """
        return self._outcome_id

    @outcome_id.setter
    def outcome_id(self, outcome_id: str) -> None:
        """
        Sets the outcome_id of this OutcomeAttributionRequest.
        ID of Outcome.

        :param outcome_id: The outcome_id of this OutcomeAttributionRequest.
        :type: str
        """
        

        self._outcome_id = outcome_id

    @property
    def external_contact_id(self) -> str:
        """
        Gets the external_contact_id of this OutcomeAttributionRequest.
        The external contact ID of the customer who achieved the outcome.

        :return: The external_contact_id of this OutcomeAttributionRequest.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id: str) -> None:
        """
        Sets the external_contact_id of this OutcomeAttributionRequest.
        The external contact ID of the customer who achieved the outcome.

        :param external_contact_id: The external_contact_id of this OutcomeAttributionRequest.
        :type: str
        """
        

        self._external_contact_id = external_contact_id

    @property
    def associated_value(self) -> float:
        """
        Gets the associated_value of this OutcomeAttributionRequest.
        The total value associated with the customer's outcome.

        :return: The associated_value of this OutcomeAttributionRequest.
        :rtype: float
        """
        return self._associated_value

    @associated_value.setter
    def associated_value(self, associated_value: float) -> None:
        """
        Sets the associated_value of this OutcomeAttributionRequest.
        The total value associated with the customer's outcome.

        :param associated_value: The associated_value of this OutcomeAttributionRequest.
        :type: float
        """
        

        self._associated_value = associated_value

    @property
    def touchpoints(self) -> List['Touchpoint']:
        """
        Gets the touchpoints of this OutcomeAttributionRequest.
        List of interactions that led to this outcome being achieved.

        :return: The touchpoints of this OutcomeAttributionRequest.
        :rtype: list[Touchpoint]
        """
        return self._touchpoints

    @touchpoints.setter
    def touchpoints(self, touchpoints: List['Touchpoint']) -> None:
        """
        Sets the touchpoints of this OutcomeAttributionRequest.
        List of interactions that led to this outcome being achieved.

        :param touchpoints: The touchpoints of this OutcomeAttributionRequest.
        :type: list[Touchpoint]
        """
        

        self._touchpoints = touchpoints

    @property
    def created_date(self) -> datetime:
        """
        Gets the created_date of this OutcomeAttributionRequest.
        Date outcome was achieved. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date of this OutcomeAttributionRequest.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date: datetime) -> None:
        """
        Sets the created_date of this OutcomeAttributionRequest.
        Date outcome was achieved. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date: The created_date of this OutcomeAttributionRequest.
        :type: datetime
        """
        

        self._created_date = created_date

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

