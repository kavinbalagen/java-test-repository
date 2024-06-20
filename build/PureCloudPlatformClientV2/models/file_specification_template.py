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
    from . import Column
    from . import PreprocessingRule

class FileSpecificationTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FileSpecificationTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'version': 'int',
            'description': 'str',
            'format': 'str',
            'number_of_heading_lines_skipped': 'int',
            'number_of_trailing_lines_skipped': 'int',
            'header': 'bool',
            'delimiter': 'str',
            'delimiter_value': 'str',
            'column_information': 'list[Column]',
            'preprocessing_rules': 'list[PreprocessingRule]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'version': 'version',
            'description': 'description',
            'format': 'format',
            'number_of_heading_lines_skipped': 'numberOfHeadingLinesSkipped',
            'number_of_trailing_lines_skipped': 'numberOfTrailingLinesSkipped',
            'header': 'header',
            'delimiter': 'delimiter',
            'delimiter_value': 'delimiterValue',
            'column_information': 'columnInformation',
            'preprocessing_rules': 'preprocessingRules',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._date_created = None
        self._date_modified = None
        self._version = None
        self._description = None
        self._format = None
        self._number_of_heading_lines_skipped = None
        self._number_of_trailing_lines_skipped = None
        self._header = None
        self._delimiter = None
        self._delimiter_value = None
        self._column_information = None
        self._preprocessing_rules = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this FileSpecificationTemplate.
        The globally unique identifier for the object.

        :return: The id of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this FileSpecificationTemplate.
        The globally unique identifier for the object.

        :param id: The id of this FileSpecificationTemplate.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this FileSpecificationTemplate.
        The name of the File Specification template.

        :return: The name of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this FileSpecificationTemplate.
        The name of the File Specification template.

        :param name: The name of this FileSpecificationTemplate.
        :type: str
        """
        

        self._name = name

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this FileSpecificationTemplate.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this FileSpecificationTemplate.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this FileSpecificationTemplate.
        Creation time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this FileSpecificationTemplate.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this FileSpecificationTemplate.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this FileSpecificationTemplate.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this FileSpecificationTemplate.
        Last modified time of the entity. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this FileSpecificationTemplate.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def version(self) -> int:
        """
        Gets the version of this FileSpecificationTemplate.
        Required for updates, must match the version number of the most recent update

        :return: The version of this FileSpecificationTemplate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int) -> None:
        """
        Sets the version of this FileSpecificationTemplate.
        Required for updates, must match the version number of the most recent update

        :param version: The version of this FileSpecificationTemplate.
        :type: int
        """
        

        self._version = version

    @property
    def description(self) -> str:
        """
        Gets the description of this FileSpecificationTemplate.
        Description of the file specification template

        :return: The description of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        """
        Sets the description of this FileSpecificationTemplate.
        Description of the file specification template

        :param description: The description of this FileSpecificationTemplate.
        :type: str
        """
        

        self._description = description

    @property
    def format(self) -> str:
        """
        Gets the format of this FileSpecificationTemplate.
        File format

        :return: The format of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format: str) -> None:
        """
        Sets the format of this FileSpecificationTemplate.
        File format

        :param format: The format of this FileSpecificationTemplate.
        :type: str
        """
        if isinstance(format, int):
            format = str(format)
        allowed_values = ["FixedLength", "Delimited"]
        if format.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for format -> " + format)
            self._format = "outdated_sdk_version"
        else:
            self._format = format

    @property
    def number_of_heading_lines_skipped(self) -> int:
        """
        Gets the number_of_heading_lines_skipped of this FileSpecificationTemplate.
        Number of heading lines to be skipped

        :return: The number_of_heading_lines_skipped of this FileSpecificationTemplate.
        :rtype: int
        """
        return self._number_of_heading_lines_skipped

    @number_of_heading_lines_skipped.setter
    def number_of_heading_lines_skipped(self, number_of_heading_lines_skipped: int) -> None:
        """
        Sets the number_of_heading_lines_skipped of this FileSpecificationTemplate.
        Number of heading lines to be skipped

        :param number_of_heading_lines_skipped: The number_of_heading_lines_skipped of this FileSpecificationTemplate.
        :type: int
        """
        

        self._number_of_heading_lines_skipped = number_of_heading_lines_skipped

    @property
    def number_of_trailing_lines_skipped(self) -> int:
        """
        Gets the number_of_trailing_lines_skipped of this FileSpecificationTemplate.
        Number of trailing lines to be skipped

        :return: The number_of_trailing_lines_skipped of this FileSpecificationTemplate.
        :rtype: int
        """
        return self._number_of_trailing_lines_skipped

    @number_of_trailing_lines_skipped.setter
    def number_of_trailing_lines_skipped(self, number_of_trailing_lines_skipped: int) -> None:
        """
        Sets the number_of_trailing_lines_skipped of this FileSpecificationTemplate.
        Number of trailing lines to be skipped

        :param number_of_trailing_lines_skipped: The number_of_trailing_lines_skipped of this FileSpecificationTemplate.
        :type: int
        """
        

        self._number_of_trailing_lines_skipped = number_of_trailing_lines_skipped

    @property
    def header(self) -> bool:
        """
        Gets the header of this FileSpecificationTemplate.
        If true indicates that delimited file has a header row, which can provide column names

        :return: The header of this FileSpecificationTemplate.
        :rtype: bool
        """
        return self._header

    @header.setter
    def header(self, header: bool) -> None:
        """
        Sets the header of this FileSpecificationTemplate.
        If true indicates that delimited file has a header row, which can provide column names

        :param header: The header of this FileSpecificationTemplate.
        :type: bool
        """
        

        self._header = header

    @property
    def delimiter(self) -> str:
        """
        Gets the delimiter of this FileSpecificationTemplate.
        Kind of delimiter

        :return: The delimiter of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter: str) -> None:
        """
        Sets the delimiter of this FileSpecificationTemplate.
        Kind of delimiter

        :param delimiter: The delimiter of this FileSpecificationTemplate.
        :type: str
        """
        if isinstance(delimiter, int):
            delimiter = str(delimiter)
        allowed_values = ["Comma", "Pipe", "Colon", "Tab", "Semicolon", "Custom"]
        if delimiter.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for delimiter -> " + delimiter)
            self._delimiter = "outdated_sdk_version"
        else:
            self._delimiter = delimiter

    @property
    def delimiter_value(self) -> str:
        """
        Gets the delimiter_value of this FileSpecificationTemplate.
        Delimiter character, used only when delimiter=\"Custom\"

        :return: The delimiter_value of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._delimiter_value

    @delimiter_value.setter
    def delimiter_value(self, delimiter_value: str) -> None:
        """
        Sets the delimiter_value of this FileSpecificationTemplate.
        Delimiter character, used only when delimiter=\"Custom\"

        :param delimiter_value: The delimiter_value of this FileSpecificationTemplate.
        :type: str
        """
        

        self._delimiter_value = delimiter_value

    @property
    def column_information(self) -> List['Column']:
        """
        Gets the column_information of this FileSpecificationTemplate.
        Columns specification

        :return: The column_information of this FileSpecificationTemplate.
        :rtype: list[Column]
        """
        return self._column_information

    @column_information.setter
    def column_information(self, column_information: List['Column']) -> None:
        """
        Sets the column_information of this FileSpecificationTemplate.
        Columns specification

        :param column_information: The column_information of this FileSpecificationTemplate.
        :type: list[Column]
        """
        

        self._column_information = column_information

    @property
    def preprocessing_rules(self) -> List['PreprocessingRule']:
        """
        Gets the preprocessing_rules of this FileSpecificationTemplate.
        Preprocessing rules

        :return: The preprocessing_rules of this FileSpecificationTemplate.
        :rtype: list[PreprocessingRule]
        """
        return self._preprocessing_rules

    @preprocessing_rules.setter
    def preprocessing_rules(self, preprocessing_rules: List['PreprocessingRule']) -> None:
        """
        Sets the preprocessing_rules of this FileSpecificationTemplate.
        Preprocessing rules

        :param preprocessing_rules: The preprocessing_rules of this FileSpecificationTemplate.
        :type: list[PreprocessingRule]
        """
        

        self._preprocessing_rules = preprocessing_rules

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this FileSpecificationTemplate.
        The URI for this object

        :return: The self_uri of this FileSpecificationTemplate.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this FileSpecificationTemplate.
        The URI for this object

        :param self_uri: The self_uri of this FileSpecificationTemplate.
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
