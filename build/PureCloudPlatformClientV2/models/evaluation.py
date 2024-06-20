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
    from . import Calibration
    from . import ConversationReference
    from . import EvaluationForm
    from . import EvaluationScoringSet
    from . import EvaluationSource
    from . import Queue
    from . import Team
    from . import User

class Evaluation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Evaluation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'conversation': 'ConversationReference',
            'evaluation_form': 'EvaluationForm',
            'evaluator': 'User',
            'agent': 'User',
            'calibration': 'Calibration',
            'status': 'str',
            'answers': 'EvaluationScoringSet',
            'agent_has_read': 'bool',
            'assignee': 'User',
            'assignee_applicable': 'bool',
            'release_date': 'datetime',
            'assigned_date': 'datetime',
            'changed_date': 'datetime',
            'revision_created_date': 'datetime',
            'queue': 'Queue',
            'media_type': 'list[str]',
            'rescore': 'bool',
            'conversation_date': 'datetime',
            'conversation_end_date': 'datetime',
            'never_release': 'bool',
            'assigned': 'bool',
            'date_assignee_changed': 'datetime',
            'resource_id': 'str',
            'resource_type': 'str',
            'redacted': 'bool',
            'agent_team': 'Team',
            'is_scoring_index': 'bool',
            'authorized_actions': 'list[str]',
            'has_assistance_failed': 'bool',
            'evaluation_source': 'EvaluationSource',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'conversation': 'conversation',
            'evaluation_form': 'evaluationForm',
            'evaluator': 'evaluator',
            'agent': 'agent',
            'calibration': 'calibration',
            'status': 'status',
            'answers': 'answers',
            'agent_has_read': 'agentHasRead',
            'assignee': 'assignee',
            'assignee_applicable': 'assigneeApplicable',
            'release_date': 'releaseDate',
            'assigned_date': 'assignedDate',
            'changed_date': 'changedDate',
            'revision_created_date': 'revisionCreatedDate',
            'queue': 'queue',
            'media_type': 'mediaType',
            'rescore': 'rescore',
            'conversation_date': 'conversationDate',
            'conversation_end_date': 'conversationEndDate',
            'never_release': 'neverRelease',
            'assigned': 'assigned',
            'date_assignee_changed': 'dateAssigneeChanged',
            'resource_id': 'resourceId',
            'resource_type': 'resourceType',
            'redacted': 'redacted',
            'agent_team': 'agentTeam',
            'is_scoring_index': 'isScoringIndex',
            'authorized_actions': 'authorizedActions',
            'has_assistance_failed': 'hasAssistanceFailed',
            'evaluation_source': 'evaluationSource',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._conversation = None
        self._evaluation_form = None
        self._evaluator = None
        self._agent = None
        self._calibration = None
        self._status = None
        self._answers = None
        self._agent_has_read = None
        self._assignee = None
        self._assignee_applicable = None
        self._release_date = None
        self._assigned_date = None
        self._changed_date = None
        self._revision_created_date = None
        self._queue = None
        self._media_type = None
        self._rescore = None
        self._conversation_date = None
        self._conversation_end_date = None
        self._never_release = None
        self._assigned = None
        self._date_assignee_changed = None
        self._resource_id = None
        self._resource_type = None
        self._redacted = None
        self._agent_team = None
        self._is_scoring_index = None
        self._authorized_actions = None
        self._has_assistance_failed = None
        self._evaluation_source = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Evaluation.
        The globally unique identifier for the object.

        :return: The id of this Evaluation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Evaluation.
        The globally unique identifier for the object.

        :param id: The id of this Evaluation.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Evaluation.


        :return: The name of this Evaluation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Evaluation.


        :param name: The name of this Evaluation.
        :type: str
        """
        

        self._name = name

    @property
    def conversation(self) -> 'ConversationReference':
        """
        Gets the conversation of this Evaluation.


        :return: The conversation of this Evaluation.
        :rtype: ConversationReference
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'ConversationReference') -> None:
        """
        Sets the conversation of this Evaluation.


        :param conversation: The conversation of this Evaluation.
        :type: ConversationReference
        """
        

        self._conversation = conversation

    @property
    def evaluation_form(self) -> 'EvaluationForm':
        """
        Gets the evaluation_form of this Evaluation.
        Evaluation form used for evaluation.

        :return: The evaluation_form of this Evaluation.
        :rtype: EvaluationForm
        """
        return self._evaluation_form

    @evaluation_form.setter
    def evaluation_form(self, evaluation_form: 'EvaluationForm') -> None:
        """
        Sets the evaluation_form of this Evaluation.
        Evaluation form used for evaluation.

        :param evaluation_form: The evaluation_form of this Evaluation.
        :type: EvaluationForm
        """
        

        self._evaluation_form = evaluation_form

    @property
    def evaluator(self) -> 'User':
        """
        Gets the evaluator of this Evaluation.


        :return: The evaluator of this Evaluation.
        :rtype: User
        """
        return self._evaluator

    @evaluator.setter
    def evaluator(self, evaluator: 'User') -> None:
        """
        Sets the evaluator of this Evaluation.


        :param evaluator: The evaluator of this Evaluation.
        :type: User
        """
        

        self._evaluator = evaluator

    @property
    def agent(self) -> 'User':
        """
        Gets the agent of this Evaluation.


        :return: The agent of this Evaluation.
        :rtype: User
        """
        return self._agent

    @agent.setter
    def agent(self, agent: 'User') -> None:
        """
        Sets the agent of this Evaluation.


        :param agent: The agent of this Evaluation.
        :type: User
        """
        

        self._agent = agent

    @property
    def calibration(self) -> 'Calibration':
        """
        Gets the calibration of this Evaluation.


        :return: The calibration of this Evaluation.
        :rtype: Calibration
        """
        return self._calibration

    @calibration.setter
    def calibration(self, calibration: 'Calibration') -> None:
        """
        Sets the calibration of this Evaluation.


        :param calibration: The calibration of this Evaluation.
        :type: Calibration
        """
        

        self._calibration = calibration

    @property
    def status(self) -> str:
        """
        Gets the status of this Evaluation.


        :return: The status of this Evaluation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this Evaluation.


        :param status: The status of this Evaluation.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["PENDING", "INPROGRESS", "FINISHED", "INREVIEW", "RETRACTED"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def answers(self) -> 'EvaluationScoringSet':
        """
        Gets the answers of this Evaluation.


        :return: The answers of this Evaluation.
        :rtype: EvaluationScoringSet
        """
        return self._answers

    @answers.setter
    def answers(self, answers: 'EvaluationScoringSet') -> None:
        """
        Sets the answers of this Evaluation.


        :param answers: The answers of this Evaluation.
        :type: EvaluationScoringSet
        """
        

        self._answers = answers

    @property
    def agent_has_read(self) -> bool:
        """
        Gets the agent_has_read of this Evaluation.


        :return: The agent_has_read of this Evaluation.
        :rtype: bool
        """
        return self._agent_has_read

    @agent_has_read.setter
    def agent_has_read(self, agent_has_read: bool) -> None:
        """
        Sets the agent_has_read of this Evaluation.


        :param agent_has_read: The agent_has_read of this Evaluation.
        :type: bool
        """
        

        self._agent_has_read = agent_has_read

    @property
    def assignee(self) -> 'User':
        """
        Gets the assignee of this Evaluation.


        :return: The assignee of this Evaluation.
        :rtype: User
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee: 'User') -> None:
        """
        Sets the assignee of this Evaluation.


        :param assignee: The assignee of this Evaluation.
        :type: User
        """
        

        self._assignee = assignee

    @property
    def assignee_applicable(self) -> bool:
        """
        Gets the assignee_applicable of this Evaluation.
        Indicates whether an assignee is applicable for the evaluation. Set to false when assignee is not applicable.

        :return: The assignee_applicable of this Evaluation.
        :rtype: bool
        """
        return self._assignee_applicable

    @assignee_applicable.setter
    def assignee_applicable(self, assignee_applicable: bool) -> None:
        """
        Sets the assignee_applicable of this Evaluation.
        Indicates whether an assignee is applicable for the evaluation. Set to false when assignee is not applicable.

        :param assignee_applicable: The assignee_applicable of this Evaluation.
        :type: bool
        """
        

        self._assignee_applicable = assignee_applicable

    @property
    def release_date(self) -> datetime:
        """
        Gets the release_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The release_date of this Evaluation.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date: datetime) -> None:
        """
        Sets the release_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param release_date: The release_date of this Evaluation.
        :type: datetime
        """
        

        self._release_date = release_date

    @property
    def assigned_date(self) -> datetime:
        """
        Gets the assigned_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The assigned_date of this Evaluation.
        :rtype: datetime
        """
        return self._assigned_date

    @assigned_date.setter
    def assigned_date(self, assigned_date: datetime) -> None:
        """
        Sets the assigned_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param assigned_date: The assigned_date of this Evaluation.
        :type: datetime
        """
        

        self._assigned_date = assigned_date

    @property
    def changed_date(self) -> datetime:
        """
        Gets the changed_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The changed_date of this Evaluation.
        :rtype: datetime
        """
        return self._changed_date

    @changed_date.setter
    def changed_date(self, changed_date: datetime) -> None:
        """
        Sets the changed_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param changed_date: The changed_date of this Evaluation.
        :type: datetime
        """
        

        self._changed_date = changed_date

    @property
    def revision_created_date(self) -> datetime:
        """
        Gets the revision_created_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The revision_created_date of this Evaluation.
        :rtype: datetime
        """
        return self._revision_created_date

    @revision_created_date.setter
    def revision_created_date(self, revision_created_date: datetime) -> None:
        """
        Sets the revision_created_date of this Evaluation.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param revision_created_date: The revision_created_date of this Evaluation.
        :type: datetime
        """
        

        self._revision_created_date = revision_created_date

    @property
    def queue(self) -> 'Queue':
        """
        Gets the queue of this Evaluation.


        :return: The queue of this Evaluation.
        :rtype: Queue
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'Queue') -> None:
        """
        Sets the queue of this Evaluation.


        :param queue: The queue of this Evaluation.
        :type: Queue
        """
        

        self._queue = queue

    @property
    def media_type(self) -> List[str]:
        """
        Gets the media_type of this Evaluation.
        List of different communication types used in conversation.

        :return: The media_type of this Evaluation.
        :rtype: list[str]
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: List[str]) -> None:
        """
        Sets the media_type of this Evaluation.
        List of different communication types used in conversation.

        :param media_type: The media_type of this Evaluation.
        :type: list[str]
        """
        

        self._media_type = media_type

    @property
    def rescore(self) -> bool:
        """
        Gets the rescore of this Evaluation.
        Is only true when evaluation is re-scored.

        :return: The rescore of this Evaluation.
        :rtype: bool
        """
        return self._rescore

    @rescore.setter
    def rescore(self, rescore: bool) -> None:
        """
        Sets the rescore of this Evaluation.
        Is only true when evaluation is re-scored.

        :param rescore: The rescore of this Evaluation.
        :type: bool
        """
        

        self._rescore = rescore

    @property
    def conversation_date(self) -> datetime:
        """
        Gets the conversation_date of this Evaluation.
        Date of conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The conversation_date of this Evaluation.
        :rtype: datetime
        """
        return self._conversation_date

    @conversation_date.setter
    def conversation_date(self, conversation_date: datetime) -> None:
        """
        Sets the conversation_date of this Evaluation.
        Date of conversation. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param conversation_date: The conversation_date of this Evaluation.
        :type: datetime
        """
        

        self._conversation_date = conversation_date

    @property
    def conversation_end_date(self) -> datetime:
        """
        Gets the conversation_end_date of this Evaluation.
        End date of conversation if it had completed before evaluation creation. Null if created before the conversation ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The conversation_end_date of this Evaluation.
        :rtype: datetime
        """
        return self._conversation_end_date

    @conversation_end_date.setter
    def conversation_end_date(self, conversation_end_date: datetime) -> None:
        """
        Sets the conversation_end_date of this Evaluation.
        End date of conversation if it had completed before evaluation creation. Null if created before the conversation ended. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param conversation_end_date: The conversation_end_date of this Evaluation.
        :type: datetime
        """
        

        self._conversation_end_date = conversation_end_date

    @property
    def never_release(self) -> bool:
        """
        Gets the never_release of this Evaluation.
        Signifies if the evaluation is never to be released. This cannot be set true if release date is also set.

        :return: The never_release of this Evaluation.
        :rtype: bool
        """
        return self._never_release

    @never_release.setter
    def never_release(self, never_release: bool) -> None:
        """
        Sets the never_release of this Evaluation.
        Signifies if the evaluation is never to be released. This cannot be set true if release date is also set.

        :param never_release: The never_release of this Evaluation.
        :type: bool
        """
        

        self._never_release = never_release

    @property
    def assigned(self) -> bool:
        """
        Gets the assigned of this Evaluation.
        Set to false to unassign the evaluation. This cannot be set to false when assignee is also set.

        :return: The assigned of this Evaluation.
        :rtype: bool
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned: bool) -> None:
        """
        Sets the assigned of this Evaluation.
        Set to false to unassign the evaluation. This cannot be set to false when assignee is also set.

        :param assigned: The assigned of this Evaluation.
        :type: bool
        """
        

        self._assigned = assigned

    @property
    def date_assignee_changed(self) -> datetime:
        """
        Gets the date_assignee_changed of this Evaluation.
        Date when the assignee was last changed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_assignee_changed of this Evaluation.
        :rtype: datetime
        """
        return self._date_assignee_changed

    @date_assignee_changed.setter
    def date_assignee_changed(self, date_assignee_changed: datetime) -> None:
        """
        Sets the date_assignee_changed of this Evaluation.
        Date when the assignee was last changed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_assignee_changed: The date_assignee_changed of this Evaluation.
        :type: datetime
        """
        

        self._date_assignee_changed = date_assignee_changed

    @property
    def resource_id(self) -> str:
        """
        Gets the resource_id of this Evaluation.
        Only used for email evaluations. Will be null for all other evaluations.

        :return: The resource_id of this Evaluation.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: str) -> None:
        """
        Sets the resource_id of this Evaluation.
        Only used for email evaluations. Will be null for all other evaluations.

        :param resource_id: The resource_id of this Evaluation.
        :type: str
        """
        

        self._resource_id = resource_id

    @property
    def resource_type(self) -> str:
        """
        Gets the resource_type of this Evaluation.
        The type of resource. Only used for email evaluations. Will be null for evaluations on all other resources.

        :return: The resource_type of this Evaluation.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type: str) -> None:
        """
        Sets the resource_type of this Evaluation.
        The type of resource. Only used for email evaluations. Will be null for evaluations on all other resources.

        :param resource_type: The resource_type of this Evaluation.
        :type: str
        """
        if isinstance(resource_type, int):
            resource_type = str(resource_type)
        allowed_values = ["EMAIL"]
        if resource_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for resource_type -> " + resource_type)
            self._resource_type = "outdated_sdk_version"
        else:
            self._resource_type = resource_type

    @property
    def redacted(self) -> bool:
        """
        Gets the redacted of this Evaluation.
        Is only true when the user making the request does not have sufficient permissions to see evaluation

        :return: The redacted of this Evaluation.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted: bool) -> None:
        """
        Sets the redacted of this Evaluation.
        Is only true when the user making the request does not have sufficient permissions to see evaluation

        :param redacted: The redacted of this Evaluation.
        :type: bool
        """
        

        self._redacted = redacted

    @property
    def agent_team(self) -> 'Team':
        """
        Gets the agent_team of this Evaluation.
        Team of the evaluation agent

        :return: The agent_team of this Evaluation.
        :rtype: Team
        """
        return self._agent_team

    @agent_team.setter
    def agent_team(self, agent_team: 'Team') -> None:
        """
        Sets the agent_team of this Evaluation.
        Team of the evaluation agent

        :param agent_team: The agent_team of this Evaluation.
        :type: Team
        """
        

        self._agent_team = agent_team

    @property
    def is_scoring_index(self) -> bool:
        """
        Gets the is_scoring_index of this Evaluation.


        :return: The is_scoring_index of this Evaluation.
        :rtype: bool
        """
        return self._is_scoring_index

    @is_scoring_index.setter
    def is_scoring_index(self, is_scoring_index: bool) -> None:
        """
        Sets the is_scoring_index of this Evaluation.


        :param is_scoring_index: The is_scoring_index of this Evaluation.
        :type: bool
        """
        

        self._is_scoring_index = is_scoring_index

    @property
    def authorized_actions(self) -> List[str]:
        """
        Gets the authorized_actions of this Evaluation.
        List of user authorized actions on evaluation. Possible values: assign, edit, editScore, editAgentSignoff, delete, release, viewAudit

        :return: The authorized_actions of this Evaluation.
        :rtype: list[str]
        """
        return self._authorized_actions

    @authorized_actions.setter
    def authorized_actions(self, authorized_actions: List[str]) -> None:
        """
        Sets the authorized_actions of this Evaluation.
        List of user authorized actions on evaluation. Possible values: assign, edit, editScore, editAgentSignoff, delete, release, viewAudit

        :param authorized_actions: The authorized_actions of this Evaluation.
        :type: list[str]
        """
        

        self._authorized_actions = authorized_actions

    @property
    def has_assistance_failed(self) -> bool:
        """
        Gets the has_assistance_failed of this Evaluation.
        Is true when evaluation assistance didn't execute successfully

        :return: The has_assistance_failed of this Evaluation.
        :rtype: bool
        """
        return self._has_assistance_failed

    @has_assistance_failed.setter
    def has_assistance_failed(self, has_assistance_failed: bool) -> None:
        """
        Sets the has_assistance_failed of this Evaluation.
        Is true when evaluation assistance didn't execute successfully

        :param has_assistance_failed: The has_assistance_failed of this Evaluation.
        :type: bool
        """
        

        self._has_assistance_failed = has_assistance_failed

    @property
    def evaluation_source(self) -> 'EvaluationSource':
        """
        Gets the evaluation_source of this Evaluation.
        The source that created the evaluation.

        :return: The evaluation_source of this Evaluation.
        :rtype: EvaluationSource
        """
        return self._evaluation_source

    @evaluation_source.setter
    def evaluation_source(self, evaluation_source: 'EvaluationSource') -> None:
        """
        Sets the evaluation_source of this Evaluation.
        The source that created the evaluation.

        :param evaluation_source: The evaluation_source of this Evaluation.
        :type: EvaluationSource
        """
        

        self._evaluation_source = evaluation_source

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Evaluation.
        The URI for this object

        :return: The self_uri of this Evaluation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Evaluation.
        The URI for this object

        :param self_uri: The self_uri of this Evaluation.
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

