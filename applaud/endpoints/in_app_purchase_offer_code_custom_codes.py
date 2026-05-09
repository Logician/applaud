from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseOfferCodeCustomCodesEndpoint(Endpoint):
    path = '/v1/inAppPurchaseOfferCodeCustomCodes'

    def create(self, request: InAppPurchaseOfferCodeCustomCodeCreateRequest) -> InAppPurchaseOfferCodeCustomCodeResponse:
        '''Create the resource.

        :param request: InAppPurchaseOfferCodeCustomCode representation
        :type request: InAppPurchaseOfferCodeCustomCodeCreateRequest

        :returns: Single InAppPurchaseOfferCodeCustomCode
        :rtype: InAppPurchaseOfferCodeCustomCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseOfferCodeCustomCodeResponse.parse_obj(json)

class InAppPurchaseOfferCodeCustomCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodeCustomCodes/{id}'

    def fields(self, *, in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]]=None) -> InAppPurchaseOfferCodeCustomCodeEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_code_custom_code: the fields to include for returned resources of type inAppPurchaseOfferCodeCustomCodes
        :type in_app_purchase_offer_code_custom_code: Union[InAppPurchaseOfferCodeCustomCodeField, list[InAppPurchaseOfferCodeCustomCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeCustomCodeEndpoint
        '''
        if in_app_purchase_offer_code_custom_code: self._set_fields('inAppPurchaseOfferCodeCustomCodes',in_app_purchase_offer_code_custom_code if type(in_app_purchase_offer_code_custom_code) is list else [in_app_purchase_offer_code_custom_code])
        return self
        
    class Include(StringEnum):
        CREATED_BY_ACTOR = 'createdByActor'
        DEACTIVATED_BY_ACTOR = 'deactivatedByActor'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseOfferCodeCustomCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeCustomCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseOfferCodeCustomCodeResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseOfferCodeCustomCode
        :rtype: InAppPurchaseOfferCodeCustomCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeCustomCodeResponse.parse_obj(json)

    def update(self, request: InAppPurchaseOfferCodeCustomCodeUpdateRequest) -> InAppPurchaseOfferCodeCustomCodeResponse:
        '''Modify the resource.

        :param request: InAppPurchaseOfferCodeCustomCode representation
        :type request: InAppPurchaseOfferCodeCustomCodeUpdateRequest

        :returns: Single InAppPurchaseOfferCodeCustomCode
        :rtype: InAppPurchaseOfferCodeCustomCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseOfferCodeCustomCodeResponse.parse_obj(json)

