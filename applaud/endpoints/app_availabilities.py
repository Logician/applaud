from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppAvailabilitiesEndpoint(Endpoint):
    path = '/v2/appAvailabilities'

    def create(self, request: AppAvailabilityV2CreateRequest) -> AppAvailabilityV2Response:
        '''Create the resource.

        :param request: AppAvailability representation
        :type request: AppAvailabilityV2CreateRequest

        :returns: Single AppAvailability
        :rtype: AppAvailabilityV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppAvailabilityV2Response.parse_obj(json)

class AppAvailabilityEndpoint(IDEndpoint):
    path = '/v2/appAvailabilities/{id}'

    @endpoint('/v2/appAvailabilities/{id}/territoryAvailabilities')
    def territory_availabilities(self) -> TerritoryAvailabilitiesOfAppAvailabilityEndpoint:
        return TerritoryAvailabilitiesOfAppAvailabilityEndpoint(self.id, self.session)
        
    @endpoint('/v2/appAvailabilities/{id}/relationships/territoryAvailabilities')
    def territory_availabilities_linkages(self) -> TerritoryAvailabilitiesLinkagesOfAppAvailabilityEndpoint:
        return TerritoryAvailabilitiesLinkagesOfAppAvailabilityEndpoint(self.id, self.session)
        
    def fields(self, *, app_availability: Union[AppAvailabilityField, list[AppAvailabilityField]]=None, territory_availability: Union[TerritoryAvailabilityField, list[TerritoryAvailabilityField]]=None) -> AppAvailabilityEndpoint:
        '''Fields to return for included related types.

        :param app_availability: the fields to include for returned resources of type appAvailabilities
        :type app_availability: Union[AppAvailabilityField, list[AppAvailabilityField]] = None

        :param territory_availability: the fields to include for returned resources of type territoryAvailabilities
        :type territory_availability: Union[TerritoryAvailabilityField, list[TerritoryAvailabilityField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppAvailabilityEndpoint
        '''
        if app_availability: self._set_fields('appAvailabilities',app_availability if type(app_availability) is list else [app_availability])
        if territory_availability: self._set_fields('territoryAvailabilities',territory_availability if type(territory_availability) is list else [territory_availability])
        return self
        
    class Include(StringEnum):
        TERRITORY_AVAILABILITIES = 'territoryAvailabilities'

    def include(self, relationship: Union[Include, list[Include]]) -> AppAvailabilityEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppAvailabilityEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, territory_availabilities: int=None) -> AppAvailabilityEndpoint:
        '''Number of included related resources to return.

        :param territory_availabilities: maximum number of related territoryAvailabilities returned (when they are included). The maximum limit is 50
        :type territory_availabilities: int = None

        :returns: self
        :rtype: applaud.endpoints.AppAvailabilityEndpoint
        '''
        if territory_availabilities and territory_availabilities > 50:
            raise ValueError(f'The maximum limit of territory_availabilities is 50')
        if territory_availabilities: self._set_limit(territory_availabilities, 'territoryAvailabilities')

        return self

    def get(self) -> AppAvailabilityV2Response:
        '''Get the resource.

        :returns: Single AppAvailability
        :rtype: AppAvailabilityV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAvailabilityV2Response.parse_obj(json)

class TerritoryAvailabilitiesLinkagesOfAppAvailabilityEndpoint(IDEndpoint):
    path = '/v2/appAvailabilities/{id}/relationships/territoryAvailabilities'

    def limit(self, number: int=None) -> TerritoryAvailabilitiesLinkagesOfAppAvailabilityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TerritoryAvailabilitiesLinkagesOfAppAvailabilityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAvailabilityV2TerritoryAvailabilitiesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAvailabilityV2TerritoryAvailabilitiesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAvailabilityV2TerritoryAvailabilitiesLinkagesResponse.parse_obj(json)

class TerritoryAvailabilitiesOfAppAvailabilityEndpoint(IDEndpoint):
    path = '/v2/appAvailabilities/{id}/territoryAvailabilities'

    def fields(self, *, territory_availability: Union[TerritoryAvailabilityField, list[TerritoryAvailabilityField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> TerritoryAvailabilitiesOfAppAvailabilityEndpoint:
        '''Fields to return for included related types.

        :param territory_availability: the fields to include for returned resources of type territoryAvailabilities
        :type territory_availability: Union[TerritoryAvailabilityField, list[TerritoryAvailabilityField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.TerritoryAvailabilitiesOfAppAvailabilityEndpoint
        '''
        if territory_availability: self._set_fields('territoryAvailabilities',territory_availability if type(territory_availability) is list else [territory_availability])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def include(self, relationship: Union[Include, list[Include]]) -> TerritoryAvailabilitiesOfAppAvailabilityEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.TerritoryAvailabilitiesOfAppAvailabilityEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> TerritoryAvailabilitiesOfAppAvailabilityEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TerritoryAvailabilitiesOfAppAvailabilityEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> TerritoryAvailabilitiesResponse:
        '''Get one or more resources.

        :returns: List of TerritoryAvailabilities
        :rtype: TerritoryAvailabilitiesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return TerritoryAvailabilitiesResponse.parse_obj(json)

