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
    from . import DomainEntityRef
    from . import FlowLogLevel
    from . import UserReference

class FlowSettingsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowSettingsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'modified_by': 'UserReference',
            'modified_by_client': 'DomainEntityRef',
            'date_modified': 'datetime',
            'log_level_characteristics': 'FlowLogLevel',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'modified_by': 'modifiedBy',
            'modified_by_client': 'modifiedByClient',
            'date_modified': 'dateModified',
            'log_level_characteristics': 'logLevelCharacteristics',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._type = None
        self._modified_by = None
        self._modified_by_client = None
        self._date_modified = None
        self._log_level_characteristics = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this FlowSettingsResponse.
        The globally unique identifier for the object.

        :return: The id of this FlowSettingsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this FlowSettingsResponse.
        The globally unique identifier for the object.

        :param id: The id of this FlowSettingsResponse.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this FlowSettingsResponse.


        :return: The name of this FlowSettingsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this FlowSettingsResponse.


        :param name: The name of this FlowSettingsResponse.
        :type: str
        """
        

        self._name = name

    @property
    def type(self) -> str:
        """
        Gets the type of this FlowSettingsResponse.
        The Flow Type

        :return: The type of this FlowSettingsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this FlowSettingsResponse.
        The Flow Type

        :param type: The type of this FlowSettingsResponse.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["bot", "commonmodule", "digitalbot", "inboundcall", "inboundchat", "inboundemail", "inboundshortmessage", "inqueuecall", "inqueueshortmessage", "inqueueemail", "outboundcall", "securecall", "surveyinvite", "voice", "voicemail", "voicesurvey", "workflow", "workitem"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def modified_by(self) -> 'UserReference':
        """
        Gets the modified_by of this FlowSettingsResponse.
        User that last changed the log level setting.

        :return: The modified_by of this FlowSettingsResponse.
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'UserReference') -> None:
        """
        Sets the modified_by of this FlowSettingsResponse.
        User that last changed the log level setting.

        :param modified_by: The modified_by of this FlowSettingsResponse.
        :type: UserReference
        """
        

        self._modified_by = modified_by

    @property
    def modified_by_client(self) -> 'DomainEntityRef':
        """
        Gets the modified_by_client of this FlowSettingsResponse.
        OAuth client that last changed the log level setting.

        :return: The modified_by_client of this FlowSettingsResponse.
        :rtype: DomainEntityRef
        """
        return self._modified_by_client

    @modified_by_client.setter
    def modified_by_client(self, modified_by_client: 'DomainEntityRef') -> None:
        """
        Sets the modified_by_client of this FlowSettingsResponse.
        OAuth client that last changed the log level setting.

        :param modified_by_client: The modified_by_client of this FlowSettingsResponse.
        :type: DomainEntityRef
        """
        

        self._modified_by_client = modified_by_client

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this FlowSettingsResponse.
        The time this log level was set. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this FlowSettingsResponse.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this FlowSettingsResponse.
        The time this log level was set. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this FlowSettingsResponse.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def log_level_characteristics(self) -> 'FlowLogLevel':
        """
        Gets the log_level_characteristics of this FlowSettingsResponse.
        The log level set for this flow

        :return: The log_level_characteristics of this FlowSettingsResponse.
        :rtype: FlowLogLevel
        """
        return self._log_level_characteristics

    @log_level_characteristics.setter
    def log_level_characteristics(self, log_level_characteristics: 'FlowLogLevel') -> None:
        """
        Sets the log_level_characteristics of this FlowSettingsResponse.
        The log level set for this flow

        :param log_level_characteristics: The log_level_characteristics of this FlowSettingsResponse.
        :type: FlowLogLevel
        """
        

        self._log_level_characteristics = log_level_characteristics

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this FlowSettingsResponse.
        The URI for this object

        :return: The self_uri of this FlowSettingsResponse.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this FlowSettingsResponse.
        The URI for this object

        :param self_uri: The self_uri of this FlowSettingsResponse.
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
