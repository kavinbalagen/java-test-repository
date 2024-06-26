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
    from . import TemplateParameter

class MessagingTemplateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MessagingTemplateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'response_id': 'str',
            'parameters': 'list[TemplateParameter]'
        }

        self.attribute_map = {
            'response_id': 'responseId',
            'parameters': 'parameters'
        }

        self._response_id = None
        self._parameters = None

    @property
    def response_id(self) -> str:
        """
        Gets the response_id of this MessagingTemplateRequest.
        A Response Management response identifier for a messaging template defined response

        :return: The response_id of this MessagingTemplateRequest.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id: str) -> None:
        """
        Sets the response_id of this MessagingTemplateRequest.
        A Response Management response identifier for a messaging template defined response

        :param response_id: The response_id of this MessagingTemplateRequest.
        :type: str
        """
        

        self._response_id = response_id

    @property
    def parameters(self) -> List['TemplateParameter']:
        """
        Gets the parameters of this MessagingTemplateRequest.
        A list of Response Management response substitutions for the response's messaging template

        :return: The parameters of this MessagingTemplateRequest.
        :rtype: list[TemplateParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: List['TemplateParameter']) -> None:
        """
        Sets the parameters of this MessagingTemplateRequest.
        A list of Response Management response substitutions for the response's messaging template

        :param parameters: The parameters of this MessagingTemplateRequest.
        :type: list[TemplateParameter]
        """
        

        self._parameters = parameters

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

