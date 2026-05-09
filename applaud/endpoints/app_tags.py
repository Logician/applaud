from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppTagEndpoint(IDEndpoint):
    path = '/v1/appTags/{id}'

    @endpoint('/v1/appTags/{id}/territories')
    def territories(self) -> TerritoriesOfAppTagEndpoint:
        return TerritoriesOfAppTagEndpoint(self.id, self.session)
        
    @endpoint('/v1/appTags/{id}/relationships/territories')
    def territories_linkages(self) -> TerritoriesLinkagesOfAppTagEndpoint:
        return TerritoriesLinkagesOfAppTagEndpoint(self.id, self.session)
        
    def update(self, request: AppTagUpdateRequest) -> AppTagResponse:
        '''Modify the resource.

        :param request: AppTag representation
        :type request: AppTagUpdateRequest

        :returns: Single AppTag
        :rtype: AppTagResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppTagResponse.parse_obj(json)

class TerritoriesLinkagesOfAppTagEndpoint(IDEndpoint):
    path = '/v1/appTags/{id}/relationships/territories'

    def limit(self, number: int=None) -> TerritoriesLinkagesOfAppTagEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TerritoriesLinkagesOfAppTagEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppTagTerritoriesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppTagTerritoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppTagTerritoriesLinkagesResponse.parse_obj(json)

class TerritoriesOfAppTagEndpoint(IDEndpoint):
    path = '/v1/appTags/{id}/territories'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> TerritoriesOfAppTagEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.TerritoriesOfAppTagEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def limit(self, number: int=None) -> TerritoriesOfAppTagEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TerritoriesOfAppTagEndpoint
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

