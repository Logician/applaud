from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BetaGroupsEndpoint(Endpoint):
    path = '/v1/betaGroups'

    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_recruitment_criteria: Union[BetaRecruitmentCriteriaField, list[BetaRecruitmentCriteriaField]]=None) -> BetaGroupsEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param beta_recruitment_criteria: the fields to include for returned resources of type betaRecruitmentCriteria
        :type beta_recruitment_criteria: Union[BetaRecruitmentCriteriaField, list[BetaRecruitmentCriteriaField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if beta_recruitment_criteria: self._set_fields('betaRecruitmentCriteria',beta_recruitment_criteria if type(beta_recruitment_criteria) is list else [beta_recruitment_criteria])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUILDS = 'builds'
        BETA_TESTERS = 'betaTesters'
        BETA_RECRUITMENT_CRITERIA = 'betaRecruitmentCriteria'

    def filter(self, *, name: Union[str, list[str]]=None, is_internal_group: Union[str, list[str]]=None, public_link_enabled: Union[str, list[str]]=None, public_link_limit_enabled: Union[str, list[str]]=None, public_link: Union[str, list[str]]=None, app: Union[str, list[str]]=None, builds: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BetaGroupsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param is_internal_group: filter by attribute 'isInternalGroup'
        :type is_internal_group: Union[str, list[str]] = None

        :param public_link_enabled: filter by attribute 'publicLinkEnabled'
        :type public_link_enabled: Union[str, list[str]] = None

        :param public_link_limit_enabled: filter by attribute 'publicLinkLimitEnabled'
        :type public_link_limit_enabled: Union[str, list[str]] = None

        :param public_link: filter by attribute 'publicLink'
        :type public_link: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if is_internal_group: self._set_filter('isInternalGroup', is_internal_group if type(is_internal_group) is list else [is_internal_group])
        
        if public_link_enabled: self._set_filter('publicLinkEnabled', public_link_enabled if type(public_link_enabled) is list else [public_link_enabled])
        
        if public_link_limit_enabled: self._set_filter('publicLinkLimitEnabled', public_link_limit_enabled if type(public_link_limit_enabled) is list else [public_link_limit_enabled])
        
        if public_link: self._set_filter('publicLink', public_link if type(public_link) is list else [public_link])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaGroupsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None, created_date: SortOrder=None, public_link_enabled: SortOrder=None, public_link_limit: SortOrder=None) -> BetaGroupsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if name: self.sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if created_date: self.sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        if public_link_enabled: self.sort_expressions.append('publicLinkEnabled' if public_link_enabled == SortOrder.ASC else '-publicLinkEnabled')
        if public_link_limit: self.sort_expressions.append('publicLinkLimit' if public_link_limit == SortOrder.ASC else '-publicLinkLimit')
        return self
        
    def limit(self, number: int=None, *, beta_testers: int=None, builds: int=None) -> BetaGroupsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param beta_testers: maximum number of related betaTesters returned (when they are included). The maximum limit is 50
        :type beta_testers: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 1000
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if beta_testers and beta_testers > 50:
            raise ValueError(f'The maximum limit of beta_testers is 50')
        if beta_testers: self._set_limit(beta_testers, 'betaTesters')

        if builds and builds > 1000:
            raise ValueError(f'The maximum limit of builds is 1000')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> BetaGroupsResponse:
        '''Get one or more resources.

        :returns: List of BetaGroups
        :rtype: BetaGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupsResponse.parse_obj(json)

    def create(self, request: BetaGroupCreateRequest) -> BetaGroupResponse:
        '''Create the resource.

        :param request: BetaGroup representation
        :type request: BetaGroupCreateRequest

        :returns: Single BetaGroup
        :rtype: BetaGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BetaGroupResponse.parse_obj(json)

class BetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}'

    @endpoint('/v1/betaGroups/{id}/app')
    def app(self) -> AppOfBetaGroupEndpoint:
        return AppOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/betaRecruitmentCriteria')
    def beta_recruitment_criteria(self) -> BetaRecruitmentCriteriaOfBetaGroupEndpoint:
        return BetaRecruitmentCriteriaOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/betaRecruitmentCriterionCompatibleBuildCheck')
    def beta_recruitment_criterion_compatible_build_check(self) -> BetaRecruitmentCriterionCompatibleBuildCheckOfBetaGroupEndpoint:
        return BetaRecruitmentCriterionCompatibleBuildCheckOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/betaTesters')
    def beta_testers(self) -> BetaTestersOfBetaGroupEndpoint:
        return BetaTestersOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/builds')
    def builds(self) -> BuildsOfBetaGroupEndpoint:
        return BuildsOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/metrics/betaTesterUsages')
    def beta_tester_usages(self) -> BetaTesterUsagesOfBetaGroupEndpoint:
        return BetaTesterUsagesOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/metrics/publicLinkUsages')
    def public_link_usages(self) -> PublicLinkUsagesOfBetaGroupEndpoint:
        return PublicLinkUsagesOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/app')
    def app_linkage(self) -> AppLinkageOfBetaGroupEndpoint:
        return AppLinkageOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/betaRecruitmentCriteria')
    def beta_recruitment_criteria_linkage(self) -> BetaRecruitmentCriteriaLinkageOfBetaGroupEndpoint:
        return BetaRecruitmentCriteriaLinkageOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/betaRecruitmentCriterionCompatibleBuildCheck')
    def beta_recruitment_criterion_compatible_build_check_linkage(self) -> BetaRecruitmentCriterionCompatibleBuildCheckLinkageOfBetaGroupEndpoint:
        return BetaRecruitmentCriterionCompatibleBuildCheckLinkageOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/betaTesters')
    def beta_testers_linkages(self) -> BetaTestersLinkagesOfBetaGroupEndpoint:
        return BetaTestersLinkagesOfBetaGroupEndpoint(self.id, self.session)
        
    @endpoint('/v1/betaGroups/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfBetaGroupEndpoint:
        return BuildsLinkagesOfBetaGroupEndpoint(self.id, self.session)
        
    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_recruitment_criteria: Union[BetaRecruitmentCriteriaField, list[BetaRecruitmentCriteriaField]]=None) -> BetaGroupEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param beta_recruitment_criteria: the fields to include for returned resources of type betaRecruitmentCriteria
        :type beta_recruitment_criteria: Union[BetaRecruitmentCriteriaField, list[BetaRecruitmentCriteriaField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if beta_recruitment_criteria: self._set_fields('betaRecruitmentCriteria',beta_recruitment_criteria if type(beta_recruitment_criteria) is list else [beta_recruitment_criteria])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUILDS = 'builds'
        BETA_TESTERS = 'betaTesters'
        BETA_RECRUITMENT_CRITERIA = 'betaRecruitmentCriteria'

    def include(self, relationship: Union[Include, list[Include]]) -> BetaGroupEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaGroupEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, beta_testers: int=None, builds: int=None) -> BetaGroupEndpoint:
        '''Number of included related resources to return.

        :param beta_testers: maximum number of related betaTesters returned (when they are included). The maximum limit is 50
        :type beta_testers: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 1000
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupEndpoint
        '''
        if beta_testers and beta_testers > 50:
            raise ValueError(f'The maximum limit of beta_testers is 50')
        if beta_testers: self._set_limit(beta_testers, 'betaTesters')

        if builds and builds > 1000:
            raise ValueError(f'The maximum limit of builds is 1000')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> BetaGroupResponse:
        '''Get the resource.

        :returns: Single BetaGroup
        :rtype: BetaGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupResponse.parse_obj(json)

    def update(self, request: BetaGroupUpdateRequest) -> BetaGroupResponse:
        '''Modify the resource.

        :param request: BetaGroup representation
        :type request: BetaGroupUpdateRequest

        :returns: Single BetaGroup
        :rtype: BetaGroupResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BetaGroupResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppLinkageOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/app'

    def get(self) -> BetaGroupAppLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BetaGroupAppLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupAppLinkageResponse.parse_obj(json)

class AppOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBetaGroupEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    def get(self) -> AppWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single App with get
        :rtype: AppWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppWithoutIncludesResponse.parse_obj(json)

class BetaRecruitmentCriteriaLinkageOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/betaRecruitmentCriteria'

    def get(self) -> BetaGroupBetaRecruitmentCriteriaLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BetaGroupBetaRecruitmentCriteriaLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupBetaRecruitmentCriteriaLinkageResponse.parse_obj(json)

class BetaRecruitmentCriteriaOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/betaRecruitmentCriteria'

    def fields(self, *, beta_recruitment_criteria: Union[BetaRecruitmentCriteriaField, list[BetaRecruitmentCriteriaField]]=None) -> BetaRecruitmentCriteriaOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param beta_recruitment_criteria: the fields to include for returned resources of type betaRecruitmentCriteria
        :type beta_recruitment_criteria: Union[BetaRecruitmentCriteriaField, list[BetaRecruitmentCriteriaField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaRecruitmentCriteriaOfBetaGroupEndpoint
        '''
        if beta_recruitment_criteria: self._set_fields('betaRecruitmentCriteria',beta_recruitment_criteria if type(beta_recruitment_criteria) is list else [beta_recruitment_criteria])
        return self
        
    def get(self) -> BetaRecruitmentCriterionResponse:
        '''Get the resource.

        :returns: Single BetaRecruitmentCriterion
        :rtype: BetaRecruitmentCriterionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaRecruitmentCriterionResponse.parse_obj(json)

class BetaRecruitmentCriterionCompatibleBuildCheckLinkageOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/betaRecruitmentCriterionCompatibleBuildCheck'

    def get(self) -> BetaGroupBetaRecruitmentCriterionCompatibleBuildCheckLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BetaGroupBetaRecruitmentCriterionCompatibleBuildCheckLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupBetaRecruitmentCriterionCompatibleBuildCheckLinkageResponse.parse_obj(json)

class BetaRecruitmentCriterionCompatibleBuildCheckOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/betaRecruitmentCriterionCompatibleBuildCheck'

    def fields(self, *, beta_recruitment_criterion_compatible_build_check: Union[BetaRecruitmentCriterionCompatibleBuildCheckField, list[BetaRecruitmentCriterionCompatibleBuildCheckField]]=None) -> BetaRecruitmentCriterionCompatibleBuildCheckOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param beta_recruitment_criterion_compatible_build_check: the fields to include for returned resources of type betaRecruitmentCriterionCompatibleBuildChecks
        :type beta_recruitment_criterion_compatible_build_check: Union[BetaRecruitmentCriterionCompatibleBuildCheckField, list[BetaRecruitmentCriterionCompatibleBuildCheckField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaRecruitmentCriterionCompatibleBuildCheckOfBetaGroupEndpoint
        '''
        if beta_recruitment_criterion_compatible_build_check: self._set_fields('betaRecruitmentCriterionCompatibleBuildChecks',beta_recruitment_criterion_compatible_build_check if type(beta_recruitment_criterion_compatible_build_check) is list else [beta_recruitment_criterion_compatible_build_check])
        return self
        
    def get(self) -> BetaRecruitmentCriterionCompatibleBuildCheckResponse:
        '''Get the resource.

        :returns: Single BetaRecruitmentCriterionCompatibleBuildCheck
        :rtype: BetaRecruitmentCriterionCompatibleBuildCheckResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaRecruitmentCriterionCompatibleBuildCheckResponse.parse_obj(json)

class BetaTestersLinkagesOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/betaTesters'

    def limit(self, number: int=None) -> BetaTestersLinkagesOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersLinkagesOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaGroupBetaTestersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaGroupBetaTestersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupBetaTestersLinkagesResponse.parse_obj(json)

    def create(self, request: BetaGroupBetaTestersLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBetaTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BetaGroupBetaTestersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBetaTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BetaTestersOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/betaTesters'

    def fields(self, *, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None) -> BetaTestersOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersOfBetaGroupEndpoint
        '''
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        return self
        
    def limit(self, number: int=None) -> BetaTestersOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTestersOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaTestersWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of BetaTesters with get
        :rtype: BetaTestersWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaTestersWithoutIncludesResponse.parse_obj(json)

class BuildsLinkagesOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/relationships/builds'

    def limit(self, number: int=None) -> BuildsLinkagesOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsLinkagesOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaGroupBuildsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BetaGroupBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupBuildsLinkagesResponse.parse_obj(json)

    def create(self, request: BetaGroupBuildsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BetaGroupBuildsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BetaGroupBuildsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildsOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfBetaGroupEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfBetaGroupEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def limit(self, number: int=None) -> BuildsOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildsWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of Builds with get
        :rtype: BuildsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildsWithoutIncludesResponse.parse_obj(json)

class BetaTesterUsagesOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/metrics/betaTesterUsages'

    def limit(self, number: int=None) -> BetaTesterUsagesOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTesterUsagesOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppsBetaTesterUsagesV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: AppsBetaTesterUsagesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppsBetaTesterUsagesV1MetricResponse.parse_obj(json)

class PublicLinkUsagesOfBetaGroupEndpoint(IDEndpoint):
    path = '/v1/betaGroups/{id}/metrics/publicLinkUsages'

    def limit(self, number: int=None) -> PublicLinkUsagesOfBetaGroupEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PublicLinkUsagesOfBetaGroupEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaPublicLinkUsagesV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: BetaPublicLinkUsagesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaPublicLinkUsagesV1MetricResponse.parse_obj(json)

