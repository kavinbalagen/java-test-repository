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
    from . import ObjectiveZone

class CreateObjective(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CreateObjective - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'template_id': 'str',
            'zones': 'list[ObjectiveZone]',
            'enabled': 'bool',
            'topic_ids': 'list[str]',
            'media_types': 'list[str]',
            'queue_ids': 'list[str]',
            'topic_ids_filter_type': 'str',
            'evaluation_form_context_ids': 'list[str]',
            'initial_direction': 'str',
            'date_start': 'date'
        }

        self.attribute_map = {
            'id': 'id',
            'template_id': 'templateId',
            'zones': 'zones',
            'enabled': 'enabled',
            'topic_ids': 'topicIds',
            'media_types': 'mediaTypes',
            'queue_ids': 'queueIds',
            'topic_ids_filter_type': 'topicIdsFilterType',
            'evaluation_form_context_ids': 'evaluationFormContextIds',
            'initial_direction': 'initialDirection',
            'date_start': 'dateStart'
        }

        self._id = None
        self._template_id = None
        self._zones = None
        self._enabled = None
        self._topic_ids = None
        self._media_types = None
        self._queue_ids = None
        self._topic_ids_filter_type = None
        self._evaluation_form_context_ids = None
        self._initial_direction = None
        self._date_start = None

    @property
    def id(self) -> str:
        """
        Gets the id of this CreateObjective.
        The globally unique identifier for the object.

        :return: The id of this CreateObjective.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this CreateObjective.
        The globally unique identifier for the object.

        :param id: The id of this CreateObjective.
        :type: str
        """
        

        self._id = id

    @property
    def template_id(self) -> str:
        """
        Gets the template_id of this CreateObjective.
        The id of this objective's base template

        :return: The template_id of this CreateObjective.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id: str) -> None:
        """
        Sets the template_id of this CreateObjective.
        The id of this objective's base template

        :param template_id: The template_id of this CreateObjective.
        :type: str
        """
        

        self._template_id = template_id

    @property
    def zones(self) -> List['ObjectiveZone']:
        """
        Gets the zones of this CreateObjective.
        Objective zone specifies min,max points and values for the associated metric

        :return: The zones of this CreateObjective.
        :rtype: list[ObjectiveZone]
        """
        return self._zones

    @zones.setter
    def zones(self, zones: List['ObjectiveZone']) -> None:
        """
        Sets the zones of this CreateObjective.
        Objective zone specifies min,max points and values for the associated metric

        :param zones: The zones of this CreateObjective.
        :type: list[ObjectiveZone]
        """
        

        self._zones = zones

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this CreateObjective.
        A flag for whether this objective is enabled for the related metric

        :return: The enabled of this CreateObjective.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this CreateObjective.
        A flag for whether this objective is enabled for the related metric

        :param enabled: The enabled of this CreateObjective.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def topic_ids(self) -> List[str]:
        """
        Gets the topic_ids of this CreateObjective.
        A list of topic ids for detected topic metrics

        :return: The topic_ids of this CreateObjective.
        :rtype: list[str]
        """
        return self._topic_ids

    @topic_ids.setter
    def topic_ids(self, topic_ids: List[str]) -> None:
        """
        Sets the topic_ids of this CreateObjective.
        A list of topic ids for detected topic metrics

        :param topic_ids: The topic_ids of this CreateObjective.
        :type: list[str]
        """
        

        self._topic_ids = topic_ids

    @property
    def media_types(self) -> List[str]:
        """
        Gets the media_types of this CreateObjective.
        A list of media types for the metric

        :return: The media_types of this CreateObjective.
        :rtype: list[str]
        """
        return self._media_types

    @media_types.setter
    def media_types(self, media_types: List[str]) -> None:
        """
        Sets the media_types of this CreateObjective.
        A list of media types for the metric

        :param media_types: The media_types of this CreateObjective.
        :type: list[str]
        """
        

        self._media_types = media_types

    @property
    def queue_ids(self) -> List[str]:
        """
        Gets the queue_ids of this CreateObjective.
        A list of queue ids for the metric

        :return: The queue_ids of this CreateObjective.
        :rtype: list[str]
        """
        return self._queue_ids

    @queue_ids.setter
    def queue_ids(self, queue_ids: List[str]) -> None:
        """
        Sets the queue_ids of this CreateObjective.
        A list of queue ids for the metric

        :param queue_ids: The queue_ids of this CreateObjective.
        :type: list[str]
        """
        

        self._queue_ids = queue_ids

    @property
    def topic_ids_filter_type(self) -> str:
        """
        Gets the topic_ids_filter_type of this CreateObjective.
        A filter type for topic Ids. It's only used for objectives with topicIds. Default filter behavior is \"or\".

        :return: The topic_ids_filter_type of this CreateObjective.
        :rtype: str
        """
        return self._topic_ids_filter_type

    @topic_ids_filter_type.setter
    def topic_ids_filter_type(self, topic_ids_filter_type: str) -> None:
        """
        Sets the topic_ids_filter_type of this CreateObjective.
        A filter type for topic Ids. It's only used for objectives with topicIds. Default filter behavior is \"or\".

        :param topic_ids_filter_type: The topic_ids_filter_type of this CreateObjective.
        :type: str
        """
        if isinstance(topic_ids_filter_type, int):
            topic_ids_filter_type = str(topic_ids_filter_type)
        allowed_values = ["and", "or"]
        if topic_ids_filter_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for topic_ids_filter_type -> " + topic_ids_filter_type)
            self._topic_ids_filter_type = "outdated_sdk_version"
        else:
            self._topic_ids_filter_type = topic_ids_filter_type

    @property
    def evaluation_form_context_ids(self) -> List[str]:
        """
        Gets the evaluation_form_context_ids of this CreateObjective.
        The ids of associated evaluation form context, for Quality Evaluation Score metrics

        :return: The evaluation_form_context_ids of this CreateObjective.
        :rtype: list[str]
        """
        return self._evaluation_form_context_ids

    @evaluation_form_context_ids.setter
    def evaluation_form_context_ids(self, evaluation_form_context_ids: List[str]) -> None:
        """
        Sets the evaluation_form_context_ids of this CreateObjective.
        The ids of associated evaluation form context, for Quality Evaluation Score metrics

        :param evaluation_form_context_ids: The evaluation_form_context_ids of this CreateObjective.
        :type: list[str]
        """
        

        self._evaluation_form_context_ids = evaluation_form_context_ids

    @property
    def initial_direction(self) -> str:
        """
        Gets the initial_direction of this CreateObjective.
        The initial direction to filter on

        :return: The initial_direction of this CreateObjective.
        :rtype: str
        """
        return self._initial_direction

    @initial_direction.setter
    def initial_direction(self, initial_direction: str) -> None:
        """
        Sets the initial_direction of this CreateObjective.
        The initial direction to filter on

        :param initial_direction: The initial_direction of this CreateObjective.
        :type: str
        """
        if isinstance(initial_direction, int):
            initial_direction = str(initial_direction)
        allowed_values = ["inbound", "outbound"]
        if initial_direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for initial_direction -> " + initial_direction)
            self._initial_direction = "outdated_sdk_version"
        else:
            self._initial_direction = initial_direction

    @property
    def date_start(self) -> date:
        """
        Gets the date_start of this CreateObjective.
        start date of the objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The date_start of this CreateObjective.
        :rtype: date
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start: date) -> None:
        """
        Sets the date_start of this CreateObjective.
        start date of the objective. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param date_start: The date_start of this CreateObjective.
        :type: date
        """
        

        self._date_start = date_start

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

