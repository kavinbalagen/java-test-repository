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
    from . import DialerCampaignRuleConfigChangeUriReference

class DialerCampaignRuleConfigChangeCampaignRuleActionEntities(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DialerCampaignRuleConfigChangeCampaignRuleActionEntities - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'use_triggering_entity': 'bool',
            'additional_properties': 'dict(str, object)',
            'campaigns': 'list[DialerCampaignRuleConfigChangeUriReference]',
            'sequences': 'list[DialerCampaignRuleConfigChangeUriReference]'
        }

        self.attribute_map = {
            'use_triggering_entity': 'useTriggeringEntity',
            'additional_properties': 'additionalProperties',
            'campaigns': 'campaigns',
            'sequences': 'sequences'
        }

        self._use_triggering_entity = None
        self._additional_properties = None
        self._campaigns = None
        self._sequences = None

    @property
    def use_triggering_entity(self) -> bool:
        """
        Gets the use_triggering_entity of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        Whether this action should act on the entity that triggered it

        :return: The use_triggering_entity of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :rtype: bool
        """
        return self._use_triggering_entity

    @use_triggering_entity.setter
    def use_triggering_entity(self, use_triggering_entity: bool) -> None:
        """
        Sets the use_triggering_entity of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        Whether this action should act on the entity that triggered it

        :param use_triggering_entity: The use_triggering_entity of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :type: bool
        """
        

        self._use_triggering_entity = use_triggering_entity

    @property
    def additional_properties(self) -> Dict[str, object]:
        """
        Gets the additional_properties of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.


        :return: The additional_properties of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :rtype: dict(str, object)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties: Dict[str, object]) -> None:
        """
        Sets the additional_properties of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.


        :param additional_properties: The additional_properties of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :type: dict(str, object)
        """
        

        self._additional_properties = additional_properties

    @property
    def campaigns(self) -> List['DialerCampaignRuleConfigChangeUriReference']:
        """
        Gets the campaigns of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        A list of campaignIds to act on

        :return: The campaigns of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :rtype: list[DialerCampaignRuleConfigChangeUriReference]
        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, campaigns: List['DialerCampaignRuleConfigChangeUriReference']) -> None:
        """
        Sets the campaigns of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        A list of campaignIds to act on

        :param campaigns: The campaigns of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :type: list[DialerCampaignRuleConfigChangeUriReference]
        """
        

        self._campaigns = campaigns

    @property
    def sequences(self) -> List['DialerCampaignRuleConfigChangeUriReference']:
        """
        Gets the sequences of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        A list of sequenceIds to act on

        :return: The sequences of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :rtype: list[DialerCampaignRuleConfigChangeUriReference]
        """
        return self._sequences

    @sequences.setter
    def sequences(self, sequences: List['DialerCampaignRuleConfigChangeUriReference']) -> None:
        """
        Sets the sequences of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        A list of sequenceIds to act on

        :param sequences: The sequences of this DialerCampaignRuleConfigChangeCampaignRuleActionEntities.
        :type: list[DialerCampaignRuleConfigChangeUriReference]
        """
        

        self._sequences = sequences

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
