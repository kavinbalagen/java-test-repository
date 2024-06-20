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


class MediaRegions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MediaRegions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aws_home_region': 'str',
            'aws_core_regions': 'list[str]',
            'aws_satellite_regions': 'list[str]'
        }

        self.attribute_map = {
            'aws_home_region': 'awsHomeRegion',
            'aws_core_regions': 'awsCoreRegions',
            'aws_satellite_regions': 'awsSatelliteRegions'
        }

        self._aws_home_region = None
        self._aws_core_regions = None
        self._aws_satellite_regions = None

    @property
    def aws_home_region(self) -> str:
        """
        Gets the aws_home_region of this MediaRegions.
        The AWS region your organization is in.

        :return: The aws_home_region of this MediaRegions.
        :rtype: str
        """
        return self._aws_home_region

    @aws_home_region.setter
    def aws_home_region(self, aws_home_region: str) -> None:
        """
        Sets the aws_home_region of this MediaRegions.
        The AWS region your organization is in.

        :param aws_home_region: The aws_home_region of this MediaRegions.
        :type: str
        """
        

        self._aws_home_region = aws_home_region

    @property
    def aws_core_regions(self) -> List[str]:
        """
        Gets the aws_core_regions of this MediaRegions.
        The list of AWS regions to which Genesys Cloud is deployed with full functionality including media streaming.

        :return: The aws_core_regions of this MediaRegions.
        :rtype: list[str]
        """
        return self._aws_core_regions

    @aws_core_regions.setter
    def aws_core_regions(self, aws_core_regions: List[str]) -> None:
        """
        Sets the aws_core_regions of this MediaRegions.
        The list of AWS regions to which Genesys Cloud is deployed with full functionality including media streaming.

        :param aws_core_regions: The aws_core_regions of this MediaRegions.
        :type: list[str]
        """
        

        self._aws_core_regions = aws_core_regions

    @property
    def aws_satellite_regions(self) -> List[str]:
        """
        Gets the aws_satellite_regions of this MediaRegions.
        The list of AWS regions that Genesys Cloud uses only for media streaming.

        :return: The aws_satellite_regions of this MediaRegions.
        :rtype: list[str]
        """
        return self._aws_satellite_regions

    @aws_satellite_regions.setter
    def aws_satellite_regions(self, aws_satellite_regions: List[str]) -> None:
        """
        Sets the aws_satellite_regions of this MediaRegions.
        The list of AWS regions that Genesys Cloud uses only for media streaming.

        :param aws_satellite_regions: The aws_satellite_regions of this MediaRegions.
        :type: list[str]
        """
        

        self._aws_satellite_regions = aws_satellite_regions

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

