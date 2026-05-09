from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionGracePeriodEndpoint(IDEndpoint):
    path = '/v1/subscriptionGracePeriods/{id}'

    def fields(self, *, subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]]=None) -> SubscriptionGracePeriodEndpoint:
        '''Fields to return for included related types.

        :param subscription_grace_period: the fields to include for returned resources of type subscriptionGracePeriods
        :type subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGracePeriodEndpoint
        '''
        if subscription_grace_period: self._set_fields('subscriptionGracePeriods',subscription_grace_period if type(subscription_grace_period) is list else [subscription_grace_period])
        return self
        
    def get(self) -> SubscriptionGracePeriodResponse:
        '''Get the resource.

        :returns: Single SubscriptionGracePeriod
        :rtype: SubscriptionGracePeriodResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGracePeriodResponse.parse_obj(json)

    def update(self, request: SubscriptionGracePeriodUpdateRequest) -> SubscriptionGracePeriodResponse:
        '''Modify the resource.

        :param request: SubscriptionGracePeriod representation
        :type request: SubscriptionGracePeriodUpdateRequest

        :returns: Single SubscriptionGracePeriod
        :rtype: SubscriptionGracePeriodResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionGracePeriodResponse.parse_obj(json)

