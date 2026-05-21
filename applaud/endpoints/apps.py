from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppsEndpoint(Endpoint):
    path = '/v1/apps'

    class ReviewSubmissions_state(StringEnum):
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        UNRESOLVED_ISSUES = 'UNRESOLVED_ISSUES'
        CANCELING = 'CANCELING'
        COMPLETING = 'COMPLETING'
        COMPLETE = 'COMPLETE'

    class ReviewSubmissions_platform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, app: Union[AppField, list[AppField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app_info: Union[AppInfoField, list[AppInfoField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, app_event: Union[AppEventField, list[AppEventField]]=None, review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]]=None, subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]]=None) -> AppsEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

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
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
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

    def exists(self, *, game_center_enabled_versions: bool=None) -> AppsEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if game_center_enabled_versions == None:
            return
        
        self._set_exists('gameCenterEnabledVersions', 'true' if game_center_enabled_versions  else 'false')
        return self
        
    def filter(self, *, name: Union[str, list[str]]=None, bundle_id: Union[str, list[str]]=None, sku: Union[str, list[str]]=None, app_store_versions_app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]]=None, app_store_versions_platform: Union[Platform, list[Platform]]=None, app_store_versions_app_version_state: Union[AppVersionState, list[AppVersionState]]=None, review_submissions_state: Union[ReviewSubmissions_state, list[ReviewSubmissions_state]]=None, review_submissions_platform: Union[ReviewSubmissions_platform, list[ReviewSubmissions_platform]]=None, app_store_versions: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> AppsEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param bundle_id: filter by attribute 'bundleId'
        :type bundle_id: Union[str, list[str]] = None

        :param sku: filter by attribute 'sku'
        :type sku: Union[str, list[str]] = None

        :param app_store_versions_app_store_state: filter by attribute 'appStoreVersions.appStoreState'
        :type app_store_versions_app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]] = None

        :param app_store_versions_platform: filter by attribute 'appStoreVersions.platform'
        :type app_store_versions_platform: Union[Platform, list[Platform]] = None

        :param app_store_versions_app_version_state: filter by attribute 'appStoreVersions.appVersionState'
        :type app_store_versions_app_version_state: Union[AppVersionState, list[AppVersionState]] = None

        :param review_submissions_state: filter by attribute 'reviewSubmissions.state'
        :type review_submissions_state: Union[ReviewSubmissions_state, list[ReviewSubmissions_state]] = None

        :param review_submissions_platform: filter by attribute 'reviewSubmissions.platform'
        :type review_submissions_platform: Union[ReviewSubmissions_platform, list[ReviewSubmissions_platform]] = None

        :param app_store_versions: filter by id(s) of related 'appStoreVersions'
        :type app_store_versions: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if bundle_id: self._set_filter('bundleId', bundle_id if type(bundle_id) is list else [bundle_id])
        
        if sku: self._set_filter('sku', sku if type(sku) is list else [sku])
        
        if app_store_versions_app_store_state: self._set_filter('appStoreVersions.appStoreState', app_store_versions_app_store_state if type(app_store_versions_app_store_state) is list else [app_store_versions_app_store_state])
        
        if app_store_versions_platform: self._set_filter('appStoreVersions.platform', app_store_versions_platform if type(app_store_versions_platform) is list else [app_store_versions_platform])
        
        if app_store_versions_app_version_state: self._set_filter('appStoreVersions.appVersionState', app_store_versions_app_version_state if type(app_store_versions_app_version_state) is list else [app_store_versions_app_version_state])
        
        if review_submissions_state: self._set_filter('reviewSubmissions.state', review_submissions_state if type(review_submissions_state) is list else [review_submissions_state])
        
        if review_submissions_platform: self._set_filter('reviewSubmissions.platform', review_submissions_platform if type(review_submissions_platform) is list else [review_submissions_platform])
        
        if app_store_versions: self._set_filter('appStoreVersions', app_store_versions if type(app_store_versions) is list else [app_store_versions])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppsEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None, bundle_id: SortOrder=None, sku: SortOrder=None) -> AppsEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        sort_expressions = []
        if name: sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if bundle_id: sort_expressions.append('bundleId' if bundle_id == SortOrder.ASC else '-bundleId')
        if sku: sort_expressions.append('sku' if sku == SortOrder.ASC else '-sku')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None, *, android_to_ios_app_mapping_details: int=None, app_clips: int=None, app_custom_product_pages: int=None, app_encryption_declarations: int=None, app_events: int=None, app_infos: int=None, app_store_version_experiments_v2: int=None, app_store_versions: int=None, beta_app_localizations: int=None, beta_groups: int=None, builds: int=None, game_center_enabled_versions: int=None, in_app_purchases: int=None, in_app_purchases_v2: int=None, pre_release_versions: int=None, promoted_purchases: int=None, review_submissions: int=None, subscription_groups: int=None) -> AppsEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param android_to_ios_app_mapping_details: maximum number of related androidToIosAppMappingDetails returned (when they are included). The maximum limit is 50
        :type android_to_ios_app_mapping_details: int = None

        :param app_clips: maximum number of related appClips returned (when they are included). The maximum limit is 50
        :type app_clips: int = None

        :param app_custom_product_pages: maximum number of related appCustomProductPages returned (when they are included). The maximum limit is 50
        :type app_custom_product_pages: int = None

        :param app_encryption_declarations: maximum number of related appEncryptionDeclarations returned (when they are included). The maximum limit is 50
        :type app_encryption_declarations: int = None

        :param app_events: maximum number of related appEvents returned (when they are included). The maximum limit is 50
        :type app_events: int = None

        :param app_infos: maximum number of related appInfos returned (when they are included). The maximum limit is 50
        :type app_infos: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :param app_store_versions: maximum number of related appStoreVersions returned (when they are included). The maximum limit is 50
        :type app_store_versions: int = None

        :param beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_localizations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :param game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included). The maximum limit is 50
        :type game_center_enabled_versions: int = None

        :param in_app_purchases: maximum number of related inAppPurchases returned (when they are included). The maximum limit is 50
        :type in_app_purchases: int = None

        :param in_app_purchases_v2: maximum number of related inAppPurchasesV2 returned (when they are included). The maximum limit is 50
        :type in_app_purchases_v2: int = None

        :param pre_release_versions: maximum number of related preReleaseVersions returned (when they are included). The maximum limit is 50
        :type pre_release_versions: int = None

        :param promoted_purchases: maximum number of related promotedPurchases returned (when they are included). The maximum limit is 50
        :type promoted_purchases: int = None

        :param review_submissions: maximum number of related reviewSubmissions returned (when they are included). The maximum limit is 50
        :type review_submissions: int = None

        :param subscription_groups: maximum number of related subscriptionGroups returned (when they are included). The maximum limit is 50
        :type subscription_groups: int = None

        :returns: self
        :rtype: applaud.endpoints.AppsEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if android_to_ios_app_mapping_details and android_to_ios_app_mapping_details > 50:
            raise ValueError(f'The maximum limit of android_to_ios_app_mapping_details is 50')
        if android_to_ios_app_mapping_details: self._set_limit(android_to_ios_app_mapping_details, 'androidToIosAppMappingDetails')

        if app_clips and app_clips > 50:
            raise ValueError(f'The maximum limit of app_clips is 50')
        if app_clips: self._set_limit(app_clips, 'appClips')

        if app_custom_product_pages and app_custom_product_pages > 50:
            raise ValueError(f'The maximum limit of app_custom_product_pages is 50')
        if app_custom_product_pages: self._set_limit(app_custom_product_pages, 'appCustomProductPages')

        if app_encryption_declarations and app_encryption_declarations > 50:
            raise ValueError(f'The maximum limit of app_encryption_declarations is 50')
        if app_encryption_declarations: self._set_limit(app_encryption_declarations, 'appEncryptionDeclarations')

        if app_events and app_events > 50:
            raise ValueError(f'The maximum limit of app_events is 50')
        if app_events: self._set_limit(app_events, 'appEvents')

        if app_infos and app_infos > 50:
            raise ValueError(f'The maximum limit of app_infos is 50')
        if app_infos: self._set_limit(app_infos, 'appInfos')

        if app_store_version_experiments_v2 and app_store_version_experiments_v2 > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments_v2 is 50')
        if app_store_version_experiments_v2: self._set_limit(app_store_version_experiments_v2, 'appStoreVersionExperimentsV2')

        if app_store_versions and app_store_versions > 50:
            raise ValueError(f'The maximum limit of app_store_versions is 50')
        if app_store_versions: self._set_limit(app_store_versions, 'appStoreVersions')

        if beta_app_localizations and beta_app_localizations > 50:
            raise ValueError(f'The maximum limit of beta_app_localizations is 50')
        if beta_app_localizations: self._set_limit(beta_app_localizations, 'betaAppLocalizations')

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        if game_center_enabled_versions and game_center_enabled_versions > 50:
            raise ValueError(f'The maximum limit of game_center_enabled_versions is 50')
        if game_center_enabled_versions: self._set_limit(game_center_enabled_versions, 'gameCenterEnabledVersions')

        if in_app_purchases and in_app_purchases > 50:
            raise ValueError(f'The maximum limit of in_app_purchases is 50')
        if in_app_purchases: self._set_limit(in_app_purchases, 'inAppPurchases')

        if in_app_purchases_v2 and in_app_purchases_v2 > 50:
            raise ValueError(f'The maximum limit of in_app_purchases_v2 is 50')
        if in_app_purchases_v2: self._set_limit(in_app_purchases_v2, 'inAppPurchasesV2')

        if pre_release_versions and pre_release_versions > 50:
            raise ValueError(f'The maximum limit of pre_release_versions is 50')
        if pre_release_versions: self._set_limit(pre_release_versions, 'preReleaseVersions')

        if promoted_purchases and promoted_purchases > 50:
            raise ValueError(f'The maximum limit of promoted_purchases is 50')
        if promoted_purchases: self._set_limit(promoted_purchases, 'promotedPurchases')

        if review_submissions and review_submissions > 50:
            raise ValueError(f'The maximum limit of review_submissions is 50')
        if review_submissions: self._set_limit(review_submissions, 'reviewSubmissions')

        if subscription_groups and subscription_groups > 50:
            raise ValueError(f'The maximum limit of subscription_groups is 50')
        if subscription_groups: self._set_limit(subscription_groups, 'subscriptionGroups')

        return self

    def get(self) -> AppsResponse:
        '''Get one or more resources.

        :returns: List of Apps
        :rtype: AppsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppsResponse.parse_obj(json)

    def get_all(self) -> AppsResponse:
        '''
        Get all resources.

        :returns: List of Apps
        :rtype: AppsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}'

    @endpoint('/v1/apps/{id}/accessibilityDeclarations')
    def accessibility_declarations(self) -> AccessibilityDeclarationsOfAppEndpoint:
        return AccessibilityDeclarationsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/alternativeDistributionKey')
    def alternative_distribution_key(self) -> AlternativeDistributionKeyOfAppEndpoint:
        return AlternativeDistributionKeyOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/analyticsReportRequests')
    def analytics_report_requests(self) -> AnalyticsReportRequestsOfAppEndpoint:
        return AnalyticsReportRequestsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/androidToIosAppMappingDetails')
    def android_to_ios_app_mapping_details(self) -> AndroidToIosAppMappingDetailsOfAppEndpoint:
        return AndroidToIosAppMappingDetailsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appAvailabilityV2')
    def app_availability_v2(self) -> AppAvailabilityV2OfAppEndpoint:
        return AppAvailabilityV2OfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appClips')
    def app_clips(self) -> AppClipsOfAppEndpoint:
        return AppClipsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appCustomProductPages')
    def app_custom_product_pages(self) -> AppCustomProductPagesOfAppEndpoint:
        return AppCustomProductPagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appEncryptionDeclarations')
    def app_encryption_declarations(self) -> AppEncryptionDeclarationsOfAppEndpoint:
        return AppEncryptionDeclarationsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appEvents')
    def app_events(self) -> AppEventsOfAppEndpoint:
        return AppEventsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appInfos')
    def app_infos(self) -> AppInfosOfAppEndpoint:
        return AppInfosOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appPricePoints')
    def app_price_points(self) -> AppPricePointsOfAppEndpoint:
        return AppPricePointsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appPriceSchedule')
    def app_price_schedule(self) -> AppPriceScheduleOfAppEndpoint:
        return AppPriceScheduleOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appStoreVersionExperimentsV2')
    def app_store_version_experiments_v2(self) -> AppStoreVersionExperimentsV2OfAppEndpoint:
        return AppStoreVersionExperimentsV2OfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appStoreVersions')
    def app_store_versions(self) -> AppStoreVersionsOfAppEndpoint:
        return AppStoreVersionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/appTags')
    def app_tags(self) -> AppTagsOfAppEndpoint:
        return AppTagsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/backgroundAssets')
    def background_assets(self) -> BackgroundAssetsOfAppEndpoint:
        return BackgroundAssetsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaAppLocalizations')
    def beta_app_localizations(self) -> BetaAppLocalizationsOfAppEndpoint:
        return BetaAppLocalizationsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaAppReviewDetail')
    def beta_app_review_detail(self) -> BetaAppReviewDetailOfAppEndpoint:
        return BetaAppReviewDetailOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaFeedbackCrashSubmissions')
    def beta_feedback_crash_submissions(self) -> BetaFeedbackCrashSubmissionsOfAppEndpoint:
        return BetaFeedbackCrashSubmissionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaFeedbackScreenshotSubmissions')
    def beta_feedback_screenshot_submissions(self) -> BetaFeedbackScreenshotSubmissionsOfAppEndpoint:
        return BetaFeedbackScreenshotSubmissionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaGroups')
    def beta_groups(self) -> BetaGroupsOfAppEndpoint:
        return BetaGroupsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/betaLicenseAgreement')
    def beta_license_agreement(self) -> BetaLicenseAgreementOfAppEndpoint:
        return BetaLicenseAgreementOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/buildUploads')
    def build_uploads(self) -> BuildUploadsOfAppEndpoint:
        return BuildUploadsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/builds')
    def builds(self) -> BuildsOfAppEndpoint:
        return BuildsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/ciProduct')
    def ci_product(self) -> CiProductOfAppEndpoint:
        return CiProductOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/customerReviewSummarizations')
    def customer_review_summarizations(self) -> CustomerReviewSummarizationsOfAppEndpoint:
        return CustomerReviewSummarizationsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/customerReviews')
    def customer_reviews(self) -> CustomerReviewsOfAppEndpoint:
        return CustomerReviewsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/endUserLicenseAgreement')
    def end_user_license_agreement(self) -> EndUserLicenseAgreementOfAppEndpoint:
        return EndUserLicenseAgreementOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/gameCenterDetail')
    def game_center_detail(self) -> GameCenterDetailOfAppEndpoint:
        return GameCenterDetailOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/gameCenterEnabledVersions')
    def game_center_enabled_versions(self) -> GameCenterEnabledVersionsOfAppEndpoint:
        return GameCenterEnabledVersionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/inAppPurchases')
    def in_app_purchases(self) -> InAppPurchasesOfAppEndpoint:
        return InAppPurchasesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/inAppPurchasesV2')
    def in_app_purchases_v2(self) -> InAppPurchasesV2OfAppEndpoint:
        return InAppPurchasesV2OfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/marketplaceSearchDetail')
    def marketplace_search_detail(self) -> MarketplaceSearchDetailOfAppEndpoint:
        return MarketplaceSearchDetailOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/perfPowerMetrics')
    def perf_power_metrics(self) -> PerfPowerMetricsOfAppEndpoint:
        return PerfPowerMetricsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/preReleaseVersions')
    def pre_release_versions(self) -> PreReleaseVersionsOfAppEndpoint:
        return PreReleaseVersionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/promotedPurchases')
    def promoted_purchases(self) -> PromotedPurchasesOfAppEndpoint:
        return PromotedPurchasesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/reviewSubmissions')
    def review_submissions(self) -> ReviewSubmissionsOfAppEndpoint:
        return ReviewSubmissionsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/searchKeywords')
    def search_keywords(self) -> SearchKeywordsOfAppEndpoint:
        return SearchKeywordsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/subscriptionGracePeriod')
    def subscription_grace_period(self) -> SubscriptionGracePeriodOfAppEndpoint:
        return SubscriptionGracePeriodOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/subscriptionGroups')
    def subscription_groups(self) -> SubscriptionGroupsOfAppEndpoint:
        return SubscriptionGroupsOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/webhooks')
    def webhooks(self) -> WebhooksOfAppEndpoint:
        return WebhooksOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/metrics/betaTesterUsages')
    def beta_tester_usages(self) -> BetaTesterUsagesOfAppEndpoint:
        return BetaTesterUsagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/accessibilityDeclarations')
    def accessibility_declarations_linkages(self) -> AccessibilityDeclarationsLinkagesOfAppEndpoint:
        return AccessibilityDeclarationsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/alternativeDistributionKey')
    def alternative_distribution_key_linkage(self) -> AlternativeDistributionKeyLinkageOfAppEndpoint:
        return AlternativeDistributionKeyLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/analyticsReportRequests')
    def analytics_report_requests_linkages(self) -> AnalyticsReportRequestsLinkagesOfAppEndpoint:
        return AnalyticsReportRequestsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/androidToIosAppMappingDetails')
    def android_to_ios_app_mapping_details_linkages(self) -> AndroidToIosAppMappingDetailsLinkagesOfAppEndpoint:
        return AndroidToIosAppMappingDetailsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appAvailabilityV2')
    def app_availability_v2_linkage(self) -> AppAvailabilityV2LinkageOfAppEndpoint:
        return AppAvailabilityV2LinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appClips')
    def app_clips_linkages(self) -> AppClipsLinkagesOfAppEndpoint:
        return AppClipsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appCustomProductPages')
    def app_custom_product_pages_linkages(self) -> AppCustomProductPagesLinkagesOfAppEndpoint:
        return AppCustomProductPagesLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appEncryptionDeclarations')
    def app_encryption_declarations_linkages(self) -> AppEncryptionDeclarationsLinkagesOfAppEndpoint:
        return AppEncryptionDeclarationsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appEvents')
    def app_events_linkages(self) -> AppEventsLinkagesOfAppEndpoint:
        return AppEventsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appInfos')
    def app_infos_linkages(self) -> AppInfosLinkagesOfAppEndpoint:
        return AppInfosLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appPricePoints')
    def app_price_points_linkages(self) -> AppPricePointsLinkagesOfAppEndpoint:
        return AppPricePointsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appPriceSchedule')
    def app_price_schedule_linkage(self) -> AppPriceScheduleLinkageOfAppEndpoint:
        return AppPriceScheduleLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appStoreVersionExperimentsV2')
    def app_store_version_experiments_v2_linkage(self) -> AppStoreVersionExperimentsV2LinkageOfAppEndpoint:
        return AppStoreVersionExperimentsV2LinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appStoreVersions')
    def app_store_versions_linkages(self) -> AppStoreVersionsLinkagesOfAppEndpoint:
        return AppStoreVersionsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/appTags')
    def app_tags_linkages(self) -> AppTagsLinkagesOfAppEndpoint:
        return AppTagsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/backgroundAssets')
    def background_assets_linkages(self) -> BackgroundAssetsLinkagesOfAppEndpoint:
        return BackgroundAssetsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaAppLocalizations')
    def beta_app_localizations_linkages(self) -> BetaAppLocalizationsLinkagesOfAppEndpoint:
        return BetaAppLocalizationsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaAppReviewDetail')
    def beta_app_review_detail_linkage(self) -> BetaAppReviewDetailLinkageOfAppEndpoint:
        return BetaAppReviewDetailLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaFeedbackCrashSubmissions')
    def beta_feedback_crash_submissions_linkages(self) -> BetaFeedbackCrashSubmissionsLinkagesOfAppEndpoint:
        return BetaFeedbackCrashSubmissionsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaFeedbackScreenshotSubmissions')
    def beta_feedback_screenshot_submissions_linkages(self) -> BetaFeedbackScreenshotSubmissionsLinkagesOfAppEndpoint:
        return BetaFeedbackScreenshotSubmissionsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaGroups')
    def beta_groups_linkages(self) -> BetaGroupsLinkagesOfAppEndpoint:
        return BetaGroupsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaLicenseAgreement')
    def beta_license_agreement_linkage(self) -> BetaLicenseAgreementLinkageOfAppEndpoint:
        return BetaLicenseAgreementLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/betaTesters')
    def beta_testers_linkages(self) -> BetaTestersLinkagesOfAppEndpoint:
        return BetaTestersLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/buildUploads')
    def build_uploads_linkages(self) -> BuildUploadsLinkagesOfAppEndpoint:
        return BuildUploadsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/builds')
    def builds_linkages(self) -> BuildsLinkagesOfAppEndpoint:
        return BuildsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/ciProduct')
    def ci_product_linkage(self) -> CiProductLinkageOfAppEndpoint:
        return CiProductLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/customerReviews')
    def customer_reviews_linkages(self) -> CustomerReviewsLinkagesOfAppEndpoint:
        return CustomerReviewsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/endUserLicenseAgreement')
    def end_user_license_agreement_linkage(self) -> EndUserLicenseAgreementLinkageOfAppEndpoint:
        return EndUserLicenseAgreementLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/gameCenterDetail')
    def game_center_detail_linkage(self) -> GameCenterDetailLinkageOfAppEndpoint:
        return GameCenterDetailLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/gameCenterEnabledVersions')
    def game_center_enabled_versions_linkages(self) -> GameCenterEnabledVersionsLinkagesOfAppEndpoint:
        return GameCenterEnabledVersionsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/inAppPurchases')
    def in_app_purchases_linkages(self) -> InAppPurchasesLinkagesOfAppEndpoint:
        return InAppPurchasesLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/inAppPurchasesV2')
    def in_app_purchases_v2_linkage(self) -> InAppPurchasesV2LinkageOfAppEndpoint:
        return InAppPurchasesV2LinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/marketplaceSearchDetail')
    def marketplace_search_detail_linkage(self) -> MarketplaceSearchDetailLinkageOfAppEndpoint:
        return MarketplaceSearchDetailLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/preReleaseVersions')
    def pre_release_versions_linkages(self) -> PreReleaseVersionsLinkagesOfAppEndpoint:
        return PreReleaseVersionsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/promotedPurchases')
    def promoted_purchases_linkages(self) -> PromotedPurchasesLinkagesOfAppEndpoint:
        return PromotedPurchasesLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/reviewSubmissions')
    def review_submissions_linkages(self) -> ReviewSubmissionsLinkagesOfAppEndpoint:
        return ReviewSubmissionsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/searchKeywords')
    def search_keywords_linkages(self) -> SearchKeywordsLinkagesOfAppEndpoint:
        return SearchKeywordsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/subscriptionGracePeriod')
    def subscription_grace_period_linkage(self) -> SubscriptionGracePeriodLinkageOfAppEndpoint:
        return SubscriptionGracePeriodLinkageOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/subscriptionGroups')
    def subscription_groups_linkages(self) -> SubscriptionGroupsLinkagesOfAppEndpoint:
        return SubscriptionGroupsLinkagesOfAppEndpoint(self.id, self.session)
        
    @endpoint('/v1/apps/{id}/relationships/webhooks')
    def webhooks_linkages(self) -> WebhooksLinkagesOfAppEndpoint:
        return WebhooksLinkagesOfAppEndpoint(self.id, self.session)
        
    def fields(self, *, app: Union[AppField, list[AppField]]=None, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, ci_product: Union[CiProductField, list[CiProductField]]=None, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None, app_info: Union[AppInfoField, list[AppInfoField]]=None, app_clip: Union[AppClipField, list[AppClipField]]=None, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, app_event: Union[AppEventField, list[AppEventField]]=None, review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]]=None, subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]]=None, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]]=None) -> AppEndpoint:
        '''Fields to return for included related types.

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

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
        :rtype: applaud.endpoints.AppEndpoint
        '''
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
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

    def include(self, relationship: Union[Include, list[Include]]) -> AppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, android_to_ios_app_mapping_details: int=None, app_clips: int=None, app_custom_product_pages: int=None, app_encryption_declarations: int=None, app_events: int=None, app_infos: int=None, app_store_version_experiments_v2: int=None, app_store_versions: int=None, beta_app_localizations: int=None, beta_groups: int=None, builds: int=None, game_center_enabled_versions: int=None, in_app_purchases: int=None, in_app_purchases_v2: int=None, pre_release_versions: int=None, promoted_purchases: int=None, review_submissions: int=None, subscription_groups: int=None) -> AppEndpoint:
        '''Number of included related resources to return.

        :param android_to_ios_app_mapping_details: maximum number of related androidToIosAppMappingDetails returned (when they are included). The maximum limit is 50
        :type android_to_ios_app_mapping_details: int = None

        :param app_clips: maximum number of related appClips returned (when they are included). The maximum limit is 50
        :type app_clips: int = None

        :param app_custom_product_pages: maximum number of related appCustomProductPages returned (when they are included). The maximum limit is 50
        :type app_custom_product_pages: int = None

        :param app_encryption_declarations: maximum number of related appEncryptionDeclarations returned (when they are included). The maximum limit is 50
        :type app_encryption_declarations: int = None

        :param app_events: maximum number of related appEvents returned (when they are included). The maximum limit is 50
        :type app_events: int = None

        :param app_infos: maximum number of related appInfos returned (when they are included). The maximum limit is 50
        :type app_infos: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :param app_store_versions: maximum number of related appStoreVersions returned (when they are included). The maximum limit is 50
        :type app_store_versions: int = None

        :param beta_app_localizations: maximum number of related betaAppLocalizations returned (when they are included). The maximum limit is 50
        :type beta_app_localizations: int = None

        :param beta_groups: maximum number of related betaGroups returned (when they are included). The maximum limit is 50
        :type beta_groups: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :param game_center_enabled_versions: maximum number of related gameCenterEnabledVersions returned (when they are included). The maximum limit is 50
        :type game_center_enabled_versions: int = None

        :param in_app_purchases: maximum number of related inAppPurchases returned (when they are included). The maximum limit is 50
        :type in_app_purchases: int = None

        :param in_app_purchases_v2: maximum number of related inAppPurchasesV2 returned (when they are included). The maximum limit is 50
        :type in_app_purchases_v2: int = None

        :param pre_release_versions: maximum number of related preReleaseVersions returned (when they are included). The maximum limit is 50
        :type pre_release_versions: int = None

        :param promoted_purchases: maximum number of related promotedPurchases returned (when they are included). The maximum limit is 50
        :type promoted_purchases: int = None

        :param review_submissions: maximum number of related reviewSubmissions returned (when they are included). The maximum limit is 50
        :type review_submissions: int = None

        :param subscription_groups: maximum number of related subscriptionGroups returned (when they are included). The maximum limit is 50
        :type subscription_groups: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEndpoint
        '''
        if android_to_ios_app_mapping_details and android_to_ios_app_mapping_details > 50:
            raise ValueError(f'The maximum limit of android_to_ios_app_mapping_details is 50')
        if android_to_ios_app_mapping_details: self._set_limit(android_to_ios_app_mapping_details, 'androidToIosAppMappingDetails')

        if app_clips and app_clips > 50:
            raise ValueError(f'The maximum limit of app_clips is 50')
        if app_clips: self._set_limit(app_clips, 'appClips')

        if app_custom_product_pages and app_custom_product_pages > 50:
            raise ValueError(f'The maximum limit of app_custom_product_pages is 50')
        if app_custom_product_pages: self._set_limit(app_custom_product_pages, 'appCustomProductPages')

        if app_encryption_declarations and app_encryption_declarations > 50:
            raise ValueError(f'The maximum limit of app_encryption_declarations is 50')
        if app_encryption_declarations: self._set_limit(app_encryption_declarations, 'appEncryptionDeclarations')

        if app_events and app_events > 50:
            raise ValueError(f'The maximum limit of app_events is 50')
        if app_events: self._set_limit(app_events, 'appEvents')

        if app_infos and app_infos > 50:
            raise ValueError(f'The maximum limit of app_infos is 50')
        if app_infos: self._set_limit(app_infos, 'appInfos')

        if app_store_version_experiments_v2 and app_store_version_experiments_v2 > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiments_v2 is 50')
        if app_store_version_experiments_v2: self._set_limit(app_store_version_experiments_v2, 'appStoreVersionExperimentsV2')

        if app_store_versions and app_store_versions > 50:
            raise ValueError(f'The maximum limit of app_store_versions is 50')
        if app_store_versions: self._set_limit(app_store_versions, 'appStoreVersions')

        if beta_app_localizations and beta_app_localizations > 50:
            raise ValueError(f'The maximum limit of beta_app_localizations is 50')
        if beta_app_localizations: self._set_limit(beta_app_localizations, 'betaAppLocalizations')

        if beta_groups and beta_groups > 50:
            raise ValueError(f'The maximum limit of beta_groups is 50')
        if beta_groups: self._set_limit(beta_groups, 'betaGroups')

        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        if game_center_enabled_versions and game_center_enabled_versions > 50:
            raise ValueError(f'The maximum limit of game_center_enabled_versions is 50')
        if game_center_enabled_versions: self._set_limit(game_center_enabled_versions, 'gameCenterEnabledVersions')

        if in_app_purchases and in_app_purchases > 50:
            raise ValueError(f'The maximum limit of in_app_purchases is 50')
        if in_app_purchases: self._set_limit(in_app_purchases, 'inAppPurchases')

        if in_app_purchases_v2 and in_app_purchases_v2 > 50:
            raise ValueError(f'The maximum limit of in_app_purchases_v2 is 50')
        if in_app_purchases_v2: self._set_limit(in_app_purchases_v2, 'inAppPurchasesV2')

        if pre_release_versions and pre_release_versions > 50:
            raise ValueError(f'The maximum limit of pre_release_versions is 50')
        if pre_release_versions: self._set_limit(pre_release_versions, 'preReleaseVersions')

        if promoted_purchases and promoted_purchases > 50:
            raise ValueError(f'The maximum limit of promoted_purchases is 50')
        if promoted_purchases: self._set_limit(promoted_purchases, 'promotedPurchases')

        if review_submissions and review_submissions > 50:
            raise ValueError(f'The maximum limit of review_submissions is 50')
        if review_submissions: self._set_limit(review_submissions, 'reviewSubmissions')

        if subscription_groups and subscription_groups > 50:
            raise ValueError(f'The maximum limit of subscription_groups is 50')
        if subscription_groups: self._set_limit(subscription_groups, 'subscriptionGroups')

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

    def update(self, request: AppUpdateRequest) -> AppResponse:
        '''Modify the resource.

        :param request: App representation
        :type request: AppUpdateRequest

        :returns: Single App
        :rtype: AppResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppResponse.parse_obj(json)

class AccessibilityDeclarationsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/accessibilityDeclarations'

    def limit(self, number: int=None) -> AccessibilityDeclarationsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AccessibilityDeclarationsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAccessibilityDeclarationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAccessibilityDeclarationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAccessibilityDeclarationsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAccessibilityDeclarationsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAccessibilityDeclarationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAccessibilityDeclarationsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAccessibilityDeclarationsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AccessibilityDeclarationsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/accessibilityDeclarations'

    class DeviceFamily(StringEnum):
        IPHONE = 'IPHONE'
        IPAD = 'IPAD'
        APPLE_TV = 'APPLE_TV'
        APPLE_WATCH = 'APPLE_WATCH'
        MAC = 'MAC'
        VISION = 'VISION'

    class State(StringEnum):
        DRAFT = 'DRAFT'
        PUBLISHED = 'PUBLISHED'
        REPLACED = 'REPLACED'

    def fields(self, *, accessibility_declaration: Union[AccessibilityDeclarationField, list[AccessibilityDeclarationField]]=None) -> AccessibilityDeclarationsOfAppEndpoint:
        '''Fields to return for included related types.

        :param accessibility_declaration: the fields to include for returned resources of type accessibilityDeclarations
        :type accessibility_declaration: Union[AccessibilityDeclarationField, list[AccessibilityDeclarationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AccessibilityDeclarationsOfAppEndpoint
        '''
        if accessibility_declaration: self._set_fields('accessibilityDeclarations',accessibility_declaration if type(accessibility_declaration) is list else [accessibility_declaration])
        return self
        
    def filter(self, *, device_family: Union[DeviceFamily, list[DeviceFamily]]=None, state: Union[State, list[State]]=None) -> AccessibilityDeclarationsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param device_family: filter by attribute 'deviceFamily'
        :type device_family: Union[DeviceFamily, list[DeviceFamily]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.AccessibilityDeclarationsOfAppEndpoint
        '''
        if device_family: self._set_filter('deviceFamily', device_family if type(device_family) is list else [device_family])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def limit(self, number: int=None) -> AccessibilityDeclarationsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AccessibilityDeclarationsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AccessibilityDeclarationsResponse:
        '''Get one or more resources.

        :returns: List of AccessibilityDeclarations
        :rtype: AccessibilityDeclarationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AccessibilityDeclarationsResponse.parse_obj(json)

    def get_all(self) -> AccessibilityDeclarationsResponse:
        '''
        Get all resources.

        :returns: List of AccessibilityDeclarations
        :rtype: AccessibilityDeclarationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AccessibilityDeclarationsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AccessibilityDeclarationsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AlternativeDistributionKeyLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/alternativeDistributionKey'

    def get(self) -> AppAlternativeDistributionKeyLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppAlternativeDistributionKeyLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAlternativeDistributionKeyLinkageResponse.parse_obj(json)
class AlternativeDistributionKeyOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/alternativeDistributionKey'

    def fields(self, *, alternative_distribution_key: Union[AlternativeDistributionKeyField, list[AlternativeDistributionKeyField]]=None) -> AlternativeDistributionKeyOfAppEndpoint:
        '''Fields to return for included related types.

        :param alternative_distribution_key: the fields to include for returned resources of type alternativeDistributionKeys
        :type alternative_distribution_key: Union[AlternativeDistributionKeyField, list[AlternativeDistributionKeyField]] = None

        :returns: self
        :rtype: applaud.endpoints.AlternativeDistributionKeyOfAppEndpoint
        '''
        if alternative_distribution_key: self._set_fields('alternativeDistributionKeys',alternative_distribution_key if type(alternative_distribution_key) is list else [alternative_distribution_key])
        return self
        
    def get(self) -> AlternativeDistributionKeyResponse:
        '''Get the resource.

        :returns: Single AlternativeDistributionKey
        :rtype: AlternativeDistributionKeyResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AlternativeDistributionKeyResponse.parse_obj(json)
class AnalyticsReportRequestsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/analyticsReportRequests'

    def limit(self, number: int=None) -> AnalyticsReportRequestsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAnalyticsReportRequestsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAnalyticsReportRequestsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAnalyticsReportRequestsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAnalyticsReportRequestsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAnalyticsReportRequestsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAnalyticsReportRequestsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAnalyticsReportRequestsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AnalyticsReportRequestsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/analyticsReportRequests'

    class AccessType(StringEnum):
        ONE_TIME_SNAPSHOT = 'ONE_TIME_SNAPSHOT'
        ONGOING = 'ONGOING'

    def fields(self, *, analytics_report_request: Union[AnalyticsReportRequestField, list[AnalyticsReportRequestField]]=None, analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]]=None) -> AnalyticsReportRequestsOfAppEndpoint:
        '''Fields to return for included related types.

        :param analytics_report_request: the fields to include for returned resources of type analyticsReportRequests
        :type analytics_report_request: Union[AnalyticsReportRequestField, list[AnalyticsReportRequestField]] = None

        :param analytics_report: the fields to include for returned resources of type analyticsReports
        :type analytics_report: Union[AnalyticsReportField, list[AnalyticsReportField]] = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestsOfAppEndpoint
        '''
        if analytics_report_request: self._set_fields('analyticsReportRequests',analytics_report_request if type(analytics_report_request) is list else [analytics_report_request])
        if analytics_report: self._set_fields('analyticsReports',analytics_report if type(analytics_report) is list else [analytics_report])
        return self
        
    class Include(StringEnum):
        REPORTS = 'reports'

    def filter(self, *, access_type: Union[AccessType, list[AccessType]]=None) -> AnalyticsReportRequestsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param access_type: filter by attribute 'accessType'
        :type access_type: Union[AccessType, list[AccessType]] = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestsOfAppEndpoint
        '''
        if access_type: self._set_filter('accessType', access_type if type(access_type) is list else [access_type])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AnalyticsReportRequestsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, reports: int=None) -> AnalyticsReportRequestsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param reports: maximum number of related reports returned (when they are included). The maximum limit is 50
        :type reports: int = None

        :returns: self
        :rtype: applaud.endpoints.AnalyticsReportRequestsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if reports and reports > 50:
            raise ValueError(f'The maximum limit of reports is 50')
        if reports: self._set_limit(reports, 'reports')

        return self

    def get(self) -> AnalyticsReportRequestsResponse:
        '''Get one or more resources.

        :returns: List of AnalyticsReportRequests
        :rtype: AnalyticsReportRequestsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AnalyticsReportRequestsResponse.parse_obj(json)

    def get_all(self) -> AnalyticsReportRequestsResponse:
        '''
        Get all resources.

        :returns: List of AnalyticsReportRequests
        :rtype: AnalyticsReportRequestsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AnalyticsReportRequestsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AnalyticsReportRequestsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AndroidToIosAppMappingDetailsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/androidToIosAppMappingDetails'

    def limit(self, number: int=None) -> AndroidToIosAppMappingDetailsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AndroidToIosAppMappingDetailsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAndroidToIosAppMappingDetailsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAndroidToIosAppMappingDetailsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAndroidToIosAppMappingDetailsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAndroidToIosAppMappingDetailsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAndroidToIosAppMappingDetailsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAndroidToIosAppMappingDetailsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAndroidToIosAppMappingDetailsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AndroidToIosAppMappingDetailsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/androidToIosAppMappingDetails'

    def fields(self, *, android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]]=None) -> AndroidToIosAppMappingDetailsOfAppEndpoint:
        '''Fields to return for included related types.

        :param android_to_ios_app_mapping_detail: the fields to include for returned resources of type androidToIosAppMappingDetails
        :type android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AndroidToIosAppMappingDetailsOfAppEndpoint
        '''
        if android_to_ios_app_mapping_detail: self._set_fields('androidToIosAppMappingDetails',android_to_ios_app_mapping_detail if type(android_to_ios_app_mapping_detail) is list else [android_to_ios_app_mapping_detail])
        return self
        
    def limit(self, number: int=None) -> AndroidToIosAppMappingDetailsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AndroidToIosAppMappingDetailsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AndroidToIosAppMappingDetailsResponse:
        '''Get one or more resources.

        :returns: List of AndroidToIosAppMappingDetails
        :rtype: AndroidToIosAppMappingDetailsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AndroidToIosAppMappingDetailsResponse.parse_obj(json)

    def get_all(self) -> AndroidToIosAppMappingDetailsResponse:
        '''
        Get all resources.

        :returns: List of AndroidToIosAppMappingDetails
        :rtype: AndroidToIosAppMappingDetailsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AndroidToIosAppMappingDetailsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AndroidToIosAppMappingDetailsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppAvailabilityV2LinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appAvailabilityV2'

    def get(self) -> AppAppAvailabilityV2LinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppAppAvailabilityV2LinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppAvailabilityV2LinkageResponse.parse_obj(json)
