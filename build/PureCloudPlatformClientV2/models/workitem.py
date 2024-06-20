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
    from . import AutoStatusTransitionDetail
    from . import Division
    from . import ExternalContactReference
    from . import LanguageReference
    from . import RoutingSkillReference
    from . import UserReference
    from . import UserReferenceWithName
    from . import WorkbinReference
    from . import WorkitemQueueReference
    from . import WorkitemSchema
    from . import WorkitemScoredAgent
    from . import WorkitemStatusReference
    from . import WorkitemUtilizationLabelReference
    from . import WorktypeReference

class Workitem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Workitem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'division': 'Division',
            'type': 'WorktypeReference',
            'description': 'str',
            'language': 'LanguageReference',
            'utilization_label': 'WorkitemUtilizationLabelReference',
            'priority': 'int',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'date_due': 'datetime',
            'date_expires': 'datetime',
            'duration_seconds': 'int',
            'ttl': 'int',
            'status': 'WorkitemStatusReference',
            'status_category': 'str',
            'date_status_changed': 'datetime',
            'date_closed': 'datetime',
            'workbin': 'WorkbinReference',
            'reporter': 'UserReferenceWithName',
            'assignee': 'UserReferenceWithName',
            'external_contact': 'ExternalContactReference',
            'external_tag': 'str',
            'modified_by': 'UserReference',
            'queue': 'WorkitemQueueReference',
            'assignment_state': 'str',
            'date_assignment_state_changed': 'datetime',
            'alert_timeout_seconds': 'int',
            'skills': 'list[RoutingSkillReference]',
            'preferred_agents': 'list[UserReference]',
            'auto_status_transition': 'bool',
            'schema': 'WorkitemSchema',
            'custom_fields': 'dict(str, object)',
            'auto_status_transition_detail': 'AutoStatusTransitionDetail',
            'scored_agents': 'list[WorkitemScoredAgent]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'type': 'type',
            'description': 'description',
            'language': 'language',
            'utilization_label': 'utilizationLabel',
            'priority': 'priority',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'date_due': 'dateDue',
            'date_expires': 'dateExpires',
            'duration_seconds': 'durationSeconds',
            'ttl': 'ttl',
            'status': 'status',
            'status_category': 'statusCategory',
            'date_status_changed': 'dateStatusChanged',
            'date_closed': 'dateClosed',
            'workbin': 'workbin',
            'reporter': 'reporter',
            'assignee': 'assignee',
            'external_contact': 'externalContact',
            'external_tag': 'externalTag',
            'modified_by': 'modifiedBy',
            'queue': 'queue',
            'assignment_state': 'assignmentState',
            'date_assignment_state_changed': 'dateAssignmentStateChanged',
            'alert_timeout_seconds': 'alertTimeoutSeconds',
            'skills': 'skills',
            'preferred_agents': 'preferredAgents',
            'auto_status_transition': 'autoStatusTransition',
            'schema': 'schema',
            'custom_fields': 'customFields',
            'auto_status_transition_detail': 'autoStatusTransitionDetail',
            'scored_agents': 'scoredAgents',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._type = None
        self._description = None
        self._language = None
        self._utilization_label = None
        self._priority = None
        self._date_created = None
        self._date_modified = None
        self._date_due = None
        self._date_expires = None
        self._duration_seconds = None
        self._ttl = None
        self._status = None
        self._status_category = None
        self._date_status_changed = None
        self._date_closed = None
        self._workbin = None
        self._reporter = None
        self._assignee = None
        self._external_contact = None
        self._external_tag = None
        self._modified_by = None
        self._queue = None
        self._assignment_state = None
        self._date_assignment_state_changed = None
        self._alert_timeout_seconds = None
        self._skills = None
        self._preferred_agents = None
        self._auto_status_transition = None
        self._schema = None
        self._custom_fields = None
        self._auto_status_transition_detail = None
        self._scored_agents = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Workitem.
        The globally unique identifier for the object.

        :return: The id of this Workitem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Workitem.
        The globally unique identifier for the object.

        :param id: The id of this Workitem.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Workitem.
        The name of the Workitem.

        :return: The name of this Workitem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Workitem.
        The name of the Workitem.

        :param name: The name of this Workitem.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this Workitem.
        The division to which this entity belongs.

        :return: The division of this Workitem.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this Workitem.
        The division to which this entity belongs.

        :param division: The division of this Workitem.
        :type: Division
        """
        

        self._division = division

    @property
    def type(self) -> 'WorktypeReference':
        """
        Gets the type of this Workitem.
        The Worktype of the Workitem.

        :return: The type of this Workitem.
        :rtype: WorktypeReference
        """
        return self._type

    @type.setter
    def type(self, type: 'WorktypeReference') -> None:
        """
        Sets the type of this Workitem.
        The Worktype of the Workitem.

        :param type: The type of this Workitem.
        :type: WorktypeReference
        """
        

        self._type = type

    @property
    def description(self) -> str:
        """
        Gets the description of this Workitem.
        The description of the Workitem.

        :return: The description of this Workitem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this Workitem.
        The description of the Workitem.

        :param description: The description of this Workitem.
        :type: str
        """
        

        self._description = description

    @property
    def language(self) -> 'LanguageReference':
        """
        Gets the language of this Workitem.
        The language of the Workitem.

        :return: The language of this Workitem.
        :rtype: LanguageReference
        """
        return self._language

    @language.setter
    def language(self, language: 'LanguageReference') -> None:
        """
        Sets the language of this Workitem.
        The language of the Workitem.

        :param language: The language of this Workitem.
        :type: LanguageReference
        """
        

        self._language = language

    @property
    def utilization_label(self) -> 'WorkitemUtilizationLabelReference':
        """
        Gets the utilization_label of this Workitem.
        The utilization label of the Workitem.

        :return: The utilization_label of this Workitem.
        :rtype: WorkitemUtilizationLabelReference
        """
        return self._utilization_label

    @utilization_label.setter
    def utilization_label(self, utilization_label: 'WorkitemUtilizationLabelReference') -> None:
        """
        Sets the utilization_label of this Workitem.
        The utilization label of the Workitem.

        :param utilization_label: The utilization_label of this Workitem.
        :type: WorkitemUtilizationLabelReference
        """
        

        self._utilization_label = utilization_label

    @property
    def priority(self) -> int:
        """
        Gets the priority of this Workitem.
        The priority of the Workitem. The valid range is between -25,000,000 and 25,000,000.

        :return: The priority of this Workitem.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority: int) -> None:
        """
        Sets the priority of this Workitem.
        The priority of the Workitem. The valid range is between -25,000,000 and 25,000,000.

        :param priority: The priority of this Workitem.
        :type: int
        """
        

        self._priority = priority

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Workitem.
        The creation date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Workitem.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Workitem.
        The creation date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Workitem.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this Workitem.
        The modified date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Workitem.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this Workitem.
        The modified date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Workitem.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def date_due(self) -> datetime:
        """
        Gets the date_due of this Workitem.
        The due date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_due of this Workitem.
        :rtype: datetime
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due: datetime) -> None:
        """
        Sets the date_due of this Workitem.
        The due date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_due: The date_due of this Workitem.
        :type: datetime
        """
        

        self._date_due = date_due

    @property
    def date_expires(self) -> datetime:
        """
        Gets the date_expires of this Workitem.
        The expiry date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_expires of this Workitem.
        :rtype: datetime
        """
        return self._date_expires

    @date_expires.setter
    def date_expires(self, date_expires: datetime) -> None:
        """
        Sets the date_expires of this Workitem.
        The expiry date of the Workitem. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_expires: The date_expires of this Workitem.
        :type: datetime
        """
        

        self._date_expires = date_expires

    @property
    def duration_seconds(self) -> int:
        """
        Gets the duration_seconds of this Workitem.
        The estimated duration in seconds to complete the workitem.

        :return: The duration_seconds of this Workitem.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds: int) -> None:
        """
        Sets the duration_seconds of this Workitem.
        The estimated duration in seconds to complete the workitem.

        :param duration_seconds: The duration_seconds of this Workitem.
        :type: int
        """
        

        self._duration_seconds = duration_seconds

    @property
    def ttl(self) -> int:
        """
        Gets the ttl of this Workitem.
        The time to live of the Workitem in seconds.

        :return: The ttl of this Workitem.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl: int) -> None:
        """
        Sets the ttl of this Workitem.
        The time to live of the Workitem in seconds.

        :param ttl: The ttl of this Workitem.
        :type: int
        """
        

        self._ttl = ttl

    @property
    def status(self) -> 'WorkitemStatusReference':
        """
        Gets the status of this Workitem.
        The current Status of the Workitem.

        :return: The status of this Workitem.
        :rtype: WorkitemStatusReference
        """
        return self._status

    @status.setter
    def status(self, status: 'WorkitemStatusReference') -> None:
        """
        Sets the status of this Workitem.
        The current Status of the Workitem.

        :param status: The status of this Workitem.
        :type: WorkitemStatusReference
        """
        

        self._status = status

    @property
    def status_category(self) -> str:
        """
        Gets the status_category of this Workitem.
        The Category of the current Status of the Workitem.

        :return: The status_category of this Workitem.
        :rtype: str
        """
        return self._status_category

    @status_category.setter
    def status_category(self, status_category: str) -> None:
        """
        Sets the status_category of this Workitem.
        The Category of the current Status of the Workitem.

        :param status_category: The status_category of this Workitem.
        :type: str
        """
        if isinstance(status_category, int):
            status_category = str(status_category)
        allowed_values = ["Open", "InProgress", "Waiting", "Closed", "Unknown"]
        if status_category.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status_category -> " + status_category)
            self._status_category = "outdated_sdk_version"
        else:
            self._status_category = status_category

    @property
    def date_status_changed(self) -> datetime:
        """
        Gets the date_status_changed of this Workitem.
        The State change date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_status_changed of this Workitem.
        :rtype: datetime
        """
        return self._date_status_changed

    @date_status_changed.setter
    def date_status_changed(self, date_status_changed: datetime) -> None:
        """
        Sets the date_status_changed of this Workitem.
        The State change date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_status_changed: The date_status_changed of this Workitem.
        :type: datetime
        """
        

        self._date_status_changed = date_status_changed

    @property
    def date_closed(self) -> datetime:
        """
        Gets the date_closed of this Workitem.
        The date the Workitem was closed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_closed of this Workitem.
        :rtype: datetime
        """
        return self._date_closed

    @date_closed.setter
    def date_closed(self, date_closed: datetime) -> None:
        """
        Sets the date_closed of this Workitem.
        The date the Workitem was closed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_closed: The date_closed of this Workitem.
        :type: datetime
        """
        

        self._date_closed = date_closed

    @property
    def workbin(self) -> 'WorkbinReference':
        """
        Gets the workbin of this Workitem.
        The Workbin that contains the Workitem.

        :return: The workbin of this Workitem.
        :rtype: WorkbinReference
        """
        return self._workbin

    @workbin.setter
    def workbin(self, workbin: 'WorkbinReference') -> None:
        """
        Sets the workbin of this Workitem.
        The Workbin that contains the Workitem.

        :param workbin: The workbin of this Workitem.
        :type: WorkbinReference
        """
        

        self._workbin = workbin

    @property
    def reporter(self) -> 'UserReferenceWithName':
        """
        Gets the reporter of this Workitem.
        The reporter of the Workitem.

        :return: The reporter of this Workitem.
        :rtype: UserReferenceWithName
        """
        return self._reporter

    @reporter.setter
    def reporter(self, reporter: 'UserReferenceWithName') -> None:
        """
        Sets the reporter of this Workitem.
        The reporter of the Workitem.

        :param reporter: The reporter of this Workitem.
        :type: UserReferenceWithName
        """
        

        self._reporter = reporter

    @property
    def assignee(self) -> 'UserReferenceWithName':
        """
        Gets the assignee of this Workitem.
        The assignee of the Workitem.

        :return: The assignee of this Workitem.
        :rtype: UserReferenceWithName
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee: 'UserReferenceWithName') -> None:
        """
        Sets the assignee of this Workitem.
        The assignee of the Workitem.

        :param assignee: The assignee of this Workitem.
        :type: UserReferenceWithName
        """
        

        self._assignee = assignee

    @property
    def external_contact(self) -> 'ExternalContactReference':
        """
        Gets the external_contact of this Workitem.
        The external contact of the Workitem.

        :return: The external_contact of this Workitem.
        :rtype: ExternalContactReference
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact: 'ExternalContactReference') -> None:
        """
        Sets the external_contact of this Workitem.
        The external contact of the Workitem.

        :param external_contact: The external_contact of this Workitem.
        :type: ExternalContactReference
        """
        

        self._external_contact = external_contact

    @property
    def external_tag(self) -> str:
        """
        Gets the external_tag of this Workitem.
        The external tag of the Workitem.

        :return: The external_tag of this Workitem.
        :rtype: str
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag: str) -> None:
        """
        Sets the external_tag of this Workitem.
        The external tag of the Workitem.

        :param external_tag: The external_tag of this Workitem.
        :type: str
        """
        

        self._external_tag = external_tag

    @property
    def modified_by(self) -> 'UserReference':
        """
        Gets the modified_by of this Workitem.
        The User who modified the Workitem.

        :return: The modified_by of this Workitem.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'UserReference') -> None:
        """
        Sets the modified_by of this Workitem.
        The User who modified the Workitem.

        :param modified_by: The modified_by of this Workitem.
        :type: UserReference
        """
        

        self._modified_by = modified_by

    @property
    def queue(self) -> 'WorkitemQueueReference':
        """
        Gets the queue of this Workitem.
        The Workitems queue.

        :return: The queue of this Workitem.
        :rtype: WorkitemQueueReference
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'WorkitemQueueReference') -> None:
        """
        Sets the queue of this Workitem.
        The Workitems queue.

        :param queue: The queue of this Workitem.
        :type: WorkitemQueueReference
        """
        

        self._queue = queue

    @property
    def assignment_state(self) -> str:
        """
        Gets the assignment_state of this Workitem.
        The assignment state of the workitem.

        :return: The assignment_state of this Workitem.
        :rtype: str
        """
        return self._assignment_state

    @assignment_state.setter
    def assignment_state(self, assignment_state: str) -> None:
        """
        Sets the assignment_state of this Workitem.
        The assignment state of the workitem.

        :param assignment_state: The assignment_state of this Workitem.
        :type: str
        """
        if isinstance(assignment_state, int):
            assignment_state = str(assignment_state)
        allowed_values = ["Unknown", "AcdStarted", "Alerting", "AlertTimeout", "AcdCancelled", "Terminated", "Idle", "Declined", "Connected", "Disconnected", "Parked", "Held", "AcdExpired"]
        if assignment_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for assignment_state -> " + assignment_state)
            self._assignment_state = "outdated_sdk_version"
        else:
            self._assignment_state = assignment_state

    @property
    def date_assignment_state_changed(self) -> datetime:
        """
        Gets the date_assignment_state_changed of this Workitem.
        The assignment state change date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_assignment_state_changed of this Workitem.
        :rtype: datetime
        """
        return self._date_assignment_state_changed

    @date_assignment_state_changed.setter
    def date_assignment_state_changed(self, date_assignment_state_changed: datetime) -> None:
        """
        Sets the date_assignment_state_changed of this Workitem.
        The assignment state change date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_assignment_state_changed: The date_assignment_state_changed of this Workitem.
        :type: datetime
        """
        

        self._date_assignment_state_changed = date_assignment_state_changed

    @property
    def alert_timeout_seconds(self) -> int:
        """
        Gets the alert_timeout_seconds of this Workitem.
        The duration in seconds before an alert will timeout.

        :return: The alert_timeout_seconds of this Workitem.
        :rtype: int
        """
        return self._alert_timeout_seconds

    @alert_timeout_seconds.setter
    def alert_timeout_seconds(self, alert_timeout_seconds: int) -> None:
        """
        Sets the alert_timeout_seconds of this Workitem.
        The duration in seconds before an alert will timeout.

        :param alert_timeout_seconds: The alert_timeout_seconds of this Workitem.
        :type: int
        """
        

        self._alert_timeout_seconds = alert_timeout_seconds

    @property
    def skills(self) -> List['RoutingSkillReference']:
        """
        Gets the skills of this Workitem.
        The skills of the Workitem.

        :return: The skills of this Workitem.
        :rtype: list[RoutingSkillReference]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List['RoutingSkillReference']) -> None:
        """
        Sets the skills of this Workitem.
        The skills of the Workitem.

        :param skills: The skills of this Workitem.
        :type: list[RoutingSkillReference]
        """
        

        self._skills = skills

    @property
    def preferred_agents(self) -> List['UserReference']:
        """
        Gets the preferred_agents of this Workitem.
        The preferred agents of the Workitem.

        :return: The preferred_agents of this Workitem.
        :rtype: list[UserReference]
        """
        return self._preferred_agents

    @preferred_agents.setter
    def preferred_agents(self, preferred_agents: List['UserReference']) -> None:
        """
        Sets the preferred_agents of this Workitem.
        The preferred agents of the Workitem.

        :param preferred_agents: The preferred_agents of this Workitem.
        :type: list[UserReference]
        """
        

        self._preferred_agents = preferred_agents

    @property
    def auto_status_transition(self) -> bool:
        """
        Gets the auto_status_transition of this Workitem.
        Set it to false to disable auto status transition. By default, it is enabled.

        :return: The auto_status_transition of this Workitem.
        :rtype: bool
        """
        return self._auto_status_transition

    @auto_status_transition.setter
    def auto_status_transition(self, auto_status_transition: bool) -> None:
        """
        Sets the auto_status_transition of this Workitem.
        Set it to false to disable auto status transition. By default, it is enabled.

        :param auto_status_transition: The auto_status_transition of this Workitem.
        :type: bool
        """
        

        self._auto_status_transition = auto_status_transition

    @property
    def schema(self) -> 'WorkitemSchema':
        """
        Gets the schema of this Workitem.
        The schema defining the custom fields of the Workitem. The schema is inherited from the Workitems Worktype at creation time.

        :return: The schema of this Workitem.
        :rtype: WorkitemSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema: 'WorkitemSchema') -> None:
        """
        Sets the schema of this Workitem.
        The schema defining the custom fields of the Workitem. The schema is inherited from the Workitems Worktype at creation time.

        :param schema: The schema of this Workitem.
        :type: WorkitemSchema
        """
        

        self._schema = schema

    @property
    def custom_fields(self) -> Dict[str, object]:
        """
        Gets the custom_fields of this Workitem.
        Custom fields defined in the schema referenced by the Workitem.

        :return: The custom_fields of this Workitem.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields: Dict[str, object]) -> None:
        """
        Sets the custom_fields of this Workitem.
        Custom fields defined in the schema referenced by the Workitem.

        :param custom_fields: The custom_fields of this Workitem.
        :type: dict(str, object)
        """
        

        self._custom_fields = custom_fields

    @property
    def auto_status_transition_detail(self) -> 'AutoStatusTransitionDetail':
        """
        Gets the auto_status_transition_detail of this Workitem.
        Auto status transition details of Workitem.

        :return: The auto_status_transition_detail of this Workitem.
        :rtype: AutoStatusTransitionDetail
        """
        return self._auto_status_transition_detail

    @auto_status_transition_detail.setter
    def auto_status_transition_detail(self, auto_status_transition_detail: 'AutoStatusTransitionDetail') -> None:
        """
        Sets the auto_status_transition_detail of this Workitem.
        Auto status transition details of Workitem.

        :param auto_status_transition_detail: The auto_status_transition_detail of this Workitem.
        :type: AutoStatusTransitionDetail
        """
        

        self._auto_status_transition_detail = auto_status_transition_detail

    @property
    def scored_agents(self) -> List['WorkitemScoredAgent']:
        """
        Gets the scored_agents of this Workitem.
        A list of scored agents for the Workitem.

        :return: The scored_agents of this Workitem.
        :rtype: list[WorkitemScoredAgent]
        """
        return self._scored_agents

    @scored_agents.setter
    def scored_agents(self, scored_agents: List['WorkitemScoredAgent']) -> None:
        """
        Sets the scored_agents of this Workitem.
        A list of scored agents for the Workitem.

        :param scored_agents: The scored_agents of this Workitem.
        :type: list[WorkitemScoredAgent]
        """
        

        self._scored_agents = scored_agents

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Workitem.
        The URI for this object

        :return: The self_uri of this Workitem.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Workitem.
        The URI for this object

        :param self_uri: The self_uri of this Workitem.
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

