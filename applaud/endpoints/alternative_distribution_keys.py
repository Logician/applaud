from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AlternativeDistributionKeysEndpoint(Endpoint):
    path = '/v1/alternativeDistributionKeys'

    def fields(self, *, alternative_distribution_key: Union[AlternativeDistributionKeyField, list[AlternativeDistributionKeyField]]=None) -> AlternativeDistributionKeysEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_key: the fields to include for returned resources of type alternativeDistributionKeys
        :type alternative_distribution_key: Union[AlternativeDistributionKeyField, list[AlternativeDistributionKeyField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionKeysEndpoint
        '''
        if alternative_distribution_key: self._set_fields('alternativeDistributionKeys',alternative_distribution_key if type(alternative_distribution_key) is list else [alternative_distribution_key])
        return self
        
    def exists(self, *, app: bool=None) -> AlternativeDistributionKeysEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionKeysEndpoint
        '''
        if app == None:
            return
        
        self._set_exists('app', 'true' if app  else 'false')
        return self
        
    def limit(self, number: int=None) -> AlternativeDistributionKeysEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionKeysEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionKeysResponse:
        '''Get one or more resources.

        :returns: List of AlternativeDistributionKeys
        :rtype: AlternativeDistributionKeysResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionKeysResponse.parse_obj(json)

    def create(self, request: AlternativeDistributionKeyCreateRequest) -> AlternativeDistributionKeyResponse:
        '''Create the resource.

        :param request: AlternativeDistributionKey representation
        :type request: AlternativeDistributionKeyCreateRequest

        :returns: Single AlternativeDistributionKey
        :rtype: AlternativeDistributionKeyResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AlternativeDistributionKeyResponse.parse_obj(json)

class AlternativeDistributionKeyEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionKeys/{id}'

    def fields(self, *, alternative_distribution_key: Union[AlternativeDistributionKeyField, list[AlternativeDistributionKeyField]]=None) -> AlternativeDistributionKeyEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_key: the fields to include for returned resources of type alternativeDistributionKeys
        :type alternative_distribution_key: Union[AlternativeDistributionKeyField, list[AlternativeDistributionKeyField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionKeyEndpoint
        '''
        if alternative_distribution_key: self._set_fields('alternativeDistributionKeys',alternative_distribution_key if type(alternative_distribution_key) is list else [alternative_distribution_key])
        return self
        
    def get(self) -> AlternativeDistributionKeyResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionKey
        :rtype: AlternativeDistributionKeyResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionKeyResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

