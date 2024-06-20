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
    from . import ContentAttachment
    from . import ContentButtonResponse
    from . import ContentCard
    from . import ContentCarousel
    from . import ContentGeneric
    from . import ContentList
    from . import ContentLocation
    from . import ContentNotificationTemplate
    from . import ContentPostback
    from . import ContentQuickReply
    from . import ContentQuickReplyV2
    from . import ContentReaction
    from . import ContentStory
    from . import ContentText
    from . import MessagingRecipient

class MessageContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        MessageContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content_type': 'str',
            'location': 'ContentLocation',
            'attachment': 'ContentAttachment',
            'quick_reply': 'ContentQuickReply',
            'button_response': 'ContentButtonResponse',
            'generic': 'ContentGeneric',
            'list': 'ContentList',
            'template': 'ContentNotificationTemplate',
            'reactions': 'list[ContentReaction]',
            'mention': 'MessagingRecipient',
            'postback': 'ContentPostback',
            'story': 'ContentStory',
            'card': 'ContentCard',
            'carousel': 'ContentCarousel',
            'text': 'ContentText',
            'quick_reply_v2': 'ContentQuickReplyV2'
        }

        self.attribute_map = {
            'content_type': 'contentType',
            'location': 'location',
            'attachment': 'attachment',
            'quick_reply': 'quickReply',
            'button_response': 'buttonResponse',
            'generic': 'generic',
            'list': 'list',
            'template': 'template',
            'reactions': 'reactions',
            'mention': 'mention',
            'postback': 'postback',
            'story': 'story',
            'card': 'card',
            'carousel': 'carousel',
            'text': 'text',
            'quick_reply_v2': 'quickReplyV2'
        }

        self._content_type = None
        self._location = None
        self._attachment = None
        self._quick_reply = None
        self._button_response = None
        self._generic = None
        self._list = None
        self._template = None
        self._reactions = None
        self._mention = None
        self._postback = None
        self._story = None
        self._card = None
        self._carousel = None
        self._text = None
        self._quick_reply_v2 = None

    @property
    def content_type(self) -> str:
        """
        Gets the content_type of this MessageContent.
        Type of this content element.

        :return: The content_type of this MessageContent.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type: str) -> None:
        """
        Sets the content_type of this MessageContent.
        Type of this content element.

        :param content_type: The content_type of this MessageContent.
        :type: str
        """
        if isinstance(content_type, int):
            content_type = str(content_type)
        allowed_values = ["Attachment", "Location", "QuickReply", "Notification", "GenericTemplate", "ListTemplate", "Postback", "Reactions", "Mention", "ButtonResponse", "Story", "Card", "Carousel", "Text", "QuickReplyV2"]
        if content_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for content_type -> " + content_type)
            self._content_type = "outdated_sdk_version"
        else:
            self._content_type = content_type

    @property
    def location(self) -> 'ContentLocation':
        """
        Gets the location of this MessageContent.
        Location content.

        :return: The location of this MessageContent.
        :rtype: ContentLocation
        """
        return self._location

    @location.setter
    def location(self, location: 'ContentLocation') -> None:
        """
        Sets the location of this MessageContent.
        Location content.

        :param location: The location of this MessageContent.
        :type: ContentLocation
        """
        

        self._location = location

    @property
    def attachment(self) -> 'ContentAttachment':
        """
        Gets the attachment of this MessageContent.
        Attachment content.

        :return: The attachment of this MessageContent.
        :rtype: ContentAttachment
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment: 'ContentAttachment') -> None:
        """
        Sets the attachment of this MessageContent.
        Attachment content.

        :param attachment: The attachment of this MessageContent.
        :type: ContentAttachment
        """
        

        self._attachment = attachment

    @property
    def quick_reply(self) -> 'ContentQuickReply':
        """
        Gets the quick_reply of this MessageContent.
        Quick reply content.

        :return: The quick_reply of this MessageContent.
        :rtype: ContentQuickReply
        """
        return self._quick_reply

    @quick_reply.setter
    def quick_reply(self, quick_reply: 'ContentQuickReply') -> None:
        """
        Sets the quick_reply of this MessageContent.
        Quick reply content.

        :param quick_reply: The quick_reply of this MessageContent.
        :type: ContentQuickReply
        """
        

        self._quick_reply = quick_reply

    @property
    def button_response(self) -> 'ContentButtonResponse':
        """
        Gets the button_response of this MessageContent.
        Button response content.

        :return: The button_response of this MessageContent.
        :rtype: ContentButtonResponse
        """
        return self._button_response

    @button_response.setter
    def button_response(self, button_response: 'ContentButtonResponse') -> None:
        """
        Sets the button_response of this MessageContent.
        Button response content.

        :param button_response: The button_response of this MessageContent.
        :type: ContentButtonResponse
        """
        

        self._button_response = button_response

    @property
    def generic(self) -> 'ContentGeneric':
        """
        Gets the generic of this MessageContent.
        Generic content (Deprecated).

        :return: The generic of this MessageContent.
        :rtype: ContentGeneric
        """
        return self._generic

    @generic.setter
    def generic(self, generic: 'ContentGeneric') -> None:
        """
        Sets the generic of this MessageContent.
        Generic content (Deprecated).

        :param generic: The generic of this MessageContent.
        :type: ContentGeneric
        """
        

        self._generic = generic

    @property
    def list(self) -> 'ContentList':
        """
        Gets the list of this MessageContent.
        List content (Deprecated).

        :return: The list of this MessageContent.
        :rtype: ContentList
        """
        return self._list

    @list.setter
    def list(self, list: 'ContentList') -> None:
        """
        Sets the list of this MessageContent.
        List content (Deprecated).

        :param list: The list of this MessageContent.
        :type: ContentList
        """
        

        self._list = list

    @property
    def template(self) -> 'ContentNotificationTemplate':
        """
        Gets the template of this MessageContent.
        Template notification content.

        :return: The template of this MessageContent.
        :rtype: ContentNotificationTemplate
        """
        return self._template

    @template.setter
    def template(self, template: 'ContentNotificationTemplate') -> None:
        """
        Sets the template of this MessageContent.
        Template notification content.

        :param template: The template of this MessageContent.
        :type: ContentNotificationTemplate
        """
        

        self._template = template

    @property
    def reactions(self) -> List['ContentReaction']:
        """
        Gets the reactions of this MessageContent.
        A set of reactions to a message.

        :return: The reactions of this MessageContent.
        :rtype: list[ContentReaction]
        """
        return self._reactions

    @reactions.setter
    def reactions(self, reactions: List['ContentReaction']) -> None:
        """
        Sets the reactions of this MessageContent.
        A set of reactions to a message.

        :param reactions: The reactions of this MessageContent.
        :type: list[ContentReaction]
        """
        

        self._reactions = reactions

    @property
    def mention(self) -> 'MessagingRecipient':
        """
        Gets the mention of this MessageContent.
        Mention content.

        :return: The mention of this MessageContent.
        :rtype: MessagingRecipient
        """
        return self._mention

    @mention.setter
    def mention(self, mention: 'MessagingRecipient') -> None:
        """
        Sets the mention of this MessageContent.
        Mention content.

        :param mention: The mention of this MessageContent.
        :type: MessagingRecipient
        """
        

        self._mention = mention

    @property
    def postback(self) -> 'ContentPostback':
        """
        Gets the postback of this MessageContent.
        Structured message postback (Deprecated).

        :return: The postback of this MessageContent.
        :rtype: ContentPostback
        """
        return self._postback

    @postback.setter
    def postback(self, postback: 'ContentPostback') -> None:
        """
        Sets the postback of this MessageContent.
        Structured message postback (Deprecated).

        :param postback: The postback of this MessageContent.
        :type: ContentPostback
        """
        

        self._postback = postback

    @property
    def story(self) -> 'ContentStory':
        """
        Gets the story of this MessageContent.
        Ephemeral story content.

        :return: The story of this MessageContent.
        :rtype: ContentStory
        """
        return self._story

    @story.setter
    def story(self, story: 'ContentStory') -> None:
        """
        Sets the story of this MessageContent.
        Ephemeral story content.

        :param story: The story of this MessageContent.
        :type: ContentStory
        """
        

        self._story = story

    @property
    def card(self) -> 'ContentCard':
        """
        Gets the card of this MessageContent.
        Card content

        :return: The card of this MessageContent.
        :rtype: ContentCard
        """
        return self._card

    @card.setter
    def card(self, card: 'ContentCard') -> None:
        """
        Sets the card of this MessageContent.
        Card content

        :param card: The card of this MessageContent.
        :type: ContentCard
        """
        

        self._card = card

    @property
    def carousel(self) -> 'ContentCarousel':
        """
        Gets the carousel of this MessageContent.
        Carousel content

        :return: The carousel of this MessageContent.
        :rtype: ContentCarousel
        """
        return self._carousel

    @carousel.setter
    def carousel(self, carousel: 'ContentCarousel') -> None:
        """
        Sets the carousel of this MessageContent.
        Carousel content

        :param carousel: The carousel of this MessageContent.
        :type: ContentCarousel
        """
        

        self._carousel = carousel

    @property
    def text(self) -> 'ContentText':
        """
        Gets the text of this MessageContent.
        Text content.

        :return: The text of this MessageContent.
        :rtype: ContentText
        """
        return self._text

    @text.setter
    def text(self, text: 'ContentText') -> None:
        """
        Sets the text of this MessageContent.
        Text content.

        :param text: The text of this MessageContent.
        :type: ContentText
        """
        

        self._text = text

    @property
    def quick_reply_v2(self) -> 'ContentQuickReplyV2':
        """
        Gets the quick_reply_v2 of this MessageContent.
        Quick reply V2 content.

        :return: The quick_reply_v2 of this MessageContent.
        :rtype: ContentQuickReplyV2
        """
        return self._quick_reply_v2

    @quick_reply_v2.setter
    def quick_reply_v2(self, quick_reply_v2: 'ContentQuickReplyV2') -> None:
        """
        Sets the quick_reply_v2 of this MessageContent.
        Quick reply V2 content.

        :param quick_reply_v2: The quick_reply_v2 of this MessageContent.
        :type: ContentQuickReplyV2
        """
        

        self._quick_reply_v2 = quick_reply_v2

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

