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
    from . import CoachingSlot
    from . import UserAvailableTimes
    from . import WfmScheduleActivity

class CoachingSlotsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CoachingSlotsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'suggested_slots': 'list[CoachingSlot]',
            'attendee_schedules': 'list[UserAvailableTimes]',
            'facilitator_schedules': 'list[UserAvailableTimes]',
            'wfm_schedule_activities': 'list[WfmScheduleActivity]'
        }

        self.attribute_map = {
            'suggested_slots': 'suggestedSlots',
            'attendee_schedules': 'attendeeSchedules',
            'facilitator_schedules': 'facilitatorSchedules',
            'wfm_schedule_activities': 'wfmScheduleActivities'
        }

        self._suggested_slots = None
        self._attendee_schedules = None
        self._facilitator_schedules = None
        self._wfm_schedule_activities = None

    @property
    def suggested_slots(self) -> List['CoachingSlot']:
        """
        Gets the suggested_slots of this CoachingSlotsResponse.
        List of slots where coaching appointment can be scheduled

        :return: The suggested_slots of this CoachingSlotsResponse.
        :rtype: list[CoachingSlot]
        """
        return self._suggested_slots

    @suggested_slots.setter
    def suggested_slots(self, suggested_slots: List['CoachingSlot']) -> None:
        """
        Sets the suggested_slots of this CoachingSlotsResponse.
        List of slots where coaching appointment can be scheduled

        :param suggested_slots: The suggested_slots of this CoachingSlotsResponse.
        :type: list[CoachingSlot]
        """
        

        self._suggested_slots = suggested_slots

    @property
    def attendee_schedules(self) -> List['UserAvailableTimes']:
        """
        Gets the attendee_schedules of this CoachingSlotsResponse.
        Periods of availability for attendees to schedule coaching appointment

        :return: The attendee_schedules of this CoachingSlotsResponse.
        :rtype: list[UserAvailableTimes]
        """
        return self._attendee_schedules

    @attendee_schedules.setter
    def attendee_schedules(self, attendee_schedules: List['UserAvailableTimes']) -> None:
        """
        Sets the attendee_schedules of this CoachingSlotsResponse.
        Periods of availability for attendees to schedule coaching appointment

        :param attendee_schedules: The attendee_schedules of this CoachingSlotsResponse.
        :type: list[UserAvailableTimes]
        """
        

        self._attendee_schedules = attendee_schedules

    @property
    def facilitator_schedules(self) -> List['UserAvailableTimes']:
        """
        Gets the facilitator_schedules of this CoachingSlotsResponse.
        Periods of availability for facilitators to schedule coaching appointment

        :return: The facilitator_schedules of this CoachingSlotsResponse.
        :rtype: list[UserAvailableTimes]
        """
        return self._facilitator_schedules

    @facilitator_schedules.setter
    def facilitator_schedules(self, facilitator_schedules: List['UserAvailableTimes']) -> None:
        """
        Sets the facilitator_schedules of this CoachingSlotsResponse.
        Periods of availability for facilitators to schedule coaching appointment

        :param facilitator_schedules: The facilitator_schedules of this CoachingSlotsResponse.
        :type: list[UserAvailableTimes]
        """
        

        self._facilitator_schedules = facilitator_schedules

    @property
    def wfm_schedule_activities(self) -> List['WfmScheduleActivity']:
        """
        Gets the wfm_schedule_activities of this CoachingSlotsResponse.
        Detailed data for WFM scheduled activities

        :return: The wfm_schedule_activities of this CoachingSlotsResponse.
        :rtype: list[WfmScheduleActivity]
        """
        return self._wfm_schedule_activities

    @wfm_schedule_activities.setter
    def wfm_schedule_activities(self, wfm_schedule_activities: List['WfmScheduleActivity']) -> None:
        """
        Sets the wfm_schedule_activities of this CoachingSlotsResponse.
        Detailed data for WFM scheduled activities

        :param wfm_schedule_activities: The wfm_schedule_activities of this CoachingSlotsResponse.
        :type: list[WfmScheduleActivity]
        """
        

        self._wfm_schedule_activities = wfm_schedule_activities

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
