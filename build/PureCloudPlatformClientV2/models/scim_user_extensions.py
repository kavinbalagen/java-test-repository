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
    from . import ScimGenesysUserExternalId
    from . import ScimUserRoutingLanguage
    from . import ScimUserRoutingSkill

class ScimUserExtensions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ScimUserExtensions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'routing_skills': 'list[ScimUserRoutingSkill]',
            'routing_languages': 'list[ScimUserRoutingLanguage]',
            'external_ids': 'list[ScimGenesysUserExternalId]'
        }

        self.attribute_map = {
            'routing_skills': 'routingSkills',
            'routing_languages': 'routingLanguages',
            'external_ids': 'externalIds'
        }

        self._routing_skills = None
        self._routing_languages = None
        self._external_ids = None

    @property
    def routing_skills(self) -> List['ScimUserRoutingSkill']:
        """
        Gets the routing_skills of this ScimUserExtensions.
        The list of routing skills assigned to a user. Maximum 50 skills.

        :return: The routing_skills of this ScimUserExtensions.
        :rtype: list[ScimUserRoutingSkill]
        """
        return self._routing_skills

    @routing_skills.setter
    def routing_skills(self, routing_skills: List['ScimUserRoutingSkill']) -> None:
        """
        Sets the routing_skills of this ScimUserExtensions.
        The list of routing skills assigned to a user. Maximum 50 skills.

        :param routing_skills: The routing_skills of this ScimUserExtensions.
        :type: list[ScimUserRoutingSkill]
        """
        

        self._routing_skills = routing_skills

    @property
    def routing_languages(self) -> List['ScimUserRoutingLanguage']:
        """
        Gets the routing_languages of this ScimUserExtensions.
        The list of routing languages assigned to a user. Maximum 50 languages.

        :return: The routing_languages of this ScimUserExtensions.
        :rtype: list[ScimUserRoutingLanguage]
        """
        return self._routing_languages

    @routing_languages.setter
    def routing_languages(self, routing_languages: List['ScimUserRoutingLanguage']) -> None:
        """
        Sets the routing_languages of this ScimUserExtensions.
        The list of routing languages assigned to a user. Maximum 50 languages.

        :param routing_languages: The routing_languages of this ScimUserExtensions.
        :type: list[ScimUserRoutingLanguage]
        """
        

        self._routing_languages = routing_languages

    @property
    def external_ids(self) -> List['ScimGenesysUserExternalId']:
        """
        Gets the external_ids of this ScimUserExtensions.
        The list of external identifiers assigned to user. Always includes an immutable SCIM authority prefixed with \"x-pc:scimv2:v1\". ExternalIds are searchable with complex filter query parameter using 'authority' and 'value', e.g., filter=urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds[authority eq \"matchAuthName\" and value eq \"matchingExternalKeyValue\"].

        :return: The external_ids of this ScimUserExtensions.
        :rtype: list[ScimGenesysUserExternalId]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids: List['ScimGenesysUserExternalId']) -> None:
        """
        Sets the external_ids of this ScimUserExtensions.
        The list of external identifiers assigned to user. Always includes an immutable SCIM authority prefixed with \"x-pc:scimv2:v1\". ExternalIds are searchable with complex filter query parameter using 'authority' and 'value', e.g., filter=urn:ietf:params:scim:schemas:extension:genesys:purecloud:2.0:User:externalIds[authority eq \"matchAuthName\" and value eq \"matchingExternalKeyValue\"].

        :param external_ids: The external_ids of this ScimUserExtensions.
        :type: list[ScimGenesysUserExternalId]
        """
        

        self._external_ids = external_ids

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

