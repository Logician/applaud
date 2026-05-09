from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class WinBackOffersEndpoint(Endpoint):
    path = '/v1/winBackOffers'

    def create(self, request: WinBackOfferCreateRequest) -> WinBackOfferResponse:
        '''Create the resource.

        :param request: WinBackOffer representation
        :type request: WinBackOfferCreateRequest

        :returns: Single WinBackOffer
        :rtype: WinBackOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return WinBackOfferResponse.parse_obj(json)

class WinBackOfferEndpoint(IDEndpoint):
    path = '/v1/winBackOffers/{id}'

    @endpoint('/v1/winBackOffers/{id}/prices')
    def prices(self) -> PricesOfWinBackOfferEndpoint:
        return PricesOfWinBackOfferEndpoint(self.id, self.session)
        
    @endpoint('/v1/winBackOffers/{id}/relationships/prices')
    def prices_linkages(self) -> PricesLinkagesOfWinBackOfferEndpoint:
        return PricesLinkagesOfWinBackOfferEndpoint(self.id, self.session)
        
    def fields(self, *, win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]]=None, win_back_offer_price: Union[WinBackOfferPriceField, list[WinBackOfferPriceField]]=None) -> WinBackOfferEndpoint:
        '''Fields to return for included related types.

        :param win_back_offer: the fields to include for returned resources of type winBackOffers
        :type win_back_offer: Union[WinBackOfferField, list[WinBackOfferField]] = None

        :param win_back_offer_price: the fields to include for returned resources of type winBackOfferPrices
        :type win_back_offer_price: Union[WinBackOfferPriceField, list[WinBackOfferPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.WinBackOfferEndpoint
        '''
        if win_back_offer: self._set_fields('winBackOffers',win_back_offer if type(win_back_offer) is list else [win_back_offer])
        if win_back_offer_price: self._set_fields('winBackOfferPrices',win_back_offer_price if type(win_back_offer_price) is list else [win_back_offer_price])
        return self
        
    class Include(StringEnum):
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> WinBackOfferEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.WinBackOfferEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, prices: int=None) -> WinBackOfferEndpoint:
        '''Number of included related resources to return.

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.WinBackOfferEndpoint
        '''
        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        return self

    def get(self) -> WinBackOfferResponse:
        '''Get the resource.

        :returns: Single WinBackOffer
        :rtype: WinBackOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WinBackOfferResponse.parse_obj(json)

    def update(self, request: WinBackOfferUpdateRequest) -> WinBackOfferResponse:
        '''Modify the resource.

        :param request: WinBackOffer representation
        :type request: WinBackOfferUpdateRequest

        :returns: Single WinBackOffer
        :rtype: WinBackOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return WinBackOfferResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class PricesLinkagesOfWinBackOfferEndpoint(IDEndpoint):
    path = '/v1/winBackOffers/{id}/relationships/prices'

    def limit(self, number: int=None) -> PricesLinkagesOfWinBackOfferEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesLinkagesOfWinBackOfferEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> WinBackOfferPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: WinBackOfferPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WinBackOfferPricesLinkagesResponse.parse_obj(json)

class PricesOfWinBackOfferEndpoint(IDEndpoint):
    path = '/v1/winBackOffers/{id}/prices'

    def fields(self, *, win_back_offer_price: Union[WinBackOfferPriceField, list[WinBackOfferPriceField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None) -> PricesOfWinBackOfferEndpoint:
        '''Fields to return for included related types.

        :param win_back_offer_price: the fields to include for returned resources of type winBackOfferPrices
        :type win_back_offer_price: Union[WinBackOfferPriceField, list[WinBackOfferPriceField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfWinBackOfferEndpoint
        '''
        if win_back_offer_price: self._set_fields('winBackOfferPrices',win_back_offer_price if type(win_back_offer_price) is list else [win_back_offer_price])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'
        SUBSCRIPTION_PRICE_POINT = 'subscriptionPricePoint'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PricesOfWinBackOfferEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfWinBackOfferEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricesOfWinBackOfferEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricesOfWinBackOfferEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricesOfWinBackOfferEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfWinBackOfferEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> WinBackOfferPricesResponse:
        '''Get one or more resources.

        :returns: List of WinBackOfferPrices
        :rtype: WinBackOfferPricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WinBackOfferPricesResponse.parse_obj(json)

