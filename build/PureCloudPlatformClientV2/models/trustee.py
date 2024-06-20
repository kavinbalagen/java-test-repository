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

class Trustee(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Trustee - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'enabled': 'bool',
            'uses_default_role': 'bool',
            'date_created': 'datetime',
            'date_expired': 'datetime',
            'created_by': 'OrgUser',
            'organization': 'Organization',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'enabled': 'enabled',
            'uses_default_role': 'usesDefaultRole',
            'date_created': 'dateCreated',
            'date_expired': 'dateExpired',
            'created_by': 'createdBy',
            'organization': 'organization',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._enabled = None
        self._uses_default_role = None
        self._date_created = None
        self._date_expired = None
        self._created_by = None
        self._organization = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Trustee.
        Organization Id for this trust.

        :return: The id of this Trustee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Trustee.
        Organization Id for this trust.

        :param id: The id of this Trustee.
        :type: str
        """
        

        self._id = id

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this Trustee.
        If disabled no trustee user will have access, even if they were previously added.

        :return: The enabled of this Trustee.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this Trustee.
        If disabled no trustee user will have access, even if they were previously added.

        :param enabled: The enabled of this Trustee.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def uses_default_role(self) -> bool:
        """
        Gets the uses_default_role of this Trustee.
        Denotes if trustee uses admin role by default.

        :return: The uses_default_role of this Trustee.
        :rtype: bool
        """
        return self._uses_default_role

    @uses_default_role.setter
    def uses_default_role(self, uses_default_role: bool) -> None:
        """
        Sets the uses_default_role of this Trustee.
        Denotes if trustee uses admin role by default.

        :param uses_default_role: The uses_default_role of this Trustee.
        :type: bool
        """
        

        self._uses_default_role = uses_default_role

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Trustee.
        Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Trustee.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Trustee.
        Date Trust was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Trustee.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_expired(self) -> datetime:
        """
        Gets the date_expired of this Trustee.
        The expiration date of the trust. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_expired of this Trustee.
        :rtype: datetime
        """
        return self._date_expired

    @date_expired.setter
    def date_expired(self, date_expired: datetime) -> None:
        """
        Sets the date_expired of this Trustee.
        The expiration date of the trust. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_expired: The date_expired of this Trustee.
        :type: datetime
        """
        

        self._date_expired = date_expired

    @property
    def created_by(self) -> 'OrgUser':
        """
        Gets the created_by of this Trustee.
        User that created trust.

        :return: The created_by of this Trustee.
        :rtype: OrgUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: 'OrgUser') -> None:
        """
        Sets the created_by of this Trustee.
        User that created trust.

        :param created_by: The created_by of this Trustee.
        :type: OrgUser
        """
        

        self._created_by = created_by

    @property
    def organization(self) -> 'Organization':
        """
        Gets the organization of this Trustee.
        Organization associated with this trust.

        :return: The organization of this Trustee.
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization: 'Organization') -> None:
        """
        Sets the organization of this Trustee.
        Organization associated with this trust.

        :param organization: The organization of this Trustee.
        :type: Organization
        """
        

        self._organization = organization

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Trustee.
        The URI for this object

        :return: The self_uri of this Trustee.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Trustee.
        The URI for this object

        :param self_uri: The self_uri of this Trustee.
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
