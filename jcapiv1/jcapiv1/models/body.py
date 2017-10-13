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


class Body(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, network_source_ip=None, tags=None):
        """
        Body - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'network_source_ip': 'str',
            'tags': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'network_source_ip': 'networkSourceIp',
            'tags': 'tags'
        }

        self._name = name
        self._network_source_ip = network_source_ip
        self._tags = tags

    @property
    def name(self):
        """
        Gets the name of this Body.

        :return: The name of this Body.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Body.

        :param name: The name of this Body.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def network_source_ip(self):
        """
        Gets the network_source_ip of this Body.

        :return: The network_source_ip of this Body.
        :rtype: str
        """
        return self._network_source_ip

    @network_source_ip.setter
    def network_source_ip(self, network_source_ip):
        """
        Sets the network_source_ip of this Body.

        :param network_source_ip: The network_source_ip of this Body.
        :type: str
        """
        if network_source_ip is None:
            raise ValueError("Invalid value for `network_source_ip`, must not be `None`")

        self._network_source_ip = network_source_ip

    @property
    def tags(self):
        """
        Gets the tags of this Body.

        :return: The tags of this Body.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Body.

        :param tags: The tags of this Body.
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Body):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
