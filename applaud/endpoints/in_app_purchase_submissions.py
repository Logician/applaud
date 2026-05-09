from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class InAppPurchaseSubmissionsEndpoint(Endpoint):
    path = '/v1/inAppPurchaseSubmissions'

    def create(self, request: InAppPurchaseSubmissionCreateRequest) -> InAppPurchaseSubmissionResponse:
        '''Create the resource.

        :param request: InAppPurchaseSubmission representation
        :type request: InAppPurchaseSubmissionCreateRequest

        :returns: Single InAppPurchaseSubmission
        :rtype: InAppPurchaseSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return InAppPurchaseSubmissionResponse.parse_obj(json)

