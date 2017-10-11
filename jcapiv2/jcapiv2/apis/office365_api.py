# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class Office365Api(object):
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

    def graph_office365_associations_list(self, office365_id, targets, content_type, accept, **kwargs):
        """
        List the associations of an Office 365 instance
        This endpoint returns _direct_ associations of an Office 365 instance.   A direct association can be a non-homogenous relationship between 2 different objects. for example Office 365 and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/associations?targets=user ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_associations_list(office365_id, targets, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param list[str] targets:  (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_office365_associations_list_with_http_info(office365_id, targets, content_type, accept, **kwargs)
        else:
            (data) = self.graph_office365_associations_list_with_http_info(office365_id, targets, content_type, accept, **kwargs)
            return data

    def graph_office365_associations_list_with_http_info(self, office365_id, targets, content_type, accept, **kwargs):
        """
        List the associations of an Office 365 instance
        This endpoint returns _direct_ associations of an Office 365 instance.   A direct association can be a non-homogenous relationship between 2 different objects. for example Office 365 and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/associations?targets=user ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_associations_list_with_http_info(office365_id, targets, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param list[str] targets:  (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'targets', 'content_type', 'accept', 'limit', 'skip']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params) or (params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_associations_list`")
        # verify the required parameter 'targets' is set
        if ('targets' not in params) or (params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_office365_associations_list`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_office365_associations_list`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_office365_associations_list`")


        collection_formats = {}

        resource_path = '/office365s/{office365_id}/associations'.replace('{format}', 'json')
        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']

        query_params = {}
        if 'targets' in params:
            query_params['targets'] = params['targets']
            collection_formats['targets'] = 'csv'
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'skip' in params:
            query_params['skip'] = params['skip']

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GraphConnection]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def graph_office365_associations_post(self, office365_id, content_type, accept, **kwargs):
        """
        Manage the associations of an Office 365 instance
        This endpoint allows you to manage the _direct_ associations of a Office 365 instance.  A direct association can be a non-homogenous relationship between 2 different objects. for example Office 365 and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/associations ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_associations_post(office365_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param GraphManagementReq body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_office365_associations_post_with_http_info(office365_id, content_type, accept, **kwargs)
        else:
            (data) = self.graph_office365_associations_post_with_http_info(office365_id, content_type, accept, **kwargs)
            return data

    def graph_office365_associations_post_with_http_info(self, office365_id, content_type, accept, **kwargs):
        """
        Manage the associations of an Office 365 instance
        This endpoint allows you to manage the _direct_ associations of a Office 365 instance.  A direct association can be a non-homogenous relationship between 2 different objects. for example Office 365 and Users.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/associations ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_associations_post_with_http_info(office365_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 instance. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param GraphManagementReq body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'content_type', 'accept', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params) or (params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_associations_post`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_office365_associations_post`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_office365_associations_post`")


        collection_formats = {}

        resource_path = '/office365s/{office365_id}/associations'.replace('{format}', 'json')
        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']

        query_params = {}

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def graph_office365_traverse_user(self, office365_id, content_type, accept, **kwargs):
        """
        List the Users associated with an Office 365 instance
        This endpoint will return Users associated with an Office 365 instance. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/users ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_traverse_user(office365_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_office365_traverse_user_with_http_info(office365_id, content_type, accept, **kwargs)
        else:
            (data) = self.graph_office365_traverse_user_with_http_info(office365_id, content_type, accept, **kwargs)
            return data

    def graph_office365_traverse_user_with_http_info(self, office365_id, content_type, accept, **kwargs):
        """
        List the Users associated with an Office 365 instance
        This endpoint will return Users associated with an Office 365 instance. Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User; this array represents all grouping and/or associations that would have to be removed to deprovision the User from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/users ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_traverse_user_with_http_info(office365_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'content_type', 'accept', 'limit', 'skip']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_traverse_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params) or (params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_traverse_user`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_office365_traverse_user`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_office365_traverse_user`")


        collection_formats = {}

        resource_path = '/office365s/{office365_id}/users'.replace('{format}', 'json')
        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'skip' in params:
            query_params['skip'] = params['skip']

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GraphObjectWithPaths]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def graph_office365_traverse_user_group(self, office365_id, content_type, accept, **kwargs):
        """
        List the User Groups associated with an Office 365 instance
        This endpoint will return User Groups associated with an Office 365 instance. Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/usergroups ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_traverse_user_group(office365_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_office365_traverse_user_group_with_http_info(office365_id, content_type, accept, **kwargs)
        else:
            (data) = self.graph_office365_traverse_user_group_with_http_info(office365_id, content_type, accept, **kwargs)
            return data

    def graph_office365_traverse_user_group_with_http_info(self, office365_id, content_type, accept, **kwargs):
        """
        List the User Groups associated with an Office 365 instance
        This endpoint will return User Groups associated with an Office 365 instance. Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of attributes specifically set for this group.  The `paths` array enumerates each path from this Office 365 instance to the corresponding User Group; this array represents all grouping and/or associations that would have to be removed to deprovision the User Group from this Office 365 instance.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` https://console.jumpcloud.com/api/v2/office365s/{office365_id}/usergroups ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_office365_traverse_user_group_with_http_info(office365_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str office365_id: ObjectID of the Office 365 suite. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['office365_id', 'content_type', 'accept', 'limit', 'skip']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_office365_traverse_user_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'office365_id' is set
        if ('office365_id' not in params) or (params['office365_id'] is None):
            raise ValueError("Missing the required parameter `office365_id` when calling `graph_office365_traverse_user_group`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_office365_traverse_user_group`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_office365_traverse_user_group`")


        collection_formats = {}

        resource_path = '/office365s/{office365_id}/usergroups'.replace('{format}', 'json')
        path_params = {}
        if 'office365_id' in params:
            path_params['office365_id'] = params['office365_id']

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'skip' in params:
            query_params['skip'] = params['skip']

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GraphObjectWithPaths]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
