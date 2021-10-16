# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.api_model import ApiModel  # noqa: F401,E501
from swagger_server import util


class ApiListModelsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, models: List[ApiModel]=None, total_size: int=None, next_page_token: str=None):  # noqa: E501
        """ApiListModelsResponse - a model defined in Swagger

        :param models: The models of this ApiListModelsResponse.  # noqa: E501
        :type models: List[ApiModel]
        :param total_size: The total_size of this ApiListModelsResponse.  # noqa: E501
        :type total_size: int
        :param next_page_token: The next_page_token of this ApiListModelsResponse.  # noqa: E501
        :type next_page_token: str
        """
        self.swagger_types = {
            'models': List[ApiModel],
            'total_size': int,
            'next_page_token': str
        }

        self.attribute_map = {
            'models': 'models',
            'total_size': 'total_size',
            'next_page_token': 'next_page_token'
        }

        self._models = models
        self._total_size = total_size
        self._next_page_token = next_page_token

    @classmethod
    def from_dict(cls, dikt) -> 'ApiListModelsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiListModelsResponse of this ApiListModelsResponse.  # noqa: E501
        :rtype: ApiListModelsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def models(self) -> List[ApiModel]:
        """Gets the models of this ApiListModelsResponse.


        :return: The models of this ApiListModelsResponse.
        :rtype: List[ApiModel]
        """
        return self._models

    @models.setter
    def models(self, models: List[ApiModel]):
        """Sets the models of this ApiListModelsResponse.


        :param models: The models of this ApiListModelsResponse.
        :type models: List[ApiModel]
        """

        self._models = models

    @property
    def total_size(self) -> int:
        """Gets the total_size of this ApiListModelsResponse.


        :return: The total_size of this ApiListModelsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size: int):
        """Sets the total_size of this ApiListModelsResponse.


        :param total_size: The total_size of this ApiListModelsResponse.
        :type total_size: int
        """

        self._total_size = total_size

    @property
    def next_page_token(self) -> str:
        """Gets the next_page_token of this ApiListModelsResponse.


        :return: The next_page_token of this ApiListModelsResponse.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token: str):
        """Sets the next_page_token of this ApiListModelsResponse.


        :param next_page_token: The next_page_token of this ApiListModelsResponse.
        :type next_page_token: str
        """

        self._next_page_token = next_page_token
