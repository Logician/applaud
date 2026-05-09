from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionImagesEndpoint(Endpoint):
    path = '/v1/subscriptionImages'

    def create(self, request: SubscriptionImageCreateRequest) -> SubscriptionImageResponse:
        '''Create the resource.

        :param request: SubscriptionImage representation
        :type request: SubscriptionImageCreateRequest

        :returns: Single SubscriptionImage
        :rtype: SubscriptionImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionImageResponse.parse_obj(json)

class SubscriptionImageEndpoint(IDEndpoint):
    path = '/v1/subscriptionImages/{id}'

    def fields(self, *, subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]]=None) -> SubscriptionImageEndpoint:
        '''Fields to return for included related types.

        :param subscription_image: the fields to include for returned resources of type subscriptionImages
        :type subscription_image: Union[SubscriptionImageField, list[SubscriptionImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionImageEndpoint
        '''
        if subscription_image: self._set_fields('subscriptionImages',subscription_image if type(subscription_image) is list else [subscription_image])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionImageResponse:
        '''Get the resource.

        :returns: Single SubscriptionImage
        :rtype: SubscriptionImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionImageResponse.parse_obj(json)

    def update(self, request: SubscriptionImageUpdateRequest) -> SubscriptionImageResponse:
        '''Modify the resource.

        :param request: SubscriptionImage representation
        :type request: SubscriptionImageUpdateRequest

        :returns: Single SubscriptionImage
        :rtype: SubscriptionImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

