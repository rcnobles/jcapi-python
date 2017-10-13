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


class ApplicationConfigIdpEntityIdTooltip(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, template=None, variables=None):
        """
        ApplicationConfigIdpEntityIdTooltip - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'template': 'str',
            'variables': 'ApplicationConfigIdpEntityIdTooltipVariables'
        }

        self.attribute_map = {
            'template': 'template',
            'variables': 'variables'
        }

        self._template = template
        self._variables = variables

    @property
    def template(self):
        """
        Gets the template of this ApplicationConfigIdpEntityIdTooltip.

        :return: The template of this ApplicationConfigIdpEntityIdTooltip.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this ApplicationConfigIdpEntityIdTooltip.

        :param template: The template of this ApplicationConfigIdpEntityIdTooltip.
        :type: str
        """

        self._template = template

    @property
    def variables(self):
        """
        Gets the variables of this ApplicationConfigIdpEntityIdTooltip.

        :return: The variables of this ApplicationConfigIdpEntityIdTooltip.
        :rtype: ApplicationConfigIdpEntityIdTooltipVariables
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this ApplicationConfigIdpEntityIdTooltip.

        :param variables: The variables of this ApplicationConfigIdpEntityIdTooltip.
        :type: ApplicationConfigIdpEntityIdTooltipVariables
        """

        self._variables = variables

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
        if not isinstance(other, ApplicationConfigIdpEntityIdTooltip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
