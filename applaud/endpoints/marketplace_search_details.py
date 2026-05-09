from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class MarketplaceSearchDetailsEndpoint(Endpoint):
    path = '/v1/marketplaceSearchDetails'

    def create(self, request: MarketplaceSearchDetailCreateRequest) -> MarketplaceSearchDetailResponse:
        '''Create the resource.

        :param request: MarketplaceSearchDetail representation
        :type request: MarketplaceSearchDetailCreateRequest

        :returns: Single MarketplaceSearchDetail
        :rtype: MarketplaceSearchDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return MarketplaceSearchDetailResponse.parse_obj(json)

class MarketplaceSearchDetailEndpoint(IDEndpoint):
    path = '/v1/marketplaceSearchDetails/{id}'

    def update(self, request: MarketplaceSearchDetailUpdateRequest) -> MarketplaceSearchDetailResponse:
        '''Modify the resource.

        :param request: MarketplaceSearchDetail representation
        :type request: MarketplaceSearchDetailUpdateRequest

        :returns: Single MarketplaceSearchDetail
        :rtype: MarketplaceSearchDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return MarketplaceSearchDetailResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

