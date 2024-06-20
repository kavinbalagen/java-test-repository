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
    from . import CalibrationAssignment
    from . import EvaluationAssignment
    from . import IntegrationExport
    from . import MediaTranscription
    from . import MeteredAssignmentByAgent
    from . import MeteredEvaluationAssignment
    from . import RetentionDuration

class CrossPlatformPolicyActions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        CrossPlatformPolicyActions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'retain_recording': 'bool',
            'delete_recording': 'bool',
            'always_delete': 'bool',
            'assign_evaluations': 'list[EvaluationAssignment]',
            'assign_metered_evaluations': 'list[MeteredEvaluationAssignment]',
            'assign_metered_assignment_by_agent': 'list[MeteredAssignmentByAgent]',
            'assign_calibrations': 'list[CalibrationAssignment]',
            'retention_duration': 'RetentionDuration',
            'media_transcriptions': 'list[MediaTranscription]',
            'integration_export': 'IntegrationExport'
        }

        self.attribute_map = {
            'retain_recording': 'retainRecording',
            'delete_recording': 'deleteRecording',
            'always_delete': 'alwaysDelete',
            'assign_evaluations': 'assignEvaluations',
            'assign_metered_evaluations': 'assignMeteredEvaluations',
            'assign_metered_assignment_by_agent': 'assignMeteredAssignmentByAgent',
            'assign_calibrations': 'assignCalibrations',
            'retention_duration': 'retentionDuration',
            'media_transcriptions': 'mediaTranscriptions',
            'integration_export': 'integrationExport'
        }

        self._retain_recording = None
        self._delete_recording = None
        self._always_delete = None
        self._assign_evaluations = None
        self._assign_metered_evaluations = None
        self._assign_metered_assignment_by_agent = None
        self._assign_calibrations = None
        self._retention_duration = None
        self._media_transcriptions = None
        self._integration_export = None

    @property
    def retain_recording(self) -> bool:
        """
        Gets the retain_recording of this CrossPlatformPolicyActions.
        true to retain the recording associated with the conversation. Default = true

        :return: The retain_recording of this CrossPlatformPolicyActions.
        :rtype: bool
        """
        return self._retain_recording

    @retain_recording.setter
    def retain_recording(self, retain_recording: bool) -> None:
        """
        Sets the retain_recording of this CrossPlatformPolicyActions.
        true to retain the recording associated with the conversation. Default = true

        :param retain_recording: The retain_recording of this CrossPlatformPolicyActions.
        :type: bool
        """
        

        self._retain_recording = retain_recording

    @property
    def delete_recording(self) -> bool:
        """
        Gets the delete_recording of this CrossPlatformPolicyActions.
        true to delete the recording associated with the conversation. If retainRecording = true, this will be ignored. Default = false

        :return: The delete_recording of this CrossPlatformPolicyActions.
        :rtype: bool
        """
        return self._delete_recording

    @delete_recording.setter
    def delete_recording(self, delete_recording: bool) -> None:
        """
        Sets the delete_recording of this CrossPlatformPolicyActions.
        true to delete the recording associated with the conversation. If retainRecording = true, this will be ignored. Default = false

        :param delete_recording: The delete_recording of this CrossPlatformPolicyActions.
        :type: bool
        """
        

        self._delete_recording = delete_recording

    @property
    def always_delete(self) -> bool:
        """
        Gets the always_delete of this CrossPlatformPolicyActions.
        true to delete the recording associated with the conversation regardless of the values of retainRecording or deleteRecording. Default = false

        :return: The always_delete of this CrossPlatformPolicyActions.
        :rtype: bool
        """
        return self._always_delete

    @always_delete.setter
    def always_delete(self, always_delete: bool) -> None:
        """
        Sets the always_delete of this CrossPlatformPolicyActions.
        true to delete the recording associated with the conversation regardless of the values of retainRecording or deleteRecording. Default = false

        :param always_delete: The always_delete of this CrossPlatformPolicyActions.
        :type: bool
        """
        

        self._always_delete = always_delete

    @property
    def assign_evaluations(self) -> List['EvaluationAssignment']:
        """
        Gets the assign_evaluations of this CrossPlatformPolicyActions.


        :return: The assign_evaluations of this CrossPlatformPolicyActions.
        :rtype: list[EvaluationAssignment]
        """
        return self._assign_evaluations

    @assign_evaluations.setter
    def assign_evaluations(self, assign_evaluations: List['EvaluationAssignment']) -> None:
        """
        Sets the assign_evaluations of this CrossPlatformPolicyActions.


        :param assign_evaluations: The assign_evaluations of this CrossPlatformPolicyActions.
        :type: list[EvaluationAssignment]
        """
        

        self._assign_evaluations = assign_evaluations

    @property
    def assign_metered_evaluations(self) -> List['MeteredEvaluationAssignment']:
        """
        Gets the assign_metered_evaluations of this CrossPlatformPolicyActions.


        :return: The assign_metered_evaluations of this CrossPlatformPolicyActions.
        :rtype: list[MeteredEvaluationAssignment]
        """
        return self._assign_metered_evaluations

    @assign_metered_evaluations.setter
    def assign_metered_evaluations(self, assign_metered_evaluations: List['MeteredEvaluationAssignment']) -> None:
        """
        Sets the assign_metered_evaluations of this CrossPlatformPolicyActions.


        :param assign_metered_evaluations: The assign_metered_evaluations of this CrossPlatformPolicyActions.
        :type: list[MeteredEvaluationAssignment]
        """
        

        self._assign_metered_evaluations = assign_metered_evaluations

    @property
    def assign_metered_assignment_by_agent(self) -> List['MeteredAssignmentByAgent']:
        """
        Gets the assign_metered_assignment_by_agent of this CrossPlatformPolicyActions.


        :return: The assign_metered_assignment_by_agent of this CrossPlatformPolicyActions.
        :rtype: list[MeteredAssignmentByAgent]
        """
        return self._assign_metered_assignment_by_agent

    @assign_metered_assignment_by_agent.setter
    def assign_metered_assignment_by_agent(self, assign_metered_assignment_by_agent: List['MeteredAssignmentByAgent']) -> None:
        """
        Sets the assign_metered_assignment_by_agent of this CrossPlatformPolicyActions.


        :param assign_metered_assignment_by_agent: The assign_metered_assignment_by_agent of this CrossPlatformPolicyActions.
        :type: list[MeteredAssignmentByAgent]
        """
        

        self._assign_metered_assignment_by_agent = assign_metered_assignment_by_agent

    @property
    def assign_calibrations(self) -> List['CalibrationAssignment']:
        """
        Gets the assign_calibrations of this CrossPlatformPolicyActions.


        :return: The assign_calibrations of this CrossPlatformPolicyActions.
        :rtype: list[CalibrationAssignment]
        """
        return self._assign_calibrations

    @assign_calibrations.setter
    def assign_calibrations(self, assign_calibrations: List['CalibrationAssignment']) -> None:
        """
        Sets the assign_calibrations of this CrossPlatformPolicyActions.


        :param assign_calibrations: The assign_calibrations of this CrossPlatformPolicyActions.
        :type: list[CalibrationAssignment]
        """
        

        self._assign_calibrations = assign_calibrations

    @property
    def retention_duration(self) -> 'RetentionDuration':
        """
        Gets the retention_duration of this CrossPlatformPolicyActions.


        :return: The retention_duration of this CrossPlatformPolicyActions.
        :rtype: RetentionDuration
        """
        return self._retention_duration

    @retention_duration.setter
    def retention_duration(self, retention_duration: 'RetentionDuration') -> None:
        """
        Sets the retention_duration of this CrossPlatformPolicyActions.


        :param retention_duration: The retention_duration of this CrossPlatformPolicyActions.
        :type: RetentionDuration
        """
        

        self._retention_duration = retention_duration

    @property
    def media_transcriptions(self) -> List['MediaTranscription']:
        """
        Gets the media_transcriptions of this CrossPlatformPolicyActions.


        :return: The media_transcriptions of this CrossPlatformPolicyActions.
        :rtype: list[MediaTranscription]
        """
        return self._media_transcriptions

    @media_transcriptions.setter
    def media_transcriptions(self, media_transcriptions: List['MediaTranscription']) -> None:
        """
        Sets the media_transcriptions of this CrossPlatformPolicyActions.


        :param media_transcriptions: The media_transcriptions of this CrossPlatformPolicyActions.
        :type: list[MediaTranscription]
        """
        

        self._media_transcriptions = media_transcriptions

    @property
    def integration_export(self) -> 'IntegrationExport':
        """
        Gets the integration_export of this CrossPlatformPolicyActions.
        Policy action for exporting recordings using an integration to 3rd party s3.

        :return: The integration_export of this CrossPlatformPolicyActions.
        :rtype: IntegrationExport
        """
        return self._integration_export

    @integration_export.setter
    def integration_export(self, integration_export: 'IntegrationExport') -> None:
        """
        Sets the integration_export of this CrossPlatformPolicyActions.
        Policy action for exporting recordings using an integration to 3rd party s3.

        :param integration_export: The integration_export of this CrossPlatformPolicyActions.
        :type: IntegrationExport
        """
        

        self._integration_export = integration_export

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
