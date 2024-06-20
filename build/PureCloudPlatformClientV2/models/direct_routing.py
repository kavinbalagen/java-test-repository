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
    from . import DirectRoutingMediaSettings

class DirectRouting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DirectRouting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'call_media_settings': 'DirectRoutingMediaSettings',
            'email_media_settings': 'DirectRoutingMediaSettings',
            'message_media_settings': 'DirectRoutingMediaSettings',
            'backup_queue_id': 'str',
            'wait_for_agent': 'bool',
            'agent_wait_seconds': 'int'
        }

        self.attribute_map = {
            'call_media_settings': 'callMediaSettings',
            'email_media_settings': 'emailMediaSettings',
            'message_media_settings': 'messageMediaSettings',
            'backup_queue_id': 'backupQueueId',
            'wait_for_agent': 'waitForAgent',
            'agent_wait_seconds': 'agentWaitSeconds'
        }

        self._call_media_settings = None
        self._email_media_settings = None
        self._message_media_settings = None
        self._backup_queue_id = None
        self._wait_for_agent = None
        self._agent_wait_seconds = None

    @property
    def call_media_settings(self) -> 'DirectRoutingMediaSettings':
        """
        Gets the call_media_settings of this DirectRouting.
        Direct Routing Settings specific to Call media.

        :return: The call_media_settings of this DirectRouting.
        :rtype: DirectRoutingMediaSettings
        """
        return self._call_media_settings

    @call_media_settings.setter
    def call_media_settings(self, call_media_settings: 'DirectRoutingMediaSettings') -> None:
        """
        Sets the call_media_settings of this DirectRouting.
        Direct Routing Settings specific to Call media.

        :param call_media_settings: The call_media_settings of this DirectRouting.
        :type: DirectRoutingMediaSettings
        """
        

        self._call_media_settings = call_media_settings

    @property
    def email_media_settings(self) -> 'DirectRoutingMediaSettings':
        """
        Gets the email_media_settings of this DirectRouting.
        Direct Routing Settings specific to Email media.

        :return: The email_media_settings of this DirectRouting.
        :rtype: DirectRoutingMediaSettings
        """
        return self._email_media_settings

    @email_media_settings.setter
    def email_media_settings(self, email_media_settings: 'DirectRoutingMediaSettings') -> None:
        """
        Sets the email_media_settings of this DirectRouting.
        Direct Routing Settings specific to Email media.

        :param email_media_settings: The email_media_settings of this DirectRouting.
        :type: DirectRoutingMediaSettings
        """
        

        self._email_media_settings = email_media_settings

    @property
    def message_media_settings(self) -> 'DirectRoutingMediaSettings':
        """
        Gets the message_media_settings of this DirectRouting.
        Direct Routing Settings specific to Message media.

        :return: The message_media_settings of this DirectRouting.
        :rtype: DirectRoutingMediaSettings
        """
        return self._message_media_settings

    @message_media_settings.setter
    def message_media_settings(self, message_media_settings: 'DirectRoutingMediaSettings') -> None:
        """
        Sets the message_media_settings of this DirectRouting.
        Direct Routing Settings specific to Message media.

        :param message_media_settings: The message_media_settings of this DirectRouting.
        :type: DirectRoutingMediaSettings
        """
        

        self._message_media_settings = message_media_settings

    @property
    def backup_queue_id(self) -> str:
        """
        Gets the backup_queue_id of this DirectRouting.
        ID of another queue to be used as the default backup if an agent does not have their Backup Settings configured. If not set, the current queue will be used as backup, but with Direct Routing criteria removed from the conversation.

        :return: The backup_queue_id of this DirectRouting.
        :rtype: str
        """
        return self._backup_queue_id

    @backup_queue_id.setter
    def backup_queue_id(self, backup_queue_id: str) -> None:
        """
        Sets the backup_queue_id of this DirectRouting.
        ID of another queue to be used as the default backup if an agent does not have their Backup Settings configured. If not set, the current queue will be used as backup, but with Direct Routing criteria removed from the conversation.

        :param backup_queue_id: The backup_queue_id of this DirectRouting.
        :type: str
        """
        

        self._backup_queue_id = backup_queue_id

    @property
    def wait_for_agent(self) -> bool:
        """
        Gets the wait_for_agent of this DirectRouting.
        Flag indicating if Direct Routing interactions should wait for Direct Routing agent or go immediately to selected backup.

        :return: The wait_for_agent of this DirectRouting.
        :rtype: bool
        """
        return self._wait_for_agent

    @wait_for_agent.setter
    def wait_for_agent(self, wait_for_agent: bool) -> None:
        """
        Sets the wait_for_agent of this DirectRouting.
        Flag indicating if Direct Routing interactions should wait for Direct Routing agent or go immediately to selected backup.

        :param wait_for_agent: The wait_for_agent of this DirectRouting.
        :type: bool
        """
        

        self._wait_for_agent = wait_for_agent

    @property
    def agent_wait_seconds(self) -> int:
        """
        Gets the agent_wait_seconds of this DirectRouting.
        Time (in seconds) that a Direct Routing interaction will wait for Direct Routing agent before going to selected backup. Valid range [60, 864000].

        :return: The agent_wait_seconds of this DirectRouting.
        :rtype: int
        """
        return self._agent_wait_seconds

    @agent_wait_seconds.setter
    def agent_wait_seconds(self, agent_wait_seconds: int) -> None:
        """
        Sets the agent_wait_seconds of this DirectRouting.
        Time (in seconds) that a Direct Routing interaction will wait for Direct Routing agent before going to selected backup. Valid range [60, 864000].

        :param agent_wait_seconds: The agent_wait_seconds of this DirectRouting.
        :type: int
        """
        

        self._agent_wait_seconds = agent_wait_seconds

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

