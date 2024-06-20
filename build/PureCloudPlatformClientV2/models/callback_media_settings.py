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
    from . import BaseMediaSettings
    from . import ServiceLevel

class CallbackMediaSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CallbackMediaSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enable_auto_answer': 'bool',
            'alerting_timeout_seconds': 'int',
            'service_level': 'ServiceLevel',
            'auto_answer_alert_tone_seconds': 'float',
            'manual_answer_alert_tone_seconds': 'float',
            'sub_type_settings': 'dict(str, BaseMediaSettings)',
            'enable_auto_dial_and_end': 'bool',
            'auto_dial_delay_seconds': 'int',
            'auto_end_delay_seconds': 'int'
        }

        self.attribute_map = {
            'enable_auto_answer': 'enableAutoAnswer',
            'alerting_timeout_seconds': 'alertingTimeoutSeconds',
            'service_level': 'serviceLevel',
            'auto_answer_alert_tone_seconds': 'autoAnswerAlertToneSeconds',
            'manual_answer_alert_tone_seconds': 'manualAnswerAlertToneSeconds',
            'sub_type_settings': 'subTypeSettings',
            'enable_auto_dial_and_end': 'enableAutoDialAndEnd',
            'auto_dial_delay_seconds': 'autoDialDelaySeconds',
            'auto_end_delay_seconds': 'autoEndDelaySeconds'
        }

        self._enable_auto_answer = None
        self._alerting_timeout_seconds = None
        self._service_level = None
        self._auto_answer_alert_tone_seconds = None
        self._manual_answer_alert_tone_seconds = None
        self._sub_type_settings = None
        self._enable_auto_dial_and_end = None
        self._auto_dial_delay_seconds = None
        self._auto_end_delay_seconds = None

    @property
    def enable_auto_answer(self) -> bool:
        """
        Gets the enable_auto_answer of this CallbackMediaSettings.
        Indicates if auto-answer is enabled for the given media type or subtype (default is false).  Subtype settings take precedence over media type settings.

        :return: The enable_auto_answer of this CallbackMediaSettings.
        :rtype: bool
        """
        return self._enable_auto_answer

    @enable_auto_answer.setter
    def enable_auto_answer(self, enable_auto_answer: bool) -> None:
        """
        Sets the enable_auto_answer of this CallbackMediaSettings.
        Indicates if auto-answer is enabled for the given media type or subtype (default is false).  Subtype settings take precedence over media type settings.

        :param enable_auto_answer: The enable_auto_answer of this CallbackMediaSettings.
        :type: bool
        """
        

        self._enable_auto_answer = enable_auto_answer

    @property
    def alerting_timeout_seconds(self) -> int:
        """
        Gets the alerting_timeout_seconds of this CallbackMediaSettings.
        The alerting timeout for the media type, in seconds

        :return: The alerting_timeout_seconds of this CallbackMediaSettings.
        :rtype: int
        """
        return self._alerting_timeout_seconds

    @alerting_timeout_seconds.setter
    def alerting_timeout_seconds(self, alerting_timeout_seconds: int) -> None:
        """
        Sets the alerting_timeout_seconds of this CallbackMediaSettings.
        The alerting timeout for the media type, in seconds

        :param alerting_timeout_seconds: The alerting_timeout_seconds of this CallbackMediaSettings.
        :type: int
        """
        

        self._alerting_timeout_seconds = alerting_timeout_seconds

    @property
    def service_level(self) -> 'ServiceLevel':
        """
        Gets the service_level of this CallbackMediaSettings.
        The targeted service level for the media type

        :return: The service_level of this CallbackMediaSettings.
        :rtype: ServiceLevel
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level: 'ServiceLevel') -> None:
        """
        Sets the service_level of this CallbackMediaSettings.
        The targeted service level for the media type

        :param service_level: The service_level of this CallbackMediaSettings.
        :type: ServiceLevel
        """
        

        self._service_level = service_level

    @property
    def auto_answer_alert_tone_seconds(self) -> float:
        """
        Gets the auto_answer_alert_tone_seconds of this CallbackMediaSettings.
        How long to play the alerting tone for an auto-answer interaction

        :return: The auto_answer_alert_tone_seconds of this CallbackMediaSettings.
        :rtype: float
        """
        return self._auto_answer_alert_tone_seconds

    @auto_answer_alert_tone_seconds.setter
    def auto_answer_alert_tone_seconds(self, auto_answer_alert_tone_seconds: float) -> None:
        """
        Sets the auto_answer_alert_tone_seconds of this CallbackMediaSettings.
        How long to play the alerting tone for an auto-answer interaction

        :param auto_answer_alert_tone_seconds: The auto_answer_alert_tone_seconds of this CallbackMediaSettings.
        :type: float
        """
        

        self._auto_answer_alert_tone_seconds = auto_answer_alert_tone_seconds

    @property
    def manual_answer_alert_tone_seconds(self) -> float:
        """
        Gets the manual_answer_alert_tone_seconds of this CallbackMediaSettings.
        How long to play the alerting tone for a manual-answer interaction

        :return: The manual_answer_alert_tone_seconds of this CallbackMediaSettings.
        :rtype: float
        """
        return self._manual_answer_alert_tone_seconds

    @manual_answer_alert_tone_seconds.setter
    def manual_answer_alert_tone_seconds(self, manual_answer_alert_tone_seconds: float) -> None:
        """
        Sets the manual_answer_alert_tone_seconds of this CallbackMediaSettings.
        How long to play the alerting tone for a manual-answer interaction

        :param manual_answer_alert_tone_seconds: The manual_answer_alert_tone_seconds of this CallbackMediaSettings.
        :type: float
        """
        

        self._manual_answer_alert_tone_seconds = manual_answer_alert_tone_seconds

    @property
    def sub_type_settings(self) -> Dict[str, 'BaseMediaSettings']:
        """
        Gets the sub_type_settings of this CallbackMediaSettings.
        Map of media subtype to media subtype specific settings.

        :return: The sub_type_settings of this CallbackMediaSettings.
        :rtype: dict(str, BaseMediaSettings)
        """
        return self._sub_type_settings

    @sub_type_settings.setter
    def sub_type_settings(self, sub_type_settings: Dict[str, 'BaseMediaSettings']) -> None:
        """
        Sets the sub_type_settings of this CallbackMediaSettings.
        Map of media subtype to media subtype specific settings.

        :param sub_type_settings: The sub_type_settings of this CallbackMediaSettings.
        :type: dict(str, BaseMediaSettings)
        """
        

        self._sub_type_settings = sub_type_settings

    @property
    def enable_auto_dial_and_end(self) -> bool:
        """
        Gets the enable_auto_dial_and_end of this CallbackMediaSettings.
        Flag to enable Auto-Dial and Auto-End automation for callbacks on this queue.

        :return: The enable_auto_dial_and_end of this CallbackMediaSettings.
        :rtype: bool
        """
        return self._enable_auto_dial_and_end

    @enable_auto_dial_and_end.setter
    def enable_auto_dial_and_end(self, enable_auto_dial_and_end: bool) -> None:
        """
        Sets the enable_auto_dial_and_end of this CallbackMediaSettings.
        Flag to enable Auto-Dial and Auto-End automation for callbacks on this queue.

        :param enable_auto_dial_and_end: The enable_auto_dial_and_end of this CallbackMediaSettings.
        :type: bool
        """
        

        self._enable_auto_dial_and_end = enable_auto_dial_and_end

    @property
    def auto_dial_delay_seconds(self) -> int:
        """
        Gets the auto_dial_delay_seconds of this CallbackMediaSettings.
        Time in seconds after agent connects to callback before outgoing call is auto-dialed. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds.

        :return: The auto_dial_delay_seconds of this CallbackMediaSettings.
        :rtype: int
        """
        return self._auto_dial_delay_seconds

    @auto_dial_delay_seconds.setter
    def auto_dial_delay_seconds(self, auto_dial_delay_seconds: int) -> None:
        """
        Sets the auto_dial_delay_seconds of this CallbackMediaSettings.
        Time in seconds after agent connects to callback before outgoing call is auto-dialed. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds.

        :param auto_dial_delay_seconds: The auto_dial_delay_seconds of this CallbackMediaSettings.
        :type: int
        """
        

        self._auto_dial_delay_seconds = auto_dial_delay_seconds

    @property
    def auto_end_delay_seconds(self) -> int:
        """
        Gets the auto_end_delay_seconds of this CallbackMediaSettings.
        Time in seconds after agent disconnects from the outgoing call before the encasing callback is auto-ended. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds.

        :return: The auto_end_delay_seconds of this CallbackMediaSettings.
        :rtype: int
        """
        return self._auto_end_delay_seconds

    @auto_end_delay_seconds.setter
    def auto_end_delay_seconds(self, auto_end_delay_seconds: int) -> None:
        """
        Sets the auto_end_delay_seconds of this CallbackMediaSettings.
        Time in seconds after agent disconnects from the outgoing call before the encasing callback is auto-ended. Allowable values in range 0 - 1200 seconds. Defaults to 300 seconds.

        :param auto_end_delay_seconds: The auto_end_delay_seconds of this CallbackMediaSettings.
        :type: int
        """
        

        self._auto_end_delay_seconds = auto_end_delay_seconds

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
