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
    from . import DialerContactlistConfigChangeContactPhoneNumberColumn
    from . import DialerContactlistConfigChangeEmailColumn
    from . import DialerContactlistConfigChangeImportStatus
    from . import DialerContactlistConfigChangeUriReference

class DialerContactlistConfigChangeContactList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerContactlistConfigChangeContactList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'column_names': 'list[str]',
            'phone_columns': 'list[DialerContactlistConfigChangeContactPhoneNumberColumn]',
            'email_columns': 'list[DialerContactlistConfigChangeEmailColumn]',
            'import_status': 'DialerContactlistConfigChangeImportStatus',
            'preview_mode_column_name': 'str',
            'preview_mode_accepted_values': 'list[str]',
            'size': 'int',
            'attempt_limits': 'DialerContactlistConfigChangeUriReference',
            'automatic_time_zone_mapping': 'bool',
            'zip_code_column_name': 'str',
            'division': 'DialerContactlistConfigChangeUriReference',
            'additional_properties': 'dict(str, object)',
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int'
        }

        self.attribute_map = {
            'column_names': 'columnNames',
            'phone_columns': 'phoneColumns',
            'email_columns': 'emailColumns',
            'import_status': 'importStatus',
            'preview_mode_column_name': 'previewModeColumnName',
            'preview_mode_accepted_values': 'previewModeAcceptedValues',
            'size': 'size',
            'attempt_limits': 'attemptLimits',
            'automatic_time_zone_mapping': 'automaticTimeZoneMapping',
            'zip_code_column_name': 'zipCodeColumnName',
            'division': 'division',
            'additional_properties': 'additionalProperties',
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version'
        }

        self._column_names = None
        self._phone_columns = None
        self._email_columns = None
        self._import_status = None
        self._preview_mode_column_name = None
        self._preview_mode_accepted_values = None
        self._size = None
        self._attempt_limits = None
        self._automatic_time_zone_mapping = None
        self._zip_code_column_name = None
        self._division = None
        self._additional_properties = None
        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None

    @property
    def column_names(self) -> List[str]:
        """
        Gets the column_names of this DialerContactlistConfigChangeContactList.
        the contact column names

        :return: The column_names of this DialerContactlistConfigChangeContactList.
        :rtype: list[str]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names: List[str]) -> None:
        """
        Sets the column_names of this DialerContactlistConfigChangeContactList.
        the contact column names

        :param column_names: The column_names of this DialerContactlistConfigChangeContactList.
        :type: list[str]
        """
        

        self._column_names = column_names

    @property
    def phone_columns(self) -> List['DialerContactlistConfigChangeContactPhoneNumberColumn']:
        """
        Gets the phone_columns of this DialerContactlistConfigChangeContactList.
        the columns containing phone numbers

        :return: The phone_columns of this DialerContactlistConfigChangeContactList.
        :rtype: list[DialerContactlistConfigChangeContactPhoneNumberColumn]
        """
        return self._phone_columns

    @phone_columns.setter
    def phone_columns(self, phone_columns: List['DialerContactlistConfigChangeContactPhoneNumberColumn']) -> None:
        """
        Sets the phone_columns of this DialerContactlistConfigChangeContactList.
        the columns containing phone numbers

        :param phone_columns: The phone_columns of this DialerContactlistConfigChangeContactList.
        :type: list[DialerContactlistConfigChangeContactPhoneNumberColumn]
        """
        

        self._phone_columns = phone_columns

    @property
    def email_columns(self) -> List['DialerContactlistConfigChangeEmailColumn']:
        """
        Gets the email_columns of this DialerContactlistConfigChangeContactList.
        the columns containing email addresses

        :return: The email_columns of this DialerContactlistConfigChangeContactList.
        :rtype: list[DialerContactlistConfigChangeEmailColumn]
        """
        return self._email_columns

    @email_columns.setter
    def email_columns(self, email_columns: List['DialerContactlistConfigChangeEmailColumn']) -> None:
        """
        Sets the email_columns of this DialerContactlistConfigChangeContactList.
        the columns containing email addresses

        :param email_columns: The email_columns of this DialerContactlistConfigChangeContactList.
        :type: list[DialerContactlistConfigChangeEmailColumn]
        """
        

        self._email_columns = email_columns

    @property
    def import_status(self) -> 'DialerContactlistConfigChangeImportStatus':
        """
        Gets the import_status of this DialerContactlistConfigChangeContactList.


        :return: The import_status of this DialerContactlistConfigChangeContactList.
        :rtype: DialerContactlistConfigChangeImportStatus
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status: 'DialerContactlistConfigChangeImportStatus') -> None:
        """
        Sets the import_status of this DialerContactlistConfigChangeContactList.


        :param import_status: The import_status of this DialerContactlistConfigChangeContactList.
        :type: DialerContactlistConfigChangeImportStatus
        """
        

        self._import_status = import_status

    @property
    def preview_mode_column_name(self) -> str:
        """
        Gets the preview_mode_column_name of this DialerContactlistConfigChangeContactList.
        the name of the column that holds the indicators for contacts that are to be dialed in preview mode only

        :return: The preview_mode_column_name of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._preview_mode_column_name

    @preview_mode_column_name.setter
    def preview_mode_column_name(self, preview_mode_column_name: str) -> None:
        """
        Sets the preview_mode_column_name of this DialerContactlistConfigChangeContactList.
        the name of the column that holds the indicators for contacts that are to be dialed in preview mode only

        :param preview_mode_column_name: The preview_mode_column_name of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        

        self._preview_mode_column_name = preview_mode_column_name

    @property
    def preview_mode_accepted_values(self) -> List[str]:
        """
        Gets the preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.
        list of user-defined values indicating the contact is to be dialed in preview mode only

        :return: The preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.
        :rtype: list[str]
        """
        return self._preview_mode_accepted_values

    @preview_mode_accepted_values.setter
    def preview_mode_accepted_values(self, preview_mode_accepted_values: List[str]) -> None:
        """
        Sets the preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.
        list of user-defined values indicating the contact is to be dialed in preview mode only

        :param preview_mode_accepted_values: The preview_mode_accepted_values of this DialerContactlistConfigChangeContactList.
        :type: list[str]
        """
        

        self._preview_mode_accepted_values = preview_mode_accepted_values

    @property
    def size(self) -> int:
        """
        Gets the size of this DialerContactlistConfigChangeContactList.
        the number of contacts in the contact list

        :return: The size of this DialerContactlistConfigChangeContactList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        """
        Sets the size of this DialerContactlistConfigChangeContactList.
        the number of contacts in the contact list

        :param size: The size of this DialerContactlistConfigChangeContactList.
        :type: int
        """
        

        self._size = size

    @property
    def attempt_limits(self) -> 'DialerContactlistConfigChangeUriReference':
        """
        Gets the attempt_limits of this DialerContactlistConfigChangeContactList.


        :return: The attempt_limits of this DialerContactlistConfigChangeContactList.
        :rtype: DialerContactlistConfigChangeUriReference
        """
        return self._attempt_limits

    @attempt_limits.setter
    def attempt_limits(self, attempt_limits: 'DialerContactlistConfigChangeUriReference') -> None:
        """
        Sets the attempt_limits of this DialerContactlistConfigChangeContactList.


        :param attempt_limits: The attempt_limits of this DialerContactlistConfigChangeContactList.
        :type: DialerContactlistConfigChangeUriReference
        """
        

        self._attempt_limits = attempt_limits

    @property
    def automatic_time_zone_mapping(self) -> bool:
        """
        Gets the automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.
        whether or not automatic time zone mapping is enabled on the list

        :return: The automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.
        :rtype: bool
        """
        return self._automatic_time_zone_mapping

    @automatic_time_zone_mapping.setter
    def automatic_time_zone_mapping(self, automatic_time_zone_mapping: bool) -> None:
        """
        Sets the automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.
        whether or not automatic time zone mapping is enabled on the list

        :param automatic_time_zone_mapping: The automatic_time_zone_mapping of this DialerContactlistConfigChangeContactList.
        :type: bool
        """
        

        self._automatic_time_zone_mapping = automatic_time_zone_mapping

    @property
    def zip_code_column_name(self) -> str:
        """
        Gets the zip_code_column_name of this DialerContactlistConfigChangeContactList.
        zip code column from the contact list to be used optionally with automatic time zone mapping

        :return: The zip_code_column_name of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._zip_code_column_name

    @zip_code_column_name.setter
    def zip_code_column_name(self, zip_code_column_name: str) -> None:
        """
        Sets the zip_code_column_name of this DialerContactlistConfigChangeContactList.
        zip code column from the contact list to be used optionally with automatic time zone mapping

        :param zip_code_column_name: The zip_code_column_name of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        

        self._zip_code_column_name = zip_code_column_name

    @property
    def division(self) -> 'DialerContactlistConfigChangeUriReference':
        """
        Gets the division of this DialerContactlistConfigChangeContactList.
        A UriReference for a resource

        :return: The division of this DialerContactlistConfigChangeContactList.
        :rtype: DialerContactlistConfigChangeUriReference
        """
        return self._division

    @division.setter
    def division(self, division: 'DialerContactlistConfigChangeUriReference') -> None:
        """
        Sets the division of this DialerContactlistConfigChangeContactList.
        A UriReference for a resource

        :param division: The division of this DialerContactlistConfigChangeContactList.
        :type: DialerContactlistConfigChangeUriReference
        """
        

        self._division = division

    @property
    def additional_properties(self) -> Dict[str, object]:
        """
        Gets the additional_properties of this DialerContactlistConfigChangeContactList.


        :return: The additional_properties of this DialerContactlistConfigChangeContactList.
        :rtype: dict(str, object)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties: Dict[str, object]) -> None:
        """
        Sets the additional_properties of this DialerContactlistConfigChangeContactList.


        :param additional_properties: The additional_properties of this DialerContactlistConfigChangeContactList.
        :type: dict(str, object)
        """
        

        self._additional_properties = additional_properties

    @property
    def id(self) -> str:
        """
        Gets the id of this DialerContactlistConfigChangeContactList.
        The globally unique identifier for the object.

        :return: The id of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this DialerContactlistConfigChangeContactList.
        The globally unique identifier for the object.

        :param id: The id of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this DialerContactlistConfigChangeContactList.
        The UI-visible name of the object

        :return: The name of this DialerContactlistConfigChangeContactList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this DialerContactlistConfigChangeContactList.
        The UI-visible name of the object

        :param name: The name of this DialerContactlistConfigChangeContactList.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this DialerContactlistConfigChangeContactList.
        Creation time of the entity

        :return: The date_created of this DialerContactlistConfigChangeContactList.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this DialerContactlistConfigChangeContactList.
        Creation time of the entity

        :param date_created: The date_created of this DialerContactlistConfigChangeContactList.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this DialerContactlistConfigChangeContactList.
        Last modified time of the entity

        :return: The date_modified of this DialerContactlistConfigChangeContactList.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this DialerContactlistConfigChangeContactList.
        Last modified time of the entity

        :param date_modified: The date_modified of this DialerContactlistConfigChangeContactList.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this DialerContactlistConfigChangeContactList.
        Required for updates, must match the version number of the most recent update

        :return: The version of this DialerContactlistConfigChangeContactList.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this DialerContactlistConfigChangeContactList.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this DialerContactlistConfigChangeContactList.
        :type: int
        """
        

        self._version = version

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

