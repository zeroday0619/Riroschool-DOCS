# coding: utf-8

"""
    리로스쿨 API

    리로스쿨 2.9 버전의 API  # noqa: E501

    OpenAPI spec version: 2.9.0
    Contact: develop@rirosoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.school_api import SchoolApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSchoolApi(unittest.TestCase):
    """SchoolApi unit test stubs"""

    def setUp(self):
        self.api = api.school_api.SchoolApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_get(self):
        """Test case for check_get

        상태 체크  # noqa: E501
        """
        pass

    def test_health_check_get(self):
        """Test case for health_check_get

        상태 체크  # noqa: E501
        """
        pass

    def test_school_get(self):
        """Test case for school_get

        리로스쿨 학교 리스트  # noqa: E501
        """
        pass

    def test_school_menu_get(self):
        """Test case for school_menu_get

        학교 사이드 메뉴  # noqa: E501
        """
        pass

    def test_school_search_get(self):
        """Test case for school_search_get

        리로스쿨 학교 검색  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
