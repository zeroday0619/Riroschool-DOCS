# coding: utf-8

"""
    리로스쿨 API

    리로스쿨 2.9 버전의 API  # noqa: E501

    OpenAPI spec version: 2.9.0
    Contact: develop@rirosoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Device(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'uuid': 'str',
        'ip': 'str',
        'fcm_code': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'ip': 'ip',
        'fcm_code': 'fcmCode',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, uuid=None, ip=None, fcm_code=None, type=None, version=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._uuid = None
        self._ip = None
        self._fcm_code = None
        self._type = None
        self._version = None
        self.discriminator = None
        if uuid is not None:
            self.uuid = uuid
        if ip is not None:
            self.ip = ip
        if fcm_code is not None:
            self.fcm_code = fcm_code
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def uuid(self):
        """Gets the uuid of this Device.  # noqa: E501

        기기 고유번호  # noqa: E501

        :return: The uuid of this Device.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Device.

        기기 고유번호  # noqa: E501

        :param uuid: The uuid of this Device.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def ip(self):
        """Gets the ip of this Device.  # noqa: E501

        접속 아이피  # noqa: E501

        :return: The ip of this Device.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Device.

        접속 아이피  # noqa: E501

        :param ip: The ip of this Device.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def fcm_code(self):
        """Gets the fcm_code of this Device.  # noqa: E501

        fcm 코드  # noqa: E501

        :return: The fcm_code of this Device.  # noqa: E501
        :rtype: str
        """
        return self._fcm_code

    @fcm_code.setter
    def fcm_code(self, fcm_code):
        """Sets the fcm_code of this Device.

        fcm 코드  # noqa: E501

        :param fcm_code: The fcm_code of this Device.  # noqa: E501
        :type: str
        """

        self._fcm_code = fcm_code

    @property
    def type(self):
        """Gets the type of this Device.  # noqa: E501

        Android || iPhone || iPop || iPad  # noqa: E501

        :return: The type of this Device.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Device.

        Android || iPhone || iPop || iPad  # noqa: E501

        :param type: The type of this Device.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this Device.  # noqa: E501

        앱 버전  # noqa: E501

        :return: The version of this Device.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Device.

        앱 버전  # noqa: E501

        :param version: The version of this Device.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Device, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
