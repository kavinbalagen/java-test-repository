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


class ArchitectFlowNotificationErrorDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ArchitectFlowNotificationErrorDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_code': 'str',
            'entity_id': 'str',
            'entity_name': 'str',
            'field_name': 'str'
        }

        self.attribute_map = {
            'error_code': 'errorCode',
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'field_name': 'fieldName'
        }

        self._error_code = None
        self._entity_id = None
        self._entity_name = None
        self._field_name = None

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this ArchitectFlowNotificationErrorDetail.


        :return: The error_code of this ArchitectFlowNotificationErrorDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this ArchitectFlowNotificationErrorDetail.


        :param error_code: The error_code of this ArchitectFlowNotificationErrorDetail.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def entity_id(self) -> str:
        """
        Gets the entity_id of this ArchitectFlowNotificationErrorDetail.


        :return: The entity_id of this ArchitectFlowNotificationErrorDetail.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id: str) -> None:
        """
        Sets the entity_id of this ArchitectFlowNotificationErrorDetail.


        :param entity_id: The entity_id of this ArchitectFlowNotificationErrorDetail.
        :type: str
        """
        

        self._entity_id = entity_id

    @property
    def entity_name(self) -> str:
        """
        Gets the entity_name of this ArchitectFlowNotificationErrorDetail.


        :return: The entity_name of this ArchitectFlowNotificationErrorDetail.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name: str) -> None:
        """
        Sets the entity_name of this ArchitectFlowNotificationErrorDetail.


        :param entity_name: The entity_name of this ArchitectFlowNotificationErrorDetail.
        :type: str
        """
        

        self._entity_name = entity_name

    @property
    def field_name(self) -> str:
        """
        Gets the field_name of this ArchitectFlowNotificationErrorDetail.


        :return: The field_name of this ArchitectFlowNotificationErrorDetail.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name: str) -> None:
        """
        Sets the field_name of this ArchitectFlowNotificationErrorDetail.


        :param field_name: The field_name of this ArchitectFlowNotificationErrorDetail.
        :type: str
        """
        

        self._field_name = field_name

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

