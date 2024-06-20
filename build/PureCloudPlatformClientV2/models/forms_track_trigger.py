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


class FormsTrackTrigger(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        FormsTrackTrigger - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'selector': 'str',
            'form_name': 'str',
            'capture_data_on_form_abandon': 'bool',
            'capture_data_on_form_submit': 'bool'
        }

        self.attribute_map = {
            'selector': 'selector',
            'form_name': 'formName',
            'capture_data_on_form_abandon': 'captureDataOnFormAbandon',
            'capture_data_on_form_submit': 'captureDataOnFormSubmit'
        }

        self._selector = None
        self._form_name = None
        self._capture_data_on_form_abandon = None
        self._capture_data_on_form_submit = None

    @property
    def selector(self) -> str:
        """
        Gets the selector of this FormsTrackTrigger.
        Form element that triggers the form submitted or abandoned event.

        :return: The selector of this FormsTrackTrigger.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector: str) -> None:
        """
        Sets the selector of this FormsTrackTrigger.
        Form element that triggers the form submitted or abandoned event.

        :param selector: The selector of this FormsTrackTrigger.
        :type: str
        """
        

        self._selector = selector

    @property
    def form_name(self) -> str:
        """
        Gets the form_name of this FormsTrackTrigger.
        Prefix for the form submitted or abandoned event name.

        :return: The form_name of this FormsTrackTrigger.
        :rtype: str
        """
        return self._form_name

    @form_name.setter
    def form_name(self, form_name: str) -> None:
        """
        Sets the form_name of this FormsTrackTrigger.
        Prefix for the form submitted or abandoned event name.

        :param form_name: The form_name of this FormsTrackTrigger.
        :type: str
        """
        

        self._form_name = form_name

    @property
    def capture_data_on_form_abandon(self) -> bool:
        """
        Gets the capture_data_on_form_abandon of this FormsTrackTrigger.
        Whether to capture the form data in the form abandoned event.

        :return: The capture_data_on_form_abandon of this FormsTrackTrigger.
        :rtype: bool
        """
        return self._capture_data_on_form_abandon

    @capture_data_on_form_abandon.setter
    def capture_data_on_form_abandon(self, capture_data_on_form_abandon: bool) -> None:
        """
        Sets the capture_data_on_form_abandon of this FormsTrackTrigger.
        Whether to capture the form data in the form abandoned event.

        :param capture_data_on_form_abandon: The capture_data_on_form_abandon of this FormsTrackTrigger.
        :type: bool
        """
        

        self._capture_data_on_form_abandon = capture_data_on_form_abandon

    @property
    def capture_data_on_form_submit(self) -> bool:
        """
        Gets the capture_data_on_form_submit of this FormsTrackTrigger.
        Whether to capture the form data in the form submitted event.

        :return: The capture_data_on_form_submit of this FormsTrackTrigger.
        :rtype: bool
        """
        return self._capture_data_on_form_submit

    @capture_data_on_form_submit.setter
    def capture_data_on_form_submit(self, capture_data_on_form_submit: bool) -> None:
        """
        Sets the capture_data_on_form_submit of this FormsTrackTrigger.
        Whether to capture the form data in the form submitted event.

        :param capture_data_on_form_submit: The capture_data_on_form_submit of this FormsTrackTrigger.
        :type: bool
        """
        

        self._capture_data_on_form_submit = capture_data_on_form_submit

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

