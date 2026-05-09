from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionIntroductoryOffersEndpoint(Endpoint):
    path = '/v1/subscriptionIntroductoryOffers'

    def create(self, request: SubscriptionIntroductoryOfferCreateRequest) -> SubscriptionIntroductoryOfferResponse:
        '''Create the resource.

        :param request: SubscriptionIntroductoryOffer representation
        :type request: SubscriptionIntroductoryOfferCreateRequest

        :returns: Single SubscriptionIntroductoryOffer
        :rtype: SubscriptionIntroductoryOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionIntroductoryOfferResponse.parse_obj(json)

class SubscriptionIntroductoryOfferEndpoint(IDEndpoint):
    path = '/v1/subscriptionIntroductoryOffers/{id}'

    def update(self, request: SubscriptionIntroductoryOfferUpdateRequest) -> SubscriptionIntroductoryOfferResponse:
        '''Modify the resource.

        :param request: SubscriptionIntroductoryOffer representation
        :type request: SubscriptionIntroductoryOfferUpdateRequest

        :returns: Single SubscriptionIntroductoryOffer
        :rtype: SubscriptionIntroductoryOfferResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return SubscriptionIntroductoryOfferResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

