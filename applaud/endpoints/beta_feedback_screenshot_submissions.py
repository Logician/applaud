from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaFeedbackScreenshotSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaFeedbackScreenshotSubmissions/{id}'

    def fields(self, *, beta_feedback_screenshot_submission: Union[BetaFeedbackScreenshotSubmissionField, list[BetaFeedbackScreenshotSubmissionField]]=None) -> BetaFeedbackScreenshotSubmissionEndpoint:
        '''Fields to return for included related types.

        :param beta_feedback_screenshot_submission: the fields to include for returned resources of type betaFeedbackScreenshotSubmissions
        :type beta_feedback_screenshot_submission: Union[BetaFeedbackScreenshotSubmissionField, list[BetaFeedbackScreenshotSubmissionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionEndpoint
        '''
        if beta_feedback_screenshot_submission: self._set_fields('betaFeedbackScreenshotSubmissions',beta_feedback_screenshot_submission if type(beta_feedback_screenshot_submission) is list else [beta_feedback_screenshot_submission])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'
        TESTER = 'tester'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaFeedbackScreenshotSubmissionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaFeedbackScreenshotSubmissionResponse:
        '''Get the resource.

        :returns: Single BetaFeedbackScreenshotSubmission
        :rtype: BetaFeedbackScreenshotSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaFeedbackScreenshotSubmissionResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

