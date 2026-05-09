from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionsEndpoint(Endpoint):
    path = '/v1/appStoreVersions'

    def create(self, request: AppStoreVersionCreateRequest) -> AppStoreVersionResponse:
        '''Create the resource.

        :param request: AppStoreVersion representation
        :type request: AppStoreVersionCreateRequest

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionResponse.parse_obj(json)

class AppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}'

    @endpoint('/v1/appStoreVersions/{id}/alternativeDistributionPackage')
    def alternative_distribution_package(self) -> AlternativeDistributionPackageOfAppStoreVersionEndpoint:
        return AlternativeDistributionPackageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appClipDefaultExperience')
    def app_clip_default_experience(self) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        return AppClipDefaultExperienceOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreReviewDetail')
    def app_store_review_detail(self) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        return AppStoreReviewDetailOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionExperiments')
    def app_store_version_experiments(self) -> AppStoreVersionExperimentsOfAppStoreVersionEndpoint:
        return AppStoreVersionExperimentsOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionExperimentsV2')
    def app_store_version_experiments_v2(self) -> AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint:
        return AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionLocalizations')
    def app_store_version_localizations(self) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        return AppStoreVersionLocalizationsOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionPhasedRelease')
    def app_store_version_phased_release(self) -> AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint:
        return AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/appStoreVersionSubmission')
    def app_store_version_submission(self) -> AppStoreVersionSubmissionOfAppStoreVersionEndpoint:
        return AppStoreVersionSubmissionOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/build')
    def build(self) -> BuildOfAppStoreVersionEndpoint:
        return BuildOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/customerReviews')
    def customer_reviews(self) -> CustomerReviewsOfAppStoreVersionEndpoint:
        return CustomerReviewsOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/gameCenterAppVersion')
    def game_center_app_version(self) -> GameCenterAppVersionOfAppStoreVersionEndpoint:
        return GameCenterAppVersionOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/routingAppCoverage')
    def routing_app_coverage(self) -> RoutingAppCoverageOfAppStoreVersionEndpoint:
        return RoutingAppCoverageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/alternativeDistributionPackage')
    def alternative_distribution_package_linkage(self) -> AlternativeDistributionPackageLinkageOfAppStoreVersionEndpoint:
        return AlternativeDistributionPackageLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appClipDefaultExperience')
    def app_clip_default_experience_linkage(self) -> AppClipDefaultExperienceLinkageOfAppStoreVersionEndpoint:
        return AppClipDefaultExperienceLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appStoreReviewDetail')
    def app_store_review_detail_linkage(self) -> AppStoreReviewDetailLinkageOfAppStoreVersionEndpoint:
        return AppStoreReviewDetailLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appStoreVersionExperiments')
    def app_store_version_experiments_linkages(self) -> AppStoreVersionExperimentsLinkagesOfAppStoreVersionEndpoint:
        return AppStoreVersionExperimentsLinkagesOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appStoreVersionExperimentsV2')
    def app_store_version_experiments_v2_linkage(self) -> AppStoreVersionExperimentsV2LinkageOfAppStoreVersionEndpoint:
        return AppStoreVersionExperimentsV2LinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appStoreVersionLocalizations')
    def app_store_version_localizations_linkages(self) -> AppStoreVersionLocalizationsLinkagesOfAppStoreVersionEndpoint:
        return AppStoreVersionLocalizationsLinkagesOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appStoreVersionPhasedRelease')
    def app_store_version_phased_release_linkage(self) -> AppStoreVersionPhasedReleaseLinkageOfAppStoreVersionEndpoint:
        return AppStoreVersionPhasedReleaseLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/appStoreVersionSubmission')
    def app_store_version_submission_linkage(self) -> AppStoreVersionSubmissionLinkageOfAppStoreVersionEndpoint:
        return AppStoreVersionSubmissionLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/build')
    def build_linkage(self) -> BuildLinkageOfAppStoreVersionEndpoint:
        return BuildLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/customerReviews')
    def customer_reviews_linkages(self) -> CustomerReviewsLinkagesOfAppStoreVersionEndpoint:
        return CustomerReviewsLinkagesOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/gameCenterAppVersion')
    def game_center_app_version_linkage(self) -> GameCenterAppVersionLinkageOfAppStoreVersionEndpoint:
        return GameCenterAppVersionLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersions/{id}/relationships/routingAppCoverage')
    def routing_app_coverage_linkage(self) -> RoutingAppCoverageLinkageOfAppStoreVersionEndpoint:
        return RoutingAppCoverageLinkageOfAppStoreVersionEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None) -> AppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

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
        :rtype: applaud.endpoints.AppStoreVersionEndpoint
        '''
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
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

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_experiments: int=None, app_store_version_experiments_v2: int=None, app_store_version_localizations: int=None) -> AppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_experiments: maximum number of related appStoreVersionExperiments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionEndpoint
        '''
        if app_store_version_experiments and app_store_version_experiments > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments is 50')
        if app_store_version_experiments: self._set_limit(app_store_version_experiments, 'appStoreVersionExperiments')

        if app_store_version_experiments_v2 and app_store_version_experiments_v2 > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments_v2 is 50')
        if app_store_version_experiments_v2: self._set_limit(app_store_version_experiments_v2, 'appStoreVersionExperimentsV2')

        if app_store_version_localizations and app_store_version_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_localizations is 50')
        if app_store_version_localizations: self._set_limit(app_store_version_localizations, 'appStoreVersionLocalizations')

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

    def update(self, request: AppStoreVersionUpdateRequest) -> AppStoreVersionResponse:
        '''Modify the resource.

        :param request: AppStoreVersion representation
        :type request: AppStoreVersionUpdateRequest

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreVersionResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AlternativeDistributionPackageLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/alternativeDistributionPackage'

    def get(self) -> AppStoreVersionAlternativeDistributionPackageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionAlternativeDistributionPackageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAlternativeDistributionPackageLinkageResponse.parse_obj(json)

class AlternativeDistributionPackageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/alternativeDistributionPackage'

    def fields(self, *, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None, alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]]=None) -> AlternativeDistributionPackageOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_package: the fields to include for returned resources of type alternativeDistributionPackages
        :type alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]] = None

        :param alternative_distribution_package_version: the fields to include for returned resources of type alternativeDistributionPackageVersions
        :type alternative_distribution_package_version: Union[AlternativeDistributionPackageVersionField, list[AlternativeDistributionPackageVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageOfAppStoreVersionEndpoint
        '''
        if alternative_distribution_package: self._set_fields('alternativeDistributionPackages',alternative_distribution_package if type(alternative_distribution_package) is list else [alternative_distribution_package])
        if alternative_distribution_package_version: self._set_fields('alternativeDistributionPackageVersions',alternative_distribution_package_version if type(alternative_distribution_package_version) is list else [alternative_distribution_package_version])
        return self
        
    class Include(StringEnum):
        VERSIONS = 'versions'

    def include(self, relationship: Union[Include, list[Include]]) -> AlternativeDistributionPackageOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, versions: int=None) -> AlternativeDistributionPackageOfAppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param versions: maximum number of related versions returned (when they are included). The maximum limit is 50
        :type versions: int = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionPackageOfAppStoreVersionEndpoint
        '''
        if versions and versions > 50:
            raise ValueError(f'The maximum limit of versions is 50')
        if versions: self._set_limit(versions, 'versions')

        return self

    def get(self) -> AlternativeDistributionPackageResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionPackage
        :rtype: AlternativeDistributionPackageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionPackageResponse.parse_obj(json)

class AppClipDefaultExperienceLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appClipDefaultExperience'

    def get(self) -> AppStoreVersionAppClipDefaultExperienceLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionAppClipDefaultExperienceLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppClipDefaultExperienceLinkageResponse.parse_obj(json)

    def update(self, request: AppStoreVersionAppClipDefaultExperienceLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: AppStoreVersionAppClipDefaultExperienceLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class AppClipDefaultExperienceOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appClipDefaultExperience'

    def fields(self, *, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None, app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]]=None) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :param app_clip_app_store_review_detail: the fields to include for returned resources of type appClipAppStoreReviewDetails
        :type app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceOfAppStoreVersionEndpoint
        '''
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        if app_clip_app_store_review_detail: self._set_fields('appClipAppStoreReviewDetails',app_clip_app_store_review_detail if type(app_clip_app_store_review_detail) is list else [app_clip_app_store_review_detail])
        return self
        
    class Include(StringEnum):
        APP_CLIP = 'appClip'
        RELEASE_WITH_APP_STORE_VERSION = 'releaseWithAppStoreVersion'
        APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATIONS = 'appClipDefaultExperienceLocalizations'
        APP_CLIP_APP_STORE_REVIEW_DETAIL = 'appClipAppStoreReviewDetail'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_clip_default_experience_localizations: int=None) -> AppClipDefaultExperienceOfAppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param app_clip_default_experience_localizations: maximum number of related appClipDefaultExperienceLocalizations returned (when they are included). The maximum limit is 50
        :type app_clip_default_experience_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceOfAppStoreVersionEndpoint
        '''
        if app_clip_default_experience_localizations and app_clip_default_experience_localizations > 50:
            raise ValueError(f'The maximum limit of app_clip_default_experience_localizations is 50')
        if app_clip_default_experience_localizations: self._set_limit(app_clip_default_experience_localizations, 'appClipDefaultExperienceLocalizations')

        return self

    def get(self) -> AppClipDefaultExperienceResponse:
        '''Get the resource.

        :returns: Single AppClipDefaultExperience
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceResponse.parse_obj(json)

class AppStoreReviewDetailLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreReviewDetail'

    def get(self) -> AppStoreVersionAppStoreReviewDetailLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionAppStoreReviewDetailLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppStoreReviewDetailLinkageResponse.parse_obj(json)

class AppStoreReviewDetailOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreReviewDetail'

    def fields(self, *, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]]=None) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_review_detail: the fields to include for returned resources of type appStoreReviewDetails
        :type app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_store_review_attachment: the fields to include for returned resources of type appStoreReviewAttachments
        :type app_store_review_attachment: Union[AppStoreReviewAttachmentField, list[AppStoreReviewAttachmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailOfAppStoreVersionEndpoint
        '''
        if app_store_review_detail: self._set_fields('appStoreReviewDetails',app_store_review_detail if type(app_store_review_detail) is list else [app_store_review_detail])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_store_review_attachment: self._set_fields('appStoreReviewAttachments',app_store_review_attachment if type(app_store_review_attachment) is list else [app_store_review_attachment])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'
        APP_STORE_REVIEW_ATTACHMENTS = 'appStoreReviewAttachments'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_review_attachments: int=None) -> AppStoreReviewDetailOfAppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param app_store_review_attachments: maximum number of related appStoreReviewAttachments returned (when they are included). The maximum limit is 50
        :type app_store_review_attachments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreReviewDetailOfAppStoreVersionEndpoint
        '''
        if app_store_review_attachments and app_store_review_attachments > 50:
            raise ValueError(f'The maximum limit of app_store_review_attachments is 50')
        if app_store_review_attachments: self._set_limit(app_store_review_attachments, 'appStoreReviewAttachments')

        return self

    def get(self) -> AppStoreReviewDetailResponse:
        '''Get the resource.

        :returns: Single AppStoreReviewDetail
        :rtype: AppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreReviewDetailResponse.parse_obj(json)

class AppStoreVersionExperimentsLinkagesOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionExperiments'

    def limit(self, number: int=None) -> AppStoreVersionExperimentsLinkagesOfAppStoreVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsLinkagesOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> AppStoreVersionAppStoreVersionExperimentsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionAppStoreVersionExperimentsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppStoreVersionExperimentsLinkagesResponse.parse_obj(json)

class AppStoreVersionExperimentsOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionExperiments'

    class State(StringEnum):
        PREPARE_FOR_SUBMISSION = 'PREPARE_FOR_SUBMISSION'
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        ACCEPTED = 'ACCEPTED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
        COMPLETED = 'COMPLETED'
        STOPPED = 'STOPPED'

    def fields(self, *, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None) -> AppStoreVersionExperimentsOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsOfAppStoreVersionEndpoint
        '''
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'
        APP_STORE_VERSION_EXPERIMENT_TREATMENTS = 'appStoreVersionExperimentTreatments'

    def filter(self, *, state: Union[State, list[State]]=None) -> AppStoreVersionExperimentsOfAppStoreVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsOfAppStoreVersionEndpoint
        '''
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentsOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_store_version_experiment_treatments: int=None) -> AppStoreVersionExperimentsOfAppStoreVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_store_version_experiment_treatments: maximum number of related appStoreVersionExperimentTreatments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_store_version_experiment_treatments and app_store_version_experiment_treatments > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatments is 50')
        if app_store_version_experiment_treatments: self._set_limit(app_store_version_experiment_treatments, 'appStoreVersionExperimentTreatments')

        return self

    @deprecated
    def get(self) -> AppStoreVersionExperimentsResponse:
        '''Get one or more resources.

        :returns: List of AppStoreVersionExperiments
        :rtype: AppStoreVersionExperimentsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentsResponse.parse_obj(json)

class AppStoreVersionExperimentsV2LinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionExperimentsV2'

    def limit(self, number: int=None) -> AppStoreVersionExperimentsV2LinkageOfAppStoreVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2LinkageOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppStoreVersionAppStoreVersionExperimentsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionAppStoreVersionExperimentsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppStoreVersionExperimentsV2LinkagesResponse.parse_obj(json)

class AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionExperimentsV2'

    class State(StringEnum):
        PREPARE_FOR_SUBMISSION = 'PREPARE_FOR_SUBMISSION'
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        ACCEPTED = 'ACCEPTED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
        COMPLETED = 'COMPLETED'
        STOPPED = 'STOPPED'

    def fields(self, *, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app: Union[AppField, list[AppField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None) -> AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint
        '''
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        LATEST_CONTROL_VERSION = 'latestControlVersion'
        CONTROL_VERSIONS = 'controlVersions'
        APP_STORE_VERSION_EXPERIMENT_TREATMENTS = 'appStoreVersionExperimentTreatments'

    def filter(self, *, state: Union[State, list[State]]=None) -> AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint
        '''
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, control_versions: int=None, app_store_version_experiment_treatments: int=None) -> AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param control_versions: maximum number of related controlVersions returned (when they are included). The maximum limit is 50
        :type control_versions: int = None

        :param app_store_version_experiment_treatments: maximum number of related appStoreVersionExperimentTreatments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if control_versions and control_versions > 50:
            raise ValueError(f'The maximum limit of control_versions is 50')
        if control_versions: self._set_limit(control_versions, 'controlVersions')

        if app_store_version_experiment_treatments and app_store_version_experiment_treatments > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatments is 50')
        if app_store_version_experiment_treatments: self._set_limit(app_store_version_experiment_treatments, 'appStoreVersionExperimentTreatments')

        return self

    def get(self) -> AppStoreVersionExperimentsV2Response:
        '''Get one or more resources.

        :returns: List of AppStoreVersionExperiments
        :rtype: AppStoreVersionExperimentsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentsV2Response.parse_obj(json)

class AppStoreVersionLocalizationsLinkagesOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionLocalizations'

    def limit(self, number: int=None) -> AppStoreVersionLocalizationsLinkagesOfAppStoreVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsLinkagesOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppStoreVersionAppStoreVersionLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionAppStoreVersionLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppStoreVersionLocalizationsLinkagesResponse.parse_obj(json)

class AppStoreVersionLocalizationsOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionLocalizations'

    def fields(self, *, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None, app_keyword: Union[AppKeywordField, list[AppKeywordField]]=None) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :param app_keyword: the fields to include for returned resources of type appKeywords
        :type app_keyword: Union[AppKeywordField, list[AppKeywordField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsOfAppStoreVersionEndpoint
        '''
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        if app_keyword: self._set_fields('appKeywords',app_keyword if type(app_keyword) is list else [app_keyword])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'
        APP_SCREENSHOT_SETS = 'appScreenshotSets'
        APP_PREVIEW_SETS = 'appPreviewSets'
        SEARCH_KEYWORDS = 'searchKeywords'

    def filter(self, *, locale: Union[str, list[str]]=None) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsOfAppStoreVersionEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_screenshot_sets: int=None, app_preview_sets: int=None, search_keywords: int=None) -> AppStoreVersionLocalizationsOfAppStoreVersionEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_screenshot_sets: maximum number of related appScreenshotSets returned (when they are included). The maximum limit is 50
        :type app_screenshot_sets: int = None

        :param app_preview_sets: maximum number of related appPreviewSets returned (when they are included). The maximum limit is 50
        :type app_preview_sets: int = None

        :param search_keywords: maximum number of related searchKeywords returned (when they are included). The maximum limit is 50
        :type search_keywords: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionLocalizationsOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_screenshot_sets and app_screenshot_sets > 50:
            raise ValueError(f'The maximum limit of app_screenshot_sets is 50')
        if app_screenshot_sets: self._set_limit(app_screenshot_sets, 'appScreenshotSets')

        if app_preview_sets and app_preview_sets > 50:
            raise ValueError(f'The maximum limit of app_preview_sets is 50')
        if app_preview_sets: self._set_limit(app_preview_sets, 'appPreviewSets')

        if search_keywords and search_keywords > 50:
            raise ValueError(f'The maximum limit of search_keywords is 50')
        if search_keywords: self._set_limit(search_keywords, 'searchKeywords')

        return self

    def get(self) -> AppStoreVersionLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of AppStoreVersionLocalizations
        :rtype: AppStoreVersionLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionLocalizationsResponse.parse_obj(json)

class AppStoreVersionPhasedReleaseLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionPhasedRelease'

    def get(self) -> AppStoreVersionAppStoreVersionPhasedReleaseLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionAppStoreVersionPhasedReleaseLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppStoreVersionPhasedReleaseLinkageResponse.parse_obj(json)

class AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionPhasedRelease'

    def fields(self, *, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None) -> AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_phased_release: the fields to include for returned resources of type appStoreVersionPhasedReleases
        :type app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionPhasedReleaseOfAppStoreVersionEndpoint
        '''
        if app_store_version_phased_release: self._set_fields('appStoreVersionPhasedReleases',app_store_version_phased_release if type(app_store_version_phased_release) is list else [app_store_version_phased_release])
        return self
        
    def get(self) -> AppStoreVersionPhasedReleaseWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single AppStoreVersionPhasedRelease with get
        :rtype: AppStoreVersionPhasedReleaseWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionPhasedReleaseWithoutIncludesResponse.parse_obj(json)

class AppStoreVersionSubmissionLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/appStoreVersionSubmission'

    @deprecated
    def get(self) -> AppStoreVersionAppStoreVersionSubmissionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionAppStoreVersionSubmissionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionAppStoreVersionSubmissionLinkageResponse.parse_obj(json)

class AppStoreVersionSubmissionOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/appStoreVersionSubmission'

    def fields(self, *, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> AppStoreVersionSubmissionOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_submission: the fields to include for returned resources of type appStoreVersionSubmissions
        :type app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionSubmissionOfAppStoreVersionEndpoint
        '''
        if app_store_version_submission: self._set_fields('appStoreVersionSubmissions',app_store_version_submission if type(app_store_version_submission) is list else [app_store_version_submission])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionSubmissionOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionSubmissionOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> AppStoreVersionSubmissionResponse:
        '''Get the resource.

        :returns: Single AppStoreVersionSubmission
        :rtype: AppStoreVersionSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionSubmissionResponse.parse_obj(json)

class BuildLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/build'

    def get(self) -> AppStoreVersionBuildLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionBuildLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionBuildLinkageResponse.parse_obj(json)

    def update(self, request: AppStoreVersionBuildLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: AppStoreVersionBuildLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class BuildOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/build'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfAppStoreVersionEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def get(self) -> BuildWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single Build with get
        :rtype: BuildWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildWithoutIncludesResponse.parse_obj(json)

class CustomerReviewsLinkagesOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/customerReviews'

    def limit(self, number: int=None) -> CustomerReviewsLinkagesOfAppStoreVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsLinkagesOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppStoreVersionCustomerReviewsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionCustomerReviewsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionCustomerReviewsLinkagesResponse.parse_obj(json)

class CustomerReviewsOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/customerReviews'

    class Territory(StringEnum):
        ABW = 'ABW'
        AFG = 'AFG'
        AGO = 'AGO'
        AIA = 'AIA'
        ALB = 'ALB'
        AND = 'AND'
        ANT = 'ANT'
        ARE = 'ARE'
        ARG = 'ARG'
        ARM = 'ARM'
        ASM = 'ASM'
        ATG = 'ATG'
        AUS = 'AUS'
        AUT = 'AUT'
        AZE = 'AZE'
        BDI = 'BDI'
        BEL = 'BEL'
        BEN = 'BEN'
        BES = 'BES'
        BFA = 'BFA'
        BGD = 'BGD'
        BGR = 'BGR'
        BHR = 'BHR'
        BHS = 'BHS'
        BIH = 'BIH'
        BLR = 'BLR'
        BLZ = 'BLZ'
        BMU = 'BMU'
        BOL = 'BOL'
        BRA = 'BRA'
        BRB = 'BRB'
        BRN = 'BRN'
        BTN = 'BTN'
        BWA = 'BWA'
        CAF = 'CAF'
        CAN = 'CAN'
        CHE = 'CHE'
        CHL = 'CHL'
        CHN = 'CHN'
        CIV = 'CIV'
        CMR = 'CMR'
        COD = 'COD'
        COG = 'COG'
        COK = 'COK'
        COL = 'COL'
        COM = 'COM'
        CPV = 'CPV'
        CRI = 'CRI'
        CUB = 'CUB'
        CUW = 'CUW'
        CXR = 'CXR'
        CYM = 'CYM'
        CYP = 'CYP'
        CZE = 'CZE'
        DEU = 'DEU'
        DJI = 'DJI'
        DMA = 'DMA'
        DNK = 'DNK'
        DOM = 'DOM'
        DZA = 'DZA'
        ECU = 'ECU'
        EGY = 'EGY'
        ERI = 'ERI'
        ESP = 'ESP'
        EST = 'EST'
        ETH = 'ETH'
        FIN = 'FIN'
        FJI = 'FJI'
        FLK = 'FLK'
        FRA = 'FRA'
        FRO = 'FRO'
        FSM = 'FSM'
        GAB = 'GAB'
        GBR = 'GBR'
        GEO = 'GEO'
        GGY = 'GGY'
        GHA = 'GHA'
        GIB = 'GIB'
        GIN = 'GIN'
        GLP = 'GLP'
        GMB = 'GMB'
        GNB = 'GNB'
        GNQ = 'GNQ'
        GRC = 'GRC'
        GRD = 'GRD'
        GRL = 'GRL'
        GTM = 'GTM'
        GUF = 'GUF'
        GUM = 'GUM'
        GUY = 'GUY'
        HKG = 'HKG'
        HND = 'HND'
        HRV = 'HRV'
        HTI = 'HTI'
        HUN = 'HUN'
        IDN = 'IDN'
        IMN = 'IMN'
        IND = 'IND'
        IRL = 'IRL'
        IRQ = 'IRQ'
        ISL = 'ISL'
        ISR = 'ISR'
        ITA = 'ITA'
        JAM = 'JAM'
        JEY = 'JEY'
        JOR = 'JOR'
        JPN = 'JPN'
        KAZ = 'KAZ'
        KEN = 'KEN'
        KGZ = 'KGZ'
        KHM = 'KHM'
        KIR = 'KIR'
        KNA = 'KNA'
        KOR = 'KOR'
        KWT = 'KWT'
        LAO = 'LAO'
        LBN = 'LBN'
        LBR = 'LBR'
        LBY = 'LBY'
        LCA = 'LCA'
        LIE = 'LIE'
        LKA = 'LKA'
        LSO = 'LSO'
        LTU = 'LTU'
        LUX = 'LUX'
        LVA = 'LVA'
        MAC = 'MAC'
        MAR = 'MAR'
        MCO = 'MCO'
        MDA = 'MDA'
        MDG = 'MDG'
        MDV = 'MDV'
        MEX = 'MEX'
        MHL = 'MHL'
        MKD = 'MKD'
        MLI = 'MLI'
        MLT = 'MLT'
        MMR = 'MMR'
        MNE = 'MNE'
        MNG = 'MNG'
        MNP = 'MNP'
        MOZ = 'MOZ'
        MRT = 'MRT'
        MSR = 'MSR'
        MTQ = 'MTQ'
        MUS = 'MUS'
        MWI = 'MWI'
        MYS = 'MYS'
        MYT = 'MYT'
        NAM = 'NAM'
        NCL = 'NCL'
        NER = 'NER'
        NFK = 'NFK'
        NGA = 'NGA'
        NIC = 'NIC'
        NIU = 'NIU'
        NLD = 'NLD'
        NOR = 'NOR'
        NPL = 'NPL'
        NRU = 'NRU'
        NZL = 'NZL'
        OMN = 'OMN'
        PAK = 'PAK'
        PAN = 'PAN'
        PER = 'PER'
        PHL = 'PHL'
        PLW = 'PLW'
        PNG = 'PNG'
        POL = 'POL'
        PRI = 'PRI'
        PRT = 'PRT'
        PRY = 'PRY'
        PSE = 'PSE'
        PYF = 'PYF'
        QAT = 'QAT'
        REU = 'REU'
        ROU = 'ROU'
        RUS = 'RUS'
        RWA = 'RWA'
        SAU = 'SAU'
        SEN = 'SEN'
        SGP = 'SGP'
        SHN = 'SHN'
        SLB = 'SLB'
        SLE = 'SLE'
        SLV = 'SLV'
        SMR = 'SMR'
        SOM = 'SOM'
        SPM = 'SPM'
        SRB = 'SRB'
        SSD = 'SSD'
        STP = 'STP'
        SUR = 'SUR'
        SVK = 'SVK'
        SVN = 'SVN'
        SWE = 'SWE'
        SWZ = 'SWZ'
        SXM = 'SXM'
        SYC = 'SYC'
        TCA = 'TCA'
        TCD = 'TCD'
        TGO = 'TGO'
        THA = 'THA'
        TJK = 'TJK'
        TKM = 'TKM'
        TLS = 'TLS'
        TON = 'TON'
        TTO = 'TTO'
        TUN = 'TUN'
        TUR = 'TUR'
        TUV = 'TUV'
        TWN = 'TWN'
        TZA = 'TZA'
        UGA = 'UGA'
        UKR = 'UKR'
        UMI = 'UMI'
        URY = 'URY'
        USA = 'USA'
        UZB = 'UZB'
        VAT = 'VAT'
        VCT = 'VCT'
        VEN = 'VEN'
        VGB = 'VGB'
        VIR = 'VIR'
        VNM = 'VNM'
        VUT = 'VUT'
        WLF = 'WLF'
        WSM = 'WSM'
        XKS = 'XKS'
        YEM = 'YEM'
        ZAF = 'ZAF'
        ZMB = 'ZMB'
        ZWE = 'ZWE'

    def fields(self, *, customer_review: Union[CustomerReviewField, list[CustomerReviewField]]=None, customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]]=None) -> CustomerReviewsOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param customer_review: the fields to include for returned resources of type customerReviews
        :type customer_review: Union[CustomerReviewField, list[CustomerReviewField]] = None

        :param customer_review_response: the fields to include for returned resources of type customerReviewResponses
        :type customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppStoreVersionEndpoint
        '''
        if customer_review: self._set_fields('customerReviews',customer_review if type(customer_review) is list else [customer_review])
        if customer_review_response: self._set_fields('customerReviewResponses',customer_review_response if type(customer_review_response) is list else [customer_review_response])
        return self
        
    class Include(StringEnum):
        RESPONSE = 'response'

    def exists(self, *, published_response: bool=None) -> CustomerReviewsOfAppStoreVersionEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppStoreVersionEndpoint
        '''
        if published_response == None:
            return
        
        self._set_exists('publishedResponse', 'true' if published_response  else 'false')
        return self
        
    def filter(self, *, territory: Union[Territory, list[Territory]]=None, rating: Union[str, list[str]]=None) -> CustomerReviewsOfAppStoreVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by attribute 'territory'
        :type territory: Union[Territory, list[Territory]] = None

        :param rating: filter by attribute 'rating'
        :type rating: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppStoreVersionEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        if rating: self._set_filter('rating', rating if type(rating) is list else [rating])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CustomerReviewsOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, rating: SortOrder=None, created_date: SortOrder=None) -> CustomerReviewsOfAppStoreVersionEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppStoreVersionEndpoint
        '''
        if rating: self.sort_expressions.append('rating' if rating == SortOrder.ASC else '-rating')
        if created_date: self.sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        return self
        
    def limit(self, number: int=None) -> CustomerReviewsOfAppStoreVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppStoreVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CustomerReviewsResponse:
        '''Get one or more resources.

        :returns: List of CustomerReviews
        :rtype: CustomerReviewsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CustomerReviewsResponse.parse_obj(json)

class GameCenterAppVersionLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/gameCenterAppVersion'

    def get(self) -> AppStoreVersionGameCenterAppVersionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionGameCenterAppVersionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionGameCenterAppVersionLinkageResponse.parse_obj(json)

class GameCenterAppVersionOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/gameCenterAppVersion'

    def fields(self, *, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> GameCenterAppVersionOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionOfAppStoreVersionEndpoint
        '''
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        COMPATIBILITY_VERSIONS = 'compatibilityVersions'
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAppVersionOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, compatibility_versions: int=None) -> GameCenterAppVersionOfAppStoreVersionEndpoint:
        '''Number of included related resources to return.

        :param compatibility_versions: maximum number of related compatibilityVersions returned (when they are included). The maximum limit is 50
        :type compatibility_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAppVersionOfAppStoreVersionEndpoint
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

class RoutingAppCoverageLinkageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/relationships/routingAppCoverage'

    def get(self) -> AppStoreVersionRoutingAppCoverageLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppStoreVersionRoutingAppCoverageLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionRoutingAppCoverageLinkageResponse.parse_obj(json)

class RoutingAppCoverageOfAppStoreVersionEndpoint(IDEndpoint):
    path = '/v1/appStoreVersions/{id}/routingAppCoverage'

    def fields(self, *, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> RoutingAppCoverageOfAppStoreVersionEndpoint:
        '''Fields to return for included related types.

        :param routing_app_coverage: the fields to include for returned resources of type routingAppCoverages
        :type routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.RoutingAppCoverageOfAppStoreVersionEndpoint
        '''
        if routing_app_coverage: self._set_fields('routingAppCoverages',routing_app_coverage if type(routing_app_coverage) is list else [routing_app_coverage])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> RoutingAppCoverageOfAppStoreVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.RoutingAppCoverageOfAppStoreVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> RoutingAppCoverageResponse:
        '''Get the resource.

        :returns: Single RoutingAppCoverage
        :rtype: RoutingAppCoverageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return RoutingAppCoverageResponse.parse_obj(json)

