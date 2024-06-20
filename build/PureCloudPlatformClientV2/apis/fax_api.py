# coding: utf-8

"""
FaxApi.py
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
from ..models import DownloadResponse
from ..models import ErrorBody
from ..models import FaxConfig
from ..models import FaxDocument
from ..models import FaxDocumentEntityListing
from ..models import FaxSummary

class FaxApi(object):
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

    def delete_fax_document(self, document_id: str, **kwargs) -> None:
        """
        Delete a fax document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_fax_document(document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fax_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `delete_fax_document`")


        resource_path = '/api/v2/fax/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

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

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_fax_document(self, document_id: str, **kwargs) -> 'FaxDocument':
        """
        Get a document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fax_document(document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :return: FaxDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fax_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_fax_document`")


        resource_path = '/api/v2/fax/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

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
                                            response_type='FaxDocument',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_fax_document_content(self, document_id: str, **kwargs) -> 'DownloadResponse':
        """
        Download a fax document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fax_document_content(document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :return: DownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fax_document_content" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_fax_document_content`")


        resource_path = '/api/v2/fax/documents/{documentId}/content'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = {}

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
                                            response_type='DownloadResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_fax_documents(self, **kwargs) -> 'FaxDocumentEntityListing':
        """
        Get a list of fax documents.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fax_documents(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: Page size
        :param int page_number: Page number
        :return: FaxDocumentEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fax_documents" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/fax/documents'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']

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
                                            response_type='FaxDocumentEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_fax_settings(self, **kwargs) -> 'FaxConfig':
        """
        Get organization config for given organization
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fax_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FaxConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fax_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/fax/settings'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

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
                                            response_type='FaxConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_fax_summary(self, **kwargs) -> 'FaxSummary':
        """
        Get fax summary
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_fax_summary(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: FaxSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fax_summary" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/fax/summary'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

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
                                            response_type='FaxSummary',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_fax_document(self, document_id: str, body: 'FaxDocument', **kwargs) -> 'FaxDocument':
        """
        Update a fax document.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_fax_document(document_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str document_id: Document ID (required)
        :param FaxDocument body: Document (required)
        :return: FaxDocument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_fax_document" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `put_fax_document`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_fax_document`")


        resource_path = '/api/v2/fax/documents/{documentId}'.replace('{format}', 'json')
        path_params = {}
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FaxDocument',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_fax_settings(self, **kwargs) -> 'FaxConfig':
        """
        Update/write organization config for given organization
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_fax_settings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param FaxConfig body: 
        :return: FaxConfig
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
                    " to method put_fax_settings" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/fax/settings'.replace('{format}', 'json')
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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='FaxConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
