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
    from . import ConversationEventTopicDestination
    from . import ConversationEventTopicInitiator
    from . import ConversationEventTopicModifiedBy

class ConversationEventTopicRecentTransfer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationEventTopicRecentTransfer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'date_issued': 'datetime',
            'initiator': 'ConversationEventTopicInitiator',
            'modified_by': 'ConversationEventTopicModifiedBy',
            'destination': 'ConversationEventTopicDestination',
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
        Gets the id of this ConversationEventTopicRecentTransfer.
        The id of the command.

        :return: The id of this ConversationEventTopicRecentTransfer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this ConversationEventTopicRecentTransfer.
        The id of the command.

        :param id: The id of this ConversationEventTopicRecentTransfer.
        :type: str
        """
        

        self._id = id

    @property
    def state(self) -> str:
        """
        Gets the state of this ConversationEventTopicRecentTransfer.


        :return: The state of this ConversationEventTopicRecentTransfer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this ConversationEventTopicRecentTransfer.


        :param state: The state of this ConversationEventTopicRecentTransfer.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["pending", "active", "complete", "canceled", "failed", "timeout", "unknown"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def date_issued(self) -> datetime:
        """
        Gets the date_issued of this ConversationEventTopicRecentTransfer.
        The date/time that this command was issued.

        :return: The date_issued of this ConversationEventTopicRecentTransfer.
        :rtype: datetime
        """
        return self._date_issued

    @date_issued.setter
    def date_issued(self, date_issued: datetime) -> None:
        """
        Sets the date_issued of this ConversationEventTopicRecentTransfer.
        The date/time that this command was issued.

        :param date_issued: The date_issued of this ConversationEventTopicRecentTransfer.
        :type: datetime
        """
        

        self._date_issued = date_issued

    @property
    def initiator(self) -> 'ConversationEventTopicInitiator':
        """
        Gets the initiator of this ConversationEventTopicRecentTransfer.


        :return: The initiator of this ConversationEventTopicRecentTransfer.
        :rtype: ConversationEventTopicInitiator
        """
        return self._initiator

    @initiator.setter
    def initiator(self, initiator: 'ConversationEventTopicInitiator') -> None:
        """
        Sets the initiator of this ConversationEventTopicRecentTransfer.


        :param initiator: The initiator of this ConversationEventTopicRecentTransfer.
        :type: ConversationEventTopicInitiator
        """
        

        self._initiator = initiator

    @property
    def modified_by(self) -> 'ConversationEventTopicModifiedBy':
        """
        Gets the modified_by of this ConversationEventTopicRecentTransfer.


        :return: The modified_by of this ConversationEventTopicRecentTransfer.
        :rtype: ConversationEventTopicModifiedBy
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'ConversationEventTopicModifiedBy') -> None:
        """
        Sets the modified_by of this ConversationEventTopicRecentTransfer.


        :param modified_by: The modified_by of this ConversationEventTopicRecentTransfer.
        :type: ConversationEventTopicModifiedBy
        """
        

        self._modified_by = modified_by

    @property
    def destination(self) -> 'ConversationEventTopicDestination':
        """
        Gets the destination of this ConversationEventTopicRecentTransfer.


        :return: The destination of this ConversationEventTopicRecentTransfer.
        :rtype: ConversationEventTopicDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination: 'ConversationEventTopicDestination') -> None:
        """
        Sets the destination of this ConversationEventTopicRecentTransfer.


        :param destination: The destination of this ConversationEventTopicRecentTransfer.
        :type: ConversationEventTopicDestination
        """
        

        self._destination = destination

    @property
    def transfer_type(self) -> str:
        """
        Gets the transfer_type of this ConversationEventTopicRecentTransfer.
        The type of transfer to perform.

        :return: The transfer_type of this ConversationEventTopicRecentTransfer.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type: str) -> None:
        """
        Sets the transfer_type of this ConversationEventTopicRecentTransfer.
        The type of transfer to perform.

        :param transfer_type: The transfer_type of this ConversationEventTopicRecentTransfer.
        :type: str
        """
        if isinstance(transfer_type, int):
            transfer_type = str(transfer_type)
        allowed_values = ["attended", "unattended"]
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

