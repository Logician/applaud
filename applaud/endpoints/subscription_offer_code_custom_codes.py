from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionOfferCodeCustomCodesEndpoint(Endpoint):
    path = '/v1/subscriptionOfferCodeCustomCodes'

    def create(self, request: SubscriptionOfferCodeCustomCodeCreateRequest) -> SubscriptionOfferCodeCustomCodeResponse:
        '''Create the resource.

        :param request: SubscriptionOfferCodeCustomCode representation
        :type request: SubscriptionOfferCodeCustomCodeCreateRequest

        :returns: Single SubscriptionOfferCodeCustomCode
        :rtype: SubscriptionOfferCodeCustomCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionOfferCodeCustomCodeResponse.parse_obj(json)

class SubscriptionOfferCodeCustomCodeEndpoint(IDEndpoint):
    path = '/v1/subscriptionOfferCodeCustomCodes/{id}'

    def fields(self, *, subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]]=None) -> SubscriptionOfferCodeCustomCodeEndpoint:
        '''Fields to return for included related types.

        :param subscription_offer_code_custom_code: the fields to include for returned resources of type subscriptionOfferCodeCustomCodes
        :type subscription_offer_code_custom_code: Union[SubscriptionOfferCodeCustomCodeField, list[SubscriptionOfferCodeCustomCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeCustomCodeEndpoint
        '''
        if subscription_offer_code_custom_code: self._set_fields('subscriptionOfferCodeCustomCodes',subscription_offer_code_custom_code if type(subscription_offer_code_custom_code) is list else [subscription_offer_code_custom_code])
        return self
        
    class Include(StringEnum):
        OFFER_CODE = 'offerCode'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionOfferCodeCustomCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionOfferCodeCustomCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionOfferCodeCustomCodeResponse:
        '''Get the resource.

        :returns: Single SubscriptionOfferCodeCustomCode
        :rtype: SubscriptionOfferCodeCustomCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionOfferCodeCustomCodeResponse.parse_obj(json)

    def update(self, request: SubscriptionOfferCodeCustomCodeUpdateRequest) -> SubscriptionOfferCodeCustomCodeResponse:
        '''Modify the resource.

        :param request: SubscriptionOfferCodeCustomCode representation
        :type request: SubscriptionOfferCodeCustomCodeUpdateRequest

        :returns: Single SubscriptionOfferCodeCustomCode
        :rtype: SubscriptionOfferCodeCustomCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionOfferCodeCustomCodeResponse.parse_obj(json)

