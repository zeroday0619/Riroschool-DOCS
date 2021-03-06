# coding: utf-8

"""
    리로스쿨 API

    리로스쿨 2.9 버전의 API  # noqa: E501

    OpenAPI spec version: 2.9.0
    Contact: develop@rirosoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ChildApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def child_delete(self, client_id, authorization, site_id, name, snum, **kwargs):  # noqa: E501
        """자녀 등록 해제  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_delete(client_id, authorization, site_id, name, snum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: API Key (required)
        :param str authorization: 토큰 : tokenType + ' ' + token (required)
        :param str site_id: 학교 아이디 (required)
        :param str name: 자녀 이름 (required)
        :param str snum: 자녀 학번 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.child_delete_with_http_info(client_id, authorization, site_id, name, snum, **kwargs)  # noqa: E501
        else:
            (data) = self.child_delete_with_http_info(client_id, authorization, site_id, name, snum, **kwargs)  # noqa: E501
            return data

    def child_delete_with_http_info(self, client_id, authorization, site_id, name, snum, **kwargs):  # noqa: E501
        """자녀 등록 해제  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_delete_with_http_info(client_id, authorization, site_id, name, snum, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: API Key (required)
        :param str authorization: 토큰 : tokenType + ' ' + token (required)
        :param str site_id: 학교 아이디 (required)
        :param str name: 자녀 이름 (required)
        :param str snum: 자녀 학번 (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'authorization', 'site_id', 'name', 'snum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method child_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `child_delete`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `child_delete`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `child_delete`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `child_delete`")  # noqa: E501
        # verify the required parameter 'snum' is set
        if ('snum' not in params or
                params['snum'] is None):
            raise ValueError("Missing the required parameter `snum` when calling `child_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'site_id' in params:
            query_params.append(('siteId', params['site_id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'snum' in params:
            query_params.append(('snum', params['snum']))  # noqa: E501

        header_params = {}
        if 'client_id' in params:
            header_params['client-id'] = params['client_id']  # noqa: E501
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/child', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def child_get(self, client_id, authorization, **kwargs):  # noqa: E501
        """자녀 목록  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_get(client_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: API Key (required)
        :param str authorization: 토큰 : tokenType + ' ' + token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.child_get_with_http_info(client_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.child_get_with_http_info(client_id, authorization, **kwargs)  # noqa: E501
            return data

    def child_get_with_http_info(self, client_id, authorization, **kwargs):  # noqa: E501
        """자녀 목록  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_get_with_http_info(client_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: API Key (required)
        :param str authorization: 토큰 : tokenType + ' ' + token (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method child_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `child_get`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `child_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_id' in params:
            header_params['client-id'] = params['client_id']  # noqa: E501
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/child', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def child_post(self, client_id, **kwargs):  # noqa: E501
        """자녀 인증  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_post(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: API Key (required)
        :param Child body: 학생정보
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.child_post_with_http_info(client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.child_post_with_http_info(client_id, **kwargs)  # noqa: E501
            return data

    def child_post_with_http_info(self, client_id, **kwargs):  # noqa: E501
        """자녀 인증  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_post_with_http_info(client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: API Key (required)
        :param Child body: 학생정보
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method child_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `child_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'client_id' in params:
            header_params['client-id'] = params['client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/child', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def child_put(self, authorization, client_id, **kwargs):  # noqa: E501
        """자녀 등록  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_put(authorization, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: 토큰 : tokenType + ' ' + token (required)
        :param str client_id: API Key (required)
        :param Child body: 학생정보
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.child_put_with_http_info(authorization, client_id, **kwargs)  # noqa: E501
        else:
            (data) = self.child_put_with_http_info(authorization, client_id, **kwargs)  # noqa: E501
            return data

    def child_put_with_http_info(self, authorization, client_id, **kwargs):  # noqa: E501
        """자녀 등록  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.child_put_with_http_info(authorization, client_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: 토큰 : tokenType + ' ' + token (required)
        :param str client_id: API Key (required)
        :param Child body: 학생정보
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'client_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method child_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `child_put`")  # noqa: E501
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params or
                params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `child_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['authorization'] = params['authorization']  # noqa: E501
        if 'client_id' in params:
            header_params['client-id'] = params['client_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/child', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
