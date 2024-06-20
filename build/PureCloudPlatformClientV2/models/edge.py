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
    from . import DomainEdgeSoftwareUpdateDto
    from . import EdgeGroup
    from . import EdgeInterface
    from . import Site

class Edge(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Edge - a model defined in Swagger

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
            'interfaces': 'list[EdgeInterface]',
            'make': 'str',
            'model': 'str',
            'api_version': 'str',
            'software_version': 'str',
            'software_version_timestamp': 'str',
            'software_version_platform': 'str',
            'software_version_configuration': 'str',
            'full_software_version': 'str',
            'pairing_id': 'str',
            'fingerprint': 'str',
            'fingerprint_hint': 'str',
            'current_version': 'str',
            'staged_version': 'str',
            'patch': 'str',
            'status_code': 'str',
            'edge_group': 'EdgeGroup',
            'site': 'Site',
            'software_status': 'DomainEdgeSoftwareUpdateDto',
            'online_status': 'str',
            'serial_number': 'str',
            'physical_edge': 'bool',
            'managed': 'bool',
            'edge_deployment_type': 'str',
            'cert_type': 'str',
            'call_draining_state': 'str',
            'conversation_count': 'int',
            'proxy': 'str',
            'offline_config_called': 'bool',
            'os_name': 'str',
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
            'interfaces': 'interfaces',
            'make': 'make',
            'model': 'model',
            'api_version': 'apiVersion',
            'software_version': 'softwareVersion',
            'software_version_timestamp': 'softwareVersionTimestamp',
            'software_version_platform': 'softwareVersionPlatform',
            'software_version_configuration': 'softwareVersionConfiguration',
            'full_software_version': 'fullSoftwareVersion',
            'pairing_id': 'pairingId',
            'fingerprint': 'fingerprint',
            'fingerprint_hint': 'fingerprintHint',
            'current_version': 'currentVersion',
            'staged_version': 'stagedVersion',
            'patch': 'patch',
            'status_code': 'statusCode',
            'edge_group': 'edgeGroup',
            'site': 'site',
            'software_status': 'softwareStatus',
            'online_status': 'onlineStatus',
            'serial_number': 'serialNumber',
            'physical_edge': 'physicalEdge',
            'managed': 'managed',
            'edge_deployment_type': 'edgeDeploymentType',
            'cert_type': 'certType',
            'call_draining_state': 'callDrainingState',
            'conversation_count': 'conversationCount',
            'proxy': 'proxy',
            'offline_config_called': 'offlineConfigCalled',
            'os_name': 'osName',
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
        self._interfaces = None
        self._make = None
        self._model = None
        self._api_version = None
        self._software_version = None
        self._software_version_timestamp = None
        self._software_version_platform = None
        self._software_version_configuration = None
        self._full_software_version = None
        self._pairing_id = None
        self._fingerprint = None
        self._fingerprint_hint = None
        self._current_version = None
        self._staged_version = None
        self._patch = None
        self._status_code = None
        self._edge_group = None
        self._site = None
        self._software_status = None
        self._online_status = None
        self._serial_number = None
        self._physical_edge = None
        self._managed = None
        self._edge_deployment_type = None
        self._cert_type = None
        self._call_draining_state = None
        self._conversation_count = None
        self._proxy = None
        self._offline_config_called = None
        self._os_name = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Edge.
        The globally unique identifier for the object.

        :return: The id of this Edge.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Edge.
        The globally unique identifier for the object.

        :param id: The id of this Edge.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Edge.
        The name of the entity.

        :return: The name of this Edge.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Edge.
        The name of the entity.

        :param name: The name of this Edge.
        :type: str
        """
        

        self._name = name

    @property
    def division(self) -> 'Division':
        """
        Gets the division of this Edge.
        The division to which this entity belongs.

        :return: The division of this Edge.
        :rtype: Division
        """
        return self._division

    @division.setter
    def division(self, division: 'Division') -> None:
        """
        Sets the division of this Edge.
        The division to which this entity belongs.

        :param division: The division of this Edge.
        :type: Division
        """
        

        self._division = division

    @property
    def description(self) -> str:
        """
        Gets the description of this Edge.
        The resource's description.

        :return: The description of this Edge.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this Edge.
        The resource's description.

        :param description: The description of this Edge.
        :type: str
        """
        

        self._description = description

    @property
    def version(self) -> int:
        """
        Gets the version of this Edge.
        The current version of the resource.

        :return: The version of this Edge.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this Edge.
        The current version of the resource.

        :param version: The version of this Edge.
        :type: int
        """
        

        self._version = version

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Edge.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Edge.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Edge.
        The date the resource was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Edge.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this Edge.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Edge.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this Edge.
        The date of the last modification to the resource. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Edge.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> str:
        """
        Gets the modified_by of this Edge.
        The ID of the user that last modified the resource.

        :return: The modified_by of this Edge.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: str) -> None:
        """
        Sets the modified_by of this Edge.
        The ID of the user that last modified the resource.

        :param modified_by: The modified_by of this Edge.
        :type: str
        """
        

        self._modified_by = modified_by

    @property
    def created_by(self) -> str:
        """
        Gets the created_by of this Edge.
        The ID of the user that created the resource.

        :return: The created_by of this Edge.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by: str) -> None:
        """
        Sets the created_by of this Edge.
        The ID of the user that created the resource.

        :param created_by: The created_by of this Edge.
        :type: str
        """
        

        self._created_by = created_by

    @property
    def state(self) -> str:
        """
        Gets the state of this Edge.
        Indicates if the resource is active, inactive, or deleted.

        :return: The state of this Edge.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this Edge.
        Indicates if the resource is active, inactive, or deleted.

        :param state: The state of this Edge.
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
        Gets the modified_by_app of this Edge.
        The application that last modified the resource.

        :return: The modified_by_app of this Edge.
        :rtype: str
        """
        return self._modified_by_app

    @modified_by_app.setter
    def modified_by_app(self, modified_by_app: str) -> None:
        """
        Sets the modified_by_app of this Edge.
        The application that last modified the resource.

        :param modified_by_app: The modified_by_app of this Edge.
        :type: str
        """
        

        self._modified_by_app = modified_by_app

    @property
    def created_by_app(self) -> str:
        """
        Gets the created_by_app of this Edge.
        The application that created the resource.

        :return: The created_by_app of this Edge.
        :rtype: str
        """
        return self._created_by_app

    @created_by_app.setter
    def created_by_app(self, created_by_app: str) -> None:
        """
        Sets the created_by_app of this Edge.
        The application that created the resource.

        :param created_by_app: The created_by_app of this Edge.
        :type: str
        """
        

        self._created_by_app = created_by_app

    @property
    def interfaces(self) -> List['EdgeInterface']:
        """
        Gets the interfaces of this Edge.
        The list of interfaces for the edge. (Deprecated) Replaced by configuring trunks/ip info on the logical interface instead

        :return: The interfaces of this Edge.
        :rtype: list[EdgeInterface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces: List['EdgeInterface']) -> None:
        """
        Sets the interfaces of this Edge.
        The list of interfaces for the edge. (Deprecated) Replaced by configuring trunks/ip info on the logical interface instead

        :param interfaces: The interfaces of this Edge.
        :type: list[EdgeInterface]
        """
        

        self._interfaces = interfaces

    @property
    def make(self) -> str:
        """
        Gets the make of this Edge.


        :return: The make of this Edge.
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make: str) -> None:
        """
        Sets the make of this Edge.


        :param make: The make of this Edge.
        :type: str
        """
        

        self._make = make

    @property
    def model(self) -> str:
        """
        Gets the model of this Edge.


        :return: The model of this Edge.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str) -> None:
        """
        Sets the model of this Edge.


        :param model: The model of this Edge.
        :type: str
        """
        

        self._model = model

    @property
    def api_version(self) -> str:
        """
        Gets the api_version of this Edge.


        :return: The api_version of this Edge.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version: str) -> None:
        """
        Sets the api_version of this Edge.


        :param api_version: The api_version of this Edge.
        :type: str
        """
        

        self._api_version = api_version

    @property
    def software_version(self) -> str:
        """
        Gets the software_version of this Edge.


        :return: The software_version of this Edge.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version: str) -> None:
        """
        Sets the software_version of this Edge.


        :param software_version: The software_version of this Edge.
        :type: str
        """
        

        self._software_version = software_version

    @property
    def software_version_timestamp(self) -> str:
        """
        Gets the software_version_timestamp of this Edge.


        :return: The software_version_timestamp of this Edge.
        :rtype: str
        """
        return self._software_version_timestamp

    @software_version_timestamp.setter
    def software_version_timestamp(self, software_version_timestamp: str) -> None:
        """
        Sets the software_version_timestamp of this Edge.


        :param software_version_timestamp: The software_version_timestamp of this Edge.
        :type: str
        """
        

        self._software_version_timestamp = software_version_timestamp

    @property
    def software_version_platform(self) -> str:
        """
        Gets the software_version_platform of this Edge.


        :return: The software_version_platform of this Edge.
        :rtype: str
        """
        return self._software_version_platform

    @software_version_platform.setter
    def software_version_platform(self, software_version_platform: str) -> None:
        """
        Sets the software_version_platform of this Edge.


        :param software_version_platform: The software_version_platform of this Edge.
        :type: str
        """
        

        self._software_version_platform = software_version_platform

    @property
    def software_version_configuration(self) -> str:
        """
        Gets the software_version_configuration of this Edge.


        :return: The software_version_configuration of this Edge.
        :rtype: str
        """
        return self._software_version_configuration

    @software_version_configuration.setter
    def software_version_configuration(self, software_version_configuration: str) -> None:
        """
        Sets the software_version_configuration of this Edge.


        :param software_version_configuration: The software_version_configuration of this Edge.
        :type: str
        """
        

        self._software_version_configuration = software_version_configuration

    @property
    def full_software_version(self) -> str:
        """
        Gets the full_software_version of this Edge.


        :return: The full_software_version of this Edge.
        :rtype: str
        """
        return self._full_software_version

    @full_software_version.setter
    def full_software_version(self, full_software_version: str) -> None:
        """
        Sets the full_software_version of this Edge.


        :param full_software_version: The full_software_version of this Edge.
        :type: str
        """
        

        self._full_software_version = full_software_version

    @property
    def pairing_id(self) -> str:
        """
        Gets the pairing_id of this Edge.
        The pairing Id for a hardware Edge in the format: 00000-00000-00000-00000-00000. This field is only required when creating an Edge with a deployment type of HARDWARE.

        :return: The pairing_id of this Edge.
        :rtype: str
        """
        return self._pairing_id

    @pairing_id.setter
    def pairing_id(self, pairing_id: str) -> None:
        """
        Sets the pairing_id of this Edge.
        The pairing Id for a hardware Edge in the format: 00000-00000-00000-00000-00000. This field is only required when creating an Edge with a deployment type of HARDWARE.

        :param pairing_id: The pairing_id of this Edge.
        :type: str
        """
        

        self._pairing_id = pairing_id

    @property
    def fingerprint(self) -> str:
        """
        Gets the fingerprint of this Edge.


        :return: The fingerprint of this Edge.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint: str) -> None:
        """
        Sets the fingerprint of this Edge.


        :param fingerprint: The fingerprint of this Edge.
        :type: str
        """
        

        self._fingerprint = fingerprint

    @property
    def fingerprint_hint(self) -> str:
        """
        Gets the fingerprint_hint of this Edge.


        :return: The fingerprint_hint of this Edge.
        :rtype: str
        """
        return self._fingerprint_hint

    @fingerprint_hint.setter
    def fingerprint_hint(self, fingerprint_hint: str) -> None:
        """
        Sets the fingerprint_hint of this Edge.


        :param fingerprint_hint: The fingerprint_hint of this Edge.
        :type: str
        """
        

        self._fingerprint_hint = fingerprint_hint

    @property
    def current_version(self) -> str:
        """
        Gets the current_version of this Edge.


        :return: The current_version of this Edge.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version: str) -> None:
        """
        Sets the current_version of this Edge.


        :param current_version: The current_version of this Edge.
        :type: str
        """
        

        self._current_version = current_version

    @property
    def staged_version(self) -> str:
        """
        Gets the staged_version of this Edge.


        :return: The staged_version of this Edge.
        :rtype: str
        """
        return self._staged_version

    @staged_version.setter
    def staged_version(self, staged_version: str) -> None:
        """
        Sets the staged_version of this Edge.


        :param staged_version: The staged_version of this Edge.
        :type: str
        """
        

        self._staged_version = staged_version

    @property
    def patch(self) -> str:
        """
        Gets the patch of this Edge.


        :return: The patch of this Edge.
        :rtype: str
        """
        return self._patch

    @patch.setter
    def patch(self, patch: str) -> None:
        """
        Sets the patch of this Edge.


        :param patch: The patch of this Edge.
        :type: str
        """
        

        self._patch = patch

    @property
    def status_code(self) -> str:
        """
        Gets the status_code of this Edge.
        The current status of the Edge.

        :return: The status_code of this Edge.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: str) -> None:
        """
        Sets the status_code of this Edge.
        The current status of the Edge.

        :param status_code: The status_code of this Edge.
        :type: str
        """
        if isinstance(status_code, int):
            status_code = str(status_code)
        allowed_values = ["NEW", "AWAITING_CONNECTION", "AWAITING_FINGERPRINT", "AWAITING_FINGERPRINT_VERIFICATION", "FINGERPRINT_VERIFIED", "AWAITING_BOOTSTRAP", "ACTIVE", "INACTIVE", "RMA", "UNPAIRING", "UNPAIRED", "INITIALIZING"]
        if status_code.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status_code -> " + status_code)
            self._status_code = "outdated_sdk_version"
        else:
            self._status_code = status_code

    @property
    def edge_group(self) -> 'EdgeGroup':
        """
        Gets the edge_group of this Edge.


        :return: The edge_group of this Edge.
        :rtype: EdgeGroup
        """
        return self._edge_group

    @edge_group.setter
    def edge_group(self, edge_group: 'EdgeGroup') -> None:
        """
        Sets the edge_group of this Edge.


        :param edge_group: The edge_group of this Edge.
        :type: EdgeGroup
        """
        

        self._edge_group = edge_group

    @property
    def site(self) -> 'Site':
        """
        Gets the site of this Edge.
        The Site to which the Edge is assigned.

        :return: The site of this Edge.
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site: 'Site') -> None:
        """
        Sets the site of this Edge.
        The Site to which the Edge is assigned.

        :param site: The site of this Edge.
        :type: Site
        """
        

        self._site = site

    @property
    def software_status(self) -> 'DomainEdgeSoftwareUpdateDto':
        """
        Gets the software_status of this Edge.
        Details about an in-progress or recently in-progress Edge software upgrade. This node appears only if a software upgrade was recently initiated for this Edge.

        :return: The software_status of this Edge.
        :rtype: DomainEdgeSoftwareUpdateDto
        """
        return self._software_status

    @software_status.setter
    def software_status(self, software_status: 'DomainEdgeSoftwareUpdateDto') -> None:
        """
        Sets the software_status of this Edge.
        Details about an in-progress or recently in-progress Edge software upgrade. This node appears only if a software upgrade was recently initiated for this Edge.

        :param software_status: The software_status of this Edge.
        :type: DomainEdgeSoftwareUpdateDto
        """
        

        self._software_status = software_status

    @property
    def online_status(self) -> str:
        """
        Gets the online_status of this Edge.


        :return: The online_status of this Edge.
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status: str) -> None:
        """
        Sets the online_status of this Edge.


        :param online_status: The online_status of this Edge.
        :type: str
        """
        if isinstance(online_status, int):
            online_status = str(online_status)
        allowed_values = ["ONLINE", "OFFLINE"]
        if online_status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for online_status -> " + online_status)
            self._online_status = "outdated_sdk_version"
        else:
            self._online_status = online_status

    @property
    def serial_number(self) -> str:
        """
        Gets the serial_number of this Edge.


        :return: The serial_number of this Edge.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str) -> None:
        """
        Sets the serial_number of this Edge.


        :param serial_number: The serial_number of this Edge.
        :type: str
        """
        

        self._serial_number = serial_number

    @property
    def physical_edge(self) -> bool:
        """
        Gets the physical_edge of this Edge.


        :return: The physical_edge of this Edge.
        :rtype: bool
        """
        return self._physical_edge

    @physical_edge.setter
    def physical_edge(self, physical_edge: bool) -> None:
        """
        Sets the physical_edge of this Edge.


        :param physical_edge: The physical_edge of this Edge.
        :type: bool
        """
        

        self._physical_edge = physical_edge

    @property
    def managed(self) -> bool:
        """
        Gets the managed of this Edge.


        :return: The managed of this Edge.
        :rtype: bool
        """
        return self._managed

    @managed.setter
    def managed(self, managed: bool) -> None:
        """
        Sets the managed of this Edge.


        :param managed: The managed of this Edge.
        :type: bool
        """
        

        self._managed = managed

    @property
    def edge_deployment_type(self) -> str:
        """
        Gets the edge_deployment_type of this Edge.


        :return: The edge_deployment_type of this Edge.
        :rtype: str
        """
        return self._edge_deployment_type

    @edge_deployment_type.setter
    def edge_deployment_type(self, edge_deployment_type: str) -> None:
        """
        Sets the edge_deployment_type of this Edge.


        :param edge_deployment_type: The edge_deployment_type of this Edge.
        :type: str
        """
        if isinstance(edge_deployment_type, int):
            edge_deployment_type = str(edge_deployment_type)
        allowed_values = ["HARDWARE", "LDM", "CDM", "CHS", "INVALID"]
        if edge_deployment_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for edge_deployment_type -> " + edge_deployment_type)
            self._edge_deployment_type = "outdated_sdk_version"
        else:
            self._edge_deployment_type = edge_deployment_type

    @property
    def cert_type(self) -> str:
        """
        Gets the cert_type of this Edge.
        The type of certificate used to communicate with edge-proxy.

        :return: The cert_type of this Edge.
        :rtype: str
        """
        return self._cert_type

    @cert_type.setter
    def cert_type(self, cert_type: str) -> None:
        """
        Sets the cert_type of this Edge.
        The type of certificate used to communicate with edge-proxy.

        :param cert_type: The cert_type of this Edge.
        :type: str
        """
        if isinstance(cert_type, int):
            cert_type = str(cert_type)
        allowed_values = ["PureCloud", "Public", "China", "NotRequested"]
        if cert_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for cert_type -> " + cert_type)
            self._cert_type = "outdated_sdk_version"
        else:
            self._cert_type = cert_type

    @property
    def call_draining_state(self) -> str:
        """
        Gets the call_draining_state of this Edge.
        The current state of the Edge's call draining process before it can be safely rebooted or updated.

        :return: The call_draining_state of this Edge.
        :rtype: str
        """
        return self._call_draining_state

    @call_draining_state.setter
    def call_draining_state(self, call_draining_state: str) -> None:
        """
        Sets the call_draining_state of this Edge.
        The current state of the Edge's call draining process before it can be safely rebooted or updated.

        :param call_draining_state: The call_draining_state of this Edge.
        :type: str
        """
        if isinstance(call_draining_state, int):
            call_draining_state = str(call_draining_state)
        allowed_values = ["NONE", "WAIT", "WAIT_TIMEOUT", "TERMINATE", "COMPLETE"]
        if call_draining_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for call_draining_state -> " + call_draining_state)
            self._call_draining_state = "outdated_sdk_version"
        else:
            self._call_draining_state = call_draining_state

    @property
    def conversation_count(self) -> int:
        """
        Gets the conversation_count of this Edge.
        The remaining number of conversations the Edge has to drain before it can be safely rebooted or updated. When an Edge is not draining conversations, this will be NULL or 0.

        :return: The conversation_count of this Edge.
        :rtype: int
        """
        return self._conversation_count

    @conversation_count.setter
    def conversation_count(self, conversation_count: int) -> None:
        """
        Sets the conversation_count of this Edge.
        The remaining number of conversations the Edge has to drain before it can be safely rebooted or updated. When an Edge is not draining conversations, this will be NULL or 0.

        :param conversation_count: The conversation_count of this Edge.
        :type: int
        """
        

        self._conversation_count = conversation_count

    @property
    def proxy(self) -> str:
        """
        Gets the proxy of this Edge.
        Edge HTTP proxy configuration for the WAN port. The field can be a hostname, FQDN, IPv4 or IPv6 address. If port is not included, port 80 is assumed.

        :return: The proxy of this Edge.
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: str) -> None:
        """
        Sets the proxy of this Edge.
        Edge HTTP proxy configuration for the WAN port. The field can be a hostname, FQDN, IPv4 or IPv6 address. If port is not included, port 80 is assumed.

        :param proxy: The proxy of this Edge.
        :type: str
        """
        

        self._proxy = proxy

    @property
    def offline_config_called(self) -> bool:
        """
        Gets the offline_config_called of this Edge.
        True if the offline edge configuration endpoint has been called for this edge.

        :return: The offline_config_called of this Edge.
        :rtype: bool
        """
        return self._offline_config_called

    @offline_config_called.setter
    def offline_config_called(self, offline_config_called: bool) -> None:
        """
        Sets the offline_config_called of this Edge.
        True if the offline edge configuration endpoint has been called for this edge.

        :param offline_config_called: The offline_config_called of this Edge.
        :type: bool
        """
        

        self._offline_config_called = offline_config_called

    @property
    def os_name(self) -> str:
        """
        Gets the os_name of this Edge.
        The name provided by the operating system of the Edge.

        :return: The os_name of this Edge.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name: str) -> None:
        """
        Sets the os_name of this Edge.
        The name provided by the operating system of the Edge.

        :param os_name: The os_name of this Edge.
        :type: str
        """
        

        self._os_name = os_name

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Edge.
        The URI for this object

        :return: The self_uri of this Edge.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Edge.
        The URI for this object

        :param self_uri: The self_uri of this Edge.
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

