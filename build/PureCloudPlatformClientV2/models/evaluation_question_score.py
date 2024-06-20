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


class EvaluationQuestionScore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EvaluationQuestionScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'question_id': 'str',
            'answer_id': 'str',
            'score': 'int',
            'marked_na': 'bool',
            'system_marked_na': 'bool',
            'assisted_answer_id': 'str',
            'failed_kill_question': 'bool',
            'comments': 'str'
        }

        self.attribute_map = {
            'question_id': 'questionId',
            'answer_id': 'answerId',
            'score': 'score',
            'marked_na': 'markedNA',
            'system_marked_na': 'systemMarkedNA',
            'assisted_answer_id': 'assistedAnswerId',
            'failed_kill_question': 'failedKillQuestion',
            'comments': 'comments'
        }

        self._question_id = None
        self._answer_id = None
        self._score = None
        self._marked_na = None
        self._system_marked_na = None
        self._assisted_answer_id = None
        self._failed_kill_question = None
        self._comments = None

    @property
    def question_id(self) -> str:
        """
        Gets the question_id of this EvaluationQuestionScore.


        :return: The question_id of this EvaluationQuestionScore.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id: str) -> None:
        """
        Sets the question_id of this EvaluationQuestionScore.


        :param question_id: The question_id of this EvaluationQuestionScore.
        :type: str
        """
        

        self._question_id = question_id

    @property
    def answer_id(self) -> str:
        """
        Gets the answer_id of this EvaluationQuestionScore.


        :return: The answer_id of this EvaluationQuestionScore.
        :rtype: str
        """
        return self._answer_id

    @answer_id.setter
    def answer_id(self, answer_id: str) -> None:
        """
        Sets the answer_id of this EvaluationQuestionScore.


        :param answer_id: The answer_id of this EvaluationQuestionScore.
        :type: str
        """
        

        self._answer_id = answer_id

    @property
    def score(self) -> int:
        """
        Gets the score of this EvaluationQuestionScore.
        Unweighted score of the question

        :return: The score of this EvaluationQuestionScore.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score: int) -> None:
        """
        Sets the score of this EvaluationQuestionScore.
        Unweighted score of the question

        :param score: The score of this EvaluationQuestionScore.
        :type: int
        """
        

        self._score = score

    @property
    def marked_na(self) -> bool:
        """
        Gets the marked_na of this EvaluationQuestionScore.
        True when the evaluation is submitted with a question that does not have an answer. Only allowed when naEnabled is true or if set by the system

        :return: The marked_na of this EvaluationQuestionScore.
        :rtype: bool
        """
        return self._marked_na

    @marked_na.setter
    def marked_na(self, marked_na: bool) -> None:
        """
        Sets the marked_na of this EvaluationQuestionScore.
        True when the evaluation is submitted with a question that does not have an answer. Only allowed when naEnabled is true or if set by the system

        :param marked_na: The marked_na of this EvaluationQuestionScore.
        :type: bool
        """
        

        self._marked_na = marked_na

    @property
    def system_marked_na(self) -> bool:
        """
        Gets the system_marked_na of this EvaluationQuestionScore.
        If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false.

        :return: The system_marked_na of this EvaluationQuestionScore.
        :rtype: bool
        """
        return self._system_marked_na

    @system_marked_na.setter
    def system_marked_na(self, system_marked_na: bool) -> None:
        """
        Sets the system_marked_na of this EvaluationQuestionScore.
        If markedNA is true, systemMarkedNA indicates whether it was marked by a user or by the system due to visibility conditions. Always false if markedNA is false.

        :param system_marked_na: The system_marked_na of this EvaluationQuestionScore.
        :type: bool
        """
        

        self._system_marked_na = system_marked_na

    @property
    def assisted_answer_id(self) -> str:
        """
        Gets the assisted_answer_id of this EvaluationQuestionScore.
        AnswerId found with evaluation assistance conditions

        :return: The assisted_answer_id of this EvaluationQuestionScore.
        :rtype: str
        """
        return self._assisted_answer_id

    @assisted_answer_id.setter
    def assisted_answer_id(self, assisted_answer_id: str) -> None:
        """
        Sets the assisted_answer_id of this EvaluationQuestionScore.
        AnswerId found with evaluation assistance conditions

        :param assisted_answer_id: The assisted_answer_id of this EvaluationQuestionScore.
        :type: str
        """
        

        self._assisted_answer_id = assisted_answer_id

    @property
    def failed_kill_question(self) -> bool:
        """
        Gets the failed_kill_question of this EvaluationQuestionScore.
        Applicable only on fatal questions. Indicates that the answer selected was not the highest score available for the question

        :return: The failed_kill_question of this EvaluationQuestionScore.
        :rtype: bool
        """
        return self._failed_kill_question

    @failed_kill_question.setter
    def failed_kill_question(self, failed_kill_question: bool) -> None:
        """
        Sets the failed_kill_question of this EvaluationQuestionScore.
        Applicable only on fatal questions. Indicates that the answer selected was not the highest score available for the question

        :param failed_kill_question: The failed_kill_question of this EvaluationQuestionScore.
        :type: bool
        """
        

        self._failed_kill_question = failed_kill_question

    @property
    def comments(self) -> str:
        """
        Gets the comments of this EvaluationQuestionScore.
        Comments from the evaluator specific to this question

        :return: The comments of this EvaluationQuestionScore.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments: str) -> None:
        """
        Sets the comments of this EvaluationQuestionScore.
        Comments from the evaluator specific to this question

        :param comments: The comments of this EvaluationQuestionScore.
        :type: str
        """
        

        self._comments = comments

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

