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
    from . import KnowledgeBase
    from . import KnowledgeImportJobReport
    from . import KnowledgeImportJobSettings
    from . import UserReference

class KnowledgeImportJobResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        KnowledgeImportJobResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'download_url': 'str',
            'failed_entities_url': 'str',
            'upload_key': 'str',
            'file_type': 'str',
            'settings': 'KnowledgeImportJobSettings',
            'status': 'str',
            'report': 'KnowledgeImportJobReport',
            'knowledge_base': 'KnowledgeBase',
            'created_by': 'UserReference',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'skip_confirmation_step': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'download_url': 'downloadURL',
            'failed_entities_url': 'failedEntitiesURL',
            'upload_key': 'uploadKey',
            'file_type': 'fileType',
            'settings': 'settings',
            'status': 'status',
            'report': 'report',
            'knowledge_base': 'knowledgeBase',
            'created_by': 'createdBy',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'skip_confirmation_step': 'skipConfirmationStep',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._download_url = None
        self._failed_entities_url = None
        self._upload_key = None
        self._file_type = None
        self._settings = None
        self._status = None
        self._report = None
        self._knowledge_base = None
        self._created_by = None
        self._date_created = None
        self._date_modified = None
        self._skip_confirmation_step = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this KnowledgeImportJobResponse.
        Id of the import job

        :return: The id of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this KnowledgeImportJobResponse.
        Id of the import job

        :param id: The id of this KnowledgeImportJobResponse.
        :type: str
        """
        

        self._id = id

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this KnowledgeImportJobResponse.
        The URL of the location at which the caller can download the imported file.

        :return: The download_url of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this KnowledgeImportJobResponse.
        The URL of the location at which the caller can download the imported file.

        :param download_url: The download_url of this KnowledgeImportJobResponse.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def failed_entities_url(self) -> str:
        """
        Gets the failed_entities_url of this KnowledgeImportJobResponse.
        The URL of the location at which the caller can download the entities in json format that failed during the import.

        :return: The failed_entities_url of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._failed_entities_url

    @failed_entities_url.setter
    def failed_entities_url(self, failed_entities_url: str) -> None:
        """
        Sets the failed_entities_url of this KnowledgeImportJobResponse.
        The URL of the location at which the caller can download the entities in json format that failed during the import.

        :param failed_entities_url: The failed_entities_url of this KnowledgeImportJobResponse.
        :type: str
        """
        

        self._failed_entities_url = failed_entities_url

    @property
    def upload_key(self) -> str:
        """
        Gets the upload_key of this KnowledgeImportJobResponse.
        Upload key

        :return: The upload_key of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._upload_key

    @upload_key.setter
    def upload_key(self, upload_key: str) -> None:
        """
        Sets the upload_key of this KnowledgeImportJobResponse.
        Upload key

        :param upload_key: The upload_key of this KnowledgeImportJobResponse.
        :type: str
        """
        

        self._upload_key = upload_key

    @property
    def file_type(self) -> str:
        """
        Gets the file_type of this KnowledgeImportJobResponse.
        File type of the document

        :return: The file_type of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type: str) -> None:
        """
        Sets the file_type of this KnowledgeImportJobResponse.
        File type of the document

        :param file_type: The file_type of this KnowledgeImportJobResponse.
        :type: str
        """
        if isinstance(file_type, int):
            file_type = str(file_type)
        allowed_values = ["Json", "Csv", "Xlsx"]
        if file_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for file_type -> " + file_type)
            self._file_type = "outdated_sdk_version"
        else:
            self._file_type = file_type

    @property
    def settings(self) -> 'KnowledgeImportJobSettings':
        """
        Gets the settings of this KnowledgeImportJobResponse.
        Additional optional settings

        :return: The settings of this KnowledgeImportJobResponse.
        :rtype: KnowledgeImportJobSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings: 'KnowledgeImportJobSettings') -> None:
        """
        Sets the settings of this KnowledgeImportJobResponse.
        Additional optional settings

        :param settings: The settings of this KnowledgeImportJobResponse.
        :type: KnowledgeImportJobSettings
        """
        

        self._settings = settings

    @property
    def status(self) -> str:
        """
        Gets the status of this KnowledgeImportJobResponse.
        Status of the import job

        :return: The status of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this KnowledgeImportJobResponse.
        Status of the import job

        :param status: The status of this KnowledgeImportJobResponse.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Created", "ValidationInProgress", "ValidationCompleted", "ValidationFailed", "Started", "InProgress", "Completed", "PartialCompleted", "Failed", "AbortRequested", "Aborted"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def report(self) -> 'KnowledgeImportJobReport':
        """
        Gets the report of this KnowledgeImportJobResponse.
        Report of the import job

        :return: The report of this KnowledgeImportJobResponse.
        :rtype: KnowledgeImportJobReport
        """
        return self._report

    @report.setter
    def report(self, report: 'KnowledgeImportJobReport') -> None:
        """
        Sets the report of this KnowledgeImportJobResponse.
        Report of the import job

        :param report: The report of this KnowledgeImportJobResponse.
        :type: KnowledgeImportJobReport
        """
        

        self._report = report

    @property
    def knowledge_base(self) -> 'KnowledgeBase':
        """
        Gets the knowledge_base of this KnowledgeImportJobResponse.
        Knowledge base which document import does belong to

        :return: The knowledge_base of this KnowledgeImportJobResponse.
        :rtype: KnowledgeBase
        """
        return self._knowledge_base

    @knowledge_base.setter
    def knowledge_base(self, knowledge_base: 'KnowledgeBase') -> None:
        """
        Sets the knowledge_base of this KnowledgeImportJobResponse.
        Knowledge base which document import does belong to

        :param knowledge_base: The knowledge_base of this KnowledgeImportJobResponse.
        :type: KnowledgeBase
        """
        

        self._knowledge_base = knowledge_base

    @property
    def created_by(self) -> 'UserReference':
        """
        Gets the created_by of this KnowledgeImportJobResponse.
        The user who created the operation

        :return: The created_by of this KnowledgeImportJobResponse.
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'UserReference') -> None:
        """
        Sets the created_by of this KnowledgeImportJobResponse.
        The user who created the operation

        :param created_by: The created_by of this KnowledgeImportJobResponse.
        :type: UserReference
        """
        

        self._created_by = created_by

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this KnowledgeImportJobResponse.
        Created date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this KnowledgeImportJobResponse.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this KnowledgeImportJobResponse.
        Created date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this KnowledgeImportJobResponse.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this KnowledgeImportJobResponse.
        Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this KnowledgeImportJobResponse.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this KnowledgeImportJobResponse.
        Last modified date. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this KnowledgeImportJobResponse.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def skip_confirmation_step(self) -> bool:
        """
        Gets the skip_confirmation_step of this KnowledgeImportJobResponse.
        If enabled pre-validation step will be skipped.

        :return: The skip_confirmation_step of this KnowledgeImportJobResponse.
        :rtype: bool
        """
        return self._skip_confirmation_step

    @skip_confirmation_step.setter
    def skip_confirmation_step(self, skip_confirmation_step: bool) -> None:
        """
        Sets the skip_confirmation_step of this KnowledgeImportJobResponse.
        If enabled pre-validation step will be skipped.

        :param skip_confirmation_step: The skip_confirmation_step of this KnowledgeImportJobResponse.
        :type: bool
        """
        

        self._skip_confirmation_step = skip_confirmation_step

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this KnowledgeImportJobResponse.
        The URI for this object

        :return: The self_uri of this KnowledgeImportJobResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this KnowledgeImportJobResponse.
        The URI for this object

        :param self_uri: The self_uri of this KnowledgeImportJobResponse.
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
