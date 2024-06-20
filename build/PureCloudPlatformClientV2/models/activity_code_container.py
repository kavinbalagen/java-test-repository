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
    from . import ActivityCode
    from . import WfmVersionedEntityMetadata

class ActivityCodeContainer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ActivityCodeContainer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_codes': 'dict(str, ActivityCode)',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'activity_codes': 'activityCodes',
            'metadata': 'metadata'
        }

        self._activity_codes = None
        self._metadata = None

    @property
    def activity_codes(self) -> Dict[str, 'ActivityCode']:
        """
        Gets the activity_codes of this ActivityCodeContainer.
        Map of activity code id to activity code

        :return: The activity_codes of this ActivityCodeContainer.
        :rtype: dict(str, ActivityCode)
        """
        return self._activity_codes

    @activity_codes.setter
    def activity_codes(self, activity_codes: Dict[str, 'ActivityCode']) -> None:
        """
        Sets the activity_codes of this ActivityCodeContainer.
        Map of activity code id to activity code

        :param activity_codes: The activity_codes of this ActivityCodeContainer.
        :type: dict(str, ActivityCode)
        """
        

        self._activity_codes = activity_codes

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this ActivityCodeContainer.
        Version metadata for the associated management unit's list of activity codes

        :return: The metadata of this ActivityCodeContainer.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this ActivityCodeContainer.
        Version metadata for the associated management unit's list of activity codes

        :param metadata: The metadata of this ActivityCodeContainer.
        :type: WfmVersionedEntityMetadata
        """
        

        self._metadata = metadata

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

