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
    from . import AssessmentForm
    from . import AssessmentScoringSet

class LearningAssessmentScoringRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LearningAssessmentScoringRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'assessment_form': 'AssessmentForm',
            'answers': 'AssessmentScoringSet'
        }

        self.attribute_map = {
            'assessment_form': 'assessmentForm',
            'answers': 'answers'
        }

        self._assessment_form = None
        self._answers = None

    @property
    def assessment_form(self) -> 'AssessmentForm':
        """
        Gets the assessment_form of this LearningAssessmentScoringRequest.
        The assessment form to score against

        :return: The assessment_form of this LearningAssessmentScoringRequest.
        :rtype: AssessmentForm
        """
        return self._assessment_form

    @assessment_form.setter
    def assessment_form(self, assessment_form: 'AssessmentForm') -> None:
        """
        Sets the assessment_form of this LearningAssessmentScoringRequest.
        The assessment form to score against

        :param assessment_form: The assessment_form of this LearningAssessmentScoringRequest.
        :type: AssessmentForm
        """
        

        self._assessment_form = assessment_form

    @property
    def answers(self) -> 'AssessmentScoringSet':
        """
        Gets the answers of this LearningAssessmentScoringRequest.
        The answers to score

        :return: The answers of this LearningAssessmentScoringRequest.
        :rtype: AssessmentScoringSet
        """
        return self._answers

    @answers.setter
    def answers(self, answers: 'AssessmentScoringSet') -> None:
        """
        Sets the answers of this LearningAssessmentScoringRequest.
        The answers to score

        :param answers: The answers of this LearningAssessmentScoringRequest.
        :type: AssessmentScoringSet
        """
        

        self._answers = answers

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

