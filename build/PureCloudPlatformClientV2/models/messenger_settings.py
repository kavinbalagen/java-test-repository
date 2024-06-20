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
    from . import FileUploadSettings
    from . import LauncherButtonSettings
    from . import MessengerApps
    from . import MessengerHomeScreen
    from . import MessengerStyles

class MessengerSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MessengerSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'enabled': 'bool',
            'styles': 'MessengerStyles',
            'launcher_button': 'LauncherButtonSettings',
            'file_upload': 'FileUploadSettings',
            'apps': 'MessengerApps',
            'home_screen': 'MessengerHomeScreen'
        }

        self.attribute_map = {
            'enabled': 'enabled',
            'styles': 'styles',
            'launcher_button': 'launcherButton',
            'file_upload': 'fileUpload',
            'apps': 'apps',
            'home_screen': 'homeScreen'
        }

        self._enabled = None
        self._styles = None
        self._launcher_button = None
        self._file_upload = None
        self._apps = None
        self._home_screen = None

    @property
    def enabled(self) -> bool:
        """
        Gets the enabled of this MessengerSettings.
        Whether or not messenger is enabled

        :return: The enabled of this MessengerSettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled: bool) -> None:
        """
        Sets the enabled of this MessengerSettings.
        Whether or not messenger is enabled

        :param enabled: The enabled of this MessengerSettings.
        :type: bool
        """
        

        self._enabled = enabled

    @property
    def styles(self) -> 'MessengerStyles':
        """
        Gets the styles of this MessengerSettings.
        The style settings for messenger

        :return: The styles of this MessengerSettings.
        :rtype: MessengerStyles
        """
        return self._styles

    @styles.setter
    def styles(self, styles: 'MessengerStyles') -> None:
        """
        Sets the styles of this MessengerSettings.
        The style settings for messenger

        :param styles: The styles of this MessengerSettings.
        :type: MessengerStyles
        """
        

        self._styles = styles

    @property
    def launcher_button(self) -> 'LauncherButtonSettings':
        """
        Gets the launcher_button of this MessengerSettings.
        The launcher button settings for messenger

        :return: The launcher_button of this MessengerSettings.
        :rtype: LauncherButtonSettings
        """
        return self._launcher_button

    @launcher_button.setter
    def launcher_button(self, launcher_button: 'LauncherButtonSettings') -> None:
        """
        Sets the launcher_button of this MessengerSettings.
        The launcher button settings for messenger

        :param launcher_button: The launcher_button of this MessengerSettings.
        :type: LauncherButtonSettings
        """
        

        self._launcher_button = launcher_button

    @property
    def file_upload(self) -> 'FileUploadSettings':
        """
        Gets the file_upload of this MessengerSettings.
        The file upload settings for messenger

        :return: The file_upload of this MessengerSettings.
        :rtype: FileUploadSettings
        """
        return self._file_upload

    @file_upload.setter
    def file_upload(self, file_upload: 'FileUploadSettings') -> None:
        """
        Sets the file_upload of this MessengerSettings.
        The file upload settings for messenger

        :param file_upload: The file_upload of this MessengerSettings.
        :type: FileUploadSettings
        """
        

        self._file_upload = file_upload

    @property
    def apps(self) -> 'MessengerApps':
        """
        Gets the apps of this MessengerSettings.
        The apps embedded in the messenger

        :return: The apps of this MessengerSettings.
        :rtype: MessengerApps
        """
        return self._apps

    @apps.setter
    def apps(self, apps: 'MessengerApps') -> None:
        """
        Sets the apps of this MessengerSettings.
        The apps embedded in the messenger

        :param apps: The apps of this MessengerSettings.
        :type: MessengerApps
        """
        

        self._apps = apps

    @property
    def home_screen(self) -> 'MessengerHomeScreen':
        """
        Gets the home_screen of this MessengerSettings.
        The homescreen settings for messenger

        :return: The home_screen of this MessengerSettings.
        :rtype: MessengerHomeScreen
        """
        return self._home_screen

    @home_screen.setter
    def home_screen(self, home_screen: 'MessengerHomeScreen') -> None:
        """
        Sets the home_screen of this MessengerSettings.
        The homescreen settings for messenger

        :param home_screen: The home_screen of this MessengerSettings.
        :type: MessengerHomeScreen
        """
        

        self._home_screen = home_screen

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
