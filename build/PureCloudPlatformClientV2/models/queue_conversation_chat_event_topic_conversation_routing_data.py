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
    from . import QueueConversationChatEventTopicScoredAgent
    from . import QueueConversationChatEventTopicUriReference

class QueueConversationChatEventTopicConversationRoutingData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        QueueConversationChatEventTopicConversationRoutingData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'queue': 'QueueConversationChatEventTopicUriReference',
            'language': 'QueueConversationChatEventTopicUriReference',
            'priority': 'int',
            'skills': 'list[QueueConversationChatEventTopicUriReference]',
            'scored_agents': 'list[QueueConversationChatEventTopicScoredAgent]'
        }

        self.attribute_map = {
            'queue': 'queue',
            'language': 'language',
            'priority': 'priority',
            'skills': 'skills',
            'scored_agents': 'scoredAgents'
        }

        self._queue = None
        self._language = None
        self._priority = None
        self._skills = None
        self._scored_agents = None

    @property
    def queue(self) -> 'QueueConversationChatEventTopicUriReference':
        """
        Gets the queue of this QueueConversationChatEventTopicConversationRoutingData.
        A UriReference for a resource

        :return: The queue of this QueueConversationChatEventTopicConversationRoutingData.
        :rtype: QueueConversationChatEventTopicUriReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'QueueConversationChatEventTopicUriReference') -> None:
        """
        Sets the queue of this QueueConversationChatEventTopicConversationRoutingData.
        A UriReference for a resource

        :param queue: The queue of this QueueConversationChatEventTopicConversationRoutingData.
        :type: QueueConversationChatEventTopicUriReference
        """
        

        self._queue = queue

    @property
    def language(self) -> 'QueueConversationChatEventTopicUriReference':
        """
        Gets the language of this QueueConversationChatEventTopicConversationRoutingData.
        A UriReference for a resource

        :return: The language of this QueueConversationChatEventTopicConversationRoutingData.
        :rtype: QueueConversationChatEventTopicUriReference
        """
        return self._language

    @language.setter
    def language(self, language: 'QueueConversationChatEventTopicUriReference') -> None:
        """
        Sets the language of this QueueConversationChatEventTopicConversationRoutingData.
        A UriReference for a resource

        :param language: The language of this QueueConversationChatEventTopicConversationRoutingData.
        :type: QueueConversationChatEventTopicUriReference
        """
        

        self._language = language

    @property
    def priority(self) -> int:
        """
        Gets the priority of this QueueConversationChatEventTopicConversationRoutingData.
        The priority of the conversation to use for routing decisions

        :return: The priority of this QueueConversationChatEventTopicConversationRoutingData.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority: int) -> None:
        """
        Sets the priority of this QueueConversationChatEventTopicConversationRoutingData.
        The priority of the conversation to use for routing decisions

        :param priority: The priority of this QueueConversationChatEventTopicConversationRoutingData.
        :type: int
        """
        

        self._priority = priority

    @property
    def skills(self) -> List['QueueConversationChatEventTopicUriReference']:
        """
        Gets the skills of this QueueConversationChatEventTopicConversationRoutingData.
        The skills to use for routing decisions

        :return: The skills of this QueueConversationChatEventTopicConversationRoutingData.
        :rtype: list[QueueConversationChatEventTopicUriReference]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List['QueueConversationChatEventTopicUriReference']) -> None:
        """
        Sets the skills of this QueueConversationChatEventTopicConversationRoutingData.
        The skills to use for routing decisions

        :param skills: The skills of this QueueConversationChatEventTopicConversationRoutingData.
        :type: list[QueueConversationChatEventTopicUriReference]
        """
        

        self._skills = skills

    @property
    def scored_agents(self) -> List['QueueConversationChatEventTopicScoredAgent']:
        """
        Gets the scored_agents of this QueueConversationChatEventTopicConversationRoutingData.
        A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents

        :return: The scored_agents of this QueueConversationChatEventTopicConversationRoutingData.
        :rtype: list[QueueConversationChatEventTopicScoredAgent]
        """
        return self._scored_agents

    @scored_agents.setter
    def scored_agents(self, scored_agents: List['QueueConversationChatEventTopicScoredAgent']) -> None:
        """
        Sets the scored_agents of this QueueConversationChatEventTopicConversationRoutingData.
        A collection of agents and their assigned scores for this conversation (0 - 100, higher being better), for use in routing to preferred agents

        :param scored_agents: The scored_agents of this QueueConversationChatEventTopicConversationRoutingData.
        :type: list[QueueConversationChatEventTopicScoredAgent]
        """
        

        self._scored_agents = scored_agents

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

