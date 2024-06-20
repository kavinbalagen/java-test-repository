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
    from . import AdherenceExplanationNotification
    from . import AlternativeShiftNotification
    from . import ShiftTradeNotification
    from . import TimeOffRequestNotification

class WfmUserNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WfmUserNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'mutable_group_id': 'str',
            'timestamp': 'datetime',
            'type': 'str',
            'shift_trade': 'ShiftTradeNotification',
            'time_off_request': 'TimeOffRequestNotification',
            'adherence_explanation': 'AdherenceExplanationNotification',
            'alternative_shift': 'AlternativeShiftNotification',
            'marked_as_read': 'bool',
            'agent_notification': 'bool',
            'other_notification_ids_in_group': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'mutable_group_id': 'mutableGroupId',
            'timestamp': 'timestamp',
            'type': 'type',
            'shift_trade': 'shiftTrade',
            'time_off_request': 'timeOffRequest',
            'adherence_explanation': 'adherenceExplanation',
            'alternative_shift': 'alternativeShift',
            'marked_as_read': 'markedAsRead',
            'agent_notification': 'agentNotification',
            'other_notification_ids_in_group': 'otherNotificationIdsInGroup'
        }

        self._id = None
        self._mutable_group_id = None
        self._timestamp = None
        self._type = None
        self._shift_trade = None
        self._time_off_request = None
        self._adherence_explanation = None
        self._alternative_shift = None
        self._marked_as_read = None
        self._agent_notification = None
        self._other_notification_ids_in_group = None

    @property
    def id(self) -> str:
        """
        Gets the id of this WfmUserNotification.
        The immutable globally unique identifier for the object.

        :return: The id of this WfmUserNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this WfmUserNotification.
        The immutable globally unique identifier for the object.

        :param id: The id of this WfmUserNotification.
        :type: str
        """
        

        self._id = id

    @property
    def mutable_group_id(self) -> str:
        """
        Gets the mutable_group_id of this WfmUserNotification.
        The group ID of the notification (mutable, may change  on update)

        :return: The mutable_group_id of this WfmUserNotification.
        :rtype: str
        """
        return self._mutable_group_id

    @mutable_group_id.setter
    def mutable_group_id(self, mutable_group_id: str) -> None:
        """
        Sets the mutable_group_id of this WfmUserNotification.
        The group ID of the notification (mutable, may change  on update)

        :param mutable_group_id: The mutable_group_id of this WfmUserNotification.
        :type: str
        """
        

        self._mutable_group_id = mutable_group_id

    @property
    def timestamp(self) -> datetime:
        """
        Gets the timestamp of this WfmUserNotification.
        The timestamp for this notification. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The timestamp of this WfmUserNotification.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime) -> None:
        """
        Sets the timestamp of this WfmUserNotification.
        The timestamp for this notification. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param timestamp: The timestamp of this WfmUserNotification.
        :type: datetime
        """
        

        self._timestamp = timestamp

    @property
    def type(self) -> str:
        """
        Gets the type of this WfmUserNotification.
        The type of this notification

        :return: The type of this WfmUserNotification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this WfmUserNotification.
        The type of this notification

        :param type: The type of this WfmUserNotification.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["AdherenceExplanation", "ShiftTrade", "TimeOffRequest", "AlternativeShift"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def shift_trade(self) -> 'ShiftTradeNotification':
        """
        Gets the shift_trade of this WfmUserNotification.
        A shift trade notification.  Only set if type == ShiftTrade

        :return: The shift_trade of this WfmUserNotification.
        :rtype: ShiftTradeNotification
        """
        return self._shift_trade

    @shift_trade.setter
    def shift_trade(self, shift_trade: 'ShiftTradeNotification') -> None:
        """
        Sets the shift_trade of this WfmUserNotification.
        A shift trade notification.  Only set if type == ShiftTrade

        :param shift_trade: The shift_trade of this WfmUserNotification.
        :type: ShiftTradeNotification
        """
        

        self._shift_trade = shift_trade

    @property
    def time_off_request(self) -> 'TimeOffRequestNotification':
        """
        Gets the time_off_request of this WfmUserNotification.
        A time off request notification.  Only set if type == TimeOffRequest

        :return: The time_off_request of this WfmUserNotification.
        :rtype: TimeOffRequestNotification
        """
        return self._time_off_request

    @time_off_request.setter
    def time_off_request(self, time_off_request: 'TimeOffRequestNotification') -> None:
        """
        Sets the time_off_request of this WfmUserNotification.
        A time off request notification.  Only set if type == TimeOffRequest

        :param time_off_request: The time_off_request of this WfmUserNotification.
        :type: TimeOffRequestNotification
        """
        

        self._time_off_request = time_off_request

    @property
    def adherence_explanation(self) -> 'AdherenceExplanationNotification':
        """
        Gets the adherence_explanation of this WfmUserNotification.
        An adherence explanation notification.  Only set if type == AdherenceExplanation

        :return: The adherence_explanation of this WfmUserNotification.
        :rtype: AdherenceExplanationNotification
        """
        return self._adherence_explanation

    @adherence_explanation.setter
    def adherence_explanation(self, adherence_explanation: 'AdherenceExplanationNotification') -> None:
        """
        Sets the adherence_explanation of this WfmUserNotification.
        An adherence explanation notification.  Only set if type == AdherenceExplanation

        :param adherence_explanation: The adherence_explanation of this WfmUserNotification.
        :type: AdherenceExplanationNotification
        """
        

        self._adherence_explanation = adherence_explanation

    @property
    def alternative_shift(self) -> 'AlternativeShiftNotification':
        """
        Gets the alternative_shift of this WfmUserNotification.
        An alternative shift trade notification.  Only set if type == AlternativeShift

        :return: The alternative_shift of this WfmUserNotification.
        :rtype: AlternativeShiftNotification
        """
        return self._alternative_shift

    @alternative_shift.setter
    def alternative_shift(self, alternative_shift: 'AlternativeShiftNotification') -> None:
        """
        Sets the alternative_shift of this WfmUserNotification.
        An alternative shift trade notification.  Only set if type == AlternativeShift

        :param alternative_shift: The alternative_shift of this WfmUserNotification.
        :type: AlternativeShiftNotification
        """
        

        self._alternative_shift = alternative_shift

    @property
    def marked_as_read(self) -> bool:
        """
        Gets the marked_as_read of this WfmUserNotification.
        Whether this notification has been marked \"read\"

        :return: The marked_as_read of this WfmUserNotification.
        :rtype: bool
        """
        return self._marked_as_read

    @marked_as_read.setter
    def marked_as_read(self, marked_as_read: bool) -> None:
        """
        Sets the marked_as_read of this WfmUserNotification.
        Whether this notification has been marked \"read\"

        :param marked_as_read: The marked_as_read of this WfmUserNotification.
        :type: bool
        """
        

        self._marked_as_read = marked_as_read

    @property
    def agent_notification(self) -> bool:
        """
        Gets the agent_notification of this WfmUserNotification.
        Whether this notification is for an agent

        :return: The agent_notification of this WfmUserNotification.
        :rtype: bool
        """
        return self._agent_notification

    @agent_notification.setter
    def agent_notification(self, agent_notification: bool) -> None:
        """
        Sets the agent_notification of this WfmUserNotification.
        Whether this notification is for an agent

        :param agent_notification: The agent_notification of this WfmUserNotification.
        :type: bool
        """
        

        self._agent_notification = agent_notification

    @property
    def other_notification_ids_in_group(self) -> List[str]:
        """
        Gets the other_notification_ids_in_group of this WfmUserNotification.
        Other notification IDs in group.  This field is only populated in real-time notifications

        :return: The other_notification_ids_in_group of this WfmUserNotification.
        :rtype: list[str]
        """
        return self._other_notification_ids_in_group

    @other_notification_ids_in_group.setter
    def other_notification_ids_in_group(self, other_notification_ids_in_group: List[str]) -> None:
        """
        Sets the other_notification_ids_in_group of this WfmUserNotification.
        Other notification IDs in group.  This field is only populated in real-time notifications

        :param other_notification_ids_in_group: The other_notification_ids_in_group of this WfmUserNotification.
        :type: list[str]
        """
        

        self._other_notification_ids_in_group = other_notification_ids_in_group

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
