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
    from . import OrgUser
    from . import Organization
    from . import TrusteeAuthorization

class Trustor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Trustor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'enabled': 'bool',
            'date_created': 'datetime',
            'created_by': 'OrgUser',
            'organization': 'Organization',
            'authorization': 'TrusteeAuthorization',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'enabled': 'enabled',
            'date_created': 'dateCreated',
            'created_by': 'createdBy',
            'organization': 'organization',
            'authorization': 'authorization',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._enabled = None
        self._date_created = None
        self._created_by = None
        self._organization = None
        self._authorization = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Trustor.
        Organization Id for this trust.

        :return: The id of this Trustor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Trustor.
        Organization Id for this trust.

        :param id: The id of this Trustor.
        :type: str
        """
        

        self._id = id

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this Trustor.
        If disabled no trustee user will have access, even if they were previously added.

        :return: The enabled of this Trustor.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this Trustor.
        If disabled no trustee user will have access, even if they were previously added.

        :param enabled: The enabled of this Trustor.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Trustor.
        Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Trustor.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Trustor.
        Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Trustor.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def created_by(self) -> 'OrgUser':
        """
        Gets the created_by of this Trustor.
        User that created trust.

        :return: The created_by of this Trustor.
        :rtype: OrgUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'OrgUser') -> None:
        """
        Sets the created_by of this Trustor.
        User that created trust.

        :param created_by: The created_by of this Trustor.
        :type: OrgUser
        """
        

        self._created_by = created_by

    @property
    def organization(self) -> 'Organization':
        """
        Gets the organization of this Trustor.
        Organization associated with this trust.

        :return: The organization of this Trustor.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization: 'Organization') -> None:
        """
        Sets the organization of this Trustor.
        Organization associated with this trust.

        :param organization: The organization of this Trustor.
        :type: Organization
        """
        

        self._organization = organization

    @property
    def authorization(self) -> 'TrusteeAuthorization':
        """
        Gets the authorization of this Trustor.
        Authorization for the trustee user has in this trustor organization

        :return: The authorization of this Trustor.
        :rtype: TrusteeAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization: 'TrusteeAuthorization') -> None:
        """
        Sets the authorization of this Trustor.
        Authorization for the trustee user has in this trustor organization

        :param authorization: The authorization of this Trustor.
        :type: TrusteeAuthorization
        """
        

        self._authorization = authorization

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Trustor.
        The URI for this object

        :return: The self_uri of this Trustor.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Trustor.
        The URI for this object

        :param self_uri: The self_uri of this Trustor.
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

