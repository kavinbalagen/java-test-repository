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
    from . import JourneyAppEventsNotificationAppMessage
    from . import JourneyAppEventsNotificationExternalContact
    from . import JourneyAppEventsNotificationOutcomeAchievedMessage
    from . import JourneyAppEventsNotificationSegmentAssignmentMessage
    from . import JourneyAppEventsNotificationSession

class JourneyAppEventsNotificationAppEventsNotification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneyAppEventsNotificationAppEventsNotification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'correlation_id': 'str',
            'external_contact': 'JourneyAppEventsNotificationExternalContact',
            'created_date': 'datetime',
            'customer_id': 'str',
            'customer_id_type': 'str',
            'session': 'JourneyAppEventsNotificationSession',
            'event_type': 'str',
            'app_event': 'JourneyAppEventsNotificationAppMessage',
            'outcome_achieved_event': 'JourneyAppEventsNotificationOutcomeAchievedMessage',
            'segment_assignment_event': 'JourneyAppEventsNotificationSegmentAssignmentMessage'
        }

        self.attribute_map = {
            'id': 'id',
            'correlation_id': 'correlationId',
            'external_contact': 'externalContact',
            'created_date': 'createdDate',
            'customer_id': 'customerId',
            'customer_id_type': 'customerIdType',
            'session': 'session',
            'event_type': 'eventType',
            'app_event': 'appEvent',
            'outcome_achieved_event': 'outcomeAchievedEvent',
            'segment_assignment_event': 'segmentAssignmentEvent'
        }

        self._id = None
        self._correlation_id = None
        self._external_contact = None
        self._created_date = None
        self._customer_id = None
        self._customer_id_type = None
        self._session = None
        self._event_type = None
        self._app_event = None
        self._outcome_achieved_event = None
        self._segment_assignment_event = None

    @property
    def id(self) -> str:
        """
        Gets the id of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The id of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this JourneyAppEventsNotificationAppEventsNotification.


        :param id: The id of this JourneyAppEventsNotificationAppEventsNotification.
        :type: str
        """
        

        self._id = id

    @property
    def correlation_id(self) -> str:
        """
        Gets the correlation_id of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The correlation_id of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id: str) -> None:
        """
        Sets the correlation_id of this JourneyAppEventsNotificationAppEventsNotification.


        :param correlation_id: The correlation_id of this JourneyAppEventsNotificationAppEventsNotification.
        :type: str
        """
        

        self._correlation_id = correlation_id

    @property
    def external_contact(self) -> 'JourneyAppEventsNotificationExternalContact':
        """
        Gets the external_contact of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The external_contact of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: JourneyAppEventsNotificationExternalContact
        """
        return self._external_contact

    @external_contact.setter
    def external_contact(self, external_contact: 'JourneyAppEventsNotificationExternalContact') -> None:
        """
        Sets the external_contact of this JourneyAppEventsNotificationAppEventsNotification.


        :param external_contact: The external_contact of this JourneyAppEventsNotificationAppEventsNotification.
        :type: JourneyAppEventsNotificationExternalContact
        """
        

        self._external_contact = external_contact

    @property
    def created_date(self) -> datetime:
        """
        Gets the created_date of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The created_date of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date: datetime) -> None:
        """
        Sets the created_date of this JourneyAppEventsNotificationAppEventsNotification.


        :param created_date: The created_date of this JourneyAppEventsNotificationAppEventsNotification.
        :type: datetime
        """
        

        self._created_date = created_date

    @property
    def customer_id(self) -> str:
        """
        Gets the customer_id of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The customer_id of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str) -> None:
        """
        Sets the customer_id of this JourneyAppEventsNotificationAppEventsNotification.


        :param customer_id: The customer_id of this JourneyAppEventsNotificationAppEventsNotification.
        :type: str
        """
        

        self._customer_id = customer_id

    @property
    def customer_id_type(self) -> str:
        """
        Gets the customer_id_type of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The customer_id_type of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: str
        """
        return self._customer_id_type

    @customer_id_type.setter
    def customer_id_type(self, customer_id_type: str) -> None:
        """
        Sets the customer_id_type of this JourneyAppEventsNotificationAppEventsNotification.


        :param customer_id_type: The customer_id_type of this JourneyAppEventsNotificationAppEventsNotification.
        :type: str
        """
        

        self._customer_id_type = customer_id_type

    @property
    def session(self) -> 'JourneyAppEventsNotificationSession':
        """
        Gets the session of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The session of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: JourneyAppEventsNotificationSession
        """
        return self._session

    @session.setter
    def session(self, session: 'JourneyAppEventsNotificationSession') -> None:
        """
        Sets the session of this JourneyAppEventsNotificationAppEventsNotification.


        :param session: The session of this JourneyAppEventsNotificationAppEventsNotification.
        :type: JourneyAppEventsNotificationSession
        """
        

        self._session = session

    @property
    def event_type(self) -> str:
        """
        Gets the event_type of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The event_type of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: str) -> None:
        """
        Sets the event_type of this JourneyAppEventsNotificationAppEventsNotification.


        :param event_type: The event_type of this JourneyAppEventsNotificationAppEventsNotification.
        :type: str
        """
        if isinstance(event_type, int):
            event_type = str(event_type)
        allowed_values = ["AppEvent", "OutcomeAchievedEvent", "SegmentAssignmentEvent"]
        if event_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for event_type -> " + event_type)
            self._event_type = "outdated_sdk_version"
        else:
            self._event_type = event_type

    @property
    def app_event(self) -> 'JourneyAppEventsNotificationAppMessage':
        """
        Gets the app_event of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The app_event of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: JourneyAppEventsNotificationAppMessage
        """
        return self._app_event

    @app_event.setter
    def app_event(self, app_event: 'JourneyAppEventsNotificationAppMessage') -> None:
        """
        Sets the app_event of this JourneyAppEventsNotificationAppEventsNotification.


        :param app_event: The app_event of this JourneyAppEventsNotificationAppEventsNotification.
        :type: JourneyAppEventsNotificationAppMessage
        """
        

        self._app_event = app_event

    @property
    def outcome_achieved_event(self) -> 'JourneyAppEventsNotificationOutcomeAchievedMessage':
        """
        Gets the outcome_achieved_event of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The outcome_achieved_event of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: JourneyAppEventsNotificationOutcomeAchievedMessage
        """
        return self._outcome_achieved_event

    @outcome_achieved_event.setter
    def outcome_achieved_event(self, outcome_achieved_event: 'JourneyAppEventsNotificationOutcomeAchievedMessage') -> None:
        """
        Sets the outcome_achieved_event of this JourneyAppEventsNotificationAppEventsNotification.


        :param outcome_achieved_event: The outcome_achieved_event of this JourneyAppEventsNotificationAppEventsNotification.
        :type: JourneyAppEventsNotificationOutcomeAchievedMessage
        """
        

        self._outcome_achieved_event = outcome_achieved_event

    @property
    def segment_assignment_event(self) -> 'JourneyAppEventsNotificationSegmentAssignmentMessage':
        """
        Gets the segment_assignment_event of this JourneyAppEventsNotificationAppEventsNotification.


        :return: The segment_assignment_event of this JourneyAppEventsNotificationAppEventsNotification.
        :rtype: JourneyAppEventsNotificationSegmentAssignmentMessage
        """
        return self._segment_assignment_event

    @segment_assignment_event.setter
    def segment_assignment_event(self, segment_assignment_event: 'JourneyAppEventsNotificationSegmentAssignmentMessage') -> None:
        """
        Sets the segment_assignment_event of this JourneyAppEventsNotificationAppEventsNotification.


        :param segment_assignment_event: The segment_assignment_event of this JourneyAppEventsNotificationAppEventsNotification.
        :type: JourneyAppEventsNotificationSegmentAssignmentMessage
        """
        

        self._segment_assignment_event = segment_assignment_event

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

