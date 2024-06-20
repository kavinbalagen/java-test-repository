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
    from . import AddressableEntityRef
    from . import PredictorModelBrief
    from . import PredictorSchedule
    from . import PredictorWorkloadBalancing

class Predictor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Predictor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'queues': 'list[AddressableEntityRef]',
            'kpi': 'str',
            'routing_timeout_seconds': 'int',
            'schedule': 'PredictorSchedule',
            'state': 'str',
            'date_created': 'datetime',
            'date_modified': 'datetime',
            'workload_balancing_config': 'PredictorWorkloadBalancing',
            'error_code': 'str',
            'models': 'list[PredictorModelBrief]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'queues': 'queues',
            'kpi': 'kpi',
            'routing_timeout_seconds': 'routingTimeoutSeconds',
            'schedule': 'schedule',
            'state': 'state',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'workload_balancing_config': 'workloadBalancingConfig',
            'error_code': 'errorCode',
            'models': 'models',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._queues = None
        self._kpi = None
        self._routing_timeout_seconds = None
        self._schedule = None
        self._state = None
        self._date_created = None
        self._date_modified = None
        self._workload_balancing_config = None
        self._error_code = None
        self._models = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Predictor.
        The globally unique identifier for the object.

        :return: The id of this Predictor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Predictor.
        The globally unique identifier for the object.

        :param id: The id of this Predictor.
        :type: str
        """
        

        self._id = id

    @property
    def queues(self) -> List['AddressableEntityRef']:
        """
        Gets the queues of this Predictor.
        The queue IDs associated with the predictor.

        :return: The queues of this Predictor.
        :rtype: list[AddressableEntityRef]
        """
        return self._queues

    @queues.setter
    def queues(self, queues: List['AddressableEntityRef']) -> None:
        """
        Sets the queues of this Predictor.
        The queue IDs associated with the predictor.

        :param queues: The queues of this Predictor.
        :type: list[AddressableEntityRef]
        """
        

        self._queues = queues

    @property
    def kpi(self) -> str:
        """
        Gets the kpi of this Predictor.
        The KPI that the predictor attempts to maximize/minimize.

        :return: The kpi of this Predictor.
        :rtype: str
        """
        return self._kpi

    @kpi.setter
    def kpi(self, kpi: str) -> None:
        """
        Sets the kpi of this Predictor.
        The KPI that the predictor attempts to maximize/minimize.

        :param kpi: The kpi of this Predictor.
        :type: str
        """
        

        self._kpi = kpi

    @property
    def routing_timeout_seconds(self) -> int:
        """
        Gets the routing_timeout_seconds of this Predictor.
        Number of seconds allocated to predictive routing before attempting a different routing method. This is a value between 12 and 900 seconds.

        :return: The routing_timeout_seconds of this Predictor.
        :rtype: int
        """
        return self._routing_timeout_seconds

    @routing_timeout_seconds.setter
    def routing_timeout_seconds(self, routing_timeout_seconds: int) -> None:
        """
        Sets the routing_timeout_seconds of this Predictor.
        Number of seconds allocated to predictive routing before attempting a different routing method. This is a value between 12 and 900 seconds.

        :param routing_timeout_seconds: The routing_timeout_seconds of this Predictor.
        :type: int
        """
        

        self._routing_timeout_seconds = routing_timeout_seconds

    @property
    def schedule(self) -> 'PredictorSchedule':
        """
        Gets the schedule of this Predictor.
        The predictor schedule that determines when the predictor is used for routing interactions.

        :return: The schedule of this Predictor.
        :rtype: PredictorSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule: 'PredictorSchedule') -> None:
        """
        Sets the schedule of this Predictor.
        The predictor schedule that determines when the predictor is used for routing interactions.

        :param schedule: The schedule of this Predictor.
        :type: PredictorSchedule
        """
        

        self._schedule = schedule

    @property
    def state(self) -> str:
        """
        Gets the state of this Predictor.
        The predictor state.

        :return: The state of this Predictor.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str) -> None:
        """
        Sets the state of this Predictor.
        The predictor state.

        :param state: The state of this Predictor.
        :type: str
        """
        if isinstance(state, int):
            state = str(state)
        allowed_values = ["Created", "Error", "Active"]
        if state.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for state -> " + state)
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def date_created(self) -> datetime:
        """
        Gets the date_created of this Predictor.
        DateTime indicating when the predictor was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_created of this Predictor.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime) -> None:
        """
        Sets the date_created of this Predictor.
        DateTime indicating when the predictor was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_created: The date_created of this Predictor.
        :type: datetime
        """
        

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """
        Gets the date_modified of this Predictor.
        DateTime indicating when the predictor was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The date_modified of this Predictor.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime) -> None:
        """
        Sets the date_modified of this Predictor.
        DateTime indicating when the predictor was last updated. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param date_modified: The date_modified of this Predictor.
        :type: datetime
        """
        

        self._date_modified = date_modified

    @property
    def workload_balancing_config(self) -> 'PredictorWorkloadBalancing':
        """
        Gets the workload_balancing_config of this Predictor.
        The predictor balancing configuration to enable workload balancing.

        :return: The workload_balancing_config of this Predictor.
        :rtype: PredictorWorkloadBalancing
        """
        return self._workload_balancing_config

    @workload_balancing_config.setter
    def workload_balancing_config(self, workload_balancing_config: 'PredictorWorkloadBalancing') -> None:
        """
        Sets the workload_balancing_config of this Predictor.
        The predictor balancing configuration to enable workload balancing.

        :param workload_balancing_config: The workload_balancing_config of this Predictor.
        :type: PredictorWorkloadBalancing
        """
        

        self._workload_balancing_config = workload_balancing_config

    @property
    def error_code(self) -> str:
        """
        Gets the error_code of this Predictor.
        Predictor error code - optional details on why the predictor went into error state.

        :return: The error_code of this Predictor.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code: str) -> None:
        """
        Sets the error_code of this Predictor.
        Predictor error code - optional details on why the predictor went into error state.

        :param error_code: The error_code of this Predictor.
        :type: str
        """
        

        self._error_code = error_code

    @property
    def models(self) -> List['PredictorModelBrief']:
        """
        Gets the models of this Predictor.
        Predictor's models

        :return: The models of this Predictor.
        :rtype: list[PredictorModelBrief]
        """
        return self._models

    @models.setter
    def models(self, models: List['PredictorModelBrief']) -> None:
        """
        Sets the models of this Predictor.
        Predictor's models

        :param models: The models of this Predictor.
        :type: list[PredictorModelBrief]
        """
        

        self._models = models

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Predictor.
        The URI for this object

        :return: The self_uri of this Predictor.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Predictor.
        The URI for this object

        :param self_uri: The self_uri of this Predictor.
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

