from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiBuildRunsEndpoint(Endpoint):
    path = '/v1/ciBuildRuns'

    def create(self, request: CiBuildRunCreateRequest) -> CiBuildRunResponse:
        '''Create the resource.

        :param request: CiBuildRun representation
        :type request: CiBuildRunCreateRequest

        :returns: Single CiBuildRun
        :rtype: CiBuildRunResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return CiBuildRunResponse.parse_obj(json)

class CiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}'

    @endpoint('/v1/ciBuildRuns/{id}/actions')
    def actions(self) -> ActionsOfCiBuildRunEndpoint:
        return ActionsOfCiBuildRunEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildRuns/{id}/builds')
    def builds(self) -> BuildsOfCiBuildRunEndpoint:
        return BuildsOfCiBuildRunEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildRuns/{id}/relationships/actions')
    def actions_linkages(self) -> ActionsLinkagesOfCiBuildRunEndpoint:
        return ActionsLinkagesOfCiBuildRunEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciBuildRuns/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfCiBuildRunEndpoint:
        return BuildsLinkagesOfCiBuildRunEndpoint(self.id, self.session)
        
    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, build: Union[BuildField, list[BuildField]]=None) -> CiBuildRunEndpoint:
        '''Fields to return for included related types.

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiBuildRunEndpoint
        '''
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    class Include(StringEnum):
        BUILDS = 'builds'
        WORKFLOW = 'workflow'
        PRODUCT = 'product'
        SOURCE_BRANCH_OR_TAG = 'sourceBranchOrTag'
        DESTINATION_BRANCH = 'destinationBranch'
        PULL_REQUEST = 'pullRequest'

    def include(self, relationship: Union[Include, list[Include]]) -> CiBuildRunEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiBuildRunEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, builds: int=None) -> CiBuildRunEndpoint:
        '''Number of included related resources to return.

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.CiBuildRunEndpoint
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

class ActionsLinkagesOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/relationships/actions'

    def limit(self, number: int=None) -> ActionsLinkagesOfCiBuildRunEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ActionsLinkagesOfCiBuildRunEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildRunActionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiBuildRunActionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunActionsLinkagesResponse.parse_obj(json)

class ActionsOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/actions'

    def fields(self, *, ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]]=None, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None) -> ActionsOfCiBuildRunEndpoint:
        '''Fields to return for included related types.

        :param ci_build_action: the fields to include for returned resources of type ciBuildActions
        :type ci_build_action: Union[CiBuildActionField, list[CiBuildActionField]] = None

        :param ci_build_run: the fields to include for returned resources of type ciBuildRuns
        :type ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]] = None

        :returns: self
        :rtype: applaud.endpoints.ActionsOfCiBuildRunEndpoint
        '''
        if ci_build_action: self._set_fields('ciBuildActions',ci_build_action if type(ci_build_action) is list else [ci_build_action])
        if ci_build_run: self._set_fields('ciBuildRuns',ci_build_run if type(ci_build_run) is list else [ci_build_run])
        return self
        
    class Include(StringEnum):
        BUILD_RUN = 'buildRun'

    def include(self, relationship: Union[Include, list[Include]]) -> ActionsOfCiBuildRunEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ActionsOfCiBuildRunEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> ActionsOfCiBuildRunEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ActionsOfCiBuildRunEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildActionsResponse:
        '''Get one or more resources.

        :returns: List of CiBuildActions
        :rtype: CiBuildActionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildActionsResponse.parse_obj(json)

class BuildsLinkagesOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/relationships/builds'

    def limit(self, number: int=None) -> BuildsLinkagesOfCiBuildRunEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsLinkagesOfCiBuildRunEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiBuildRunBuildsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiBuildRunBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiBuildRunBuildsLinkagesResponse.parse_obj(json)

class BuildsOfCiBuildRunEndpoint(IDEndpoint):
    path = '/v1/ciBuildRuns/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, beta_build_localization: Union[BetaBuildLocalizationField, list[BetaBuildLocalizationField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, beta_app_review_submission: Union[BetaAppReviewSubmissionField, list[BetaAppReviewSubmissionField]]=None, app: Union[AppField, list[AppField]]=None, build_beta_detail: Union[BuildBetaDetailField, list[BuildBetaDetailField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None, build_bundle: Union[BuildBundleField, list[BuildBundleField]]=None, build_upload: Union[BuildUploadField, list[BuildUploadField]]=None) -> BuildsOfCiBuildRunEndpoint:
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
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
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

    def exists(self, *, uses_non_exempt_encryption: bool=None) -> BuildsOfCiBuildRunEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if uses_non_exempt_encryption == None:
            return
        
        self._set_exists('usesNonExemptEncryption', 'true' if uses_non_exempt_encryption  else 'false')
        return self
        
    def filter(self, *, version: Union[str, list[str]]=None, expired: Union[str, list[str]]=None, processing_state: Union[BuildProcessingState, list[BuildProcessingState]]=None, beta_app_review_submission_beta_review_state: Union[BetaReviewState, list[BetaReviewState]]=None, uses_non_exempt_encryption: Union[str, list[str]]=None, pre_release_version_version: Union[str, list[str]]=None, pre_release_version_platform: Union[Platform, list[Platform]]=None, build_audience_type: Union[BuildAudienceType, list[BuildAudienceType]]=None, pre_release_version: Union[str, list[str]]=None, app: Union[str, list[str]]=None, beta_groups: Union[str, list[str]]=None, app_store_version: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> BuildsOfCiBuildRunEndpoint:
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
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
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
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildsOfCiBuildRunEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version: SortOrder=None, uploaded_date: SortOrder=None, pre_release_version: SortOrder=None) -> BuildsOfCiBuildRunEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if version: self.sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        if uploaded_date: self.sort_expressions.append('uploadedDate' if uploaded_date == SortOrder.ASC else '-uploadedDate')
        if pre_release_version: self.sort_expressions.append('preReleaseVersion' if pre_release_version == SortOrder.ASC else '-preReleaseVersion')
        return self
        
    def limit(self, number: int=None, *, individual_testers: int=None, beta_groups: int=None, beta_build_localizations: int=None, icons: int=None, build_bundles: int=None) -> BuildsOfCiBuildRunEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

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
        :rtype: applaud.endpoints.BuildsOfCiBuildRunEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
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

    def get(self) -> BuildsResponse:
        '''Get one or more resources.

        :returns: List of Builds
        :rtype: BuildsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildsResponse.parse_obj(json)

