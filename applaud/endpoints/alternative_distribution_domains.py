from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AlternativeDistributionDomainsEndpoint(Endpoint):
    path = '/v1/alternativeDistributionDomains'

    def fields(self, *, alternative_distribution_domain: Union[AlternativeDistributionDomainField, list[AlternativeDistributionDomainField]]=None) -> AlternativeDistributionDomainsEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_domain: the fields to include for returned resources of type alternativeDistributionDomains
        :type alternative_distribution_domain: Union[AlternativeDistributionDomainField, list[AlternativeDistributionDomainField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionDomainsEndpoint
        '''
        if alternative_distribution_domain: self._set_fields('alternativeDistributionDomains',alternative_distribution_domain if type(alternative_distribution_domain) is list else [alternative_distribution_domain])
        return self
        
    def limit(self, number: int=None) -> AlternativeDistributionDomainsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionDomainsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AlternativeDistributionDomainsResponse:
        '''Get one or more resources.

        :returns: List of AlternativeDistributionDomains
        :rtype: AlternativeDistributionDomainsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionDomainsResponse.parse_obj(json)

    def create(self, request: AlternativeDistributionDomainCreateRequest) -> AlternativeDistributionDomainResponse:
        '''Create the resource.

        :param request: AlternativeDistributionDomain representation
        :type request: AlternativeDistributionDomainCreateRequest

        :returns: Single AlternativeDistributionDomain
        :rtype: AlternativeDistributionDomainResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AlternativeDistributionDomainResponse.parse_obj(json)

class AlternativeDistributionDomainEndpoint(IDEndpoint):
    path = '/v1/alternativeDistributionDomains/{id}'

    def fields(self, *, alternative_distribution_domain: Union[AlternativeDistributionDomainField, list[AlternativeDistributionDomainField]]=None) -> AlternativeDistributionDomainEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_domain: the fields to include for returned resources of type alternativeDistributionDomains
        :type alternative_distribution_domain: Union[AlternativeDistributionDomainField, list[AlternativeDistributionDomainField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionDomainEndpoint
        '''
        if alternative_distribution_domain: self._set_fields('alternativeDistributionDomains',alternative_distribution_domain if type(alternative_distribution_domain) is list else [alternative_distribution_domain])
        return self
        
    def get(self) -> AlternativeDistributionDomainResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionDomain
        :rtype: AlternativeDistributionDomainResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionDomainResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

