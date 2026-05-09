from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaRecruitmentCriterionOptionsEndpoint(Endpoint):
    path = '/v1/betaRecruitmentCriterionOptions'

    def fields(self, *, beta_recruitment_criterion_option: Union[BetaRecruitmentCriterionOptionField, list[BetaRecruitmentCriterionOptionField]]=None) -> BetaRecruitmentCriterionOptionsEndpoint:
        '''Fields to return for included related types.

        :param beta_recruitment_criterion_option: the fields to include for returned resources of type betaRecruitmentCriterionOptions
        :type beta_recruitment_criterion_option: Union[BetaRecruitmentCriterionOptionField, list[BetaRecruitmentCriterionOptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaRecruitmentCriterionOptionsEndpoint
        '''
        if beta_recruitment_criterion_option: self._set_fields('betaRecruitmentCriterionOptions',beta_recruitment_criterion_option if type(beta_recruitment_criterion_option) is list else [beta_recruitment_criterion_option])
        return self
        
    def limit(self, number: int=None) -> BetaRecruitmentCriterionOptionsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaRecruitmentCriterionOptionsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaRecruitmentCriterionOptionsResponse:
        '''Get one or more resources.

        :returns: List of BetaRecruitmentCriterionOptions
        :rtype: BetaRecruitmentCriterionOptionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaRecruitmentCriterionOptionsResponse.parse_obj(json)

