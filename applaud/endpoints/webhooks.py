from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class WebhooksEndpoint(Endpoint):
    path = '/v1/webhooks'

    def create(self, request: WebhookCreateRequest) -> WebhookResponse:
        '''Create the resource.

        :param request: Webhook representation
        :type request: WebhookCreateRequest

        :returns: Single Webhook
        :rtype: WebhookResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return WebhookResponse.parse_obj(json)

class WebhookEndpoint(IDEndpoint):
    path = '/v1/webhooks/{id}'

    @endpoint('/v1/webhooks/{id}/deliveries')
    def deliveries(self) -> DeliveriesOfWebhookEndpoint:
        return DeliveriesOfWebhookEndpoint(self.id, self.session)
        
    @endpoint('/v1/webhooks/{id}/relationships/deliveries')
    def deliveries_linkages(self) -> DeliveriesLinkagesOfWebhookEndpoint:
        return DeliveriesLinkagesOfWebhookEndpoint(self.id, self.session)
        
    def fields(self, *, webhook: Union[WebhookField, list[WebhookField]]=None) -> WebhookEndpoint:
        '''Fields to return for included related types.

        :param webhook: the fields to include for returned resources of type webhooks
        :type webhook: Union[WebhookField, list[WebhookField]] = None

        :returns: self
        :rtype: applaud.endpoints.WebhookEndpoint
        '''
        if webhook: self._set_fields('webhooks',webhook if type(webhook) is list else [webhook])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> WebhookEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.WebhookEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> WebhookResponse:
        '''Get the resource.

        :returns: Single Webhook
        :rtype: WebhookResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WebhookResponse.parse_obj(json)

    def update(self, request: WebhookUpdateRequest) -> WebhookResponse:
        '''Modify the resource.

        :param request: Webhook representation
        :type request: WebhookUpdateRequest

        :returns: Single Webhook
        :rtype: WebhookResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return WebhookResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class DeliveriesLinkagesOfWebhookEndpoint(IDEndpoint):
    path = '/v1/webhooks/{id}/relationships/deliveries'

    def limit(self, number: int=None) -> DeliveriesLinkagesOfWebhookEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DeliveriesLinkagesOfWebhookEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> WebhookDeliveriesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: WebhookDeliveriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WebhookDeliveriesLinkagesResponse.parse_obj(json)

class DeliveriesOfWebhookEndpoint(IDEndpoint):
    path = '/v1/webhooks/{id}/deliveries'

    class DeliveryState(StringEnum):
        SUCCEEDED = 'SUCCEEDED'
        FAILED = 'FAILED'
        PENDING = 'PENDING'

    def fields(self, *, webhook_delivery: Union[WebhookDeliveryField, list[WebhookDeliveryField]]=None, webhook_event: Union[WebhookEventField, list[WebhookEventField]]=None) -> DeliveriesOfWebhookEndpoint:
        '''Fields to return for included related types.

        :param webhook_delivery: the fields to include for returned resources of type webhookDeliveries
        :type webhook_delivery: Union[WebhookDeliveryField, list[WebhookDeliveryField]] = None

        :param webhook_event: the fields to include for returned resources of type webhookEvents
        :type webhook_event: Union[WebhookEventField, list[WebhookEventField]] = None

        :returns: self
        :rtype: applaud.endpoints.DeliveriesOfWebhookEndpoint
        '''
        if webhook_delivery: self._set_fields('webhookDeliveries',webhook_delivery if type(webhook_delivery) is list else [webhook_delivery])
        if webhook_event: self._set_fields('webhookEvents',webhook_event if type(webhook_event) is list else [webhook_event])
        return self
        
    class Include(StringEnum):
        EVENT = 'event'

    def filter(self, *, delivery_state: Union[DeliveryState, list[DeliveryState]]=None, created_date_greater_than_or_equal_to: Union[str, list[str]]=None, created_date_less_than: Union[str, list[str]]=None) -> DeliveriesOfWebhookEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param delivery_state: filter by attribute 'deliveryState'
        :type delivery_state: Union[DeliveryState, list[DeliveryState]] = None

        :param created_date_greater_than_or_equal_to: filter by createdDateGreaterThanOrEqualTo
        :type created_date_greater_than_or_equal_to: Union[str, list[str]] = None

        :param created_date_less_than: filter by createdDateLessThan
        :type created_date_less_than: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.DeliveriesOfWebhookEndpoint
        '''
        if delivery_state: self._set_filter('deliveryState', delivery_state if type(delivery_state) is list else [delivery_state])
        
        if created_date_greater_than_or_equal_to: self._set_filter('createdDateGreaterThanOrEqualTo', created_date_greater_than_or_equal_to if type(created_date_greater_than_or_equal_to) is list else [created_date_greater_than_or_equal_to])
        
        if created_date_less_than: self._set_filter('createdDateLessThan', created_date_less_than if type(created_date_less_than) is list else [created_date_less_than])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> DeliveriesOfWebhookEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.DeliveriesOfWebhookEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> DeliveriesOfWebhookEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DeliveriesOfWebhookEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> WebhookDeliveriesResponse:
        '''Get one or more resources.

        :returns: List of WebhookDeliveries
        :rtype: WebhookDeliveriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WebhookDeliveriesResponse.parse_obj(json)

