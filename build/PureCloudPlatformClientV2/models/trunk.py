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
    from . import TrunkConnectedStatus
    from . import TrunkMetricsNetworkTypeIp
    from . import TrunkMetricsOptions
    from . import TrunkMetricsRegisters

class Trunk(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Trunk - a model defined in Swagger

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
            'trunk_type': 'str',
            'edge': 'DomainEntityRef',
            'trunk_base': 'DomainEntityRef',
            'trunk_metabase': 'DomainEntityRef',
            'edge_group': 'DomainEntityRef',
            'in_service': 'bool',
            'enabled': 'bool',
            'logical_interface': 'DomainEntityRef',
            'connected_status': 'TrunkConnectedStatus',
            'options_status': 'list[TrunkMetricsOptions]',
            'registers_status': 'list[TrunkMetricsRegisters]',
            'ip_status': 'TrunkMetricsNetworkTypeIp',
            'options_enabled_status': 'str',
            'registers_enabled_status': 'str',
            'family': 'int',
            'proxy_address_list': 'list[str]',
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
            'trunk_type': 'trunkType',
            'edge': 'edge',
            'trunk_base': 'trunkBase',
            'trunk_metabase': 'trunkMetabase',
            'edge_group': 'edgeGroup',
            'in_service': 'inService',
            'enabled': 'enabled',
            'logical_interface': 'logicalInterface',
            'connected_status': 'connectedStatus',
            'options_status': 'optionsStatus',
            'registers_status': 'registersStatus',
            'ip_status': 'ipStatus',
            'options_enabled_status': 'optionsEnabledStatus',
            'registers_enabled_status': 'registersEnabledStatus',
            'family': 'family',
            'proxy_address_list': 'proxyAddressList',
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
        self._trunk_type = None
        self._edge = None
        self._trunk_base = None
        self._trunk_metabase = None
        self._edge_group = None
        self._in_service = None
        self._enabled = None
        self._logical_interface = None
        self._connected_status = None
        self._options_status = None
        self._registers_status = None
        self._ip_status = None
        self._options_enabled_status = None
        self._registers_enabled_status = None
        self._family = None
        self._proxy_address_list = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Trunk.
        The globally unique identifier for the object.

        :return: The id of this Trunk.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Trunk.
        The globally unique identifier for the object.

        :param id: The id of this Trunk.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Trunk.
        The name of the entity.

        :return: The name of this Trunk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Trunk.
        The name of the entity.

        :param name: The name of this Trunk.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this Trunk.
        The division to which this entity belongs.

        :return: The division of this Trunk.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this Trunk.
        The division to which this entity belongs.

        :param division: The division of this Trunk.
        :type: Division
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this Trunk.
        The resource's description.

        :return: The description of this Trunk.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this Trunk.
        The resource's description.

        :param description: The description of this Trunk.
        :type: str
        """
        

        self._description = description

    @property
    def version(self) -> int:
        """
        Gets the version of this Trunk.
        The current version of the resource.

        :return: The version of this Trunk.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this Trunk.
        The current version of the resource.

        :param version: The version of this Trunk.
        :type: int
        """
        

        self._version = version

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Trunk.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Trunk.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Trunk.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Trunk.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this Trunk.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Trunk.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this Trunk.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Trunk.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> str:
        """
        Gets the modified_by of this Trunk.
        The ID of the user that last modified the resource.

        :return: The modified_by of this Trunk.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: str) -> None:
        """
        Sets the modified_by of this Trunk.
        The ID of the user that last modified the resource.

        :param modified_by: The modified_by of this Trunk.
        :type: str
        """
        

        self._modified_by = modified_by

    @property
    def created_by(self) -> str:
        """
        Gets the created_by of this Trunk.
        The ID of the user that created the resource.

        :return: The created_by of this Trunk.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: str) -> None:
        """
        Sets the created_by of this Trunk.
        The ID of the user that created the resource.

        :param created_by: The created_by of this Trunk.
        :type: str
        """
        

        self._created_by = created_by

    @property
    def state(self) -> str:
        """
        Gets the state of this Trunk.
        Indicates if the resource is active, inactive, or deleted.

        :return: The state of this Trunk.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this Trunk.
        Indicates if the resource is active, inactive, or deleted.

        :param state: The state of this Trunk.
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
        Gets the modified_by_app of this Trunk.
        The application that last modified the resource.

        :return: The modified_by_app of this Trunk.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app: str) -> None:
        """
        Sets the modified_by_app of this Trunk.
        The application that last modified the resource.

        :param modified_by_app: The modified_by_app of this Trunk.
        :type: str
        """
        

        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self) -> str:
        """
        Gets the created_by_app of this Trunk.
        The application that created the resource.

        :return: The created_by_app of this Trunk.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app: str) -> None:
        """
        Sets the created_by_app of this Trunk.
        The application that created the resource.

        :param created_by_app: The created_by_app of this Trunk.
        :type: str
        """
        

        self._created_by_app = created_by_app

    @property
    def trunk_type(self) -> str:
        """
        Gets the trunk_type of this Trunk.
        The type of this trunk.

        :return: The trunk_type of this Trunk.
        :rtype: str
        """
        return self._trunk_type

    @trunk_type.setter
    def trunk_type(self, trunk_type: str) -> None:
        """
        Sets the trunk_type of this Trunk.
        The type of this trunk.

        :param trunk_type: The trunk_type of this Trunk.
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
    def edge(self) -> 'DomainEntityRef':
        """
        Gets the edge of this Trunk.
        The Edge using this trunk.

        :return: The edge of this Trunk.
        :rtype: DomainEntityRef
        """
        return self._edge

    @edge.setter
    def edge(self, edge: 'DomainEntityRef') -> None:
        """
        Sets the edge of this Trunk.
        The Edge using this trunk.

        :param edge: The edge of this Trunk.
        :type: DomainEntityRef
        """
        

        self._edge = edge

    @property
    def trunk_base(self) -> 'DomainEntityRef':
        """
        Gets the trunk_base of this Trunk.
        The trunk base configuration used on this trunk.

        :return: The trunk_base of this Trunk.
        :rtype: DomainEntityRef
        """
        return self._trunk_base

    @trunk_base.setter
    def trunk_base(self, trunk_base: 'DomainEntityRef') -> None:
        """
        Sets the trunk_base of this Trunk.
        The trunk base configuration used on this trunk.

        :param trunk_base: The trunk_base of this Trunk.
        :type: DomainEntityRef
        """
        

        self._trunk_base = trunk_base

    @property
    def trunk_metabase(self) -> 'DomainEntityRef':
        """
        Gets the trunk_metabase of this Trunk.
        The metabase used to create this trunk.

        :return: The trunk_metabase of this Trunk.
        :rtype: DomainEntityRef
        """
        return self._trunk_metabase

    @trunk_metabase.setter
    def trunk_metabase(self, trunk_metabase: 'DomainEntityRef') -> None:
        """
        Sets the trunk_metabase of this Trunk.
        The metabase used to create this trunk.

        :param trunk_metabase: The trunk_metabase of this Trunk.
        :type: DomainEntityRef
        """
        

        self._trunk_metabase = trunk_metabase

    @property
    def edge_group(self) -> 'DomainEntityRef':
        """
        Gets the edge_group of this Trunk.
        The edge group associated with this trunk.

        :return: The edge_group of this Trunk.
        :rtype: DomainEntityRef
        """
        return self._edge_group

    @edge_group.setter
    def edge_group(self, edge_group: 'DomainEntityRef') -> None:
        """
        Sets the edge_group of this Trunk.
        The edge group associated with this trunk.

        :param edge_group: The edge_group of this Trunk.
        :type: DomainEntityRef
        """
        

        self._edge_group = edge_group

    @property
    def in_service(self) -> bool:
        """
        Gets the in_service of this Trunk.
        True if this trunk is in-service.  This comes from the trunk_enabled property of the referenced trunk base.

        :return: The in_service of this Trunk.
        :rtype: bool
        """
        return self._in_service

    @in_service.setter
    def in_service(self, in_service: bool) -> None:
        """
        Sets the in_service of this Trunk.
        True if this trunk is in-service.  This comes from the trunk_enabled property of the referenced trunk base.

        :param in_service: The in_service of this Trunk.
        :type: bool
        """
        

        self._in_service = in_service

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this Trunk.
        True if the Edge used by this trunk is in-service

        :return: The enabled of this Trunk.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this Trunk.
        True if the Edge used by this trunk is in-service

        :param enabled: The enabled of this Trunk.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def logical_interface(self) -> 'DomainEntityRef':
        """
        Gets the logical_interface of this Trunk.
        The Logical Interface on the Edge to which the trunk is assigned.

        :return: The logical_interface of this Trunk.
        :rtype: DomainEntityRef
        """
        return self._logical_interface

    @logical_interface.setter
    def logical_interface(self, logical_interface: 'DomainEntityRef') -> None:
        """
        Sets the logical_interface of this Trunk.
        The Logical Interface on the Edge to which the trunk is assigned.

        :param logical_interface: The logical_interface of this Trunk.
        :type: DomainEntityRef
        """
        

        self._logical_interface = logical_interface

    @property
    def connected_status(self) -> 'TrunkConnectedStatus':
        """
        Gets the connected_status of this Trunk.
        The connected status of the trunk

        :return: The connected_status of this Trunk.
        :rtype: TrunkConnectedStatus
        """
        return self._connected_status

    @connected_status.setter
    def connected_status(self, connected_status: 'TrunkConnectedStatus') -> None:
        """
        Sets the connected_status of this Trunk.
        The connected status of the trunk

        :param connected_status: The connected_status of this Trunk.
        :type: TrunkConnectedStatus
        """
        

        self._connected_status = connected_status

    @property
    def options_status(self) -> List['TrunkMetricsOptions']:
        """
        Gets the options_status of this Trunk.
        The trunk optionsStatus

        :return: The options_status of this Trunk.
        :rtype: list[TrunkMetricsOptions]
        """
        return self._options_status

    @options_status.setter
    def options_status(self, options_status: List['TrunkMetricsOptions']) -> None:
        """
        Sets the options_status of this Trunk.
        The trunk optionsStatus

        :param options_status: The options_status of this Trunk.
        :type: list[TrunkMetricsOptions]
        """
        

        self._options_status = options_status

    @property
    def registers_status(self) -> List['TrunkMetricsRegisters']:
        """
        Gets the registers_status of this Trunk.
        The trunk registersStatus

        :return: The registers_status of this Trunk.
        :rtype: list[TrunkMetricsRegisters]
        """
        return self._registers_status

    @registers_status.setter
    def registers_status(self, registers_status: List['TrunkMetricsRegisters']) -> None:
        """
        Sets the registers_status of this Trunk.
        The trunk registersStatus

        :param registers_status: The registers_status of this Trunk.
        :type: list[TrunkMetricsRegisters]
        """
        

        self._registers_status = registers_status

    @property
    def ip_status(self) -> 'TrunkMetricsNetworkTypeIp':
        """
        Gets the ip_status of this Trunk.
        The trunk ipStatus

        :return: The ip_status of this Trunk.
        :rtype: TrunkMetricsNetworkTypeIp
        """
        return self._ip_status

    @ip_status.setter
    def ip_status(self, ip_status: 'TrunkMetricsNetworkTypeIp') -> None:
        """
        Sets the ip_status of this Trunk.
        The trunk ipStatus

        :param ip_status: The ip_status of this Trunk.
        :type: TrunkMetricsNetworkTypeIp
        """
        

        self._ip_status = ip_status

    @property
    def options_enabled_status(self) -> str:
        """
        Gets the options_enabled_status of this Trunk.
        Returns Enabled when the trunk base supports the availability interval and it has a value greater than 0.

        :return: The options_enabled_status of this Trunk.
        :rtype: str
        """
        return self._options_enabled_status

    @options_enabled_status.setter
    def options_enabled_status(self, options_enabled_status: str) -> None:
        """
        Sets the options_enabled_status of this Trunk.
        Returns Enabled when the trunk base supports the availability interval and it has a value greater than 0.

        :param options_enabled_status: The options_enabled_status of this Trunk.
        :type: str
        """
        if isinstance(options_enabled_status, int):
            options_enabled_status = str(options_enabled_status)
        allowed_values = ["ENABLED", "DISABLED", "NOT_SUPPORTED"]
        if options_enabled_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for options_enabled_status -> " + options_enabled_status)
            self._options_enabled_status = "outdated_sdk_version"
        else:
            self._options_enabled_status = options_enabled_status

    @property
    def registers_enabled_status(self) -> str:
        """
        Gets the registers_enabled_status of this Trunk.
        Returns Enabled when the trunk base supports the registration interval and it has a value greater than 0.

        :return: The registers_enabled_status of this Trunk.
        :rtype: str
        """
        return self._registers_enabled_status

    @registers_enabled_status.setter
    def registers_enabled_status(self, registers_enabled_status: str) -> None:
        """
        Sets the registers_enabled_status of this Trunk.
        Returns Enabled when the trunk base supports the registration interval and it has a value greater than 0.

        :param registers_enabled_status: The registers_enabled_status of this Trunk.
        :type: str
        """
        if isinstance(registers_enabled_status, int):
            registers_enabled_status = str(registers_enabled_status)
        allowed_values = ["ENABLED", "DISABLED", "NOT_SUPPORTED"]
        if registers_enabled_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for registers_enabled_status -> " + registers_enabled_status)
            self._registers_enabled_status = "outdated_sdk_version"
        else:
            self._registers_enabled_status = registers_enabled_status

    @property
    def family(self) -> int:
        """
        Gets the family of this Trunk.
        The IP Network Family of the trunk

        :return: The family of this Trunk.
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family: int) -> None:
        """
        Sets the family of this Trunk.
        The IP Network Family of the trunk

        :param family: The family of this Trunk.
        :type: int
        """
        

        self._family = family

    @property
    def proxy_address_list(self) -> List[str]:
        """
        Gets the proxy_address_list of this Trunk.
        The list of proxy addresses (ports if provided) for the trunk

        :return: The proxy_address_list of this Trunk.
        :rtype: list[str]
        """
        return self._proxy_address_list

    @proxy_address_list.setter
    def proxy_address_list(self, proxy_address_list: List[str]) -> None:
        """
        Sets the proxy_address_list of this Trunk.
        The list of proxy addresses (ports if provided) for the trunk

        :param proxy_address_list: The proxy_address_list of this Trunk.
        :type: list[str]
        """
        

        self._proxy_address_list = proxy_address_list

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Trunk.
        The URI for this object

        :return: The self_uri of this Trunk.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Trunk.
        The URI for this object

        :param self_uri: The self_uri of this Trunk.
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

