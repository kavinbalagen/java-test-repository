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

class EdgeLogsJobFile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EdgeLogsJobFile - a model defined in Swagger

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
            'version': 'int',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'modified_by': 'str',
            'created_by': 'str',
            'state': 'str',
            'modified_by_app': 'str',
            'created_by_app': 'str',
            'time_created': 'datetime',
            'time_modified': 'datetime',
            'size_bytes': 'float',
            'upload_status': 'str',
            'edge_path': 'str',
            'download_id': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'division': 'division',
            'description': 'description',
            'version': 'version',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'created_by': 'createdBy',
            'state': 'state',
            'modified_by_app': 'modifiedByApp',
            'created_by_app': 'createdByApp',
            'time_created': 'timeCreated',
            'time_modified': 'timeModified',
            'size_bytes': 'sizeBytes',
            'upload_status': 'uploadStatus',
            'edge_path': 'edgePath',
            'download_id': 'downloadId',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._division = None
        self._description = None
        self._version = None
        self._date_created = None
        self._date_modified = None
        self._modified_by = None
        self._created_by = None
        self._state = None
        self._modified_by_app = None
        self._created_by_app = None
        self._time_created = None
        self._time_modified = None
        self._size_bytes = None
        self._upload_status = None
        self._edge_path = None
        self._download_id = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this EdgeLogsJobFile.
        The globally unique identifier for the object.

        :return: The id of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this EdgeLogsJobFile.
        The globally unique identifier for the object.

        :param id: The id of this EdgeLogsJobFile.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this EdgeLogsJobFile.
        The name of the entity.

        :return: The name of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this EdgeLogsJobFile.
        The name of the entity.

        :param name: The name of this EdgeLogsJobFile.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this EdgeLogsJobFile.
        The division to which this entity belongs.

        :return: The division of this EdgeLogsJobFile.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this EdgeLogsJobFile.
        The division to which this entity belongs.

        :param division: The division of this EdgeLogsJobFile.
        :type: Division
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this EdgeLogsJobFile.
        The resource's description.

        :return: The description of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this EdgeLogsJobFile.
        The resource's description.

        :param description: The description of this EdgeLogsJobFile.
        :type: str
        """
        

        self._description = description

    @property
    def version(self) -> int:
        """
        Gets the version of this EdgeLogsJobFile.
        The current version of the resource.

        :return: The version of this EdgeLogsJobFile.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this EdgeLogsJobFile.
        The current version of the resource.

        :param version: The version of this EdgeLogsJobFile.
        :type: int
        """
        

        self._version = version

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this EdgeLogsJobFile.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this EdgeLogsJobFile.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this EdgeLogsJobFile.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this EdgeLogsJobFile.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this EdgeLogsJobFile.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this EdgeLogsJobFile.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this EdgeLogsJobFile.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this EdgeLogsJobFile.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> str:
        """
        Gets the modified_by of this EdgeLogsJobFile.
        The ID of the user that last modified the resource.

        :return: The modified_by of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: str) -> None:
        """
        Sets the modified_by of this EdgeLogsJobFile.
        The ID of the user that last modified the resource.

        :param modified_by: The modified_by of this EdgeLogsJobFile.
        :type: str
        """
        

        self._modified_by = modified_by

    @property
    def created_by(self) -> str:
        """
        Gets the created_by of this EdgeLogsJobFile.
        The ID of the user that created the resource.

        :return: The created_by of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: str) -> None:
        """
        Sets the created_by of this EdgeLogsJobFile.
        The ID of the user that created the resource.

        :param created_by: The created_by of this EdgeLogsJobFile.
        :type: str
        """
        

        self._created_by = created_by

    @property
    def state(self) -> str:
        """
        Gets the state of this EdgeLogsJobFile.
        Indicates if the resource is active, inactive, or deleted.

        :return: The state of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this EdgeLogsJobFile.
        Indicates if the resource is active, inactive, or deleted.

        :param state: The state of this EdgeLogsJobFile.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def modified_by_app(self) -> str:
        """
        Gets the modified_by_app of this EdgeLogsJobFile.
        The application that last modified the resource.

        :return: The modified_by_app of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app: str) -> None:
        """
        Sets the modified_by_app of this EdgeLogsJobFile.
        The application that last modified the resource.

        :param modified_by_app: The modified_by_app of this EdgeLogsJobFile.
        :type: str
        """
        

        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self) -> str:
        """
        Gets the created_by_app of this EdgeLogsJobFile.
        The application that created the resource.

        :return: The created_by_app of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app: str) -> None:
        """
        Sets the created_by_app of this EdgeLogsJobFile.
        The application that created the resource.

        :param created_by_app: The created_by_app of this EdgeLogsJobFile.
        :type: str
        """
        

        self._created_by_app = created_by_app

    @property
    def time_created(self) -> datetime:
        """
        Gets the time_created of this EdgeLogsJobFile.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The time_created of this EdgeLogsJobFile.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created: datetime) -> None:
        """
        Sets the time_created of this EdgeLogsJobFile.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param time_created: The time_created of this EdgeLogsJobFile.
        :type: datetime
        """
        

        self._time_created = time_created

    @property
    def time_modified(self) -> datetime:
        """
        Gets the time_modified of this EdgeLogsJobFile.
        The time this log file was last modified on the Edge. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The time_modified of this EdgeLogsJobFile.
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified: datetime) -> None:
        """
        Sets the time_modified of this EdgeLogsJobFile.
        The time this log file was last modified on the Edge. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param time_modified: The time_modified of this EdgeLogsJobFile.
        :type: datetime
        """
        

        self._time_modified = time_modified

    @property
    def size_bytes(self) -> float:
        """
        Gets the size_bytes of this EdgeLogsJobFile.
        The size of this file in bytes.

        :return: The size_bytes of this EdgeLogsJobFile.
        :rtype: float
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes: float) -> None:
        """
        Sets the size_bytes of this EdgeLogsJobFile.
        The size of this file in bytes.

        :param size_bytes: The size_bytes of this EdgeLogsJobFile.
        :type: float
        """
        

        self._size_bytes = size_bytes

    @property
    def upload_status(self) -> str:
        """
        Gets the upload_status of this EdgeLogsJobFile.
        The status of the upload of this file from the Edge to the cloud.  Use /upload to start an upload.

        :return: The upload_status of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status: str) -> None:
        """
        Sets the upload_status of this EdgeLogsJobFile.
        The status of the upload of this file from the Edge to the cloud.  Use /upload to start an upload.

        :param upload_status: The upload_status of this EdgeLogsJobFile.
        :type: str
        """
        if isinstance(upload_status, int):
            upload_status = str(upload_status)
        allowed_values = ["UPLOADING", "NOT_UPLOADED", "UPLOADED", "ERROR_ON_UPLOAD"]
        if upload_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for upload_status -> " + upload_status)
            self._upload_status = "outdated_sdk_version"
        else:
            self._upload_status = upload_status

    @property
    def edge_path(self) -> str:
        """
        Gets the edge_path of this EdgeLogsJobFile.
        The path of this file on the Edge.

        :return: The edge_path of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._edge_path

    @edge_path.setter
    def edge_path(self, edge_path: str) -> None:
        """
        Sets the edge_path of this EdgeLogsJobFile.
        The path of this file on the Edge.

        :param edge_path: The edge_path of this EdgeLogsJobFile.
        :type: str
        """
        

        self._edge_path = edge_path

    @property
    def download_id(self) -> str:
        """
        Gets the download_id of this EdgeLogsJobFile.
        The download ID to use with the downloads API.

        :return: The download_id of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._download_id

    @download_id.setter
    def download_id(self, download_id: str) -> None:
        """
        Sets the download_id of this EdgeLogsJobFile.
        The download ID to use with the downloads API.

        :param download_id: The download_id of this EdgeLogsJobFile.
        :type: str
        """
        

        self._download_id = download_id

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this EdgeLogsJobFile.
        The URI for this object

        :return: The self_uri of this EdgeLogsJobFile.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this EdgeLogsJobFile.
        The URI for this object

        :param self_uri: The self_uri of this EdgeLogsJobFile.
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

