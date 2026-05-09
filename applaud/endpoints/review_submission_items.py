from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class ReviewSubmissionItemsEndpoint(Endpoint):
    path = '/v1/reviewSubmissionItems'

    def create(self, request: ReviewSubmissionItemCreateRequest) -> ReviewSubmissionItemResponse:
        '''Create the resource.

        :param request: ReviewSubmissionItem representation
        :type request: ReviewSubmissionItemCreateRequest

        :returns: Single ReviewSubmissionItem
        :rtype: ReviewSubmissionItemResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return ReviewSubmissionItemResponse.parse_obj(json)

class ReviewSubmissionItemEndpoint(IDEndpoint):
    path = '/v1/reviewSubmissionItems/{id}'

    def update(self, request: ReviewSubmissionItemUpdateRequest) -> ReviewSubmissionItemResponse:
        '''Modify the resource.

        :param request: ReviewSubmissionItem representation
        :type request: ReviewSubmissionItemUpdateRequest

        :returns: Single ReviewSubmissionItem
        :rtype: ReviewSubmissionItemResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return ReviewSubmissionItemResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

