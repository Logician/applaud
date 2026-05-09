from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class TerritoryAvailabilityEndpoint(IDEndpoint):
    path = '/v1/territoryAvailabilities/{id}'

    def update(self, request: TerritoryAvailabilityUpdateRequest) -> TerritoryAvailabilityResponse:
        '''Modify the resource.

        :param request: TerritoryAvailability representation
        :type request: TerritoryAvailabilityUpdateRequest

        :returns: Single TerritoryAvailability
        :rtype: TerritoryAvailabilityResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return TerritoryAvailabilityResponse.parse_obj(json)

