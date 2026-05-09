from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionPricePointEndpoint(IDEndpoint):
    path = '/v1/subscriptionPricePoints/{id}'

    @endpoint('/v1/subscriptionPricePoints/{id}/equalizations')
    def equalizations(self) -> EqualizationsOfSubscriptionPricePointEndpoint:
        return EqualizationsOfSubscriptionPricePointEndpoint(self.id, self.session)
        
    @endpoint('/v1/subscriptionPricePoints/{id}/relationships/equalizations')
    def equalizations_linkages(self) -> EqualizationsLinkagesOfSubscriptionPricePointEndpoint:
        return EqualizationsLinkagesOfSubscriptionPricePointEndpoint(self.id, self.session)
        
    def fields(self, *, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None) -> SubscriptionPricePointEndpoint:
        '''Fields to return for included related types.

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionPricePointEndpoint
        '''
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionPricePointEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionPricePointEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> SubscriptionPricePointResponse:
        '''Get the resource.

        :returns: Single SubscriptionPricePoint
        :rtype: SubscriptionPricePointResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricePointResponse.parse_obj(json)

class EqualizationsLinkagesOfSubscriptionPricePointEndpoint(IDEndpoint):
    path = '/v1/subscriptionPricePoints/{id}/relationships/equalizations'

    def limit(self, number: int=None) -> EqualizationsLinkagesOfSubscriptionPricePointEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsLinkagesOfSubscriptionPricePointEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPricePointEqualizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: SubscriptionPricePointEqualizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricePointEqualizationsLinkagesResponse.parse_obj(json)

class EqualizationsOfSubscriptionPricePointEndpoint(IDEndpoint):
    path = '/v1/subscriptionPricePoints/{id}/equalizations'

    def fields(self, *, subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> EqualizationsOfSubscriptionPricePointEndpoint:
        '''Fields to return for included related types.

        :param subscription_price_point: the fields to include for returned resources of type subscriptionPricePoints
        :type subscription_price_point: Union[SubscriptionPricePointField, list[SubscriptionPricePointField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfSubscriptionPricePointEndpoint
        '''
        if subscription_price_point: self._set_fields('subscriptionPricePoints',subscription_price_point if type(subscription_price_point) is list else [subscription_price_point])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None, subscription: Union[str, list[str]]=None) -> EqualizationsOfSubscriptionPricePointEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :param subscription: filter by id(s) of related 'subscription'
        :type subscription: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfSubscriptionPricePointEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        if subscription: self._set_filter('subscription', subscription if type(subscription) is list else [subscription])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> EqualizationsOfSubscriptionPricePointEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfSubscriptionPricePointEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> EqualizationsOfSubscriptionPricePointEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 8000
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.EqualizationsOfSubscriptionPricePointEndpoint
        '''
        if number and number > 8000:
            raise ValueError(f'The maximum limit of number is 8000')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> SubscriptionPricePointsResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionPricePoints
        :rtype: SubscriptionPricePointsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionPricePointsResponse.parse_obj(json)

