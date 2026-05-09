from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SandboxTestersClearPurchaseHistoryRequestEndpoint(Endpoint):
    path = '/v2/sandboxTestersClearPurchaseHistoryRequest'

    def create(self, request: SandboxTestersClearPurchaseHistoryRequestV2CreateRequest) -> SandboxTestersClearPurchaseHistoryRequestV2Response:
        '''Create the resource.

        :param request: SandboxTestersClearPurchaseHistoryRequest representation
        :type request: SandboxTestersClearPurchaseHistoryRequestV2CreateRequest

        :returns: Single SandboxTestersClearPurchaseHistoryRequest
        :rtype: SandboxTestersClearPurchaseHistoryRequestV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SandboxTestersClearPurchaseHistoryRequestV2Response.parse_obj(json)

