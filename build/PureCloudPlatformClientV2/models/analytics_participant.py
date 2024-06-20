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
    from . import AnalyticsSession

class AnalyticsParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AnalyticsParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'external_contact_id': 'str',
            'external_organization_id': 'str',
            'flagged_reason': 'str',
            'participant_id': 'str',
            'participant_name': 'str',
            'purpose': 'str',
            'team_id': 'str',
            'user_id': 'str',
            'sessions': 'list[AnalyticsSession]',
            'attributes': 'dict(str, str)'
        }

        self.attribute_map = {
            'external_contact_id': 'externalContactId',
            'external_organization_id': 'externalOrganizationId',
            'flagged_reason': 'flaggedReason',
            'participant_id': 'participantId',
            'participant_name': 'participantName',
            'purpose': 'purpose',
            'team_id': 'teamId',
            'user_id': 'userId',
            'sessions': 'sessions',
            'attributes': 'attributes'
        }

        self._external_contact_id = None
        self._external_organization_id = None
        self._flagged_reason = None
        self._participant_id = None
        self._participant_name = None
        self._purpose = None
        self._team_id = None
        self._user_id = None
        self._sessions = None
        self._attributes = None

    @property
    def external_contact_id(self) -> str:
        """
        Gets the external_contact_id of this AnalyticsParticipant.
        External contact identifier

        :return: The external_contact_id of this AnalyticsParticipant.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id: str) -> None:
        """
        Sets the external_contact_id of this AnalyticsParticipant.
        External contact identifier

        :param external_contact_id: The external_contact_id of this AnalyticsParticipant.
        :type: str
        """
        

        self._external_contact_id = external_contact_id

    @property
    def external_organization_id(self) -> str:
        """
        Gets the external_organization_id of this AnalyticsParticipant.
        External organization identifier

        :return: The external_organization_id of this AnalyticsParticipant.
        :rtype: str
        """
        return self._external_organization_id

    @external_organization_id.setter
    def external_organization_id(self, external_organization_id: str) -> None:
        """
        Sets the external_organization_id of this AnalyticsParticipant.
        External organization identifier

        :param external_organization_id: The external_organization_id of this AnalyticsParticipant.
        :type: str
        """
        

        self._external_organization_id = external_organization_id

    @property
    def flagged_reason(self) -> str:
        """
        Gets the flagged_reason of this AnalyticsParticipant.
        Reason for which participant flagged conversation

        :return: The flagged_reason of this AnalyticsParticipant.
        :rtype: str
        """
        return self._flagged_reason

    @flagged_reason.setter
    def flagged_reason(self, flagged_reason: str) -> None:
        """
        Sets the flagged_reason of this AnalyticsParticipant.
        Reason for which participant flagged conversation

        :param flagged_reason: The flagged_reason of this AnalyticsParticipant.
        :type: str
        """
        if isinstance(flagged_reason, int):
            flagged_reason = str(flagged_reason)
        allowed_values = ["general"]
        if flagged_reason.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for flagged_reason -> " + flagged_reason)
            self._flagged_reason = "outdated_sdk_version"
        else:
            self._flagged_reason = flagged_reason

    @property
    def participant_id(self) -> str:
        """
        Gets the participant_id of this AnalyticsParticipant.
        Unique identifier for the participant

        :return: The participant_id of this AnalyticsParticipant.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id: str) -> None:
        """
        Sets the participant_id of this AnalyticsParticipant.
        Unique identifier for the participant

        :param participant_id: The participant_id of this AnalyticsParticipant.
        :type: str
        """
        

        self._participant_id = participant_id

    @property
    def participant_name(self) -> str:
        """
        Gets the participant_name of this AnalyticsParticipant.
        A human readable name identifying the participant

        :return: The participant_name of this AnalyticsParticipant.
        :rtype: str
        """
        return self._participant_name

    @participant_name.setter
    def participant_name(self, participant_name: str) -> None:
        """
        Sets the participant_name of this AnalyticsParticipant.
        A human readable name identifying the participant

        :param participant_name: The participant_name of this AnalyticsParticipant.
        :type: str
        """
        

        self._participant_name = participant_name

    @property
    def purpose(self) -> str:
        """
        Gets the purpose of this AnalyticsParticipant.
        The participant's purpose

        :return: The purpose of this AnalyticsParticipant.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose: str) -> None:
        """
        Sets the purpose of this AnalyticsParticipant.
        The participant's purpose

        :param purpose: The purpose of this AnalyticsParticipant.
        :type: str
        """
        if isinstance(purpose, int):
            purpose = str(purpose)
        allowed_values = ["acd", "agent", "api", "botflow", "campaign", "customer", "dialer", "external", "fax", "group", "inbound", "ivr", "manual", "outbound", "station", "user", "voicemail", "voicesurveyflow", "workflow"]
        if purpose.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for purpose -> " + purpose)
            self._purpose = "outdated_sdk_version"
        else:
            self._purpose = purpose

    @property
    def team_id(self) -> str:
        """
        Gets the team_id of this AnalyticsParticipant.
        The team ID the user is a member of

        :return: The team_id of this AnalyticsParticipant.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id: str) -> None:
        """
        Sets the team_id of this AnalyticsParticipant.
        The team ID the user is a member of

        :param team_id: The team_id of this AnalyticsParticipant.
        :type: str
        """
        

        self._team_id = team_id

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this AnalyticsParticipant.
        Unique identifier for the user

        :return: The user_id of this AnalyticsParticipant.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this AnalyticsParticipant.
        Unique identifier for the user

        :param user_id: The user_id of this AnalyticsParticipant.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def sessions(self) -> List['AnalyticsSession']:
        """
        Gets the sessions of this AnalyticsParticipant.
        List of sessions associated to this participant

        :return: The sessions of this AnalyticsParticipant.
        :rtype: list[AnalyticsSession]
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions: List['AnalyticsSession']) -> None:
        """
        Sets the sessions of this AnalyticsParticipant.
        List of sessions associated to this participant

        :param sessions: The sessions of this AnalyticsParticipant.
        :type: list[AnalyticsSession]
        """
        

        self._sessions = sessions

    @property
    def attributes(self) -> Dict[str, str]:
        """
        Gets the attributes of this AnalyticsParticipant.
        List of attributes associated to this participant

        :return: The attributes of this AnalyticsParticipant.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: Dict[str, str]) -> None:
        """
        Sets the attributes of this AnalyticsParticipant.
        List of attributes associated to this participant

        :param attributes: The attributes of this AnalyticsParticipant.
        :type: dict(str, str)
        """
        

        self._attributes = attributes

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

