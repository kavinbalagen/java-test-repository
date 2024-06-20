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
    from . import Endpoint
    from . import Recording

class OrphanRecording(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        OrphanRecording - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'created_time': 'datetime',
            'recovered_time': 'datetime',
            'provider_type': 'str',
            'media_size_bytes': 'int',
            'media_type': 'str',
            'media_subtype': 'str',
            'media_subject': 'str',
            'file_state': 'str',
            'provider_endpoint': 'Endpoint',
            'recording': 'Recording',
            'orphan_status': 'str',
            'source_orphaning_id': 'str',
            'region': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'created_time': 'createdTime',
            'recovered_time': 'recoveredTime',
            'provider_type': 'providerType',
            'media_size_bytes': 'mediaSizeBytes',
            'media_type': 'mediaType',
            'media_subtype': 'mediaSubtype',
            'media_subject': 'mediaSubject',
            'file_state': 'fileState',
            'provider_endpoint': 'providerEndpoint',
            'recording': 'recording',
            'orphan_status': 'orphanStatus',
            'source_orphaning_id': 'sourceOrphaningId',
            'region': 'region',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._created_time = None
        self._recovered_time = None
        self._provider_type = None
        self._media_size_bytes = None
        self._media_type = None
        self._media_subtype = None
        self._media_subject = None
        self._file_state = None
        self._provider_endpoint = None
        self._recording = None
        self._orphan_status = None
        self._source_orphaning_id = None
        self._region = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this OrphanRecording.
        The globally unique identifier for the object.

        :return: The id of this OrphanRecording.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this OrphanRecording.
        The globally unique identifier for the object.

        :param id: The id of this OrphanRecording.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this OrphanRecording.


        :return: The name of this OrphanRecording.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this OrphanRecording.


        :param name: The name of this OrphanRecording.
        :type: str
        """
        

        self._name = name

    @property
    def created_time(self) -> datetime:
        """
        Gets the created_time of this OrphanRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_time of this OrphanRecording.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time: datetime) -> None:
        """
        Sets the created_time of this OrphanRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_time: The created_time of this OrphanRecording.
        :type: datetime
        """
        

        self._created_time = created_time

    @property
    def recovered_time(self) -> datetime:
        """
        Gets the recovered_time of this OrphanRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The recovered_time of this OrphanRecording.
        :rtype: datetime
        """
        return self._recovered_time

    @recovered_time.setter
    def recovered_time(self, recovered_time: datetime) -> None:
        """
        Sets the recovered_time of this OrphanRecording.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param recovered_time: The recovered_time of this OrphanRecording.
        :type: datetime
        """
        

        self._recovered_time = recovered_time

    @property
    def provider_type(self) -> str:
        """
        Gets the provider_type of this OrphanRecording.


        :return: The provider_type of this OrphanRecording.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type: str) -> None:
        """
        Sets the provider_type of this OrphanRecording.


        :param provider_type: The provider_type of this OrphanRecording.
        :type: str
        """
        if isinstance(provider_type, int):
            provider_type = str(provider_type)
        allowed_values = ["EDGE", "CHAT", "EMAIL", "SCREEN_RECORDING", "PUREENGAGE", "PURECONNECT"]
        if provider_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for provider_type -> " + provider_type)
            self._provider_type = "outdated_sdk_version"
        else:
            self._provider_type = provider_type

    @property
    def media_size_bytes(self) -> int:
        """
        Gets the media_size_bytes of this OrphanRecording.


        :return: The media_size_bytes of this OrphanRecording.
        :rtype: int
        """
        return self._media_size_bytes

    @media_size_bytes.setter
    def media_size_bytes(self, media_size_bytes: int) -> None:
        """
        Sets the media_size_bytes of this OrphanRecording.


        :param media_size_bytes: The media_size_bytes of this OrphanRecording.
        :type: int
        """
        

        self._media_size_bytes = media_size_bytes

    @property
    def media_type(self) -> str:
        """
        Gets the media_type of this OrphanRecording.


        :return: The media_type of this OrphanRecording.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type: str) -> None:
        """
        Sets the media_type of this OrphanRecording.


        :param media_type: The media_type of this OrphanRecording.
        :type: str
        """
        if isinstance(media_type, int):
            media_type = str(media_type)
        allowed_values = ["CALL", "CHAT", "EMAIL", "SCREEN"]
        if media_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_type -> " + media_type)
            self._media_type = "outdated_sdk_version"
        else:
            self._media_type = media_type

    @property
    def media_subtype(self) -> str:
        """
        Gets the media_subtype of this OrphanRecording.


        :return: The media_subtype of this OrphanRecording.
        :rtype: str
        """
        return self._media_subtype

    @media_subtype.setter
    def media_subtype(self, media_subtype: str) -> None:
        """
        Sets the media_subtype of this OrphanRecording.


        :param media_subtype: The media_subtype of this OrphanRecording.
        :type: str
        """
        if isinstance(media_subtype, int):
            media_subtype = str(media_subtype)
        allowed_values = ["Trunk", "Station", "Consult", "Screen"]
        if media_subtype.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for media_subtype -> " + media_subtype)
            self._media_subtype = "outdated_sdk_version"
        else:
            self._media_subtype = media_subtype

    @property
    def media_subject(self) -> str:
        """
        Gets the media_subject of this OrphanRecording.


        :return: The media_subject of this OrphanRecording.
        :rtype: str
        """
        return self._media_subject

    @media_subject.setter
    def media_subject(self, media_subject: str) -> None:
        """
        Sets the media_subject of this OrphanRecording.


        :param media_subject: The media_subject of this OrphanRecording.
        :type: str
        """
        

        self._media_subject = media_subject

    @property
    def file_state(self) -> str:
        """
        Gets the file_state of this OrphanRecording.


        :return: The file_state of this OrphanRecording.
        :rtype: str
        """
        return self._file_state

    @file_state.setter
    def file_state(self, file_state: str) -> None:
        """
        Sets the file_state of this OrphanRecording.


        :param file_state: The file_state of this OrphanRecording.
        :type: str
        """
        if isinstance(file_state, int):
            file_state = str(file_state)
        allowed_values = ["ARCHIVED", "AVAILABLE", "DELETED", "RESTORED", "RESTORING", "UPLOADING"]
        if file_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for file_state -> " + file_state)
            self._file_state = "outdated_sdk_version"
        else:
            self._file_state = file_state

    @property
    def provider_endpoint(self) -> 'Endpoint':
        """
        Gets the provider_endpoint of this OrphanRecording.


        :return: The provider_endpoint of this OrphanRecording.
        :rtype: Endpoint
        """
        return self._provider_endpoint

    @provider_endpoint.setter
    def provider_endpoint(self, provider_endpoint: 'Endpoint') -> None:
        """
        Sets the provider_endpoint of this OrphanRecording.


        :param provider_endpoint: The provider_endpoint of this OrphanRecording.
        :type: Endpoint
        """
        

        self._provider_endpoint = provider_endpoint

    @property
    def recording(self) -> 'Recording':
        """
        Gets the recording of this OrphanRecording.


        :return: The recording of this OrphanRecording.
        :rtype: Recording
        """
        return self._recording

    @recording.setter
    def recording(self, recording: 'Recording') -> None:
        """
        Sets the recording of this OrphanRecording.


        :param recording: The recording of this OrphanRecording.
        :type: Recording
        """
        

        self._recording = recording

    @property
    def orphan_status(self) -> str:
        """
        Gets the orphan_status of this OrphanRecording.
        The status of the orphaned recording's conversation.

        :return: The orphan_status of this OrphanRecording.
        :rtype: str
        """
        return self._orphan_status

    @orphan_status.setter
    def orphan_status(self, orphan_status: str) -> None:
        """
        Sets the orphan_status of this OrphanRecording.
        The status of the orphaned recording's conversation.

        :param orphan_status: The orphan_status of this OrphanRecording.
        :type: str
        """
        if isinstance(orphan_status, int):
            orphan_status = str(orphan_status)
        allowed_values = ["NO_CONVERSATION", "UNKNOWN_CONVERSATION", "CONVERSATION_NOT_COMPLETE", "CONVERSATION_NOT_EVALUATED", "EVALUATED"]
        if orphan_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for orphan_status -> " + orphan_status)
            self._orphan_status = "outdated_sdk_version"
        else:
            self._orphan_status = orphan_status

    @property
    def source_orphaning_id(self) -> str:
        """
        Gets the source_orphaning_id of this OrphanRecording.
        An identifier used during recovery operations by the supplying hybrid platform to track back and determine which interaction this recording is associated with

        :return: The source_orphaning_id of this OrphanRecording.
        :rtype: str
        """
        return self._source_orphaning_id

    @source_orphaning_id.setter
    def source_orphaning_id(self, source_orphaning_id: str) -> None:
        """
        Sets the source_orphaning_id of this OrphanRecording.
        An identifier used during recovery operations by the supplying hybrid platform to track back and determine which interaction this recording is associated with

        :param source_orphaning_id: The source_orphaning_id of this OrphanRecording.
        :type: str
        """
        

        self._source_orphaning_id = source_orphaning_id

    @property
    def region(self) -> str:
        """
        Gets the region of this OrphanRecording.


        :return: The region of this OrphanRecording.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region: str) -> None:
        """
        Sets the region of this OrphanRecording.


        :param region: The region of this OrphanRecording.
        :type: str
        """
        if isinstance(region, int):
            region = str(region)
        allowed_values = ["af-south-1", "ap-east-1", "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-south-1", "ap-southeast-1", "ap-southeast-2", "ap-southeast-3", "ca-central-1", "eu-central-1", "eu-central-2", "eu-west-1", "eu-west-2", "eu-west-3", "me-central-1", "sa-east-1", "us-east-1", "us-west-2"]
        if region.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for region -> " + region)
            self._region = "outdated_sdk_version"
        else:
            self._region = region

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this OrphanRecording.
        The URI for this object

        :return: The self_uri of this OrphanRecording.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this OrphanRecording.
        The URI for this object

        :param self_uri: The self_uri of this OrphanRecording.
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
