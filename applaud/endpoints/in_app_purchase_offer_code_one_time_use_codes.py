from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseOfferCodeOneTimeUseCodesEndpoint(Endpoint):
    path = '/v1/inAppPurchaseOfferCodeOneTimeUseCodes'

    def create(self, request: InAppPurchaseOfferCodeOneTimeUseCodeCreateRequest) -> InAppPurchaseOfferCodeOneTimeUseCodeResponse:
        '''Create the resource.

        :param request: InAppPurchaseOfferCodeOneTimeUseCode representation
        :type request: InAppPurchaseOfferCodeOneTimeUseCodeCreateRequest

        :returns: Single InAppPurchaseOfferCodeOneTimeUseCode
        :rtype: InAppPurchaseOfferCodeOneTimeUseCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseOfferCodeOneTimeUseCodeResponse.parse_obj(json)

class InAppPurchaseOfferCodeOneTimeUseCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodeOneTimeUseCodes/{id}'

    @endpoint('/v1/inAppPurchaseOfferCodeOneTimeUseCodes/{id}/values')
    def values(self) -> ValuesOfInAppPurchaseOfferCodeOneTimeUseCodeEndpoint:
        return ValuesOfInAppPurchaseOfferCodeOneTimeUseCodeEndpoint(self.id, self.session)
        
    def fields(self, *, in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]]=None) -> InAppPurchaseOfferCodeOneTimeUseCodeEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_offer_code_one_time_use_code: the fields to include for returned resources of type inAppPurchaseOfferCodeOneTimeUseCodes
        :type in_app_purchase_offer_code_one_time_use_code: Union[InAppPurchaseOfferCodeOneTimeUseCodeField, list[InAppPurchaseOfferCodeOneTimeUseCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeOneTimeUseCodeEndpoint
        '''
        if in_app_purchase_offer_code_one_time_use_code: self._set_fields('inAppPurchaseOfferCodeOneTimeUseCodes',in_app_purchase_offer_code_one_time_use_code if type(in_app_purchase_offer_code_one_time_use_code) is list else [in_app_purchase_offer_code_one_time_use_code])
        return self
        
    class Include(StringEnum):
        CREATED_BY_ACTOR = 'createdByActor'
        DEACTIVATED_BY_ACTOR = 'deactivatedByActor'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseOfferCodeOneTimeUseCodeEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseOfferCodeOneTimeUseCodeEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseOfferCodeOneTimeUseCodeResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseOfferCodeOneTimeUseCode
        :rtype: InAppPurchaseOfferCodeOneTimeUseCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseOfferCodeOneTimeUseCodeResponse.parse_obj(json)
    def update(self, request: InAppPurchaseOfferCodeOneTimeUseCodeUpdateRequest) -> InAppPurchaseOfferCodeOneTimeUseCodeResponse:
        '''Modify the resource.

        :param request: InAppPurchaseOfferCodeOneTimeUseCode representation
        :type request: InAppPurchaseOfferCodeOneTimeUseCodeUpdateRequest

        :returns: Single InAppPurchaseOfferCodeOneTimeUseCode
        :rtype: InAppPurchaseOfferCodeOneTimeUseCodeResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseOfferCodeOneTimeUseCodeResponse.parse_obj(json)

class ValuesOfInAppPurchaseOfferCodeOneTimeUseCodeEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseOfferCodeOneTimeUseCodes/{id}/values'

    def get(self) -> CsvStreamResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseOfferCodeOneTimeUseCodeValue
        :rtype: CsvStreamResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CsvStreamResponse.parse_obj(json)
