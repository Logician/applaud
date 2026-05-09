from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionGroupLocalizationsEndpoint(Endpoint):
    path = '/v1/subscriptionGroupLocalizations'

    def create(self, request: SubscriptionGroupLocalizationCreateRequest) -> SubscriptionGroupLocalizationResponse:
        '''Create the resource.

        :param request: SubscriptionGroupLocalization representation
        :type request: SubscriptionGroupLocalizationCreateRequest

        :returns: Single SubscriptionGroupLocalization
        :rtype: SubscriptionGroupLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionGroupLocalizationResponse.parse_obj(json)

class SubscriptionGroupLocalizationEndpoint(IDEndpoint):
    path = '/v1/subscriptionGroupLocalizations/{id}'

    def fields(self, *, subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]]=None) -> SubscriptionGroupLocalizationEndpoint:
        '''Fields to return for included related types.

        :param subscription_group_localization: the fields to include for returned resources of type subscriptionGroupLocalizations
        :type subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupLocalizationEndpoint
        '''
        if subscription_group_localization: self._set_fields('subscriptionGroupLocalizations',subscription_group_localization if type(subscription_group_localization) is list else [subscription_group_localization])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTION_GROUP = 'subscriptionGroup'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionGroupLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionGroupLocalizationResponse:
        '''Get the resource.

        :returns: Single SubscriptionGroupLocalization
        :rtype: SubscriptionGroupLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGroupLocalizationResponse.parse_obj(json)

    def update(self, request: SubscriptionGroupLocalizationUpdateRequest) -> SubscriptionGroupLocalizationResponse:
        '''Modify the resource.

        :param request: SubscriptionGroupLocalization representation
        :type request: SubscriptionGroupLocalizationUpdateRequest

        :returns: Single SubscriptionGroupLocalization
        :rtype: SubscriptionGroupLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionGroupLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

