from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class EndAppAvailabilityPreOrdersEndpoint(Endpoint):
    path = '/v1/endAppAvailabilityPreOrders'

    def create(self, request: EndAppAvailabilityPreOrderCreateRequest) -> EndAppAvailabilityPreOrderResponse:
        '''Create the resource.

        :param request: EndAppAvailabilityPreOrder representation
        :type request: EndAppAvailabilityPreOrderCreateRequest

        :returns: Single EndAppAvailabilityPreOrder
        :rtype: EndAppAvailabilityPreOrderResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return EndAppAvailabilityPreOrderResponse.parse_obj(json)

