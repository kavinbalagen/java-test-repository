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


class LearningAssignmentStepScoStructure(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LearningAssignmentStepScoStructure - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'success_status': 'str',
            'completion_status': 'str',
            'children': 'list[LearningAssignmentStepScoStructure]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'success_status': 'successStatus',
            'completion_status': 'completionStatus',
            'children': 'children'
        }

        self._id = None
        self._name = None
        self._success_status = None
        self._completion_status = None
        self._children = None

    @property
    def id(self) -> str:
        """
        Gets the id of this LearningAssignmentStepScoStructure.
        The id of this SCO in the course manifest

        :return: The id of this LearningAssignmentStepScoStructure.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this LearningAssignmentStepScoStructure.
        The id of this SCO in the course manifest

        :param id: The id of this LearningAssignmentStepScoStructure.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this LearningAssignmentStepScoStructure.
        The name of this SCO in the course manifest

        :return: The name of this LearningAssignmentStepScoStructure.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this LearningAssignmentStepScoStructure.
        The name of this SCO in the course manifest

        :param name: The name of this LearningAssignmentStepScoStructure.
        :type: str
        """
        

        self._name = name

    @property
    def success_status(self) -> str:
        """
        Gets the success_status of this LearningAssignmentStepScoStructure.
        The success status of this SCO

        :return: The success_status of this LearningAssignmentStepScoStructure.
        :rtype: str
        """
        return self._success_status

    @success_status.setter
    def success_status(self, success_status: str) -> None:
        """
        Sets the success_status of this LearningAssignmentStepScoStructure.
        The success status of this SCO

        :param success_status: The success_status of this LearningAssignmentStepScoStructure.
        :type: str
        """
        if isinstance(success_status, int):
            success_status = str(success_status)
        allowed_values = ["Passed", "Failed", "Unknown"]
        if success_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for success_status -> " + success_status)
            self._success_status = "outdated_sdk_version"
        else:
            self._success_status = success_status

    @property
    def completion_status(self) -> str:
        """
        Gets the completion_status of this LearningAssignmentStepScoStructure.
        The completion status of this SCO

        :return: The completion_status of this LearningAssignmentStepScoStructure.
        :rtype: str
        """
        return self._completion_status

    @completion_status.setter
    def completion_status(self, completion_status: str) -> None:
        """
        Sets the completion_status of this LearningAssignmentStepScoStructure.
        The completion status of this SCO

        :param completion_status: The completion_status of this LearningAssignmentStepScoStructure.
        :type: str
        """
        if isinstance(completion_status, int):
            completion_status = str(completion_status)
        allowed_values = ["Completed", "Incomplete", "NotAttempted", "Unknown"]
        if completion_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for completion_status -> " + completion_status)
            self._completion_status = "outdated_sdk_version"
        else:
            self._completion_status = completion_status

    @property
    def children(self) -> List['LearningAssignmentStepScoStructure']:
        """
        Gets the children of this LearningAssignmentStepScoStructure.
        Child items belonging to this SCO in the course manifest

        :return: The children of this LearningAssignmentStepScoStructure.
        :rtype: list[LearningAssignmentStepScoStructure]
        """
        return self._children

    @children.setter
    def children(self, children: List['LearningAssignmentStepScoStructure']) -> None:
        """
        Sets the children of this LearningAssignmentStepScoStructure.
        Child items belonging to this SCO in the course manifest

        :param children: The children of this LearningAssignmentStepScoStructure.
        :type: list[LearningAssignmentStepScoStructure]
        """
        

        self._children = children

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

