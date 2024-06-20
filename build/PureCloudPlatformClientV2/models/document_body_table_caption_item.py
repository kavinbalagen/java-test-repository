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
    from . import DocumentBodyImage
    from . import DocumentBodyList
    from . import DocumentBodyParagraph
    from . import DocumentBodyVideo
    from . import DocumentText

class DocumentBodyTableCaptionItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DocumentBodyTableCaptionItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'text': 'DocumentText',
            'paragraph': 'DocumentBodyParagraph',
            'image': 'DocumentBodyImage',
            'video': 'DocumentBodyVideo',
            'list': 'DocumentBodyList'
        }

        self.attribute_map = {
            'type': 'type',
            'text': 'text',
            'paragraph': 'paragraph',
            'image': 'image',
            'video': 'video',
            'list': 'list'
        }

        self._type = None
        self._text = None
        self._paragraph = None
        self._image = None
        self._video = None
        self._list = None

    @property
    def type(self) -> str:
        """
        Gets the type of this DocumentBodyTableCaptionItem.
        The type of the caption item.

        :return: The type of this DocumentBodyTableCaptionItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str) -> None:
        """
        Sets the type of this DocumentBodyTableCaptionItem.
        The type of the caption item.

        :param type: The type of this DocumentBodyTableCaptionItem.
        :type: str
        """
        if isinstance(type, int):
            type = str(type)
        allowed_values = ["Text", "Paragraph", "Image", "Video", "OrderedList", "UnorderedList"]
        if type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for type -> " + type)
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def text(self) -> 'DocumentText':
        """
        Gets the text of this DocumentBodyTableCaptionItem.
        Text. It must contain a value if the type of the block is Text.

        :return: The text of this DocumentBodyTableCaptionItem.
        :rtype: DocumentText
        """
        return self._text

    @text.setter
    def text(self, text: 'DocumentText') -> None:
        """
        Sets the text of this DocumentBodyTableCaptionItem.
        Text. It must contain a value if the type of the block is Text.

        :param text: The text of this DocumentBodyTableCaptionItem.
        :type: DocumentText
        """
        

        self._text = text

    @property
    def paragraph(self) -> 'DocumentBodyParagraph':
        """
        Gets the paragraph of this DocumentBodyTableCaptionItem.
        Paragraph. It must contain a value if the type of the block is Paragraph.

        :return: The paragraph of this DocumentBodyTableCaptionItem.
        :rtype: DocumentBodyParagraph
        """
        return self._paragraph

    @paragraph.setter
    def paragraph(self, paragraph: 'DocumentBodyParagraph') -> None:
        """
        Sets the paragraph of this DocumentBodyTableCaptionItem.
        Paragraph. It must contain a value if the type of the block is Paragraph.

        :param paragraph: The paragraph of this DocumentBodyTableCaptionItem.
        :type: DocumentBodyParagraph
        """
        

        self._paragraph = paragraph

    @property
    def image(self) -> 'DocumentBodyImage':
        """
        Gets the image of this DocumentBodyTableCaptionItem.
        Image. It must contain a value if the type of the block is Image.

        :return: The image of this DocumentBodyTableCaptionItem.
        :rtype: DocumentBodyImage
        """
        return self._image

    @image.setter
    def image(self, image: 'DocumentBodyImage') -> None:
        """
        Sets the image of this DocumentBodyTableCaptionItem.
        Image. It must contain a value if the type of the block is Image.

        :param image: The image of this DocumentBodyTableCaptionItem.
        :type: DocumentBodyImage
        """
        

        self._image = image

    @property
    def video(self) -> 'DocumentBodyVideo':
        """
        Gets the video of this DocumentBodyTableCaptionItem.
        Video. It must contain a value if the type of the block is Video.

        :return: The video of this DocumentBodyTableCaptionItem.
        :rtype: DocumentBodyVideo
        """
        return self._video

    @video.setter
    def video(self, video: 'DocumentBodyVideo') -> None:
        """
        Sets the video of this DocumentBodyTableCaptionItem.
        Video. It must contain a value if the type of the block is Video.

        :param video: The video of this DocumentBodyTableCaptionItem.
        :type: DocumentBodyVideo
        """
        

        self._video = video

    @property
    def list(self) -> 'DocumentBodyList':
        """
        Gets the list of this DocumentBodyTableCaptionItem.
        List. It must contain a value if the type of the block is UnorderedList or OrderedList.

        :return: The list of this DocumentBodyTableCaptionItem.
        :rtype: DocumentBodyList
        """
        return self._list

    @list.setter
    def list(self, list: 'DocumentBodyList') -> None:
        """
        Sets the list of this DocumentBodyTableCaptionItem.
        List. It must contain a value if the type of the block is UnorderedList or OrderedList.

        :param list: The list of this DocumentBodyTableCaptionItem.
        :type: DocumentBodyList
        """
        

        self._list = list

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

