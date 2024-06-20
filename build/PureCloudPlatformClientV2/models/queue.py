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
    from . import AcwSettings
    from . import AgentOwnedRouting
    from . import Bullseye
    from . import ConditionalGroupRouting
    from . import DirectRouting
    from . import Division
    from . import DomainEntityRef
    from . import MemberGroup
    from . import QueueEmailAddress
    from . import QueueMediaSettings
    from . import QueueMessagingAddresses
    from . import RoutingRule
    from . import Script

class Queue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Queue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'Division',
            'description': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'modified_by': 'str',
            'created_by': 'str',
            'member_count': 'int',
            'user_member_count': 'int',
            'joined_member_count': 'int',
            'media_settings': 'QueueMediaSettings',
            'routing_rules': 'list[RoutingRule]',
            'conditional_group_routing': 'ConditionalGroupRouting',
            'bullseye': 'Bullseye',
            'scoring_method': 'str',
            'acw_settings': 'AcwSettings',
            'skill_evaluation_method': 'str',
            'member_groups': 'list[MemberGroup]',
            'queue_flow': 'DomainEntityRef',
            'email_in_queue_flow': 'DomainEntityRef',
            'message_in_queue_flow': 'DomainEntityRef',
            'whisper_prompt': 'DomainEntityRef',
            'on_hold_prompt': 'DomainEntityRef',
            'auto_answer_only': 'bool',
            'enable_transcription': 'bool',
            'enable_audio_monitoring': 'bool',
            'enable_manual_assignment': 'bool',
            'agent_owned_routing': 'AgentOwnedRouting',
            'direct_routing': 'DirectRouting',
            'calling_party_name': 'str',
            'calling_party_number': 'str',
            'default_scripts': 'dict(str, Script)',
            'outbound_messaging_addresses': 'QueueMessagingAddresses',
            'outbound_email_address': 'QueueEmailAddress',
            'peer_id': 'str',
            'suppress_in_queue_call_recording': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'description': 'description',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'created_by': 'createdBy',
            'member_count': 'memberCount',
            'user_member_count': 'userMemberCount',
            'joined_member_count': 'joinedMemberCount',
            'media_settings': 'mediaSettings',
            'routing_rules': 'routingRules',
            'conditional_group_routing': 'conditionalGroupRouting',
            'bullseye': 'bullseye',
            'scoring_method': 'scoringMethod',
            'acw_settings': 'acwSettings',
            'skill_evaluation_method': 'skillEvaluationMethod',
            'member_groups': 'memberGroups',
            'queue_flow': 'queueFlow',
            'email_in_queue_flow': 'emailInQueueFlow',
            'message_in_queue_flow': 'messageInQueueFlow',
            'whisper_prompt': 'whisperPrompt',
            'on_hold_prompt': 'onHoldPrompt',
            'auto_answer_only': 'autoAnswerOnly',
            'enable_transcription': 'enableTranscription',
            'enable_audio_monitoring': 'enableAudioMonitoring',
            'enable_manual_assignment': 'enableManualAssignment',
            'agent_owned_routing': 'agentOwnedRouting',
            'direct_routing': 'directRouting',
            'calling_party_name': 'callingPartyName',
            'calling_party_number': 'callingPartyNumber',
            'default_scripts': 'defaultScripts',
            'outbound_messaging_addresses': 'outboundMessagingAddresses',
            'outbound_email_address': 'outboundEmailAddress',
            'peer_id': 'peerId',
            'suppress_in_queue_call_recording': 'suppressInQueueCallRecording',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._description = None
        self._date_created = None
        self._date_modified = None
        self._modified_by = None
        self._created_by = None
        self._member_count = None
        self._user_member_count = None
        self._joined_member_count = None
        self._media_settings = None
        self._routing_rules = None
        self._conditional_group_routing = None
        self._bullseye = None
        self._scoring_method = None
        self._acw_settings = None
        self._skill_evaluation_method = None
        self._member_groups = None
        self._queue_flow = None
        self._email_in_queue_flow = None
        self._message_in_queue_flow = None
        self._whisper_prompt = None
        self._on_hold_prompt = None
        self._auto_answer_only = None
        self._enable_transcription = None
        self._enable_audio_monitoring = None
        self._enable_manual_assignment = None
        self._agent_owned_routing = None
        self._direct_routing = None
        self._calling_party_name = None
        self._calling_party_number = None
        self._default_scripts = None
        self._outbound_messaging_addresses = None
        self._outbound_email_address = None
        self._peer_id = None
        self._suppress_in_queue_call_recording = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Queue.
        The globally unique identifier for the object.

        :return: The id of this Queue.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Queue.
        The globally unique identifier for the object.

        :param id: The id of this Queue.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Queue.


        :return: The name of this Queue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Queue.


        :param name: The name of this Queue.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this Queue.
        The division to which this entity belongs.

        :return: The division of this Queue.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this Queue.
        The division to which this entity belongs.

        :param division: The division of this Queue.
        :type: Division
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this Queue.
        The queue description.

        :return: The description of this Queue.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this Queue.
        The queue description.

        :param description: The description of this Queue.
        :type: str
        """
        

        self._description = description

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Queue.
        The date the queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Queue.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Queue.
        The date the queue was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Queue.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this Queue.
        The date of the last modification to the queue. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Queue.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this Queue.
        The date of the last modification to the queue. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Queue.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> str:
        """
        Gets the modified_by of this Queue.
        The ID of the user that last modified the queue.

        :return: The modified_by of this Queue.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: str) -> None:
        """
        Sets the modified_by of this Queue.
        The ID of the user that last modified the queue.

        :param modified_by: The modified_by of this Queue.
        :type: str
        """
        

        self._modified_by = modified_by

    @property
    def created_by(self) -> str:
        """
        Gets the created_by of this Queue.
        The ID of the user that created the queue.

        :return: The created_by of this Queue.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: str) -> None:
        """
        Sets the created_by of this Queue.
        The ID of the user that created the queue.

        :param created_by: The created_by of this Queue.
        :type: str
        """
        

        self._created_by = created_by

    @property
    def member_count(self) -> int:
        """
        Gets the member_count of this Queue.
        The total number of members in the queue.

        :return: The member_count of this Queue.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count: int) -> None:
        """
        Sets the member_count of this Queue.
        The total number of members in the queue.

        :param member_count: The member_count of this Queue.
        :type: int
        """
        

        self._member_count = member_count

    @property
    def user_member_count(self) -> int:
        """
        Gets the user_member_count of this Queue.
        The number of user members (i.e., non-group members) in the queue.

        :return: The user_member_count of this Queue.
        :rtype: int
        """
        return self._user_member_count

    @user_member_count.setter
    def user_member_count(self, user_member_count: int) -> None:
        """
        Sets the user_member_count of this Queue.
        The number of user members (i.e., non-group members) in the queue.

        :param user_member_count: The user_member_count of this Queue.
        :type: int
        """
        

        self._user_member_count = user_member_count

    @property
    def joined_member_count(self) -> int:
        """
        Gets the joined_member_count of this Queue.
        The number of joined members in the queue.

        :return: The joined_member_count of this Queue.
        :rtype: int
        """
        return self._joined_member_count

    @joined_member_count.setter
    def joined_member_count(self, joined_member_count: int) -> None:
        """
        Sets the joined_member_count of this Queue.
        The number of joined members in the queue.

        :param joined_member_count: The joined_member_count of this Queue.
        :type: int
        """
        

        self._joined_member_count = joined_member_count

    @property
    def media_settings(self) -> 'QueueMediaSettings':
        """
        Gets the media_settings of this Queue.
        The media settings for the queue.

        :return: The media_settings of this Queue.
        :rtype: QueueMediaSettings
        """
        return self._media_settings

    @media_settings.setter
    def media_settings(self, media_settings: 'QueueMediaSettings') -> None:
        """
        Sets the media_settings of this Queue.
        The media settings for the queue.

        :param media_settings: The media_settings of this Queue.
        :type: QueueMediaSettings
        """
        

        self._media_settings = media_settings

    @property
    def routing_rules(self) -> List['RoutingRule']:
        """
        Gets the routing_rules of this Queue.
        The routing rules for the queue, used for Preferred Agent Routing.

        :return: The routing_rules of this Queue.
        :rtype: list[RoutingRule]
        """
        return self._routing_rules

    @routing_rules.setter
    def routing_rules(self, routing_rules: List['RoutingRule']) -> None:
        """
        Sets the routing_rules of this Queue.
        The routing rules for the queue, used for Preferred Agent Routing.

        :param routing_rules: The routing_rules of this Queue.
        :type: list[RoutingRule]
        """
        

        self._routing_rules = routing_rules

    @property
    def conditional_group_routing(self) -> 'ConditionalGroupRouting':
        """
        Gets the conditional_group_routing of this Queue.
        The Conditional Group Routing settings for the queue.

        :return: The conditional_group_routing of this Queue.
        :rtype: ConditionalGroupRouting
        """
        return self._conditional_group_routing

    @conditional_group_routing.setter
    def conditional_group_routing(self, conditional_group_routing: 'ConditionalGroupRouting') -> None:
        """
        Sets the conditional_group_routing of this Queue.
        The Conditional Group Routing settings for the queue.

        :param conditional_group_routing: The conditional_group_routing of this Queue.
        :type: ConditionalGroupRouting
        """
        

        self._conditional_group_routing = conditional_group_routing

    @property
    def bullseye(self) -> 'Bullseye':
        """
        Gets the bullseye of this Queue.
        The bullseye settings for the queue.

        :return: The bullseye of this Queue.
        :rtype: Bullseye
        """
        return self._bullseye

    @bullseye.setter
    def bullseye(self, bullseye: 'Bullseye') -> None:
        """
        Sets the bullseye of this Queue.
        The bullseye settings for the queue.

        :param bullseye: The bullseye of this Queue.
        :type: Bullseye
        """
        

        self._bullseye = bullseye

    @property
    def scoring_method(self) -> str:
        """
        Gets the scoring_method of this Queue.
        The Scoring Method for the queue

        :return: The scoring_method of this Queue.
        :rtype: str
        """
        return self._scoring_method

    @scoring_method.setter
    def scoring_method(self, scoring_method: str) -> None:
        """
        Sets the scoring_method of this Queue.
        The Scoring Method for the queue

        :param scoring_method: The scoring_method of this Queue.
        :type: str
        """
        if isinstance(scoring_method, int):
            scoring_method = str(scoring_method)
        allowed_values = ["TimestampAndPriority", "PriorityOnly"]
        if scoring_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for scoring_method -> " + scoring_method)
            self._scoring_method = "outdated_sdk_version"
        else:
            self._scoring_method = scoring_method

    @property
    def acw_settings(self) -> 'AcwSettings':
        """
        Gets the acw_settings of this Queue.
        The ACW settings for the queue.

        :return: The acw_settings of this Queue.
        :rtype: AcwSettings
        """
        return self._acw_settings

    @acw_settings.setter
    def acw_settings(self, acw_settings: 'AcwSettings') -> None:
        """
        Sets the acw_settings of this Queue.
        The ACW settings for the queue.

        :param acw_settings: The acw_settings of this Queue.
        :type: AcwSettings
        """
        

        self._acw_settings = acw_settings

    @property
    def skill_evaluation_method(self) -> str:
        """
        Gets the skill_evaluation_method of this Queue.
        The skill evaluation method to use when routing conversations.

        :return: The skill_evaluation_method of this Queue.
        :rtype: str
        """
        return self._skill_evaluation_method

    @skill_evaluation_method.setter
    def skill_evaluation_method(self, skill_evaluation_method: str) -> None:
        """
        Sets the skill_evaluation_method of this Queue.
        The skill evaluation method to use when routing conversations.

        :param skill_evaluation_method: The skill_evaluation_method of this Queue.
        :type: str
        """
        if isinstance(skill_evaluation_method, int):
            skill_evaluation_method = str(skill_evaluation_method)
        allowed_values = ["NONE", "BEST", "ALL"]
        if skill_evaluation_method.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for skill_evaluation_method -> " + skill_evaluation_method)
            self._skill_evaluation_method = "outdated_sdk_version"
        else:
            self._skill_evaluation_method = skill_evaluation_method

    @property
    def member_groups(self) -> List['MemberGroup']:
        """
        Gets the member_groups of this Queue.
        The groups of agents associated with the queue, if any.  Queue membership will update to match group membership changes.

        :return: The member_groups of this Queue.
        :rtype: list[MemberGroup]
        """
        return self._member_groups

    @member_groups.setter
    def member_groups(self, member_groups: List['MemberGroup']) -> None:
        """
        Sets the member_groups of this Queue.
        The groups of agents associated with the queue, if any.  Queue membership will update to match group membership changes.

        :param member_groups: The member_groups of this Queue.
        :type: list[MemberGroup]
        """
        

        self._member_groups = member_groups

    @property
    def queue_flow(self) -> 'DomainEntityRef':
        """
        Gets the queue_flow of this Queue.
        The in-queue flow to use for call conversations waiting in queue.

        :return: The queue_flow of this Queue.
        :rtype: DomainEntityRef
        """
        return self._queue_flow

    @queue_flow.setter
    def queue_flow(self, queue_flow: 'DomainEntityRef') -> None:
        """
        Sets the queue_flow of this Queue.
        The in-queue flow to use for call conversations waiting in queue.

        :param queue_flow: The queue_flow of this Queue.
        :type: DomainEntityRef
        """
        

        self._queue_flow = queue_flow

    @property
    def email_in_queue_flow(self) -> 'DomainEntityRef':
        """
        Gets the email_in_queue_flow of this Queue.
        The in-queue flow to use for email conversations waiting in queue.

        :return: The email_in_queue_flow of this Queue.
        :rtype: DomainEntityRef
        """
        return self._email_in_queue_flow

    @email_in_queue_flow.setter
    def email_in_queue_flow(self, email_in_queue_flow: 'DomainEntityRef') -> None:
        """
        Sets the email_in_queue_flow of this Queue.
        The in-queue flow to use for email conversations waiting in queue.

        :param email_in_queue_flow: The email_in_queue_flow of this Queue.
        :type: DomainEntityRef
        """
        

        self._email_in_queue_flow = email_in_queue_flow

    @property
    def message_in_queue_flow(self) -> 'DomainEntityRef':
        """
        Gets the message_in_queue_flow of this Queue.
        The in-queue flow to use for message conversations waiting in queue.

        :return: The message_in_queue_flow of this Queue.
        :rtype: DomainEntityRef
        """
        return self._message_in_queue_flow

    @message_in_queue_flow.setter
    def message_in_queue_flow(self, message_in_queue_flow: 'DomainEntityRef') -> None:
        """
        Sets the message_in_queue_flow of this Queue.
        The in-queue flow to use for message conversations waiting in queue.

        :param message_in_queue_flow: The message_in_queue_flow of this Queue.
        :type: DomainEntityRef
        """
        

        self._message_in_queue_flow = message_in_queue_flow

    @property
    def whisper_prompt(self) -> 'DomainEntityRef':
        """
        Gets the whisper_prompt of this Queue.
        The prompt used for whisper on the queue, if configured.

        :return: The whisper_prompt of this Queue.
        :rtype: DomainEntityRef
        """
        return self._whisper_prompt

    @whisper_prompt.setter
    def whisper_prompt(self, whisper_prompt: 'DomainEntityRef') -> None:
        """
        Sets the whisper_prompt of this Queue.
        The prompt used for whisper on the queue, if configured.

        :param whisper_prompt: The whisper_prompt of this Queue.
        :type: DomainEntityRef
        """
        

        self._whisper_prompt = whisper_prompt

    @property
    def on_hold_prompt(self) -> 'DomainEntityRef':
        """
        Gets the on_hold_prompt of this Queue.
        The audio to be played when calls on this queue are on hold. If not configured, the default on-hold music will play.

        :return: The on_hold_prompt of this Queue.
        :rtype: DomainEntityRef
        """
        return self._on_hold_prompt

    @on_hold_prompt.setter
    def on_hold_prompt(self, on_hold_prompt: 'DomainEntityRef') -> None:
        """
        Sets the on_hold_prompt of this Queue.
        The audio to be played when calls on this queue are on hold. If not configured, the default on-hold music will play.

        :param on_hold_prompt: The on_hold_prompt of this Queue.
        :type: DomainEntityRef
        """
        

        self._on_hold_prompt = on_hold_prompt

    @property
    def auto_answer_only(self) -> bool:
        """
        Gets the auto_answer_only of this Queue.
        Specifies whether the configured whisper should play for all ACD calls, or only for those which are auto-answered.

        :return: The auto_answer_only of this Queue.
        :rtype: bool
        """
        return self._auto_answer_only

    @auto_answer_only.setter
    def auto_answer_only(self, auto_answer_only: bool) -> None:
        """
        Sets the auto_answer_only of this Queue.
        Specifies whether the configured whisper should play for all ACD calls, or only for those which are auto-answered.

        :param auto_answer_only: The auto_answer_only of this Queue.
        :type: bool
        """
        

        self._auto_answer_only = auto_answer_only

    @property
    def enable_transcription(self) -> bool:
        """
        Gets the enable_transcription of this Queue.
        Indicates whether voice transcription is enabled for this queue.

        :return: The enable_transcription of this Queue.
        :rtype: bool
        """
        return self._enable_transcription

    @enable_transcription.setter
    def enable_transcription(self, enable_transcription: bool) -> None:
        """
        Sets the enable_transcription of this Queue.
        Indicates whether voice transcription is enabled for this queue.

        :param enable_transcription: The enable_transcription of this Queue.
        :type: bool
        """
        

        self._enable_transcription = enable_transcription

    @property
    def enable_audio_monitoring(self) -> bool:
        """
        Gets the enable_audio_monitoring of this Queue.
        Indicates whether audio monitoring is enabled for this queue.

        :return: The enable_audio_monitoring of this Queue.
        :rtype: bool
        """
        return self._enable_audio_monitoring

    @enable_audio_monitoring.setter
    def enable_audio_monitoring(self, enable_audio_monitoring: bool) -> None:
        """
        Sets the enable_audio_monitoring of this Queue.
        Indicates whether audio monitoring is enabled for this queue.

        :param enable_audio_monitoring: The enable_audio_monitoring of this Queue.
        :type: bool
        """
        

        self._enable_audio_monitoring = enable_audio_monitoring

    @property
    def enable_manual_assignment(self) -> bool:
        """
        Gets the enable_manual_assignment of this Queue.
        Indicates whether manual assignment is enabled for this queue.

        :return: The enable_manual_assignment of this Queue.
        :rtype: bool
        """
        return self._enable_manual_assignment

    @enable_manual_assignment.setter
    def enable_manual_assignment(self, enable_manual_assignment: bool) -> None:
        """
        Sets the enable_manual_assignment of this Queue.
        Indicates whether manual assignment is enabled for this queue.

        :param enable_manual_assignment: The enable_manual_assignment of this Queue.
        :type: bool
        """
        

        self._enable_manual_assignment = enable_manual_assignment

    @property
    def agent_owned_routing(self) -> 'AgentOwnedRouting':
        """
        Gets the agent_owned_routing of this Queue.
        The Agent Owned Routing settings for the queue

        :return: The agent_owned_routing of this Queue.
        :rtype: AgentOwnedRouting
        """
        return self._agent_owned_routing

    @agent_owned_routing.setter
    def agent_owned_routing(self, agent_owned_routing: 'AgentOwnedRouting') -> None:
        """
        Sets the agent_owned_routing of this Queue.
        The Agent Owned Routing settings for the queue

        :param agent_owned_routing: The agent_owned_routing of this Queue.
        :type: AgentOwnedRouting
        """
        

        self._agent_owned_routing = agent_owned_routing

    @property
    def direct_routing(self) -> 'DirectRouting':
        """
        Gets the direct_routing of this Queue.
        The Direct Routing settings for the queue

        :return: The direct_routing of this Queue.
        :rtype: DirectRouting
        """
        return self._direct_routing

    @direct_routing.setter
    def direct_routing(self, direct_routing: 'DirectRouting') -> None:
        """
        Sets the direct_routing of this Queue.
        The Direct Routing settings for the queue

        :param direct_routing: The direct_routing of this Queue.
        :type: DirectRouting
        """
        

        self._direct_routing = direct_routing

    @property
    def calling_party_name(self) -> str:
        """
        Gets the calling_party_name of this Queue.
        The name to use for caller identification for outbound calls from this queue.

        :return: The calling_party_name of this Queue.
        :rtype: str
        """
        return self._calling_party_name

    @calling_party_name.setter
    def calling_party_name(self, calling_party_name: str) -> None:
        """
        Sets the calling_party_name of this Queue.
        The name to use for caller identification for outbound calls from this queue.

        :param calling_party_name: The calling_party_name of this Queue.
        :type: str
        """
        

        self._calling_party_name = calling_party_name

    @property
    def calling_party_number(self) -> str:
        """
        Gets the calling_party_number of this Queue.
        The phone number to use for caller identification for outbound calls from this queue.

        :return: The calling_party_number of this Queue.
        :rtype: str
        """
        return self._calling_party_number

    @calling_party_number.setter
    def calling_party_number(self, calling_party_number: str) -> None:
        """
        Sets the calling_party_number of this Queue.
        The phone number to use for caller identification for outbound calls from this queue.

        :param calling_party_number: The calling_party_number of this Queue.
        :type: str
        """
        

        self._calling_party_number = calling_party_number

    @property
    def default_scripts(self) -> Dict[str, 'Script']:
        """
        Gets the default_scripts of this Queue.
        The default script Ids for the communication types.

        :return: The default_scripts of this Queue.
        :rtype: dict(str, Script)
        """
        return self._default_scripts

    @default_scripts.setter
    def default_scripts(self, default_scripts: Dict[str, 'Script']) -> None:
        """
        Sets the default_scripts of this Queue.
        The default script Ids for the communication types.

        :param default_scripts: The default_scripts of this Queue.
        :type: dict(str, Script)
        """
        

        self._default_scripts = default_scripts

    @property
    def outbound_messaging_addresses(self) -> 'QueueMessagingAddresses':
        """
        Gets the outbound_messaging_addresses of this Queue.
        The messaging addresses for the queue.

        :return: The outbound_messaging_addresses of this Queue.
        :rtype: QueueMessagingAddresses
        """
        return self._outbound_messaging_addresses

    @outbound_messaging_addresses.setter
    def outbound_messaging_addresses(self, outbound_messaging_addresses: 'QueueMessagingAddresses') -> None:
        """
        Sets the outbound_messaging_addresses of this Queue.
        The messaging addresses for the queue.

        :param outbound_messaging_addresses: The outbound_messaging_addresses of this Queue.
        :type: QueueMessagingAddresses
        """
        

        self._outbound_messaging_addresses = outbound_messaging_addresses

    @property
    def outbound_email_address(self) -> 'QueueEmailAddress':
        """
        Gets the outbound_email_address of this Queue.


        :return: The outbound_email_address of this Queue.
        :rtype: QueueEmailAddress
        """
        return self._outbound_email_address

    @outbound_email_address.setter
    def outbound_email_address(self, outbound_email_address: 'QueueEmailAddress') -> None:
        """
        Sets the outbound_email_address of this Queue.


        :param outbound_email_address: The outbound_email_address of this Queue.
        :type: QueueEmailAddress
        """
        

        self._outbound_email_address = outbound_email_address

    @property
    def peer_id(self) -> str:
        """
        Gets the peer_id of this Queue.
        The ID of an associated external queue.

        :return: The peer_id of this Queue.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id: str) -> None:
        """
        Sets the peer_id of this Queue.
        The ID of an associated external queue.

        :param peer_id: The peer_id of this Queue.
        :type: str
        """
        

        self._peer_id = peer_id

    @property
    def suppress_in_queue_call_recording(self) -> bool:
        """
        Gets the suppress_in_queue_call_recording of this Queue.
        Indicates whether recording in-queue calls is suppressed for this queue.

        :return: The suppress_in_queue_call_recording of this Queue.
        :rtype: bool
        """
        return self._suppress_in_queue_call_recording

    @suppress_in_queue_call_recording.setter
    def suppress_in_queue_call_recording(self, suppress_in_queue_call_recording: bool) -> None:
        """
        Sets the suppress_in_queue_call_recording of this Queue.
        Indicates whether recording in-queue calls is suppressed for this queue.

        :param suppress_in_queue_call_recording: The suppress_in_queue_call_recording of this Queue.
        :type: bool
        """
        

        self._suppress_in_queue_call_recording = suppress_in_queue_call_recording

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Queue.
        The URI for this object

        :return: The self_uri of this Queue.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Queue.
        The URI for this object

        :param self_uri: The self_uri of this Queue.
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

