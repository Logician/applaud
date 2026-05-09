from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class MarketplaceWebhooksEndpoint(Endpoint):
    path = '/v1/marketplaceWebhooks'

    def fields(self, *, marketplace_webhook: Union[MarketplaceWebhookField, list[MarketplaceWebhookField]]=None) -> MarketplaceWebhooksEndpoint:
        '''Fields to return for included related types.

        :param marketplace_webhook: the fields to include for returned resources of type marketplaceWebhooks
        :type marketplace_webhook: Union[MarketplaceWebhookField, list[MarketplaceWebhookField]] = None

        :returns: self
        :rtype: applaud.endpoints.MarketplaceWebhooksEndpoint
        '''
        if marketplace_webhook: self._set_fields('marketplaceWebhooks',marketplace_webhook if type(marketplace_webhook) is list else [marketplace_webhook])
        return self
        
    def limit(self, number: int=None) -> MarketplaceWebhooksEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.MarketplaceWebhooksEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> MarketplaceWebhooksResponse:
        '''Get one or more resources.

        :returns: List of MarketplaceWebhooks
        :rtype: MarketplaceWebhooksResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return MarketplaceWebhooksResponse.parse_obj(json)

    @deprecated
    def create(self, request: MarketplaceWebhookCreateRequest) -> MarketplaceWebhookResponse:
        '''Create the resource.

        :param request: MarketplaceWebhook representation
        :type request: MarketplaceWebhookCreateRequest

        :returns: Single MarketplaceWebhook
        :rtype: MarketplaceWebhookResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return MarketplaceWebhookResponse.parse_obj(json)

class MarketplaceWebhookEndpoint(IDEndpoint):
    path = '/v1/marketplaceWebhooks/{id}'

    @deprecated
    def update(self, request: MarketplaceWebhookUpdateRequest) -> MarketplaceWebhookResponse:
        '''Modify the resource.

        :param request: MarketplaceWebhook representation
        :type request: MarketplaceWebhookUpdateRequest

        :returns: Single MarketplaceWebhook
        :rtype: MarketplaceWebhookResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return MarketplaceWebhookResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

