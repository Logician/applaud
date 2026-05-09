from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionPromotionsEndpoint(Endpoint):
    path = '/v1/appStoreVersionPromotions'

    def create(self, request: AppStoreVersionPromotionCreateRequest) -> AppStoreVersionPromotionResponse:
        '''Create the resource.

        :param request: AppStoreVersionPromotion representation
        :type request: AppStoreVersionPromotionCreateRequest

        :returns: Single AppStoreVersionPromotion
        :rtype: AppStoreVersionPromotionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionPromotionResponse.parse_obj(json)

