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


class EdgeMetricsNetwork(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EdgeMetricsNetwork - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ifname': 'str',
            'sent_bytes_per_sec': 'int',
            'received_bytes_per_sec': 'int',
            'bandwidth_bits_per_sec': 'float',
            'utilization_pct': 'float'
        }

        self.attribute_map = {
            'ifname': 'ifname',
            'sent_bytes_per_sec': 'sentBytesPerSec',
            'received_bytes_per_sec': 'receivedBytesPerSec',
            'bandwidth_bits_per_sec': 'bandwidthBitsPerSec',
            'utilization_pct': 'utilizationPct'
        }

        self._ifname = None
        self._sent_bytes_per_sec = None
        self._received_bytes_per_sec = None
        self._bandwidth_bits_per_sec = None
        self._utilization_pct = None

    @property
    def ifname(self) -> str:
        """
        Gets the ifname of this EdgeMetricsNetwork.
        Identifier for the network adapter.

        :return: The ifname of this EdgeMetricsNetwork.
        :rtype: str
        """
        return self._ifname

    @ifname.setter
    def ifname(self, ifname: str) -> None:
        """
        Sets the ifname of this EdgeMetricsNetwork.
        Identifier for the network adapter.

        :param ifname: The ifname of this EdgeMetricsNetwork.
        :type: str
        """
        

        self._ifname = ifname

    @property
    def sent_bytes_per_sec(self) -> int:
        """
        Gets the sent_bytes_per_sec of this EdgeMetricsNetwork.
        Number of byes sent per second.

        :return: The sent_bytes_per_sec of this EdgeMetricsNetwork.
        :rtype: int
        """
        return self._sent_bytes_per_sec

    @sent_bytes_per_sec.setter
    def sent_bytes_per_sec(self, sent_bytes_per_sec: int) -> None:
        """
        Sets the sent_bytes_per_sec of this EdgeMetricsNetwork.
        Number of byes sent per second.

        :param sent_bytes_per_sec: The sent_bytes_per_sec of this EdgeMetricsNetwork.
        :type: int
        """
        

        self._sent_bytes_per_sec = sent_bytes_per_sec

    @property
    def received_bytes_per_sec(self) -> int:
        """
        Gets the received_bytes_per_sec of this EdgeMetricsNetwork.
        Number of byes received per second.

        :return: The received_bytes_per_sec of this EdgeMetricsNetwork.
        :rtype: int
        """
        return self._received_bytes_per_sec

    @received_bytes_per_sec.setter
    def received_bytes_per_sec(self, received_bytes_per_sec: int) -> None:
        """
        Sets the received_bytes_per_sec of this EdgeMetricsNetwork.
        Number of byes received per second.

        :param received_bytes_per_sec: The received_bytes_per_sec of this EdgeMetricsNetwork.
        :type: int
        """
        

        self._received_bytes_per_sec = received_bytes_per_sec

    @property
    def bandwidth_bits_per_sec(self) -> float:
        """
        Gets the bandwidth_bits_per_sec of this EdgeMetricsNetwork.
        Total bandwidth of the adapter in bits per second.

        :return: The bandwidth_bits_per_sec of this EdgeMetricsNetwork.
        :rtype: float
        """
        return self._bandwidth_bits_per_sec

    @bandwidth_bits_per_sec.setter
    def bandwidth_bits_per_sec(self, bandwidth_bits_per_sec: float) -> None:
        """
        Sets the bandwidth_bits_per_sec of this EdgeMetricsNetwork.
        Total bandwidth of the adapter in bits per second.

        :param bandwidth_bits_per_sec: The bandwidth_bits_per_sec of this EdgeMetricsNetwork.
        :type: float
        """
        

        self._bandwidth_bits_per_sec = bandwidth_bits_per_sec

    @property
    def utilization_pct(self) -> float:
        """
        Gets the utilization_pct of this EdgeMetricsNetwork.
        Percent utilization of the network adapter.

        :return: The utilization_pct of this EdgeMetricsNetwork.
        :rtype: float
        """
        return self._utilization_pct

    @utilization_pct.setter
    def utilization_pct(self, utilization_pct: float) -> None:
        """
        Sets the utilization_pct of this EdgeMetricsNetwork.
        Percent utilization of the network adapter.

        :param utilization_pct: The utilization_pct of this EdgeMetricsNetwork.
        :type: float
        """
        

        self._utilization_pct = utilization_pct

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
