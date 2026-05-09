from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class PreReleaseVersionsEndpoint(Endpoint):
    path = '/v1/preReleaseVersions'

    class Builds_buildAudienceType(StringEnum):
        INTERNAL_ONLY = 'INTERNAL_ONLY'
        APP_STORE_ELIGIBLE = 'APP_STORE_ELIGIBLE'

    def fields(self, *, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, build: Union[BuildField, list[BuildField]]=None, app: Union[AppField, list[AppField]]=None) -> PreReleaseVersionsEndpoint:
        '''Fields to return for included related types.

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsEndpoint
        '''
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'
        APP = 'app'

    def filter(self, *, builds_build_audience_type: Union[Builds_buildAudienceType, list[Builds_buildAudienceType]]=None, builds_expired: Union[str, list[str]]=None, builds_processing_state: Union[BuildProcessingState, list[BuildProcessingState]]=None, builds_version: Union[str, list[str]]=None, platform: Union[Platform, list[Platform]]=None, version: Union[str, list[str]]=None, app: Union[str, list[str]]=None, builds: Union[str, list[str]]=None) -> PreReleaseVersionsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param builds_build_audience_type: filter by attribute 'builds.buildAudienceType'
        :type builds_build_audience_type: Union[Builds_buildAudienceType, list[Builds_buildAudienceType]] = None

        :param builds_expired: filter by attribute 'builds.expired'
        :type builds_expired: Union[str, list[str]] = None

        :param builds_processing_state: filter by attribute 'builds.processingState'
        :type builds_processing_state: Union[BuildProcessingState, list[BuildProcessingState]] = None

        :param builds_version: filter by attribute 'builds.version'
        :type builds_version: Union[str, list[str]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param version: filter by attribute 'version'
        :type version: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsEndpoint
        '''
        if builds_build_audience_type: self._set_filter('builds.buildAudienceType', builds_build_audience_type if type(builds_build_audience_type) is list else [builds_build_audience_type])
        
        if builds_expired: self._set_filter('builds.expired', builds_expired if type(builds_expired) is list else [builds_expired])
        
        if builds_processing_state: self._set_filter('builds.processingState', builds_processing_state if type(builds_processing_state) is list else [builds_processing_state])
        
        if builds_version: self._set_filter('builds.version', builds_version if type(builds_version) is list else [builds_version])
        
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if version: self._set_filter('version', version if type(version) is list else [version])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PreReleaseVersionsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version: SortOrder=None) -> PreReleaseVersionsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsEndpoint
        '''
        if version: self.sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        return self
        
    def limit(self, number: int=None, *, builds: int=None) -> PreReleaseVersionsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> PreReleaseVersionsResponse:
        '''Get one or more resources.

        :returns: List of PreReleaseVersions
        :rtype: PreReleaseVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PreReleaseVersionsResponse.parse_obj(json)

class PreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}'

    @endpoint('/v1/preReleaseVersions/{id}/app')
    def app(self) -> AppOfPreReleaseVersionEndpoint:
        return AppOfPreReleaseVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/preReleaseVersions/{id}/builds')
    def builds(self) -> BuildsOfPreReleaseVersionEndpoint:
        return BuildsOfPreReleaseVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/preReleaseVersions/{id}/relationships/app')
    def app_linkage(self) -> AppLinkageOfPreReleaseVersionEndpoint:
        return AppLinkageOfPreReleaseVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/preReleaseVersions/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfPreReleaseVersionEndpoint:
        return BuildsLinkagesOfPreReleaseVersionEndpoint(self.id, self.session)
        
    def fields(self, *, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, build: Union[BuildField, list[BuildField]]=None, app: Union[AppField, list[AppField]]=None) -> PreReleaseVersionEndpoint:
        '''Fields to return for included related types.

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionEndpoint
        '''
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> PreReleaseVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, builds: int=None) -> PreReleaseVersionEndpoint:
        '''Number of included related resources to return.

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionEndpoint
        '''
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> PrereleaseVersionResponse:
        '''Get the resource.

        :returns: Single PrereleaseVersion
        :rtype: PrereleaseVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PrereleaseVersionResponse.parse_obj(json)

class AppLinkageOfPreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}/relationships/app'

    def get(self) -> PrereleaseVersionAppLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: PrereleaseVersionAppLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PrereleaseVersionAppLinkageResponse.parse_obj(json)

class AppOfPreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfPreReleaseVersionEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfPreReleaseVersionEndpoint
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

class BuildsLinkagesOfPreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}/relationships/builds'

    def limit(self, number: int=None) -> BuildsLinkagesOfPreReleaseVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsLinkagesOfPreReleaseVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> PrereleaseVersionBuildsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: PrereleaseVersionBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PrereleaseVersionBuildsLinkagesResponse.parse_obj(json)

class BuildsOfPreReleaseVersionEndpoint(IDEndpoint):
    path = '/v1/preReleaseVersions/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfPreReleaseVersionEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfPreReleaseVersionEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def limit(self, number: int=None) -> BuildsOfPreReleaseVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfPreReleaseVersionEndpoint
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

