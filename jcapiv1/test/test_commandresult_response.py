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
from jcapiv1.models.commandresult_response import CommandresultResponse


class TestCommandresultResponse(unittest.TestCase):
    """ CommandresultResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommandresultResponse(self):
        """
        Test CommandresultResponse
        """
        model = jcapiv1.models.commandresult_response.CommandresultResponse()


if __name__ == '__main__':
    unittest.main()