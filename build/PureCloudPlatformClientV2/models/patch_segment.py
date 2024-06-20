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
    from . import PatchContext
    from . import PatchExternalSegment
    from . import PatchJourney

class PatchSegment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        PatchSegment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'is_active': 'bool',
            'display_name': 'str',
            'version': 'int',
            'description': 'str',
            'color': 'str',
            'should_display_to_agent': 'bool',
            'context': 'PatchContext',
            'journey': 'PatchJourney',
            'external_segment': 'PatchExternalSegment',
            'assignment_expiration_days': 'int'
        }

        self.attribute_map = {
            'is_active': 'isActive',
            'display_name': 'displayName',
            'version': 'version',
            'description': 'description',
            'color': 'color',
            'should_display_to_agent': 'shouldDisplayToAgent',
            'context': 'context',
            'journey': 'journey',
            'external_segment': 'externalSegment',
            'assignment_expiration_days': 'assignmentExpirationDays'
        }

        self._is_active = None
        self._display_name = None
        self._version = None
        self._description = None
        self._color = None
        self._should_display_to_agent = None
        self._context = None
        self._journey = None
        self._external_segment = None
        self._assignment_expiration_days = None

    @property
    def is_active(self) -> bool:
        """
        Gets the is_active of this PatchSegment.
        Whether or not the segment is active.

        :return: The is_active of this PatchSegment.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool) -> None:
        """
        Sets the is_active of this PatchSegment.
        Whether or not the segment is active.

        :param is_active: The is_active of this PatchSegment.
        :type: bool
        """
        

        self._is_active = is_active

    @property
    def display_name(self) -> str:
        """
        Gets the display_name of this PatchSegment.
        The display name of the segment.

        :return: The display_name of this PatchSegment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name: str) -> None:
        """
        Sets the display_name of this PatchSegment.
        The display name of the segment.

        :param display_name: The display_name of this PatchSegment.
        :type: str
        """
        

        self._display_name = display_name

    @property
    def version(self) -> int:
        """
        Gets the version of this PatchSegment.
        The version of the segment.

        :return: The version of this PatchSegment.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this PatchSegment.
        The version of the segment.

        :param version: The version of this PatchSegment.
        :type: int
        """
        

        self._version = version

    @property
    def description(self) -> str:
        """
        Gets the description of this PatchSegment.
        A description of the segment.

        :return: The description of this PatchSegment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this PatchSegment.
        A description of the segment.

        :param description: The description of this PatchSegment.
        :type: str
        """
        

        self._description = description

    @property
    def color(self) -> str:
        """
        Gets the color of this PatchSegment.
        The hexadecimal color value of the segment.

        :return: The color of this PatchSegment.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        """
        Sets the color of this PatchSegment.
        The hexadecimal color value of the segment.

        :param color: The color of this PatchSegment.
        :type: str
        """
        

        self._color = color

    @property
    def should_display_to_agent(self) -> bool:
        """
        Gets the should_display_to_agent of this PatchSegment.
        Whether or not the segment should be displayed to agent/supervisor users.

        :return: The should_display_to_agent of this PatchSegment.
        :rtype: bool
        """
        return self._should_display_to_agent

    @should_display_to_agent.setter
    def should_display_to_agent(self, should_display_to_agent: bool) -> None:
        """
        Sets the should_display_to_agent of this PatchSegment.
        Whether or not the segment should be displayed to agent/supervisor users.

        :param should_display_to_agent: The should_display_to_agent of this PatchSegment.
        :type: bool
        """
        

        self._should_display_to_agent = should_display_to_agent

    @property
    def context(self) -> 'PatchContext':
        """
        Gets the context of this PatchSegment.
        The context of the segment.

        :return: The context of this PatchSegment.
        :rtype: PatchContext
        """
        return self._context

    @context.setter
    def context(self, context: 'PatchContext') -> None:
        """
        Sets the context of this PatchSegment.
        The context of the segment.

        :param context: The context of this PatchSegment.
        :type: PatchContext
        """
        

        self._context = context

    @property
    def journey(self) -> 'PatchJourney':
        """
        Gets the journey of this PatchSegment.
        The pattern of rules defining the segment.

        :return: The journey of this PatchSegment.
        :rtype: PatchJourney
        """
        return self._journey

    @journey.setter
    def journey(self, journey: 'PatchJourney') -> None:
        """
        Sets the journey of this PatchSegment.
        The pattern of rules defining the segment.

        :param journey: The journey of this PatchSegment.
        :type: PatchJourney
        """
        

        self._journey = journey

    @property
    def external_segment(self) -> 'PatchExternalSegment':
        """
        Gets the external_segment of this PatchSegment.
        Details of an entity corresponding to this segment in an external system.

        :return: The external_segment of this PatchSegment.
        :rtype: PatchExternalSegment
        """
        return self._external_segment

    @external_segment.setter
    def external_segment(self, external_segment: 'PatchExternalSegment') -> None:
        """
        Sets the external_segment of this PatchSegment.
        Details of an entity corresponding to this segment in an external system.

        :param external_segment: The external_segment of this PatchSegment.
        :type: PatchExternalSegment
        """
        

        self._external_segment = external_segment

    @property
    def assignment_expiration_days(self) -> int:
        """
        Gets the assignment_expiration_days of this PatchSegment.
        Time, in days, from when the segment is assigned until it is automatically unassigned.

        :return: The assignment_expiration_days of this PatchSegment.
        :rtype: int
        """
        return self._assignment_expiration_days

    @assignment_expiration_days.setter
    def assignment_expiration_days(self, assignment_expiration_days: int) -> None:
        """
        Sets the assignment_expiration_days of this PatchSegment.
        Time, in days, from when the segment is assigned until it is automatically unassigned.

        :param assignment_expiration_days: The assignment_expiration_days of this PatchSegment.
        :type: int
        """
        

        self._assignment_expiration_days = assignment_expiration_days

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
