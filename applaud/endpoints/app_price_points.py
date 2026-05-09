from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPricePointEndpoint(IDEndpoint):
    path = '/v3/appPricePoints/{id}'

    @endpoint('/v3/appPricePoints/{id}/equalizations')
    def equalizations(self) -> EqualizationsOfAppPricePointEndpoint:
        return EqualizationsOfAppPricePointEndpoint(self.id, self.session)
        
    @endpoint('/v3/appPricePoints/{id}/relationships/equalizations')
    def equalizations_linkages(self) -> EqualizationsLinkagesOfAppPricePointEndpoint:
        return EqualizationsLinkagesOfAppPricePointEndpoint(self.id, self.session)
        
    def fields(self, *, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None) -> AppPricePointEndpoint:
        '''Fields to return for included related types.

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointEndpoint
        '''
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        TERRITORY = 'territory'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPricePointEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPricePointEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppPricePointV3Response:
        '''Get the resource.

        :returns: Single AppPricePoint
        :rtype: AppPricePointV3Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointV3Response.parse_obj(json)

class EqualizationsLinkagesOfAppPricePointEndpoint(IDEndpoint):
    path = '/v3/appPricePoints/{id}/relationships/equalizations'

    def limit(self, number: int=None) -> EqualizationsLinkagesOfAppPricePointEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsLinkagesOfAppPricePointEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPricePointV3EqualizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppPricePointV3EqualizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointV3EqualizationsLinkagesResponse.parse_obj(json)

class EqualizationsOfAppPricePointEndpoint(IDEndpoint):
    path = '/v3/appPricePoints/{id}/equalizations'

    def fields(self, *, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None, app: Union[AppField, list[AppField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> EqualizationsOfAppPricePointEndpoint:
        '''Fields to return for included related types.

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfAppPricePointEndpoint
        '''
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None) -> EqualizationsOfAppPricePointEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfAppPricePointEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> EqualizationsOfAppPricePointEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfAppPricePointEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> EqualizationsOfAppPricePointEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfAppPricePointEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPricePointsV3Response:
        '''Get one or more resources.

        :returns: List of AppPricePoints
        :rtype: AppPricePointsV3Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointsV3Response.parse_obj(json)

