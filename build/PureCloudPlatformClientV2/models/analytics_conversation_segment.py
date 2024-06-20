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
    from . import AnalyticsProperty
    from . import AnalyticsScoredAgent

class AnalyticsConversationSegment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AnalyticsConversationSegment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'audio_muted': 'bool',
            'conference': 'bool',
            'destination_conversation_id': 'str',
            'destination_session_id': 'str',
            'disconnect_type': 'str',
            'error_code': 'str',
            'group_id': 'str',
            'q850_response_codes': 'list[int]',
            'queue_id': 'str',
            'requested_language_id': 'str',
            'requested_routing_skill_ids': 'list[str]',
            'requested_routing_user_ids': 'list[str]',
            'segment_end': 'datetime',
            'segment_start': 'datetime',
            'segment_type': 'str',
            'sip_response_codes': 'list[int]',
            'source_conversation_id': 'str',
            'source_session_id': 'str',
            'subject': 'str',
            'video_muted': 'bool',
            'wrap_up_code': 'str',
            'wrap_up_note': 'str',
            'wrap_up_tags': 'list[str]',
            'scored_agents': 'list[AnalyticsScoredAgent]',
            'properties': 'list[AnalyticsProperty]'
        }

        self.attribute_map = {
            'audio_muted': 'audioMuted',
            'conference': 'conference',
            'destination_conversation_id': 'destinationConversationId',
            'destination_session_id': 'destinationSessionId',
            'disconnect_type': 'disconnectType',
            'error_code': 'errorCode',
            'group_id': 'groupId',
            'q850_response_codes': 'q850ResponseCodes',
            'queue_id': 'queueId',
            'requested_language_id': 'requestedLanguageId',
            'requested_routing_skill_ids': 'requestedRoutingSkillIds',
            'requested_routing_user_ids': 'requestedRoutingUserIds',
            'segment_end': 'segmentEnd',
            'segment_start': 'segmentStart',
            'segment_type': 'segmentType',
            'sip_response_codes': 'sipResponseCodes',
            'source_conversation_id': 'sourceConversationId',
            'source_session_id': 'sourceSessionId',
            'subject': 'subject',
            'video_muted': 'videoMuted',
            'wrap_up_code': 'wrapUpCode',
            'wrap_up_note': 'wrapUpNote',
            'wrap_up_tags': 'wrapUpTags',
            'scored_agents': 'scoredAgents',
            'properties': 'properties'
        }

        self._audio_muted = None
        self._conference = None
        self._destination_conversation_id = None
        self._destination_session_id = None
        self._disconnect_type = None
        self._error_code = None
        self._group_id = None
        self._q850_response_codes = None
        self._queue_id = None
        self._requested_language_id = None
        self._requested_routing_skill_ids = None
        self._requested_routing_user_ids = None
        self._segment_end = None
        self._segment_start = None
        self._segment_type = None
        self._sip_response_codes = None
        self._source_conversation_id = None
        self._source_session_id = None
        self._subject = None
        self._video_muted = None
        self._wrap_up_code = None
        self._wrap_up_note = None
        self._wrap_up_tags = None
        self._scored_agents = None
        self._properties = None

    @property
    def audio_muted(self) -> bool:
        """
        Gets the audio_muted of this AnalyticsConversationSegment.
        Flag indicating if audio is muted or not (true/false)

        :return: The audio_muted of this AnalyticsConversationSegment.
        :rtype: bool
        """
        return self._audio_muted

    @audio_muted.setter
    def audio_muted(self, audio_muted: bool) -> None:
        """
        Sets the audio_muted of this AnalyticsConversationSegment.
        Flag indicating if audio is muted or not (true/false)

        :param audio_muted: The audio_muted of this AnalyticsConversationSegment.
        :type: bool
        """
        

        self._audio_muted = audio_muted

    @property
    def conference(self) -> bool:
        """
        Gets the conference of this AnalyticsConversationSegment.
        Indicates whether the segment was a conference

        :return: The conference of this AnalyticsConversationSegment.
        :rtype: bool
        """
        return self._conference

    @conference.setter
    def conference(self, conference: bool) -> None:
        """
        Sets the conference of this AnalyticsConversationSegment.
        Indicates whether the segment was a conference

        :param conference: The conference of this AnalyticsConversationSegment.
        :type: bool
        """
        

        self._conference = conference

    @property
    def destination_conversation_id(self) -> str:
        """
        Gets the destination_conversation_id of this AnalyticsConversationSegment.
        The unique identifier of a new conversation when a conversation is ended for a conference

        :return: The destination_conversation_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._destination_conversation_id

    @destination_conversation_id.setter
    def destination_conversation_id(self, destination_conversation_id: str) -> None:
        """
        Sets the destination_conversation_id of this AnalyticsConversationSegment.
        The unique identifier of a new conversation when a conversation is ended for a conference

        :param destination_conversation_id: The destination_conversation_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._destination_conversation_id = destination_conversation_id

    @property
    def destination_session_id(self) -> str:
        """
        Gets the destination_session_id of this AnalyticsConversationSegment.
        The unique identifier of a new session when a session is ended for a conference

        :return: The destination_session_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._destination_session_id

    @destination_session_id.setter
    def destination_session_id(self, destination_session_id: str) -> None:
        """
        Sets the destination_session_id of this AnalyticsConversationSegment.
        The unique identifier of a new session when a session is ended for a conference

        :param destination_session_id: The destination_session_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._destination_session_id = destination_session_id

    @property
    def disconnect_type(self) -> str:
        """
        Gets the disconnect_type of this AnalyticsConversationSegment.
        The session disconnect type

        :return: The disconnect_type of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._disconnect_type

    @disconnect_type.setter
    def disconnect_type(self, disconnect_type: str) -> None:
        """
        Sets the disconnect_type of this AnalyticsConversationSegment.
        The session disconnect type

        :param disconnect_type: The disconnect_type of this AnalyticsConversationSegment.
        :type: str
        """
        if isinstance(disconnect_type, int):
            disconnect_type = str(disconnect_type)
        allowed_values = ["client", "conferenceTransfer", "consultTransfer", "dndEndpoint", "dndTransfer", "endpoint", "error", "forwardTransfer", "noAnswerTransfer", "notAvailableTransfer", "other", "peer", "spam", "system", "timeout", "transfer", "transportFailure", "uncallable"]
        if disconnect_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for disconnect_type -> " + disconnect_type)
            self._disconnect_type = "outdated_sdk_version"
        else:
            self._disconnect_type = disconnect_type

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this AnalyticsConversationSegment.
        A code corresponding to the error that occurred

        :return: The error_code of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this AnalyticsConversationSegment.
        A code corresponding to the error that occurred

        :param error_code: The error_code of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def group_id(self) -> str:
        """
        Gets the group_id of this AnalyticsConversationSegment.
        Unique identifier for a PureCloud group

        :return: The group_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id: str) -> None:
        """
        Sets the group_id of this AnalyticsConversationSegment.
        Unique identifier for a PureCloud group

        :param group_id: The group_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._group_id = group_id

    @property
    def q850_response_codes(self) -> List[int]:
        """
        Gets the q850_response_codes of this AnalyticsConversationSegment.
        Q.850 response code(s)

        :return: The q850_response_codes of this AnalyticsConversationSegment.
        :rtype: list[int]
        """
        return self._q850_response_codes

    @q850_response_codes.setter
    def q850_response_codes(self, q850_response_codes: List[int]) -> None:
        """
        Sets the q850_response_codes of this AnalyticsConversationSegment.
        Q.850 response code(s)

        :param q850_response_codes: The q850_response_codes of this AnalyticsConversationSegment.
        :type: list[int]
        """
        

        self._q850_response_codes = q850_response_codes

    @property
    def queue_id(self) -> str:
        """
        Gets the queue_id of this AnalyticsConversationSegment.
        Queue identifier

        :return: The queue_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: str) -> None:
        """
        Sets the queue_id of this AnalyticsConversationSegment.
        Queue identifier

        :param queue_id: The queue_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._queue_id = queue_id

    @property
    def requested_language_id(self) -> str:
        """
        Gets the requested_language_id of this AnalyticsConversationSegment.
        Unique identifier for the language requested for an interaction

        :return: The requested_language_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._requested_language_id

    @requested_language_id.setter
    def requested_language_id(self, requested_language_id: str) -> None:
        """
        Sets the requested_language_id of this AnalyticsConversationSegment.
        Unique identifier for the language requested for an interaction

        :param requested_language_id: The requested_language_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._requested_language_id = requested_language_id

    @property
    def requested_routing_skill_ids(self) -> List[str]:
        """
        Gets the requested_routing_skill_ids of this AnalyticsConversationSegment.
        Unique identifier(s) for skill(s) requested for an interaction

        :return: The requested_routing_skill_ids of this AnalyticsConversationSegment.
        :rtype: list[str]
        """
        return self._requested_routing_skill_ids

    @requested_routing_skill_ids.setter
    def requested_routing_skill_ids(self, requested_routing_skill_ids: List[str]) -> None:
        """
        Sets the requested_routing_skill_ids of this AnalyticsConversationSegment.
        Unique identifier(s) for skill(s) requested for an interaction

        :param requested_routing_skill_ids: The requested_routing_skill_ids of this AnalyticsConversationSegment.
        :type: list[str]
        """
        

        self._requested_routing_skill_ids = requested_routing_skill_ids

    @property
    def requested_routing_user_ids(self) -> List[str]:
        """
        Gets the requested_routing_user_ids of this AnalyticsConversationSegment.
        Unique identifier(s) for agent(s) requested for an interaction

        :return: The requested_routing_user_ids of this AnalyticsConversationSegment.
        :rtype: list[str]
        """
        return self._requested_routing_user_ids

    @requested_routing_user_ids.setter
    def requested_routing_user_ids(self, requested_routing_user_ids: List[str]) -> None:
        """
        Sets the requested_routing_user_ids of this AnalyticsConversationSegment.
        Unique identifier(s) for agent(s) requested for an interaction

        :param requested_routing_user_ids: The requested_routing_user_ids of this AnalyticsConversationSegment.
        :type: list[str]
        """
        

        self._requested_routing_user_ids = requested_routing_user_ids

    @property
    def segment_end(self) -> datetime:
        """
        Gets the segment_end of this AnalyticsConversationSegment.
        The end time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The segment_end of this AnalyticsConversationSegment.
        :rtype: datetime
        """
        return self._segment_end

    @segment_end.setter
    def segment_end(self, segment_end: datetime) -> None:
        """
        Sets the segment_end of this AnalyticsConversationSegment.
        The end time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param segment_end: The segment_end of this AnalyticsConversationSegment.
        :type: datetime
        """
        

        self._segment_end = segment_end

    @property
    def segment_start(self) -> datetime:
        """
        Gets the segment_start of this AnalyticsConversationSegment.
        The start time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The segment_start of this AnalyticsConversationSegment.
        :rtype: datetime
        """
        return self._segment_start

    @segment_start.setter
    def segment_start(self, segment_start: datetime) -> None:
        """
        Sets the segment_start of this AnalyticsConversationSegment.
        The start time of a segment. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param segment_start: The segment_start of this AnalyticsConversationSegment.
        :type: datetime
        """
        

        self._segment_start = segment_start

    @property
    def segment_type(self) -> str:
        """
        Gets the segment_type of this AnalyticsConversationSegment.
        The activity that takes place in the segment, such as hold or interact

        :return: The segment_type of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._segment_type

    @segment_type.setter
    def segment_type(self, segment_type: str) -> None:
        """
        Sets the segment_type of this AnalyticsConversationSegment.
        The activity that takes place in the segment, such as hold or interact

        :param segment_type: The segment_type of this AnalyticsConversationSegment.
        :type: str
        """
        if isinstance(segment_type, int):
            segment_type = str(segment_type)
        allowed_values = ["alert", "barging", "callback", "coaching", "contacting", "converting", "delay", "dialing", "hold", "interact", "ivr", "monitoring", "parked", "scheduled", "sharing", "system", "transmitting", "unknown", "uploading", "voicemail", "wrapup"]
        if segment_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for segment_type -> " + segment_type)
            self._segment_type = "outdated_sdk_version"
        else:
            self._segment_type = segment_type

    @property
    def sip_response_codes(self) -> List[int]:
        """
        Gets the sip_response_codes of this AnalyticsConversationSegment.
        SIP response code(s)

        :return: The sip_response_codes of this AnalyticsConversationSegment.
        :rtype: list[int]
        """
        return self._sip_response_codes

    @sip_response_codes.setter
    def sip_response_codes(self, sip_response_codes: List[int]) -> None:
        """
        Sets the sip_response_codes of this AnalyticsConversationSegment.
        SIP response code(s)

        :param sip_response_codes: The sip_response_codes of this AnalyticsConversationSegment.
        :type: list[int]
        """
        

        self._sip_response_codes = sip_response_codes

    @property
    def source_conversation_id(self) -> str:
        """
        Gets the source_conversation_id of this AnalyticsConversationSegment.
        The unique identifier of the previous conversation when a new conversation is created for a conference

        :return: The source_conversation_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._source_conversation_id

    @source_conversation_id.setter
    def source_conversation_id(self, source_conversation_id: str) -> None:
        """
        Sets the source_conversation_id of this AnalyticsConversationSegment.
        The unique identifier of the previous conversation when a new conversation is created for a conference

        :param source_conversation_id: The source_conversation_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._source_conversation_id = source_conversation_id

    @property
    def source_session_id(self) -> str:
        """
        Gets the source_session_id of this AnalyticsConversationSegment.
        The unique identifier of the previous session when a new session is created for a conference

        :return: The source_session_id of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._source_session_id

    @source_session_id.setter
    def source_session_id(self, source_session_id: str) -> None:
        """
        Sets the source_session_id of this AnalyticsConversationSegment.
        The unique identifier of the previous session when a new session is created for a conference

        :param source_session_id: The source_session_id of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._source_session_id = source_session_id

    @property
    def subject(self) -> str:
        """
        Gets the subject of this AnalyticsConversationSegment.
        The subject for the initial email that started this conversation

        :return: The subject of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str) -> None:
        """
        Sets the subject of this AnalyticsConversationSegment.
        The subject for the initial email that started this conversation

        :param subject: The subject of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._subject = subject

    @property
    def video_muted(self) -> bool:
        """
        Gets the video_muted of this AnalyticsConversationSegment.
        Flag indicating if video is muted/paused or not (true/false)

        :return: The video_muted of this AnalyticsConversationSegment.
        :rtype: bool
        """
        return self._video_muted

    @video_muted.setter
    def video_muted(self, video_muted: bool) -> None:
        """
        Sets the video_muted of this AnalyticsConversationSegment.
        Flag indicating if video is muted/paused or not (true/false)

        :param video_muted: The video_muted of this AnalyticsConversationSegment.
        :type: bool
        """
        

        self._video_muted = video_muted

    @property
    def wrap_up_code(self) -> str:
        """
        Gets the wrap_up_code of this AnalyticsConversationSegment.
        Wrap up code

        :return: The wrap_up_code of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._wrap_up_code

    @wrap_up_code.setter
    def wrap_up_code(self, wrap_up_code: str) -> None:
        """
        Sets the wrap_up_code of this AnalyticsConversationSegment.
        Wrap up code

        :param wrap_up_code: The wrap_up_code of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._wrap_up_code = wrap_up_code

    @property
    def wrap_up_note(self) -> str:
        """
        Gets the wrap_up_note of this AnalyticsConversationSegment.
        Note entered by an agent during after-call work

        :return: The wrap_up_note of this AnalyticsConversationSegment.
        :rtype: str
        """
        return self._wrap_up_note

    @wrap_up_note.setter
    def wrap_up_note(self, wrap_up_note: str) -> None:
        """
        Sets the wrap_up_note of this AnalyticsConversationSegment.
        Note entered by an agent during after-call work

        :param wrap_up_note: The wrap_up_note of this AnalyticsConversationSegment.
        :type: str
        """
        

        self._wrap_up_note = wrap_up_note

    @property
    def wrap_up_tags(self) -> List[str]:
        """
        Gets the wrap_up_tags of this AnalyticsConversationSegment.
        Tag(s) assigned during after-call work

        :return: The wrap_up_tags of this AnalyticsConversationSegment.
        :rtype: list[str]
        """
        return self._wrap_up_tags

    @wrap_up_tags.setter
    def wrap_up_tags(self, wrap_up_tags: List[str]) -> None:
        """
        Sets the wrap_up_tags of this AnalyticsConversationSegment.
        Tag(s) assigned during after-call work

        :param wrap_up_tags: The wrap_up_tags of this AnalyticsConversationSegment.
        :type: list[str]
        """
        

        self._wrap_up_tags = wrap_up_tags

    @property
    def scored_agents(self) -> List['AnalyticsScoredAgent']:
        """
        Gets the scored_agents of this AnalyticsConversationSegment.
        Scored agents

        :return: The scored_agents of this AnalyticsConversationSegment.
        :rtype: list[AnalyticsScoredAgent]
        """
        return self._scored_agents

    @scored_agents.setter
    def scored_agents(self, scored_agents: List['AnalyticsScoredAgent']) -> None:
        """
        Sets the scored_agents of this AnalyticsConversationSegment.
        Scored agents

        :param scored_agents: The scored_agents of this AnalyticsConversationSegment.
        :type: list[AnalyticsScoredAgent]
        """
        

        self._scored_agents = scored_agents

    @property
    def properties(self) -> List['AnalyticsProperty']:
        """
        Gets the properties of this AnalyticsConversationSegment.
        Additional segment properties

        :return: The properties of this AnalyticsConversationSegment.
        :rtype: list[AnalyticsProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: List['AnalyticsProperty']) -> None:
        """
        Sets the properties of this AnalyticsConversationSegment.
        Additional segment properties

        :param properties: The properties of this AnalyticsConversationSegment.
        :type: list[AnalyticsProperty]
        """
        

        self._properties = properties

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

