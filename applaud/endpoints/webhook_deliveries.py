from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class WebhookDeliveriesEndpoint(Endpoint):
    path = '/v1/webhookDeliveries'

    def create(self, request: WebhookDeliveryCreateRequest) -> WebhookDeliveryResponse:
        '''Create the resource.

        :param request: WebhookDelivery representation
        :type request: WebhookDeliveryCreateRequest

        :returns: Single WebhookDelivery
        :rtype: WebhookDeliveryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return WebhookDeliveryResponse.parse_obj(json)

