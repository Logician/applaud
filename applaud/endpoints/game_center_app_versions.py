from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterAppVersionsEndpoint(Endpoint):
    path = '/v1/gameCenterAppVersions'

    def create(self, request: GameCenterAppVersionCreateRequest) -> GameCenterAppVersionResponse:
        '''Create the resource.

        :param request: GameCenterAppVersion representation
        :type request: GameCenterAppVersionCreateRequest

        :returns: Single GameCenterAppVersion
        :rtype: GameCenterAppVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAppVersionResponse.parse_obj(json)

class GameCenterAppVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterAppVersions/{id}'

    @endpoint('/v1/gameCenterAppVersions/{id}/appStoreVersion')
    def app_store_version(self) -> AppStoreVersionOfGameCenterAppVersionEndpoint:
        return AppStoreVersionOfGameCenterAppVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAppVersions/{id}/compatibilityVersions')
    def compatibility_versions(self) -> CompatibilityVersionsOfGameCenterAppVersionEndpoint:
        return CompatibilityVersionsOfGameCenterAppVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAppVersions/{id}/relationships/appStoreVersion')
    def app_store_version_linkage(self) -> AppStoreVersionLinkageOfGameCenterAppVersionEndpoint:
        return AppStoreVersionLinkageOfGameCenterAppVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions')
    def compatibility_versions_linkages(self) -> CompatibilityVersionsLinkagesOfGameCenterAppVersionEndpoint:
        return CompatibilityVersionsLinkagesOfGameCenterAppVersionEndpoint(self.id, self.session)
        
    def fields(self, *, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> GameCenterAppVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionEndpoint
        '''
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        COMPATIBILITY_VERSIONS = 'compatibilityVersions'
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAppVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, compatibility_versions: int=None) -> GameCenterAppVersionEndpoint:
        '''Number of included related resources to return.

        :param compatibility_versions: maximum number of related compatibilityVersions returned (when they are included). The maximum limit is 50
        :type compatibility_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionEndpoint
        '''
        if compatibility_versions and compatibility_versions > 50:
            raise ValueError(f'The maximum limit of compatibility_versions is 50')
        if compatibility_versions: self._set_limit(compatibility_versions, 'compatibilityVersions')

        return self

    def get(self) -> GameCenterAppVersionResponse:
        '''Get the resource.

        :returns: Single GameCenterAppVersion
        :rtype: GameCenterAppVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAppVersionResponse.parse_obj(json)

    def update(self, request: GameCenterAppVersionUpdateRequest) -> GameCenterAppVersionResponse:
        '''Modify the resource.

        :param request: GameCenterAppVersion representation
        :type request: GameCenterAppVersionUpdateRequest

        :returns: Single GameCenterAppVersion
        :rtype: GameCenterAppVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAppVersionResponse.parse_obj(json)

class AppStoreVersionLinkageOfGameCenterAppVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterAppVersions/{id}/relationships/appStoreVersion'

    def get(self) -> GameCenterAppVersionAppStoreVersionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: GameCenterAppVersionAppStoreVersionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAppVersionAppStoreVersionLinkageResponse.parse_obj(json)

class AppStoreVersionOfGameCenterAppVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterAppVersions/{id}/appStoreVersion'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app: Union[AppField, list[AppField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None) -> AppStoreVersionOfGameCenterAppVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param app_store_version_phased_release: the fields to include for returned resources of type appStoreVersionPhasedReleases
        :type app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]] = None

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param routing_app_coverage: the fields to include for returned resources of type routingAppCoverages
        :type routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]] = None

        :param app_store_review_detail: the fields to include for returned resources of type appStoreReviewDetails
        :type app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]] = None

        :param app_store_version_submission: the fields to include for returned resources of type appStoreVersionSubmissions
        :type app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param alternative_distribution_package: the fields to include for returned resources of type alternativeDistributionPackages
        :type alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionOfGameCenterAppVersionEndpoint
        '''
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if app_store_version_phased_release: self._set_fields('appStoreVersionPhasedReleases',app_store_version_phased_release if type(app_store_version_phased_release) is list else [app_store_version_phased_release])
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if routing_app_coverage: self._set_fields('routingAppCoverages',routing_app_coverage if type(routing_app_coverage) is list else [routing_app_coverage])
        if app_store_review_detail: self._set_fields('appStoreReviewDetails',app_store_review_detail if type(app_store_review_detail) is list else [app_store_review_detail])
        if app_store_version_submission: self._set_fields('appStoreVersionSubmissions',app_store_version_submission if type(app_store_version_submission) is list else [app_store_version_submission])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if alternative_distribution_package: self._set_fields('alternativeDistributionPackages',alternative_distribution_package if type(alternative_distribution_package) is list else [alternative_distribution_package])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_STORE_VERSION_LOCALIZATIONS = 'appStoreVersionLocalizations'
        BUILD = 'build'
        APP_STORE_VERSION_PHASED_RELEASE = 'appStoreVersionPhasedRelease'
        GAME_CENTER_APP_VERSION = 'gameCenterAppVersion'
        ROUTING_APP_COVERAGE = 'routingAppCoverage'
        APP_STORE_REVIEW_DETAIL = 'appStoreReviewDetail'
        APP_STORE_VERSION_SUBMISSION = 'appStoreVersionSubmission'
        APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
        APP_STORE_VERSION_EXPERIMENTS = 'appStoreVersionExperiments'
        APP_STORE_VERSION_EXPERIMENTS_V2 = 'appStoreVersionExperimentsV2'
        ALTERNATIVE_DISTRIBUTION_PACKAGE = 'alternativeDistributionPackage'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionOfGameCenterAppVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionOfGameCenterAppVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_localizations: int=None, app_store_version_experiments: int=None, app_store_version_experiments_v2: int=None) -> AppStoreVersionOfGameCenterAppVersionEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :param app_store_version_experiments: maximum number of related appStoreVersionExperiments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionOfGameCenterAppVersionEndpoint
        '''
        if app_store_version_localizations and app_store_version_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_localizations is 50')
        if app_store_version_localizations: self._set_limit(app_store_version_localizations, 'appStoreVersionLocalizations')

        if app_store_version_experiments and app_store_version_experiments > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments is 50')
        if app_store_version_experiments: self._set_limit(app_store_version_experiments, 'appStoreVersionExperiments')

        if app_store_version_experiments_v2 and app_store_version_experiments_v2 > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments_v2 is 50')
        if app_store_version_experiments_v2: self._set_limit(app_store_version_experiments_v2, 'appStoreVersionExperimentsV2')

        return self

    def get(self) -> AppStoreVersionResponse:
        '''Get the resource.

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionResponse.parse_obj(json)

class CompatibilityVersionsLinkagesOfGameCenterAppVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions'

    def limit(self, number: int=None) -> CompatibilityVersionsLinkagesOfGameCenterAppVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CompatibilityVersionsLinkagesOfGameCenterAppVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> GameCenterAppVersionCompatibilityVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: GameCenterAppVersionCompatibilityVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAppVersionCompatibilityVersionsLinkagesResponse.parse_obj(json)

    def create(self, request: GameCenterAppVersionCompatibilityVersionsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterAppVersionCompatibilityVersionsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: GameCenterAppVersionCompatibilityVersionsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: GameCenterAppVersionCompatibilityVersionsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class CompatibilityVersionsOfGameCenterAppVersionEndpoint(IDEndpoint):
    path = '/v1/gameCenterAppVersions/{id}/compatibilityVersions'

    def fields(self, *, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> CompatibilityVersionsOfGameCenterAppVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.CompatibilityVersionsOfGameCenterAppVersionEndpoint
        '''
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        COMPATIBILITY_VERSIONS = 'compatibilityVersions'
        APP_STORE_VERSION = 'appStoreVersion'

    def filter(self, *, enabled: Union[str, list[str]]=None) -> CompatibilityVersionsOfGameCenterAppVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param enabled: filter by attribute 'enabled'
        :type enabled: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CompatibilityVersionsOfGameCenterAppVersionEndpoint
        '''
        if enabled: self._set_filter('enabled', enabled if type(enabled) is list else [enabled])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CompatibilityVersionsOfGameCenterAppVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CompatibilityVersionsOfGameCenterAppVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, compatibility_versions: int=None) -> CompatibilityVersionsOfGameCenterAppVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param compatibility_versions: maximum number of related compatibilityVersions returned (when they are included). The maximum limit is 50
        :type compatibility_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.CompatibilityVersionsOfGameCenterAppVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if compatibility_versions and compatibility_versions > 50:
            raise ValueError(f'The maximum limit of compatibility_versions is 50')
        if compatibility_versions: self._set_limit(compatibility_versions, 'compatibilityVersions')

        return self

    def get(self) -> GameCenterAppVersionsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterAppVersions
        :rtype: GameCenterAppVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAppVersionsResponse.parse_obj(json)

