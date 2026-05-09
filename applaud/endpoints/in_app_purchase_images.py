from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseImagesEndpoint(Endpoint):
    path = '/v1/inAppPurchaseImages'

    def create(self, request: InAppPurchaseImageCreateRequest) -> InAppPurchaseImageResponse:
        '''Create the resource.

        :param request: InAppPurchaseImage representation
        :type request: InAppPurchaseImageCreateRequest

        :returns: Single InAppPurchaseImage
        :rtype: InAppPurchaseImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseImageResponse.parse_obj(json)

class InAppPurchaseImageEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseImages/{id}'

    def fields(self, *, in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]]=None) -> InAppPurchaseImageEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_image: the fields to include for returned resources of type inAppPurchaseImages
        :type in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseImageEndpoint
        '''
        if in_app_purchase_image: self._set_fields('inAppPurchaseImages',in_app_purchase_image if type(in_app_purchase_image) is list else [in_app_purchase_image])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE = 'inAppPurchase'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseImageResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseImage
        :rtype: InAppPurchaseImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseImageResponse.parse_obj(json)

    def update(self, request: InAppPurchaseImageUpdateRequest) -> InAppPurchaseImageResponse:
        '''Modify the resource.

        :param request: InAppPurchaseImage representation
        :type request: InAppPurchaseImageUpdateRequest

        :returns: Single InAppPurchaseImage
        :rtype: InAppPurchaseImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

