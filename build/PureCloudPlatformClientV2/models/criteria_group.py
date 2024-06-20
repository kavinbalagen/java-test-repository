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
    from . import CriteriaItem

class CriteriaGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CriteriaGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pcAnd': 'list[CriteriaItem]',
            'pcOr': 'list[CriteriaItem]',
            'pcNot': 'list[CriteriaItem]',
            'criteria': 'CriteriaItem'
        }

        self.attribute_map = {
            'pcAnd': 'and',
            'pcOr': 'or',
            'pcNot': 'not',
            'criteria': 'criteria'
        }

        self._pcAnd = None
        self._pcOr = None
        self._pcNot = None
        self._criteria = None

    @property
    def pcAnd(self) -> List['CriteriaItem']:
        """
        Gets the pcAnd of this CriteriaGroup.
        These criteriaItems will be AND'd together to find a match.

        :return: The pcAnd of this CriteriaGroup.
        :rtype: list[CriteriaItem]
        """
        return self._pcAnd

    @pcAnd.setter
    def pcAnd(self, pcAnd: List['CriteriaItem']) -> None:
        """
        Sets the pcAnd of this CriteriaGroup.
        These criteriaItems will be AND'd together to find a match.

        :param pcAnd: The pcAnd of this CriteriaGroup.
        :type: list[CriteriaItem]
        """
        

        self._pcAnd = pcAnd

    @property
    def pcOr(self) -> List['CriteriaItem']:
        """
        Gets the pcOr of this CriteriaGroup.
        These criteriaItems will be OR'd together to find a match.

        :return: The pcOr of this CriteriaGroup.
        :rtype: list[CriteriaItem]
        """
        return self._pcOr

    @pcOr.setter
    def pcOr(self, pcOr: List['CriteriaItem']) -> None:
        """
        Sets the pcOr of this CriteriaGroup.
        These criteriaItems will be OR'd together to find a match.

        :param pcOr: The pcOr of this CriteriaGroup.
        :type: list[CriteriaItem]
        """
        

        self._pcOr = pcOr

    @property
    def pcNot(self) -> List['CriteriaItem']:
        """
        Gets the pcNot of this CriteriaGroup.
        These criteriaItems must all be false to find a match.

        :return: The pcNot of this CriteriaGroup.
        :rtype: list[CriteriaItem]
        """
        return self._pcNot

    @pcNot.setter
    def pcNot(self, pcNot: List['CriteriaItem']) -> None:
        """
        Sets the pcNot of this CriteriaGroup.
        These criteriaItems must all be false to find a match.

        :param pcNot: The pcNot of this CriteriaGroup.
        :type: list[CriteriaItem]
        """
        

        self._pcNot = pcNot

    @property
    def criteria(self) -> 'CriteriaItem':
        """
        Gets the criteria of this CriteriaGroup.
        A singular critieriaItem to match.

        :return: The criteria of this CriteriaGroup.
        :rtype: CriteriaItem
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria: 'CriteriaItem') -> None:
        """
        Sets the criteria of this CriteriaGroup.
        A singular critieriaItem to match.

        :param criteria: The criteria of this CriteriaGroup.
        :type: CriteriaItem
        """
        

        self._criteria = criteria

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

