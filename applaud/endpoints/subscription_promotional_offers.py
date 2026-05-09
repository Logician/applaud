from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionPromotionalOffersEndpoint(Endpoint):
    path = '/v1/subscriptionPromotionalOffers'

    def create(self, request: SubscriptionPromotionalOfferCreateRequest) -> SubscriptionPromotionalOfferResponse:
        '''Create the resource.

        :param request: SubscriptionPromotionalOffer representation
        :type request: SubscriptionPromotionalOfferCreateRequest

        :returns: Single SubscriptionPromotionalOffer
        :rtype: SubscriptionPromotionalOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionPromotionalOfferResponse.parse_obj(json)

class SubscriptionPromotionalOfferEndpoint(IDEndpoint):
    path = '/v1/subscriptionPromotionalOffers/{id}'

    @endpoint('/v1/subscriptionPromotionalOffers/{id}/prices')
    def prices(self) -> PricesOfSubscriptionPromotionalOfferEndpoint:
        return PricesOfSubscriptionPromotionalOfferEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionPromotionalOffers/{id}/relationships/prices')
    def prices_linkages(self) -> PricesLinkagesOfSubscriptionPromotionalOfferEndpoint:
        return PricesLinkagesOfSubscriptionPromotionalOfferEndpoint(self.id, self.session)
        
    def fields(self, *, subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]]=None, subscription_promotional_offer_price: Union[SubscriptionPromotionalOfferPriceField, list[SubscriptionPromotionalOfferPriceField]]=None) -> SubscriptionPromotionalOfferEndpoint:
        '''Fields to return for included related types.

        :param subscription_promotional_offer: the fields to include for returned resources of type subscriptionPromotionalOffers
        :type subscription_promotional_offer: Union[SubscriptionPromotionalOfferField, list[SubscriptionPromotionalOfferField]] = None

        :param subscription_promotional_offer_price: the fields to include for returned resources of type subscriptionPromotionalOfferPrices
        :type subscription_promotional_offer_price: Union[SubscriptionPromotionalOfferPriceField, list[SubscriptionPromotionalOfferPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionPromotionalOfferEndpoint
        '''
        if subscription_promotional_offer: self._set_fields('subscriptionPromotionalOffers',subscription_promotional_offer if type(subscription_promotional_offer) is list else [subscription_promotional_offer])
        if subscription_promotional_offer_price: self._set_fields('subscriptionPromotionalOfferPrices',subscription_promotional_offer_price if type(subscription_promotional_offer_price) is list else [subscription_promotional_offer_price])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionPromotionalOfferEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionPromotionalOfferEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, prices: int=None) -> SubscriptionPromotionalOfferEndpoint:
        '''Number of included related resources to return.

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionPromotionalOfferEndpoint
        '''
        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        return self

    def get(self) -> SubscriptionPromotionalOfferResponse:
        '''Get the resource.

        :returns: Single SubscriptionPromotionalOffer
        :rtype: SubscriptionPromotionalOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPromotionalOfferResponse.parse_obj(json)

    def update(self, request: SubscriptionPromotionalOfferUpdateRequest) -> SubscriptionPromotionalOfferResponse:
        '''Modify the resource.

        :param request: SubscriptionPromotionalOffer representation
        :type request: SubscriptionPromotionalOfferUpdateRequest

        :returns: Single SubscriptionPromotionalOffer
        :rtype: SubscriptionPromotionalOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionPromotionalOfferResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class PricesLinkagesOfSubscriptionPromotionalOfferEndpoint(IDEndpoint):
    path = '/v1/subscriptionPromotionalOffers/{id}/relationships/prices'

    def limit(self, number: int=None) -> PricesLinkagesOfSubscriptionPromotionalOfferEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesLinkagesOfSubscriptionPromotionalOfferEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPromotionalOfferPricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionPromotionalOfferPricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPromotionalOfferPricesLinkagesResponse.parse_obj(json)

class PricesOfSubscriptionPromotionalOfferEndpoint(IDEndpoint):
    path = '/v1/subscriptionPromotionalOffers/{id}/prices'

    def fields(self, *, subscription_promotional_offer_price: Union[SubscriptionPromotionalOfferPriceField, list[SubscriptionPromotionalOfferPriceField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None) -> PricesOfSubscriptionPromotionalOfferEndpoint:
        '''Fields to return for included related types.

        :param subscription_promotional_offer_price: the fields to include for returned resources of type subscriptionPromotionalOfferPrices
        :type subscription_promotional_offer_price: Union[SubscriptionPromotionalOfferPriceField, list[SubscriptionPromotionalOfferPriceField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionPromotionalOfferEndpoint
        '''
        if subscription_promotional_offer_price: self._set_fields('subscriptionPromotionalOfferPrices',subscription_promotional_offer_price if type(subscription_promotional_offer_price) is list else [subscription_promotional_offer_price])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'
        SUBSCRIPTION_PRICE_POINT = 'subscriptionPricePoint'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PricesOfSubscriptionPromotionalOfferEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionPromotionalOfferEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricesOfSubscriptionPromotionalOfferEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionPromotionalOfferEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricesOfSubscriptionPromotionalOfferEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionPromotionalOfferEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPromotionalOfferPricesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionPromotionalOfferPrices
        :rtype: SubscriptionPromotionalOfferPricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPromotionalOfferPricesResponse.parse_obj(json)

