from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionLocalizationsEndpoint(Endpoint):
    path = '/v1/subscriptionLocalizations'

    def create(self, request: SubscriptionLocalizationCreateRequest) -> SubscriptionLocalizationResponse:
        '''Create the resource.

        :param request: SubscriptionLocalization representation
        :type request: SubscriptionLocalizationCreateRequest

        :returns: Single SubscriptionLocalization
        :rtype: SubscriptionLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionLocalizationResponse.parse_obj(json)

class SubscriptionLocalizationEndpoint(IDEndpoint):
    path = '/v1/subscriptionLocalizations/{id}'

    def fields(self, *, subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]]=None) -> SubscriptionLocalizationEndpoint:
        '''Fields to return for included related types.

        :param subscription_localization: the fields to include for returned resources of type subscriptionLocalizations
        :type subscription_localization: Union[SubscriptionLocalizationField, list[SubscriptionLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionLocalizationEndpoint
        '''
        if subscription_localization: self._set_fields('subscriptionLocalizations',subscription_localization if type(subscription_localization) is list else [subscription_localization])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionLocalizationResponse:
        '''Get the resource.

        :returns: Single SubscriptionLocalization
        :rtype: SubscriptionLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionLocalizationResponse.parse_obj(json)

    def update(self, request: SubscriptionLocalizationUpdateRequest) -> SubscriptionLocalizationResponse:
        '''Modify the resource.

        :param request: SubscriptionLocalization representation
        :type request: SubscriptionLocalizationUpdateRequest

        :returns: Single SubscriptionLocalization
        :rtype: SubscriptionLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

