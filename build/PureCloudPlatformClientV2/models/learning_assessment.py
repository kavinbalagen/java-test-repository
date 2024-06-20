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
    from . import AssessmentScoringSet

class LearningAssessment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        LearningAssessment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'assessment_id': 'str',
            'context_id': 'str',
            'assessment_form_id': 'str',
            'status': 'str',
            'answers': 'AssessmentScoringSet',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'date_submitted': 'datetime'
        }

        self.attribute_map = {
            'assessment_id': 'assessmentId',
            'context_id': 'contextId',
            'assessment_form_id': 'assessmentFormId',
            'status': 'status',
            'answers': 'answers',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'date_submitted': 'dateSubmitted'
        }

        self._assessment_id = None
        self._context_id = None
        self._assessment_form_id = None
        self._status = None
        self._answers = None
        self._date_created = None
        self._date_modified = None
        self._date_submitted = None

    @property
    def assessment_id(self) -> str:
        """
        Gets the assessment_id of this LearningAssessment.
        The Id of the assessment

        :return: The assessment_id of this LearningAssessment.
        :rtype: str
        """
        return self._assessment_id

    @assessment_id.setter
    def assessment_id(self, assessment_id: str) -> None:
        """
        Sets the assessment_id of this LearningAssessment.
        The Id of the assessment

        :param assessment_id: The assessment_id of this LearningAssessment.
        :type: str
        """
        

        self._assessment_id = assessment_id

    @property
    def context_id(self) -> str:
        """
        Gets the context_id of this LearningAssessment.
        The context Id of the related assessment form

        :return: The context_id of this LearningAssessment.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id: str) -> None:
        """
        Sets the context_id of this LearningAssessment.
        The context Id of the related assessment form

        :param context_id: The context_id of this LearningAssessment.
        :type: str
        """
        

        self._context_id = context_id

    @property
    def assessment_form_id(self) -> str:
        """
        Gets the assessment_form_id of this LearningAssessment.
        The Id of the related assessment form

        :return: The assessment_form_id of this LearningAssessment.
        :rtype: str
        """
        return self._assessment_form_id

    @assessment_form_id.setter
    def assessment_form_id(self, assessment_form_id: str) -> None:
        """
        Sets the assessment_form_id of this LearningAssessment.
        The Id of the related assessment form

        :param assessment_form_id: The assessment_form_id of this LearningAssessment.
        :type: str
        """
        

        self._assessment_form_id = assessment_form_id

    @property
    def status(self) -> str:
        """
        Gets the status of this LearningAssessment.
        Status of the assessment

        :return: The status of this LearningAssessment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str) -> None:
        """
        Sets the status of this LearningAssessment.
        Status of the assessment

        :param status: The status of this LearningAssessment.
        :type: str
        """
        if isinstance(status, int):
            status = str(status)
        allowed_values = ["Pending", "InProgress", "Finished"]
        if status.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for status -> " + status)
            self._status = "outdated_sdk_version"
        else:
            self._status = status

    @property
    def answers(self) -> 'AssessmentScoringSet':
        """
        Gets the answers of this LearningAssessment.
        Answers for the assessment

        :return: The answers of this LearningAssessment.
        :rtype: AssessmentScoringSet
        """
        return self._answers

    @answers.setter
    def answers(self, answers: 'AssessmentScoringSet') -> None:
        """
        Sets the answers of this LearningAssessment.
        Answers for the assessment

        :param answers: The answers of this LearningAssessment.
        :type: AssessmentScoringSet
        """
        

        self._answers = answers

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this LearningAssessment.
        Date the assessment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this LearningAssessment.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this LearningAssessment.
        Date the assessment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this LearningAssessment.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this LearningAssessment.
        Date the assessment was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this LearningAssessment.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this LearningAssessment.
        Date the assessment was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this LearningAssessment.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def date_submitted(self) -> datetime:
        """
        Gets the date_submitted of this LearningAssessment.
        Date the assessment was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_submitted of this LearningAssessment.
        :rtype: datetime
        """
        return self._date_submitted

    @date_submitted.setter
    def date_submitted(self, date_submitted: datetime) -> None:
        """
        Sets the date_submitted of this LearningAssessment.
        Date the assessment was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_submitted: The date_submitted of this LearningAssessment.
        :type: datetime
        """
        

        self._date_submitted = date_submitted

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

