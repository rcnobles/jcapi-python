# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The previous version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Tagput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, systems=None, systemusers=None, regular_expressions=None, externally_managed=None, external_dn=None, external_source_type=None, send_to_ldap=None, group_gid=None, group_name=None):
        """
        Tagput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'systems': 'list[str]',
            'systemusers': 'list[str]',
            'regular_expressions': 'list[str]',
            'externally_managed': 'bool',
            'external_dn': 'str',
            'external_source_type': 'str',
            'send_to_ldap': 'bool',
            'group_gid': 'str',
            'group_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'systems': 'systems',
            'systemusers': 'systemusers',
            'regular_expressions': 'regularExpressions',
            'externally_managed': 'externallyManaged',
            'external_dn': 'externalDN',
            'external_source_type': 'externalSourceType',
            'send_to_ldap': 'sendToLDAP',
            'group_gid': 'groupGid',
            'group_name': 'groupName'
        }

        self._name = name
        self._systems = systems
        self._systemusers = systemusers
        self._regular_expressions = regular_expressions
        self._externally_managed = externally_managed
        self._external_dn = external_dn
        self._external_source_type = external_source_type
        self._send_to_ldap = send_to_ldap
        self._group_gid = group_gid
        self._group_name = group_name

    @property
    def name(self):
        """
        Gets the name of this Tagput.
        A unique name for the Tag.

        :return: The name of this Tagput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tagput.
        A unique name for the Tag.

        :param name: The name of this Tagput.
        :type: str
        """

        self._name = name

    @property
    def systems(self):
        """
        Gets the systems of this Tagput.
        An array of system ids that are associated to the Tag.

        :return: The systems of this Tagput.
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """
        Sets the systems of this Tagput.
        An array of system ids that are associated to the Tag.

        :param systems: The systems of this Tagput.
        :type: list[str]
        """

        self._systems = systems

    @property
    def systemusers(self):
        """
        Gets the systemusers of this Tagput.
        An array of system user ids that are associated to the Tag.

        :return: The systemusers of this Tagput.
        :rtype: list[str]
        """
        return self._systemusers

    @systemusers.setter
    def systemusers(self, systemusers):
        """
        Sets the systemusers of this Tagput.
        An array of system user ids that are associated to the Tag.

        :param systemusers: The systemusers of this Tagput.
        :type: list[str]
        """

        self._systemusers = systemusers

    @property
    def regular_expressions(self):
        """
        Gets the regular_expressions of this Tagput.

        :return: The regular_expressions of this Tagput.
        :rtype: list[str]
        """
        return self._regular_expressions

    @regular_expressions.setter
    def regular_expressions(self, regular_expressions):
        """
        Sets the regular_expressions of this Tagput.

        :param regular_expressions: The regular_expressions of this Tagput.
        :type: list[str]
        """

        self._regular_expressions = regular_expressions

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this Tagput.

        :return: The externally_managed of this Tagput.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this Tagput.

        :param externally_managed: The externally_managed of this Tagput.
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def external_dn(self):
        """
        Gets the external_dn of this Tagput.

        :return: The external_dn of this Tagput.
        :rtype: str
        """
        return self._external_dn

    @external_dn.setter
    def external_dn(self, external_dn):
        """
        Sets the external_dn of this Tagput.

        :param external_dn: The external_dn of this Tagput.
        :type: str
        """

        self._external_dn = external_dn

    @property
    def external_source_type(self):
        """
        Gets the external_source_type of this Tagput.

        :return: The external_source_type of this Tagput.
        :rtype: str
        """
        return self._external_source_type

    @external_source_type.setter
    def external_source_type(self, external_source_type):
        """
        Sets the external_source_type of this Tagput.

        :param external_source_type: The external_source_type of this Tagput.
        :type: str
        """

        self._external_source_type = external_source_type

    @property
    def send_to_ldap(self):
        """
        Gets the send_to_ldap of this Tagput.

        :return: The send_to_ldap of this Tagput.
        :rtype: bool
        """
        return self._send_to_ldap

    @send_to_ldap.setter
    def send_to_ldap(self, send_to_ldap):
        """
        Sets the send_to_ldap of this Tagput.

        :param send_to_ldap: The send_to_ldap of this Tagput.
        :type: bool
        """

        self._send_to_ldap = send_to_ldap

    @property
    def group_gid(self):
        """
        Gets the group_gid of this Tagput.

        :return: The group_gid of this Tagput.
        :rtype: str
        """
        return self._group_gid

    @group_gid.setter
    def group_gid(self, group_gid):
        """
        Sets the group_gid of this Tagput.

        :param group_gid: The group_gid of this Tagput.
        :type: str
        """

        self._group_gid = group_gid

    @property
    def group_name(self):
        """
        Gets the group_name of this Tagput.

        :return: The group_name of this Tagput.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this Tagput.

        :param group_name: The group_name of this Tagput.
        :type: str
        """

        self._group_name = group_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Tagput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
