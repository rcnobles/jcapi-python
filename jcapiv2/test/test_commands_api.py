# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import jcapiv2
from jcapiv2.rest import ApiException
from jcapiv2.apis.commands_api import CommandsApi


class TestCommandsApi(unittest.TestCase):
    """ CommandsApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.commands_api.CommandsApi()

    def tearDown(self):
        pass

    def test_graph_command_associations_list(self):
        """
        Test case for graph_command_associations_list

        List the associations of a Command
        """
        pass

    def test_graph_command_associations_post(self):
        """
        Test case for graph_command_associations_post

        Manage the associations of a Command
        """
        pass

    def test_graph_command_traverse_system(self):
        """
        Test case for graph_command_traverse_system

        List the Systems bound to a Command
        """
        pass

    def test_graph_command_traverse_system_group(self):
        """
        Test case for graph_command_traverse_system_group

        List the System Groups bound to a Command
        """
        pass


if __name__ == '__main__':
    unittest.main()
