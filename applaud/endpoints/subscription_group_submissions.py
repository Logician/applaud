from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class SubscriptionGroupSubmissionsEndpoint(Endpoint):
    path = '/v1/subscriptionGroupSubmissions'

    def create(self, request: SubscriptionGroupSubmissionCreateRequest) -> SubscriptionGroupSubmissionResponse:
        '''Create the resource.

        :param request: SubscriptionGroupSubmission representation
        :type request: SubscriptionGroupSubmissionCreateRequest

        :returns: Single SubscriptionGroupSubmission
        :rtype: SubscriptionGroupSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return SubscriptionGroupSubmissionResponse.parse_obj(json)

