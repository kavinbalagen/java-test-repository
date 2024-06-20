# coding: utf-8

"""
CarrierServicesApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

from datetime import datetime
from datetime import date

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from ..utils import deprecated

from typing import List
from typing import Dict
from typing import Any

from ..models import Empty
from ..models import EmergencyLocation
from ..models import ErrorBody
from ..models import ErrorInfo

class CarrierServicesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_carrierservices_integrations_emergencylocations_me(self, phone_number: str, **kwargs) -> 'EmergencyLocation':
        """
        Get location for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_carrierservices_integrations_emergencylocations_me(phone_number, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str phone_number: Phone number in E164 format (required)
        :return: EmergencyLocation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['phone_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_carrierservices_integrations_emergencylocations_me" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in params) or (params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `get_carrierservices_integrations_emergencylocations_me`")


        resource_path = '/api/v2/carrierservices/integrations/emergencylocations/me'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'phone_number' in params:
            query_params['phoneNumber'] = params['phone_number']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EmergencyLocation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_carrierservices_integrations_emergencylocations_me(self, **kwargs) -> 'EmergencyLocation':
        """
        Set current location for the logged in user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_carrierservices_integrations_emergencylocations_me(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EmergencyLocation body: 
        :return: EmergencyLocation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_carrierservices_integrations_emergencylocations_me" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/carrierservices/integrations/emergencylocations/me'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EmergencyLocation',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response