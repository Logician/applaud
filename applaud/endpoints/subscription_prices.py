from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionPricesEndpoint(Endpoint):
    path = '/v1/subscriptionPrices'

    def create(self, request: SubscriptionPriceCreateRequest) -> SubscriptionPriceResponse:
        '''Create the resource.

        :param request: SubscriptionPrice representation
        :type request: SubscriptionPriceCreateRequest

        :returns: Single SubscriptionPrice
        :rtype: SubscriptionPriceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionPriceResponse.parse_obj(json)

class SubscriptionPriceEndpoint(IDEndpoint):
    path = '/v1/subscriptionPrices/{id}'

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

