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
    from . import JourneyAppEventsNotificationAssociatedValue
    from . import JourneyAppEventsNotificationBrowser
    from . import JourneyAppEventsNotificationDevice
    from . import JourneyAppEventsNotificationGeoLocation
    from . import JourneyAppEventsNotificationMktCampaign
    from . import JourneyAppEventsNotificationOutcome
    from . import JourneyAppEventsNotificationReferrer

class JourneyAppEventsNotificationOutcomeAchievedMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneyAppEventsNotificationOutcomeAchievedMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'outcome': 'JourneyAppEventsNotificationOutcome',
            'browser': 'JourneyAppEventsNotificationBrowser',
            'visit_created_date': 'datetime',
            'ip_address': 'str',
            'ip_organization': 'str',
            'user_agent_string': 'str',
            'device': 'JourneyAppEventsNotificationDevice',
            'geolocation': 'JourneyAppEventsNotificationGeoLocation',
            'mkt_campaign': 'JourneyAppEventsNotificationMktCampaign',
            'visit_referrer': 'JourneyAppEventsNotificationReferrer',
            'associated_value': 'JourneyAppEventsNotificationAssociatedValue'
        }

        self.attribute_map = {
            'outcome': 'outcome',
            'browser': 'browser',
            'visit_created_date': 'visitCreatedDate',
            'ip_address': 'ipAddress',
            'ip_organization': 'ipOrganization',
            'user_agent_string': 'userAgentString',
            'device': 'device',
            'geolocation': 'geolocation',
            'mkt_campaign': 'mktCampaign',
            'visit_referrer': 'visitReferrer',
            'associated_value': 'associatedValue'
        }

        self._outcome = None
        self._browser = None
        self._visit_created_date = None
        self._ip_address = None
        self._ip_organization = None
        self._user_agent_string = None
        self._device = None
        self._geolocation = None
        self._mkt_campaign = None
        self._visit_referrer = None
        self._associated_value = None

    @property
    def outcome(self) -> 'JourneyAppEventsNotificationOutcome':
        """
        Gets the outcome of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The outcome of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationOutcome
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome: 'JourneyAppEventsNotificationOutcome') -> None:
        """
        Sets the outcome of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param outcome: The outcome of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationOutcome
        """
        

        self._outcome = outcome

    @property
    def browser(self) -> 'JourneyAppEventsNotificationBrowser':
        """
        Gets the browser of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The browser of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationBrowser
        """
        return self._browser

    @browser.setter
    def browser(self, browser: 'JourneyAppEventsNotificationBrowser') -> None:
        """
        Sets the browser of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param browser: The browser of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationBrowser
        """
        

        self._browser = browser

    @property
    def visit_created_date(self) -> datetime:
        """
        Gets the visit_created_date of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The visit_created_date of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: datetime
        """
        return self._visit_created_date

    @visit_created_date.setter
    def visit_created_date(self, visit_created_date: datetime) -> None:
        """
        Sets the visit_created_date of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param visit_created_date: The visit_created_date of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: datetime
        """
        

        self._visit_created_date = visit_created_date

    @property
    def ip_address(self) -> str:
        """
        Gets the ip_address of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The ip_address of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str) -> None:
        """
        Sets the ip_address of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param ip_address: The ip_address of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: str
        """
        

        self._ip_address = ip_address

    @property
    def ip_organization(self) -> str:
        """
        Gets the ip_organization of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The ip_organization of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: str
        """
        return self._ip_organization

    @ip_organization.setter
    def ip_organization(self, ip_organization: str) -> None:
        """
        Sets the ip_organization of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param ip_organization: The ip_organization of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: str
        """
        

        self._ip_organization = ip_organization

    @property
    def user_agent_string(self) -> str:
        """
        Gets the user_agent_string of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The user_agent_string of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: str
        """
        return self._user_agent_string

    @user_agent_string.setter
    def user_agent_string(self, user_agent_string: str) -> None:
        """
        Sets the user_agent_string of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param user_agent_string: The user_agent_string of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: str
        """
        

        self._user_agent_string = user_agent_string

    @property
    def device(self) -> 'JourneyAppEventsNotificationDevice':
        """
        Gets the device of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The device of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationDevice
        """
        return self._device

    @device.setter
    def device(self, device: 'JourneyAppEventsNotificationDevice') -> None:
        """
        Sets the device of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param device: The device of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationDevice
        """
        

        self._device = device

    @property
    def geolocation(self) -> 'JourneyAppEventsNotificationGeoLocation':
        """
        Gets the geolocation of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The geolocation of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationGeoLocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: 'JourneyAppEventsNotificationGeoLocation') -> None:
        """
        Sets the geolocation of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param geolocation: The geolocation of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationGeoLocation
        """
        

        self._geolocation = geolocation

    @property
    def mkt_campaign(self) -> 'JourneyAppEventsNotificationMktCampaign':
        """
        Gets the mkt_campaign of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The mkt_campaign of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationMktCampaign
        """
        return self._mkt_campaign

    @mkt_campaign.setter
    def mkt_campaign(self, mkt_campaign: 'JourneyAppEventsNotificationMktCampaign') -> None:
        """
        Sets the mkt_campaign of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param mkt_campaign: The mkt_campaign of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationMktCampaign
        """
        

        self._mkt_campaign = mkt_campaign

    @property
    def visit_referrer(self) -> 'JourneyAppEventsNotificationReferrer':
        """
        Gets the visit_referrer of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The visit_referrer of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationReferrer
        """
        return self._visit_referrer

    @visit_referrer.setter
    def visit_referrer(self, visit_referrer: 'JourneyAppEventsNotificationReferrer') -> None:
        """
        Sets the visit_referrer of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param visit_referrer: The visit_referrer of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationReferrer
        """
        

        self._visit_referrer = visit_referrer

    @property
    def associated_value(self) -> 'JourneyAppEventsNotificationAssociatedValue':
        """
        Gets the associated_value of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :return: The associated_value of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :rtype: JourneyAppEventsNotificationAssociatedValue
        """
        return self._associated_value

    @associated_value.setter
    def associated_value(self, associated_value: 'JourneyAppEventsNotificationAssociatedValue') -> None:
        """
        Sets the associated_value of this JourneyAppEventsNotificationOutcomeAchievedMessage.


        :param associated_value: The associated_value of this JourneyAppEventsNotificationOutcomeAchievedMessage.
        :type: JourneyAppEventsNotificationAssociatedValue
        """
        

        self._associated_value = associated_value

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

