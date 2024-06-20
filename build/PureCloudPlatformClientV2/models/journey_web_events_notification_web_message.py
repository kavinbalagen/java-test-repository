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
    from . import JourneyWebEventsNotificationBrowser
    from . import JourneyWebEventsNotificationCustomEventAttribute
    from . import JourneyWebEventsNotificationDevice
    from . import JourneyWebEventsNotificationGeoLocation
    from . import JourneyWebEventsNotificationMktCampaign
    from . import JourneyWebEventsNotificationPage
    from . import JourneyWebEventsNotificationReferrer

class JourneyWebEventsNotificationWebMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        JourneyWebEventsNotificationWebMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_name': 'str',
            'total_event_count': 'int',
            'total_pageview_count': 'int',
            'user_agent_string': 'str',
            'ip_address': 'str',
            'ip_organization': 'str',
            'search_query': 'str',
            'authenticated': 'bool',
            'browser': 'JourneyWebEventsNotificationBrowser',
            'device': 'JourneyWebEventsNotificationDevice',
            'geolocation': 'JourneyWebEventsNotificationGeoLocation',
            'mkt_campaign': 'JourneyWebEventsNotificationMktCampaign',
            'page': 'JourneyWebEventsNotificationPage',
            'referrer': 'JourneyWebEventsNotificationReferrer',
            'attributes': 'dict(str, JourneyWebEventsNotificationCustomEventAttribute)',
            'traits': 'dict(str, JourneyWebEventsNotificationCustomEventAttribute)'
        }

        self.attribute_map = {
            'event_name': 'eventName',
            'total_event_count': 'totalEventCount',
            'total_pageview_count': 'totalPageviewCount',
            'user_agent_string': 'userAgentString',
            'ip_address': 'ipAddress',
            'ip_organization': 'ipOrganization',
            'search_query': 'searchQuery',
            'authenticated': 'authenticated',
            'browser': 'browser',
            'device': 'device',
            'geolocation': 'geolocation',
            'mkt_campaign': 'mktCampaign',
            'page': 'page',
            'referrer': 'referrer',
            'attributes': 'attributes',
            'traits': 'traits'
        }

        self._event_name = None
        self._total_event_count = None
        self._total_pageview_count = None
        self._user_agent_string = None
        self._ip_address = None
        self._ip_organization = None
        self._search_query = None
        self._authenticated = None
        self._browser = None
        self._device = None
        self._geolocation = None
        self._mkt_campaign = None
        self._page = None
        self._referrer = None
        self._attributes = None
        self._traits = None

    @property
    def event_name(self) -> str:
        """
        Gets the event_name of this JourneyWebEventsNotificationWebMessage.


        :return: The event_name of this JourneyWebEventsNotificationWebMessage.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name: str) -> None:
        """
        Sets the event_name of this JourneyWebEventsNotificationWebMessage.


        :param event_name: The event_name of this JourneyWebEventsNotificationWebMessage.
        :type: str
        """
        

        self._event_name = event_name

    @property
    def total_event_count(self) -> int:
        """
        Gets the total_event_count of this JourneyWebEventsNotificationWebMessage.


        :return: The total_event_count of this JourneyWebEventsNotificationWebMessage.
        :rtype: int
        """
        return self._total_event_count

    @total_event_count.setter
    def total_event_count(self, total_event_count: int) -> None:
        """
        Sets the total_event_count of this JourneyWebEventsNotificationWebMessage.


        :param total_event_count: The total_event_count of this JourneyWebEventsNotificationWebMessage.
        :type: int
        """
        

        self._total_event_count = total_event_count

    @property
    def total_pageview_count(self) -> int:
        """
        Gets the total_pageview_count of this JourneyWebEventsNotificationWebMessage.


        :return: The total_pageview_count of this JourneyWebEventsNotificationWebMessage.
        :rtype: int
        """
        return self._total_pageview_count

    @total_pageview_count.setter
    def total_pageview_count(self, total_pageview_count: int) -> None:
        """
        Sets the total_pageview_count of this JourneyWebEventsNotificationWebMessage.


        :param total_pageview_count: The total_pageview_count of this JourneyWebEventsNotificationWebMessage.
        :type: int
        """
        

        self._total_pageview_count = total_pageview_count

    @property
    def user_agent_string(self) -> str:
        """
        Gets the user_agent_string of this JourneyWebEventsNotificationWebMessage.


        :return: The user_agent_string of this JourneyWebEventsNotificationWebMessage.
        :rtype: str
        """
        return self._user_agent_string

    @user_agent_string.setter
    def user_agent_string(self, user_agent_string: str) -> None:
        """
        Sets the user_agent_string of this JourneyWebEventsNotificationWebMessage.


        :param user_agent_string: The user_agent_string of this JourneyWebEventsNotificationWebMessage.
        :type: str
        """
        

        self._user_agent_string = user_agent_string

    @property
    def ip_address(self) -> str:
        """
        Gets the ip_address of this JourneyWebEventsNotificationWebMessage.


        :return: The ip_address of this JourneyWebEventsNotificationWebMessage.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str) -> None:
        """
        Sets the ip_address of this JourneyWebEventsNotificationWebMessage.


        :param ip_address: The ip_address of this JourneyWebEventsNotificationWebMessage.
        :type: str
        """
        

        self._ip_address = ip_address

    @property
    def ip_organization(self) -> str:
        """
        Gets the ip_organization of this JourneyWebEventsNotificationWebMessage.


        :return: The ip_organization of this JourneyWebEventsNotificationWebMessage.
        :rtype: str
        """
        return self._ip_organization

    @ip_organization.setter
    def ip_organization(self, ip_organization: str) -> None:
        """
        Sets the ip_organization of this JourneyWebEventsNotificationWebMessage.


        :param ip_organization: The ip_organization of this JourneyWebEventsNotificationWebMessage.
        :type: str
        """
        

        self._ip_organization = ip_organization

    @property
    def search_query(self) -> str:
        """
        Gets the search_query of this JourneyWebEventsNotificationWebMessage.


        :return: The search_query of this JourneyWebEventsNotificationWebMessage.
        :rtype: str
        """
        return self._search_query

    @search_query.setter
    def search_query(self, search_query: str) -> None:
        """
        Sets the search_query of this JourneyWebEventsNotificationWebMessage.


        :param search_query: The search_query of this JourneyWebEventsNotificationWebMessage.
        :type: str
        """
        

        self._search_query = search_query

    @property
    def authenticated(self) -> bool:
        """
        Gets the authenticated of this JourneyWebEventsNotificationWebMessage.


        :return: The authenticated of this JourneyWebEventsNotificationWebMessage.
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated: bool) -> None:
        """
        Sets the authenticated of this JourneyWebEventsNotificationWebMessage.


        :param authenticated: The authenticated of this JourneyWebEventsNotificationWebMessage.
        :type: bool
        """
        

        self._authenticated = authenticated

    @property
    def browser(self) -> 'JourneyWebEventsNotificationBrowser':
        """
        Gets the browser of this JourneyWebEventsNotificationWebMessage.


        :return: The browser of this JourneyWebEventsNotificationWebMessage.
        :rtype: JourneyWebEventsNotificationBrowser
        """
        return self._browser

    @browser.setter
    def browser(self, browser: 'JourneyWebEventsNotificationBrowser') -> None:
        """
        Sets the browser of this JourneyWebEventsNotificationWebMessage.


        :param browser: The browser of this JourneyWebEventsNotificationWebMessage.
        :type: JourneyWebEventsNotificationBrowser
        """
        

        self._browser = browser

    @property
    def device(self) -> 'JourneyWebEventsNotificationDevice':
        """
        Gets the device of this JourneyWebEventsNotificationWebMessage.


        :return: The device of this JourneyWebEventsNotificationWebMessage.
        :rtype: JourneyWebEventsNotificationDevice
        """
        return self._device

    @device.setter
    def device(self, device: 'JourneyWebEventsNotificationDevice') -> None:
        """
        Sets the device of this JourneyWebEventsNotificationWebMessage.


        :param device: The device of this JourneyWebEventsNotificationWebMessage.
        :type: JourneyWebEventsNotificationDevice
        """
        

        self._device = device

    @property
    def geolocation(self) -> 'JourneyWebEventsNotificationGeoLocation':
        """
        Gets the geolocation of this JourneyWebEventsNotificationWebMessage.


        :return: The geolocation of this JourneyWebEventsNotificationWebMessage.
        :rtype: JourneyWebEventsNotificationGeoLocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: 'JourneyWebEventsNotificationGeoLocation') -> None:
        """
        Sets the geolocation of this JourneyWebEventsNotificationWebMessage.


        :param geolocation: The geolocation of this JourneyWebEventsNotificationWebMessage.
        :type: JourneyWebEventsNotificationGeoLocation
        """
        

        self._geolocation = geolocation

    @property
    def mkt_campaign(self) -> 'JourneyWebEventsNotificationMktCampaign':
        """
        Gets the mkt_campaign of this JourneyWebEventsNotificationWebMessage.


        :return: The mkt_campaign of this JourneyWebEventsNotificationWebMessage.
        :rtype: JourneyWebEventsNotificationMktCampaign
        """
        return self._mkt_campaign

    @mkt_campaign.setter
    def mkt_campaign(self, mkt_campaign: 'JourneyWebEventsNotificationMktCampaign') -> None:
        """
        Sets the mkt_campaign of this JourneyWebEventsNotificationWebMessage.


        :param mkt_campaign: The mkt_campaign of this JourneyWebEventsNotificationWebMessage.
        :type: JourneyWebEventsNotificationMktCampaign
        """
        

        self._mkt_campaign = mkt_campaign

    @property
    def page(self) -> 'JourneyWebEventsNotificationPage':
        """
        Gets the page of this JourneyWebEventsNotificationWebMessage.


        :return: The page of this JourneyWebEventsNotificationWebMessage.
        :rtype: JourneyWebEventsNotificationPage
        """
        return self._page

    @page.setter
    def page(self, page: 'JourneyWebEventsNotificationPage') -> None:
        """
        Sets the page of this JourneyWebEventsNotificationWebMessage.


        :param page: The page of this JourneyWebEventsNotificationWebMessage.
        :type: JourneyWebEventsNotificationPage
        """
        

        self._page = page

    @property
    def referrer(self) -> 'JourneyWebEventsNotificationReferrer':
        """
        Gets the referrer of this JourneyWebEventsNotificationWebMessage.


        :return: The referrer of this JourneyWebEventsNotificationWebMessage.
        :rtype: JourneyWebEventsNotificationReferrer
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer: 'JourneyWebEventsNotificationReferrer') -> None:
        """
        Sets the referrer of this JourneyWebEventsNotificationWebMessage.


        :param referrer: The referrer of this JourneyWebEventsNotificationWebMessage.
        :type: JourneyWebEventsNotificationReferrer
        """
        

        self._referrer = referrer

    @property
    def attributes(self) -> Dict[str, 'JourneyWebEventsNotificationCustomEventAttribute']:
        """
        Gets the attributes of this JourneyWebEventsNotificationWebMessage.


        :return: The attributes of this JourneyWebEventsNotificationWebMessage.
        :rtype: dict(str, JourneyWebEventsNotificationCustomEventAttribute)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: Dict[str, 'JourneyWebEventsNotificationCustomEventAttribute']) -> None:
        """
        Sets the attributes of this JourneyWebEventsNotificationWebMessage.


        :param attributes: The attributes of this JourneyWebEventsNotificationWebMessage.
        :type: dict(str, JourneyWebEventsNotificationCustomEventAttribute)
        """
        

        self._attributes = attributes

    @property
    def traits(self) -> Dict[str, 'JourneyWebEventsNotificationCustomEventAttribute']:
        """
        Gets the traits of this JourneyWebEventsNotificationWebMessage.


        :return: The traits of this JourneyWebEventsNotificationWebMessage.
        :rtype: dict(str, JourneyWebEventsNotificationCustomEventAttribute)
        """
        return self._traits

    @traits.setter
    def traits(self, traits: Dict[str, 'JourneyWebEventsNotificationCustomEventAttribute']) -> None:
        """
        Sets the traits of this JourneyWebEventsNotificationWebMessage.


        :param traits: The traits of this JourneyWebEventsNotificationWebMessage.
        :type: dict(str, JourneyWebEventsNotificationCustomEventAttribute)
        """
        

        self._traits = traits

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

