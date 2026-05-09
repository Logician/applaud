from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildBetaDetailsEndpoint(Endpoint):
    path = '/v1/buildBetaDetails'

    def fields(self, *, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildBetaDetailsEndpoint:
        '''Fields to return for included related types.

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailsEndpoint
        '''
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def filter(self, *, build: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BuildBetaDetailsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param build: filter by id(s) of related 'build'
        :type build: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailsEndpoint
        '''
        if build: self._set_filter('build', build if type(build) is list else [build])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildBetaDetailsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> BuildBetaDetailsEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildBetaDetailsResponse:
        '''Get one or more resources.

        :returns: List of BuildBetaDetails
        :rtype: BuildBetaDetailsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaDetailsResponse.parse_obj(json)

class BuildBetaDetailEndpoint(IDEndpoint):
    path = '/v1/buildBetaDetails/{id}'

    @endpoint('/v1/buildBetaDetails/{id}/build')
    def build(self) -> BuildOfBuildBetaDetailEndpoint:
        return BuildOfBuildBetaDetailEndpoint(self.id, self.session)
        
    @endpoint('/v1/buildBetaDetails/{id}/relationships/build')
    def build_linkage(self) -> BuildLinkageOfBuildBetaDetailEndpoint:
        return BuildLinkageOfBuildBetaDetailEndpoint(self.id, self.session)
        
    def fields(self, *, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildBetaDetailEndpoint:
        '''Fields to return for included related types.

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailEndpoint
        '''
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildBetaDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BuildBetaDetailResponse:
        '''Get the resource.

        :returns: Single BuildBetaDetail
        :rtype: BuildBetaDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaDetailResponse.parse_obj(json)

    def update(self, request: BuildBetaDetailUpdateRequest) -> BuildBetaDetailResponse:
        '''Modify the resource.

        :param request: BuildBetaDetail representation
        :type request: BuildBetaDetailUpdateRequest

        :returns: Single BuildBetaDetail
        :rtype: BuildBetaDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BuildBetaDetailResponse.parse_obj(json)

class BuildLinkageOfBuildBetaDetailEndpoint(IDEndpoint):
    path = '/v1/buildBetaDetails/{id}/relationships/build'

    def get(self) -> BuildBetaDetailBuildLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildBetaDetailBuildLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaDetailBuildLinkageResponse.parse_obj(json)

class BuildOfBuildBetaDetailEndpoint(IDEndpoint):
    path = '/v1/buildBetaDetails/{id}/build'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, app: Union[AppField, list[AppField]]=None, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None, build_bundle: Union[BuildBundleField, list[BuildBundleField]]=None, build_upload: Union[BuildUploadField, list[BuildUploadField]]=None) -> BuildOfBuildBetaDetailEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :param build_bundle: the fields to include for returned resources of type buildBundles
        :type build_bundle: Union[BuildBundleField, list[BuildBundleField]] = None

        :param build_upload: the fields to include for returned resources of type buildUploads
        :type build_upload: Union[BuildUploadField, list[BuildUploadField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfBuildBetaDetailEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        if build_bundle: self._set_fields('buildBundles',build_bundle if type(build_bundle) is list else [build_bundle])
        if build_upload: self._set_fields('buildUploads',build_upload if type(build_upload) is list else [build_upload])
        return self
        
    class Include(StringEnum):
        PRE_RELEASE_VERSION = 'preReleaseVersion'
        INDIVIDUAL_TESTERS = 'individualTesters'
        BETA_GROUPS = 'betaGroups'
        BETA_BUILD_LOCALIZATIONS = 'betaBuildLocalizations'
        APP_ENCRYPTION_DECLARATION = 'appEncryptionDeclaration'
        BETA_APP_REVIEW_SUBMISSION = 'betaAppReviewSubmission'
        APP = 'app'
        BUILD_BETA_DETAIL = 'buildBetaDetail'
        APP_STORE_VERSION = 'appStoreVersion'
        ICONS = 'icons'
        BUILD_BUNDLES = 'buildBundles'
        BUILD_UPLOAD = 'buildUpload'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildOfBuildBetaDetailEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildOfBuildBetaDetailEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, individual_testers: int=None, beta_groups: int=None, beta_build_localizations: int=None, icons: int=None, build_bundles: int=None) -> BuildOfBuildBetaDetailEndpoint:
        '''Number of included related resources to return.

        :param individual_testers: maximum number of related individualTesters returned (when they are included). The maximum limit is 50
        :type individual_testers: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included). The maximum limit is 50
        :type beta_build_localizations: int = None

        :param icons: maximum number of related icons returned (when they are included). The maximum limit is 50
        :type icons: int = None

        :param build_bundles: maximum number of related buildBundles returned (when they are included). The maximum limit is 50
        :type build_bundles: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildOfBuildBetaDetailEndpoint
        '''
        if individual_testers and individual_testers > 50:
            raise ValueError(f'The maximum limit of individual_testers is 50')
        if individual_testers: self._set_limit(individual_testers, 'individualTesters')

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if beta_build_localizations and beta_build_localizations > 50:
            raise ValueError(f'The maximum limit of beta_build_localizations is 50')
        if beta_build_localizations: self._set_limit(beta_build_localizations, 'betaBuildLocalizations')

        if icons and icons > 50:
            raise ValueError(f'The maximum limit of icons is 50')
        if icons: self._set_limit(icons, 'icons')

        if build_bundles and build_bundles > 50:
            raise ValueError(f'The maximum limit of build_bundles is 50')
        if build_bundles: self._set_limit(build_bundles, 'buildBundles')

        return self

    def get(self) -> BuildResponse:
        '''Get the resource.

        :returns: Single Build
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildResponse.parse_obj(json)

