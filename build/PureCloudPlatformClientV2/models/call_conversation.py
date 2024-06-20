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
    from . import CallMediaParticipant
    from . import TransferResponse

class CallConversation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CallConversation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'participants': 'list[CallMediaParticipant]',
            'other_media_uris': 'list[str]',
            'recent_transfers': 'list[TransferResponse]',
            'utilization_label_id': 'str',
            'recording_state': 'str',
            'max_participants': 'int',
            'secure_pause': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'participants': 'participants',
            'other_media_uris': 'otherMediaUris',
            'recent_transfers': 'recentTransfers',
            'utilization_label_id': 'utilizationLabelId',
            'recording_state': 'recordingState',
            'max_participants': 'maxParticipants',
            'secure_pause': 'securePause',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._participants = None
        self._other_media_uris = None
        self._recent_transfers = None
        self._utilization_label_id = None
        self._recording_state = None
        self._max_participants = None
        self._secure_pause = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this CallConversation.
        The globally unique identifier for the object.

        :return: The id of this CallConversation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this CallConversation.
        The globally unique identifier for the object.

        :param id: The id of this CallConversation.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this CallConversation.


        :return: The name of this CallConversation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this CallConversation.


        :param name: The name of this CallConversation.
        :type: str
        """
        

        self._name = name

    @property
    def participants(self) -> List['CallMediaParticipant']:
        """
        Gets the participants of this CallConversation.
        The list of participants involved in the conversation.

        :return: The participants of this CallConversation.
        :rtype: list[CallMediaParticipant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants: List['CallMediaParticipant']) -> None:
        """
        Sets the participants of this CallConversation.
        The list of participants involved in the conversation.

        :param participants: The participants of this CallConversation.
        :type: list[CallMediaParticipant]
        """
        

        self._participants = participants

    @property
    def other_media_uris(self) -> List[str]:
        """
        Gets the other_media_uris of this CallConversation.
        The list of other media channels involved in the conversation.

        :return: The other_media_uris of this CallConversation.
        :rtype: list[str]
        """
        return self._other_media_uris

    @other_media_uris.setter
    def other_media_uris(self, other_media_uris: List[str]) -> None:
        """
        Sets the other_media_uris of this CallConversation.
        The list of other media channels involved in the conversation.

        :param other_media_uris: The other_media_uris of this CallConversation.
        :type: list[str]
        """
        

        self._other_media_uris = other_media_uris

    @property
    def recent_transfers(self) -> List['TransferResponse']:
        """
        Gets the recent_transfers of this CallConversation.
        The list of the most recent 20 transfer commands applied to this conversation.

        :return: The recent_transfers of this CallConversation.
        :rtype: list[TransferResponse]
        """
        return self._recent_transfers

    @recent_transfers.setter
    def recent_transfers(self, recent_transfers: List['TransferResponse']) -> None:
        """
        Sets the recent_transfers of this CallConversation.
        The list of the most recent 20 transfer commands applied to this conversation.

        :param recent_transfers: The recent_transfers of this CallConversation.
        :type: list[TransferResponse]
        """
        

        self._recent_transfers = recent_transfers

    @property
    def utilization_label_id(self) -> str:
        """
        Gets the utilization_label_id of this CallConversation.
        An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level

        :return: The utilization_label_id of this CallConversation.
        :rtype: str
        """
        return self._utilization_label_id

    @utilization_label_id.setter
    def utilization_label_id(self, utilization_label_id: str) -> None:
        """
        Sets the utilization_label_id of this CallConversation.
        An optional label that categorizes the conversation.  Max-utilization settings can be configured at a per-label level

        :param utilization_label_id: The utilization_label_id of this CallConversation.
        :type: str
        """
        

        self._utilization_label_id = utilization_label_id

    @property
    def recording_state(self) -> str:
        """
        Gets the recording_state of this CallConversation.


        :return: The recording_state of this CallConversation.
        :rtype: str
        """
        return self._recording_state

    @recording_state.setter
    def recording_state(self, recording_state: str) -> None:
        """
        Sets the recording_state of this CallConversation.


        :param recording_state: The recording_state of this CallConversation.
        :type: str
        """
        if isinstance(recording_state, int):
            recording_state = str(recording_state)
        allowed_values = ["none", "active", "paused"]
        if recording_state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for recording_state -> " + recording_state)
            self._recording_state = "outdated_sdk_version"
        else:
            self._recording_state = recording_state

    @property
    def max_participants(self) -> int:
        """
        Gets the max_participants of this CallConversation.
        If this is a conference conversation, then this field indicates the maximum number of participants allowed to participant in the conference.

        :return: The max_participants of this CallConversation.
        :rtype: int
        """
        return self._max_participants

    @max_participants.setter
    def max_participants(self, max_participants: int) -> None:
        """
        Sets the max_participants of this CallConversation.
        If this is a conference conversation, then this field indicates the maximum number of participants allowed to participant in the conference.

        :param max_participants: The max_participants of this CallConversation.
        :type: int
        """
        

        self._max_participants = max_participants

    @property
    def secure_pause(self) -> bool:
        """
        Gets the secure_pause of this CallConversation.
        True when the recording of this conversation is in secure pause status.

        :return: The secure_pause of this CallConversation.
        :rtype: bool
        """
        return self._secure_pause

    @secure_pause.setter
    def secure_pause(self, secure_pause: bool) -> None:
        """
        Sets the secure_pause of this CallConversation.
        True when the recording of this conversation is in secure pause status.

        :param secure_pause: The secure_pause of this CallConversation.
        :type: bool
        """
        

        self._secure_pause = secure_pause

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this CallConversation.
        The URI for this object

        :return: The self_uri of this CallConversation.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this CallConversation.
        The URI for this object

        :param self_uri: The self_uri of this CallConversation.
        :type: str
        """
        

        self._self_uri = self_uri

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
