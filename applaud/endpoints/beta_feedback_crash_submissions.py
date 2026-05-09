from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaFeedbackCrashSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaFeedbackCrashSubmissions/{id}'

    @endpoint('/v1/betaFeedbackCrashSubmissions/{id}/crashLog')
    def crash_log(self) -> CrashLogOfBetaFeedbackCrashSubmissionEndpoint:
        return CrashLogOfBetaFeedbackCrashSubmissionEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaFeedbackCrashSubmissions/{id}/relationships/crashLog')
    def crash_log_linkage(self) -> CrashLogLinkageOfBetaFeedbackCrashSubmissionEndpoint:
        return CrashLogLinkageOfBetaFeedbackCrashSubmissionEndpoint(self.id, self.session)
        
    def fields(self, *, beta_feedback_crash_submission: Union[BetaFeedbackCrashSubmissionField, list[BetaFeedbackCrashSubmissionField]]=None) -> BetaFeedbackCrashSubmissionEndpoint:
        '''Fields to return for included related types.

        :param beta_feedback_crash_submission: the fields to include for returned resources of type betaFeedbackCrashSubmissions
        :type beta_feedback_crash_submission: Union[BetaFeedbackCrashSubmissionField, list[BetaFeedbackCrashSubmissionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionEndpoint
        '''
        if beta_feedback_crash_submission: self._set_fields('betaFeedbackCrashSubmissions',beta_feedback_crash_submission if type(beta_feedback_crash_submission) is list else [beta_feedback_crash_submission])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'
        TESTER = 'tester'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaFeedbackCrashSubmissionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BetaFeedbackCrashSubmissionResponse:
        '''Get the resource.

        :returns: Single BetaFeedbackCrashSubmission
        :rtype: BetaFeedbackCrashSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaFeedbackCrashSubmissionResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class CrashLogLinkageOfBetaFeedbackCrashSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaFeedbackCrashSubmissions/{id}/relationships/crashLog'

    def get(self) -> BetaFeedbackCrashSubmissionCrashLogLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BetaFeedbackCrashSubmissionCrashLogLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaFeedbackCrashSubmissionCrashLogLinkageResponse.parse_obj(json)

class CrashLogOfBetaFeedbackCrashSubmissionEndpoint(IDEndpoint):
    path = '/v1/betaFeedbackCrashSubmissions/{id}/crashLog'

    def fields(self, *, beta_crash_log: Union[BetaCrashLogField, list[BetaCrashLogField]]=None) -> CrashLogOfBetaFeedbackCrashSubmissionEndpoint:
        '''Fields to return for included related types.

        :param beta_crash_log: the fields to include for returned resources of type betaCrashLogs
        :type beta_crash_log: Union[BetaCrashLogField, list[BetaCrashLogField]] = None

        :returns: self
        :rtype: applaud.endpoints.CrashLogOfBetaFeedbackCrashSubmissionEndpoint
        '''
        if beta_crash_log: self._set_fields('betaCrashLogs',beta_crash_log if type(beta_crash_log) is list else [beta_crash_log])
        return self
        
    def get(self) -> BetaCrashLogResponse:
        '''Get the resource.

        :returns: Single BetaCrashLog
        :rtype: BetaCrashLogResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaCrashLogResponse.parse_obj(json)

