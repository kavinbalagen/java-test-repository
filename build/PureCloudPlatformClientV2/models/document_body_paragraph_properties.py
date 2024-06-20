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


class DocumentBodyParagraphProperties(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        DocumentBodyParagraphProperties - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'font_size': 'str',
            'font_type': 'str',
            'text_color': 'str',
            'background_color': 'str',
            'align': 'str',
            'indentation': 'float'
        }

        self.attribute_map = {
            'font_size': 'fontSize',
            'font_type': 'fontType',
            'text_color': 'textColor',
            'background_color': 'backgroundColor',
            'align': 'align',
            'indentation': 'indentation'
        }

        self._font_size = None
        self._font_type = None
        self._text_color = None
        self._background_color = None
        self._align = None
        self._indentation = None

    @property
    def font_size(self) -> str:
        """
        Gets the font_size of this DocumentBodyParagraphProperties.
        The font size for the paragraph. The valid values in 'em'.

        :return: The font_size of this DocumentBodyParagraphProperties.
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size: str) -> None:
        """
        Sets the font_size of this DocumentBodyParagraphProperties.
        The font size for the paragraph. The valid values in 'em'.

        :param font_size: The font_size of this DocumentBodyParagraphProperties.
        :type: str
        """
        if isinstance(font_size, int):
            font_size = str(font_size)
        allowed_values = ["XxSmall", "XSmall", "Small", "Medium", "Large", "XLarge", "XxLarge", "XxxLarge"]
        if font_size.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for font_size -> " + font_size)
            self._font_size = "outdated_sdk_version"
        else:
            self._font_size = font_size

    @property
    def font_type(self) -> str:
        """
        Gets the font_type of this DocumentBodyParagraphProperties.
        The font type for the paragraph.

        :return: The font_type of this DocumentBodyParagraphProperties.
        :rtype: str
        """
        return self._font_type

    @font_type.setter
    def font_type(self, font_type: str) -> None:
        """
        Sets the font_type of this DocumentBodyParagraphProperties.
        The font type for the paragraph.

        :param font_type: The font_type of this DocumentBodyParagraphProperties.
        :type: str
        """
        if isinstance(font_type, int):
            font_type = str(font_type)
        allowed_values = ["Paragraph", "Heading1", "Heading2", "Heading3", "Heading4", "Heading5", "Heading6", "Preformatted"]
        if font_type.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for font_type -> " + font_type)
            self._font_type = "outdated_sdk_version"
        else:
            self._font_type = font_type

    @property
    def text_color(self) -> str:
        """
        Gets the text_color of this DocumentBodyParagraphProperties.
        The text color for the paragraph. The valid values in hex color code representation. For example black color - #000000

        :return: The text_color of this DocumentBodyParagraphProperties.
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color: str) -> None:
        """
        Sets the text_color of this DocumentBodyParagraphProperties.
        The text color for the paragraph. The valid values in hex color code representation. For example black color - #000000

        :param text_color: The text_color of this DocumentBodyParagraphProperties.
        :type: str
        """
        

        self._text_color = text_color

    @property
    def background_color(self) -> str:
        """
        Gets the background_color of this DocumentBodyParagraphProperties.
        The background color for the paragraph. The valid values in hex color code representation. For example black color - #000000

        :return: The background_color of this DocumentBodyParagraphProperties.
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color: str) -> None:
        """
        Sets the background_color of this DocumentBodyParagraphProperties.
        The background color for the paragraph. The valid values in hex color code representation. For example black color - #000000

        :param background_color: The background_color of this DocumentBodyParagraphProperties.
        :type: str
        """
        

        self._background_color = background_color

    @property
    def align(self) -> str:
        """
        Gets the align of this DocumentBodyParagraphProperties.
        The align type for the paragraph.

        :return: The align of this DocumentBodyParagraphProperties.
        :rtype: str
        """
        return self._align

    @align.setter
    def align(self, align: str) -> None:
        """
        Sets the align of this DocumentBodyParagraphProperties.
        The align type for the paragraph.

        :param align: The align of this DocumentBodyParagraphProperties.
        :type: str
        """
        if isinstance(align, int):
            align = str(align)
        allowed_values = ["Center", "Left", "Right", "Justify"]
        if align.lower() not in map(str.lower, allowed_values):
            # print("Invalid value for align -> " + align)
            self._align = "outdated_sdk_version"
        else:
            self._align = align

    @property
    def indentation(self) -> float:
        """
        Gets the indentation of this DocumentBodyParagraphProperties.
        The indentation color for the paragraph. The valid values in 'em'.

        :return: The indentation of this DocumentBodyParagraphProperties.
        :rtype: float
        """
        return self._indentation

    @indentation.setter
    def indentation(self, indentation: float) -> None:
        """
        Sets the indentation of this DocumentBodyParagraphProperties.
        The indentation color for the paragraph. The valid values in 'em'.

        :param indentation: The indentation of this DocumentBodyParagraphProperties.
        :type: float
        """
        

        self._indentation = indentation

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

