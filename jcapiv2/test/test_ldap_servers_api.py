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
from jcapiv2.apis.ldap_servers_api import LDAPServersApi


class TestLDAPServersApi(unittest.TestCase):
    """ LDAPServersApi unit test stubs """

    def setUp(self):
        self.api = jcapiv2.apis.ldap_servers_api.LDAPServersApi()

    def tearDown(self):
        pass

    def test_graph_ldap_server_associations_list(self):
        """
        Test case for graph_ldap_server_associations_list

        List the associations of a LDAP Server
        """
        pass

    def test_graph_ldap_server_associations_post(self):
        """
        Test case for graph_ldap_server_associations_post

        Manage the associations of a LDAP Server
        """
        pass

    def test_graph_ldap_server_traverse_user(self):
        """
        Test case for graph_ldap_server_traverse_user

        List the Users bound to a LDAP Server
        """
        pass

    def test_graph_ldap_server_traverse_user_group(self):
        """
        Test case for graph_ldap_server_traverse_user_group

        List the User Groups bound to a LDAP Server
        """
        pass

    def test_ldapservers_get(self):
        """
        Test case for ldapservers_get

        Get LDAP Server
        """
        pass

    def test_ldapservers_list(self):
        """
        Test case for ldapservers_list

        List LDAP Servers
        """
        pass


if __name__ == '__main__':
    unittest.main()
