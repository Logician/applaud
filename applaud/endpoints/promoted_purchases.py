from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class PromotedPurchasesEndpoint(Endpoint):
    path = '/v1/promotedPurchases'

    def create(self, request: PromotedPurchaseCreateRequest) -> PromotedPurchaseResponse:
        '''Create the resource.

        :param request: PromotedPurchase representation
        :type request: PromotedPurchaseCreateRequest

        :returns: Single PromotedPurchase
        :rtype: PromotedPurchaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return PromotedPurchaseResponse.parse_obj(json)

class PromotedPurchaseEndpoint(IDEndpoint):
    path = '/v1/promotedPurchases/{id}'

    def fields(self, *, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None) -> PromotedPurchaseEndpoint:
        '''Fields to return for included related types.

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchaseEndpoint
        '''
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> PromotedPurchaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> PromotedPurchaseResponse:
        '''Get the resource.

        :returns: Single PromotedPurchase
        :rtype: PromotedPurchaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PromotedPurchaseResponse.parse_obj(json)

    def update(self, request: PromotedPurchaseUpdateRequest) -> PromotedPurchaseResponse:
        '''Modify the resource.

        :param request: PromotedPurchase representation
        :type request: PromotedPurchaseUpdateRequest

        :returns: Single PromotedPurchase
        :rtype: PromotedPurchaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return PromotedPurchaseResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

