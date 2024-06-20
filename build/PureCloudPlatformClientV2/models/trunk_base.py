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
    from . import DomainEntityRef

class TrunkBase(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        TrunkBase - a model defined in Swagger

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
            'trunk_metabase': 'DomainEntityRef',
            'properties': 'dict(str, object)',
            'trunk_type': 'str',
            'managed': 'bool',
            'site': 'DomainEntityRef',
            'inbound_site': 'DomainEntityRef',
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
            'trunk_metabase': 'trunkMetabase',
            'properties': 'properties',
            'trunk_type': 'trunkType',
            'managed': 'managed',
            'site': 'site',
            'inbound_site': 'inboundSite',
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
        self._trunk_metabase = None
        self._properties = None
        self._trunk_type = None
        self._managed = None
        self._site = None
        self._inbound_site = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this TrunkBase.
        The globally unique identifier for the object.

        :return: The id of this TrunkBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this TrunkBase.
        The globally unique identifier for the object.

        :param id: The id of this TrunkBase.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this TrunkBase.
        The name of the entity.

        :return: The name of this TrunkBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this TrunkBase.
        The name of the entity.

        :param name: The name of this TrunkBase.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this TrunkBase.
        The division to which this entity belongs.

        :return: The division of this TrunkBase.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this TrunkBase.
        The division to which this entity belongs.

        :param division: The division of this TrunkBase.
        :type: Division
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this TrunkBase.
        The resource's description.

        :return: The description of this TrunkBase.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this TrunkBase.
        The resource's description.

        :param description: The description of this TrunkBase.
        :type: str
        """
        

        self._description = description

    @property
    def version(self) -> int:
        """
        Gets the version of this TrunkBase.
        The current version of the resource.

        :return: The version of this TrunkBase.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this TrunkBase.
        The current version of the resource.

        :param version: The version of this TrunkBase.
        :type: int
        """
        

        self._version = version

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this TrunkBase.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this TrunkBase.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this TrunkBase.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this TrunkBase.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this TrunkBase.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this TrunkBase.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this TrunkBase.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this TrunkBase.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> str:
        """
        Gets the modified_by of this TrunkBase.
        The ID of the user that last modified the resource.

        :return: The modified_by of this TrunkBase.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: str) -> None:
        """
        Sets the modified_by of this TrunkBase.
        The ID of the user that last modified the resource.

        :param modified_by: The modified_by of this TrunkBase.
        :type: str
        """
        

        self._modified_by = modified_by

    @property
    def created_by(self) -> str:
        """
        Gets the created_by of this TrunkBase.
        The ID of the user that created the resource.

        :return: The created_by of this TrunkBase.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: str) -> None:
        """
        Sets the created_by of this TrunkBase.
        The ID of the user that created the resource.

        :param created_by: The created_by of this TrunkBase.
        :type: str
        """
        

        self._created_by = created_by

    @property
    def state(self) -> str:
        """
        Gets the state of this TrunkBase.
        Indicates if the resource is active, inactive, or deleted.

        :return: The state of this TrunkBase.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this TrunkBase.
        Indicates if the resource is active, inactive, or deleted.

        :param state: The state of this TrunkBase.
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
        Gets the modified_by_app of this TrunkBase.
        The application that last modified the resource.

        :return: The modified_by_app of this TrunkBase.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app: str) -> None:
        """
        Sets the modified_by_app of this TrunkBase.
        The application that last modified the resource.

        :param modified_by_app: The modified_by_app of this TrunkBase.
        :type: str
        """
        

        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self) -> str:
        """
        Gets the created_by_app of this TrunkBase.
        The application that created the resource.

        :return: The created_by_app of this TrunkBase.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app: str) -> None:
        """
        Sets the created_by_app of this TrunkBase.
        The application that created the resource.

        :param created_by_app: The created_by_app of this TrunkBase.
        :type: str
        """
        

        self._created_by_app = created_by_app

    @property
    def trunk_metabase(self) -> 'DomainEntityRef':
        """
        Gets the trunk_metabase of this TrunkBase.
        The meta-base this trunk is based on.

        :return: The trunk_metabase of this TrunkBase.
        :rtype: DomainEntityRef
        """
        return self._trunk_metabase

    @trunk_metabase.setter
    def trunk_metabase(self, trunk_metabase: 'DomainEntityRef') -> None:
        """
        Sets the trunk_metabase of this TrunkBase.
        The meta-base this trunk is based on.

        :param trunk_metabase: The trunk_metabase of this TrunkBase.
        :type: DomainEntityRef
        """
        

        self._trunk_metabase = trunk_metabase

    @property
    def properties(self) -> Dict[str, object]:
        """
        Gets the properties of this TrunkBase.


        :return: The properties of this TrunkBase.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, object]) -> None:
        """
        Sets the properties of this TrunkBase.


        :param properties: The properties of this TrunkBase.
        :type: dict(str, object)
        """
        

        self._properties = properties

    @property
    def trunk_type(self) -> str:
        """
        Gets the trunk_type of this TrunkBase.
        The type of this trunk base.

        :return: The trunk_type of this TrunkBase.
        :rtype: str
        """
        return self._trunk_type

    @trunk_type.setter
    def trunk_type(self, trunk_type: str) -> None:
        """
        Sets the trunk_type of this TrunkBase.
        The type of this trunk base.

        :param trunk_type: The trunk_type of this TrunkBase.
        :type: str
        """
        if isinstance(trunk_type, int):
            trunk_type = str(trunk_type)
        allowed_values = ["EXTERNAL", "PHONE", "EDGE"]
        if trunk_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for trunk_type -> " + trunk_type)
            self._trunk_type = "outdated_sdk_version"
        else:
            self._trunk_type = trunk_type

    @property
    def managed(self) -> bool:
        """
        Gets the managed of this TrunkBase.
        Is this trunk being managed remotely. This property is synchronized with the managed property of the Edge Group to which it is assigned.

        :return: The managed of this TrunkBase.
        :rtype: bool
        """
        return self._managed

    @managed.setter
    def managed(self, managed: bool) -> None:
        """
        Sets the managed of this TrunkBase.
        Is this trunk being managed remotely. This property is synchronized with the managed property of the Edge Group to which it is assigned.

        :param managed: The managed of this TrunkBase.
        :type: bool
        """
        

        self._managed = managed

    @property
    def site(self) -> 'DomainEntityRef':
        """
        Gets the site of this TrunkBase.
        Used to determine the media regions for inbound and outbound calls through a trunk. Also determines the dial plan to use for calls that came in on a trunk and have to be sent out on it as well.

        :return: The site of this TrunkBase.
        :rtype: DomainEntityRef
        """
        return self._site

    @site.setter
    def site(self, site: 'DomainEntityRef') -> None:
        """
        Sets the site of this TrunkBase.
        Used to determine the media regions for inbound and outbound calls through a trunk. Also determines the dial plan to use for calls that came in on a trunk and have to be sent out on it as well.

        :param site: The site of this TrunkBase.
        :type: DomainEntityRef
        """
        

        self._site = site

    @property
    def inbound_site(self) -> 'DomainEntityRef':
        """
        Gets the inbound_site of this TrunkBase.
        Allows a customer to set the site to which inbound calls will be routed

        :return: The inbound_site of this TrunkBase.
        :rtype: DomainEntityRef
        """
        return self._inbound_site

    @inbound_site.setter
    def inbound_site(self, inbound_site: 'DomainEntityRef') -> None:
        """
        Sets the inbound_site of this TrunkBase.
        Allows a customer to set the site to which inbound calls will be routed

        :param inbound_site: The inbound_site of this TrunkBase.
        :type: DomainEntityRef
        """
        

        self._inbound_site = inbound_site

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this TrunkBase.
        The URI for this object

        :return: The self_uri of this TrunkBase.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this TrunkBase.
        The URI for this object

        :param self_uri: The self_uri of this TrunkBase.
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

