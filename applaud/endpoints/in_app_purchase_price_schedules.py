from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchasePriceSchedulesEndpoint(Endpoint):
    path = '/v1/inAppPurchasePriceSchedules'

    def create(self, request: InAppPurchasePriceScheduleCreateRequest) -> InAppPurchasePriceScheduleResponse:
        '''Create the resource.

        :param request: InAppPurchasePriceSchedule representation
        :type request: InAppPurchasePriceScheduleCreateRequest

        :returns: Single InAppPurchasePriceSchedule
        :rtype: InAppPurchasePriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchasePriceScheduleResponse.parse_obj(json)

class InAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}'

    @endpoint('/v1/inAppPurchasePriceSchedules/{id}/automaticPrices')
    def automatic_prices(self) -> AutomaticPricesOfInAppPurchasePriceScheduleEndpoint:
        return AutomaticPricesOfInAppPurchasePriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchasePriceSchedules/{id}/baseTerritory')
    def base_territory(self) -> BaseTerritoryOfInAppPurchasePriceScheduleEndpoint:
        return BaseTerritoryOfInAppPurchasePriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchasePriceSchedules/{id}/manualPrices')
    def manual_prices(self) -> ManualPricesOfInAppPurchasePriceScheduleEndpoint:
        return ManualPricesOfInAppPurchasePriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchasePriceSchedules/{id}/relationships/automaticPrices')
    def automatic_prices_linkages(self) -> AutomaticPricesLinkagesOfInAppPurchasePriceScheduleEndpoint:
        return AutomaticPricesLinkagesOfInAppPurchasePriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchasePriceSchedules/{id}/relationships/baseTerritory')
    def base_territory_linkage(self) -> BaseTerritoryLinkageOfInAppPurchasePriceScheduleEndpoint:
        return BaseTerritoryLinkageOfInAppPurchasePriceScheduleEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchasePriceSchedules/{id}/relationships/manualPrices')
    def manual_prices_linkages(self) -> ManualPricesLinkagesOfInAppPurchasePriceScheduleEndpoint:
        return ManualPricesLinkagesOfInAppPurchasePriceScheduleEndpoint(self.id, self.session)
        
    def fields(self, *, in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]]=None) -> InAppPurchasePriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_price_schedule: the fields to include for returned resources of type inAppPurchasePriceSchedules
        :type in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param in_app_purchase_price: the fields to include for returned resources of type inAppPurchasePrices
        :type in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasePriceScheduleEndpoint
        '''
        if in_app_purchase_price_schedule: self._set_fields('inAppPurchasePriceSchedules',in_app_purchase_price_schedule if type(in_app_purchase_price_schedule) is list else [in_app_purchase_price_schedule])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if in_app_purchase_price: self._set_fields('inAppPurchasePrices',in_app_purchase_price if type(in_app_purchase_price) is list else [in_app_purchase_price])
        return self
        
    class Include(StringEnum):
        BASE_TERRITORY = 'baseTerritory'
        MANUAL_PRICES = 'manualPrices'
        AUTOMATIC_PRICES = 'automaticPrices'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchasePriceScheduleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasePriceScheduleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, automatic_prices: int=None, manual_prices: int=None) -> InAppPurchasePriceScheduleEndpoint:
        '''Number of included related resources to return.

        :param automatic_prices: maximum number of related automaticPrices returned (when they are included). The maximum limit is 50
        :type automatic_prices: int = None

        :param manual_prices: maximum number of related manualPrices returned (when they are included). The maximum limit is 50
        :type manual_prices: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasePriceScheduleEndpoint
        '''
        if automatic_prices and automatic_prices > 50:
            raise ValueError(f'The maximum limit of automatic_prices is 50')
        if automatic_prices: self._set_limit(automatic_prices, 'automaticPrices')

        if manual_prices and manual_prices > 50:
            raise ValueError(f'The maximum limit of manual_prices is 50')
        if manual_prices: self._set_limit(manual_prices, 'manualPrices')

        return self

    def get(self) -> InAppPurchasePriceScheduleResponse:
        '''Get the resource.

        :returns: Single InAppPurchasePriceSchedule
        :rtype: InAppPurchasePriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePriceScheduleResponse.parse_obj(json)

class AutomaticPricesLinkagesOfInAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}/relationships/automaticPrices'

    def limit(self, number: int=None) -> AutomaticPricesLinkagesOfInAppPurchasePriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesLinkagesOfInAppPurchasePriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePriceScheduleAutomaticPricesLinkagesResponse.parse_obj(json)

class AutomaticPricesOfInAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}/automaticPrices'

    def fields(self, *, in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]]=None, in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AutomaticPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_price: the fields to include for returned resources of type inAppPurchasePrices
        :type in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]] = None

        :param in_app_purchase_price_point: the fields to include for returned resources of type inAppPurchasePricePoints
        :type in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if in_app_purchase_price: self._set_fields('inAppPurchasePrices',in_app_purchase_price if type(in_app_purchase_price) is list else [in_app_purchase_price])
        if in_app_purchase_price_point: self._set_fields('inAppPurchasePricePoints',in_app_purchase_price_point if type(in_app_purchase_price_point) is list else [in_app_purchase_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_PRICE_POINT = 'inAppPurchasePricePoint'
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None) -> AutomaticPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AutomaticPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AutomaticPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AutomaticPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePricesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchasePrices
        :rtype: InAppPurchasePricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePricesResponse.parse_obj(json)

class BaseTerritoryLinkageOfInAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}/relationships/baseTerritory'

    def get(self) -> InAppPurchasePriceScheduleBaseTerritoryLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: InAppPurchasePriceScheduleBaseTerritoryLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePriceScheduleBaseTerritoryLinkageResponse.parse_obj(json)

class BaseTerritoryOfInAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}/baseTerritory'

    def fields(self, *, territory: Union[TerritoryField, list[TerritoryField]]=None) -> BaseTerritoryOfInAppPurchasePriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.BaseTerritoryOfInAppPurchasePriceScheduleEndpoint
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

class ManualPricesLinkagesOfInAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}/relationships/manualPrices'

    def limit(self, number: int=None) -> ManualPricesLinkagesOfInAppPurchasePriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesLinkagesOfInAppPurchasePriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePriceScheduleManualPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchasePriceScheduleManualPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePriceScheduleManualPricesLinkagesResponse.parse_obj(json)

class ManualPricesOfInAppPurchasePriceScheduleEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePriceSchedules/{id}/manualPrices'

    def fields(self, *, in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]]=None, in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> ManualPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_price: the fields to include for returned resources of type inAppPurchasePrices
        :type in_app_purchase_price: Union[InAppPurchasePriceField, list[InAppPurchasePriceField]] = None

        :param in_app_purchase_price_point: the fields to include for returned resources of type inAppPurchasePricePoints
        :type in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if in_app_purchase_price: self._set_fields('inAppPurchasePrices',in_app_purchase_price if type(in_app_purchase_price) is list else [in_app_purchase_price])
        if in_app_purchase_price_point: self._set_fields('inAppPurchasePricePoints',in_app_purchase_price_point if type(in_app_purchase_price_point) is list else [in_app_purchase_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_PRICE_POINT = 'inAppPurchasePricePoint'
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None) -> ManualPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ManualPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ManualPricesOfInAppPurchasePriceScheduleEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ManualPricesOfInAppPurchasePriceScheduleEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePricesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchasePrices
        :rtype: InAppPurchasePricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePricesResponse.parse_obj(json)

