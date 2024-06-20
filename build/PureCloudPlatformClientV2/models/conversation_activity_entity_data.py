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
    from . import ConversationActivityScoredAgent

class ConversationActivityEntityData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ConversationActivityEntityData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_date': 'datetime',
            'metric': 'str',
            'active_routing': 'str',
            'address_from': 'str',
            'address_to': 'str',
            'ani': 'str',
            'conversation_id': 'str',
            'converted_from': 'str',
            'converted_to': 'str',
            'direction': 'str',
            'dnis': 'str',
            'media_type': 'str',
            'participant_name': 'str',
            'queue_id': 'str',
            'requested_language_id': 'str',
            'requested_routing_skill_ids': 'list[str]',
            'requested_routings': 'list[str]',
            'routing_priority': 'int',
            'session_id': 'str',
            'team_id': 'str',
            'used_routing': 'str',
            'user_id': 'str',
            'scored_agents': 'list[ConversationActivityScoredAgent]'
        }

        self.attribute_map = {
            'activity_date': 'activityDate',
            'metric': 'metric',
            'active_routing': 'activeRouting',
            'address_from': 'addressFrom',
            'address_to': 'addressTo',
            'ani': 'ani',
            'conversation_id': 'conversationId',
            'converted_from': 'convertedFrom',
            'converted_to': 'convertedTo',
            'direction': 'direction',
            'dnis': 'dnis',
            'media_type': 'mediaType',
            'participant_name': 'participantName',
            'queue_id': 'queueId',
            'requested_language_id': 'requestedLanguageId',
            'requested_routing_skill_ids': 'requestedRoutingSkillIds',
            'requested_routings': 'requestedRoutings',
            'routing_priority': 'routingPriority',
            'session_id': 'sessionId',
            'team_id': 'teamId',
            'used_routing': 'usedRouting',
            'user_id': 'userId',
            'scored_agents': 'scoredAgents'
        }

        self._activity_date = None
        self._metric = None
        self._active_routing = None
        self._address_from = None
        self._address_to = None
        self._ani = None
        self._conversation_id = None
        self._converted_from = None
        self._converted_to = None
        self._direction = None
        self._dnis = None
        self._media_type = None
        self._participant_name = None
        self._queue_id = None
        self._requested_language_id = None
        self._requested_routing_skill_ids = None
        self._requested_routings = None
        self._routing_priority = None
        self._session_id = None
        self._team_id = None
        self._used_routing = None
        self._user_id = None
        self._scored_agents = None

    @property
    def activity_date(self) -> datetime:
        """
        Gets the activity_date of this ConversationActivityEntityData.
        The time at which the activity was observed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The activity_date of this ConversationActivityEntityData.
        :rtype: datetime
        """
        return self._activity_date

    @activity_date.setter
    def activity_date(self, activity_date: datetime) -> None:
        """
        Sets the activity_date of this ConversationActivityEntityData.
        The time at which the activity was observed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param activity_date: The activity_date of this ConversationActivityEntityData.
        :type: datetime
        """
        

        self._activity_date = activity_date

    @property
    def metric(self) -> str:
        """
        Gets the metric of this ConversationActivityEntityData.
        Activity metric

        :return: The metric of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric: str) -> None:
        """
        Sets the metric of this ConversationActivityEntityData.
        Activity metric

        :param metric: The metric of this ConversationActivityEntityData.
        :type: str
        """
        if isinstance(metric, int):
            metric = str(metric)
        allowed_values = ["oAlerting", "oInteracting", "oWaiting"]
        if metric.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for metric -> " + metric)
            self._metric = "outdated_sdk_version"
        else:
            self._metric = metric

    @property
    def active_routing(self) -> str:
        """
        Gets the active_routing of this ConversationActivityEntityData.
        Active routing method

        :return: The active_routing of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._active_routing

    @active_routing.setter
    def active_routing(self, active_routing: str) -> None:
        """
        Sets the active_routing of this ConversationActivityEntityData.
        Active routing method

        :param active_routing: The active_routing of this ConversationActivityEntityData.
        :type: str
        """
        if isinstance(active_routing, int):
            active_routing = str(active_routing)
        allowed_values = ["Bullseye", "Conditional", "Direct", "Last", "Manual", "Predictive", "Preferred", "Standard", "Vip"]
        if active_routing.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for active_routing -> " + active_routing)
            self._active_routing = "outdated_sdk_version"
        else:
            self._active_routing = active_routing

    @property
    def address_from(self) -> str:
        """
        Gets the address_from of this ConversationActivityEntityData.
        The address that initiated an action

        :return: The address_from of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._address_from

    @address_from.setter
    def address_from(self, address_from: str) -> None:
        """
        Sets the address_from of this ConversationActivityEntityData.
        The address that initiated an action

        :param address_from: The address_from of this ConversationActivityEntityData.
        :type: str
        """
        

        self._address_from = address_from

    @property
    def address_to(self) -> str:
        """
        Gets the address_to of this ConversationActivityEntityData.
        The address receiving an action

        :return: The address_to of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._address_to

    @address_to.setter
    def address_to(self, address_to: str) -> None:
        """
        Sets the address_to of this ConversationActivityEntityData.
        The address receiving an action

        :param address_to: The address_to of this ConversationActivityEntityData.
        :type: str
        """
        

        self._address_to = address_to

    @property
    def ani(self) -> str:
        """
        Gets the ani of this ConversationActivityEntityData.
        Automatic Number Identification (caller's number)

        :return: The ani of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._ani

    @ani.setter
    def ani(self, ani: str) -> None:
        """
        Sets the ani of this ConversationActivityEntityData.
        Automatic Number Identification (caller's number)

        :param ani: The ani of this ConversationActivityEntityData.
        :type: str
        """
        

        self._ani = ani

    @property
    def conversation_id(self) -> str:
        """
        Gets the conversation_id of this ConversationActivityEntityData.
        Unique identifier for the conversation

        :return: The conversation_id of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, conversation_id: str) -> None:
        """
        Sets the conversation_id of this ConversationActivityEntityData.
        Unique identifier for the conversation

        :param conversation_id: The conversation_id of this ConversationActivityEntityData.
        :type: str
        """
        

        self._conversation_id = conversation_id

    @property
    def converted_from(self) -> str:
        """
        Gets the converted_from of this ConversationActivityEntityData.
        Session media type that was converted from in case of a media type conversion

        :return: The converted_from of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._converted_from

    @converted_from.setter
    def converted_from(self, converted_from: str) -> None:
        """
        Sets the converted_from of this ConversationActivityEntityData.
        Session media type that was converted from in case of a media type conversion

        :param converted_from: The converted_from of this ConversationActivityEntityData.
        :type: str
        """
        

        self._converted_from = converted_from

    @property
    def converted_to(self) -> str:
        """
        Gets the converted_to of this ConversationActivityEntityData.
        Session media type that was converted to in case of a media type conversion

        :return: The converted_to of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._converted_to

    @converted_to.setter
    def converted_to(self, converted_to: str) -> None:
        """
        Sets the converted_to of this ConversationActivityEntityData.
        Session media type that was converted to in case of a media type conversion

        :param converted_to: The converted_to of this ConversationActivityEntityData.
        :type: str
        """
        

        self._converted_to = converted_to

    @property
    def direction(self) -> str:
        """
        Gets the direction of this ConversationActivityEntityData.
        The direction of the communication

        :return: The direction of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str) -> None:
        """
        Sets the direction of this ConversationActivityEntityData.
        The direction of the communication

        :param direction: The direction of this ConversationActivityEntityData.
        :type: str
        """
        if isinstance(direction, int):
            direction = str(direction)
        allowed_values = ["inbound", "outbound"]
        if direction.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for direction -> " + direction)
            self._direction = "outdated_sdk_version"
        else:
            self._direction = direction

    @property
    def dnis(self) -> str:
        """
        Gets the dnis of this ConversationActivityEntityData.
        Dialed number identification service (number dialed by the calling party)

        :return: The dnis of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._dnis

    @dnis.setter
    def dnis(self, dnis: str) -> None:
        """
        Sets the dnis of this ConversationActivityEntityData.
        Dialed number identification service (number dialed by the calling party)

        :param dnis: The dnis of this ConversationActivityEntityData.
        :type: str
        """
        

        self._dnis = dnis

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this ConversationActivityEntityData.
        The session media type

        :return: The media_type of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this ConversationActivityEntityData.
        The session media type

        :param media_type: The media_type of this ConversationActivityEntityData.
        :type: str
        """
        if isinstance(media_type, int):
            media_type = str(media_type)
        allowed_values = ["callback", "chat", "cobrowse", "email", "message", "screenshare", "unknown", "video", "voice"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def participant_name(self) -> str:
        """
        Gets the participant_name of this ConversationActivityEntityData.
        A human readable name identifying the participant

        :return: The participant_name of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._participant_name

    @participant_name.setter
    def participant_name(self, participant_name: str) -> None:
        """
        Sets the participant_name of this ConversationActivityEntityData.
        A human readable name identifying the participant

        :param participant_name: The participant_name of this ConversationActivityEntityData.
        :type: str
        """
        

        self._participant_name = participant_name

    @property
    def queue_id(self) -> str:
        """
        Gets the queue_id of this ConversationActivityEntityData.
        Queue identifier

        :return: The queue_id of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: str) -> None:
        """
        Sets the queue_id of this ConversationActivityEntityData.
        Queue identifier

        :param queue_id: The queue_id of this ConversationActivityEntityData.
        :type: str
        """
        

        self._queue_id = queue_id

    @property
    def requested_language_id(self) -> str:
        """
        Gets the requested_language_id of this ConversationActivityEntityData.
        Unique identifier for the language requested for an interaction

        :return: The requested_language_id of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._requested_language_id

    @requested_language_id.setter
    def requested_language_id(self, requested_language_id: str) -> None:
        """
        Sets the requested_language_id of this ConversationActivityEntityData.
        Unique identifier for the language requested for an interaction

        :param requested_language_id: The requested_language_id of this ConversationActivityEntityData.
        :type: str
        """
        

        self._requested_language_id = requested_language_id

    @property
    def requested_routing_skill_ids(self) -> List[str]:
        """
        Gets the requested_routing_skill_ids of this ConversationActivityEntityData.
        Unique identifier(s) for skill(s) requested for an interaction

        :return: The requested_routing_skill_ids of this ConversationActivityEntityData.
        :rtype: list[str]
        """
        return self._requested_routing_skill_ids

    @requested_routing_skill_ids.setter
    def requested_routing_skill_ids(self, requested_routing_skill_ids: List[str]) -> None:
        """
        Sets the requested_routing_skill_ids of this ConversationActivityEntityData.
        Unique identifier(s) for skill(s) requested for an interaction

        :param requested_routing_skill_ids: The requested_routing_skill_ids of this ConversationActivityEntityData.
        :type: list[str]
        """
        

        self._requested_routing_skill_ids = requested_routing_skill_ids

    @property
    def requested_routings(self) -> List[str]:
        """
        Gets the requested_routings of this ConversationActivityEntityData.
        Routing type(s) for requested/attempted routing methods.

        :return: The requested_routings of this ConversationActivityEntityData.
        :rtype: list[str]
        """
        return self._requested_routings

    @requested_routings.setter
    def requested_routings(self, requested_routings: List[str]) -> None:
        """
        Sets the requested_routings of this ConversationActivityEntityData.
        Routing type(s) for requested/attempted routing methods.

        :param requested_routings: The requested_routings of this ConversationActivityEntityData.
        :type: list[str]
        """
        

        self._requested_routings = requested_routings

    @property
    def routing_priority(self) -> int:
        """
        Gets the routing_priority of this ConversationActivityEntityData.
        Routing priority for the current interaction

        :return: The routing_priority of this ConversationActivityEntityData.
        :rtype: int
        """
        return self._routing_priority

    @routing_priority.setter
    def routing_priority(self, routing_priority: int) -> None:
        """
        Sets the routing_priority of this ConversationActivityEntityData.
        Routing priority for the current interaction

        :param routing_priority: The routing_priority of this ConversationActivityEntityData.
        :type: int
        """
        

        self._routing_priority = routing_priority

    @property
    def session_id(self) -> str:
        """
        Gets the session_id of this ConversationActivityEntityData.
        The unique identifier of this session

        :return: The session_id of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str) -> None:
        """
        Sets the session_id of this ConversationActivityEntityData.
        The unique identifier of this session

        :param session_id: The session_id of this ConversationActivityEntityData.
        :type: str
        """
        

        self._session_id = session_id

    @property
    def team_id(self) -> str:
        """
        Gets the team_id of this ConversationActivityEntityData.
        The team ID the user is a member of

        :return: The team_id of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id: str) -> None:
        """
        Sets the team_id of this ConversationActivityEntityData.
        The team ID the user is a member of

        :param team_id: The team_id of this ConversationActivityEntityData.
        :type: str
        """
        

        self._team_id = team_id

    @property
    def used_routing(self) -> str:
        """
        Gets the used_routing of this ConversationActivityEntityData.
        Complete routing method

        :return: The used_routing of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._used_routing

    @used_routing.setter
    def used_routing(self, used_routing: str) -> None:
        """
        Sets the used_routing of this ConversationActivityEntityData.
        Complete routing method

        :param used_routing: The used_routing of this ConversationActivityEntityData.
        :type: str
        """
        if isinstance(used_routing, int):
            used_routing = str(used_routing)
        allowed_values = ["Bullseye", "Conditional", "Direct", "Last", "Manual", "Predictive", "Preferred", "Standard", "Vip"]
        if used_routing.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for used_routing -> " + used_routing)
            self._used_routing = "outdated_sdk_version"
        else:
            self._used_routing = used_routing

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this ConversationActivityEntityData.
        Unique identifier for the user

        :return: The user_id of this ConversationActivityEntityData.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this ConversationActivityEntityData.
        Unique identifier for the user

        :param user_id: The user_id of this ConversationActivityEntityData.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def scored_agents(self) -> List['ConversationActivityScoredAgent']:
        """
        Gets the scored_agents of this ConversationActivityEntityData.
        Scored agents

        :return: The scored_agents of this ConversationActivityEntityData.
        :rtype: list[ConversationActivityScoredAgent]
        """
        return self._scored_agents

    @scored_agents.setter
    def scored_agents(self, scored_agents: List['ConversationActivityScoredAgent']) -> None:
        """
        Sets the scored_agents of this ConversationActivityEntityData.
        Scored agents

        :param scored_agents: The scored_agents of this ConversationActivityEntityData.
        :type: list[ConversationActivityScoredAgent]
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

