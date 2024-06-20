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
    from . import ActionConfig
    from . import ActionContractInput

class PostActionInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PostActionInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'name': 'str',
            'integration_id': 'str',
            'config': 'ActionConfig',
            'contract': 'ActionContractInput',
            'secure': 'bool'
        }

        self.attribute_map = {
            'category': 'category',
            'name': 'name',
            'integration_id': 'integrationId',
            'config': 'config',
            'contract': 'contract',
            'secure': 'secure'
        }

        self._category = None
        self._name = None
        self._integration_id = None
        self._config = None
        self._contract = None
        self._secure = None

    @property
    def category(self) -> str:
        """
        Gets the category of this PostActionInput.
        Category of action, Can be up to 256 characters long

        :return: The category of this PostActionInput.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Sets the category of this PostActionInput.
        Category of action, Can be up to 256 characters long

        :param category: The category of this PostActionInput.
        :type: str
        """
        

        self._category = category

    @property
    def name(self) -> str:
        """
        Gets the name of this PostActionInput.
        Name of action, Can be up to 256 characters long

        :return: The name of this PostActionInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this PostActionInput.
        Name of action, Can be up to 256 characters long

        :param name: The name of this PostActionInput.
        :type: str
        """
        

        self._name = name

    @property
    def integration_id(self) -> str:
        """
        Gets the integration_id of this PostActionInput.
        The ID of the integration this action is associated to

        :return: The integration_id of this PostActionInput.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id: str) -> None:
        """
        Sets the integration_id of this PostActionInput.
        The ID of the integration this action is associated to

        :param integration_id: The integration_id of this PostActionInput.
        :type: str
        """
        

        self._integration_id = integration_id

    @property
    def config(self) -> 'ActionConfig':
        """
        Gets the config of this PostActionInput.
        Configuration to support request and response processing

        :return: The config of this PostActionInput.
        :rtype: ActionConfig
        """
        return self._config

    @config.setter
    def config(self, config: 'ActionConfig') -> None:
        """
        Sets the config of this PostActionInput.
        Configuration to support request and response processing

        :param config: The config of this PostActionInput.
        :type: ActionConfig
        """
        

        self._config = config

    @property
    def contract(self) -> 'ActionContractInput':
        """
        Gets the contract of this PostActionInput.
        Action contract

        :return: The contract of this PostActionInput.
        :rtype: ActionContractInput
        """
        return self._contract

    @contract.setter
    def contract(self, contract: 'ActionContractInput') -> None:
        """
        Sets the contract of this PostActionInput.
        Action contract

        :param contract: The contract of this PostActionInput.
        :type: ActionContractInput
        """
        

        self._contract = contract

    @property
    def secure(self) -> bool:
        """
        Gets the secure of this PostActionInput.
        Indication of whether or not the action is designed to accept sensitive data

        :return: The secure of this PostActionInput.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure: bool) -> None:
        """
        Sets the secure of this PostActionInput.
        Indication of whether or not the action is designed to accept sensitive data

        :param secure: The secure of this PostActionInput.
        :type: bool
        """
        

        self._secure = secure

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
