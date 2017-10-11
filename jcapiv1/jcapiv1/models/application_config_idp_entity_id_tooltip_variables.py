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


class ApplicationConfigIdpEntityIdTooltipVariables(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, icon=None, message=None):
        """
        ApplicationConfigIdpEntityIdTooltipVariables - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'icon': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'icon': 'icon',
            'message': 'message'
        }

        self._icon = icon
        self._message = message

    @property
    def icon(self):
        """
        Gets the icon of this ApplicationConfigIdpEntityIdTooltipVariables.

        :return: The icon of this ApplicationConfigIdpEntityIdTooltipVariables.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this ApplicationConfigIdpEntityIdTooltipVariables.

        :param icon: The icon of this ApplicationConfigIdpEntityIdTooltipVariables.
        :type: str
        """

        self._icon = icon

    @property
    def message(self):
        """
        Gets the message of this ApplicationConfigIdpEntityIdTooltipVariables.

        :return: The message of this ApplicationConfigIdpEntityIdTooltipVariables.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ApplicationConfigIdpEntityIdTooltipVariables.

        :param message: The message of this ApplicationConfigIdpEntityIdTooltipVariables.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ApplicationConfigIdpEntityIdTooltipVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
