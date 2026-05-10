from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildsEndpoint(Endpoint):
    path = '/v1/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, app: Union[AppField, list[AppField]]=None, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None) -> BuildsEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

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

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
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

    def exists(self, *, uses_non_exempt_encryption: bool=None) -> BuildsEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if uses_non_exempt_encryption == None:
            return
        
        self._set_exists('usesNonExemptEncryption', 'true' if uses_non_exempt_encryption  else 'false')
        return self
        
    def filter(self, *, version: Union[str, list[str]]=None, expired: Union[str, list[str]]=None, processing_state: Union[BuildProcessingState, list[BuildProcessingState]]=None, beta_app_review_submission_beta_review_state: Union[BetaReviewState, list[BetaReviewState]]=None, uses_non_exempt_encryption: Union[str, list[str]]=None, pre_release_version_version: Union[str, list[str]]=None, pre_release_version_platform: Union[Platform, list[Platform]]=None, build_audience_type: Union[BuildAudienceType, list[BuildAudienceType]]=None, pre_release_version: Union[str, list[str]]=None, app: Union[str, list[str]]=None, beta_groups: Union[str, list[str]]=None, app_store_version: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BuildsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param version: filter by attribute 'version'
        :type version: Union[str, list[str]] = None

        :param expired: filter by attribute 'expired'
        :type expired: Union[str, list[str]] = None

        :param processing_state: filter by attribute 'processingState'
        :type processing_state: Union[BuildProcessingState, list[BuildProcessingState]] = None

        :param beta_app_review_submission_beta_review_state: filter by attribute 'betaAppReviewSubmission.betaReviewState'
        :type beta_app_review_submission_beta_review_state: Union[BetaReviewState, list[BetaReviewState]] = None

        :param uses_non_exempt_encryption: filter by attribute 'usesNonExemptEncryption'
        :type uses_non_exempt_encryption: Union[str, list[str]] = None

        :param pre_release_version_version: filter by attribute 'preReleaseVersion.version'
        :type pre_release_version_version: Union[str, list[str]] = None

        :param pre_release_version_platform: filter by attribute 'preReleaseVersion.platform'
        :type pre_release_version_platform: Union[Platform, list[Platform]] = None

        :param build_audience_type: filter by attribute 'buildAudienceType'
        :type build_audience_type: Union[BuildAudienceType, list[BuildAudienceType]] = None

        :param pre_release_version: filter by id(s) of related 'preReleaseVersion'
        :type pre_release_version: Union[str, list[str]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :param beta_groups: filter by id(s) of related 'betaGroups'
        :type beta_groups: Union[str, list[str]] = None

        :param app_store_version: filter by id(s) of related 'appStoreVersion'
        :type app_store_version: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if version: self._set_filter('version', version if type(version) is list else [version])
        
        if expired: self._set_filter('expired', expired if type(expired) is list else [expired])
        
        if processing_state: self._set_filter('processingState', processing_state if type(processing_state) is list else [processing_state])
        
        if beta_app_review_submission_beta_review_state: self._set_filter('betaAppReviewSubmission.betaReviewState', beta_app_review_submission_beta_review_state if type(beta_app_review_submission_beta_review_state) is list else [beta_app_review_submission_beta_review_state])
        
        if uses_non_exempt_encryption: self._set_filter('usesNonExemptEncryption', uses_non_exempt_encryption if type(uses_non_exempt_encryption) is list else [uses_non_exempt_encryption])
        
        if pre_release_version_version: self._set_filter('preReleaseVersion.version', pre_release_version_version if type(pre_release_version_version) is list else [pre_release_version_version])
        
        if pre_release_version_platform: self._set_filter('preReleaseVersion.platform', pre_release_version_platform if type(pre_release_version_platform) is list else [pre_release_version_platform])
        
        if build_audience_type: self._set_filter('buildAudienceType', build_audience_type if type(build_audience_type) is list else [build_audience_type])
        
        if pre_release_version: self._set_filter('preReleaseVersion', pre_release_version if type(pre_release_version) is list else [pre_release_version])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        if beta_groups: self._set_filter('betaGroups', beta_groups if type(beta_groups) is list else [beta_groups])
        
        if app_store_version: self._set_filter('appStoreVersion', app_store_version if type(app_store_version) is list else [app_store_version])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version: SortOrder=None, uploaded_date: SortOrder=None, pre_release_version: SortOrder=None) -> BuildsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if version: self.sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        if uploaded_date: self.sort_expressions.append('uploadedDate' if uploaded_date == SortOrder.ASC else '-uploadedDate')
        if pre_release_version: self.sort_expressions.append('preReleaseVersion' if pre_release_version == SortOrder.ASC else '-preReleaseVersion')
        return self
        
    def limit(self, number: int=None, *, beta_build_localizations: int=None, beta_groups: int=None, build_bundles: int=None, icons: int=None, individual_testers: int=None) -> BuildsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included). The maximum limit is 50
        :type beta_build_localizations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param build_bundles: maximum number of related buildBundles returned (when they are included). The maximum limit is 50
        :type build_bundles: int = None

        :param icons: maximum number of related icons returned (when they are included). The maximum limit is 50
        :type icons: int = None

        :param individual_testers: maximum number of related individualTesters returned (when they are included). The maximum limit is 50
        :type individual_testers: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if beta_build_localizations and beta_build_localizations > 50:
            raise ValueError(f'The maximum limit of beta_build_localizations is 50')
        if beta_build_localizations: self._set_limit(beta_build_localizations, 'betaBuildLocalizations')

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if build_bundles and build_bundles > 50:
            raise ValueError(f'The maximum limit of build_bundles is 50')
        if build_bundles: self._set_limit(build_bundles, 'buildBundles')

        if icons and icons > 50:
            raise ValueError(f'The maximum limit of icons is 50')
        if icons: self._set_limit(icons, 'icons')

        if individual_testers and individual_testers > 50:
            raise ValueError(f'The maximum limit of individual_testers is 50')
        if individual_testers: self._set_limit(individual_testers, 'individualTesters')

        return self

    def get(self) -> BuildsResponse:
        '''Get one or more resources.

        :returns: List of Builds
        :rtype: BuildsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildsResponse.parse_obj(json)

    def get_all(self) -> BuildsResponse:
        '''
        Get all resources.

        :returns: List of Builds
        :rtype: BuildsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}'

    @endpoint('/v1/builds/{id}/app')
    def app(self) -> AppOfBuildEndpoint:
        return AppOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/appEncryptionDeclaration')
    def app_encryption_declaration(self) -> AppEncryptionDeclarationOfBuildEndpoint:
        return AppEncryptionDeclarationOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/appStoreVersion')
    def app_store_version(self) -> AppStoreVersionOfBuildEndpoint:
        return AppStoreVersionOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/betaAppReviewSubmission')
    def beta_app_review_submission(self) -> BetaAppReviewSubmissionOfBuildEndpoint:
        return BetaAppReviewSubmissionOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/betaBuildLocalizations')
    def beta_build_localizations(self) -> BetaBuildLocalizationsOfBuildEndpoint:
        return BetaBuildLocalizationsOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/buildBetaDetail')
    def build_beta_detail(self) -> BuildBetaDetailOfBuildEndpoint:
        return BuildBetaDetailOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/diagnosticSignatures')
    def diagnostic_signatures(self) -> DiagnosticSignaturesOfBuildEndpoint:
        return DiagnosticSignaturesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/icons')
    def icons(self) -> IconsOfBuildEndpoint:
        return IconsOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/individualTesters')
    def individual_testers(self) -> IndividualTestersOfBuildEndpoint:
        return IndividualTestersOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/perfPowerMetrics')
    def perf_power_metrics(self) -> PerfPowerMetricsOfBuildEndpoint:
        return PerfPowerMetricsOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/preReleaseVersion')
    def pre_release_version(self) -> PreReleaseVersionOfBuildEndpoint:
        return PreReleaseVersionOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/metrics/betaBuildUsages')
    def beta_build_usages(self) -> BetaBuildUsagesOfBuildEndpoint:
        return BetaBuildUsagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/app')
    def app_linkage(self) -> AppLinkageOfBuildEndpoint:
        return AppLinkageOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/appEncryptionDeclaration')
    def app_encryption_declaration_linkage(self) -> AppEncryptionDeclarationLinkageOfBuildEndpoint:
        return AppEncryptionDeclarationLinkageOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/appStoreVersion')
    def app_store_version_linkage(self) -> AppStoreVersionLinkageOfBuildEndpoint:
        return AppStoreVersionLinkageOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/betaAppReviewSubmission')
    def beta_app_review_submission_linkage(self) -> BetaAppReviewSubmissionLinkageOfBuildEndpoint:
        return BetaAppReviewSubmissionLinkageOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/betaBuildLocalizations')
    def beta_build_localizations_linkages(self) -> BetaBuildLocalizationsLinkagesOfBuildEndpoint:
        return BetaBuildLocalizationsLinkagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/betaGroups')
    def beta_groups_linkages(self) -> BetaGroupsLinkagesOfBuildEndpoint:
        return BetaGroupsLinkagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/buildBetaDetail')
    def build_beta_detail_linkage(self) -> BuildBetaDetailLinkageOfBuildEndpoint:
        return BuildBetaDetailLinkageOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/diagnosticSignatures')
    def diagnostic_signatures_linkages(self) -> DiagnosticSignaturesLinkagesOfBuildEndpoint:
        return DiagnosticSignaturesLinkagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/icons')
    def icons_linkages(self) -> IconsLinkagesOfBuildEndpoint:
        return IconsLinkagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/individualTesters')
    def individual_testers_linkages(self) -> IndividualTestersLinkagesOfBuildEndpoint:
        return IndividualTestersLinkagesOfBuildEndpoint(self.id, self.session)
        
    @endpoint('/v1/builds/{id}/relationships/preReleaseVersion')
    def pre_release_version_linkage(self) -> PreReleaseVersionLinkageOfBuildEndpoint:
        return PreReleaseVersionLinkageOfBuildEndpoint(self.id, self.session)
        
    def fields(self, *, build: Union[BuildField, list[BuildField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, app: Union[AppField, list[AppField]]=None, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None) -> BuildEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

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

        :returns: self
        :rtype: applaud.endpoints.BuildEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
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

    def include(self, relationship: Union[Include, list[Include]]) -> BuildEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, beta_build_localizations: int=None, beta_groups: int=None, build_bundles: int=None, icons: int=None, individual_testers: int=None) -> BuildEndpoint:
        '''Number of included related resources to return.

        :param beta_build_localizations: maximum number of related betaBuildLocalizations returned (when they are included). The maximum limit is 50
        :type beta_build_localizations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param build_bundles: maximum number of related buildBundles returned (when they are included). The maximum limit is 50
        :type build_bundles: int = None

        :param icons: maximum number of related icons returned (when they are included). The maximum limit is 50
        :type icons: int = None

        :param individual_testers: maximum number of related individualTesters returned (when they are included). The maximum limit is 50
        :type individual_testers: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildEndpoint
        '''
        if beta_build_localizations and beta_build_localizations > 50:
            raise ValueError(f'The maximum limit of beta_build_localizations is 50')
        if beta_build_localizations: self._set_limit(beta_build_localizations, 'betaBuildLocalizations')

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if build_bundles and build_bundles > 50:
            raise ValueError(f'The maximum limit of build_bundles is 50')
        if build_bundles: self._set_limit(build_bundles, 'buildBundles')

        if icons and icons > 50:
            raise ValueError(f'The maximum limit of icons is 50')
        if icons: self._set_limit(icons, 'icons')

        if individual_testers and individual_testers > 50:
            raise ValueError(f'The maximum limit of individual_testers is 50')
        if individual_testers: self._set_limit(individual_testers, 'individualTesters')

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

    def get_all(self) -> BuildResponse:
        '''
        Get all resources.

        :returns: Single Build
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def update(self, request: BuildUpdateRequest) -> BuildResponse:
        '''Modify the resource.

        :param request: Build representation
        :type request: BuildUpdateRequest

        :returns: Single Build
        :rtype: BuildResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BuildResponse.parse_obj(json)

class AppLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/app'

    def get(self) -> BuildAppLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildAppLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildAppLinkageResponse.parse_obj(json)
class AppOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None) -> AppOfBuildEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfBuildEndpoint
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
class AppEncryptionDeclarationLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/appEncryptionDeclaration'

    def get(self) -> BuildAppEncryptionDeclarationLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildAppEncryptionDeclarationLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildAppEncryptionDeclarationLinkageResponse.parse_obj(json)
    def update(self, request: BuildAppEncryptionDeclarationLinkageRequest):
        '''Modify the resource.

        :param request: Related linkage
        :type request: BuildAppEncryptionDeclarationLinkageRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class AppEncryptionDeclarationOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/appEncryptionDeclaration'

    def fields(self, *, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None) -> AppEncryptionDeclarationOfBuildEndpoint:
        '''Fields to return for included related types.

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationOfBuildEndpoint
        '''
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        return self
        
    def get(self) -> AppEncryptionDeclarationWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single AppEncryptionDeclaration with get
        :rtype: AppEncryptionDeclarationWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEncryptionDeclarationWithoutIncludesResponse.parse_obj(json)
class AppStoreVersionLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/appStoreVersion'

    def get(self) -> BuildAppStoreVersionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildAppStoreVersionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildAppStoreVersionLinkageResponse.parse_obj(json)
class AppStoreVersionOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/appStoreVersion'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app: Union[AppField, list[AppField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None) -> AppStoreVersionOfBuildEndpoint:
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
        :rtype: applaud.endpoints.AppStoreVersionOfBuildEndpoint
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

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionOfBuildEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionOfBuildEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_localizations: int=None, app_store_version_experiments: int=None, app_store_version_experiments_v2: int=None) -> AppStoreVersionOfBuildEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :param app_store_version_experiments: maximum number of related appStoreVersionExperiments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionOfBuildEndpoint
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

    def get_all(self) -> AppStoreVersionResponse:
        '''
        Get all resources.

        :returns: Single AppStoreVersion
        :rtype: AppStoreVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppStoreVersionResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppStoreVersionResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaAppReviewSubmissionLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/betaAppReviewSubmission'

    def get(self) -> BuildBetaAppReviewSubmissionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildBetaAppReviewSubmissionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaAppReviewSubmissionLinkageResponse.parse_obj(json)
class BetaAppReviewSubmissionOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/betaAppReviewSubmission'

    def fields(self, *, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None) -> BetaAppReviewSubmissionOfBuildEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_submission: the fields to include for returned resources of type betaAppReviewSubmissions
        :type beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewSubmissionOfBuildEndpoint
        '''
        if beta_app_review_submission: self._set_fields('betaAppReviewSubmissions',beta_app_review_submission if type(beta_app_review_submission) is list else [beta_app_review_submission])
        return self
        
    def get(self) -> BetaAppReviewSubmissionWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single BetaAppReviewSubmission with get
        :rtype: BetaAppReviewSubmissionWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewSubmissionWithoutIncludesResponse.parse_obj(json)
class BetaBuildLocalizationsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/betaBuildLocalizations'

    def limit(self, number: int=None) -> BetaBuildLocalizationsLinkagesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsLinkagesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildBetaBuildLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BuildBetaBuildLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBetaBuildLocalizationsLinkagesResponse.parse_obj(json)

    def get_all(self) -> BuildBetaBuildLocalizationsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: BuildBetaBuildLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildBetaBuildLocalizationsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildBetaBuildLocalizationsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaBuildLocalizationsOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/betaBuildLocalizations'

    def fields(self, *, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None) -> BetaBuildLocalizationsOfBuildEndpoint:
        '''Fields to return for included related types.

        :param beta_build_localization: the fields to include for returned resources of type betaBuildLocalizations
        :type beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsOfBuildEndpoint
        '''
        if beta_build_localization: self._set_fields('betaBuildLocalizations',beta_build_localization if type(beta_build_localization) is list else [beta_build_localization])
        return self
        
    def limit(self, number: int=None) -> BetaBuildLocalizationsOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildLocalizationsOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaBuildLocalizationsWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of BetaBuildLocalizations with get
        :rtype: BetaBuildLocalizationsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaBuildLocalizationsWithoutIncludesResponse.parse_obj(json)

    def get_all(self) -> BetaBuildLocalizationsWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of BetaBuildLocalizations with get
        :rtype: BetaBuildLocalizationsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaBuildLocalizationsWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaBuildLocalizationsWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaGroupsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/betaGroups'

    def create(self, request: BuildBetaGroupsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BuildBetaGroupsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BuildBetaGroupsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BuildBetaGroupsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildBetaDetailLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/buildBetaDetail'

    def get(self) -> BuildBuildBetaDetailLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildBuildBetaDetailLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildBuildBetaDetailLinkageResponse.parse_obj(json)
class BuildBetaDetailOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/buildBetaDetail'

    def fields(self, *, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, build: Union[BuildField, list[BuildField]]=None) -> BuildBetaDetailOfBuildEndpoint:
        '''Fields to return for included related types.

        :param build_beta_detail: the fields to include for returned resources of type buildBetaDetails
        :type build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailOfBuildEndpoint
        '''
        if build_beta_detail: self._set_fields('buildBetaDetails',build_beta_detail if type(build_beta_detail) is list else [build_beta_detail])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildBetaDetailOfBuildEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildBetaDetailOfBuildEndpoint
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
class DiagnosticSignaturesLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/diagnosticSignatures'

    def limit(self, number: int=None) -> DiagnosticSignaturesLinkagesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesLinkagesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildDiagnosticSignaturesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BuildDiagnosticSignaturesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildDiagnosticSignaturesLinkagesResponse.parse_obj(json)

    def get_all(self) -> BuildDiagnosticSignaturesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: BuildDiagnosticSignaturesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildDiagnosticSignaturesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildDiagnosticSignaturesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class DiagnosticSignaturesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/diagnosticSignatures'

    def fields(self, *, diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]]=None) -> DiagnosticSignaturesOfBuildEndpoint:
        '''Fields to return for included related types.

        :param diagnostic_signature: the fields to include for returned resources of type diagnosticSignatures
        :type diagnostic_signature: Union[DiagnosticSignatureField, list[DiagnosticSignatureField]] = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesOfBuildEndpoint
        '''
        if diagnostic_signature: self._set_fields('diagnosticSignatures',diagnostic_signature if type(diagnostic_signature) is list else [diagnostic_signature])
        return self
        
    def filter(self, *, diagnostic_type: Union[DiagnosticType, list[DiagnosticType]]=None) -> DiagnosticSignaturesOfBuildEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param diagnostic_type: filter by attribute 'diagnosticType'
        :type diagnostic_type: Union[DiagnosticType, list[DiagnosticType]] = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesOfBuildEndpoint
        '''
        if diagnostic_type: self._set_filter('diagnosticType', diagnostic_type if type(diagnostic_type) is list else [diagnostic_type])
        
        return self
        
    def limit(self, number: int=None) -> DiagnosticSignaturesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.DiagnosticSignaturesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> DiagnosticSignaturesResponse:
        '''Get one or more resources.

        :returns: List of DiagnosticSignatures
        :rtype: DiagnosticSignaturesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return DiagnosticSignaturesResponse.parse_obj(json)

    def get_all(self) -> DiagnosticSignaturesResponse:
        '''
        Get all resources.

        :returns: List of DiagnosticSignatures
        :rtype: DiagnosticSignaturesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = DiagnosticSignaturesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = DiagnosticSignaturesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class IconsLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/icons'

    def limit(self, number: int=None) -> IconsLinkagesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IconsLinkagesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildIconsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BuildIconsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildIconsLinkagesResponse.parse_obj(json)

    def get_all(self) -> BuildIconsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: BuildIconsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildIconsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildIconsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class IconsOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/icons'

    def fields(self, *, build_icon: Union[BuildIconField, list[BuildIconField]]=None) -> IconsOfBuildEndpoint:
        '''Fields to return for included related types.

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :returns: self
        :rtype: applaud.endpoints.IconsOfBuildEndpoint
        '''
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        return self
        
    def limit(self, number: int=None) -> IconsOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IconsOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildIconsWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of BuildIcons with get
        :rtype: BuildIconsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildIconsWithoutIncludesResponse.parse_obj(json)

    def get_all(self) -> BuildIconsWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of BuildIcons with get
        :rtype: BuildIconsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildIconsWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildIconsWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class IndividualTestersLinkagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/individualTesters'

    def limit(self, number: int=None) -> IndividualTestersLinkagesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IndividualTestersLinkagesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildIndividualTestersLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BuildIndividualTestersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildIndividualTestersLinkagesResponse.parse_obj(json)

    def get_all(self) -> BuildIndividualTestersLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: BuildIndividualTestersLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildIndividualTestersLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildIndividualTestersLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def create(self, request: BuildIndividualTestersLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: BuildIndividualTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: BuildIndividualTestersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: BuildIndividualTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class IndividualTestersOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/individualTesters'

    def fields(self, *, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None) -> IndividualTestersOfBuildEndpoint:
        '''Fields to return for included related types.

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.IndividualTestersOfBuildEndpoint
        '''
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        return self
        
    def limit(self, number: int=None) -> IndividualTestersOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.IndividualTestersOfBuildEndpoint
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

    def get_all(self) -> BetaTestersWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of BetaTesters with get
        :rtype: BetaTestersWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaTestersWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaTestersWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class PerfPowerMetricsOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/perfPowerMetrics'

    def filter(self, *, platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]]=None, metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]]=None, device_type: Union[str, list[str]]=None) -> PerfPowerMetricsOfBuildEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]] = None

        :param metric_type: filter by attribute 'metricType'
        :type metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]] = None

        :param device_type: filter by attribute 'deviceType'
        :type device_type: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PerfPowerMetricsOfBuildEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if metric_type: self._set_filter('metricType', metric_type if type(metric_type) is list else [metric_type])
        
        if device_type: self._set_filter('deviceType', device_type if type(device_type) is list else [device_type])
        
        return self
        
    def get(self) -> XcodeMetricsResponse:
        '''Get one or more resources.

        :returns: List of PerfPowerMetrics
        :rtype: XcodeMetricsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return XcodeMetricsResponse.parse_obj(json)
class PreReleaseVersionLinkageOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/relationships/preReleaseVersion'

    def get(self) -> BuildPreReleaseVersionLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: BuildPreReleaseVersionLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildPreReleaseVersionLinkageResponse.parse_obj(json)
class PreReleaseVersionOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/preReleaseVersion'

    def fields(self, *, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None) -> PreReleaseVersionOfBuildEndpoint:
        '''Fields to return for included related types.

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionOfBuildEndpoint
        '''
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        return self
        
    def get(self) -> PrereleaseVersionWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single PrereleaseVersion with get
        :rtype: PrereleaseVersionWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PrereleaseVersionWithoutIncludesResponse.parse_obj(json)
class BetaBuildUsagesOfBuildEndpoint(IDEndpoint):
    path = '/v1/builds/{id}/metrics/betaBuildUsages'

    def limit(self, number: int=None) -> BetaBuildUsagesOfBuildEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaBuildUsagesOfBuildEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaBuildUsagesV1MetricResponse:
        '''Get the resource.

        :returns: Metrics data response
        :rtype: BetaBuildUsagesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaBuildUsagesV1MetricResponse.parse_obj(json)

    def get_all(self) -> BetaBuildUsagesV1MetricResponse:
        '''
        Get all resources.

        :returns: Metrics data response
        :rtype: BetaBuildUsagesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaBuildUsagesV1MetricResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaBuildUsagesV1MetricResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

