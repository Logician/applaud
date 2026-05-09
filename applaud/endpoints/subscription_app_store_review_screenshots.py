from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionAppStoreReviewScreenshotsEndpoint(Endpoint):
    path = '/v1/subscriptionAppStoreReviewScreenshots'

    def create(self, request: SubscriptionAppStoreReviewScreenshotCreateRequest) -> SubscriptionAppStoreReviewScreenshotResponse:
        '''Create the resource.

        :param request: SubscriptionAppStoreReviewScreenshot representation
        :type request: SubscriptionAppStoreReviewScreenshotCreateRequest

        :returns: Single SubscriptionAppStoreReviewScreenshot
        :rtype: SubscriptionAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionAppStoreReviewScreenshotResponse.parse_obj(json)

class SubscriptionAppStoreReviewScreenshotEndpoint(IDEndpoint):
    path = '/v1/subscriptionAppStoreReviewScreenshots/{id}'

    def fields(self, *, subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]]=None) -> SubscriptionAppStoreReviewScreenshotEndpoint:
        '''Fields to return for included related types.

        :param subscription_app_store_review_screenshot: the fields to include for returned resources of type subscriptionAppStoreReviewScreenshots
        :type subscription_app_store_review_screenshot: Union[SubscriptionAppStoreReviewScreenshotField, list[SubscriptionAppStoreReviewScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAppStoreReviewScreenshotEndpoint
        '''
        if subscription_app_store_review_screenshot: self._set_fields('subscriptionAppStoreReviewScreenshots',subscription_app_store_review_screenshot if type(subscription_app_store_review_screenshot) is list else [subscription_app_store_review_screenshot])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionAppStoreReviewScreenshotEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionAppStoreReviewScreenshotEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionAppStoreReviewScreenshotResponse:
        '''Get the resource.

        :returns: Single SubscriptionAppStoreReviewScreenshot
        :rtype: SubscriptionAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionAppStoreReviewScreenshotResponse.parse_obj(json)

    def update(self, request: SubscriptionAppStoreReviewScreenshotUpdateRequest) -> SubscriptionAppStoreReviewScreenshotResponse:
        '''Modify the resource.

        :param request: SubscriptionAppStoreReviewScreenshot representation
        :type request: SubscriptionAppStoreReviewScreenshotUpdateRequest

        :returns: Single SubscriptionAppStoreReviewScreenshot
        :rtype: SubscriptionAppStoreReviewScreenshotResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionAppStoreReviewScreenshotResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

