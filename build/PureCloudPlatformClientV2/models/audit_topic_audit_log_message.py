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
    from . import AuditTopicAddressableEntityRef
    from . import AuditTopicDomainEntityRef
    from . import AuditTopicMessageInfo
    from . import AuditTopicPropertyChange

class AuditTopicAuditLogMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        AuditTopicAuditLogMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'user_home_org_id': 'str',
            'username': 'AuditTopicDomainEntityRef',
            'user_display': 'str',
            'client_id': 'AuditTopicAddressableEntityRef',
            'remote_ip': 'list[str]',
            'service_name': 'str',
            'level': 'str',
            'event_time': 'datetime',
            'message': 'AuditTopicMessageInfo',
            'action': 'str',
            'entity_type': 'str',
            'entity': 'AuditTopicDomainEntityRef',
            'property_changes': 'list[AuditTopicPropertyChange]',
            'context': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'user_home_org_id': 'userHomeOrgId',
            'username': 'username',
            'user_display': 'userDisplay',
            'client_id': 'clientId',
            'remote_ip': 'remoteIp',
            'service_name': 'serviceName',
            'level': 'level',
            'event_time': 'eventTime',
            'message': 'message',
            'action': 'action',
            'entity_type': 'entityType',
            'entity': 'entity',
            'property_changes': 'propertyChanges',
            'context': 'context'
        }

        self._id = None
        self._user_id = None
        self._user_home_org_id = None
        self._username = None
        self._user_display = None
        self._client_id = None
        self._remote_ip = None
        self._service_name = None
        self._level = None
        self._event_time = None
        self._message = None
        self._action = None
        self._entity_type = None
        self._entity = None
        self._property_changes = None
        self._context = None

    @property
    def id(self) -> str:
        """
        Gets the id of this AuditTopicAuditLogMessage.


        :return: The id of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this AuditTopicAuditLogMessage.


        :param id: The id of this AuditTopicAuditLogMessage.
        :type: str
        """
        

        self._id = id

    @property
    def user_id(self) -> str:
        """
        Gets the user_id of this AuditTopicAuditLogMessage.


        :return: The user_id of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        """
        Sets the user_id of this AuditTopicAuditLogMessage.


        :param user_id: The user_id of this AuditTopicAuditLogMessage.
        :type: str
        """
        

        self._user_id = user_id

    @property
    def user_home_org_id(self) -> str:
        """
        Gets the user_home_org_id of this AuditTopicAuditLogMessage.


        :return: The user_home_org_id of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._user_home_org_id

    @user_home_org_id.setter
    def user_home_org_id(self, user_home_org_id: str) -> None:
        """
        Sets the user_home_org_id of this AuditTopicAuditLogMessage.


        :param user_home_org_id: The user_home_org_id of this AuditTopicAuditLogMessage.
        :type: str
        """
        

        self._user_home_org_id = user_home_org_id

    @property
    def username(self) -> 'AuditTopicDomainEntityRef':
        """
        Gets the username of this AuditTopicAuditLogMessage.


        :return: The username of this AuditTopicAuditLogMessage.
        :rtype: AuditTopicDomainEntityRef
        """
        return self._username

    @username.setter
    def username(self, username: 'AuditTopicDomainEntityRef') -> None:
        """
        Sets the username of this AuditTopicAuditLogMessage.


        :param username: The username of this AuditTopicAuditLogMessage.
        :type: AuditTopicDomainEntityRef
        """
        

        self._username = username

    @property
    def user_display(self) -> str:
        """
        Gets the user_display of this AuditTopicAuditLogMessage.


        :return: The user_display of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._user_display

    @user_display.setter
    def user_display(self, user_display: str) -> None:
        """
        Sets the user_display of this AuditTopicAuditLogMessage.


        :param user_display: The user_display of this AuditTopicAuditLogMessage.
        :type: str
        """
        

        self._user_display = user_display

    @property
    def client_id(self) -> 'AuditTopicAddressableEntityRef':
        """
        Gets the client_id of this AuditTopicAuditLogMessage.


        :return: The client_id of this AuditTopicAuditLogMessage.
        :rtype: AuditTopicAddressableEntityRef
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: 'AuditTopicAddressableEntityRef') -> None:
        """
        Sets the client_id of this AuditTopicAuditLogMessage.


        :param client_id: The client_id of this AuditTopicAuditLogMessage.
        :type: AuditTopicAddressableEntityRef
        """
        

        self._client_id = client_id

    @property
    def remote_ip(self) -> List[str]:
        """
        Gets the remote_ip of this AuditTopicAuditLogMessage.


        :return: The remote_ip of this AuditTopicAuditLogMessage.
        :rtype: list[str]
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip: List[str]) -> None:
        """
        Sets the remote_ip of this AuditTopicAuditLogMessage.


        :param remote_ip: The remote_ip of this AuditTopicAuditLogMessage.
        :type: list[str]
        """
        

        self._remote_ip = remote_ip

    @property
    def service_name(self) -> str:
        """
        Gets the service_name of this AuditTopicAuditLogMessage.


        :return: The service_name of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name: str) -> None:
        """
        Sets the service_name of this AuditTopicAuditLogMessage.


        :param service_name: The service_name of this AuditTopicAuditLogMessage.
        :type: str
        """
        if isinstance(service_name, int):
            service_name = str(service_name)
        allowed_values = ["LanguageUnderstanding", "ContentManagement", "PeoplePermissions", "Presence", "Architect", "ContactCenter", "Quality", "SpeechAndTextAnalytics", "PredictiveEngagement", "Knowledge", "Coaching", "Learning", "EmployeeEngagement", "WorkforceManagement", "Triggers", "ProcessAutomation", "ResponseManagement", "Groups", "Telephony", "Outbound", "Routing", "Gamification", "Integrations", "Webhooks", "AnalyticsReporting", "Limits", "EmployeePerformance", "Datatables", "Messaging", "WebDeployments", "Supportability", "Callback", "Directory", "ExternalContacts", "TaskManagement", "SCIM", "NumberPurchasing", "Marketplace", "LogCapture", "GDPR", "AgentConfig", "Emails", "Scripter", "Billing", "JourneyAnalytics", "NerService", "Onboarding"]
        if service_name.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for service_name -> " + service_name)
            self._service_name = "outdated_sdk_version"
        else:
            self._service_name = service_name

    @property
    def level(self) -> str:
        """
        Gets the level of this AuditTopicAuditLogMessage.


        :return: The level of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level: str) -> None:
        """
        Sets the level of this AuditTopicAuditLogMessage.


        :param level: The level of this AuditTopicAuditLogMessage.
        :type: str
        """
        

        self._level = level

    @property
    def event_time(self) -> datetime:
        """
        Gets the event_time of this AuditTopicAuditLogMessage.


        :return: The event_time of this AuditTopicAuditLogMessage.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: datetime) -> None:
        """
        Sets the event_time of this AuditTopicAuditLogMessage.


        :param event_time: The event_time of this AuditTopicAuditLogMessage.
        :type: datetime
        """
        

        self._event_time = event_time

    @property
    def message(self) -> 'AuditTopicMessageInfo':
        """
        Gets the message of this AuditTopicAuditLogMessage.


        :return: The message of this AuditTopicAuditLogMessage.
        :rtype: AuditTopicMessageInfo
        """
        return self._message

    @message.setter
    def message(self, message: 'AuditTopicMessageInfo') -> None:
        """
        Sets the message of this AuditTopicAuditLogMessage.


        :param message: The message of this AuditTopicAuditLogMessage.
        :type: AuditTopicMessageInfo
        """
        

        self._message = message

    @property
    def action(self) -> str:
        """
        Gets the action of this AuditTopicAuditLogMessage.


        :return: The action of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str) -> None:
        """
        Sets the action of this AuditTopicAuditLogMessage.


        :param action: The action of this AuditTopicAuditLogMessage.
        :type: str
        """
        if isinstance(action, int):
            action = str(action)
        allowed_values = ["View", "Create", "Update", "Delete", "Move", "Copy", "Download", "ShareAdd", "ShareRemove", "Fax", "VersionCreate", "TagAdd", "TagRemove", "TagUpdate", "Add", "Remove", "MemberAdd", "MemberUpdate", "MemberRemove", "Authorize", "Deauthorize", "Authenticate", "ChangePassword", "AuthenticationFailed", "Revoke", "Checkin", "Checkout", "Deactivate", "Debug", "Publish", "Revert", "Save", "Transcode", "Upload", "WrapupCodeAdd", "WrapupCodeRemove", "Read", "Execute", "Abandon", "Archive", "Export", "RestoreRequest", "RestoreComplete", "UpdateRetention", "ApplyProtection", "RevokeProtection", "Rotate", "DeleteAll", "Reassign", "Unarchive", "Activate", "Assign", "Unassign", "Reset", "Reschedule", "Unpublish", "Purge", "Processed", "Enable", "Disable", "Recycle", "Append", "ContactsUpdated", "ContactsDeleted", "Restore", "Open", "Approved", "Rejected", "Rollback", "ImplementingChange", "ChangeImplemented", "ImplementingRollback", "RollbackImplemented", "Write", "Replace", "UpdateInService", "UpdateOutOfService", "Cycle", "Scale", "IpAllowlistClear", "AddPairingRole", "Verify", "RestoreDeleted", "RestoreAll", "Approve", "Reject", "Reverse", "Cancel", "HardDelete", "SoftDelete", "EnableCapture", "DownloadCapture", "Initiate", "ReverseManually"]
        if action.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for action -> " + action)
            self._action = "outdated_sdk_version"
        else:
            self._action = action

    @property
    def entity_type(self) -> str:
        """
        Gets the entity_type of this AuditTopicAuditLogMessage.


        :return: The entity_type of this AuditTopicAuditLogMessage.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type: str) -> None:
        """
        Sets the entity_type of this AuditTopicAuditLogMessage.


        :param entity_type: The entity_type of this AuditTopicAuditLogMessage.
        :type: str
        """
        if isinstance(entity_type, int):
            entity_type = str(entity_type)
        allowed_values = ["Feedback", "Document", "Workspace", "Tag", "AccessToken", "OAuthClientAuthorization", "AuthOrganization", "OAuthClient", "AuthUser", "OrganizationAuthorizationTrust", "OrganizationAuthorizationUserTrust", "Role", "RoleSettings", "Policy", "VoicemailUserPolicy", "UserPresence", "DependencyTrackingBuild", "Flow", "Prompt", "PromptResource", "FlowOutcome", "FlowMilestone", "Grammar", "GrammarLanguage", "AgentRoutingInfo", "Queue", "WrapupCode", "MaxOrgRoutingUtilizationCapacity", "ConversationAttributes", "RoutingUtilizationTag", "Evaluation", "Calibration", "Survey", "EvaluationForm", "SurveyForm", "Recording", "ScreenRecording", "BulkActions", "OrphanedRecording", "RecordingAnnotation", "RecordingSettings", "RecordingKey", "RecordingKeyConfig", "Topic", "Program", "Category", "SentimentFeedback", "DictionaryFeedback", "Segment", "Outcome", "ActionMap", "ActionTemplate", "ClickstreamSettings", "EventType", "SessionType", "KnowledgeBase", "KnowledgeCategory", "KnowledgeContext", "KnowledgeContextValue", "KnowledgeDocument", "KnowledgeDocumentVariation", "KnowledgeLabel", "KnowledgeTraining", "KnowledgeSearchFeedback", "TranscriptionSettings", "SpeechTextAnalyticsSettings", "Appointment", "Annotation", "Organization", "Module", "Rule", "Assignment", "Recognition", "ActivityCode", "ActivityPlan", "ActivityPlanOccurrence", "AdherenceExplanation", "AlternativeShift", "BusinessUnit", "Forecast", "ManagementUnit", "PlanningGroup", "Schedule", "ServiceGoalTemplate", "ShiftTrade", "TimeOffLimit", "TimeOffPlan", "TimeOffRequest", "WorkPlan", "WorkPlanBid", "WorkPlanBidGroup", "WorkPlanRotation", "HistoricalData", "StaffingGroup", "Trigger", "Response", "ResponseAsset", "SkillGroup", "DirectoryGroup", "Team", "SkillGroupDefinition", "Edge", "EdgeGroup", "VoicemailPolicy", "RoutingTranscriptionSettings", "Trunk", "TrunkBase", "ScheduleGroup", "EmergencyGroup", "IVR", "DID", "DIDPool", "Extension", "ExtensionPool", "Phone", "PhoneBase", "Line", "LineBase", "OutboundRoute", "NumberPlan", "Site", "AttemptLimits", "CallableTimeSet", "Campaign", "CampaignRule", "CampaignSchedule", "Sequence", "SequenceSchedule", "ContactList", "ContactListFilter", "ContactListTemplate", "DigitalRuleSet", "DNCList", "FileSpecificationTemplate", "ImportTemplate", "OrganizationSettings", "CallAnalysisResponseSet", "RuleSet", "WrapUpCodeMapping", "MessagingCampaign", "MessagingCampaignSchedule", "EmailCampaignSchedule", "Predictor", "KpiSpecification", "Metric", "Status", "Profile", "ProfileMembers", "Action", "ActionDraft", "Integration", "Webhook", "DashboardSettings", "InsightSettings", "AnalyticsReportingSettings", "ScheduledExports", "Exports", "ChangeRequest", "Migration", "ExternalMetricsDefinition", "ExternalMetricsData", "Schema", "Row", "Bulk", "SupportedContent", "ConversationPhoneNumber", "ConversationRecipient", "ConversationAccount", "ConversationDefaultSupportedContent", "ConversationThreadingWindow", "Deployment", "Configuration", "ConfigurationVersion", "EdgePreferences", "EdgeTraceLevel", "OrganizationIntegrationsAccess", "SupportFile", "EdgeLogZip", "Pcaps", "MediaDiagnosticsTraceFile", "EdgePcaps", "EdgeLog", "OrganizationFeature", "Product", "User", "Location", "Conversation", "OrganizationSuspension", "Participant", "ContactSchema", "ExternalOrganizationSchema", "Workbin", "Worktype", "Credential", "NumberOrder", "EnterpriseAgreement", "GdprRequest", "DefaultPanelSettings", "InboundDomain", "OutboundDomain", "InboundRoute", "OrganizationLimits", "UserSkill", "UserLanguage", "ComposerPage", "ComposerPublishedScript", "ComposerScript", "ComposerTemplate", "IntentMiner", "TopicMiner", "SoftSuspension", "JourneyView", "CustomEntity", "DirectoryFeature"]
        if entity_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for entity_type -> " + entity_type)
            self._entity_type = "outdated_sdk_version"
        else:
            self._entity_type = entity_type

    @property
    def entity(self) -> 'AuditTopicDomainEntityRef':
        """
        Gets the entity of this AuditTopicAuditLogMessage.


        :return: The entity of this AuditTopicAuditLogMessage.
        :rtype: AuditTopicDomainEntityRef
        """
        return self._entity

    @entity.setter
    def entity(self, entity: 'AuditTopicDomainEntityRef') -> None:
        """
        Sets the entity of this AuditTopicAuditLogMessage.


        :param entity: The entity of this AuditTopicAuditLogMessage.
        :type: AuditTopicDomainEntityRef
        """
        

        self._entity = entity

    @property
    def property_changes(self) -> List['AuditTopicPropertyChange']:
        """
        Gets the property_changes of this AuditTopicAuditLogMessage.


        :return: The property_changes of this AuditTopicAuditLogMessage.
        :rtype: list[AuditTopicPropertyChange]
        """
        return self._property_changes

    @property_changes.setter
    def property_changes(self, property_changes: List['AuditTopicPropertyChange']) -> None:
        """
        Sets the property_changes of this AuditTopicAuditLogMessage.


        :param property_changes: The property_changes of this AuditTopicAuditLogMessage.
        :type: list[AuditTopicPropertyChange]
        """
        

        self._property_changes = property_changes

    @property
    def context(self) -> Dict[str, str]:
        """
        Gets the context of this AuditTopicAuditLogMessage.


        :return: The context of this AuditTopicAuditLogMessage.
        :rtype: dict(str, str)
        """
        return self._context

    @context.setter
    def context(self, context: Dict[str, str]) -> None:
        """
        Sets the context of this AuditTopicAuditLogMessage.


        :param context: The context of this AuditTopicAuditLogMessage.
        :type: dict(str, str)
        """
        

        self._context = context

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

