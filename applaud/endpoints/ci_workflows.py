from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiWorkflowsEndpoint(Endpoint):
    path = '/v1/ciWorkflows'

    def create(self, request: CiWorkflowCreateRequest) -> CiWorkflowResponse:
        '''Create the resource.

        :param request: CiWorkflow representation
        :type request: CiWorkflowCreateRequest

        :returns: Single CiWorkflow
        :rtype: CiWorkflowResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return CiWorkflowResponse.parse_obj(json)

class CiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}'

    @endpoint('/v1/ciWorkflows/{id}/buildRuns')
    def build_runs(self) -> BuildRunsOfCiWorkflowEndpoint:
        return BuildRunsOfCiWorkflowEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciWorkflows/{id}/repository')
    def repository(self) -> RepositoryOfCiWorkflowEndpoint:
        return RepositoryOfCiWorkflowEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciWorkflows/{id}/relationships/buildRuns')
    def build_runs_linkages(self) -> BuildRunsLinkagesOfCiWorkflowEndpoint:
        return BuildRunsLinkagesOfCiWorkflowEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciWorkflows/{id}/relationships/repository')
    def repository_linkage(self) -> RepositoryLinkageOfCiWorkflowEndpoint:
        return RepositoryLinkageOfCiWorkflowEndpoint(self.id, self.session)
        
    def fields(self, *, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiWorkflowEndpoint:
        '''Fields to return for included related types.

        :param ci_workflow: the fields to include for returned resources of type ciWorkflows
        :type ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiWorkflowEndpoint
        '''
        if ci_workflow: self._set_fields('ciWorkflows',ci_workflow if type(ci_workflow) is list else [ci_workflow])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        PRODUCT = 'product'
        REPOSITORY = 'repository'
        XCODE_VERSION = 'xcodeVersion'
        MAC_OS_VERSION = 'macOsVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> CiWorkflowEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiWorkflowEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> CiWorkflowResponse:
        '''Get the resource.

        :returns: Single CiWorkflow
        :rtype: CiWorkflowResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiWorkflowResponse.parse_obj(json)

    def update(self, request: CiWorkflowUpdateRequest) -> CiWorkflowResponse:
        '''Modify the resource.

        :param request: CiWorkflow representation
        :type request: CiWorkflowUpdateRequest

        :returns: Single CiWorkflow
        :rtype: CiWorkflowResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return CiWorkflowResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class BuildRunsLinkagesOfCiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}/relationships/buildRuns'

    def limit(self, number: int=None) -> BuildRunsLinkagesOfCiWorkflowEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsLinkagesOfCiWorkflowEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiWorkflowBuildRunsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiWorkflowBuildRunsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiWorkflowBuildRunsLinkagesResponse.parse_obj(json)

class BuildRunsOfCiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}/buildRuns'

    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, build: Union[BuildField, list[BuildField]]=None, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> BuildRunsOfCiWorkflowEndpoint:
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
        :rtype: applaud.endpoints.BuildRunsOfCiWorkflowEndpoint
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

    def filter(self, *, builds: Union[str, list[str]]=None) -> BuildRunsOfCiWorkflowEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiWorkflowEndpoint
        '''
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildRunsOfCiWorkflowEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiWorkflowEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, number: SortOrder=None) -> BuildRunsOfCiWorkflowEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiWorkflowEndpoint
        '''
        if number: self.sort_expressions.append('number' if number == SortOrder.ASC else '-number')
        return self
        
    def limit(self, number: int=None, *, builds: int=None) -> BuildRunsOfCiWorkflowEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiWorkflowEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> CiBuildRunsResponse:
        '''Get one or more resources.

        :returns: List of CiBuildRuns
        :rtype: CiBuildRunsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunsResponse.parse_obj(json)

class RepositoryLinkageOfCiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}/relationships/repository'

    def get(self) -> CiWorkflowRepositoryLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: CiWorkflowRepositoryLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiWorkflowRepositoryLinkageResponse.parse_obj(json)

class RepositoryOfCiWorkflowEndpoint(IDEndpoint):
    path = '/v1/ciWorkflows/{id}/repository'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None, scm_provider: Union[ScmProviderField, list[ScmProviderField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None) -> RepositoryOfCiWorkflowEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :param scm_provider: the fields to include for returned resources of type scmProviders
        :type scm_provider: Union[ScmProviderField, list[ScmProviderField]] = None

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :returns: self
        :rtype: applaud.endpoints.RepositoryOfCiWorkflowEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        if scm_provider: self._set_fields('scmProviders',scm_provider if type(scm_provider) is list else [scm_provider])
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        return self
        
    class Include(StringEnum):
        SCM_PROVIDER = 'scmProvider'
        DEFAULT_BRANCH = 'defaultBranch'

    def include(self, relationship: Union[Include, list[Include]]) -> RepositoryOfCiWorkflowEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.RepositoryOfCiWorkflowEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> ScmRepositoryResponse:
        '''Get the resource.

        :returns: Single ScmRepository
        :rtype: ScmRepositoryResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoryResponse.parse_obj(json)

