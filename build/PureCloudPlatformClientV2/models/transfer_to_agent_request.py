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


class TransferToAgentRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TransferToAgentRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'transfer_type': 'str',
            'user_id': 'str',
            'user_name': 'str',
            'user_display_name': 'str',
            'voicemail': 'bool'
        }

        self.attribute_map = {
            'transfer_type': 'transferType',
            'user_id': 'userId',
            'user_name': 'userName',
            'user_display_name': 'userDisplayName',
            'voicemail': 'voicemail'
        }

        self._transfer_type = None
        self._user_id = None
        self._user_name = None
        self._user_display_name = None
        self._voicemail = None

    @property
    def transfer_type(self) -> str:
        """
        Gets the transfer_type of this TransferToAgentRequest.
        The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended.

        :return: The transfer_type of this TransferToAgentRequest.
        :rtype: str
        """
        return self._transfer_type

    @transfer_type.setter
    def transfer_type(self, transfer_type: str) -> None:
        """
        Sets the transfer_type of this TransferToAgentRequest.
        The type of transfer to perform. Attended, where the initiating agent maintains ownership of the conversation until the intended recipient accepts the transfer, or Unattended, where the initiating agent immediately disconnects. Default is Unattended.

        :param transfer_type: The transfer_type of this TransferToAgentRequest.
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

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this TransferToAgentRequest.
        The id of the internal user.

        :return: The user_id of this TransferToAgentRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this TransferToAgentRequest.
        The id of the internal user.

        :param user_id: The user_id of this TransferToAgentRequest.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def user_name(self) -> str:
        """
        Gets the user_name of this TransferToAgentRequest.
        The userName (like user’s email) of the internal user.

        :return: The user_name of this TransferToAgentRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name: str) -> None:
        """
        Sets the user_name of this TransferToAgentRequest.
        The userName (like user’s email) of the internal user.

        :param user_name: The user_name of this TransferToAgentRequest.
        :type: str
        """
        

        self._user_name = user_name

    @property
    def user_display_name(self) -> str:
        """
        Gets the user_display_name of this TransferToAgentRequest.
        The name of the internal user.

        :return: The user_display_name of this TransferToAgentRequest.
        :rtype: str
        """
        return self._user_display_name

    @user_display_name.setter
    def user_display_name(self, user_display_name: str) -> None:
        """
        Sets the user_display_name of this TransferToAgentRequest.
        The name of the internal user.

        :param user_display_name: The user_display_name of this TransferToAgentRequest.
        :type: str
        """
        

        self._user_display_name = user_display_name

    @property
    def voicemail(self) -> bool:
        """
        Gets the voicemail of this TransferToAgentRequest.
        If true, transfer to the voicemail inbox of the participant that is being replaced.

        :return: The voicemail of this TransferToAgentRequest.
        :rtype: bool
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail: bool) -> None:
        """
        Sets the voicemail of this TransferToAgentRequest.
        If true, transfer to the voicemail inbox of the participant that is being replaced.

        :param voicemail: The voicemail of this TransferToAgentRequest.
        :type: bool
        """
        

        self._voicemail = voicemail

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