class AppAvailabilityV2OfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appAvailabilityV2'

    def fields(self, *, app_availability: Union[AppAvailabilityField, list[AppAvailabilityField]]=None, territory_availability: Union[TerritoryAvailabilityField, list[TerritoryAvailabilityField]]=None) -> AppAvailabilityV2OfAppEndpoint:
        '''Fields to return for included related types.

        :param app_availability: the fields to include for returned resources of type appAvailabilities
        :type app_availability: Union[AppAvailabilityField, list[AppAvailabilityField]] = None

        :param territory_availability: the fields to include for returned resources of type territoryAvailabilities
        :type territory_availability: Union[TerritoryAvailabilityField, list[TerritoryAvailabilityField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppAvailabilityV2OfAppEndpoint
        '''
        if app_availability: self._set_fields('appAvailabilities',app_availability if type(app_availability) is list else [app_availability])
        if territory_availability: self._set_fields('territoryAvailabilities',territory_availability if type(territory_availability) is list else [territory_availability])
        return self
        
    class Include(StringEnum):
        TERRITORY_AVAILABILITIES = 'territoryAvailabilities'

    def include(self, relationship: Union[Include, list[Include]]) -> AppAvailabilityV2OfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppAvailabilityV2OfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, territory_availabilities: int=None) -> AppAvailabilityV2OfAppEndpoint:
        '''Number of included related resources to return.

        :param territory_availabilities: maximum number of related territoryAvailabilities returned (when they are included). The maximum limit is 50
        :type territory_availabilities: int = None

        :returns: self
        :rtype: applaud.endpoints.AppAvailabilityV2OfAppEndpoint
        '''
        if territory_availabilities and territory_availabilities > 50:
            raise ValueError(f'The maximum limit of territory_availabilities is 50')
        if territory_availabilities: self._set_limit(territory_availabilities, 'territoryAvailabilities')

        return self

    def get(self) -> AppAvailabilityV2Response:
        '''Get the resource.

        :returns: Single AppAvailability
        :rtype: AppAvailabilityV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAvailabilityV2Response.parse_obj(json)

    def get_all(self) -> AppAvailabilityV2Response:
        '''
        Get all resources.

        :returns: Single AppAvailability
        :rtype: AppAvailabilityV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAvailabilityV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAvailabilityV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppClipsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appClips'

    def limit(self, number: int=None) -> AppClipsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppClipsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppClipsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppClipsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppClipsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppClipsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppClipsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppClipsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppClipsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appClips'

    def fields(self, *, app_clip: Union[AppClipField, list[AppClipField]]=None, app: Union[AppField, list[AppField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None) -> AppClipsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_clip: the fields to include for returned resources of type appClips
        :type app_clip: Union[AppClipField, list[AppClipField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_clip_default_experience: the fields to include for returned resources of type appClipDefaultExperiences
        :type app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if app_clip: self._set_fields('appClips',app_clip if type(app_clip) is list else [app_clip])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_clip_default_experience: self._set_fields('appClipDefaultExperiences',app_clip_default_experience if type(app_clip_default_experience) is list else [app_clip_default_experience])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_CLIP_DEFAULT_EXPERIENCES = 'appClipDefaultExperiences'

    def filter(self, *, bundle_id: Union[str, list[str]]=None) -> AppClipsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param bundle_id: filter by attribute 'bundleId'
        :type bundle_id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if bundle_id: self._set_filter('bundleId', bundle_id if type(bundle_id) is list else [bundle_id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppClipsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_clip_default_experiences: int=None) -> AppClipsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_clip_default_experiences: maximum number of related appClipDefaultExperiences returned (when they are included). The maximum limit is 50
        :type app_clip_default_experiences: int = None

        :returns: self
        :rtype: applaud.endpoints.AppClipsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_clip_default_experiences and app_clip_default_experiences > 50:
            raise ValueError(f'The maximum limit of app_clip_default_experiences is 50')
        if app_clip_default_experiences: self._set_limit(app_clip_default_experiences, 'appClipDefaultExperiences')

        return self

    def get(self) -> AppClipsResponse:
        '''Get one or more resources.

        :returns: List of AppClips
        :rtype: AppClipsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppClipsResponse.parse_obj(json)

    def get_all(self) -> AppClipsResponse:
        '''
        Get all resources.

        :returns: List of AppClips
        :rtype: AppClipsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppClipsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppClipsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppCustomProductPagesLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appCustomProductPages'

    def limit(self, number: int=None) -> AppCustomProductPagesLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPagesLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppCustomProductPagesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppCustomProductPagesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppCustomProductPagesLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppCustomProductPagesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppCustomProductPagesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppCustomProductPagesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppCustomProductPagesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppCustomProductPagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appCustomProductPages'

    def fields(self, *, app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]]=None, app: Union[AppField, list[AppField]]=None, app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]]=None) -> AppCustomProductPagesOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_custom_product_page: the fields to include for returned resources of type appCustomProductPages
        :type app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param app_custom_product_page_version: the fields to include for returned resources of type appCustomProductPageVersions
        :type app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPagesOfAppEndpoint
        '''
        if app_custom_product_page: self._set_fields('appCustomProductPages',app_custom_product_page if type(app_custom_product_page) is list else [app_custom_product_page])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if app_custom_product_page_version: self._set_fields('appCustomProductPageVersions',app_custom_product_page_version if type(app_custom_product_page_version) is list else [app_custom_product_page_version])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_CUSTOM_PRODUCT_PAGE_VERSIONS = 'appCustomProductPageVersions'

    def filter(self, *, visible: Union[str, list[str]]=None) -> AppCustomProductPagesOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param visible: filter by attribute 'visible'
        :type visible: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPagesOfAppEndpoint
        '''
        if visible: self._set_filter('visible', visible if type(visible) is list else [visible])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppCustomProductPagesOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPagesOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_custom_product_page_versions: int=None) -> AppCustomProductPagesOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_custom_product_page_versions: maximum number of related appCustomProductPageVersions returned (when they are included). The maximum limit is 50
        :type app_custom_product_page_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_custom_product_page_versions and app_custom_product_page_versions > 50:
            raise ValueError(f'The maximum limit of app_custom_product_page_versions is 50')
        if app_custom_product_page_versions: self._set_limit(app_custom_product_page_versions, 'appCustomProductPageVersions')

        return self

    def get(self) -> AppCustomProductPagesResponse:
        '''Get one or more resources.

        :returns: List of AppCustomProductPages
        :rtype: AppCustomProductPagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPagesResponse.parse_obj(json)

    def get_all(self) -> AppCustomProductPagesResponse:
        '''
        Get all resources.

        :returns: List of AppCustomProductPages
        :rtype: AppCustomProductPagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppCustomProductPagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppCustomProductPagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppEncryptionDeclarationsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appEncryptionDeclarations'

    def limit(self, number: int=None) -> AppEncryptionDeclarationsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppEncryptionDeclarationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppEncryptionDeclarationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppEncryptionDeclarationsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppEncryptionDeclarationsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppEncryptionDeclarationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppEncryptionDeclarationsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppEncryptionDeclarationsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppEncryptionDeclarationsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appEncryptionDeclarations'

    class Platform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]]=None, app: Union[AppField, list[AppField]]=None, build: Union[BuildField, list[BuildField]]=None, app_encryption_declaration_document: Union[AppEncryptionDeclarationDocumentField, list[AppEncryptionDeclarationDocumentField]]=None) -> AppEncryptionDeclarationsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_encryption_declaration: the fields to include for returned resources of type appEncryptionDeclarations
        :type app_encryption_declaration: Union[AppEncryptionDeclarationField, list[AppEncryptionDeclarationField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param app_encryption_declaration_document: the fields to include for returned resources of type appEncryptionDeclarationDocuments
        :type app_encryption_declaration_document: Union[AppEncryptionDeclarationDocumentField, list[AppEncryptionDeclarationDocumentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsOfAppEndpoint
        '''
        if app_encryption_declaration: self._set_fields('appEncryptionDeclarations',app_encryption_declaration if type(app_encryption_declaration) is list else [app_encryption_declaration])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if app_encryption_declaration_document: self._set_fields('appEncryptionDeclarationDocuments',app_encryption_declaration_document if type(app_encryption_declaration_document) is list else [app_encryption_declaration_document])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUILDS = 'builds'
        APP_ENCRYPTION_DECLARATION_DOCUMENT = 'appEncryptionDeclarationDocument'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, builds: Union[str, list[str]]=None) -> AppEncryptionDeclarationsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param builds: filter by id(s) of related 'builds'
        :type builds: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if builds: self._set_filter('builds', builds if type(builds) is list else [builds])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppEncryptionDeclarationsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, builds: int=None) -> AppEncryptionDeclarationsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param builds: maximum number of related builds returned (when they are included). The maximum limit is 50
        :type builds: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEncryptionDeclarationsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if builds and builds > 50:
            raise ValueError(f'The maximum limit of builds is 50')
        if builds: self._set_limit(builds, 'builds')

        return self

    def get(self) -> AppEncryptionDeclarationsResponse:
        '''Get one or more resources.

        :returns: List of AppEncryptionDeclarations
        :rtype: AppEncryptionDeclarationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEncryptionDeclarationsResponse.parse_obj(json)

    def get_all(self) -> AppEncryptionDeclarationsResponse:
        '''
        Get all resources.

        :returns: List of AppEncryptionDeclarations
        :rtype: AppEncryptionDeclarationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppEncryptionDeclarationsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppEncryptionDeclarationsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppEventsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appEvents'

    def limit(self, number: int=None) -> AppEventsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppEventsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppEventsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppEventsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppEventsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppEventsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppEventsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppEventsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppEventsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appEvents'

    class EventState(StringEnum):
        DRAFT = 'DRAFT'
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        REJECTED = 'REJECTED'
        ACCEPTED = 'ACCEPTED'
        APPROVED = 'APPROVED'
        PUBLISHED = 'PUBLISHED'
        PAST = 'PAST'
        ARCHIVED = 'ARCHIVED'

    def fields(self, *, app_event: Union[AppEventField, list[AppEventField]]=None, app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]]=None) -> AppEventsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_event: the fields to include for returned resources of type appEvents
        :type app_event: Union[AppEventField, list[AppEventField]] = None

        :param app_event_localization: the fields to include for returned resources of type appEventLocalizations
        :type app_event_localization: Union[AppEventLocalizationField, list[AppEventLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventsOfAppEndpoint
        '''
        if app_event: self._set_fields('appEvents',app_event if type(app_event) is list else [app_event])
        if app_event_localization: self._set_fields('appEventLocalizations',app_event_localization if type(app_event_localization) is list else [app_event_localization])
        return self
        
    class Include(StringEnum):
        LOCALIZATIONS = 'localizations'

    def filter(self, *, event_state: Union[EventState, list[EventState]]=None, id: Union[str, list[str]]=None) -> AppEventsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param event_state: filter by attribute 'eventState'
        :type event_state: Union[EventState, list[EventState]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppEventsOfAppEndpoint
        '''
        if event_state: self._set_filter('eventState', event_state if type(event_state) is list else [event_state])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppEventsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppEventsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, localizations: int=None) -> AppEventsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param localizations: maximum number of related localizations returned (when they are included). The maximum limit is 50
        :type localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppEventsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if localizations and localizations > 50:
            raise ValueError(f'The maximum limit of localizations is 50')
        if localizations: self._set_limit(localizations, 'localizations')

        return self

    def get(self) -> AppEventsResponse:
        '''Get one or more resources.

        :returns: List of AppEvents
        :rtype: AppEventsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEventsResponse.parse_obj(json)

    def get_all(self) -> AppEventsResponse:
        '''
        Get all resources.

        :returns: List of AppEvents
        :rtype: AppEventsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppEventsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppEventsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppInfosLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appInfos'

    def limit(self, number: int=None) -> AppInfosLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppInfosLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppInfosLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppInfosLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppInfosLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppInfosLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppInfosLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppInfosLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppInfosLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppInfosOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appInfos'

    def fields(self, *, app_info: Union[AppInfoField, list[AppInfoField]]=None, app: Union[AppField, list[AppField]]=None, age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]]=None, app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]]=None, app_category: Union[AppCategoryField, list[AppCategoryField]]=None) -> AppInfosOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_info: the fields to include for returned resources of type appInfos
        :type app_info: Union[AppInfoField, list[AppInfoField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param age_rating_declaration: the fields to include for returned resources of type ageRatingDeclarations
        :type age_rating_declaration: Union[AgeRatingDeclarationField, list[AgeRatingDeclarationField]] = None

        :param app_info_localization: the fields to include for returned resources of type appInfoLocalizations
        :type app_info_localization: Union[AppInfoLocalizationField, list[AppInfoLocalizationField]] = None

        :param app_category: the fields to include for returned resources of type appCategories
        :type app_category: Union[AppCategoryField, list[AppCategoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppInfosOfAppEndpoint
        '''
        if app_info: self._set_fields('appInfos',app_info if type(app_info) is list else [app_info])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if age_rating_declaration: self._set_fields('ageRatingDeclarations',age_rating_declaration if type(age_rating_declaration) is list else [age_rating_declaration])
        if app_info_localization: self._set_fields('appInfoLocalizations',app_info_localization if type(app_info_localization) is list else [app_info_localization])
        if app_category: self._set_fields('appCategories',app_category if type(app_category) is list else [app_category])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        AGE_RATING_DECLARATION = 'ageRatingDeclaration'
        APP_INFO_LOCALIZATIONS = 'appInfoLocalizations'
        PRIMARY_CATEGORY = 'primaryCategory'
        PRIMARY_SUBCATEGORY_ONE = 'primarySubcategoryOne'
        PRIMARY_SUBCATEGORY_TWO = 'primarySubcategoryTwo'
        SECONDARY_CATEGORY = 'secondaryCategory'
        SECONDARY_SUBCATEGORY_ONE = 'secondarySubcategoryOne'
        SECONDARY_SUBCATEGORY_TWO = 'secondarySubcategoryTwo'

    def include(self, relationship: Union[Include, list[Include]]) -> AppInfosOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppInfosOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_info_localizations: int=None) -> AppInfosOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_info_localizations: maximum number of related appInfoLocalizations returned (when they are included). The maximum limit is 50
        :type app_info_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppInfosOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_info_localizations and app_info_localizations > 50:
            raise ValueError(f'The maximum limit of app_info_localizations is 50')
        if app_info_localizations: self._set_limit(app_info_localizations, 'appInfoLocalizations')

        return self

    def get(self) -> AppInfosResponse:
        '''Get one or more resources.

        :returns: List of AppInfos
        :rtype: AppInfosResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInfosResponse.parse_obj(json)

    def get_all(self) -> AppInfosResponse:
        '''
        Get all resources.

        :returns: List of AppInfos
        :rtype: AppInfosResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppInfosResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppInfosResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppPricePointsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appPricePoints'

    def limit(self, number: int=None) -> AppPricePointsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppPricePointsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppPricePointsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppPricePointsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppPricePointsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppPricePointsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppPricePointsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppPricePointsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppPricePointsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appPricePoints'

    def fields(self, *, app_price_point: Union[AppPricePointField, list[AppPricePointField]]=None, app: Union[AppField, list[AppField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AppPricePointsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_price_point: the fields to include for returned resources of type appPricePoints
        :type app_price_point: Union[AppPricePointField, list[AppPricePointField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsOfAppEndpoint
        '''
        if app_price_point: self._set_fields('appPricePoints',app_price_point if type(app_price_point) is list else [app_price_point])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        TERRITORY = 'territory'

    def filter(self, *, territory: Union[str, list[str]]=None) -> AppPricePointsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsOfAppEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppPricePointsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> AppPricePointsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPricePointsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPricePointsV3Response:
        '''Get one or more resources.

        :returns: List of AppPricePoints
        :rtype: AppPricePointsV3Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPricePointsV3Response.parse_obj(json)

    def get_all(self) -> AppPricePointsV3Response:
        '''
        Get all resources.

        :returns: List of AppPricePoints
        :rtype: AppPricePointsV3Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppPricePointsV3Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppPricePointsV3Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppPriceScheduleLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appPriceSchedule'

    def get(self) -> AppAppPriceScheduleLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppAppPriceScheduleLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppPriceScheduleLinkageResponse.parse_obj(json)
class AppPriceScheduleOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appPriceSchedule'

    def fields(self, *, app_price_schedule: Union[AppPriceScheduleField, list[AppPriceScheduleField]]=None, app: Union[AppField, list[AppField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None, app_price: Union[AppPriceField, list[AppPriceField]]=None) -> AppPriceScheduleOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_price_schedule: the fields to include for returned resources of type appPriceSchedules
        :type app_price_schedule: Union[AppPriceScheduleField, list[AppPriceScheduleField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :param app_price: the fields to include for returned resources of type appPrices
        :type app_price: Union[AppPriceField, list[AppPriceField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceScheduleOfAppEndpoint
        '''
        if app_price_schedule: self._set_fields('appPriceSchedules',app_price_schedule if type(app_price_schedule) is list else [app_price_schedule])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        if app_price: self._set_fields('appPrices',app_price if type(app_price) is list else [app_price])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BASE_TERRITORY = 'baseTerritory'
        MANUAL_PRICES = 'manualPrices'
        AUTOMATIC_PRICES = 'automaticPrices'

    def include(self, relationship: Union[Include, list[Include]]) -> AppPriceScheduleOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPriceScheduleOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, manual_prices: int=None, automatic_prices: int=None) -> AppPriceScheduleOfAppEndpoint:
        '''Number of included related resources to return.

        :param manual_prices: maximum number of related manualPrices returned (when they are included). The maximum limit is 50
        :type manual_prices: int = None

        :param automatic_prices: maximum number of related automaticPrices returned (when they are included). The maximum limit is 50
        :type automatic_prices: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPriceScheduleOfAppEndpoint
        '''
        if manual_prices and manual_prices > 50:
            raise ValueError(f'The maximum limit of manual_prices is 50')
        if manual_prices: self._set_limit(manual_prices, 'manualPrices')

        if automatic_prices and automatic_prices > 50:
            raise ValueError(f'The maximum limit of automatic_prices is 50')
        if automatic_prices: self._set_limit(automatic_prices, 'automaticPrices')

        return self

    def get(self) -> AppPriceScheduleResponse:
        '''Get the resource.

        :returns: Single AppPriceSchedule
        :rtype: AppPriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPriceScheduleResponse.parse_obj(json)

    def get_all(self) -> AppPriceScheduleResponse:
        '''
        Get all resources.

        :returns: Single AppPriceSchedule
        :rtype: AppPriceScheduleResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppPriceScheduleResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppPriceScheduleResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppStoreVersionExperimentsV2LinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appStoreVersionExperimentsV2'

    def limit(self, number: int=None) -> AppStoreVersionExperimentsV2LinkageOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2LinkageOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppStoreVersionExperimentsV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppStoreVersionExperimentsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppStoreVersionExperimentsV2LinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppStoreVersionExperimentsV2LinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppStoreVersionExperimentsV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppStoreVersionExperimentsV2LinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppStoreVersionExperimentsV2LinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppStoreVersionExperimentsV2OfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appStoreVersionExperimentsV2'

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

    def fields(self, *, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app: Union[AppField, list[AppField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None) -> AppStoreVersionExperimentsV2OfAppEndpoint:
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
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppEndpoint
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

    def filter(self, *, state: Union[State, list[State]]=None) -> AppStoreVersionExperimentsV2OfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppEndpoint
        '''
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentsV2OfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, control_versions: int=None, app_store_version_experiment_treatments: int=None) -> AppStoreVersionExperimentsV2OfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param control_versions: maximum number of related controlVersions returned (when they are included). The maximum limit is 50
        :type control_versions: int = None

        :param app_store_version_experiment_treatments: maximum number of related appStoreVersionExperimentTreatments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentsV2OfAppEndpoint
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

    def get_all(self) -> AppStoreVersionExperimentsV2Response:
        '''
        Get all resources.

        :returns: List of AppStoreVersionExperiments
        :rtype: AppStoreVersionExperimentsV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppStoreVersionExperimentsV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppStoreVersionExperimentsV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppStoreVersionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appStoreVersions'

    def limit(self, number: int=None) -> AppStoreVersionsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppStoreVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppStoreVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppStoreVersionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppStoreVersionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppStoreVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppStoreVersionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppStoreVersionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppStoreVersionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appStoreVersions'

    class AppVersionState(StringEnum):
        ACCEPTED = 'ACCEPTED'
        DEVELOPER_REJECTED = 'DEVELOPER_REJECTED'
        IN_REVIEW = 'IN_REVIEW'
        INVALID_BINARY = 'INVALID_BINARY'
        METADATA_REJECTED = 'METADATA_REJECTED'
        PENDING_APPLE_RELEASE = 'PENDING_APPLE_RELEASE'
        PENDING_DEVELOPER_RELEASE = 'PENDING_DEVELOPER_RELEASE'
        PREPARE_FOR_SUBMISSION = 'PREPARE_FOR_SUBMISSION'
        PROCESSING_FOR_DISTRIBUTION = 'PROCESSING_FOR_DISTRIBUTION'
        READY_FOR_DISTRIBUTION = 'READY_FOR_DISTRIBUTION'
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        REJECTED = 'REJECTED'
        REPLACED_WITH_NEW_VERSION = 'REPLACED_WITH_NEW_VERSION'
        WAITING_FOR_EXPORT_COMPLIANCE = 'WAITING_FOR_EXPORT_COMPLIANCE'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'

    def fields(self, *, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, app: Union[AppField, list[AppField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, build: Union[BuildField, list[BuildField]]=None, app_store_version_phased_release: Union[AppStoreVersionPhasedReleaseField, list[AppStoreVersionPhasedReleaseField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, routing_app_coverage: Union[RoutingAppCoverageField, list[RoutingAppCoverageField]]=None, app_store_review_detail: Union[AppStoreReviewDetailField, list[AppStoreReviewDetailField]]=None, app_store_version_submission: Union[AppStoreVersionSubmissionField, list[AppStoreVersionSubmissionField]]=None, app_clip_default_experience: Union[AppClipDefaultExperienceField, list[AppClipDefaultExperienceField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, alternative_distribution_package: Union[AlternativeDistributionPackageField, list[AlternativeDistributionPackageField]]=None) -> AppStoreVersionsOfAppEndpoint:
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
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
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

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, version_string: Union[str, list[str]]=None, app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]]=None, app_version_state: Union[AppVersionState, list[AppVersionState]]=None, id: Union[str, list[str]]=None) -> AppStoreVersionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param version_string: filter by attribute 'versionString'
        :type version_string: Union[str, list[str]] = None

        :param app_store_state: filter by attribute 'appStoreState'
        :type app_store_state: Union[AppStoreVersionState, list[AppStoreVersionState]] = None

        :param app_version_state: filter by attribute 'appVersionState'
        :type app_version_state: Union[AppVersionState, list[AppVersionState]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if version_string: self._set_filter('versionString', version_string if type(version_string) is list else [version_string])
        
        if app_store_state: self._set_filter('appStoreState', app_store_state if type(app_store_state) is list else [app_store_state])
        
        if app_version_state: self._set_filter('appVersionState', app_version_state if type(app_version_state) is list else [app_version_state])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_store_version_localizations: int=None, app_store_version_experiments: int=None, app_store_version_experiments_v2: int=None) -> AppStoreVersionsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_store_version_localizations: maximum number of related appStoreVersionLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_localizations: int = None

        :param app_store_version_experiments: maximum number of related appStoreVersionExperiments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments: int = None

        :param app_store_version_experiments_v2: maximum number of related appStoreVersionExperimentsV2 returned (when they are included). The maximum limit is 50
        :type app_store_version_experiments_v2: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
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

    def get(self) -> AppStoreVersionsResponse:
        '''Get one or more resources.

        :returns: List of AppStoreVersions
        :rtype: AppStoreVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionsResponse.parse_obj(json)

    def get_all(self) -> AppStoreVersionsResponse:
        '''
        Get all resources.

        :returns: List of AppStoreVersions
        :rtype: AppStoreVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppStoreVersionsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppStoreVersionsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppTagsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/appTags'

    def limit(self, number: int=None) -> AppTagsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppTagsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppAppTagsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppAppTagsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppAppTagsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppAppTagsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppAppTagsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppAppTagsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppAppTagsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class AppTagsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/appTags'

    def fields(self, *, app_tag: Union[AppTagField, list[AppTagField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> AppTagsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_tag: the fields to include for returned resources of type appTags
        :type app_tag: Union[AppTagField, list[AppTagField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppTagsOfAppEndpoint
        '''
        if app_tag: self._set_fields('appTags',app_tag if type(app_tag) is list else [app_tag])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORIES = 'territories'

    def filter(self, *, visible_in_app_store: Union[str, list[str]]=None) -> AppTagsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param visible_in_app_store: filter by attribute 'visibleInAppStore'
        :type visible_in_app_store: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppTagsOfAppEndpoint
        '''
        if visible_in_app_store: self._set_filter('visibleInAppStore', visible_in_app_store if type(visible_in_app_store) is list else [visible_in_app_store])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppTagsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppTagsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None) -> AppTagsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.AppTagsOfAppEndpoint
        '''
        sort_expressions = []
        if name: sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None, *, territories: int=None) -> AppTagsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param territories: maximum number of related territories returned (when they are included). The maximum limit is 50
        :type territories: int = None

        :returns: self
        :rtype: applaud.endpoints.AppTagsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if territories and territories > 50:
            raise ValueError(f'The maximum limit of territories is 50')
        if territories: self._set_limit(territories, 'territories')

        return self

    def get(self) -> AppTagsResponse:
        '''Get one or more resources.

        :returns: List of AppTags
        :rtype: AppTagsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppTagsResponse.parse_obj(json)

    def get_all(self) -> AppTagsResponse:
        '''
        Get all resources.

        :returns: List of AppTags
        :rtype: AppTagsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppTagsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppTagsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BackgroundAssetsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/backgroundAssets'

    def limit(self, number: int=None) -> BackgroundAssetsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBackgroundAssetsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBackgroundAssetsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBackgroundAssetsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBackgroundAssetsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBackgroundAssetsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBackgroundAssetsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBackgroundAssetsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BackgroundAssetsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/backgroundAssets'

    class Versions_platforms(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]]=None, app: Union[AppField, list[AppField]]=None, background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]]=None) -> BackgroundAssetsOfAppEndpoint:
        '''Fields to return for included related types.

        :param background_asset: the fields to include for returned resources of type backgroundAssets
        :type background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param background_asset_version: the fields to include for returned resources of type backgroundAssetVersions
        :type background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetsOfAppEndpoint
        '''
        if background_asset: self._set_fields('backgroundAssets',background_asset if type(background_asset) is list else [background_asset])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if background_asset_version: self._set_fields('backgroundAssetVersions',background_asset_version if type(background_asset_version) is list else [background_asset_version])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_STORE_VERSION = 'appStoreVersion'
        INTERNAL_BETA_VERSION = 'internalBetaVersion'
        EXTERNAL_BETA_VERSION = 'externalBetaVersion'

    def filter(self, *, archived: Union[str, list[str]]=None, asset_pack_identifier: Union[str, list[str]]=None, versions_platforms: Union[Versions_platforms, list[Versions_platforms]]=None) -> BackgroundAssetsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param archived: filter by attribute 'archived'
        :type archived: Union[str, list[str]] = None

        :param asset_pack_identifier: filter by attribute 'assetPackIdentifier'
        :type asset_pack_identifier: Union[str, list[str]] = None

        :param versions_platforms: filter by attribute 'versions.platforms'
        :type versions_platforms: Union[Versions_platforms, list[Versions_platforms]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetsOfAppEndpoint
        '''
        if archived: self._set_filter('archived', archived if type(archived) is list else [archived])
        
        if asset_pack_identifier: self._set_filter('assetPackIdentifier', asset_pack_identifier if type(asset_pack_identifier) is list else [asset_pack_identifier])
        
        if versions_platforms: self._set_filter('versions.platforms', versions_platforms if type(versions_platforms) is list else [versions_platforms])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BackgroundAssetsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, asset_pack_identifier: SortOrder=None, created_date: SortOrder=None) -> BackgroundAssetsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetsOfAppEndpoint
        '''
        sort_expressions = []
        if asset_pack_identifier: sort_expressions.append('assetPackIdentifier' if asset_pack_identifier == SortOrder.ASC else '-assetPackIdentifier')
        if created_date: sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None) -> BackgroundAssetsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetsResponse:
        '''Get one or more resources.

        :returns: List of BackgroundAssets
        :rtype: BackgroundAssetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetsResponse.parse_obj(json)

    def get_all(self) -> BackgroundAssetsResponse:
        '''
        Get all resources.

        :returns: List of BackgroundAssets
        :rtype: BackgroundAssetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BackgroundAssetsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BackgroundAssetsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaAppLocalizationsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaAppLocalizations'

    def limit(self, number: int=None) -> BetaAppLocalizationsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBetaAppLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBetaAppLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBetaAppLocalizationsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBetaAppLocalizationsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBetaAppLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBetaAppLocalizationsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBetaAppLocalizationsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaAppLocalizationsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaAppLocalizations'

    def fields(self, *, beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]]=None) -> BetaAppLocalizationsOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_app_localization: the fields to include for returned resources of type betaAppLocalizations
        :type beta_app_localization: Union[BetaAppLocalizationField, list[BetaAppLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsOfAppEndpoint
        '''
        if beta_app_localization: self._set_fields('betaAppLocalizations',beta_app_localization if type(beta_app_localization) is list else [beta_app_localization])
        return self
        
    def limit(self, number: int=None) -> BetaAppLocalizationsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppLocalizationsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaAppLocalizationsWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of BetaAppLocalizations with get
        :rtype: BetaAppLocalizationsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppLocalizationsWithoutIncludesResponse.parse_obj(json)

    def get_all(self) -> BetaAppLocalizationsWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of BetaAppLocalizations with get
        :rtype: BetaAppLocalizationsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaAppLocalizationsWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaAppLocalizationsWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaAppReviewDetailLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaAppReviewDetail'

    def get(self) -> AppBetaAppReviewDetailLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppBetaAppReviewDetailLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBetaAppReviewDetailLinkageResponse.parse_obj(json)
class BetaAppReviewDetailOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaAppReviewDetail'

    def fields(self, *, beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]]=None) -> BetaAppReviewDetailOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_app_review_detail: the fields to include for returned resources of type betaAppReviewDetails
        :type beta_app_review_detail: Union[BetaAppReviewDetailField, list[BetaAppReviewDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaAppReviewDetailOfAppEndpoint
        '''
        if beta_app_review_detail: self._set_fields('betaAppReviewDetails',beta_app_review_detail if type(beta_app_review_detail) is list else [beta_app_review_detail])
        return self
        
    def get(self) -> BetaAppReviewDetailWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single BetaAppReviewDetail with get
        :rtype: BetaAppReviewDetailWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaAppReviewDetailWithoutIncludesResponse.parse_obj(json)
class BetaFeedbackCrashSubmissionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaFeedbackCrashSubmissions'

    def limit(self, number: int=None) -> BetaFeedbackCrashSubmissionsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBetaFeedbackCrashSubmissionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBetaFeedbackCrashSubmissionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBetaFeedbackCrashSubmissionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBetaFeedbackCrashSubmissionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBetaFeedbackCrashSubmissionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBetaFeedbackCrashSubmissionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBetaFeedbackCrashSubmissionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaFeedbackCrashSubmissionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaFeedbackCrashSubmissions'

    class AppPlatform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    class DevicePlatform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, beta_feedback_crash_submission: Union[BetaFeedbackCrashSubmissionField, list[BetaFeedbackCrashSubmissionField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None) -> BetaFeedbackCrashSubmissionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_feedback_crash_submission: the fields to include for returned resources of type betaFeedbackCrashSubmissions
        :type beta_feedback_crash_submission: Union[BetaFeedbackCrashSubmissionField, list[BetaFeedbackCrashSubmissionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionsOfAppEndpoint
        '''
        if beta_feedback_crash_submission: self._set_fields('betaFeedbackCrashSubmissions',beta_feedback_crash_submission if type(beta_feedback_crash_submission) is list else [beta_feedback_crash_submission])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'
        TESTER = 'tester'

    def filter(self, *, device_model: Union[str, list[str]]=None, os_version: Union[str, list[str]]=None, app_platform: Union[AppPlatform, list[AppPlatform]]=None, device_platform: Union[DevicePlatform, list[DevicePlatform]]=None, build: Union[str, list[str]]=None, build_pre_release_version: Union[str, list[str]]=None, tester: Union[str, list[str]]=None) -> BetaFeedbackCrashSubmissionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param device_model: filter by attribute 'deviceModel'
        :type device_model: Union[str, list[str]] = None

        :param os_version: filter by attribute 'osVersion'
        :type os_version: Union[str, list[str]] = None

        :param app_platform: filter by attribute 'appPlatform'
        :type app_platform: Union[AppPlatform, list[AppPlatform]] = None

        :param device_platform: filter by attribute 'devicePlatform'
        :type device_platform: Union[DevicePlatform, list[DevicePlatform]] = None

        :param build: filter by id(s) of related 'build'
        :type build: Union[str, list[str]] = None

        :param build_pre_release_version: filter by id(s) of related 'build.preReleaseVersion'
        :type build_pre_release_version: Union[str, list[str]] = None

        :param tester: filter by id(s) of related 'tester'
        :type tester: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionsOfAppEndpoint
        '''
        if device_model: self._set_filter('deviceModel', device_model if type(device_model) is list else [device_model])
        
        if os_version: self._set_filter('osVersion', os_version if type(os_version) is list else [os_version])
        
        if app_platform: self._set_filter('appPlatform', app_platform if type(app_platform) is list else [app_platform])
        
        if device_platform: self._set_filter('devicePlatform', device_platform if type(device_platform) is list else [device_platform])
        
        if build: self._set_filter('build', build if type(build) is list else [build])
        
        if build_pre_release_version: self._set_filter('build.preReleaseVersion', build_pre_release_version if type(build_pre_release_version) is list else [build_pre_release_version])
        
        if tester: self._set_filter('tester', tester if type(tester) is list else [tester])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaFeedbackCrashSubmissionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, created_date: SortOrder=None) -> BetaFeedbackCrashSubmissionsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionsOfAppEndpoint
        '''
        sort_expressions = []
        if created_date: sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None) -> BetaFeedbackCrashSubmissionsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackCrashSubmissionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaFeedbackCrashSubmissionsResponse:
        '''Get one or more resources.

        :returns: List of BetaFeedbackCrashSubmissions
        :rtype: BetaFeedbackCrashSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaFeedbackCrashSubmissionsResponse.parse_obj(json)

    def get_all(self) -> BetaFeedbackCrashSubmissionsResponse:
        '''
        Get all resources.

        :returns: List of BetaFeedbackCrashSubmissions
        :rtype: BetaFeedbackCrashSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaFeedbackCrashSubmissionsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaFeedbackCrashSubmissionsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaFeedbackScreenshotSubmissionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaFeedbackScreenshotSubmissions'

    def limit(self, number: int=None) -> BetaFeedbackScreenshotSubmissionsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBetaFeedbackScreenshotSubmissionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBetaFeedbackScreenshotSubmissionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBetaFeedbackScreenshotSubmissionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBetaFeedbackScreenshotSubmissionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBetaFeedbackScreenshotSubmissionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBetaFeedbackScreenshotSubmissionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBetaFeedbackScreenshotSubmissionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaFeedbackScreenshotSubmissionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaFeedbackScreenshotSubmissions'

    class AppPlatform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    class DevicePlatform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, beta_feedback_screenshot_submission: Union[BetaFeedbackScreenshotSubmissionField, list[BetaFeedbackScreenshotSubmissionField]]=None, build: Union[BuildField, list[BuildField]]=None, beta_tester: Union[BetaTesterField, list[BetaTesterField]]=None) -> BetaFeedbackScreenshotSubmissionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_feedback_screenshot_submission: the fields to include for returned resources of type betaFeedbackScreenshotSubmissions
        :type beta_feedback_screenshot_submission: Union[BetaFeedbackScreenshotSubmissionField, list[BetaFeedbackScreenshotSubmissionField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param beta_tester: the fields to include for returned resources of type betaTesters
        :type beta_tester: Union[BetaTesterField, list[BetaTesterField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionsOfAppEndpoint
        '''
        if beta_feedback_screenshot_submission: self._set_fields('betaFeedbackScreenshotSubmissions',beta_feedback_screenshot_submission if type(beta_feedback_screenshot_submission) is list else [beta_feedback_screenshot_submission])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if beta_tester: self._set_fields('betaTesters',beta_tester if type(beta_tester) is list else [beta_tester])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'
        TESTER = 'tester'

    def filter(self, *, device_model: Union[str, list[str]]=None, os_version: Union[str, list[str]]=None, app_platform: Union[AppPlatform, list[AppPlatform]]=None, device_platform: Union[DevicePlatform, list[DevicePlatform]]=None, build: Union[str, list[str]]=None, build_pre_release_version: Union[str, list[str]]=None, tester: Union[str, list[str]]=None) -> BetaFeedbackScreenshotSubmissionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param device_model: filter by attribute 'deviceModel'
        :type device_model: Union[str, list[str]] = None

        :param os_version: filter by attribute 'osVersion'
        :type os_version: Union[str, list[str]] = None

        :param app_platform: filter by attribute 'appPlatform'
        :type app_platform: Union[AppPlatform, list[AppPlatform]] = None

        :param device_platform: filter by attribute 'devicePlatform'
        :type device_platform: Union[DevicePlatform, list[DevicePlatform]] = None

        :param build: filter by id(s) of related 'build'
        :type build: Union[str, list[str]] = None

        :param build_pre_release_version: filter by id(s) of related 'build.preReleaseVersion'
        :type build_pre_release_version: Union[str, list[str]] = None

        :param tester: filter by id(s) of related 'tester'
        :type tester: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionsOfAppEndpoint
        '''
        if device_model: self._set_filter('deviceModel', device_model if type(device_model) is list else [device_model])
        
        if os_version: self._set_filter('osVersion', os_version if type(os_version) is list else [os_version])
        
        if app_platform: self._set_filter('appPlatform', app_platform if type(app_platform) is list else [app_platform])
        
        if device_platform: self._set_filter('devicePlatform', device_platform if type(device_platform) is list else [device_platform])
        
        if build: self._set_filter('build', build if type(build) is list else [build])
        
        if build_pre_release_version: self._set_filter('build.preReleaseVersion', build_pre_release_version if type(build_pre_release_version) is list else [build_pre_release_version])
        
        if tester: self._set_filter('tester', tester if type(tester) is list else [tester])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BetaFeedbackScreenshotSubmissionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, created_date: SortOrder=None) -> BetaFeedbackScreenshotSubmissionsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionsOfAppEndpoint
        '''
        sort_expressions = []
        if created_date: sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None) -> BetaFeedbackScreenshotSubmissionsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaFeedbackScreenshotSubmissionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaFeedbackScreenshotSubmissionsResponse:
        '''Get one or more resources.

        :returns: List of BetaFeedbackScreenshotSubmissions
        :rtype: BetaFeedbackScreenshotSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaFeedbackScreenshotSubmissionsResponse.parse_obj(json)

    def get_all(self) -> BetaFeedbackScreenshotSubmissionsResponse:
        '''
        Get all resources.

        :returns: List of BetaFeedbackScreenshotSubmissions
        :rtype: BetaFeedbackScreenshotSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaFeedbackScreenshotSubmissionsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaFeedbackScreenshotSubmissionsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaGroupsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaGroups'

    def limit(self, number: int=None) -> BetaGroupsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBetaGroupsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBetaGroupsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBetaGroupsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBetaGroupsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBetaGroupsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBetaGroupsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBetaGroupsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaGroupsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaGroups'

    def fields(self, *, beta_group: Union[BetaGroupField, list[BetaGroupField]]=None) -> BetaGroupsOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_group: the fields to include for returned resources of type betaGroups
        :type beta_group: Union[BetaGroupField, list[BetaGroupField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsOfAppEndpoint
        '''
        if beta_group: self._set_fields('betaGroups',beta_group if type(beta_group) is list else [beta_group])
        return self
        
    def limit(self, number: int=None) -> BetaGroupsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaGroupsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BetaGroupsWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of BetaGroups with get
        :rtype: BetaGroupsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaGroupsWithoutIncludesResponse.parse_obj(json)

    def get_all(self) -> BetaGroupsWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of BetaGroups with get
        :rtype: BetaGroupsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BetaGroupsWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BetaGroupsWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaLicenseAgreementLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaLicenseAgreement'

    def get(self) -> AppBetaLicenseAgreementLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppBetaLicenseAgreementLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBetaLicenseAgreementLinkageResponse.parse_obj(json)
class BetaLicenseAgreementOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/betaLicenseAgreement'

    def fields(self, *, beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]]=None) -> BetaLicenseAgreementOfAppEndpoint:
        '''Fields to return for included related types.

        :param beta_license_agreement: the fields to include for returned resources of type betaLicenseAgreements
        :type beta_license_agreement: Union[BetaLicenseAgreementField, list[BetaLicenseAgreementField]] = None

        :returns: self
        :rtype: applaud.endpoints.BetaLicenseAgreementOfAppEndpoint
        '''
        if beta_license_agreement: self._set_fields('betaLicenseAgreements',beta_license_agreement if type(beta_license_agreement) is list else [beta_license_agreement])
        return self
        
    def get(self) -> BetaLicenseAgreementWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single BetaLicenseAgreement with get
        :rtype: BetaLicenseAgreementWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BetaLicenseAgreementWithoutIncludesResponse.parse_obj(json)
class BetaTestersLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/betaTesters'

    def delete(self, request: AppBetaTestersLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: AppBetaTestersLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class BuildUploadsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/buildUploads'

    def limit(self, number: int=None) -> BuildUploadsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBuildUploadsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBuildUploadsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBuildUploadsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBuildUploadsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBuildUploadsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBuildUploadsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBuildUploadsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BuildUploadsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/buildUploads'

    class Platform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, build_upload: Union[BuildUploadField, list[BuildUploadField]]=None, build: Union[BuildField, list[BuildField]]=None, build_upload_file: Union[BuildUploadFileField, list[BuildUploadFileField]]=None) -> BuildUploadsOfAppEndpoint:
        '''Fields to return for included related types.

        :param build_upload: the fields to include for returned resources of type buildUploads
        :type build_upload: Union[BuildUploadField, list[BuildUploadField]] = None

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :param build_upload_file: the fields to include for returned resources of type buildUploadFiles
        :type build_upload_file: Union[BuildUploadFileField, list[BuildUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadsOfAppEndpoint
        '''
        if build_upload: self._set_fields('buildUploads',build_upload if type(build_upload) is list else [build_upload])
        if build: self._set_fields('builds',build if type(build) is list else [build])
        if build_upload_file: self._set_fields('buildUploadFiles',build_upload_file if type(build_upload_file) is list else [build_upload_file])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'
        ASSET_FILE = 'assetFile'
        ASSET_DESCRIPTION_FILE = 'assetDescriptionFile'
        ASSET_SPI_FILE = 'assetSpiFile'

    def filter(self, *, cf_bundle_short_version_string: Union[str, list[str]]=None, cf_bundle_version: Union[str, list[str]]=None, platform: Union[Platform, list[Platform]]=None, state: Union[str, list[str]]=None) -> BuildUploadsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param cf_bundle_short_version_string: filter by attribute 'cfBundleShortVersionString'
        :type cf_bundle_short_version_string: Union[str, list[str]] = None

        :param cf_bundle_version: filter by attribute 'cfBundleVersion'
        :type cf_bundle_version: Union[str, list[str]] = None

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param state: filter by state
        :type state: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadsOfAppEndpoint
        '''
        if cf_bundle_short_version_string: self._set_filter('cfBundleShortVersionString', cf_bundle_short_version_string if type(cf_bundle_short_version_string) is list else [cf_bundle_short_version_string])
        
        if cf_bundle_version: self._set_filter('cfBundleVersion', cf_bundle_version if type(cf_bundle_version) is list else [cf_bundle_version])
        
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> BuildUploadsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildUploadsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, cf_bundle_version: SortOrder=None, uploaded_date: SortOrder=None) -> BuildUploadsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.BuildUploadsOfAppEndpoint
        '''
        sort_expressions = []
        if cf_bundle_version: sort_expressions.append('cfBundleVersion' if cf_bundle_version == SortOrder.ASC else '-cfBundleVersion')
        if uploaded_date: sort_expressions.append('uploadedDate' if uploaded_date == SortOrder.ASC else '-uploadedDate')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None) -> BuildUploadsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildUploadsResponse:
        '''Get one or more resources.

        :returns: List of BuildUploads
        :rtype: BuildUploadsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildUploadsResponse.parse_obj(json)

    def get_all(self) -> BuildUploadsResponse:
        '''
        Get all resources.

        :returns: List of BuildUploads
        :rtype: BuildUploadsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildUploadsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildUploadsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BuildsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/builds'

    def limit(self, number: int=None) -> BuildsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppBuildsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppBuildsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppBuildsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppBuildsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppBuildsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppBuildsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BuildsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/builds'

    def fields(self, *, build: Union[BuildField, list[BuildField]]=None) -> BuildsOfAppEndpoint:
        '''Fields to return for included related types.

        :param build: the fields to include for returned resources of type builds
        :type build: Union[BuildField, list[BuildField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfAppEndpoint
        '''
        if build: self._set_fields('builds',build if type(build) is list else [build])
        return self
        
    def limit(self, number: int=None) -> BuildsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildsOfAppEndpoint
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

    def get_all(self) -> BuildsWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of Builds with get
        :rtype: BuildsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BuildsWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BuildsWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class CiProductLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/ciProduct'

    def get(self) -> AppCiProductLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppCiProductLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCiProductLinkageResponse.parse_obj(json)
class CiProductOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/ciProduct'

    def fields(self, *, ci_product: Union[CiProductField, list[CiProductField]]=None, app: Union[AppField, list[AppField]]=None, bundle_id: Union[BundleIdField, list[BundleIdField]]=None, scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]]=None) -> CiProductOfAppEndpoint:
        '''Fields to return for included related types.

        :param ci_product: the fields to include for returned resources of type ciProducts
        :type ci_product: Union[CiProductField, list[CiProductField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param bundle_id: the fields to include for returned resources of type bundleIds
        :type bundle_id: Union[BundleIdField, list[BundleIdField]] = None

        :param scm_repository: the fields to include for returned resources of type scmRepositories
        :type scm_repository: Union[ScmRepositoryField, list[ScmRepositoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CiProductOfAppEndpoint
        '''
        if ci_product: self._set_fields('ciProducts',ci_product if type(ci_product) is list else [ci_product])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if bundle_id: self._set_fields('bundleIds',bundle_id if type(bundle_id) is list else [bundle_id])
        if scm_repository: self._set_fields('scmRepositories',scm_repository if type(scm_repository) is list else [scm_repository])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        BUNDLE_ID = 'bundleId'
        PRIMARY_REPOSITORIES = 'primaryRepositories'

    def include(self, relationship: Union[Include, list[Include]]) -> CiProductOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CiProductOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, primary_repositories: int=None) -> CiProductOfAppEndpoint:
        '''Number of included related resources to return.

        :param primary_repositories: maximum number of related primaryRepositories returned (when they are included). The maximum limit is 50
        :type primary_repositories: int = None

        :returns: self
        :rtype: applaud.endpoints.CiProductOfAppEndpoint
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

class CustomerReviewSummarizationsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/customerReviewSummarizations'

    class Platform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    def fields(self, *, customer_review_summarization: Union[CustomerReviewSummarizationField, list[CustomerReviewSummarizationField]]=None, territory: Union[TerritoryField, list[TerritoryField]]=None) -> CustomerReviewSummarizationsOfAppEndpoint:
        '''Fields to return for included related types.

        :param customer_review_summarization: the fields to include for returned resources of type customerReviewSummarizations
        :type customer_review_summarization: Union[CustomerReviewSummarizationField, list[CustomerReviewSummarizationField]] = None

        :param territory: the fields to include for returned resources of type territories
        :type territory: Union[TerritoryField, list[TerritoryField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewSummarizationsOfAppEndpoint
        '''
        if customer_review_summarization: self._set_fields('customerReviewSummarizations',customer_review_summarization if type(customer_review_summarization) is list else [customer_review_summarization])
        if territory: self._set_fields('territories',territory if type(territory) is list else [territory])
        return self
        
    class Include(StringEnum):
        TERRITORY = 'territory'

    def filter(self, *, platform: Union[Platform, list[Platform]], territory: Union[str, list[str]]=None) -> CustomerReviewSummarizationsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]]

        :param territory: filter by id(s) of related 'territory'
        :type territory: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewSummarizationsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CustomerReviewSummarizationsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewSummarizationsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> CustomerReviewSummarizationsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewSummarizationsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> CustomerReviewSummarizationsResponse:
        '''Get one or more resources.

        :returns: List of CustomerReviewSummarizations
        :rtype: CustomerReviewSummarizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return CustomerReviewSummarizationsResponse.parse_obj(json)

    def get_all(self) -> CustomerReviewSummarizationsResponse:
        '''
        Get all resources.

        :returns: List of CustomerReviewSummarizations
        :rtype: CustomerReviewSummarizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CustomerReviewSummarizationsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CustomerReviewSummarizationsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class CustomerReviewsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/customerReviews'

    def limit(self, number: int=None) -> CustomerReviewsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCustomerReviewsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppCustomerReviewsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomerReviewsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppCustomerReviewsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppCustomerReviewsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppCustomerReviewsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppCustomerReviewsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class CustomerReviewsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/customerReviews'

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

    def fields(self, *, customer_review: Union[CustomerReviewField, list[CustomerReviewField]]=None, customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]]=None) -> CustomerReviewsOfAppEndpoint:
        '''Fields to return for included related types.

        :param customer_review: the fields to include for returned resources of type customerReviews
        :type customer_review: Union[CustomerReviewField, list[CustomerReviewField]] = None

        :param customer_review_response: the fields to include for returned resources of type customerReviewResponses
        :type customer_review_response: Union[CustomerReviewResponseField, list[CustomerReviewResponseField]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppEndpoint
        '''
        if customer_review: self._set_fields('customerReviews',customer_review if type(customer_review) is list else [customer_review])
        if customer_review_response: self._set_fields('customerReviewResponses',customer_review_response if type(customer_review_response) is list else [customer_review_response])
        return self
        
    class Include(StringEnum):
        RESPONSE = 'response'

    def exists(self, *, published_response: bool=None) -> CustomerReviewsOfAppEndpoint:
        ''' Filter by existence or non-existence of related resource.
        
        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppEndpoint
        '''
        if published_response == None:
            return
        
        self._set_exists('publishedResponse', 'true' if published_response  else 'false')
        return self
        
    def filter(self, *, territory: Union[Territory, list[Territory]]=None, rating: Union[str, list[str]]=None) -> CustomerReviewsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param territory: filter by attribute 'territory'
        :type territory: Union[Territory, list[Territory]] = None

        :param rating: filter by attribute 'rating'
        :type rating: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppEndpoint
        '''
        if territory: self._set_filter('territory', territory if type(territory) is list else [territory])
        
        if rating: self._set_filter('rating', rating if type(rating) is list else [rating])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> CustomerReviewsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, rating: SortOrder=None, created_date: SortOrder=None) -> CustomerReviewsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppEndpoint
        '''
        sort_expressions = []
        if rating: sort_expressions.append('rating' if rating == SortOrder.ASC else '-rating')
        if created_date: sort_expressions.append('createdDate' if created_date == SortOrder.ASC else '-createdDate')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None) -> CustomerReviewsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.CustomerReviewsOfAppEndpoint
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

    def get_all(self) -> CustomerReviewsResponse:
        '''
        Get all resources.

        :returns: List of CustomerReviews
        :rtype: CustomerReviewsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = CustomerReviewsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = CustomerReviewsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class EndUserLicenseAgreementLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/endUserLicenseAgreement'

    def get(self) -> AppEndUserLicenseAgreementLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppEndUserLicenseAgreementLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppEndUserLicenseAgreementLinkageResponse.parse_obj(json)
class EndUserLicenseAgreementOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/endUserLicenseAgreement'

    def fields(self, *, end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]]=None) -> EndUserLicenseAgreementOfAppEndpoint:
        '''Fields to return for included related types.

        :param end_user_license_agreement: the fields to include for returned resources of type endUserLicenseAgreements
        :type end_user_license_agreement: Union[EndUserLicenseAgreementField, list[EndUserLicenseAgreementField]] = None

        :returns: self
        :rtype: applaud.endpoints.EndUserLicenseAgreementOfAppEndpoint
        '''
        if end_user_license_agreement: self._set_fields('endUserLicenseAgreements',end_user_license_agreement if type(end_user_license_agreement) is list else [end_user_license_agreement])
        return self
        
    def get(self) -> EndUserLicenseAgreementWithoutIncludesResponse:
        '''Get the resource.

        :returns: Single EndUserLicenseAgreement with get
        :rtype: EndUserLicenseAgreementWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return EndUserLicenseAgreementWithoutIncludesResponse.parse_obj(json)
class GameCenterDetailLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/gameCenterDetail'

    def get(self) -> AppGameCenterDetailLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppGameCenterDetailLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppGameCenterDetailLinkageResponse.parse_obj(json)
class GameCenterDetailOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/gameCenterDetail'

    def fields(self, *, game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]]=None, app: Union[AppField, list[AppField]]=None, game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]]=None, game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]]=None, game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]]=None, game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]]=None, game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]]=None, game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]]=None, game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]]=None, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None, game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]]=None, game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]]=None, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None) -> GameCenterDetailOfAppEndpoint:
        '''Fields to return for included related types.

        :param game_center_detail: the fields to include for returned resources of type gameCenterDetails
        :type game_center_detail: Union[GameCenterDetailField, list[GameCenterDetailField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param game_center_app_version: the fields to include for returned resources of type gameCenterAppVersions
        :type game_center_app_version: Union[GameCenterAppVersionField, list[GameCenterAppVersionField]] = None

        :param game_center_group: the fields to include for returned resources of type gameCenterGroups
        :type game_center_group: Union[GameCenterGroupField, list[GameCenterGroupField]] = None

        :param game_center_leaderboard: the fields to include for returned resources of type gameCenterLeaderboards
        :type game_center_leaderboard: Union[GameCenterLeaderboardField, list[GameCenterLeaderboardField]] = None

        :param game_center_leaderboard_set: the fields to include for returned resources of type gameCenterLeaderboardSets
        :type game_center_leaderboard_set: Union[GameCenterLeaderboardSetField, list[GameCenterLeaderboardSetField]] = None

        :param game_center_achievement: the fields to include for returned resources of type gameCenterAchievements
        :type game_center_achievement: Union[GameCenterAchievementField, list[GameCenterAchievementField]] = None

        :param game_center_activity: the fields to include for returned resources of type gameCenterActivities
        :type game_center_activity: Union[GameCenterActivityField, list[GameCenterActivityField]] = None

        :param game_center_challenge: the fields to include for returned resources of type gameCenterChallenges
        :type game_center_challenge: Union[GameCenterChallengeField, list[GameCenterChallengeField]] = None

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :param game_center_activity_version_release: the fields to include for returned resources of type gameCenterActivityVersionReleases
        :type game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]] = None

        :param game_center_challenge_version_release: the fields to include for returned resources of type gameCenterChallengeVersionReleases
        :type game_center_challenge_version_release: Union[GameCenterChallengeVersionReleaseField, list[GameCenterChallengeVersionReleaseField]] = None

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailOfAppEndpoint
        '''
        if game_center_detail: self._set_fields('gameCenterDetails',game_center_detail if type(game_center_detail) is list else [game_center_detail])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if game_center_app_version: self._set_fields('gameCenterAppVersions',game_center_app_version if type(game_center_app_version) is list else [game_center_app_version])
        if game_center_group: self._set_fields('gameCenterGroups',game_center_group if type(game_center_group) is list else [game_center_group])
        if game_center_leaderboard: self._set_fields('gameCenterLeaderboards',game_center_leaderboard if type(game_center_leaderboard) is list else [game_center_leaderboard])
        if game_center_leaderboard_set: self._set_fields('gameCenterLeaderboardSets',game_center_leaderboard_set if type(game_center_leaderboard_set) is list else [game_center_leaderboard_set])
        if game_center_achievement: self._set_fields('gameCenterAchievements',game_center_achievement if type(game_center_achievement) is list else [game_center_achievement])
        if game_center_activity: self._set_fields('gameCenterActivities',game_center_activity if type(game_center_activity) is list else [game_center_activity])
        if game_center_challenge: self._set_fields('gameCenterChallenges',game_center_challenge if type(game_center_challenge) is list else [game_center_challenge])
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        if game_center_activity_version_release: self._set_fields('gameCenterActivityVersionReleases',game_center_activity_version_release if type(game_center_activity_version_release) is list else [game_center_activity_version_release])
        if game_center_challenge_version_release: self._set_fields('gameCenterChallengeVersionReleases',game_center_challenge_version_release if type(game_center_challenge_version_release) is list else [game_center_challenge_version_release])
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        GAME_CENTER_APP_VERSIONS = 'gameCenterAppVersions'
        GAME_CENTER_GROUP = 'gameCenterGroup'
        GAME_CENTER_LEADERBOARDS = 'gameCenterLeaderboards'
        GAME_CENTER_LEADERBOARDS_V2 = 'gameCenterLeaderboardsV2'
        GAME_CENTER_LEADERBOARD_SETS = 'gameCenterLeaderboardSets'
        GAME_CENTER_LEADERBOARD_SETS_V2 = 'gameCenterLeaderboardSetsV2'
        GAME_CENTER_ACHIEVEMENTS = 'gameCenterAchievements'
        GAME_CENTER_ACHIEVEMENTS_V2 = 'gameCenterAchievementsV2'
        GAME_CENTER_ACTIVITIES = 'gameCenterActivities'
        GAME_CENTER_CHALLENGES = 'gameCenterChallenges'
        DEFAULT_LEADERBOARD = 'defaultLeaderboard'
        DEFAULT_LEADERBOARD_V2 = 'defaultLeaderboardV2'
        DEFAULT_GROUP_LEADERBOARD = 'defaultGroupLeaderboard'
        DEFAULT_GROUP_LEADERBOARD_V2 = 'defaultGroupLeaderboardV2'
        ACHIEVEMENT_RELEASES = 'achievementReleases'
        ACTIVITY_RELEASES = 'activityReleases'
        CHALLENGE_RELEASES = 'challengeReleases'
        LEADERBOARD_RELEASES = 'leaderboardReleases'
        LEADERBOARD_SET_RELEASES = 'leaderboardSetReleases'
        CHALLENGES_MINIMUM_PLATFORM_VERSIONS = 'challengesMinimumPlatformVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterDetailOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, game_center_app_versions: int=None, game_center_leaderboards: int=None, game_center_leaderboards_v2: int=None, game_center_leaderboard_sets: int=None, game_center_leaderboard_sets_v2: int=None, game_center_achievements: int=None, game_center_achievements_v2: int=None, game_center_activities: int=None, game_center_challenges: int=None, achievement_releases: int=None, activity_releases: int=None, challenge_releases: int=None, leaderboard_releases: int=None, leaderboard_set_releases: int=None, challenges_minimum_platform_versions: int=None) -> GameCenterDetailOfAppEndpoint:
        '''Number of included related resources to return.

        :param game_center_app_versions: maximum number of related gameCenterAppVersions returned (when they are included). The maximum limit is 50
        :type game_center_app_versions: int = None

        :param game_center_leaderboards: maximum number of related gameCenterLeaderboards returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards: int = None

        :param game_center_leaderboards_v2: maximum number of related gameCenterLeaderboardsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboards_v2: int = None

        :param game_center_leaderboard_sets: maximum number of related gameCenterLeaderboardSets returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets: int = None

        :param game_center_leaderboard_sets_v2: maximum number of related gameCenterLeaderboardSetsV2 returned (when they are included). The maximum limit is 50
        :type game_center_leaderboard_sets_v2: int = None

        :param game_center_achievements: maximum number of related gameCenterAchievements returned (when they are included). The maximum limit is 50
        :type game_center_achievements: int = None

        :param game_center_achievements_v2: maximum number of related gameCenterAchievementsV2 returned (when they are included). The maximum limit is 50
        :type game_center_achievements_v2: int = None

        :param game_center_activities: maximum number of related gameCenterActivities returned (when they are included). The maximum limit is 50
        :type game_center_activities: int = None

        :param game_center_challenges: maximum number of related gameCenterChallenges returned (when they are included). The maximum limit is 50
        :type game_center_challenges: int = None

        :param achievement_releases: maximum number of related achievementReleases returned (when they are included). The maximum limit is 50
        :type achievement_releases: int = None

        :param activity_releases: maximum number of related activityReleases returned (when they are included). The maximum limit is 50
        :type activity_releases: int = None

        :param challenge_releases: maximum number of related challengeReleases returned (when they are included). The maximum limit is 50
        :type challenge_releases: int = None

        :param leaderboard_releases: maximum number of related leaderboardReleases returned (when they are included). The maximum limit is 50
        :type leaderboard_releases: int = None

        :param leaderboard_set_releases: maximum number of related leaderboardSetReleases returned (when they are included). The maximum limit is 50
        :type leaderboard_set_releases: int = None

        :param challenges_minimum_platform_versions: maximum number of related challengesMinimumPlatformVersions returned (when they are included). The maximum limit is 50
        :type challenges_minimum_platform_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterDetailOfAppEndpoint
        '''
        if game_center_app_versions and game_center_app_versions > 50:
            raise ValueError(f'The maximum limit of game_center_app_versions is 50')
        if game_center_app_versions: self._set_limit(game_center_app_versions, 'gameCenterAppVersions')

        if game_center_leaderboards and game_center_leaderboards > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards is 50')
        if game_center_leaderboards: self._set_limit(game_center_leaderboards, 'gameCenterLeaderboards')

        if game_center_leaderboards_v2 and game_center_leaderboards_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboards_v2 is 50')
        if game_center_leaderboards_v2: self._set_limit(game_center_leaderboards_v2, 'gameCenterLeaderboardsV2')

        if game_center_leaderboard_sets and game_center_leaderboard_sets > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets is 50')
        if game_center_leaderboard_sets: self._set_limit(game_center_leaderboard_sets, 'gameCenterLeaderboardSets')

        if game_center_leaderboard_sets_v2 and game_center_leaderboard_sets_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_leaderboard_sets_v2 is 50')
        if game_center_leaderboard_sets_v2: self._set_limit(game_center_leaderboard_sets_v2, 'gameCenterLeaderboardSetsV2')

        if game_center_achievements and game_center_achievements > 50:
            raise ValueError(f'The maximum limit of game_center_achievements is 50')
        if game_center_achievements: self._set_limit(game_center_achievements, 'gameCenterAchievements')

        if game_center_achievements_v2 and game_center_achievements_v2 > 50:
            raise ValueError(f'The maximum limit of game_center_achievements_v2 is 50')
        if game_center_achievements_v2: self._set_limit(game_center_achievements_v2, 'gameCenterAchievementsV2')

        if game_center_activities and game_center_activities > 50:
            raise ValueError(f'The maximum limit of game_center_activities is 50')
        if game_center_activities: self._set_limit(game_center_activities, 'gameCenterActivities')

        if game_center_challenges and game_center_challenges > 50:
            raise ValueError(f'The maximum limit of game_center_challenges is 50')
        if game_center_challenges: self._set_limit(game_center_challenges, 'gameCenterChallenges')

        if achievement_releases and achievement_releases > 50:
            raise ValueError(f'The maximum limit of achievement_releases is 50')
        if achievement_releases: self._set_limit(achievement_releases, 'achievementReleases')

        if activity_releases and activity_releases > 50:
            raise ValueError(f'The maximum limit of activity_releases is 50')
        if activity_releases: self._set_limit(activity_releases, 'activityReleases')

        if challenge_releases and challenge_releases > 50:
            raise ValueError(f'The maximum limit of challenge_releases is 50')
        if challenge_releases: self._set_limit(challenge_releases, 'challengeReleases')

        if leaderboard_releases and leaderboard_releases > 50:
            raise ValueError(f'The maximum limit of leaderboard_releases is 50')
        if leaderboard_releases: self._set_limit(leaderboard_releases, 'leaderboardReleases')

        if leaderboard_set_releases and leaderboard_set_releases > 50:
            raise ValueError(f'The maximum limit of leaderboard_set_releases is 50')
        if leaderboard_set_releases: self._set_limit(leaderboard_set_releases, 'leaderboardSetReleases')

        if challenges_minimum_platform_versions and challenges_minimum_platform_versions > 50:
            raise ValueError(f'The maximum limit of challenges_minimum_platform_versions is 50')
        if challenges_minimum_platform_versions: self._set_limit(challenges_minimum_platform_versions, 'challengesMinimumPlatformVersions')

        return self

    def get(self) -> GameCenterDetailResponse:
        '''Get the resource.

        :returns: Single GameCenterDetail
        :rtype: GameCenterDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterDetailResponse.parse_obj(json)

    def get_all(self) -> GameCenterDetailResponse:
        '''
        Get all resources.

        :returns: Single GameCenterDetail
        :rtype: GameCenterDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterDetailResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterDetailResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class GameCenterEnabledVersionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/gameCenterEnabledVersions'

    def limit(self, number: int=None) -> GameCenterEnabledVersionsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> AppGameCenterEnabledVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppGameCenterEnabledVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppGameCenterEnabledVersionsLinkagesResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> AppGameCenterEnabledVersionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppGameCenterEnabledVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppGameCenterEnabledVersionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppGameCenterEnabledVersionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class GameCenterEnabledVersionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/gameCenterEnabledVersions'

    def fields(self, *, game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]]=None, app: Union[AppField, list[AppField]]=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param game_center_enabled_version: the fields to include for returned resources of type gameCenterEnabledVersions
        :type game_center_enabled_version: Union[GameCenterEnabledVersionField, list[GameCenterEnabledVersionField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if game_center_enabled_version: self._set_fields('gameCenterEnabledVersions',game_center_enabled_version if type(game_center_enabled_version) is list else [game_center_enabled_version])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        COMPATIBLE_VERSIONS = 'compatibleVersions'
        APP = 'app'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, version_string: Union[str, list[str]]=None, id: Union[str, list[str]]=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param version_string: filter by attribute 'versionString'
        :type version_string: Union[str, list[str]] = None

        :param id: filter by id(s)
        :type id: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if version_string: self._set_filter('versionString', version_string if type(version_string) is list else [version_string])
        
        if id: self._set_filter('id', id if type(id) is list else [id])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version_string: SortOrder=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        sort_expressions = []
        if version_string: sort_expressions.append('versionString' if version_string == SortOrder.ASC else '-versionString')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None, *, compatible_versions: int=None) -> GameCenterEnabledVersionsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param compatible_versions: maximum number of related compatibleVersions returned (when they are included). The maximum limit is 50
        :type compatible_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterEnabledVersionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if compatible_versions and compatible_versions > 50:
            raise ValueError(f'The maximum limit of compatible_versions is 50')
        if compatible_versions: self._set_limit(compatible_versions, 'compatibleVersions')

        return self

    @deprecated
    def get(self) -> GameCenterEnabledVersionsResponse:
        '''Get one or more resources.

        :returns: List of GameCenterEnabledVersions
        :rtype: GameCenterEnabledVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterEnabledVersionsResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> GameCenterEnabledVersionsResponse:
        '''
        Get all resources.

        :returns: List of GameCenterEnabledVersions
        :rtype: GameCenterEnabledVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = GameCenterEnabledVersionsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = GameCenterEnabledVersionsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class InAppPurchasesLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/inAppPurchases'

    def limit(self, number: int=None) -> InAppPurchasesLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> AppInAppPurchasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppInAppPurchasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInAppPurchasesLinkagesResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> AppInAppPurchasesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppInAppPurchasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppInAppPurchasesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppInAppPurchasesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class InAppPurchasesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/inAppPurchases'

    def fields(self, *, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, app: Union[AppField, list[AppField]]=None) -> InAppPurchasesOfAppEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APPS = 'apps'

    def filter(self, *, in_app_purchase_type: Union[InAppPurchaseType, list[InAppPurchaseType]]=None, can_be_submitted: Union[str, list[str]]=None) -> InAppPurchasesOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param in_app_purchase_type: filter by attribute 'inAppPurchaseType'
        :type in_app_purchase_type: Union[InAppPurchaseType, list[InAppPurchaseType]] = None

        :param can_be_submitted: filter by canBeSubmitted
        :type can_be_submitted: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if in_app_purchase_type: self._set_filter('inAppPurchaseType', in_app_purchase_type if type(in_app_purchase_type) is list else [in_app_purchase_type])
        
        if can_be_submitted: self._set_filter('canBeSubmitted', can_be_submitted if type(can_be_submitted) is list else [can_be_submitted])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchasesOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, reference_name: SortOrder=None, product_id: SortOrder=None, in_app_purchase_type: SortOrder=None) -> InAppPurchasesOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        sort_expressions = []
        if reference_name: sort_expressions.append('referenceName' if reference_name == SortOrder.ASC else '-referenceName')
        if product_id: sort_expressions.append('productId' if product_id == SortOrder.ASC else '-productId')
        if in_app_purchase_type: sort_expressions.append('inAppPurchaseType' if in_app_purchase_type == SortOrder.ASC else '-inAppPurchaseType')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None, *, apps: int=None) -> InAppPurchasesOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param apps: maximum number of related apps returned (when they are included). The maximum limit is 50
        :type apps: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if apps and apps > 50:
            raise ValueError(f'The maximum limit of apps is 50')
        if apps: self._set_limit(apps, 'apps')

        return self

    @deprecated
    def get(self) -> InAppPurchasesResponse:
        '''Get one or more resources.

        :returns: List of InAppPurchases
        :rtype: InAppPurchasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasesResponse.parse_obj(json)

    @deprecated
    def get_all(self) -> InAppPurchasesResponse:
        '''
        Get all resources.

        :returns: List of InAppPurchases
        :rtype: InAppPurchasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = InAppPurchasesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = InAppPurchasesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class InAppPurchasesV2LinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/inAppPurchasesV2'

    def limit(self, number: int=None) -> InAppPurchasesV2LinkageOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesV2LinkageOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppInAppPurchasesV2LinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppInAppPurchasesV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppInAppPurchasesV2LinkagesResponse.parse_obj(json)

    def get_all(self) -> AppInAppPurchasesV2LinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppInAppPurchasesV2LinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppInAppPurchasesV2LinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppInAppPurchasesV2LinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class InAppPurchasesV2OfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/inAppPurchasesV2'

    class State(StringEnum):
        MISSING_METADATA = 'MISSING_METADATA'
        WAITING_FOR_UPLOAD = 'WAITING_FOR_UPLOAD'
        PROCESSING_CONTENT = 'PROCESSING_CONTENT'
        READY_TO_SUBMIT = 'READY_TO_SUBMIT'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        DEVELOPER_ACTION_NEEDED = 'DEVELOPER_ACTION_NEEDED'
        PENDING_BINARY_APPROVAL = 'PENDING_BINARY_APPROVAL'
        APPROVED = 'APPROVED'
        DEVELOPER_REMOVED_FROM_SALE = 'DEVELOPER_REMOVED_FROM_SALE'
        REMOVED_FROM_SALE = 'REMOVED_FROM_SALE'
        REJECTED = 'REJECTED'

    class InAppPurchaseType(StringEnum):
        CONSUMABLE = 'CONSUMABLE'
        NON_CONSUMABLE = 'NON_CONSUMABLE'
        NON_RENEWING_SUBSCRIPTION = 'NON_RENEWING_SUBSCRIPTION'

    def fields(self, *, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]]=None, in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]]=None, in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]]=None, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]]=None, in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]]=None, in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]]=None, in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]]=None) -> InAppPurchasesV2OfAppEndpoint:
        '''Fields to return for included related types.

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param in_app_purchase_localization: the fields to include for returned resources of type inAppPurchaseLocalizations
        :type in_app_purchase_localization: Union[InAppPurchaseLocalizationField, list[InAppPurchaseLocalizationField]] = None

        :param in_app_purchase_content: the fields to include for returned resources of type inAppPurchaseContents
        :type in_app_purchase_content: Union[InAppPurchaseContentField, list[InAppPurchaseContentField]] = None

        :param in_app_purchase_app_store_review_screenshot: the fields to include for returned resources of type inAppPurchaseAppStoreReviewScreenshots
        :type in_app_purchase_app_store_review_screenshot: Union[InAppPurchaseAppStoreReviewScreenshotField, list[InAppPurchaseAppStoreReviewScreenshotField]] = None

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param in_app_purchase_price_schedule: the fields to include for returned resources of type inAppPurchasePriceSchedules
        :type in_app_purchase_price_schedule: Union[InAppPurchasePriceScheduleField, list[InAppPurchasePriceScheduleField]] = None

        :param in_app_purchase_availability: the fields to include for returned resources of type inAppPurchaseAvailabilities
        :type in_app_purchase_availability: Union[InAppPurchaseAvailabilityField, list[InAppPurchaseAvailabilityField]] = None

        :param in_app_purchase_image: the fields to include for returned resources of type inAppPurchaseImages
        :type in_app_purchase_image: Union[InAppPurchaseImageField, list[InAppPurchaseImageField]] = None

        :param in_app_purchase_offer_code: the fields to include for returned resources of type inAppPurchaseOfferCodes
        :type in_app_purchase_offer_code: Union[InAppPurchaseOfferCodeField, list[InAppPurchaseOfferCodeField]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesV2OfAppEndpoint
        '''
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if in_app_purchase_localization: self._set_fields('inAppPurchaseLocalizations',in_app_purchase_localization if type(in_app_purchase_localization) is list else [in_app_purchase_localization])
        if in_app_purchase_content: self._set_fields('inAppPurchaseContents',in_app_purchase_content if type(in_app_purchase_content) is list else [in_app_purchase_content])
        if in_app_purchase_app_store_review_screenshot: self._set_fields('inAppPurchaseAppStoreReviewScreenshots',in_app_purchase_app_store_review_screenshot if type(in_app_purchase_app_store_review_screenshot) is list else [in_app_purchase_app_store_review_screenshot])
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if in_app_purchase_price_schedule: self._set_fields('inAppPurchasePriceSchedules',in_app_purchase_price_schedule if type(in_app_purchase_price_schedule) is list else [in_app_purchase_price_schedule])
        if in_app_purchase_availability: self._set_fields('inAppPurchaseAvailabilities',in_app_purchase_availability if type(in_app_purchase_availability) is list else [in_app_purchase_availability])
        if in_app_purchase_image: self._set_fields('inAppPurchaseImages',in_app_purchase_image if type(in_app_purchase_image) is list else [in_app_purchase_image])
        if in_app_purchase_offer_code: self._set_fields('inAppPurchaseOfferCodes',in_app_purchase_offer_code if type(in_app_purchase_offer_code) is list else [in_app_purchase_offer_code])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_LOCALIZATIONS = 'inAppPurchaseLocalizations'
        CONTENT = 'content'
        APP_STORE_REVIEW_SCREENSHOT = 'appStoreReviewScreenshot'
        PROMOTED_PURCHASE = 'promotedPurchase'
        IAP_PRICE_SCHEDULE = 'iapPriceSchedule'
        IN_APP_PURCHASE_AVAILABILITY = 'inAppPurchaseAvailability'
        IMAGES = 'images'
        OFFER_CODES = 'offerCodes'

    def filter(self, *, product_id: Union[str, list[str]]=None, name: Union[str, list[str]]=None, state: Union[State, list[State]]=None, in_app_purchase_type: Union[InAppPurchaseType, list[InAppPurchaseType]]=None) -> InAppPurchasesV2OfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param product_id: filter by attribute 'productId'
        :type product_id: Union[str, list[str]] = None

        :param name: filter by attribute 'name'
        :type name: Union[str, list[str]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :param in_app_purchase_type: filter by attribute 'inAppPurchaseType'
        :type in_app_purchase_type: Union[InAppPurchaseType, list[InAppPurchaseType]] = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesV2OfAppEndpoint
        '''
        if product_id: self._set_filter('productId', product_id if type(product_id) is list else [product_id])
        
        if name: self._set_filter('name', name if type(name) is list else [name])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        if in_app_purchase_type: self._set_filter('inAppPurchaseType', in_app_purchase_type if type(in_app_purchase_type) is list else [in_app_purchase_type])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> InAppPurchasesV2OfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesV2OfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, name: SortOrder=None, in_app_purchase_type: SortOrder=None) -> InAppPurchasesV2OfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesV2OfAppEndpoint
        '''
        sort_expressions = []
        if name: sort_expressions.append('name' if name == SortOrder.ASC else '-name')
        if in_app_purchase_type: sort_expressions.append('inAppPurchaseType' if in_app_purchase_type == SortOrder.ASC else '-inAppPurchaseType')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None, *, in_app_purchase_localizations: int=None, images: int=None, offer_codes: int=None) -> InAppPurchasesV2OfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param in_app_purchase_localizations: maximum number of related inAppPurchaseLocalizations returned (when they are included). The maximum limit is 50
        :type in_app_purchase_localizations: int = None

        :param images: maximum number of related images returned (when they are included). The maximum limit is 50
        :type images: int = None

        :param offer_codes: maximum number of related offerCodes returned (when they are included). The maximum limit is 50
        :type offer_codes: int = None

        :returns: self
        :rtype: applaud.endpoints.InAppPurchasesV2OfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if in_app_purchase_localizations and in_app_purchase_localizations > 50:
            raise ValueError(f'The maximum limit of in_app_purchase_localizations is 50')
        if in_app_purchase_localizations: self._set_limit(in_app_purchase_localizations, 'inAppPurchaseLocalizations')

        if images and images > 50:
            raise ValueError(f'The maximum limit of images is 50')
        if images: self._set_limit(images, 'images')

        if offer_codes and offer_codes > 50:
            raise ValueError(f'The maximum limit of offer_codes is 50')
        if offer_codes: self._set_limit(offer_codes, 'offerCodes')

        return self

    def get(self) -> InAppPurchasesV2Response:
        '''Get one or more resources.

        :returns: List of InAppPurchases
        :rtype: InAppPurchasesV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return InAppPurchasesV2Response.parse_obj(json)

    def get_all(self) -> InAppPurchasesV2Response:
        '''
        Get all resources.

        :returns: List of InAppPurchases
        :rtype: InAppPurchasesV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = InAppPurchasesV2Response.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = InAppPurchasesV2Response.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class MarketplaceSearchDetailLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/marketplaceSearchDetail'

    def get(self) -> AppMarketplaceSearchDetailLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppMarketplaceSearchDetailLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppMarketplaceSearchDetailLinkageResponse.parse_obj(json)
class MarketplaceSearchDetailOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/marketplaceSearchDetail'

    def fields(self, *, marketplace_search_detail: Union[MarketplaceSearchDetailField, list[MarketplaceSearchDetailField]]=None) -> MarketplaceSearchDetailOfAppEndpoint:
        '''Fields to return for included related types.

        :param marketplace_search_detail: the fields to include for returned resources of type marketplaceSearchDetails
        :type marketplace_search_detail: Union[MarketplaceSearchDetailField, list[MarketplaceSearchDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.MarketplaceSearchDetailOfAppEndpoint
        '''
        if marketplace_search_detail: self._set_fields('marketplaceSearchDetails',marketplace_search_detail if type(marketplace_search_detail) is list else [marketplace_search_detail])
        return self
        
    def get(self) -> MarketplaceSearchDetailResponse:
        '''Get the resource.

        :returns: Single MarketplaceSearchDetail
        :rtype: MarketplaceSearchDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return MarketplaceSearchDetailResponse.parse_obj(json)
class PerfPowerMetricsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/perfPowerMetrics'

    def filter(self, *, platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]]=None, metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]]=None, device_type: Union[str, list[str]]=None) -> PerfPowerMetricsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[PerfPowerMetricPlatform, list[PerfPowerMetricPlatform]] = None

        :param metric_type: filter by attribute 'metricType'
        :type metric_type: Union[PerfPowerMetricType, list[PerfPowerMetricType]] = None

        :param device_type: filter by attribute 'deviceType'
        :type device_type: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.PerfPowerMetricsOfAppEndpoint
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
class PreReleaseVersionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/preReleaseVersions'

    def limit(self, number: int=None) -> PreReleaseVersionsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPreReleaseVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppPreReleaseVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreReleaseVersionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppPreReleaseVersionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppPreReleaseVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppPreReleaseVersionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppPreReleaseVersionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class PreReleaseVersionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/preReleaseVersions'

    def fields(self, *, pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]]=None) -> PreReleaseVersionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param pre_release_version: the fields to include for returned resources of type preReleaseVersions
        :type pre_release_version: Union[PreReleaseVersionField, list[PreReleaseVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsOfAppEndpoint
        '''
        if pre_release_version: self._set_fields('preReleaseVersions',pre_release_version if type(pre_release_version) is list else [pre_release_version])
        return self
        
    def limit(self, number: int=None) -> PreReleaseVersionsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PreReleaseVersionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> PreReleaseVersionsWithoutIncludesResponse:
        '''Get one or more resources.

        :returns: List of PreReleaseVersions with get
        :rtype: PreReleaseVersionsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PreReleaseVersionsWithoutIncludesResponse.parse_obj(json)

    def get_all(self) -> PreReleaseVersionsWithoutIncludesResponse:
        '''
        Get all resources.

        :returns: List of PreReleaseVersions with get
        :rtype: PreReleaseVersionsWithoutIncludesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = PreReleaseVersionsWithoutIncludesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = PreReleaseVersionsWithoutIncludesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class PromotedPurchasesLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/promotedPurchases'

    def limit(self, number: int=None) -> PromotedPurchasesLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchasesLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppPromotedPurchasesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppPromotedPurchasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPromotedPurchasesLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppPromotedPurchasesLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppPromotedPurchasesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppPromotedPurchasesLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppPromotedPurchasesLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

    def update(self, request: AppPromotedPurchasesLinkagesRequest):
        '''Modify one or more related linkages.

        :param request: List of related linkages
        :type request: AppPromotedPurchasesLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_patch(request)

class PromotedPurchasesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/promotedPurchases'

    def fields(self, *, promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]]=None, in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None) -> PromotedPurchasesOfAppEndpoint:
        '''Fields to return for included related types.

        :param promoted_purchase: the fields to include for returned resources of type promotedPurchases
        :type promoted_purchase: Union[PromotedPurchaseField, list[PromotedPurchaseField]] = None

        :param in_app_purchase: the fields to include for returned resources of type inAppPurchases
        :type in_app_purchase: Union[InAppPurchaseField, list[InAppPurchaseField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchasesOfAppEndpoint
        '''
        if promoted_purchase: self._set_fields('promotedPurchases',promoted_purchase if type(promoted_purchase) is list else [promoted_purchase])
        if in_app_purchase: self._set_fields('inAppPurchases',in_app_purchase if type(in_app_purchase) is list else [in_app_purchase])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        return self
        
    class Include(StringEnum):
        IN_APP_PURCHASE_V2 = 'inAppPurchaseV2'
        SUBSCRIPTION = 'subscription'

    def include(self, relationship: Union[Include, list[Include]]) -> PromotedPurchasesOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchasesOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> PromotedPurchasesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.PromotedPurchasesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> PromotedPurchasesResponse:
        '''Get one or more resources.

        :returns: List of PromotedPurchases
        :rtype: PromotedPurchasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return PromotedPurchasesResponse.parse_obj(json)

    def get_all(self) -> PromotedPurchasesResponse:
        '''
        Get all resources.

        :returns: List of PromotedPurchases
        :rtype: PromotedPurchasesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = PromotedPurchasesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = PromotedPurchasesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class ReviewSubmissionsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/reviewSubmissions'

    def limit(self, number: int=None) -> ReviewSubmissionsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppReviewSubmissionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppReviewSubmissionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppReviewSubmissionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppReviewSubmissionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppReviewSubmissionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppReviewSubmissionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppReviewSubmissionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class ReviewSubmissionsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/reviewSubmissions'

    class Platform(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    class State(StringEnum):
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        UNRESOLVED_ISSUES = 'UNRESOLVED_ISSUES'
        CANCELING = 'CANCELING'
        COMPLETING = 'COMPLETING'
        COMPLETE = 'COMPLETE'

    def fields(self, *, review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]]=None, app: Union[AppField, list[AppField]]=None, review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]]=None, app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]]=None, actor: Union[ActorField, list[ActorField]]=None) -> ReviewSubmissionsOfAppEndpoint:
        '''Fields to return for included related types.

        :param review_submission: the fields to include for returned resources of type reviewSubmissions
        :type review_submission: Union[ReviewSubmissionField, list[ReviewSubmissionField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :param review_submission_item: the fields to include for returned resources of type reviewSubmissionItems
        :type review_submission_item: Union[ReviewSubmissionItemField, list[ReviewSubmissionItemField]] = None

        :param app_store_version: the fields to include for returned resources of type appStoreVersions
        :type app_store_version: Union[AppStoreVersionField, list[AppStoreVersionField]] = None

        :param actor: the fields to include for returned resources of type actors
        :type actor: Union[ActorField, list[ActorField]] = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsOfAppEndpoint
        '''
        if review_submission: self._set_fields('reviewSubmissions',review_submission if type(review_submission) is list else [review_submission])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        if review_submission_item: self._set_fields('reviewSubmissionItems',review_submission_item if type(review_submission_item) is list else [review_submission_item])
        if app_store_version: self._set_fields('appStoreVersions',app_store_version if type(app_store_version) is list else [app_store_version])
        if actor: self._set_fields('actors',actor if type(actor) is list else [actor])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        ITEMS = 'items'
        APP_STORE_VERSION_FOR_REVIEW = 'appStoreVersionForReview'
        SUBMITTED_BY_ACTOR = 'submittedByActor'
        LAST_UPDATED_BY_ACTOR = 'lastUpdatedByActor'

    def filter(self, *, platform: Union[Platform, list[Platform]]=None, state: Union[State, list[State]]=None) -> ReviewSubmissionsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by attribute 'platform'
        :type platform: Union[Platform, list[Platform]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> ReviewSubmissionsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, items: int=None) -> ReviewSubmissionsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param items: maximum number of related items returned (when they are included). The maximum limit is 50
        :type items: int = None

        :returns: self
        :rtype: applaud.endpoints.ReviewSubmissionsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if items and items > 50:
            raise ValueError(f'The maximum limit of items is 50')
        if items: self._set_limit(items, 'items')

        return self

    def get(self) -> ReviewSubmissionsResponse:
        '''Get one or more resources.

        :returns: List of ReviewSubmissions
        :rtype: ReviewSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return ReviewSubmissionsResponse.parse_obj(json)

    def get_all(self) -> ReviewSubmissionsResponse:
        '''
        Get all resources.

        :returns: List of ReviewSubmissions
        :rtype: ReviewSubmissionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = ReviewSubmissionsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = ReviewSubmissionsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class SearchKeywordsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/searchKeywords'

    def limit(self, number: int=None) -> SearchKeywordsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppSearchKeywordsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppSearchKeywordsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppSearchKeywordsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppSearchKeywordsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppSearchKeywordsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppSearchKeywordsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppSearchKeywordsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class SearchKeywordsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/searchKeywords'

    def fields(self, *, app_keyword: Union[AppKeywordField, list[AppKeywordField]]=None) -> SearchKeywordsOfAppEndpoint:
        '''Fields to return for included related types.

        :param app_keyword: the fields to include for returned resources of type appKeywords
        :type app_keyword: Union[AppKeywordField, list[AppKeywordField]] = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsOfAppEndpoint
        '''
        if app_keyword: self._set_fields('appKeywords',app_keyword if type(app_keyword) is list else [app_keyword])
        return self
        
    def filter(self, *, platform: Union[str, list[str]]=None, locale: Union[str, list[str]]=None) -> SearchKeywordsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by platform
        :type platform: Union[str, list[str]] = None

        :param locale: filter by locale
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsOfAppEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def limit(self, number: int=None) -> SearchKeywordsOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppKeywordsResponse:
        '''Get one or more resources.

        :returns: List of AppKeywords
        :rtype: AppKeywordsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppKeywordsResponse.parse_obj(json)

    def get_all(self) -> AppKeywordsResponse:
        '''
        Get all resources.

        :returns: List of AppKeywords
        :rtype: AppKeywordsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppKeywordsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppKeywordsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class SubscriptionGracePeriodLinkageOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/subscriptionGracePeriod'

    def get(self) -> AppSubscriptionGracePeriodLinkageResponse:
        '''Get the resource.

        :returns: Related linkage
        :rtype: AppSubscriptionGracePeriodLinkageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppSubscriptionGracePeriodLinkageResponse.parse_obj(json)
class SubscriptionGracePeriodOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/subscriptionGracePeriod'

    def fields(self, *, subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]]=None) -> SubscriptionGracePeriodOfAppEndpoint:
        '''Fields to return for included related types.

        :param subscription_grace_period: the fields to include for returned resources of type subscriptionGracePeriods
        :type subscription_grace_period: Union[SubscriptionGracePeriodField, list[SubscriptionGracePeriodField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGracePeriodOfAppEndpoint
        '''
        if subscription_grace_period: self._set_fields('subscriptionGracePeriods',subscription_grace_period if type(subscription_grace_period) is list else [subscription_grace_period])
        return self
        
    def get(self) -> SubscriptionGracePeriodResponse:
        '''Get the resource.

        :returns: Single SubscriptionGracePeriod
        :rtype: SubscriptionGracePeriodResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGracePeriodResponse.parse_obj(json)
class SubscriptionGroupsLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/subscriptionGroups'

    def limit(self, number: int=None) -> SubscriptionGroupsLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupsLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppSubscriptionGroupsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppSubscriptionGroupsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppSubscriptionGroupsLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppSubscriptionGroupsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppSubscriptionGroupsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppSubscriptionGroupsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppSubscriptionGroupsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class SubscriptionGroupsOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/subscriptionGroups'

    class Subscriptions_state(StringEnum):
        MISSING_METADATA = 'MISSING_METADATA'
        READY_TO_SUBMIT = 'READY_TO_SUBMIT'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        DEVELOPER_ACTION_NEEDED = 'DEVELOPER_ACTION_NEEDED'
        PENDING_BINARY_APPROVAL = 'PENDING_BINARY_APPROVAL'
        APPROVED = 'APPROVED'
        DEVELOPER_REMOVED_FROM_SALE = 'DEVELOPER_REMOVED_FROM_SALE'
        REMOVED_FROM_SALE = 'REMOVED_FROM_SALE'
        REJECTED = 'REJECTED'

    def fields(self, *, subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]]=None, subscription: Union[SubscriptionField, list[SubscriptionField]]=None, subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]]=None) -> SubscriptionGroupsOfAppEndpoint:
        '''Fields to return for included related types.

        :param subscription_group: the fields to include for returned resources of type subscriptionGroups
        :type subscription_group: Union[SubscriptionGroupField, list[SubscriptionGroupField]] = None

        :param subscription: the fields to include for returned resources of type subscriptions
        :type subscription: Union[SubscriptionField, list[SubscriptionField]] = None

        :param subscription_group_localization: the fields to include for returned resources of type subscriptionGroupLocalizations
        :type subscription_group_localization: Union[SubscriptionGroupLocalizationField, list[SubscriptionGroupLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupsOfAppEndpoint
        '''
        if subscription_group: self._set_fields('subscriptionGroups',subscription_group if type(subscription_group) is list else [subscription_group])
        if subscription: self._set_fields('subscriptions',subscription if type(subscription) is list else [subscription])
        if subscription_group_localization: self._set_fields('subscriptionGroupLocalizations',subscription_group_localization if type(subscription_group_localization) is list else [subscription_group_localization])
        return self
        
    class Include(StringEnum):
        SUBSCRIPTIONS = 'subscriptions'
        SUBSCRIPTION_GROUP_LOCALIZATIONS = 'subscriptionGroupLocalizations'

    def filter(self, *, reference_name: Union[str, list[str]]=None, subscriptions_state: Union[Subscriptions_state, list[Subscriptions_state]]=None) -> SubscriptionGroupsOfAppEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param reference_name: filter by attribute 'referenceName'
        :type reference_name: Union[str, list[str]] = None

        :param subscriptions_state: filter by attribute 'subscriptions.state'
        :type subscriptions_state: Union[Subscriptions_state, list[Subscriptions_state]] = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupsOfAppEndpoint
        '''
        if reference_name: self._set_filter('referenceName', reference_name if type(reference_name) is list else [reference_name])
        
        if subscriptions_state: self._set_filter('subscriptions.state', subscriptions_state if type(subscriptions_state) is list else [subscriptions_state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> SubscriptionGroupsOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupsOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, reference_name: SortOrder=None) -> SubscriptionGroupsOfAppEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupsOfAppEndpoint
        '''
        sort_expressions = []
        if reference_name: sort_expressions.append('referenceName' if reference_name == SortOrder.ASC else '-referenceName')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None, *, subscriptions: int=None, subscription_group_localizations: int=None) -> SubscriptionGroupsOfAppEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param subscriptions: maximum number of related subscriptions returned (when they are included). The maximum limit is 50
        :type subscriptions: int = None

        :param subscription_group_localizations: maximum number of related subscriptionGroupLocalizations returned (when they are included). The maximum limit is 50
        :type subscription_group_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.SubscriptionGroupsOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if subscriptions and subscriptions > 50:
            raise ValueError(f'The maximum limit of subscriptions is 50')
        if subscriptions: self._set_limit(subscriptions, 'subscriptions')

        if subscription_group_localizations and subscription_group_localizations > 50:
            raise ValueError(f'The maximum limit of subscription_group_localizations is 50')
        if subscription_group_localizations: self._set_limit(subscription_group_localizations, 'subscriptionGroupLocalizations')

        return self

    def get(self) -> SubscriptionGroupsResponse:
        '''Get one or more resources.

        :returns: List of SubscriptionGroups
        :rtype: SubscriptionGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return SubscriptionGroupsResponse.parse_obj(json)

    def get_all(self) -> SubscriptionGroupsResponse:
        '''
        Get all resources.

        :returns: List of SubscriptionGroups
        :rtype: SubscriptionGroupsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = SubscriptionGroupsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = SubscriptionGroupsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class WebhooksLinkagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/relationships/webhooks'

    def limit(self, number: int=None) -> WebhooksLinkagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.WebhooksLinkagesOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppWebhooksLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppWebhooksLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppWebhooksLinkagesResponse.parse_obj(json)

    def get_all(self) -> AppWebhooksLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: AppWebhooksLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppWebhooksLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppWebhooksLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class WebhooksOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/webhooks'

    def fields(self, *, webhook: Union[WebhookField, list[WebhookField]]=None, app: Union[AppField, list[AppField]]=None) -> WebhooksOfAppEndpoint:
        '''Fields to return for included related types.

        :param webhook: the fields to include for returned resources of type webhooks
        :type webhook: Union[WebhookField, list[WebhookField]] = None

        :param app: the fields to include for returned resources of type apps
        :type app: Union[AppField, list[AppField]] = None

        :returns: self
        :rtype: applaud.endpoints.WebhooksOfAppEndpoint
        '''
        if webhook: self._set_fields('webhooks',webhook if type(webhook) is list else [webhook])
        if app: self._set_fields('apps',app if type(app) is list else [app])
        return self
        
    class Include(StringEnum):
        APP = 'app'

    def include(self, relationship: Union[Include, list[Include]]) -> WebhooksOfAppEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.WebhooksOfAppEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None) -> WebhooksOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.WebhooksOfAppEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> WebhooksResponse:
        '''Get one or more resources.

        :returns: List of Webhooks
        :rtype: WebhooksResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return WebhooksResponse.parse_obj(json)

    def get_all(self) -> WebhooksResponse:
        '''
        Get all resources.

        :returns: List of Webhooks
        :rtype: WebhooksResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = WebhooksResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = WebhooksResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class BetaTesterUsagesOfAppEndpoint(IDEndpoint):
    path = '/v1/apps/{id}/metrics/betaTesterUsages'

    def limit(self, number: int=None) -> BetaTesterUsagesOfAppEndpoint:
        '''Number of resources to return.

        :param number: maximum number of groups to return per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BetaTesterUsagesOfAppEndpoint
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

    def get_all(self) -> AppsBetaTesterUsagesV1MetricResponse:
        '''
        Get all resources.

        :returns: Metrics data response
        :rtype: AppsBetaTesterUsagesV1MetricResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = AppsBetaTesterUsagesV1MetricResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = AppsBetaTesterUsagesV1MetricResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

