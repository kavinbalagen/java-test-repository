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
    from . import AdherenceSettings
    from . import SchedulingSettingsResponse
    from . import ShiftTradeSettings
    from . import ShortTermForecastingSettings
    from . import TimeOffRequestSettings
    from . import WfmVersionedEntityMetadata

class ManagementUnitSettingsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ManagementUnitSettingsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'adherence': 'AdherenceSettings',
            'short_term_forecasting': 'ShortTermForecastingSettings',
            'time_off': 'TimeOffRequestSettings',
            'scheduling': 'SchedulingSettingsResponse',
            'shift_trading': 'ShiftTradeSettings',
            'metadata': 'WfmVersionedEntityMetadata'
        }

        self.attribute_map = {
            'adherence': 'adherence',
            'short_term_forecasting': 'shortTermForecasting',
            'time_off': 'timeOff',
            'scheduling': 'scheduling',
            'shift_trading': 'shiftTrading',
            'metadata': 'metadata'
        }

        self._adherence = None
        self._short_term_forecasting = None
        self._time_off = None
        self._scheduling = None
        self._shift_trading = None
        self._metadata = None

    @property
    def adherence(self) -> 'AdherenceSettings':
        """
        Gets the adherence of this ManagementUnitSettingsResponse.
        Adherence settings for this management unit

        :return: The adherence of this ManagementUnitSettingsResponse.
        :rtype: AdherenceSettings
        """
        return self._adherence

    @adherence.setter
    def adherence(self, adherence: 'AdherenceSettings') -> None:
        """
        Sets the adherence of this ManagementUnitSettingsResponse.
        Adherence settings for this management unit

        :param adherence: The adherence of this ManagementUnitSettingsResponse.
        :type: AdherenceSettings
        """
        

        self._adherence = adherence

    @property
    def short_term_forecasting(self) -> 'ShortTermForecastingSettings':
        """
        Gets the short_term_forecasting of this ManagementUnitSettingsResponse.
        Short term forecasting settings for this management unit

        :return: The short_term_forecasting of this ManagementUnitSettingsResponse.
        :rtype: ShortTermForecastingSettings
        """
        return self._short_term_forecasting

    @short_term_forecasting.setter
    def short_term_forecasting(self, short_term_forecasting: 'ShortTermForecastingSettings') -> None:
        """
        Sets the short_term_forecasting of this ManagementUnitSettingsResponse.
        Short term forecasting settings for this management unit

        :param short_term_forecasting: The short_term_forecasting of this ManagementUnitSettingsResponse.
        :type: ShortTermForecastingSettings
        """
        

        self._short_term_forecasting = short_term_forecasting

    @property
    def time_off(self) -> 'TimeOffRequestSettings':
        """
        Gets the time_off of this ManagementUnitSettingsResponse.
        Time off request settings for this management unit

        :return: The time_off of this ManagementUnitSettingsResponse.
        :rtype: TimeOffRequestSettings
        """
        return self._time_off

    @time_off.setter
    def time_off(self, time_off: 'TimeOffRequestSettings') -> None:
        """
        Sets the time_off of this ManagementUnitSettingsResponse.
        Time off request settings for this management unit

        :param time_off: The time_off of this ManagementUnitSettingsResponse.
        :type: TimeOffRequestSettings
        """
        

        self._time_off = time_off

    @property
    def scheduling(self) -> 'SchedulingSettingsResponse':
        """
        Gets the scheduling of this ManagementUnitSettingsResponse.
        Scheduling settings for this management unit. These settings are only available if you have the permission wfm:managementUnit:view

        :return: The scheduling of this ManagementUnitSettingsResponse.
        :rtype: SchedulingSettingsResponse
        """
        return self._scheduling

    @scheduling.setter
    def scheduling(self, scheduling: 'SchedulingSettingsResponse') -> None:
        """
        Sets the scheduling of this ManagementUnitSettingsResponse.
        Scheduling settings for this management unit. These settings are only available if you have the permission wfm:managementUnit:view

        :param scheduling: The scheduling of this ManagementUnitSettingsResponse.
        :type: SchedulingSettingsResponse
        """
        

        self._scheduling = scheduling

    @property
    def shift_trading(self) -> 'ShiftTradeSettings':
        """
        Gets the shift_trading of this ManagementUnitSettingsResponse.
        Shift trade settings for this management unit

        :return: The shift_trading of this ManagementUnitSettingsResponse.
        :rtype: ShiftTradeSettings
        """
        return self._shift_trading

    @shift_trading.setter
    def shift_trading(self, shift_trading: 'ShiftTradeSettings') -> None:
        """
        Sets the shift_trading of this ManagementUnitSettingsResponse.
        Shift trade settings for this management unit

        :param shift_trading: The shift_trading of this ManagementUnitSettingsResponse.
        :type: ShiftTradeSettings
        """
        

        self._shift_trading = shift_trading

    @property
    def metadata(self) -> 'WfmVersionedEntityMetadata':
        """
        Gets the metadata of this ManagementUnitSettingsResponse.
        Version info metadata for the associated management unit

        :return: The metadata of this ManagementUnitSettingsResponse.
        :rtype: WfmVersionedEntityMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: 'WfmVersionedEntityMetadata') -> None:
        """
        Sets the metadata of this ManagementUnitSettingsResponse.
        Version info metadata for the associated management unit

        :param metadata: The metadata of this ManagementUnitSettingsResponse.
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

