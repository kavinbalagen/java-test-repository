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
    from . import DialogflowIntent
    from . import DialogflowProject
    from . import DomainEntityRef

class DialogflowAgent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialogflowAgent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'project': 'DialogflowProject',
            'languages': 'list[str]',
            'intents': 'list[DialogflowIntent]',
            'environments': 'list[str]',
            'integration': 'DomainEntityRef',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'project': 'project',
            'languages': 'languages',
            'intents': 'intents',
            'environments': 'environments',
            'integration': 'integration',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._project = None
        self._languages = None
        self._intents = None
        self._environments = None
        self._integration = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this DialogflowAgent.
        The globally unique identifier for the object.

        :return: The id of this DialogflowAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DialogflowAgent.
        The globally unique identifier for the object.

        :param id: The id of this DialogflowAgent.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DialogflowAgent.


        :return: The name of this DialogflowAgent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DialogflowAgent.


        :param name: The name of this DialogflowAgent.
        :type: str
        """
        

        self._name = name

    @property
    def project(self) -> 'DialogflowProject':
        """
        Gets the project of this DialogflowAgent.
        The project this Dialogflow agent belongs to

        :return: The project of this DialogflowAgent.
        :rtype: DialogflowProject
        """
        return self._project

    @project.setter
    def project(self, project: 'DialogflowProject') -> None:
        """
        Sets the project of this DialogflowAgent.
        The project this Dialogflow agent belongs to

        :param project: The project of this DialogflowAgent.
        :type: DialogflowProject
        """
        

        self._project = project

    @property
    def languages(self) -> List[str]:
        """
        Gets the languages of this DialogflowAgent.
        The supported languages of the Dialogflow agent

        :return: The languages of this DialogflowAgent.
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages: List[str]) -> None:
        """
        Sets the languages of this DialogflowAgent.
        The supported languages of the Dialogflow agent

        :param languages: The languages of this DialogflowAgent.
        :type: list[str]
        """
        

        self._languages = languages

    @property
    def intents(self) -> List['DialogflowIntent']:
        """
        Gets the intents of this DialogflowAgent.
        An array of Intents associated with this agent

        :return: The intents of this DialogflowAgent.
        :rtype: list[DialogflowIntent]
        """
        return self._intents

    @intents.setter
    def intents(self, intents: List['DialogflowIntent']) -> None:
        """
        Sets the intents of this DialogflowAgent.
        An array of Intents associated with this agent

        :param intents: The intents of this DialogflowAgent.
        :type: list[DialogflowIntent]
        """
        

        self._intents = intents

    @property
    def environments(self) -> List[str]:
        """
        Gets the environments of this DialogflowAgent.
        Available environments for this agent

        :return: The environments of this DialogflowAgent.
        :rtype: list[str]
        """
        return self._environments

    @environments.setter
    def environments(self, environments: List[str]) -> None:
        """
        Sets the environments of this DialogflowAgent.
        Available environments for this agent

        :param environments: The environments of this DialogflowAgent.
        :type: list[str]
        """
        

        self._environments = environments

    @property
    def integration(self) -> 'DomainEntityRef':
        """
        Gets the integration of this DialogflowAgent.
        The Integration this Dialogflow agent was referenced from.

        :return: The integration of this DialogflowAgent.
        :rtype: DomainEntityRef
        """
        return self._integration

    @integration.setter
    def integration(self, integration: 'DomainEntityRef') -> None:
        """
        Sets the integration of this DialogflowAgent.
        The Integration this Dialogflow agent was referenced from.

        :param integration: The integration of this DialogflowAgent.
        :type: DomainEntityRef
        """
        

        self._integration = integration

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this DialogflowAgent.
        The URI for this object

        :return: The self_uri of this DialogflowAgent.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this DialogflowAgent.
        The URI for this object

        :param self_uri: The self_uri of this DialogflowAgent.
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

