from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionAvailabilitiesEndpoint(Endpoint):
    path = '/v1/subscriptionAvailabilities'

    def create(self, request: SubscriptionAvailabilityCreateRequest) -> SubscriptionAvailabilityResponse:
        '''Create the resource.

        :param request: SubscriptionAvailability representation
        :type request: SubscriptionAvailabilityCreateRequest

        :returns: Single SubscriptionAvailability
        :rtype: SubscriptionAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionAvailabilityResponse.parse_obj(json)

class SubscriptionAvailabilityEndpoint(IDEndpoint):
    path = '/v1/subscriptionAvailabilities/{id}'

    @endpoint('/v1/subscriptionAvailabilities/{id}/availableTerritories')
    def available_territories(self) -> AvailableTerritoriesOfSubscriptionAvailabilityEndpoint:
        return AvailableTerritoriesOfSubscriptionAvailabilityEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionAvailabilities/{id}/relationships/availableTerritories')
    def available_territories_linkages(self) -> AvailableTerritoriesLinkagesOfSubscriptionAvailabilityEndpoint:
        return AvailableTerritoriesLinkagesOfSubscriptionAvailabilityEndpoint(self.id, self.session)
        
    def fields(self, *, subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> SubscriptionAvailabilityEndpoint:
        '''Fields to return for included related types.

        :param subscription_availability: the fields to include for returned resources of type subscriptionAvailabilities
        :type subscription_availability: Union[SubscriptionAvailabilityField, list[SubscriptionAvailabilityField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAvailabilityEndpoint
        '''
        if subscription_availability: self._set_fields('subscriptionAvailabilities',subscription_availability if type(subscription_availability) is list else [subscription_availability])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        AVAILABLE_TERRITORIES = 'availableTerritories'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionAvailabilityEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAvailabilityEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, available_territories: int=None) -> SubscriptionAvailabilityEndpoint:
        '''Number of included related resources to return.

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAvailabilityEndpoint
        '''
        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit of available_territories is 50')
        if available_territories: self._set_limit(available_territories, 'availableTerritories')

        return self

    def get(self) -> SubscriptionAvailabilityResponse:
        '''Get the resource.

        :returns: Single SubscriptionAvailability
        :rtype: SubscriptionAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionAvailabilityResponse.parse_obj(json)

class AvailableTerritoriesLinkagesOfSubscriptionAvailabilityEndpoint(IDEndpoint):
    path = '/v1/subscriptionAvailabilities/{id}/relationships/availableTerritories'

    def limit(self, number: int=None) -> AvailableTerritoriesLinkagesOfSubscriptionAvailabilityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesLinkagesOfSubscriptionAvailabilityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionAvailabilityAvailableTerritoriesLinkagesResponse.parse_obj(json)

class AvailableTerritoriesOfSubscriptionAvailabilityEndpoint(IDEndpoint):
    path = '/v1/subscriptionAvailabilities/{id}/availableTerritories'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AvailableTerritoriesOfSubscriptionAvailabilityEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesOfSubscriptionAvailabilityEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def limit(self, number: int=None) -> AvailableTerritoriesOfSubscriptionAvailabilityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesOfSubscriptionAvailabilityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> TerritoriesResponse:
        '''Get one or more resources.

        :returns: List of Territories
        :rtype: TerritoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return TerritoriesResponse.parse_obj(json)

