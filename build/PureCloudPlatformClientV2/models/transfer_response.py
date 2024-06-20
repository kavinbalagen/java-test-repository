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
    from . import TransferDestination
    from . import TransferInitiator
    from . import TransferResponseModifiedBy

class TransferResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TransferResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'date_issued': 'datetime',
            'initiator': 'TransferInitiator',
            'modified_by': 'TransferResponseModifiedBy',
            'destination': 'TransferDestination',
            'transfer_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'date_issued': 'dateIssued',
            'initiator': 'initiator',
            'modified_by': 'modifiedBy',
            'destination': 'destination',
            'transfer_type': 'transferType'
        }

        self._id = None
        self._state = None
        self._date_issued = None
        self._initiator = None
        self._modified_by = None
        self._destination = None
        self._transfer_type = None

    @property
    def id(self) -> str:
        """
        Gets the id of this TransferResponse.
        The id of the command.

        :return: The id of this TransferResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this TransferResponse.
        The id of the command.

        :param id: The id of this TransferResponse.
        :type: str
        """
        

        self._id = id

    @property
    def state(self) -> str:
        """
        Gets the state of this TransferResponse.
        The state of the command.

        :return: The state of this TransferResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this TransferResponse.
        The state of the command.

        :param state: The state of this TransferResponse.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Pending", "Active", "Complete", "Canceled", "Failed", "Timeout", "Unknown"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def date_issued(self) -> datetime:
        """
        Gets the date_issued of this TransferResponse.
        The date/time that this command was issued. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_issued of this TransferResponse.
        :rtype: datetime
        """
        return self._date_issued

    @date_issued.setter
    def date_issued(self, date_issued: datetime) -> None:
        """
        Sets the date_issued of this TransferResponse.
        The date/time that this command was issued. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_issued: The date_issued of this TransferResponse.
        :type: datetime
        """
        

        self._date_issued = date_issued

    @property
    def initiator(self) -> 'TransferInitiator':
        """
        Gets the initiator of this TransferResponse.
        The initiator of the command.

        :return: The initiator of this TransferResponse.
        :rtype: TransferInitiator
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator: 'TransferInitiator') -> None:
        """
        Sets the initiator of this TransferResponse.
        The initiator of the command.

        :param initiator: The initiator of this TransferResponse.
        :type: TransferInitiator
        """
        

        self._initiator = initiator

    @property
    def modified_by(self) -> 'TransferResponseModifiedBy':
        """
        Gets the modified_by of this TransferResponse.
        The user or entity that modified the command.

        :return: The modified_by of this TransferResponse.
        :rtype: TransferResponseModifiedBy
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'TransferResponseModifiedBy') -> None:
        """
        Sets the modified_by of this TransferResponse.
        The user or entity that modified the command.

        :param modified_by: The modified_by of this TransferResponse.
        :type: TransferResponseModifiedBy
        """
        

        self._modified_by = modified_by

    @property
    def destination(self) -> 'TransferDestination':
        """
        Gets the destination of this TransferResponse.
        The destination of the command.

        :return: The destination of this TransferResponse.
        :rtype: TransferDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination: 'TransferDestination') -> None:
        """
        Sets the destination of this TransferResponse.
        The destination of the command.

        :param destination: The destination of this TransferResponse.
        :type: TransferDestination
        """
        

        self._destination = destination

    @property
    def transfer_type(self) -> str:
        """
        Gets the transfer_type of this TransferResponse.
        The type of transfer to perform.

        :return: The transfer_type of this TransferResponse.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type: str) -> None:
        """
        Sets the transfer_type of this TransferResponse.
        The type of transfer to perform.

        :param transfer_type: The transfer_type of this TransferResponse.
        :type: str
        """
        if isinstance(transfer_type, int):
            transfer_type = str(transfer_type)
        allowed_values = ["Attended", "Unattended"]
        if transfer_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for transfer_type -> " + transfer_type)
            self._transfer_type = "outdated_sdk_version"
        else:
            self._transfer_type = transfer_type

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

