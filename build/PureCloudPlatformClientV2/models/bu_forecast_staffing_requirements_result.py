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
    from . import StaffingRequirementsPlanningGroupData

class BuForecastStaffingRequirementsResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        BuForecastStaffingRequirementsResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'week_number': 'int',
            'download_url': 'str',
            'download_url_expiration_date': 'datetime',
            'planning_group_staffing_requirements': 'list[StaffingRequirementsPlanningGroupData]'
        }

        self.attribute_map = {
            'week_number': 'weekNumber',
            'download_url': 'downloadUrl',
            'download_url_expiration_date': 'downloadUrlExpirationDate',
            'planning_group_staffing_requirements': 'planningGroupStaffingRequirements'
        }

        self._week_number = None
        self._download_url = None
        self._download_url_expiration_date = None
        self._planning_group_staffing_requirements = None

    @property
    def week_number(self) -> int:
        """
        Gets the week_number of this BuForecastStaffingRequirementsResult.
        The week number represented by this response

        :return: The week_number of this BuForecastStaffingRequirementsResult.
        :rtype: int
        """
        return self._week_number

    @week_number.setter
    def week_number(self, week_number: int) -> None:
        """
        Sets the week_number of this BuForecastStaffingRequirementsResult.
        The week number represented by this response

        :param week_number: The week_number of this BuForecastStaffingRequirementsResult.
        :type: int
        """
        

        self._week_number = week_number

    @property
    def download_url(self) -> str:
        """
        Gets the download_url of this BuForecastStaffingRequirementsResult.
        The url to get the requirements results for this week

        :return: The download_url of this BuForecastStaffingRequirementsResult.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url: str) -> None:
        """
        Sets the download_url of this BuForecastStaffingRequirementsResult.
        The url to get the requirements results for this week

        :param download_url: The download_url of this BuForecastStaffingRequirementsResult.
        :type: str
        """
        

        self._download_url = download_url

    @property
    def download_url_expiration_date(self) -> datetime:
        """
        Gets the download_url_expiration_date of this BuForecastStaffingRequirementsResult.
        The expiration date of the download url, as an ISO-8601 string

        :return: The download_url_expiration_date of this BuForecastStaffingRequirementsResult.
        :rtype: datetime
        """
        return self._download_url_expiration_date

    @download_url_expiration_date.setter
    def download_url_expiration_date(self, download_url_expiration_date: datetime) -> None:
        """
        Sets the download_url_expiration_date of this BuForecastStaffingRequirementsResult.
        The expiration date of the download url, as an ISO-8601 string

        :param download_url_expiration_date: The download_url_expiration_date of this BuForecastStaffingRequirementsResult.
        :type: datetime
        """
        

        self._download_url_expiration_date = download_url_expiration_date

    @property
    def planning_group_staffing_requirements(self) -> List['StaffingRequirementsPlanningGroupData']:
        """
        Gets the planning_group_staffing_requirements of this BuForecastStaffingRequirementsResult.
        Results will always come via downloadUrl, however the schema is included for documentation

        :return: The planning_group_staffing_requirements of this BuForecastStaffingRequirementsResult.
        :rtype: list[StaffingRequirementsPlanningGroupData]
        """
        return self._planning_group_staffing_requirements

    @planning_group_staffing_requirements.setter
    def planning_group_staffing_requirements(self, planning_group_staffing_requirements: List['StaffingRequirementsPlanningGroupData']) -> None:
        """
        Sets the planning_group_staffing_requirements of this BuForecastStaffingRequirementsResult.
        Results will always come via downloadUrl, however the schema is included for documentation

        :param planning_group_staffing_requirements: The planning_group_staffing_requirements of this BuForecastStaffingRequirementsResult.
        :type: list[StaffingRequirementsPlanningGroupData]
        """
        

        self._planning_group_staffing_requirements = planning_group_staffing_requirements

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
