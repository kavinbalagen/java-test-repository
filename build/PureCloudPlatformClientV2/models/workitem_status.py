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
    from . import WorkitemStatusReference
    from . import WorktypeReference

class WorkitemStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkitemStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'category': 'str',
            'destination_statuses': 'list[WorkitemStatusReference]',
            'description': 'str',
            'default_destination_status': 'WorkitemStatusReference',
            'status_transition_delay_seconds': 'int',
            'status_transition_time': 'str',
            'worktype': 'WorktypeReference',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'category': 'category',
            'destination_statuses': 'destinationStatuses',
            'description': 'description',
            'default_destination_status': 'defaultDestinationStatus',
            'status_transition_delay_seconds': 'statusTransitionDelaySeconds',
            'status_transition_time': 'statusTransitionTime',
            'worktype': 'worktype',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._category = None
        self._destination_statuses = None
        self._description = None
        self._default_destination_status = None
        self._status_transition_delay_seconds = None
        self._status_transition_time = None
        self._worktype = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WorkitemStatus.
        The globally unique identifier for the object.

        :return: The id of this WorkitemStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WorkitemStatus.
        The globally unique identifier for the object.

        :param id: The id of this WorkitemStatus.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this WorkitemStatus.


        :return: The name of this WorkitemStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this WorkitemStatus.


        :param name: The name of this WorkitemStatus.
        :type: str
        """
        

        self._name = name

    @property
    def category(self) -> str:
        """
        Gets the category of this WorkitemStatus.
        The Category of the Status.

        :return: The category of this WorkitemStatus.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Sets the category of this WorkitemStatus.
        The Category of the Status.

        :param category: The category of this WorkitemStatus.
        :type: str
        """
        if isinstance(category, int):
            category = str(category)
        allowed_values = ["Open", "InProgress", "Waiting", "Closed", "Unknown"]
        if category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for category -> " + category)
            self._category = "outdated_sdk_version"
        else:
            self._category = category

    @property
    def destination_statuses(self) -> List['WorkitemStatusReference']:
        """
        Gets the destination_statuses of this WorkitemStatus.
        The Statuses the Status can transition to.

        :return: The destination_statuses of this WorkitemStatus.
        :rtype: list[WorkitemStatusReference]
        """
        return self._destination_statuses

    @destination_statuses.setter
    def destination_statuses(self, destination_statuses: List['WorkitemStatusReference']) -> None:
        """
        Sets the destination_statuses of this WorkitemStatus.
        The Statuses the Status can transition to.

        :param destination_statuses: The destination_statuses of this WorkitemStatus.
        :type: list[WorkitemStatusReference]
        """
        

        self._destination_statuses = destination_statuses

    @property
    def description(self) -> str:
        """
        Gets the description of this WorkitemStatus.
        The description of the Status.

        :return: The description of this WorkitemStatus.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this WorkitemStatus.
        The description of the Status.

        :param description: The description of this WorkitemStatus.
        :type: str
        """
        

        self._description = description

    @property
    def default_destination_status(self) -> 'WorkitemStatusReference':
        """
        Gets the default_destination_status of this WorkitemStatus.
        Default destination status to which this Status will transition to if auto status transition enabled.

        :return: The default_destination_status of this WorkitemStatus.
        :rtype: WorkitemStatusReference
        """
        return self._default_destination_status

    @default_destination_status.setter
    def default_destination_status(self, default_destination_status: 'WorkitemStatusReference') -> None:
        """
        Sets the default_destination_status of this WorkitemStatus.
        Default destination status to which this Status will transition to if auto status transition enabled.

        :param default_destination_status: The default_destination_status of this WorkitemStatus.
        :type: WorkitemStatusReference
        """
        

        self._default_destination_status = default_destination_status

    @property
    def status_transition_delay_seconds(self) -> int:
        """
        Gets the status_transition_delay_seconds of this WorkitemStatus.
        Delay in seconds for auto status transition

        :return: The status_transition_delay_seconds of this WorkitemStatus.
        :rtype: int
        """
        return self._status_transition_delay_seconds

    @status_transition_delay_seconds.setter
    def status_transition_delay_seconds(self, status_transition_delay_seconds: int) -> None:
        """
        Sets the status_transition_delay_seconds of this WorkitemStatus.
        Delay in seconds for auto status transition

        :param status_transition_delay_seconds: The status_transition_delay_seconds of this WorkitemStatus.
        :type: int
        """
        

        self._status_transition_delay_seconds = status_transition_delay_seconds

    @property
    def status_transition_time(self) -> str:
        """
        Gets the status_transition_time of this WorkitemStatus.
        Time is represented as an ISO-8601 string without a timezone. For example: HH:mm:ss.SSS

        :return: The status_transition_time of this WorkitemStatus.
        :rtype: str
        """
        return self._status_transition_time

    @status_transition_time.setter
    def status_transition_time(self, status_transition_time: str) -> None:
        """
        Sets the status_transition_time of this WorkitemStatus.
        Time is represented as an ISO-8601 string without a timezone. For example: HH:mm:ss.SSS

        :param status_transition_time: The status_transition_time of this WorkitemStatus.
        :type: str
        """
        

        self._status_transition_time = status_transition_time

    @property
    def worktype(self) -> 'WorktypeReference':
        """
        Gets the worktype of this WorkitemStatus.
        The Worktype containing the Status.

        :return: The worktype of this WorkitemStatus.
        :rtype: WorktypeReference
        """
        return self._worktype

    @worktype.setter
    def worktype(self, worktype: 'WorktypeReference') -> None:
        """
        Sets the worktype of this WorkitemStatus.
        The Worktype containing the Status.

        :param worktype: The worktype of this WorkitemStatus.
        :type: WorktypeReference
        """
        

        self._worktype = worktype

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this WorkitemStatus.
        The URI for this object

        :return: The self_uri of this WorkitemStatus.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this WorkitemStatus.
        The URI for this object

        :param self_uri: The self_uri of this WorkitemStatus.
        :type: str
        """
        

        self._self_uri = self_uri

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
