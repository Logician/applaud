from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseOfferCodesEndpoint(Endpoint):
    path = '/v1/inAppPurchaseOfferCodes'

    def create(self, request: InAppPurchaseOfferCodeCreateRequest) -> InAppPurchaseOfferCodeResponse:
        '''Create the resource.

        :param request: InAppPurchaseOfferCode representation
        :type request: InAppPurchaseOfferCodeCreateRequest

        :returns: Single InAppPurchaseOfferCode
        :rtype: InAppPurchaseOfferCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseOfferCodeResponse.parse_obj(json)

class InAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}'

    @endpoint('/v1/inAppPurchaseOfferCodes/{id}/customCodes')
    def custom_codes(self) -> CustomCodesOfInAppPurchaseOfferCodeEndpoint:
        return CustomCodesOfInAppPurchaseOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchaseOfferCodes/{id}/oneTimeUseCodes')
    def one_time_use_codes(self) -> OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint:
        return OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchaseOfferCodes/{id}/prices')
    def prices(self) -> PricesOfInAppPurchaseOfferCodeEndpoint:
        return PricesOfInAppPurchaseOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchaseOfferCodes/{id}/relationships/customCodes')
    def custom_codes_linkages(self) -> CustomCodesLinkagesOfInAppPurchaseOfferCodeEndpoint:
        return CustomCodesLinkagesOfInAppPurchaseOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchaseOfferCodes/{id}/relationships/oneTimeUseCodes')
    def one_time_use_codes_linkages(self) -> OneTimeUseCodesLinkagesOfInAppPurchaseOfferCodeEndpoint:
        return OneTimeUseCodesLinkagesOfInAppPurchaseOfferCodeEndpoint(self.id, self.session)
        
    @endpoint('/v1/inAppPurchaseOfferCodes/{id}/relationships/prices')
    def prices_linkages(self) -> PricesLinkagesOfInAppPurchaseOfferCodeEndpoint:
        return PricesLinkagesOfInAppPurchaseOfferCodeEndpoint(self.id, self.session)
        
    def fields(self, *, in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]]=None, in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]]=None, in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]]=None, in_app_purchase_offer_price: Union[InAppPurchaseOfferPriceField, list[InAppPurchaseOfferPriceField]]=None) -> InAppPurchaseOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_code: the fields to include for returned resources of type inAppPurchaseOfferCodes
        :type in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]] = None

        :param in_app_purchase_offer_code_one_time_use_code: the fields to include for returned resources of type inAppPurchaseOfferCodeOneTimeUseCodes
        :type in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]] = None

        :param in_app_purchase_offer_code_custom_code: the fields to include for returned resources of type inAppPurchaseOfferCodeCustomCodes
        :type in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]] = None

        :param in_app_purchase_offer_price: the fields to include for returned resources of type inAppPurchaseOfferPrices
        :type in_app_purchase_offer_price: Union[InAppPurchaseOfferPriceField, list[InAppPurchaseOfferPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeEndpoint
        '''
        if in_app_purchase_offer_code: self._set_fields('inAppPurchaseOfferCodes',in_app_purchase_offer_code if type(in_app_purchase_offer_code) is list else [in_app_purchase_offer_code])
        if in_app_purchase_offer_code_one_time_use_code: self._set_fields('inAppPurchaseOfferCodeOneTimeUseCodes',in_app_purchase_offer_code_one_time_use_code if type(in_app_purchase_offer_code_one_time_use_code) is list else [in_app_purchase_offer_code_one_time_use_code])
        if in_app_purchase_offer_code_custom_code: self._set_fields('inAppPurchaseOfferCodeCustomCodes',in_app_purchase_offer_code_custom_code if type(in_app_purchase_offer_code_custom_code) is list else [in_app_purchase_offer_code_custom_code])
        if in_app_purchase_offer_price: self._set_fields('inAppPurchaseOfferPrices',in_app_purchase_offer_price if type(in_app_purchase_offer_price) is list else [in_app_purchase_offer_price])
        return self
        
    class Include(StringEnum):
        ONE_TIME_USE_CODES = 'oneTimeUseCodes'
        CUSTOM_CODES = 'customCodes'
        PRICES = 'prices'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, custom_codes: int=None, one_time_use_codes: int=None, prices: int=None) -> InAppPurchaseOfferCodeEndpoint:
        '''Number of included related resources to return.

        :param custom_codes: maximum number of related customCodes returned (when they are included). The maximum limit is 50
        :type custom_codes: int = None

        :param one_time_use_codes: maximum number of related oneTimeUseCodes returned (when they are included). The maximum limit is 50
        :type one_time_use_codes: int = None

        :param prices: maximum number of related prices returned (when they are included). The maximum limit is 50
        :type prices: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeEndpoint
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

    def get(self) -> InAppPurchaseOfferCodeResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseOfferCode
        :rtype: InAppPurchaseOfferCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeResponse.parse_obj(json)

    def update(self, request: InAppPurchaseOfferCodeUpdateRequest) -> InAppPurchaseOfferCodeResponse:
        '''Modify the resource.

        :param request: InAppPurchaseOfferCode representation
        :type request: InAppPurchaseOfferCodeUpdateRequest

        :returns: Single InAppPurchaseOfferCode
        :rtype: InAppPurchaseOfferCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseOfferCodeResponse.parse_obj(json)

class CustomCodesLinkagesOfInAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}/relationships/customCodes'

    def limit(self, number: int=None) -> CustomCodesLinkagesOfInAppPurchaseOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomCodesLinkagesOfInAppPurchaseOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseOfferCodeCustomCodesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseOfferCodeCustomCodesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeCustomCodesLinkagesResponse.parse_obj(json)

class CustomCodesOfInAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}/customCodes'

    def fields(self, *, in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]]=None, actor: Union[ActorField, list[ActorField]]=None) -> CustomCodesOfInAppPurchaseOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_code_custom_code: the fields to include for returned resources of type inAppPurchaseOfferCodeCustomCodes
        :type in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]] = None

        :param actor: the fields to include for returned resources of type actors
        :type actor: Union[ActorField, list[ActorField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomCodesOfInAppPurchaseOfferCodeEndpoint
        '''
        if in_app_purchase_offer_code_custom_code: self._set_fields('inAppPurchaseOfferCodeCustomCodes',in_app_purchase_offer_code_custom_code if type(in_app_purchase_offer_code_custom_code) is list else [in_app_purchase_offer_code_custom_code])
        if actor: self._set_fields('actors',actor if type(actor) is list else [actor])
        return self
        
    class Include(StringEnum):
        CREATED_BY_ACTOR = 'createdByActor'
        DEACTIVATED_BY_ACTOR = 'deactivatedByActor'

    def include(self, relationship: Union[Include, list[Include]]) -> CustomCodesOfInAppPurchaseOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomCodesOfInAppPurchaseOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> CustomCodesOfInAppPurchaseOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomCodesOfInAppPurchaseOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseOfferCodeCustomCodesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchaseOfferCodeCustomCodes
        :rtype: InAppPurchaseOfferCodeCustomCodesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeCustomCodesResponse.parse_obj(json)

class OneTimeUseCodesLinkagesOfInAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}/relationships/oneTimeUseCodes'

    def limit(self, number: int=None) -> OneTimeUseCodesLinkagesOfInAppPurchaseOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesLinkagesOfInAppPurchaseOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseOfferCodeOneTimeUseCodesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseOfferCodeOneTimeUseCodesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeOneTimeUseCodesLinkagesResponse.parse_obj(json)

class OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}/oneTimeUseCodes'

    def fields(self, *, in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]]=None, actor: Union[ActorField, list[ActorField]]=None) -> OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_code_one_time_use_code: the fields to include for returned resources of type inAppPurchaseOfferCodeOneTimeUseCodes
        :type in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]] = None

        :param actor: the fields to include for returned resources of type actors
        :type actor: Union[ActorField, list[ActorField]] = None

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint
        '''
        if in_app_purchase_offer_code_one_time_use_code: self._set_fields('inAppPurchaseOfferCodeOneTimeUseCodes',in_app_purchase_offer_code_one_time_use_code if type(in_app_purchase_offer_code_one_time_use_code) is list else [in_app_purchase_offer_code_one_time_use_code])
        if actor: self._set_fields('actors',actor if type(actor) is list else [actor])
        return self
        
    class Include(StringEnum):
        CREATED_BY_ACTOR = 'createdByActor'
        DEACTIVATED_BY_ACTOR = 'deactivatedByActor'

    def include(self, relationship: Union[Include, list[Include]]) -> OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.OneTimeUseCodesOfInAppPurchaseOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseOfferCodeOneTimeUseCodesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchaseOfferCodeOneTimeUseCodes
        :rtype: InAppPurchaseOfferCodeOneTimeUseCodesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeOneTimeUseCodesResponse.parse_obj(json)

class PricesLinkagesOfInAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}/relationships/prices'

    def limit(self, number: int=None) -> PricesLinkagesOfInAppPurchaseOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesLinkagesOfInAppPurchaseOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseOfferCodePricesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: InAppPurchaseOfferCodePricesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodePricesLinkagesResponse.parse_obj(json)

class PricesOfInAppPurchaseOfferCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodes/{id}/prices'

    def fields(self, *, in_app_purchase_offer_price: Union[InAppPurchaseOfferPriceField, list[InAppPurchaseOfferPriceField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]]=None) -> PricesOfInAppPurchaseOfferCodeEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_price: the fields to include for returned resources of type inAppPurchaseOfferPrices
        :type in_app_purchase_offer_price: Union[InAppPurchaseOfferPriceField, list[InAppPurchaseOfferPriceField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param in_app_purchase_price_point: the fields to include for returned resources of type inAppPurchasePricePoints
        :type in_app_purchase_price_point: Union[InAppPurchasePricePointField, list[InAppPurchasePricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfInAppPurchaseOfferCodeEndpoint
        '''
        if in_app_purchase_offer_price: self._set_fields('inAppPurchaseOfferPrices',in_app_purchase_offer_price if type(in_app_purchase_offer_price) is list else [in_app_purchase_offer_price])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if in_app_purchase_price_point: self._set_fields('inAppPurchasePricePoints',in_app_purchase_price_point if type(in_app_purchase_price_point) is list else [in_app_purchase_price_point])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'
        PRICE_POINT = 'pricePoint'

    def filter(self, *, territory: Union[str, list[str]]=None) -> PricesOfInAppPurchaseOfferCodeEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfInAppPurchaseOfferCodeEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PricesOfInAppPurchaseOfferCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PricesOfInAppPurchaseOfferCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PricesOfInAppPurchaseOfferCodeEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PricesOfInAppPurchaseOfferCodeEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> InAppPurchaseOfferPricesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchaseOfferPrices
        :rtype: InAppPurchaseOfferPricesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferPricesResponse.parse_obj(json)

