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
    from . import JsonSchemaDocument
    from . import NluInfo
    from . import SupportedLanguage
    from . import User

class FlowVersion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FlowVersion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'commit_version': 'str',
            'configuration_version': 'str',
            'type': 'str',
            'secure': 'bool',
            'debug': 'bool',
            'created_by': 'User',
            'created_by_client': 'DomainEntityRef',
            'configuration_uri': 'str',
            'date_created': 'int',
            'date_checked_in': 'int',
            'date_saved': 'int',
            'generation_id': 'str',
            'publish_result_uri': 'str',
            'input_schema': 'JsonSchemaDocument',
            'output_schema': 'JsonSchemaDocument',
            'date_published': 'datetime',
            'date_published_end': 'datetime',
            'nlu_info': 'NluInfo',
            'supported_languages': 'list[SupportedLanguage]',
            'compatible_flow_types': 'list[str]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'commit_version': 'commitVersion',
            'configuration_version': 'configurationVersion',
            'type': 'type',
            'secure': 'secure',
            'debug': 'debug',
            'created_by': 'createdBy',
            'created_by_client': 'createdByClient',
            'configuration_uri': 'configurationUri',
            'date_created': 'dateCreated',
            'date_checked_in': 'dateCheckedIn',
            'date_saved': 'dateSaved',
            'generation_id': 'generationId',
            'publish_result_uri': 'publishResultUri',
            'input_schema': 'inputSchema',
            'output_schema': 'outputSchema',
            'date_published': 'datePublished',
            'date_published_end': 'datePublishedEnd',
            'nlu_info': 'nluInfo',
            'supported_languages': 'supportedLanguages',
            'compatible_flow_types': 'compatibleFlowTypes',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._commit_version = None
        self._configuration_version = None
        self._type = None
        self._secure = None
        self._debug = None
        self._created_by = None
        self._created_by_client = None
        self._configuration_uri = None
        self._date_created = None
        self._date_checked_in = None
        self._date_saved = None
        self._generation_id = None
        self._publish_result_uri = None
        self._input_schema = None
        self._output_schema = None
        self._date_published = None
        self._date_published_end = None
        self._nlu_info = None
        self._supported_languages = None
        self._compatible_flow_types = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this FlowVersion.
        The flow version identifier

        :return: The id of this FlowVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this FlowVersion.
        The flow version identifier

        :param id: The id of this FlowVersion.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this FlowVersion.


        :return: The name of this FlowVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this FlowVersion.


        :param name: The name of this FlowVersion.
        :type: str
        """
        

        self._name = name

    @property
    def commit_version(self) -> str:
        """
        Gets the commit_version of this FlowVersion.


        :return: The commit_version of this FlowVersion.
        :rtype: str
        """
        return self._commit_version

    @commit_version.setter
    def commit_version(self, commit_version: str) -> None:
        """
        Sets the commit_version of this FlowVersion.


        :param commit_version: The commit_version of this FlowVersion.
        :type: str
        """
        

        self._commit_version = commit_version

    @property
    def configuration_version(self) -> str:
        """
        Gets the configuration_version of this FlowVersion.


        :return: The configuration_version of this FlowVersion.
        :rtype: str
        """
        return self._configuration_version

    @configuration_version.setter
    def configuration_version(self, configuration_version: str) -> None:
        """
        Sets the configuration_version of this FlowVersion.


        :param configuration_version: The configuration_version of this FlowVersion.
        :type: str
        """
        

        self._configuration_version = configuration_version

    @property
    def type(self) -> str:
        """
        Gets the type of this FlowVersion.


        :return: The type of this FlowVersion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this FlowVersion.


        :param type: The type of this FlowVersion.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["PUBLISH", "CHECKIN", "SAVE"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def secure(self) -> bool:
        """
        Gets the secure of this FlowVersion.


        :return: The secure of this FlowVersion.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure: bool) -> None:
        """
        Sets the secure of this FlowVersion.


        :param secure: The secure of this FlowVersion.
        :type: bool
        """
        

        self._secure = secure

    @property
    def debug(self) -> bool:
        """
        Gets the debug of this FlowVersion.


        :return: The debug of this FlowVersion.
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug: bool) -> None:
        """
        Sets the debug of this FlowVersion.


        :param debug: The debug of this FlowVersion.
        :type: bool
        """
        

        self._debug = debug

    @property
    def created_by(self) -> 'User':
        """
        Gets the created_by of this FlowVersion.


        :return: The created_by of this FlowVersion.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'User') -> None:
        """
        Sets the created_by of this FlowVersion.


        :param created_by: The created_by of this FlowVersion.
        :type: User
        """
        

        self._created_by = created_by

    @property
    def created_by_client(self) -> 'DomainEntityRef':
        """
        Gets the created_by_client of this FlowVersion.


        :return: The created_by_client of this FlowVersion.
        :rtype: DomainEntityRef
        """
        return self._created_by_client

    @created_by_client.setter
    def created_by_client(self, created_by_client: 'DomainEntityRef') -> None:
        """
        Sets the created_by_client of this FlowVersion.


        :param created_by_client: The created_by_client of this FlowVersion.
        :type: DomainEntityRef
        """
        

        self._created_by_client = created_by_client

    @property
    def configuration_uri(self) -> str:
        """
        Gets the configuration_uri of this FlowVersion.


        :return: The configuration_uri of this FlowVersion.
        :rtype: str
        """
        return self._configuration_uri

    @configuration_uri.setter
    def configuration_uri(self, configuration_uri: str) -> None:
        """
        Sets the configuration_uri of this FlowVersion.


        :param configuration_uri: The configuration_uri of this FlowVersion.
        :type: str
        """
        

        self._configuration_uri = configuration_uri

    @property
    def date_created(self) -> int:
        """
        Gets the date_created of this FlowVersion.


        :return: The date_created of this FlowVersion.
        :rtype: int
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: int) -> None:
        """
        Sets the date_created of this FlowVersion.


        :param date_created: The date_created of this FlowVersion.
        :type: int
        """
        

        self._date_created = date_created

    @property
    def date_checked_in(self) -> int:
        """
        Gets the date_checked_in of this FlowVersion.


        :return: The date_checked_in of this FlowVersion.
        :rtype: int
        """
        return self._date_checked_in

    @date_checked_in.setter
    def date_checked_in(self, date_checked_in: int) -> None:
        """
        Sets the date_checked_in of this FlowVersion.


        :param date_checked_in: The date_checked_in of this FlowVersion.
        :type: int
        """
        

        self._date_checked_in = date_checked_in

    @property
    def date_saved(self) -> int:
        """
        Gets the date_saved of this FlowVersion.


        :return: The date_saved of this FlowVersion.
        :rtype: int
        """
        return self._date_saved

    @date_saved.setter
    def date_saved(self, date_saved: int) -> None:
        """
        Sets the date_saved of this FlowVersion.


        :param date_saved: The date_saved of this FlowVersion.
        :type: int
        """
        

        self._date_saved = date_saved

    @property
    def generation_id(self) -> str:
        """
        Gets the generation_id of this FlowVersion.


        :return: The generation_id of this FlowVersion.
        :rtype: str
        """
        return self._generation_id

    @generation_id.setter
    def generation_id(self, generation_id: str) -> None:
        """
        Sets the generation_id of this FlowVersion.


        :param generation_id: The generation_id of this FlowVersion.
        :type: str
        """
        

        self._generation_id = generation_id

    @property
    def publish_result_uri(self) -> str:
        """
        Gets the publish_result_uri of this FlowVersion.


        :return: The publish_result_uri of this FlowVersion.
        :rtype: str
        """
        return self._publish_result_uri

    @publish_result_uri.setter
    def publish_result_uri(self, publish_result_uri: str) -> None:
        """
        Sets the publish_result_uri of this FlowVersion.


        :param publish_result_uri: The publish_result_uri of this FlowVersion.
        :type: str
        """
        

        self._publish_result_uri = publish_result_uri

    @property
    def input_schema(self) -> 'JsonSchemaDocument':
        """
        Gets the input_schema of this FlowVersion.


        :return: The input_schema of this FlowVersion.
        :rtype: JsonSchemaDocument
        """
        return self._input_schema

    @input_schema.setter
    def input_schema(self, input_schema: 'JsonSchemaDocument') -> None:
        """
        Sets the input_schema of this FlowVersion.


        :param input_schema: The input_schema of this FlowVersion.
        :type: JsonSchemaDocument
        """
        

        self._input_schema = input_schema

    @property
    def output_schema(self) -> 'JsonSchemaDocument':
        """
        Gets the output_schema of this FlowVersion.


        :return: The output_schema of this FlowVersion.
        :rtype: JsonSchemaDocument
        """
        return self._output_schema

    @output_schema.setter
    def output_schema(self, output_schema: 'JsonSchemaDocument') -> None:
        """
        Sets the output_schema of this FlowVersion.


        :param output_schema: The output_schema of this FlowVersion.
        :type: JsonSchemaDocument
        """
        

        self._output_schema = output_schema

    @property
    def date_published(self) -> datetime:
        """
        Gets the date_published of this FlowVersion.
        The date this version became the published version of the flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_published of this FlowVersion.
        :rtype: datetime
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published: datetime) -> None:
        """
        Sets the date_published of this FlowVersion.
        The date this version became the published version of the flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_published: The date_published of this FlowVersion.
        :type: datetime
        """
        

        self._date_published = date_published

    @property
    def date_published_end(self) -> datetime:
        """
        Gets the date_published_end of this FlowVersion.
        The date this version was no longer the published version of the flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_published_end of this FlowVersion.
        :rtype: datetime
        """
        return self._date_published_end

    @date_published_end.setter
    def date_published_end(self, date_published_end: datetime) -> None:
        """
        Sets the date_published_end of this FlowVersion.
        The date this version was no longer the published version of the flow. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_published_end: The date_published_end of this FlowVersion.
        :type: datetime
        """
        

        self._date_published_end = date_published_end

    @property
    def nlu_info(self) -> 'NluInfo':
        """
        Gets the nlu_info of this FlowVersion.
        Information about the natural language understanding configuration for the flow version

        :return: The nlu_info of this FlowVersion.
        :rtype: NluInfo
        """
        return self._nlu_info

    @nlu_info.setter
    def nlu_info(self, nlu_info: 'NluInfo') -> None:
        """
        Sets the nlu_info of this FlowVersion.
        Information about the natural language understanding configuration for the flow version

        :param nlu_info: The nlu_info of this FlowVersion.
        :type: NluInfo
        """
        

        self._nlu_info = nlu_info

    @property
    def supported_languages(self) -> List['SupportedLanguage']:
        """
        Gets the supported_languages of this FlowVersion.
        List of supported languages for this version of the flow

        :return: The supported_languages of this FlowVersion.
        :rtype: list[SupportedLanguage]
        """
        return self._supported_languages

    @supported_languages.setter
    def supported_languages(self, supported_languages: List['SupportedLanguage']) -> None:
        """
        Sets the supported_languages of this FlowVersion.
        List of supported languages for this version of the flow

        :param supported_languages: The supported_languages of this FlowVersion.
        :type: list[SupportedLanguage]
        """
        

        self._supported_languages = supported_languages

    @property
    def compatible_flow_types(self) -> List[str]:
        """
        Gets the compatible_flow_types of this FlowVersion.
        Compatible flow types designate which flow types are allowed to embed a flow’s configuration within their own flow configuration.  Currently the only flows that can be embedded are Common Module flows and the embedding flow can invoke them using the Call Common Module action.

        :return: The compatible_flow_types of this FlowVersion.
        :rtype: list[str]
        """
        return self._compatible_flow_types

    @compatible_flow_types.setter
    def compatible_flow_types(self, compatible_flow_types: List[str]) -> None:
        """
        Sets the compatible_flow_types of this FlowVersion.
        Compatible flow types designate which flow types are allowed to embed a flow’s configuration within their own flow configuration.  Currently the only flows that can be embedded are Common Module flows and the embedding flow can invoke them using the Call Common Module action.

        :param compatible_flow_types: The compatible_flow_types of this FlowVersion.
        :type: list[str]
        """
        

        self._compatible_flow_types = compatible_flow_types

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this FlowVersion.
        The URI for this object

        :return: The self_uri of this FlowVersion.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this FlowVersion.
        The URI for this object

        :param self_uri: The self_uri of this FlowVersion.
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

