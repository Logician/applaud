from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseAppStoreReviewScreenshotsEndpoint(Endpoint):
    path = '/v1/inAppPurchaseAppStoreReviewScreenshots'

    def create(self, request: InAppPurchaseAppStoreReviewScreenshotCreateRequest) -> InAppPurchaseAppStoreReviewScreenshotResponse:
        '''Create the resource.

        :param request: InAppPurchaseAppStoreReviewScreenshot representation
        :type request: InAppPurchaseAppStoreReviewScreenshotCreateRequest

        :returns: Single InAppPurchaseAppStoreReviewScreenshot
        :rtype: InAppPurchaseAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseAppStoreReviewScreenshotResponse.parse_obj(json)

class InAppPurchaseAppStoreReviewScreenshotEndpoint(IDEndpoint):
    path = '/v1/inAppPurchaseAppStoreReviewScreenshots/{id}'

    def fields(self, *, in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]]=None) -> InAppPurchaseAppStoreReviewScreenshotEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase_app_store_review_screenshot: the fields to include for returned resources of type inAppPurchaseAppStoreReviewScreenshots
        :type in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAppStoreReviewScreenshotEndpoint
        '''
        if in_app_purchase_app_store_review_screenshot: self._set_fields('inAppPurchaseAppStoreReviewScreenshots',in_app_purchase_app_store_review_screenshot if type(in_app_purchase_app_store_review_screenshot) is list else [in_app_purchase_app_store_review_screenshot])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'

    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchaseAppStoreReviewScreenshotEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchaseAppStoreReviewScreenshotEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> InAppPurchaseAppStoreReviewScreenshotResponse:
        '''Get the resource.

        :returns: Single InAppPurchaseAppStoreReviewScreenshot
        :rtype: InAppPurchaseAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchaseAppStoreReviewScreenshotResponse.parse_obj(json)

    def update(self, request: InAppPurchaseAppStoreReviewScreenshotUpdateRequest) -> InAppPurchaseAppStoreReviewScreenshotResponse:
        '''Modify the resource.

        :param request: InAppPurchaseAppStoreReviewScreenshot representation
        :type request: InAppPurchaseAppStoreReviewScreenshotUpdateRequest

        :returns: Single InAppPurchaseAppStoreReviewScreenshot
        :rtype: InAppPurchaseAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return InAppPurchaseAppStoreReviewScreenshotResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

