# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv1
from jcapiv1.rest import ApiException
from jcapiv1.models.tagpost import Tagpost


class TestTagpost(unittest.TestCase):
    """ Tagpost unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTagpost(self):
        """
        Test Tagpost
        """
        model = jcapiv1.models.tagpost.Tagpost()


if __name__ == '__main__':
    unittest.main()
