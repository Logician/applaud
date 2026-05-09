from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionOfferCodeOneTimeUseCodesEndpoint(Endpoint):
    path = '/v1/subscriptionOfferCodeOneTimeUseCodes'

    def create(self, request: SubscriptionOfferCodeOneTimeUseCodeCreateRequest) -> SubscriptionOfferCodeOneTimeUseCodeResponse:
        '''Create the resource.

        :param request: SubscriptionOfferCodeOneTimeUseCode representation
        :type request: SubscriptionOfferCodeOneTimeUseCodeCreateRequest

        :returns: Single SubscriptionOfferCodeOneTimeUseCode
        :rtype: SubscriptionOfferCodeOneTimeUseCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionOfferCodeOneTimeUseCodeResponse.parse_obj(json)

class SubscriptionOfferCodeOneTimeUseCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodeOneTimeUseCodes/{id}'

    @endpoint('/v1/subscriptionOfferCodeOneTimeUseCodes/{id}/values')
    def values(self) -> ValuesOfSubscriptionOfferCodeOneTimeUseCodeEndpoint:
        return ValuesOfSubscriptionOfferCodeOneTimeUseCodeEndpoint(self.id, self.session)
        
    def fields(self, *, subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]]=None) -> SubscriptionOfferCodeOneTimeUseCodeEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code_one_time_use_code: the fields to include for returned resources of type subscriptionOfferCodeOneTimeUseCodes
        :type subscription_offer_code_one_time_use_code: Union[SubscriptionOfferCodeOneTimeUseCodeField, list[SubscriptionOfferCodeOneTimeUseCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeOneTimeUseCodeEndpoint
        '''
        if subscription_offer_code_one_time_use_code: self._set_fields('subscriptionOfferCodeOneTimeUseCodes',subscription_offer_code_one_time_use_code if type(subscription_offer_code_one_time_use_code) is list else [subscription_offer_code_one_time_use_code])
        return self
        
    class Include(StringEnum):
        OFFER_CODE = 'offerCode'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionOfferCodeOneTimeUseCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeOneTimeUseCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionOfferCodeOneTimeUseCodeResponse:
        '''Get the resource.

        :returns: Single SubscriptionOfferCodeOneTimeUseCode
        :rtype: SubscriptionOfferCodeOneTimeUseCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeOneTimeUseCodeResponse.parse_obj(json)

    def update(self, request: SubscriptionOfferCodeOneTimeUseCodeUpdateRequest) -> SubscriptionOfferCodeOneTimeUseCodeResponse:
        '''Modify the resource.

        :param request: SubscriptionOfferCodeOneTimeUseCode representation
        :type request: SubscriptionOfferCodeOneTimeUseCodeUpdateRequest

        :returns: Single SubscriptionOfferCodeOneTimeUseCode
        :rtype: SubscriptionOfferCodeOneTimeUseCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionOfferCodeOneTimeUseCodeResponse.parse_obj(json)

class ValuesOfSubscriptionOfferCodeOneTimeUseCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodeOneTimeUseCodes/{id}/values'

    def get(self) -> CsvStreamResponse:
        '''Get the resource.

        :returns: Single SubscriptionOfferCodeOneTimeUseCodeValue
        :rtype: CsvStreamResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CsvStreamResponse.parse_obj(json)

