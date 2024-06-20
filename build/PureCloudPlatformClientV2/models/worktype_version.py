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
    from . import Division
    from . import LanguageReference
    from . import RoutingSkillReference
    from . import UserReference
    from . import WorkbinReference
    from . import WorkitemQueueReference
    from . import WorkitemSchema
    from . import WorkitemStatus
    from . import WorkitemStatusReference

class WorktypeVersion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorktypeVersion - a model defined in Swagger

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
            'default_workbin': 'WorkbinReference',
            'default_status': 'WorkitemStatusReference',
            'statuses': 'list[WorkitemStatus]',
            'default_duration_seconds': 'int',
            'default_expiration_seconds': 'int',
            'default_due_duration_seconds': 'int',
            'default_priority': 'int',
            'default_language': 'LanguageReference',
            'default_ttl_seconds': 'int',
            'modified_by': 'UserReference',
            'default_queue': 'WorkitemQueueReference',
            'default_skills': 'list[RoutingSkillReference]',
            'assignment_enabled': 'bool',
            'schema': 'WorkitemSchema',
            'service_level_target': 'int',
            'version': 'int',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'description': 'description',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'default_workbin': 'defaultWorkbin',
            'default_status': 'defaultStatus',
            'statuses': 'statuses',
            'default_duration_seconds': 'defaultDurationSeconds',
            'default_expiration_seconds': 'defaultExpirationSeconds',
            'default_due_duration_seconds': 'defaultDueDurationSeconds',
            'default_priority': 'defaultPriority',
            'default_language': 'defaultLanguage',
            'default_ttl_seconds': 'defaultTtlSeconds',
            'modified_by': 'modifiedBy',
            'default_queue': 'defaultQueue',
            'default_skills': 'defaultSkills',
            'assignment_enabled': 'assignmentEnabled',
            'schema': 'schema',
            'service_level_target': 'serviceLevelTarget',
            'version': 'version',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._description = None
        self._date_created = None
        self._date_modified = None
        self._default_workbin = None
        self._default_status = None
        self._statuses = None
        self._default_duration_seconds = None
        self._default_expiration_seconds = None
        self._default_due_duration_seconds = None
        self._default_priority = None
        self._default_language = None
        self._default_ttl_seconds = None
        self._modified_by = None
        self._default_queue = None
        self._default_skills = None
        self._assignment_enabled = None
        self._schema = None
        self._service_level_target = None
        self._version = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WorktypeVersion.
        The globally unique identifier for the object.

        :return: The id of this WorktypeVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WorktypeVersion.
        The globally unique identifier for the object.

        :param id: The id of this WorktypeVersion.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this WorktypeVersion.
        The name of the Worktype.

        :return: The name of this WorktypeVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this WorktypeVersion.
        The name of the Worktype.

        :param name: The name of this WorktypeVersion.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this WorktypeVersion.
        The division to which this entity belongs.

        :return: The division of this WorktypeVersion.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this WorktypeVersion.
        The division to which this entity belongs.

        :param division: The division of this WorktypeVersion.
        :type: Division
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this WorktypeVersion.
        The description of the Worktype.

        :return: The description of this WorktypeVersion.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this WorktypeVersion.
        The description of the Worktype.

        :param description: The description of this WorktypeVersion.
        :type: str
        """
        

        self._description = description

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this WorktypeVersion.
        The creation date of the Worktype. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this WorktypeVersion.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this WorktypeVersion.
        The creation date of the Worktype. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this WorktypeVersion.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this WorktypeVersion.
        The modified date of the Worktype. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this WorktypeVersion.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this WorktypeVersion.
        The modified date of the Worktype. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this WorktypeVersion.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def default_workbin(self) -> 'WorkbinReference':
        """
        Gets the default_workbin of this WorktypeVersion.
        The default Workbin for Workitems created from the Worktype.

        :return: The default_workbin of this WorktypeVersion.
        :rtype: WorkbinReference
        """
        return self._default_workbin

    @default_workbin.setter
    def default_workbin(self, default_workbin: 'WorkbinReference') -> None:
        """
        Sets the default_workbin of this WorktypeVersion.
        The default Workbin for Workitems created from the Worktype.

        :param default_workbin: The default_workbin of this WorktypeVersion.
        :type: WorkbinReference
        """
        

        self._default_workbin = default_workbin

    @property
    def default_status(self) -> 'WorkitemStatusReference':
        """
        Gets the default_status of this WorktypeVersion.
        The default status for Workitems created from the Worktype.

        :return: The default_status of this WorktypeVersion.
        :rtype: WorkitemStatusReference
        """
        return self._default_status

    @default_status.setter
    def default_status(self, default_status: 'WorkitemStatusReference') -> None:
        """
        Sets the default_status of this WorktypeVersion.
        The default status for Workitems created from the Worktype.

        :param default_status: The default_status of this WorktypeVersion.
        :type: WorkitemStatusReference
        """
        

        self._default_status = default_status

    @property
    def statuses(self) -> List['WorkitemStatus']:
        """
        Gets the statuses of this WorktypeVersion.
        The list of possible statuses for Workitems created from the Worktype.

        :return: The statuses of this WorktypeVersion.
        :rtype: list[WorkitemStatus]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses: List['WorkitemStatus']) -> None:
        """
        Sets the statuses of this WorktypeVersion.
        The list of possible statuses for Workitems created from the Worktype.

        :param statuses: The statuses of this WorktypeVersion.
        :type: list[WorkitemStatus]
        """
        

        self._statuses = statuses

    @property
    def default_duration_seconds(self) -> int:
        """
        Gets the default_duration_seconds of this WorktypeVersion.
        The default duration in seconds for Workitems created from the Worktype.

        :return: The default_duration_seconds of this WorktypeVersion.
        :rtype: int
        """
        return self._default_duration_seconds

    @default_duration_seconds.setter
    def default_duration_seconds(self, default_duration_seconds: int) -> None:
        """
        Sets the default_duration_seconds of this WorktypeVersion.
        The default duration in seconds for Workitems created from the Worktype.

        :param default_duration_seconds: The default_duration_seconds of this WorktypeVersion.
        :type: int
        """
        

        self._default_duration_seconds = default_duration_seconds

    @property
    def default_expiration_seconds(self) -> int:
        """
        Gets the default_expiration_seconds of this WorktypeVersion.
        The default expiration time in seconds for Workitems created from the Worktype.

        :return: The default_expiration_seconds of this WorktypeVersion.
        :rtype: int
        """
        return self._default_expiration_seconds

    @default_expiration_seconds.setter
    def default_expiration_seconds(self, default_expiration_seconds: int) -> None:
        """
        Sets the default_expiration_seconds of this WorktypeVersion.
        The default expiration time in seconds for Workitems created from the Worktype.

        :param default_expiration_seconds: The default_expiration_seconds of this WorktypeVersion.
        :type: int
        """
        

        self._default_expiration_seconds = default_expiration_seconds

    @property
    def default_due_duration_seconds(self) -> int:
        """
        Gets the default_due_duration_seconds of this WorktypeVersion.
        The default due duration in seconds for Workitems created from the Worktype.

        :return: The default_due_duration_seconds of this WorktypeVersion.
        :rtype: int
        """
        return self._default_due_duration_seconds

    @default_due_duration_seconds.setter
    def default_due_duration_seconds(self, default_due_duration_seconds: int) -> None:
        """
        Sets the default_due_duration_seconds of this WorktypeVersion.
        The default due duration in seconds for Workitems created from the Worktype.

        :param default_due_duration_seconds: The default_due_duration_seconds of this WorktypeVersion.
        :type: int
        """
        

        self._default_due_duration_seconds = default_due_duration_seconds

    @property
    def default_priority(self) -> int:
        """
        Gets the default_priority of this WorktypeVersion.
        The default priority for Workitems created from the Worktype. The valid range is between -25,000,000 and 25,000,000.

        :return: The default_priority of this WorktypeVersion.
        :rtype: int
        """
        return self._default_priority

    @default_priority.setter
    def default_priority(self, default_priority: int) -> None:
        """
        Sets the default_priority of this WorktypeVersion.
        The default priority for Workitems created from the Worktype. The valid range is between -25,000,000 and 25,000,000.

        :param default_priority: The default_priority of this WorktypeVersion.
        :type: int
        """
        

        self._default_priority = default_priority

    @property
    def default_language(self) -> 'LanguageReference':
        """
        Gets the default_language of this WorktypeVersion.
        The default language for Workitems created from the Worktype.

        :return: The default_language of this WorktypeVersion.
        :rtype: LanguageReference
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language: 'LanguageReference') -> None:
        """
        Sets the default_language of this WorktypeVersion.
        The default language for Workitems created from the Worktype.

        :param default_language: The default_language of this WorktypeVersion.
        :type: LanguageReference
        """
        

        self._default_language = default_language

    @property
    def default_ttl_seconds(self) -> int:
        """
        Gets the default_ttl_seconds of this WorktypeVersion.
        The default time to time to live in seconds for Workitems created from the Worktype.

        :return: The default_ttl_seconds of this WorktypeVersion.
        :rtype: int
        """
        return self._default_ttl_seconds

    @default_ttl_seconds.setter
    def default_ttl_seconds(self, default_ttl_seconds: int) -> None:
        """
        Sets the default_ttl_seconds of this WorktypeVersion.
        The default time to time to live in seconds for Workitems created from the Worktype.

        :param default_ttl_seconds: The default_ttl_seconds of this WorktypeVersion.
        :type: int
        """
        

        self._default_ttl_seconds = default_ttl_seconds

    @property
    def modified_by(self) -> 'UserReference':
        """
        Gets the modified_by of this WorktypeVersion.
        The id of the User who modified the Worktype.

        :return: The modified_by of this WorktypeVersion.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'UserReference') -> None:
        """
        Sets the modified_by of this WorktypeVersion.
        The id of the User who modified the Worktype.

        :param modified_by: The modified_by of this WorktypeVersion.
        :type: UserReference
        """
        

        self._modified_by = modified_by

    @property
    def default_queue(self) -> 'WorkitemQueueReference':
        """
        Gets the default_queue of this WorktypeVersion.
        The default queue for Workitems created from the Worktype.

        :return: The default_queue of this WorktypeVersion.
        :rtype: WorkitemQueueReference
        """
        return self._default_queue

    @default_queue.setter
    def default_queue(self, default_queue: 'WorkitemQueueReference') -> None:
        """
        Sets the default_queue of this WorktypeVersion.
        The default queue for Workitems created from the Worktype.

        :param default_queue: The default_queue of this WorktypeVersion.
        :type: WorkitemQueueReference
        """
        

        self._default_queue = default_queue

    @property
    def default_skills(self) -> List['RoutingSkillReference']:
        """
        Gets the default_skills of this WorktypeVersion.
        The default skills for Workitems created from the Worktype.

        :return: The default_skills of this WorktypeVersion.
        :rtype: list[RoutingSkillReference]
        """
        return self._default_skills

    @default_skills.setter
    def default_skills(self, default_skills: List['RoutingSkillReference']) -> None:
        """
        Sets the default_skills of this WorktypeVersion.
        The default skills for Workitems created from the Worktype.

        :param default_skills: The default_skills of this WorktypeVersion.
        :type: list[RoutingSkillReference]
        """
        

        self._default_skills = default_skills

    @property
    def assignment_enabled(self) -> bool:
        """
        Gets the assignment_enabled of this WorktypeVersion.
        When set to true, Workitems will be sent to the queue of the Worktype as they are created. Default value is false.

        :return: The assignment_enabled of this WorktypeVersion.
        :rtype: bool
        """
        return self._assignment_enabled

    @assignment_enabled.setter
    def assignment_enabled(self, assignment_enabled: bool) -> None:
        """
        Sets the assignment_enabled of this WorktypeVersion.
        When set to true, Workitems will be sent to the queue of the Worktype as they are created. Default value is false.

        :param assignment_enabled: The assignment_enabled of this WorktypeVersion.
        :type: bool
        """
        

        self._assignment_enabled = assignment_enabled

    @property
    def schema(self) -> 'WorkitemSchema':
        """
        Gets the schema of this WorktypeVersion.
        The schema defining the custom attributes for Workitems created from the Worktype.

        :return: The schema of this WorktypeVersion.
        :rtype: WorkitemSchema
        """
        return self._schema

    @schema.setter
    def schema(self, schema: 'WorkitemSchema') -> None:
        """
        Sets the schema of this WorktypeVersion.
        The schema defining the custom attributes for Workitems created from the Worktype.

        :param schema: The schema of this WorktypeVersion.
        :type: WorkitemSchema
        """
        

        self._schema = schema

    @property
    def service_level_target(self) -> int:
        """
        Gets the service_level_target of this WorktypeVersion.
        The target service level for Workitems created from the Worktype. The default value is 100.

        :return: The service_level_target of this WorktypeVersion.
        :rtype: int
        """
        return self._service_level_target

    @service_level_target.setter
    def service_level_target(self, service_level_target: int) -> None:
        """
        Sets the service_level_target of this WorktypeVersion.
        The target service level for Workitems created from the Worktype. The default value is 100.

        :param service_level_target: The service_level_target of this WorktypeVersion.
        :type: int
        """
        

        self._service_level_target = service_level_target

    @property
    def version(self) -> int:
        """
        Gets the version of this WorktypeVersion.
        Version

        :return: The version of this WorktypeVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this WorktypeVersion.
        Version

        :param version: The version of this WorktypeVersion.
        :type: int
        """
        

        self._version = version

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this WorktypeVersion.
        The URI for this object

        :return: The self_uri of this WorktypeVersion.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this WorktypeVersion.
        The URI for this object

        :param self_uri: The self_uri of this WorktypeVersion.
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
