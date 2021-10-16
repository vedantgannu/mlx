# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.any_value import AnyValue  # noqa: F401,E501
from swagger_server import util


class ApiParameter(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, description: str=None, default: AnyValue=None, value: AnyValue=None):  # noqa: E501
        """ApiParameter - a model defined in Swagger

        :param name: The name of this ApiParameter.  # noqa: E501
        :type name: str
        :param description: The description of this ApiParameter.  # noqa: E501
        :type description: str
        :param default: The default of this ApiParameter.  # noqa: E501
        :type default: AnyValue
        :param value: The value of this ApiParameter.  # noqa: E501
        :type value: AnyValue
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'default': AnyValue,
            'value': AnyValue
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'default': 'default',
            'value': 'value'
        }

        self._name = name
        self._description = description
        self._default = default
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'ApiParameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiParameter of this ApiParameter.  # noqa: E501
        :rtype: ApiParameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ApiParameter.


        :return: The name of this ApiParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ApiParameter.


        :param name: The name of this ApiParameter.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this ApiParameter.


        :return: The description of this ApiParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ApiParameter.


        :param description: The description of this ApiParameter.
        :type description: str
        """

        self._description = description

    @property
    def default(self) -> AnyValue:
        """Gets the default of this ApiParameter.


        :return: The default of this ApiParameter.
        :rtype: AnyValue
        """
        return self._default

    @default.setter
    def default(self, default: AnyValue):
        """Sets the default of this ApiParameter.


        :param default: The default of this ApiParameter.
        :type default: AnyValue
        """

        self._default = default

    @property
    def value(self) -> AnyValue:
        """Gets the value of this ApiParameter.


        :return: The value of this ApiParameter.
        :rtype: AnyValue
        """
        return self._value

    @value.setter
    def value(self, value: AnyValue):
        """Sets the value of this ApiParameter.


        :param value: The value of this ApiParameter.
        :type value: AnyValue
        """

        self._value = value
