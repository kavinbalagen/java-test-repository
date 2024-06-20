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
    from . import ShiftTradeActivityRule

class ShiftTradeSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ShiftTradeSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'auto_review': 'bool',
            'allow_direct_trades': 'bool',
            'min_hours_in_future': 'int',
            'unequal_paid': 'str',
            'one_sided': 'str',
            'weekly_min_paid_violations': 'str',
            'weekly_max_paid_violations': 'str',
            'requires_matching_queues': 'bool',
            'requires_matching_languages': 'bool',
            'requires_matching_skills': 'bool',
            'requires_matching_planning_groups': 'bool',
            'activity_category_rules': 'list[ShiftTradeActivityRule]'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'auto_review': 'autoReview',
            'allow_direct_trades': 'allowDirectTrades',
            'min_hours_in_future': 'minHoursInFuture',
            'unequal_paid': 'unequalPaid',
            'one_sided': 'oneSided',
            'weekly_min_paid_violations': 'weeklyMinPaidViolations',
            'weekly_max_paid_violations': 'weeklyMaxPaidViolations',
            'requires_matching_queues': 'requiresMatchingQueues',
            'requires_matching_languages': 'requiresMatchingLanguages',
            'requires_matching_skills': 'requiresMatchingSkills',
            'requires_matching_planning_groups': 'requiresMatchingPlanningGroups',
            'activity_category_rules': 'activityCategoryRules'
        }

        self._enabled = None
        self._auto_review = None
        self._allow_direct_trades = None
        self._min_hours_in_future = None
        self._unequal_paid = None
        self._one_sided = None
        self._weekly_min_paid_violations = None
        self._weekly_max_paid_violations = None
        self._requires_matching_queues = None
        self._requires_matching_languages = None
        self._requires_matching_skills = None
        self._requires_matching_planning_groups = None
        self._activity_category_rules = None

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this ShiftTradeSettings.
        Whether shift trading is enabled for this management unit

        :return: The enabled of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this ShiftTradeSettings.
        Whether shift trading is enabled for this management unit

        :param enabled: The enabled of this ShiftTradeSettings.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def auto_review(self) -> bool:
        """
        Gets the auto_review of this ShiftTradeSettings.
        Whether automatic shift trade review is enabled according to the rules defined in for this management unit

        :return: The auto_review of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._auto_review

    @auto_review.setter
    def auto_review(self, auto_review: bool) -> None:
        """
        Sets the auto_review of this ShiftTradeSettings.
        Whether automatic shift trade review is enabled according to the rules defined in for this management unit

        :param auto_review: The auto_review of this ShiftTradeSettings.
        :type: bool
        """
        

        self._auto_review = auto_review

    @property
    def allow_direct_trades(self) -> bool:
        """
        Gets the allow_direct_trades of this ShiftTradeSettings.
        Whether direct shift trades between agents are allowed

        :return: The allow_direct_trades of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._allow_direct_trades

    @allow_direct_trades.setter
    def allow_direct_trades(self, allow_direct_trades: bool) -> None:
        """
        Sets the allow_direct_trades of this ShiftTradeSettings.
        Whether direct shift trades between agents are allowed

        :param allow_direct_trades: The allow_direct_trades of this ShiftTradeSettings.
        :type: bool
        """
        

        self._allow_direct_trades = allow_direct_trades

    @property
    def min_hours_in_future(self) -> int:
        """
        Gets the min_hours_in_future of this ShiftTradeSettings.
        The minimum number of hours in the future shift trades are allowed

        :return: The min_hours_in_future of this ShiftTradeSettings.
        :rtype: int
        """
        return self._min_hours_in_future

    @min_hours_in_future.setter
    def min_hours_in_future(self, min_hours_in_future: int) -> None:
        """
        Sets the min_hours_in_future of this ShiftTradeSettings.
        The minimum number of hours in the future shift trades are allowed

        :param min_hours_in_future: The min_hours_in_future of this ShiftTradeSettings.
        :type: int
        """
        

        self._min_hours_in_future = min_hours_in_future

    @property
    def unequal_paid(self) -> str:
        """
        Gets the unequal_paid of this ShiftTradeSettings.
        How to handle shift trades which involve unequal paid times

        :return: The unequal_paid of this ShiftTradeSettings.
        :rtype: str
        """
        return self._unequal_paid

    @unequal_paid.setter
    def unequal_paid(self, unequal_paid: str) -> None:
        """
        Sets the unequal_paid of this ShiftTradeSettings.
        How to handle shift trades which involve unequal paid times

        :param unequal_paid: The unequal_paid of this ShiftTradeSettings.
        :type: str
        """
        if isinstance(unequal_paid, int):
            unequal_paid = str(unequal_paid)
        allowed_values = ["Allow", "Disallow", "AdminReview"]
        if unequal_paid.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for unequal_paid -> " + unequal_paid)
            self._unequal_paid = "outdated_sdk_version"
        else:
            self._unequal_paid = unequal_paid

    @property
    def one_sided(self) -> str:
        """
        Gets the one_sided of this ShiftTradeSettings.
        How to handle one-sided shift trades

        :return: The one_sided of this ShiftTradeSettings.
        :rtype: str
        """
        return self._one_sided

    @one_sided.setter
    def one_sided(self, one_sided: str) -> None:
        """
        Sets the one_sided of this ShiftTradeSettings.
        How to handle one-sided shift trades

        :param one_sided: The one_sided of this ShiftTradeSettings.
        :type: str
        """
        if isinstance(one_sided, int):
            one_sided = str(one_sided)
        allowed_values = ["Allow", "Disallow", "AdminReview"]
        if one_sided.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for one_sided -> " + one_sided)
            self._one_sided = "outdated_sdk_version"
        else:
            self._one_sided = one_sided

    @property
    def weekly_min_paid_violations(self) -> str:
        """
        Gets the weekly_min_paid_violations of this ShiftTradeSettings.
        How to handle shift trades which result in violations of weekly minimum paid time constraint

        :return: The weekly_min_paid_violations of this ShiftTradeSettings.
        :rtype: str
        """
        return self._weekly_min_paid_violations

    @weekly_min_paid_violations.setter
    def weekly_min_paid_violations(self, weekly_min_paid_violations: str) -> None:
        """
        Sets the weekly_min_paid_violations of this ShiftTradeSettings.
        How to handle shift trades which result in violations of weekly minimum paid time constraint

        :param weekly_min_paid_violations: The weekly_min_paid_violations of this ShiftTradeSettings.
        :type: str
        """
        if isinstance(weekly_min_paid_violations, int):
            weekly_min_paid_violations = str(weekly_min_paid_violations)
        allowed_values = ["Allow", "Disallow", "AdminReview"]
        if weekly_min_paid_violations.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for weekly_min_paid_violations -> " + weekly_min_paid_violations)
            self._weekly_min_paid_violations = "outdated_sdk_version"
        else:
            self._weekly_min_paid_violations = weekly_min_paid_violations

    @property
    def weekly_max_paid_violations(self) -> str:
        """
        Gets the weekly_max_paid_violations of this ShiftTradeSettings.
        How to handle shift trades which result in violations of weekly maximum paid time constraint

        :return: The weekly_max_paid_violations of this ShiftTradeSettings.
        :rtype: str
        """
        return self._weekly_max_paid_violations

    @weekly_max_paid_violations.setter
    def weekly_max_paid_violations(self, weekly_max_paid_violations: str) -> None:
        """
        Sets the weekly_max_paid_violations of this ShiftTradeSettings.
        How to handle shift trades which result in violations of weekly maximum paid time constraint

        :param weekly_max_paid_violations: The weekly_max_paid_violations of this ShiftTradeSettings.
        :type: str
        """
        if isinstance(weekly_max_paid_violations, int):
            weekly_max_paid_violations = str(weekly_max_paid_violations)
        allowed_values = ["Allow", "Disallow", "AdminReview"]
        if weekly_max_paid_violations.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for weekly_max_paid_violations -> " + weekly_max_paid_violations)
            self._weekly_max_paid_violations = "outdated_sdk_version"
        else:
            self._weekly_max_paid_violations = weekly_max_paid_violations

    @property
    def requires_matching_queues(self) -> bool:
        """
        Gets the requires_matching_queues of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching queues

        :return: The requires_matching_queues of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._requires_matching_queues

    @requires_matching_queues.setter
    def requires_matching_queues(self, requires_matching_queues: bool) -> None:
        """
        Sets the requires_matching_queues of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching queues

        :param requires_matching_queues: The requires_matching_queues of this ShiftTradeSettings.
        :type: bool
        """
        

        self._requires_matching_queues = requires_matching_queues

    @property
    def requires_matching_languages(self) -> bool:
        """
        Gets the requires_matching_languages of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching languages

        :return: The requires_matching_languages of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._requires_matching_languages

    @requires_matching_languages.setter
    def requires_matching_languages(self, requires_matching_languages: bool) -> None:
        """
        Sets the requires_matching_languages of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching languages

        :param requires_matching_languages: The requires_matching_languages of this ShiftTradeSettings.
        :type: bool
        """
        

        self._requires_matching_languages = requires_matching_languages

    @property
    def requires_matching_skills(self) -> bool:
        """
        Gets the requires_matching_skills of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching skills

        :return: The requires_matching_skills of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._requires_matching_skills

    @requires_matching_skills.setter
    def requires_matching_skills(self, requires_matching_skills: bool) -> None:
        """
        Sets the requires_matching_skills of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching skills

        :param requires_matching_skills: The requires_matching_skills of this ShiftTradeSettings.
        :type: bool
        """
        

        self._requires_matching_skills = requires_matching_skills

    @property
    def requires_matching_planning_groups(self) -> bool:
        """
        Gets the requires_matching_planning_groups of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching planning groups

        :return: The requires_matching_planning_groups of this ShiftTradeSettings.
        :rtype: bool
        """
        return self._requires_matching_planning_groups

    @requires_matching_planning_groups.setter
    def requires_matching_planning_groups(self, requires_matching_planning_groups: bool) -> None:
        """
        Sets the requires_matching_planning_groups of this ShiftTradeSettings.
        Whether to constrain shift trades to agents with matching planning groups

        :param requires_matching_planning_groups: The requires_matching_planning_groups of this ShiftTradeSettings.
        :type: bool
        """
        

        self._requires_matching_planning_groups = requires_matching_planning_groups

    @property
    def activity_category_rules(self) -> List['ShiftTradeActivityRule']:
        """
        Gets the activity_category_rules of this ShiftTradeSettings.
        Rules that specify what to do with activity categories that are part of a shift defined in a trade

        :return: The activity_category_rules of this ShiftTradeSettings.
        :rtype: list[ShiftTradeActivityRule]
        """
        return self._activity_category_rules

    @activity_category_rules.setter
    def activity_category_rules(self, activity_category_rules: List['ShiftTradeActivityRule']) -> None:
        """
        Sets the activity_category_rules of this ShiftTradeSettings.
        Rules that specify what to do with activity categories that are part of a shift defined in a trade

        :param activity_category_rules: The activity_category_rules of this ShiftTradeSettings.
        :type: list[ShiftTradeActivityRule]
        """
        

        self._activity_category_rules = activity_category_rules

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

