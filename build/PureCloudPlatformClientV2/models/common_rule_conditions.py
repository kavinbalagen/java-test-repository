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
    from . import CommonRulePredicate

class CommonRuleConditions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CommonRuleConditions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'clauses': 'list[CommonRuleConditions]',
            'predicates': 'list[CommonRulePredicate]',
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'clauses': 'clauses',
            'predicates': 'predicates',
            'type': 'type',
            'id': 'id'
        }

        self._clauses = None
        self._predicates = None
        self._type = None
        self._id = None

    @property
    def clauses(self) -> List['CommonRuleConditions']:
        """
        Gets the clauses of this CommonRuleConditions.
        The list of predicates groups to be evaluated

        :return: The clauses of this CommonRuleConditions.
        :rtype: list[CommonRuleConditions]
        """
        return self._clauses

    @clauses.setter
    def clauses(self, clauses: List['CommonRuleConditions']) -> None:
        """
        Sets the clauses of this CommonRuleConditions.
        The list of predicates groups to be evaluated

        :param clauses: The clauses of this CommonRuleConditions.
        :type: list[CommonRuleConditions]
        """
        

        self._clauses = clauses

    @property
    def predicates(self) -> List['CommonRulePredicate']:
        """
        Gets the predicates of this CommonRuleConditions.
        The list of rule metric predicates to be evaluated.

        :return: The predicates of this CommonRuleConditions.
        :rtype: list[CommonRulePredicate]
        """
        return self._predicates

    @predicates.setter
    def predicates(self, predicates: List['CommonRulePredicate']) -> None:
        """
        Sets the predicates of this CommonRuleConditions.
        The list of rule metric predicates to be evaluated.

        :param predicates: The predicates of this CommonRuleConditions.
        :type: list[CommonRulePredicate]
        """
        

        self._predicates = predicates

    @property
    def type(self) -> str:
        """
        Gets the type of this CommonRuleConditions.
        the logic operator performed.

        :return: The type of this CommonRuleConditions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this CommonRuleConditions.
        the logic operator performed.

        :param type: The type of this CommonRuleConditions.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["And", "Or", "Not"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def id(self) -> str:
        """
        Gets the id of this CommonRuleConditions.
        The id.

        :return: The id of this CommonRuleConditions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this CommonRuleConditions.
        The id.

        :param id: The id of this CommonRuleConditions.
        :type: str
        """
        

        self._id = id

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

