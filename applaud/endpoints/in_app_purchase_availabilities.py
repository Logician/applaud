from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseAvailabilitiesEndpoint(Endpoint):
    path = '/v1/inAppPurchaseAvailabilities'

    def create(self, request: InAppPurchaseAvailabilityCreateRequest) -> InAppPurchaseAvailabilityResponse:
        '''Create the resource.

        :param request: InAppPurchaseAvailability representation
        :type request: InAppPurchaseAvailabilityCreateRequest

        :returns: Single InAppPurchaseAvailability
        :rtype: InAppPurchaseAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseAvailabilityResponse.parse_obj(json)

class InAppPurchaseAvailabilityEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseAvailabilities/{id}'

    @endpoint('/v1/inAppPurchaseAvailabilities/{id}/availableTerritories')
    def available_territories(self) -> AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint:
        return AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchaseAvailabilities/{id}/relationships/availableTerritories')
    def available_territories_linkages(self) -> AvailableTerritoriesLinkagesOfInAppPurchaseAvailabilityEndpoint:
        return AvailableTerritoriesLinkagesOfInAppPurchaseAvailabilityEndpoint(self.id, self.session)
        
    def fields(self, *, in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> InAppPurchaseAvailabilityEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_availability: the fields to include for returned resources of type inAppPurchaseAvailabilities
        :type in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAvailabilityEndpoint
        '''
        if in_app_purchase_availability: self._set_fields('inAppPurchaseAvailabilities',in_app_purchase_availability if type(in_app_purchase_availability) is list else [in_app_purchase_availability])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        AVAILABLE_TERRITORIES = 'availableTerritories'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseAvailabilityEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAvailabilityEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, available_territories: int=None) -> InAppPurchaseAvailabilityEndpoint:
        '''Number of included related resources to return.

        :param available_territories: maximum number of related availableTerritories returned (when they are included). The maximum limit is 50
        :type available_territories: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAvailabilityEndpoint
        '''
        if available_territories and available_territories > 50:
            raise ValueError(f'The maximum limit of available_territories is 50')
        if available_territories: self._set_limit(available_territories, 'availableTerritories')

        return self

    def get(self) -> InAppPurchaseAvailabilityResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseAvailability
        :rtype: InAppPurchaseAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseAvailabilityResponse.parse_obj(json)

class AvailableTerritoriesLinkagesOfInAppPurchaseAvailabilityEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseAvailabilities/{id}/relationships/availableTerritories'

    def limit(self, number: int=None) -> AvailableTerritoriesLinkagesOfInAppPurchaseAvailabilityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesLinkagesOfInAppPurchaseAvailabilityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse.parse_obj(json)

class AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseAvailabilities/{id}/availableTerritories'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def limit(self, number: int=None) -> AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AvailableTerritoriesOfInAppPurchaseAvailabilityEndpoint
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

