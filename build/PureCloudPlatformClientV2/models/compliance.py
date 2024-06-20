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
    from . import HelpSettings
    from . import OptInSettings
    from . import StopSettings

class Compliance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Compliance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'stop_settings': 'list[StopSettings]',
            'opt_in_settings': 'list[OptInSettings]',
            'help_settings': 'list[HelpSettings]'
        }

        self.attribute_map = {
            'stop_settings': 'stopSettings',
            'opt_in_settings': 'optInSettings',
            'help_settings': 'helpSettings'
        }

        self._stop_settings = None
        self._opt_in_settings = None
        self._help_settings = None

    @property
    def stop_settings(self) -> List['StopSettings']:
        """
        Gets the stop_settings of this Compliance.
        List of configurations for 'StopSettings' compliance

        :return: The stop_settings of this Compliance.
        :rtype: list[StopSettings]
        """
        return self._stop_settings

    @stop_settings.setter
    def stop_settings(self, stop_settings: List['StopSettings']) -> None:
        """
        Sets the stop_settings of this Compliance.
        List of configurations for 'StopSettings' compliance

        :param stop_settings: The stop_settings of this Compliance.
        :type: list[StopSettings]
        """
        

        self._stop_settings = stop_settings

    @property
    def opt_in_settings(self) -> List['OptInSettings']:
        """
        Gets the opt_in_settings of this Compliance.
        List of configurations for 'OptInSettings' compliance

        :return: The opt_in_settings of this Compliance.
        :rtype: list[OptInSettings]
        """
        return self._opt_in_settings

    @opt_in_settings.setter
    def opt_in_settings(self, opt_in_settings: List['OptInSettings']) -> None:
        """
        Sets the opt_in_settings of this Compliance.
        List of configurations for 'OptInSettings' compliance

        :param opt_in_settings: The opt_in_settings of this Compliance.
        :type: list[OptInSettings]
        """
        

        self._opt_in_settings = opt_in_settings

    @property
    def help_settings(self) -> List['HelpSettings']:
        """
        Gets the help_settings of this Compliance.
        List of configurations for 'HelpSettings' compliance

        :return: The help_settings of this Compliance.
        :rtype: list[HelpSettings]
        """
        return self._help_settings

    @help_settings.setter
    def help_settings(self, help_settings: List['HelpSettings']) -> None:
        """
        Sets the help_settings of this Compliance.
        List of configurations for 'HelpSettings' compliance

        :param help_settings: The help_settings of this Compliance.
        :type: list[HelpSettings]
        """
        

        self._help_settings = help_settings

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

