---
title: ConversationActivityQuery
---
## ConversationActivityQuery

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **metrics** | [**list[ConversationActivityQueryMetric]**](ConversationActivityQueryMetric.html) | List of requested metrics | |
| **group_by** | **list[str]** | Dimension(s) to group by | |
| **filter** | [**ConversationActivityQueryFilter**](ConversationActivityQueryFilter.html) | Filter to return a subset of observations. Expresses boolean logical predicates as well as dimensional filters | [optional] |
| **order** | **str** | Sort the result set in ascending/descending order. Default is ascending | [optional] |
{: class="table table-striped"}


