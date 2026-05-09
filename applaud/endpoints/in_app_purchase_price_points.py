from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class EqualizationsLinkagesOfInAppPurchasePricePointEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePricePoints/{id}/relationships/equalizations'

    def limit(self, number: int=None) -> EqualizationsLinkagesOfInAppPurchasePricePointEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsLinkagesOfInAppPurchasePricePointEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePricePointEqualizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchasePricePointEqualizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePricePointEqualizationsLinkagesResponse.parse_obj(json)

class EqualizationsOfInAppPurchasePricePointEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePricePoints/{id}/equalizations'

    def fields(self, *, in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> EqualizationsOfInAppPurchasePricePointEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_price_point: the fields to include for returned resources of type inAppPurchasePricePoints
        :type in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfInAppPurchasePricePointEndpoint
        '''
        if in_app_purchase_price_point: self._set_fields('inAppPurchasePricePoints',in_app_purchase_price_point if type(in_app_purchase_price_point) is list else [in_app_purchase_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None, in_app_purchase_v2: Union[str, list[str]]=None) -> EqualizationsOfInAppPurchasePricePointEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :param in_app_purchase_v2: filter by id(s) of related 'inAppPurchaseV2'
        :type in_app_purchase_v2: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfInAppPurchasePricePointEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        if in_app_purchase_v2: self._set_filter('inAppPurchaseV2', in_app_purchase_v2 if type(in_app_purchase_v2) is list else [in_app_purchase_v2])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> EqualizationsOfInAppPurchasePricePointEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfInAppPurchasePricePointEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> EqualizationsOfInAppPurchasePricePointEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfInAppPurchasePricePointEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchasePricePointsResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchasePricePoints
        :rtype: InAppPurchasePricePointsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasePricePointsResponse.parse_obj(json)

class InAppPurchasePricePointEndpoint(IDEndpoint):
    path = '/v1/inAppPurchasePricePoints/{id}'

    @endpoint('/v1/inAppPurchasePricePoints/{id}/equalizations')
    def equalizations(self) -> EqualizationsOfInAppPurchasePricePointEndpoint:
        return EqualizationsOfInAppPurchasePricePointEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchasePricePoints/{id}/relationships/equalizations')
    def equalizations_linkages(self) -> EqualizationsLinkagesOfInAppPurchasePricePointEndpoint:
        return EqualizationsLinkagesOfInAppPurchasePricePointEndpoint(self.id, self.session)
        
