from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaRecruitmentCriteriaEndpoint(Endpoint):
    path = '/v1/betaRecruitmentCriteria'

    def create(self, request: BetaRecruitmentCriterionCreateRequest) -> BetaRecruitmentCriterionResponse:
        '''Create the resource.

        :param request: BetaRecruitmentCriterion representation
        :type request: BetaRecruitmentCriterionCreateRequest

        :returns: Single BetaRecruitmentCriterion
        :rtype: BetaRecruitmentCriterionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaRecruitmentCriterionResponse.parse_obj(json)

class BetaRecruitmentCriteriaEndpoint(IDEndpoint):
    path = '/v1/betaRecruitmentCriteria/{id}'

    def update(self, request: BetaRecruitmentCriterionUpdateRequest) -> BetaRecruitmentCriterionResponse:
        '''Modify the resource.

        :param request: BetaRecruitmentCriterion representation
        :type request: BetaRecruitmentCriterionUpdateRequest

        :returns: Single BetaRecruitmentCriterion
        :rtype: BetaRecruitmentCriterionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaRecruitmentCriterionResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

