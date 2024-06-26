---
title: OpenNormalizedMessage
---
## OpenNormalizedMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | Unique ID of the message. This ID is generated by Messaging Platform. Message receipts will have the same ID as the message they reference, as such should only be set when sending a message receipt. | [optional] |
| **channel** | [**OpenMessagingChannel**](OpenMessagingChannel.html) | Channel-specific information that describes the message and the message channel/provider. | |
| **type** | **str** | Message type. | |
| **text** | **str** | Message text. | [optional] |
| **content** | [**list[OpenMessageContent]**](OpenMessageContent.html) | List of content elements. | [optional] |
| **status** | **str** | Message receipt status, only used with type Receipt. | [optional] |
| **reasons** | [**list[ConversationReason]**](ConversationReason.html) | List of reasons for a message receipt that indicates the message has failed. Only used with Failed status. | [optional] |
| **is_final_receipt** | **bool** | Indicates if this is the last message receipt for this message, or if another message receipt can be expected. | [optional] |
| **direction** | **str** | The direction of the message. | [optional] |
| **metadata** | **dict(str, str)** | Additional metadata about this message. | [optional] |
{: class="table table-striped"}


