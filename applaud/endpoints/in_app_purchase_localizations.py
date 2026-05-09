from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseLocalizationsEndpoint(Endpoint):
    path = '/v1/inAppPurchaseLocalizations'

    def create(self, request: InAppPurchaseLocalizationCreateRequest) -> InAppPurchaseLocalizationResponse:
        '''Create the resource.

        :param request: InAppPurchaseLocalization representation
        :type request: InAppPurchaseLocalizationCreateRequest

        :returns: Single InAppPurchaseLocalization
        :rtype: InAppPurchaseLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseLocalizationResponse.parse_obj(json)

class InAppPurchaseLocalizationEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseLocalizations/{id}'

    def fields(self, *, in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]]=None) -> InAppPurchaseLocalizationEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_localization: the fields to include for returned resources of type inAppPurchaseLocalizations
        :type in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseLocalizationEndpoint
        '''
        if in_app_purchase_localization: self._set_fields('inAppPurchaseLocalizations',in_app_purchase_localization if type(in_app_purchase_localization) is list else [in_app_purchase_localization])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseLocalizationResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseLocalization
        :rtype: InAppPurchaseLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseLocalizationResponse.parse_obj(json)

    def update(self, request: InAppPurchaseLocalizationUpdateRequest) -> InAppPurchaseLocalizationResponse:
        '''Modify the resource.

        :param request: InAppPurchaseLocalization representation
        :type request: InAppPurchaseLocalizationUpdateRequest

        :returns: Single InAppPurchaseLocalization
        :rtype: InAppPurchaseLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

