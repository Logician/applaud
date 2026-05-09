from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionOfferCodesEndpoint(Endpoint):
    path = '/v1/subscriptionOfferCodes'

    def create(self, request: SubscriptionOfferCodeCreateRequest) -> SubscriptionOfferCodeResponse:
        '''Create the resource.

        :param request: SubscriptionOfferCode representation
        :type request: SubscriptionOfferCodeCreateRequest

        :returns: Single SubscriptionOfferCode
        :rtype: SubscriptionOfferCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionOfferCodeResponse.parse_obj(json)

class SubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}'

    @endpoint('/v1/subscriptionOfferCodes/{id}/customCodes')
    def custom_codes(self) -> CustomCodesOfSubscriptionOfferCodeEndpoint:
        return CustomCodesOfSubscriptionOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionOfferCodes/{id}/oneTimeUseCodes')
    def one_time_use_codes(self) -> OneTimeUseCodesOfSubscriptionOfferCodeEndpoint:
        return OneTimeUseCodesOfSubscriptionOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionOfferCodes/{id}/prices')
    def prices(self) -> PricesOfSubscriptionOfferCodeEndpoint:
        return PricesOfSubscriptionOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionOfferCodes/{id}/relationships/customCodes')
    def custom_codes_linkages(self) -> CustomCodesLinkagesOfSubscriptionOfferCodeEndpoint:
        return CustomCodesLinkagesOfSubscriptionOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionOfferCodes/{id}/relationships/oneTimeUseCodes')
    def one_time_use_codes_linkages(self) -> OneTimeUseCodesLinkagesOfSubscriptionOfferCodeEndpoint:
        return OneTimeUseCodesLinkagesOfSubscriptionOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionOfferCodes/{id}/relationships/prices')
    def prices_linkages(self) -> PricesLinkagesOfSubscriptionOfferCodeEndpoint:
        return PricesLinkagesOfSubscriptionOfferCodeEndpoint(self.id, self.session)
        
    def fields(self, *, subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]]=None, subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]]=None, subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]]=None, subscription_offer_code_price: Union[SubscriptionOfferCodePriceField, list[SubscriptionOfferCodePriceField]]=None) -> SubscriptionOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code: the fields to include for returned resources of type subscriptionOfferCodes
        :type subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]] = None

        :param subscription_offer_code_one_time_use_code: the fields to include for returned resources of type subscriptionOfferCodeOneTimeUseCodes
        :type subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]] = None

        :param subscription_offer_code_custom_code: the fields to include for returned resources of type subscriptionOfferCodeCustomCodes
        :type subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]] = None

        :param subscription_offer_code_price: the fields to include for returned resources of type subscriptionOfferCodePrices
        :type subscription_offer_code_price: Union[SubscriptionOfferCodePriceField, list[SubscriptionOfferCodePriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeEndpoint
        '''
        if subscription_offer_code: self._set_fields('subscriptionOfferCodes',subscription_offer_code if type(subscription_offer_code) is list else [subscription_offer_code])
        if subscription_offer_code_one_time_use_code: self._set_fields('subscriptionOfferCodeOneTimeUseCodes',subscription_offer_code_one_time_use_code if type(subscription_offer_code_one_time_use_code) is list else [subscription_offer_code_one_time_use_code])
        if subscription_offer_code_custom_code: self._set_fields('subscriptionOfferCodeCustomCodes',subscription_offer_code_custom_code if type(subscription_offer_code_custom_code) is list else [subscription_offer_code_custom_code])
        if subscription_offer_code_price: self._set_fields('subscriptionOfferCodePrices',subscription_offer_code_price if type(subscription_offer_code_price) is list else [subscription_offer_code_price])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'
        ONE_TIME_USE_CODES = 'oneTimeUseCodes'
        CUSTOM_CODES = 'customCodes'
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, custom_codes: int=None, one_time_use_codes: int=None, prices: int=None) -> SubscriptionOfferCodeEndpoint:
        '''Number of included related resources to return.

        :param custom_codes: maximum number of related customCodes returned (when they are included). The maximum limit is 50
        :type custom_codes: int = None

        :param one_time_use_codes: maximum number of related oneTimeUseCodes returned (when they are included). The maximum limit is 50
        :type one_time_use_codes: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeEndpoint
        '''
        if custom_codes and custom_codes > 50:
            raise ValueError(f'The maximum limit of custom_codes is 50')
        if custom_codes: self._set_limit(custom_codes, 'customCodes')

        if one_time_use_codes and one_time_use_codes > 50:
            raise ValueError(f'The maximum limit of one_time_use_codes is 50')
        if one_time_use_codes: self._set_limit(one_time_use_codes, 'oneTimeUseCodes')

        if prices and prices > 50:
            raise ValueError(f'The maximum limit of prices is 50')
        if prices: self._set_limit(prices, 'prices')

        return self

    def get(self) -> SubscriptionOfferCodeResponse:
        '''Get the resource.

        :returns: Single SubscriptionOfferCode
        :rtype: SubscriptionOfferCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeResponse.parse_obj(json)

    def update(self, request: SubscriptionOfferCodeUpdateRequest) -> SubscriptionOfferCodeResponse:
        '''Modify the resource.

        :param request: SubscriptionOfferCode representation
        :type request: SubscriptionOfferCodeUpdateRequest

        :returns: Single SubscriptionOfferCode
        :rtype: SubscriptionOfferCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionOfferCodeResponse.parse_obj(json)

class CustomCodesLinkagesOfSubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}/relationships/customCodes'

    def limit(self, number: int=None) -> CustomCodesLinkagesOfSubscriptionOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomCodesLinkagesOfSubscriptionOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodeCustomCodesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionOfferCodeCustomCodesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeCustomCodesLinkagesResponse.parse_obj(json)

class CustomCodesOfSubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}/customCodes'

    def fields(self, *, subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]]=None, subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]]=None) -> CustomCodesOfSubscriptionOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code_custom_code: the fields to include for returned resources of type subscriptionOfferCodeCustomCodes
        :type subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]] = None

        :param subscription_offer_code: the fields to include for returned resources of type subscriptionOfferCodes
        :type subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomCodesOfSubscriptionOfferCodeEndpoint
        '''
        if subscription_offer_code_custom_code: self._set_fields('subscriptionOfferCodeCustomCodes',subscription_offer_code_custom_code if type(subscription_offer_code_custom_code) is list else [subscription_offer_code_custom_code])
        if subscription_offer_code: self._set_fields('subscriptionOfferCodes',subscription_offer_code if type(subscription_offer_code) is list else [subscription_offer_code])
        return self
        
    class Include(StringEnum):
        OFFER_CODE = 'offerCode'

    def include(self, relationship: Union[Include, list[Include]]) -> CustomCodesOfSubscriptionOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomCodesOfSubscriptionOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> CustomCodesOfSubscriptionOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomCodesOfSubscriptionOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodeCustomCodesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionOfferCodeCustomCodes
        :rtype: SubscriptionOfferCodeCustomCodesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeCustomCodesResponse.parse_obj(json)

class OneTimeUseCodesLinkagesOfSubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}/relationships/oneTimeUseCodes'

    def limit(self, number: int=None) -> OneTimeUseCodesLinkagesOfSubscriptionOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesLinkagesOfSubscriptionOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodeOneTimeUseCodesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionOfferCodeOneTimeUseCodesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeOneTimeUseCodesLinkagesResponse.parse_obj(json)

class OneTimeUseCodesOfSubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}/oneTimeUseCodes'

    def fields(self, *, subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]]=None, subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]]=None) -> OneTimeUseCodesOfSubscriptionOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code_one_time_use_code: the fields to include for returned resources of type subscriptionOfferCodeOneTimeUseCodes
        :type subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]] = None

        :param subscription_offer_code: the fields to include for returned resources of type subscriptionOfferCodes
        :type subscription_offer_code: Union[SubscriptionOfferCodeField, list[SubscriptionOfferCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesOfSubscriptionOfferCodeEndpoint
        '''
        if subscription_offer_code_one_time_use_code: self._set_fields('subscriptionOfferCodeOneTimeUseCodes',subscription_offer_code_one_time_use_code if type(subscription_offer_code_one_time_use_code) is list else [subscription_offer_code_one_time_use_code])
        if subscription_offer_code: self._set_fields('subscriptionOfferCodes',subscription_offer_code if type(subscription_offer_code) is list else [subscription_offer_code])
        return self
        
    class Include(StringEnum):
        OFFER_CODE = 'offerCode'

    def include(self, relationship: Union[Include, list[Include]]) -> OneTimeUseCodesOfSubscriptionOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesOfSubscriptionOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> OneTimeUseCodesOfSubscriptionOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesOfSubscriptionOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodeOneTimeUseCodesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionOfferCodeOneTimeUseCodes
        :rtype: SubscriptionOfferCodeOneTimeUseCodesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeOneTimeUseCodesResponse.parse_obj(json)

class PricesLinkagesOfSubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}/relationships/prices'

    def limit(self, number: int=None) -> PricesLinkagesOfSubscriptionOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesLinkagesOfSubscriptionOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodePricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionOfferCodePricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodePricesLinkagesResponse.parse_obj(json)

class PricesOfSubscriptionOfferCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodes/{id}/prices'

    def fields(self, *, subscription_offer_code_price: Union[SubscriptionOfferCodePriceField, list[SubscriptionOfferCodePriceField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None) -> PricesOfSubscriptionOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code_price: the fields to include for returned resources of type subscriptionOfferCodePrices
        :type subscription_offer_code_price: Union[SubscriptionOfferCodePriceField, list[SubscriptionOfferCodePriceField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionOfferCodeEndpoint
        '''
        if subscription_offer_code_price: self._set_fields('subscriptionOfferCodePrices',subscription_offer_code_price if type(subscription_offer_code_price) is list else [subscription_offer_code_price])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'
        SUBSCRIPTION_PRICE_POINT = 'subscriptionPricePoint'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PricesOfSubscriptionOfferCodeEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionOfferCodeEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricesOfSubscriptionOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricesOfSubscriptionOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfSubscriptionOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionOfferCodePricesResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionOfferCodePrices
        :rtype: SubscriptionOfferCodePricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodePricesResponse.parse_obj(json)

