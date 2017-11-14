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


class ApplicationConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'idp_entity_id': 'ApplicationConfigIdpEntityId',
        'idp_certificate': 'ApplicationConfigIdpEntityId',
        'sp_entity_id': 'ApplicationConfigIdpEntityId',
        'acs_url': 'ApplicationConfigIdpEntityId',
        'constant_attributes': 'ApplicationConfigConstantAttributes',
        'database_attributes': 'ApplicationConfigDatabaseAttributes'
    }

    attribute_map = {
        'idp_entity_id': 'idpEntityId',
        'idp_certificate': 'idpCertificate',
        'sp_entity_id': 'spEntityId',
        'acs_url': 'acsUrl',
        'constant_attributes': 'constantAttributes',
        'database_attributes': 'databaseAttributes'
    }

    def __init__(self, idp_entity_id=None, idp_certificate=None, sp_entity_id=None, acs_url=None, constant_attributes=None, database_attributes=None):
        """
        ApplicationConfig - a model defined in Swagger
        """

        self._idp_entity_id = None
        self._idp_certificate = None
        self._sp_entity_id = None
        self._acs_url = None
        self._constant_attributes = None
        self._database_attributes = None

        if idp_entity_id is not None:
          self.idp_entity_id = idp_entity_id
        if idp_certificate is not None:
          self.idp_certificate = idp_certificate
        if sp_entity_id is not None:
          self.sp_entity_id = sp_entity_id
        if acs_url is not None:
          self.acs_url = acs_url
        if constant_attributes is not None:
          self.constant_attributes = constant_attributes
        if database_attributes is not None:
          self.database_attributes = database_attributes

    @property
    def idp_entity_id(self):
        """
        Gets the idp_entity_id of this ApplicationConfig.

        :return: The idp_entity_id of this ApplicationConfig.
        :rtype: ApplicationConfigIdpEntityId
        """
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, idp_entity_id):
        """
        Sets the idp_entity_id of this ApplicationConfig.

        :param idp_entity_id: The idp_entity_id of this ApplicationConfig.
        :type: ApplicationConfigIdpEntityId
        """

        self._idp_entity_id = idp_entity_id

    @property
    def idp_certificate(self):
        """
        Gets the idp_certificate of this ApplicationConfig.

        :return: The idp_certificate of this ApplicationConfig.
        :rtype: ApplicationConfigIdpEntityId
        """
        return self._idp_certificate

    @idp_certificate.setter
    def idp_certificate(self, idp_certificate):
        """
        Sets the idp_certificate of this ApplicationConfig.

        :param idp_certificate: The idp_certificate of this ApplicationConfig.
        :type: ApplicationConfigIdpEntityId
        """

        self._idp_certificate = idp_certificate

    @property
    def sp_entity_id(self):
        """
        Gets the sp_entity_id of this ApplicationConfig.

        :return: The sp_entity_id of this ApplicationConfig.
        :rtype: ApplicationConfigIdpEntityId
        """
        return self._sp_entity_id

    @sp_entity_id.setter
    def sp_entity_id(self, sp_entity_id):
        """
        Sets the sp_entity_id of this ApplicationConfig.

        :param sp_entity_id: The sp_entity_id of this ApplicationConfig.
        :type: ApplicationConfigIdpEntityId
        """

        self._sp_entity_id = sp_entity_id

    @property
    def acs_url(self):
        """
        Gets the acs_url of this ApplicationConfig.

        :return: The acs_url of this ApplicationConfig.
        :rtype: ApplicationConfigIdpEntityId
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """
        Sets the acs_url of this ApplicationConfig.

        :param acs_url: The acs_url of this ApplicationConfig.
        :type: ApplicationConfigIdpEntityId
        """

        self._acs_url = acs_url

    @property
    def constant_attributes(self):
        """
        Gets the constant_attributes of this ApplicationConfig.

        :return: The constant_attributes of this ApplicationConfig.
        :rtype: ApplicationConfigConstantAttributes
        """
        return self._constant_attributes

    @constant_attributes.setter
    def constant_attributes(self, constant_attributes):
        """
        Sets the constant_attributes of this ApplicationConfig.

        :param constant_attributes: The constant_attributes of this ApplicationConfig.
        :type: ApplicationConfigConstantAttributes
        """

        self._constant_attributes = constant_attributes

    @property
    def database_attributes(self):
        """
        Gets the database_attributes of this ApplicationConfig.

        :return: The database_attributes of this ApplicationConfig.
        :rtype: ApplicationConfigDatabaseAttributes
        """
        return self._database_attributes

    @database_attributes.setter
    def database_attributes(self, database_attributes):
        """
        Sets the database_attributes of this ApplicationConfig.

        :param database_attributes: The database_attributes of this ApplicationConfig.
        :type: ApplicationConfigDatabaseAttributes
        """

        self._database_attributes = database_attributes

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
        if not isinstance(other, ApplicationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
