from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}'

    @endpoint('/v1/ciBuildActions/{id}/artifacts')
    def artifacts(self) -> ArtifactsOfCiBuildActionEndpoint:
        return ArtifactsOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/buildRun')
    def build_run(self) -> BuildRunOfCiBuildActionEndpoint:
        return BuildRunOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/issues')
    def issues(self) -> IssuesOfCiBuildActionEndpoint:
        return IssuesOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/testResults')
    def test_results(self) -> TestResultsOfCiBuildActionEndpoint:
        return TestResultsOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/relationships/artifacts')
    def artifacts_linkages(self) -> ArtifactsLinkagesOfCiBuildActionEndpoint:
        return ArtifactsLinkagesOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/relationships/buildRun')
    def build_run_linkage(self) -> BuildRunLinkageOfCiBuildActionEndpoint:
        return BuildRunLinkageOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/relationships/issues')
    def issues_linkages(self) -> IssuesLinkagesOfCiBuildActionEndpoint:
        return IssuesLinkagesOfCiBuildActionEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildActions/{id}/relationships/testResults')
    def test_results_linkages(self) -> TestResultsLinkagesOfCiBuildActionEndpoint:
        return TestResultsLinkagesOfCiBuildActionEndpoint(self.id, self.session)
        
    def fields(self, *, ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]]=None, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None) -> CiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_build_action: the fields to include for returned resources of type ciBuildActions
        :type ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]] = None

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiBuildActionEndpoint
        '''
        if ci_build_action: self._set_fields('ciBuildActions',ci_build_action if type(ci_build_action) is list else [ci_build_action])
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        return self
        
    class Include(StringEnum):
        BUILD_RUN = 'buildRun'

    def include(self, relationship: Union[Include, list[Include]]) -> CiBuildActionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiBuildActionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> CiBuildActionResponse:
        '''Get the resource.

        :returns: Single CiBuildAction
        :rtype: CiBuildActionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionResponse.parse_obj(json)

class ArtifactsLinkagesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/artifacts'

    def limit(self, number: int=None) -> ArtifactsLinkagesOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ArtifactsLinkagesOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildActionArtifactsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiBuildActionArtifactsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionArtifactsLinkagesResponse.parse_obj(json)

class ArtifactsOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/artifacts'

    def fields(self, *, ci_artifact: Union[CiArtifactField, list[CiArtifactField]]=None) -> ArtifactsOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_artifact: the fields to include for returned resources of type ciArtifacts
        :type ci_artifact: Union[CiArtifactField, list[CiArtifactField]] = None

        :returns: self
        :rtype: applaud.endpoints.ArtifactsOfCiBuildActionEndpoint
        '''
        if ci_artifact: self._set_fields('ciArtifacts',ci_artifact if type(ci_artifact) is list else [ci_artifact])
        return self
        
    def limit(self, number: int=None) -> ArtifactsOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ArtifactsOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiArtifactsResponse:
        '''Get one or more resources.

        :returns: List of CiArtifacts
        :rtype: CiArtifactsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiArtifactsResponse.parse_obj(json)

class BuildRunLinkageOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/buildRun'

    def get(self) -> CiBuildActionBuildRunLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: CiBuildActionBuildRunLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionBuildRunLinkageResponse.parse_obj(json)

class BuildRunOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/buildRun'

    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, build: Union[BuildField, list[BuildField]]=None, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> BuildRunOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param ci_workflow: the fields to include for returned resources of type ciWorkflows
        :type ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]] = None

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :param scm_pull_request: the fields to include for returned resources of type scmPullRequests
        :type scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunOfCiBuildActionEndpoint
        '''
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if ci_workflow: self._set_fields('ciWorkflows',ci_workflow if type(ci_workflow) is list else [ci_workflow])
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        if scm_pull_request: self._set_fields('scmPullRequests',scm_pull_request if type(scm_pull_request) is list else [scm_pull_request])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'
        WORKFLOW = 'workflow'
        PRODUCT = 'product'
        SOURCE_BRANCH_OR_TAG = 'sourceBranchOrTag'
        DESTINATION_BRANCH = 'destinationBranch'
        PULL_REQUEST = 'pullRequest'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildRunOfCiBuildActionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildRunOfCiBuildActionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, builds: int=None) -> BuildRunOfCiBuildActionEndpoint:
        '''Number of included related resources to return.

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunOfCiBuildActionEndpoint
        '''
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> CiBuildRunResponse:
        '''Get the resource.

        :returns: Single CiBuildRun
        :rtype: CiBuildRunResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunResponse.parse_obj(json)

class IssuesLinkagesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/issues'

    def limit(self, number: int=None) -> IssuesLinkagesOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IssuesLinkagesOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildActionIssuesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiBuildActionIssuesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionIssuesLinkagesResponse.parse_obj(json)

class IssuesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/issues'

    def fields(self, *, ci_issue: Union[CiIssueField, list[CiIssueField]]=None) -> IssuesOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_issue: the fields to include for returned resources of type ciIssues
        :type ci_issue: Union[CiIssueField, list[CiIssueField]] = None

        :returns: self
        :rtype: applaud.endpoints.IssuesOfCiBuildActionEndpoint
        '''
        if ci_issue: self._set_fields('ciIssues',ci_issue if type(ci_issue) is list else [ci_issue])
        return self
        
    def limit(self, number: int=None) -> IssuesOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IssuesOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiIssuesResponse:
        '''Get one or more resources.

        :returns: List of CiIssues
        :rtype: CiIssuesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiIssuesResponse.parse_obj(json)

class TestResultsLinkagesOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/relationships/testResults'

    def limit(self, number: int=None) -> TestResultsLinkagesOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TestResultsLinkagesOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildActionTestResultsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiBuildActionTestResultsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionTestResultsLinkagesResponse.parse_obj(json)

class TestResultsOfCiBuildActionEndpoint(IDEndpoint):
    path = '/v1/ciBuildActions/{id}/testResults'

    def fields(self, *, ci_test_result: Union[CiTestResultField, list[CiTestResultField]]=None) -> TestResultsOfCiBuildActionEndpoint:
        '''Fields to return for included related types.

        :param ci_test_result: the fields to include for returned resources of type ciTestResults
        :type ci_test_result: Union[CiTestResultField, list[CiTestResultField]] = None

        :returns: self
        :rtype: applaud.endpoints.TestResultsOfCiBuildActionEndpoint
        '''
        if ci_test_result: self._set_fields('ciTestResults',ci_test_result if type(ci_test_result) is list else [ci_test_result])
        return self
        
    def limit(self, number: int=None) -> TestResultsOfCiBuildActionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.TestResultsOfCiBuildActionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiTestResultsResponse:
        '''Get one or more resources.

        :returns: List of CiTestResults
        :rtype: CiTestResultsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiTestResultsResponse.parse_obj(json)

