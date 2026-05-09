from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppClipDefaultExperiencesEndpoint(Endpoint):
    path = '/v1/appClipDefaultExperiences'

    def create(self, request: AppClipDefaultExperienceCreateRequest) -> AppClipDefaultExperienceResponse:
        '''Create the resource.

        :param request: AppClipDefaultExperience representation
        :type request: AppClipDefaultExperienceCreateRequest

        :returns: Single AppClipDefaultExperience
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppClipDefaultExperienceResponse.parse_obj(json)

class AppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}'

    @endpoint('/v1/appClipDefaultExperiences/{id}/appClipAppStoreReviewDetail')
    def app_clip_app_store_review_detail(self) -> AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint:
        return AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/appClipDefaultExperienceLocalizations')
    def app_clip_default_experience_localizations(self) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        return AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/releaseWithAppStoreVersion')
    def release_with_app_store_version(self) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        return ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/relationships/appClipAppStoreReviewDetail')
    def app_clip_app_store_review_detail_linkage(self) -> AppClipAppStoreReviewDetailLinkageOfAppClipDefaultExperienceEndpoint:
        return AppClipAppStoreReviewDetailLinkageOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/relationships/appClipDefaultExperienceLocalizations')
    def app_clip_default_experience_localizations_linkages(self) -> AppClipDefaultExperienceLocalizationsLinkagesOfAppClipDefaultExperienceEndpoint:
        return AppClipDefaultExperienceLocalizationsLinkagesOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    @endpoint('/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion')
    def release_with_app_store_version_linkage(self) -> ReleaseWithAppStoreVersionLinkageOfAppClipDefaultExperienceEndpoint:
        return ReleaseWithAppStoreVersionLinkageOfAppClipDefaultExperienceEndpoint(self.id, self.session)
        
    def fields(self, *, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None, app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]]=None) -> AppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :param app_clip_app_store_review_detail: the fields to include for returned resources of type appClipAppStoreReviewDetails
        :type app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceEndpoint
        '''
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        if app_clip_app_store_review_detail: self._set_fields('appClipAppStoreReviewDetails',app_clip_app_store_review_detail if type(app_clip_app_store_review_detail) is list else [app_clip_app_store_review_detail])
        return self
        
    class Include(StringEnum):
        APP_CLIP = 'appClip'
        RELEASE_WITH_APP_STORE_VERSION = 'releaseWithAppStoreVersion'
        APP_CLIP_DEFAULT_EXPERIENCE_LOCALIZATIONS = 'appClipDefaultExperienceLocalizations'
        APP_CLIP_APP_STORE_REVIEW_DETAIL = 'appClipAppStoreReviewDetail'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_clip_default_experience_localizations: int=None) -> AppClipDefaultExperienceEndpoint:
        '''Number of included related resources to return.

        :param app_clip_default_experience_localizations: maximum number of related appClipDefaultExperienceLocalizations returned (when they are included). The maximum limit is 50
        :type app_clip_default_experience_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceEndpoint
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

    def update(self, request: AppClipDefaultExperienceUpdateRequest) -> AppClipDefaultExperienceResponse:
        '''Modify the resource.

        :param request: AppClipDefaultExperience representation
        :type request: AppClipDefaultExperienceUpdateRequest

        :returns: Single AppClipDefaultExperience
        :rtype: AppClipDefaultExperienceResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppClipDefaultExperienceResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppClipAppStoreReviewDetailLinkageOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/relationships/appClipAppStoreReviewDetail'

    def get(self) -> AppClipDefaultExperienceAppClipAppStoreReviewDetailLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppClipDefaultExperienceAppClipAppStoreReviewDetailLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceAppClipAppStoreReviewDetailLinkageResponse.parse_obj(json)

class AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/appClipAppStoreReviewDetail'

    def fields(self, *, app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None) -> AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_app_store_review_detail: the fields to include for returned resources of type appClipAppStoreReviewDetails
        :type app_clip_app_store_review_detail: Union[AppClipAppStoreReviewDetailField, list[AppClipAppStoreReviewDetailField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint
        '''
        if app_clip_app_store_review_detail: self._set_fields('appClipAppStoreReviewDetails',app_clip_app_store_review_detail if type(app_clip_app_store_review_detail) is list else [app_clip_app_store_review_detail])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'

    def include(self, relationship: Union[Include, list[Include]]) -> AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipAppStoreReviewDetailOfAppClipDefaultExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> AppClipAppStoreReviewDetailResponse:
        '''Get the resource.

        :returns: Single AppClipAppStoreReviewDetail
        :rtype: AppClipAppStoreReviewDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipAppStoreReviewDetailResponse.parse_obj(json)

class AppClipDefaultExperienceLocalizationsLinkagesOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/relationships/appClipDefaultExperienceLocalizations'

    def limit(self, number: int=None) -> AppClipDefaultExperienceLocalizationsLinkagesOfAppClipDefaultExperienceEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsLinkagesOfAppClipDefaultExperienceEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppClipDefaultExperienceAppClipDefaultExperienceLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppClipDefaultExperienceAppClipDefaultExperienceLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceAppClipDefaultExperienceLocalizationsLinkagesResponse.parse_obj(json)

class AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/appClipDefaultExperienceLocalizations'

    def fields(self, *, app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]]=None) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Fields to return for included related types.

        :param app_clip_default_experience_localization: the fields to include for returned resources of type appClipDefaultExperienceLocalizations
        :type app_clip_default_experience_localization: Union[AppClipDefaultExperienceLocalizationField, list[AppClipDefaultExperienceLocalizationField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :param app_clip_header_image: the fields to include for returned resources of type appClipHeaderImages
        :type app_clip_header_image: Union[AppClipHeaderImageField, list[AppClipHeaderImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if app_clip_default_experience_localization: self._set_fields('appClipDefaultExperienceLocalizations',app_clip_default_experience_localization if type(app_clip_default_experience_localization) is list else [app_clip_default_experience_localization])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        if app_clip_header_image: self._set_fields('appClipHeaderImages',app_clip_header_image if type(app_clip_header_image) is list else [app_clip_header_image])
        return self
        
    class Include(StringEnum):
        APP_CLIP_DEFAULT_EXPERIENCE = 'appClipDefaultExperience'
        APP_CLIP_HEADER_IMAGE = 'appClipHeaderImage'

    def filter(self, *, locale: Union[str, list[str]]=None) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipDefaultExperienceLocalizationsOfAppClipDefaultExperienceEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppClipDefaultExperienceLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of AppClipDefaultExperienceLocalizations
        :rtype: AppClipDefaultExperienceLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceLocalizationsResponse.parse_obj(json)

class ReleaseWithAppStoreVersionLinkageOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/relationships/releaseWithAppStoreVersion'

    def get(self) -> AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageResponse.parse_obj(json)

    def update(self, request: AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: AppClipDefaultExperienceReleaseWithAppStoreVersionLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint(IDEndpoint):
    path = '/v1/appClipDefaultExperiences/{id}/releaseWithAppStoreVersion'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app: Union[AppField, list[AppField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
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
        :rtype: applaud.endpoints.ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_localizations: int=None, app_store_version_experiments: int=None, app_store_version_experiments_v2: int=None) -> ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :param app_store_version_experiments: maximum number of related appStoreVersionExperiments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :returns: self
        :rtype: applaud.endpoints.ReleaseWithAppStoreVersionOfAppClipDefaultExperienceEndpoint
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

