# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
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


class CommandsApi(object):
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

    def commands_delete(self, id, content_type, accept, **kwargs):
        """
        Delete a Command
        Delete a specific command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_delete(id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commands_delete_with_http_info(id, content_type, accept, **kwargs)
        else:
            (data) = self.commands_delete_with_http_info(id, content_type, accept, **kwargs)
            return data

    def commands_delete_with_http_info(self, id, content_type, accept, **kwargs):
        """
        Delete a Command
        Delete a specific command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_delete_with_http_info(id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commands_delete`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_delete`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_delete`")


        collection_formats = {}

        resource_path = '/commands/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

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
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api(resource_path, 'DELETE',
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

    def commands_get(self, id, content_type, accept, **kwargs):
        """
        List an individual Command
        Return a single command using the command ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_get(id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commands_get_with_http_info(id, content_type, accept, **kwargs)
        else:
            (data) = self.commands_get_with_http_info(id, content_type, accept, **kwargs)
            return data

    def commands_get_with_http_info(self, id, content_type, accept, **kwargs):
        """
        List an individual Command
        Return a single command using the command ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_get_with_http_info(id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept', 'fields', 'limit', 'skip', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commands_get`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_get`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_get`")


        collection_formats = {}

        resource_path = '/commands/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'skip' in params:
            query_params['skip'] = params['skip']
        if 'sort' in params:
            query_params['sort'] = params['sort']

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
            select_header_accept(['application/json; charset=utf-8'])

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
                                        response_type='Command',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def commands_list(self, content_type, accept, **kwargs):
        """
        List All Commands
        Return all commands.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_list(content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str content_type: (required)
        :param str accept: (required)
        :param int skip: The offset into the records to return.
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: Commandslist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commands_list_with_http_info(content_type, accept, **kwargs)
        else:
            (data) = self.commands_list_with_http_info(content_type, accept, **kwargs)
            return data

    def commands_list_with_http_info(self, content_type, accept, **kwargs):
        """
        List All Commands
        Return all commands.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_list_with_http_info(content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str content_type: (required)
        :param str accept: (required)
        :param int skip: The offset into the records to return.
        :param str fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once.
        :param str sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: Commandslist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'skip', 'fields', 'limit', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_list`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_list`")


        collection_formats = {}

        resource_path = '/commands/'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'skip' in params:
            query_params['skip'] = params['skip']
        if 'fields' in params:
            query_params['fields'] = params['fields']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'sort' in params:
            query_params['sort'] = params['sort']

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
            select_header_accept(['application/json; charset=utf-8'])

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
                                        response_type='Commandslist',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def commands_post(self, content_type, accept, **kwargs):
        """
        Create A Command
        Create a new command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_post(content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commands_post_with_http_info(content_type, accept, **kwargs)
        else:
            (data) = self.commands_post_with_http_info(content_type, accept, **kwargs)
            return data

    def commands_post_with_http_info(self, content_type, accept, **kwargs):
        """
        Create A Command
        Create a new command.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_post_with_http_info(content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_post`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_post`")


        collection_formats = {}

        resource_path = '/commands/'.replace('{format}', 'json')
        path_params = {}

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
            select_header_accept(['application/json; charset=utf-8'])

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
                                        response_type='Command',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def commands_put(self, id, content_type, accept, **kwargs):
        """
        Update a Command
        Updates a command record from the command ID and returns the modified command record.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_put(id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.commands_put_with_http_info(id, content_type, accept, **kwargs)
        else:
            (data) = self.commands_put_with_http_info(id, content_type, accept, **kwargs)
            return data

    def commands_put_with_http_info(self, id, content_type, accept, **kwargs):
        """
        Update a Command
        Updates a command record from the command ID and returns the modified command record.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.commands_put_with_http_info(id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param Command body:
        :return: Command
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content_type', 'accept', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method commands_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `commands_put`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `commands_put`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `commands_put`")


        collection_formats = {}

        resource_path = '/commands/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
            select_header_accept(['application/json; charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Command',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
