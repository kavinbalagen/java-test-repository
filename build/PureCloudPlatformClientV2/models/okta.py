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


class Okta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        Okta - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'disabled': 'bool',
            'issuer_uri': 'str',
            'sso_target_uri': 'str',
            'slo_uri': 'str',
            'slo_binding': 'str',
            'relying_party_identifier': 'str',
            'certificate': 'str',
            'certificates': 'list[str]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'disabled': 'disabled',
            'issuer_uri': 'issuerURI',
            'sso_target_uri': 'ssoTargetURI',
            'slo_uri': 'sloURI',
            'slo_binding': 'sloBinding',
            'relying_party_identifier': 'relyingPartyIdentifier',
            'certificate': 'certificate',
            'certificates': 'certificates',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._disabled = None
        self._issuer_uri = None
        self._sso_target_uri = None
        self._slo_uri = None
        self._slo_binding = None
        self._relying_party_identifier = None
        self._certificate = None
        self._certificates = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this Okta.
        The globally unique identifier for the object.

        :return: The id of this Okta.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this Okta.
        The globally unique identifier for the object.

        :param id: The id of this Okta.
        :type: str
        """
        

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Okta.


        :return: The name of this Okta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the name of this Okta.


        :param name: The name of this Okta.
        :type: str
        """
        

        self._name = name

    @property
    def disabled(self) -> bool:
        """
        Gets the disabled of this Okta.


        :return: The disabled of this Okta.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled: bool) -> None:
        """
        Sets the disabled of this Okta.


        :param disabled: The disabled of this Okta.
        :type: bool
        """
        

        self._disabled = disabled

    @property
    def issuer_uri(self) -> str:
        """
        Gets the issuer_uri of this Okta.


        :return: The issuer_uri of this Okta.
        :rtype: str
        """
        return self._issuer_uri

    @issuer_uri.setter
    def issuer_uri(self, issuer_uri: str) -> None:
        """
        Sets the issuer_uri of this Okta.


        :param issuer_uri: The issuer_uri of this Okta.
        :type: str
        """
        

        self._issuer_uri = issuer_uri

    @property
    def sso_target_uri(self) -> str:
        """
        Gets the sso_target_uri of this Okta.


        :return: The sso_target_uri of this Okta.
        :rtype: str
        """
        return self._sso_target_uri

    @sso_target_uri.setter
    def sso_target_uri(self, sso_target_uri: str) -> None:
        """
        Sets the sso_target_uri of this Okta.


        :param sso_target_uri: The sso_target_uri of this Okta.
        :type: str
        """
        

        self._sso_target_uri = sso_target_uri

    @property
    def slo_uri(self) -> str:
        """
        Gets the slo_uri of this Okta.


        :return: The slo_uri of this Okta.
        :rtype: str
        """
        return self._slo_uri

    @slo_uri.setter
    def slo_uri(self, slo_uri: str) -> None:
        """
        Sets the slo_uri of this Okta.


        :param slo_uri: The slo_uri of this Okta.
        :type: str
        """
        

        self._slo_uri = slo_uri

    @property
    def slo_binding(self) -> str:
        """
        Gets the slo_binding of this Okta.


        :return: The slo_binding of this Okta.
        :rtype: str
        """
        return self._slo_binding

    @slo_binding.setter
    def slo_binding(self, slo_binding: str) -> None:
        """
        Sets the slo_binding of this Okta.


        :param slo_binding: The slo_binding of this Okta.
        :type: str
        """
        

        self._slo_binding = slo_binding

    @property
    def relying_party_identifier(self) -> str:
        """
        Gets the relying_party_identifier of this Okta.


        :return: The relying_party_identifier of this Okta.
        :rtype: str
        """
        return self._relying_party_identifier

    @relying_party_identifier.setter
    def relying_party_identifier(self, relying_party_identifier: str) -> None:
        """
        Sets the relying_party_identifier of this Okta.


        :param relying_party_identifier: The relying_party_identifier of this Okta.
        :type: str
        """
        

        self._relying_party_identifier = relying_party_identifier

    @property
    def certificate(self) -> str:
        """
        Gets the certificate of this Okta.


        :return: The certificate of this Okta.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate: str) -> None:
        """
        Sets the certificate of this Okta.


        :param certificate: The certificate of this Okta.
        :type: str
        """
        

        self._certificate = certificate

    @property
    def certificates(self) -> List[str]:
        """
        Gets the certificates of this Okta.


        :return: The certificates of this Okta.
        :rtype: list[str]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates: List[str]) -> None:
        """
        Sets the certificates of this Okta.


        :param certificates: The certificates of this Okta.
        :type: list[str]
        """
        

        self._certificates = certificates

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this Okta.
        The URI for this object

        :return: The self_uri of this Okta.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this Okta.
        The URI for this object

        :param self_uri: The self_uri of this Okta.
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

