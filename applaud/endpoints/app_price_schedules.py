from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppPriceSchedulesEndpoint(Endpoint):
    path = '/v1/appPriceSchedules'

    def create(self, request: AppPriceScheduleCreateRequest) -> AppPriceScheduleResponse:
        '''Create the resource.

        :param request: AppPriceSchedule representation
        :type request: AppPriceScheduleCreateRequest

        :returns: Single AppPriceSchedule
        :rtype: AppPriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppPriceScheduleResponse.parse_obj(json)

class AppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}'

    @endpoint('/v1/appPriceSchedules/{id}/automaticPrices')
    def automatic_prices(self) -> AutomaticPricesOfAppPriceScheduleEndpoint:
        return AutomaticPricesOfAppPriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/appPriceSchedules/{id}/baseTerritory')
    def base_territory(self) -> BaseTerritoryOfAppPriceScheduleEndpoint:
        return BaseTerritoryOfAppPriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/appPriceSchedules/{id}/manualPrices')
    def manual_prices(self) -> ManualPricesOfAppPriceScheduleEndpoint:
        return ManualPricesOfAppPriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/appPriceSchedules/{id}/relationships/automaticPrices')
    def automatic_prices_linkages(self) -> AutomaticPricesLinkagesOfAppPriceScheduleEndpoint:
        return AutomaticPricesLinkagesOfAppPriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/appPriceSchedules/{id}/relationships/baseTerritory')
    def base_territory_linkage(self) -> BaseTerritoryLinkageOfAppPriceScheduleEndpoint:
        return BaseTerritoryLinkageOfAppPriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/appPriceSchedules/{id}/relationships/manualPrices')
    def manual_prices_linkages(self) -> ManualPricesLinkagesOfAppPriceScheduleEndpoint:
        return ManualPricesLinkagesOfAppPriceScheduleEndpoint(self.id, self.session)
        
    def fields(self, *, app_price_schedule: Union[AppPriceScheduleField, list[AppPriceScheduleField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, app_price: Union[AppPriceField, list[AppPriceField]]=None) -> AppPriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param app_price_schedule: the fields to include for returned resources of type appPriceSchedules
        :type app_price_schedule: Union[AppPriceScheduleField, list[AppPriceScheduleField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceScheduleEndpoint
        '''
        if app_price_schedule: self._set_fields('appPriceSchedules',app_price_schedule if type(app_price_schedule) is list else [app_price_schedule])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BASE_TERRITORY = 'baseTerritory'
        MANUAL_PRICES = 'manualPrices'
        AUTOMATIC_PRICES = 'automaticPrices'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPriceScheduleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPriceScheduleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, automatic_prices: int=None, manual_prices: int=None) -> AppPriceScheduleEndpoint:
        '''Number of included related resources to return.

        :param automatic_prices: maximum number of related automaticPrices returned (when they are included). The maximum limit is 50
        :type automatic_prices: int = None

        :param manual_prices: maximum number of related manualPrices returned (when they are included). The maximum limit is 50
        :type manual_prices: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceScheduleEndpoint
        '''
        if automatic_prices and automatic_prices > 50:
            raise ValueError(f'The maximum limit of automatic_prices is 50')
        if automatic_prices: self._set_limit(automatic_prices, 'automaticPrices')

        if manual_prices and manual_prices > 50:
            raise ValueError(f'The maximum limit of manual_prices is 50')
        if manual_prices: self._set_limit(manual_prices, 'manualPrices')

        return self

    def get(self) -> AppPriceScheduleResponse:
        '''Get the resource.

        :returns: Single AppPriceSchedule
        :rtype: AppPriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceScheduleResponse.parse_obj(json)

class AutomaticPricesLinkagesOfAppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}/relationships/automaticPrices'

    def limit(self, number: int=None) -> AutomaticPricesLinkagesOfAppPriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesLinkagesOfAppPriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPriceScheduleAutomaticPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppPriceScheduleAutomaticPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceScheduleAutomaticPricesLinkagesResponse.parse_obj(json)

class AutomaticPricesOfAppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}/automaticPrices'

    def fields(self, *, app_price: Union[AppPriceField, list[AppPriceField]]=None, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AutomaticPricesOfAppPriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfAppPriceScheduleEndpoint
        '''
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        APP_PRICE_POINT = 'appPricePoint'
        TERRITORY = 'territory'

    def filter(self, *, start_date: Union[str, list[str]]=None, end_date: Union[str, list[str]]=None, territory: Union[str, list[str]]=None) -> AutomaticPricesOfAppPriceScheduleEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param start_date: filter by attribute 'startDate'
        :type start_date: Union[str, list[str]] = None

        :param end_date: filter by attribute 'endDate'
        :type end_date: Union[str, list[str]] = None

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfAppPriceScheduleEndpoint
        '''
        if start_date: self._set_filter('startDate', start_date if type(start_date) is list else [start_date])
        
        if end_date: self._set_filter('endDate', end_date if type(end_date) is list else [end_date])
        
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AutomaticPricesOfAppPriceScheduleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfAppPriceScheduleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AutomaticPricesOfAppPriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfAppPriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPricesV2Response:
        '''Get one or more resources.

        :returns: List of AppPrices
        :rtype: AppPricesV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricesV2Response.parse_obj(json)

class BaseTerritoryLinkageOfAppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}/relationships/baseTerritory'

    def get(self) -> AppPriceScheduleBaseTerritoryLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppPriceScheduleBaseTerritoryLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceScheduleBaseTerritoryLinkageResponse.parse_obj(json)

class BaseTerritoryOfAppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}/baseTerritory'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> BaseTerritoryOfAppPriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.BaseTerritoryOfAppPriceScheduleEndpoint
        '''
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    def get(self) -> TerritoryResponse:
        '''Get the resource.

        :returns: Single Territory
        :rtype: TerritoryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return TerritoryResponse.parse_obj(json)

class ManualPricesLinkagesOfAppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}/relationships/manualPrices'

    def limit(self, number: int=None) -> ManualPricesLinkagesOfAppPriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesLinkagesOfAppPriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPriceScheduleManualPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppPriceScheduleManualPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceScheduleManualPricesLinkagesResponse.parse_obj(json)

class ManualPricesOfAppPriceScheduleEndpoint(IDEndpoint):
    path = '/v1/appPriceSchedules/{id}/manualPrices'

    def fields(self, *, app_price: Union[AppPriceField, list[AppPriceField]]=None, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> ManualPricesOfAppPriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfAppPriceScheduleEndpoint
        '''
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        APP_PRICE_POINT = 'appPricePoint'
        TERRITORY = 'territory'

    def filter(self, *, start_date: Union[str, list[str]]=None, end_date: Union[str, list[str]]=None, territory: Union[str, list[str]]=None) -> ManualPricesOfAppPriceScheduleEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param start_date: filter by attribute 'startDate'
        :type start_date: Union[str, list[str]] = None

        :param end_date: filter by attribute 'endDate'
        :type end_date: Union[str, list[str]] = None

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfAppPriceScheduleEndpoint
        '''
        if start_date: self._set_filter('startDate', start_date if type(start_date) is list else [start_date])
        
        if end_date: self._set_filter('endDate', end_date if type(end_date) is list else [end_date])
        
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ManualPricesOfAppPriceScheduleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfAppPriceScheduleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ManualPricesOfAppPriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfAppPriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPricesV2Response:
        '''Get one or more resources.

        :returns: List of AppPrices
        :rtype: AppPricesV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricesV2Response.parse_obj(json)

