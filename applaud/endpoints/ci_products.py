from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class CiProductsEndpoint(Endpoint):
    path = '/v1/ciProducts'

    def fields(self, *, ci_product: Union[CiProductField, list[CiProductField]]=None, app: Union[AppField, list[AppField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiProductsEndpoint:
        '''Fields to return for included related types.

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID = 'bundleId'
        PRIMARY_REPOSITORIES = 'primaryRepositories'

    def filter(self, *, product_type: Union[CiProductType, list[CiProductType]]=None, app: Union[str, list[str]]=None) -> CiProductsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param product_type: filter by attribute 'productType'
        :type product_type: Union[CiProductType, list[CiProductType]] = None

        :param app: filter by id(s) of related 'app'
        :type app: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if product_type: self._set_filter('productType', product_type if type(product_type) is list else [product_type])
        
        if app: self._set_filter('app', app if type(app) is list else [app])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CiProductsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, primary_repositories: int=None) -> CiProductsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param primary_repositories: maximum number of related primaryRepositories returned (when they are included). The maximum limit is 50
        :type primary_repositories: int = None

        :returns: self
        :rtype: applaud.endpoints.CiProductsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if primary_repositories and primary_repositories > 50:
            raise ValueError(f'The maximum limit of primary_repositories is 50')
        if primary_repositories: self._set_limit(primary_repositories, 'primaryRepositories')

        return self

    def get(self) -> CiProductsResponse:
        '''Get one or more resources.

        :returns: List of CiProducts
        :rtype: CiProductsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductsResponse.parse_obj(json)

    def get_all(self) -> CiProductsResponse:
        '''
        Get all resources.

        :returns: List of CiProducts
        :rtype: CiProductsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiProductsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiProductsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class CiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}'

    @endpoint('/v1/ciProducts/{id}/additionalRepositories')
    def additional_repositories(self) -> AdditionalRepositoriesOfCiProductEndpoint:
        return AdditionalRepositoriesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/app')
    def app(self) -> AppOfCiProductEndpoint:
        return AppOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/buildRuns')
    def build_runs(self) -> BuildRunsOfCiProductEndpoint:
        return BuildRunsOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/primaryRepositories')
    def primary_repositories(self) -> PrimaryRepositoriesOfCiProductEndpoint:
        return PrimaryRepositoriesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/workflows')
    def workflows(self) -> WorkflowsOfCiProductEndpoint:
        return WorkflowsOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/relationships/additionalRepositories')
    def additional_repositories_linkages(self) -> AdditionalRepositoriesLinkagesOfCiProductEndpoint:
        return AdditionalRepositoriesLinkagesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/relationships/app')
    def app_linkage(self) -> AppLinkageOfCiProductEndpoint:
        return AppLinkageOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/relationships/buildRuns')
    def build_runs_linkages(self) -> BuildRunsLinkagesOfCiProductEndpoint:
        return BuildRunsLinkagesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/relationships/primaryRepositories')
    def primary_repositories_linkages(self) -> PrimaryRepositoriesLinkagesOfCiProductEndpoint:
        return PrimaryRepositoriesLinkagesOfCiProductEndpoint(self.id, self.session)
        
    @endpoint('/v1/ciProducts/{id}/relationships/workflows')
    def workflows_linkages(self) -> WorkflowsLinkagesOfCiProductEndpoint:
        return WorkflowsLinkagesOfCiProductEndpoint(self.id, self.session)
        
    def fields(self, *, ci_product: Union[CiProductField, list[CiProductField]]=None, app: Union[AppField, list[AppField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiProductEndpoint:
        '''Fields to return for included related types.

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductEndpoint
        '''
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID = 'bundleId'
        PRIMARY_REPOSITORIES = 'primaryRepositories'

    def include(self, relationship: Union[Include, list[Include]]) -> CiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, primary_repositories: int=None) -> CiProductEndpoint:
        '''Number of included related resources to return.

        :param primary_repositories: maximum number of related primaryRepositories returned (when they are included). The maximum limit is 50
        :type primary_repositories: int = None

        :returns: self
        :rtype: applaud.endpoints.CiProductEndpoint
        '''
        if primary_repositories and primary_repositories > 50:
            raise ValueError(f'The maximum limit of primary_repositories is 50')
        if primary_repositories: self._set_limit(primary_repositories, 'primaryRepositories')

        return self

    def get(self) -> CiProductResponse:
        '''Get the resource.

        :returns: Single CiProduct
        :rtype: CiProductResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductResponse.parse_obj(json)

    def get_all(self) -> CiProductResponse:
        '''
        Get all resources.

        :returns: Single CiProduct
        :rtype: CiProductResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiProductResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiProductResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AdditionalRepositoriesLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/additionalRepositories'

    def limit(self, number: int=None) -> AdditionalRepositoriesLinkagesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesLinkagesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiProductAdditionalRepositoriesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiProductAdditionalRepositoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductAdditionalRepositoriesLinkagesResponse.parse_obj(json)

    def get_all(self) -> CiProductAdditionalRepositoriesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: CiProductAdditionalRepositoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiProductAdditionalRepositoriesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiProductAdditionalRepositoriesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AdditionalRepositoriesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/additionalRepositories'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None, scm_provider: Union[ScmProviderField, list[ScmProviderField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :param scm_provider: the fields to include for returned resources of type scmProviders
        :type scm_provider: Union[ScmProviderField, list[ScmProviderField]] = None

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        if scm_provider: self._set_fields('scmProviders',scm_provider if type(scm_provider) is list else [scm_provider])
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        return self
        
    class Include(StringEnum):
        SCM_PROVIDER = 'scmProvider'
        DEFAULT_BRANCH = 'defaultBranch'

    def filter(self, *, id: Union[str, list[str]]=None) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AdditionalRepositoriesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AdditionalRepositoriesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmRepositoriesResponse:
        '''Get one or more resources.

        :returns: List of ScmRepositories
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoriesResponse.parse_obj(json)

    def get_all(self) -> ScmRepositoriesResponse:
        '''
        Get all resources.

        :returns: List of ScmRepositories
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = ScmRepositoriesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = ScmRepositoriesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppLinkageOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/app'

    def get(self) -> CiProductAppLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: CiProductAppLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductAppLinkageResponse.parse_obj(json)
class AppOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/app'

    def fields(self, *, app: Union[AppField, list[AppField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, build_icon: Union[BuildIconField, list[BuildIconField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app_info: Union[AppInfoField, list[AppInfoField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, app_event: Union[AppEventField, list[AppEventField]]=None, review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]]=None, subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]]=None) -> AppOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param build_icon: the fields to include for returned resources of type buildIcons
        :type build_icon: Union[BuildIconField, list[BuildIconField]] = None

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param end_user_license_agreement: the fields to include for returned resources of type endUserLicenseAgreements
        :type end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param subscription_group: the fields to include for returned resources of type subscriptionGroups
        :type subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]] = None

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :param app_custom_product_page: the fields to include for returned resources of type appCustomProductPages
        :type app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]] = None

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param app_event: the fields to include for returned resources of type appEvents
        :type app_event: Union[AppEventField, list[AppEventField]] = None

        :param review_submission: the fields to include for returned resources of type reviewSubmissions
        :type review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]] = None

        :param subscription_grace_period: the fields to include for returned resources of type subscriptionGracePeriods
        :type subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]] = None

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param android_to_ios_app_mapping_detail: the fields to include for returned resources of type androidToIosAppMappingDetails
        :type android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppOfCiProductEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if build_icon: self._set_fields('buildIcons',build_icon if type(build_icon) is list else [build_icon])
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if end_user_license_agreement: self._set_fields('endUserLicenseAgreements',end_user_license_agreement if type(end_user_license_agreement) is list else [end_user_license_agreement])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if subscription_group: self._set_fields('subscriptionGroups',subscription_group if type(subscription_group) is list else [subscription_group])
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        if app_custom_product_page: self._set_fields('appCustomProductPages',app_custom_product_page if type(app_custom_product_page) is list else [app_custom_product_page])
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if app_event: self._set_fields('appEvents',app_event if type(app_event) is list else [app_event])
        if review_submission: self._set_fields('reviewSubmissions',review_submission if type(review_submission) is list else [review_submission])
        if subscription_grace_period: self._set_fields('subscriptionGracePeriods',subscription_grace_period if type(subscription_grace_period) is list else [subscription_grace_period])
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if android_to_ios_app_mapping_detail: self._set_fields('androidToIosAppMappingDetails',android_to_ios_app_mapping_detail if type(android_to_ios_app_mapping_detail) is list else [android_to_ios_app_mapping_detail])
        return self
        
    class Include(StringEnum):
        APP_ENCRYPTION_DECLARATIONS = 'appEncryptionDeclarations'
        APP_STORE_ICON = 'appStoreIcon'
        CI_PRODUCT = 'ciProduct'
        BETA_GROUPS = 'betaGroups'
        APP_STORE_VERSIONS = 'appStoreVersions'
        PRE_RELEASE_VERSIONS = 'preReleaseVersions'
        BETA_APP_LOCALIZATIONS = 'betaAppLocalizations'
        BUILDS = 'builds'
        BETA_LICENSE_AGREEMENT = 'betaLicenseAgreement'
        BETA_APP_REVIEW_DETAIL = 'betaAppReviewDetail'
        APP_INFOS = 'appInfos'
        APP_CLIPS = 'appClips'
        END_USER_LICENSE_AGREEMENT = 'endUserLicenseAgreement'
        IN_APP_PURCHASES = 'inAppPurchases'
        SUBSCRIPTION_GROUPS = 'subscriptionGroups'
        GAME_CENTER_ENABLED_VERSIONS = 'gameCenterEnabledVersions'
        APP_CUSTOM_PRODUCT_PAGES = 'appCustomProductPages'
        IN_APP_PURCHASES_V2 = 'inAppPurchasesV2'
        PROMOTED_PURCHASES = 'promotedPurchases'
        APP_EVENTS = 'appEvents'
        REVIEW_SUBMISSIONS = 'reviewSubmissions'
        SUBSCRIPTION_GRACE_PERIOD = 'subscriptionGracePeriod'
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        APP_STORE_VERSION_EXPERIMENTS_V2 = 'appStoreVersionExperimentsV2'
        ANDROID_TO_IOS_APP_MAPPING_DETAILS = 'androidToIosAppMappingDetails'

    def include(self, relationship: Union[Include, list[Include]]) -> AppOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_encryption_declarations: int=None, beta_groups: int=None, app_store_versions: int=None, pre_release_versions: int=None, beta_app_localizations: int=None, builds: int=None, app_infos: int=None, app_clips: int=None, in_app_purchases: int=None, subscription_groups: int=None, game_center_enabled_versions: int=None, app_custom_product_pages: int=None, in_app_purchases_v2: int=None, promoted_purchases: int=None, app_events: int=None, review_submissions: int=None, app_store_version_experiments_v2: int=None, android_to_ios_app_mapping_details: int=None) -> AppOfCiProductEndpoint:
        '''Number of included related resources to return.

        :param app_encryption_declarations: maximum number of related appEncryptionDeclarations returned (when they are included). The maximum limit is 50
        :type app_encryption_declarations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param app_store_versions: maximum number of related appStoreVersions returned (when they are included). The maximum limit is 50
        :type app_store_versions: int = None

        :param pre_release_versions: maximum number of related preReleaseVersions returned (when they are included). The maximum limit is 50
        :type pre_release_versions: int = None

        :param beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_localizations: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :param app_infos: maximum number of related appInfos returned (when they are included). The maximum limit is 50
        :type app_infos: int = None

        :param app_clips: maximum number of related appClips returned (when they are included). The maximum limit is 50
        :type app_clips: int = None

        :param in_app_purchases: maximum number of related inAppPurchases returned (when they are included). The maximum limit is 50
        :type in_app_purchases: int = None

        :param subscription_groups: maximum number of related subscriptionGroups returned (when they are included). The maximum limit is 50
        :type subscription_groups: int = None

        :param game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included). The maximum limit is 50
        :type game_center_enabled_versions: int = None

        :param app_custom_product_pages: maximum number of related appCustomProductPages returned (when they are included). The maximum limit is 50
        :type app_custom_product_pages: int = None

        :param in_app_purchases_v2: maximum number of related inAppPurchasesV2 returned (when they are included). The maximum limit is 50
        :type in_app_purchases_v2: int = None

        :param promoted_purchases: maximum number of related promotedPurchases returned (when they are included). The maximum limit is 50
        :type promoted_purchases: int = None

        :param app_events: maximum number of related appEvents returned (when they are included). The maximum limit is 50
        :type app_events: int = None

        :param review_submissions: maximum number of related reviewSubmissions returned (when they are included). The maximum limit is 50
        :type review_submissions: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :param android_to_ios_app_mapping_details: maximum number of related androidToIosAppMappingDetails returned (when they are included). The maximum limit is 50
        :type android_to_ios_app_mapping_details: int = None

        :returns: self
        :rtype: applaud.endpoints.AppOfCiProductEndpoint
        '''
        if app_encryption_declarations and app_encryption_declarations > 50:
            raise ValueError(f'The maximum limit of app_encryption_declarations is 50')
        if app_encryption_declarations: self._set_limit(app_encryption_declarations, 'appEncryptionDeclarations')

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if app_store_versions and app_store_versions > 50:
            raise ValueError(f'The maximum limit of app_store_versions is 50')
        if app_store_versions: self._set_limit(app_store_versions, 'appStoreVersions')

        if pre_release_versions and pre_release_versions > 50:
            raise ValueError(f'The maximum limit of pre_release_versions is 50')
        if pre_release_versions: self._set_limit(pre_release_versions, 'preReleaseVersions')

        if beta_app_localizations and beta_app_localizations > 50:
            raise ValueError(f'The maximum limit of beta_app_localizations is 50')
        if beta_app_localizations: self._set_limit(beta_app_localizations, 'betaAppLocalizations')

        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        if app_infos and app_infos > 50:
            raise ValueError(f'The maximum limit of app_infos is 50')
        if app_infos: self._set_limit(app_infos, 'appInfos')

        if app_clips and app_clips > 50:
            raise ValueError(f'The maximum limit of app_clips is 50')
        if app_clips: self._set_limit(app_clips, 'appClips')

        if in_app_purchases and in_app_purchases > 50:
            raise ValueError(f'The maximum limit of in_app_purchases is 50')
        if in_app_purchases: self._set_limit(in_app_purchases, 'inAppPurchases')

        if subscription_groups and subscription_groups > 50:
            raise ValueError(f'The maximum limit of subscription_groups is 50')
        if subscription_groups: self._set_limit(subscription_groups, 'subscriptionGroups')

        if game_center_enabled_versions and game_center_enabled_versions > 50:
            raise ValueError(f'The maximum limit of game_center_enabled_versions is 50')
        if game_center_enabled_versions: self._set_limit(game_center_enabled_versions, 'gameCenterEnabledVersions')

        if app_custom_product_pages and app_custom_product_pages > 50:
            raise ValueError(f'The maximum limit of app_custom_product_pages is 50')
        if app_custom_product_pages: self._set_limit(app_custom_product_pages, 'appCustomProductPages')

        if in_app_purchases_v2 and in_app_purchases_v2 > 50:
            raise ValueError(f'The maximum limit of in_app_purchases_v2 is 50')
        if in_app_purchases_v2: self._set_limit(in_app_purchases_v2, 'inAppPurchasesV2')

        if promoted_purchases and promoted_purchases > 50:
            raise ValueError(f'The maximum limit of promoted_purchases is 50')
        if promoted_purchases: self._set_limit(promoted_purchases, 'promotedPurchases')

        if app_events and app_events > 50:
            raise ValueError(f'The maximum limit of app_events is 50')
        if app_events: self._set_limit(app_events, 'appEvents')

        if review_submissions and review_submissions > 50:
            raise ValueError(f'The maximum limit of review_submissions is 50')
        if review_submissions: self._set_limit(review_submissions, 'reviewSubmissions')

        if app_store_version_experiments_v2 and app_store_version_experiments_v2 > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments_v2 is 50')
        if app_store_version_experiments_v2: self._set_limit(app_store_version_experiments_v2, 'appStoreVersionExperimentsV2')

        if android_to_ios_app_mapping_details and android_to_ios_app_mapping_details > 50:
            raise ValueError(f'The maximum limit of android_to_ios_app_mapping_details is 50')
        if android_to_ios_app_mapping_details: self._set_limit(android_to_ios_app_mapping_details, 'androidToIosAppMappingDetails')

        return self

    def get(self) -> AppResponse:
        '''Get the resource.

        :returns: Single App
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppResponse.parse_obj(json)

    def get_all(self) -> AppResponse:
        '''
        Get all resources.

        :returns: Single App
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BuildRunsLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/buildRuns'

    def limit(self, number: int=None) -> BuildRunsLinkagesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsLinkagesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiProductBuildRunsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiProductBuildRunsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductBuildRunsLinkagesResponse.parse_obj(json)

    def get_all(self) -> CiProductBuildRunsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: CiProductBuildRunsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiProductBuildRunsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiProductBuildRunsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BuildRunsOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/buildRuns'

    def fields(self, *, ci_build_run: Union[CiBuildRunField, list[CiBuildRunField]]=None, build: Union[BuildField, list[BuildField]]=None, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None, scm_pull_request: Union[ScmPullRequestField, list[ScmPullRequestField]]=None) -> BuildRunsOfCiProductEndpoint:
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
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
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

    def filter(self, *, builds: Union[str, list[str]]=None) -> BuildRunsOfCiProductEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildRunsOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, number: SortOrder=None) -> BuildRunsOfCiProductEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
        '''
        if number: self.sort_expressions.append('number' if number == SortOrder.ASC else '-number')
        return self
        
    def limit(self, number: int=None, *, builds: int=None) -> BuildRunsOfCiProductEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildRunsOfCiProductEndpoint
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

    def get_all(self) -> CiBuildRunsResponse:
        '''
        Get all resources.

        :returns: List of CiBuildRuns
        :rtype: CiBuildRunsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiBuildRunsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiBuildRunsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class PrimaryRepositoriesLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/primaryRepositories'

    def limit(self, number: int=None) -> PrimaryRepositoriesLinkagesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesLinkagesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiProductPrimaryRepositoriesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiProductPrimaryRepositoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductPrimaryRepositoriesLinkagesResponse.parse_obj(json)

    def get_all(self) -> CiProductPrimaryRepositoriesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: CiProductPrimaryRepositoriesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiProductPrimaryRepositoriesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiProductPrimaryRepositoriesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class PrimaryRepositoriesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/primaryRepositories'

    def fields(self, *, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None, scm_provider: Union[ScmProviderField, list[ScmProviderField]]=None, scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]]=None) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :param scm_provider: the fields to include for returned resources of type scmProviders
        :type scm_provider: Union[ScmProviderField, list[ScmProviderField]] = None

        :param scm_git_reference: the fields to include for returned resources of type scmGitReferences
        :type scm_git_reference: Union[ScmGitReferenceField, list[ScmGitReferenceField]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        if scm_provider: self._set_fields('scmProviders',scm_provider if type(scm_provider) is list else [scm_provider])
        if scm_git_reference: self._set_fields('scmGitReferences',scm_git_reference if type(scm_git_reference) is list else [scm_git_reference])
        return self
        
    class Include(StringEnum):
        SCM_PROVIDER = 'scmProvider'
        DEFAULT_BRANCH = 'defaultBranch'

    def filter(self, *, id: Union[str, list[str]]=None) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PrimaryRepositoriesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PrimaryRepositoriesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> ScmRepositoriesResponse:
        '''Get one or more resources.

        :returns: List of ScmRepositories
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ScmRepositoriesResponse.parse_obj(json)

    def get_all(self) -> ScmRepositoriesResponse:
        '''
        Get all resources.

        :returns: List of ScmRepositories
        :rtype: ScmRepositoriesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = ScmRepositoriesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = ScmRepositoriesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class WorkflowsLinkagesOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/relationships/workflows'

    def limit(self, number: int=None) -> WorkflowsLinkagesOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.WorkflowsLinkagesOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiProductWorkflowsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: CiProductWorkflowsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiProductWorkflowsLinkagesResponse.parse_obj(json)

    def get_all(self) -> CiProductWorkflowsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: CiProductWorkflowsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiProductWorkflowsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiProductWorkflowsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class WorkflowsOfCiProductEndpoint(IDEndpoint):
    path = '/v1/ciProducts/{id}/workflows'

    def fields(self, *, ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None, ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]]=None, ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]]=None) -> WorkflowsOfCiProductEndpoint:
        '''Fields to return for included related types.

        :param ci_workflow: the fields to include for returned resources of type ciWorkflows
        :type ci_workflow: Union[CiWorkflowField, list[CiWorkflowField]] = None

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :param ci_xcode_version: the fields to include for returned resources of type ciXcodeVersions
        :type ci_xcode_version: Union[CiXcodeVersionField, list[CiXcodeVersionField]] = None

        :param ci_mac_os_version: the fields to include for returned resources of type ciMacOsVersions
        :type ci_mac_os_version: Union[CiMacOsVersionField, list[CiMacOsVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.WorkflowsOfCiProductEndpoint
        '''
        if ci_workflow: self._set_fields('ciWorkflows',ci_workflow if type(ci_workflow) is list else [ci_workflow])
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        if ci_xcode_version: self._set_fields('ciXcodeVersions',ci_xcode_version if type(ci_xcode_version) is list else [ci_xcode_version])
        if ci_mac_os_version: self._set_fields('ciMacOsVersions',ci_mac_os_version if type(ci_mac_os_version) is list else [ci_mac_os_version])
        return self
        
    class Include(StringEnum):
        PRODUCT = 'product'
        REPOSITORY = 'repository'
        XCODE_VERSION = 'xcodeVersion'
        MAC_OS_VERSION = 'macOsVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> WorkflowsOfCiProductEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.WorkflowsOfCiProductEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> WorkflowsOfCiProductEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.WorkflowsOfCiProductEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CiWorkflowsResponse:
        '''Get one or more resources.

        :returns: List of CiWorkflows
        :rtype: CiWorkflowsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CiWorkflowsResponse.parse_obj(json)

    def get_all(self) -> CiWorkflowsResponse:
        '''
        Get all resources.

        :returns: List of CiWorkflows
        :rtype: CiWorkflowsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CiWorkflowsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CiWorkflowsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

