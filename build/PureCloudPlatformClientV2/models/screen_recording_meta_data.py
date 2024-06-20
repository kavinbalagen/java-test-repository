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


class ScreenRecordingMetaData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        ScreenRecordingMetaData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'track_id': 'str',
            'media_id': 'str',
            'screen_id': 'str',
            'origin_x': 'int',
            'origin_y': 'int',
            'primary': 'bool',
            'main': 'bool'
        }

        self.attribute_map = {
            'track_id': 'trackId',
            'media_id': 'mediaId',
            'screen_id': 'screenId',
            'origin_x': 'originX',
            'origin_y': 'originY',
            'primary': 'primary',
            'main': 'main'
        }

        self._track_id = None
        self._media_id = None
        self._screen_id = None
        self._origin_x = None
        self._origin_y = None
        self._primary = None
        self._main = None

    @property
    def track_id(self) -> str:
        """
        Gets the track_id of this ScreenRecordingMetaData.


        :return: The track_id of this ScreenRecordingMetaData.
        :rtype: str
        """
        return self._track_id

    @track_id.setter
    def track_id(self, track_id: str) -> None:
        """
        Sets the track_id of this ScreenRecordingMetaData.


        :param track_id: The track_id of this ScreenRecordingMetaData.
        :type: str
        """
        

        self._track_id = track_id

    @property
    def media_id(self) -> str:
        """
        Gets the media_id of this ScreenRecordingMetaData.


        :return: The media_id of this ScreenRecordingMetaData.
        :rtype: str
        """
        return self._media_id

    @media_id.setter
    def media_id(self, media_id: str) -> None:
        """
        Sets the media_id of this ScreenRecordingMetaData.


        :param media_id: The media_id of this ScreenRecordingMetaData.
        :type: str
        """
        

        self._media_id = media_id

    @property
    def screen_id(self) -> str:
        """
        Gets the screen_id of this ScreenRecordingMetaData.


        :return: The screen_id of this ScreenRecordingMetaData.
        :rtype: str
        """
        return self._screen_id

    @screen_id.setter
    def screen_id(self, screen_id: str) -> None:
        """
        Sets the screen_id of this ScreenRecordingMetaData.


        :param screen_id: The screen_id of this ScreenRecordingMetaData.
        :type: str
        """
        

        self._screen_id = screen_id

    @property
    def origin_x(self) -> int:
        """
        Gets the origin_x of this ScreenRecordingMetaData.


        :return: The origin_x of this ScreenRecordingMetaData.
        :rtype: int
        """
        return self._origin_x

    @origin_x.setter
    def origin_x(self, origin_x: int) -> None:
        """
        Sets the origin_x of this ScreenRecordingMetaData.


        :param origin_x: The origin_x of this ScreenRecordingMetaData.
        :type: int
        """
        

        self._origin_x = origin_x

    @property
    def origin_y(self) -> int:
        """
        Gets the origin_y of this ScreenRecordingMetaData.


        :return: The origin_y of this ScreenRecordingMetaData.
        :rtype: int
        """
        return self._origin_y

    @origin_y.setter
    def origin_y(self, origin_y: int) -> None:
        """
        Sets the origin_y of this ScreenRecordingMetaData.


        :param origin_y: The origin_y of this ScreenRecordingMetaData.
        :type: int
        """
        

        self._origin_y = origin_y

    @property
    def primary(self) -> bool:
        """
        Gets the primary of this ScreenRecordingMetaData.


        :return: The primary of this ScreenRecordingMetaData.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary: bool) -> None:
        """
        Sets the primary of this ScreenRecordingMetaData.


        :param primary: The primary of this ScreenRecordingMetaData.
        :type: bool
        """
        

        self._primary = primary

    @property
    def main(self) -> bool:
        """
        Gets the main of this ScreenRecordingMetaData.


        :return: The main of this ScreenRecordingMetaData.
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main: bool) -> None:
        """
        Sets the main of this ScreenRecordingMetaData.


        :param main: The main of this ScreenRecordingMetaData.
        :type: bool
        """
        

        self._main = main

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

