from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppCustomProductPageLocalizationsEndpoint(Endpoint):
    path = '/v1/appCustomProductPageLocalizations'

    def create(self, request: AppCustomProductPageLocalizationCreateRequest) -> AppCustomProductPageLocalizationResponse:
        '''Create the resource.

        :param request: AppCustomProductPageLocalization representation
        :type request: AppCustomProductPageLocalizationCreateRequest

        :returns: Single AppCustomProductPageLocalization
        :rtype: AppCustomProductPageLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppCustomProductPageLocalizationResponse.parse_obj(json)

class AppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}'

    @endpoint('/v1/appCustomProductPageLocalizations/{id}/appPreviewSets')
    def app_preview_sets(self) -> AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint:
        return AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPageLocalizations/{id}/appScreenshotSets')
    def app_screenshot_sets(self) -> AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint:
        return AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPageLocalizations/{id}/searchKeywords')
    def search_keywords(self) -> SearchKeywordsOfAppCustomProductPageLocalizationEndpoint:
        return SearchKeywordsOfAppCustomProductPageLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPageLocalizations/{id}/relationships/appPreviewSets')
    def app_preview_sets_linkages(self) -> AppPreviewSetsLinkagesOfAppCustomProductPageLocalizationEndpoint:
        return AppPreviewSetsLinkagesOfAppCustomProductPageLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPageLocalizations/{id}/relationships/appScreenshotSets')
    def app_screenshot_sets_linkages(self) -> AppScreenshotSetsLinkagesOfAppCustomProductPageLocalizationEndpoint:
        return AppScreenshotSetsLinkagesOfAppCustomProductPageLocalizationEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPageLocalizations/{id}/relationships/searchKeywords')
    def search_keywords_linkages(self) -> SearchKeywordsLinkagesOfAppCustomProductPageLocalizationEndpoint:
        return SearchKeywordsLinkagesOfAppCustomProductPageLocalizationEndpoint(self.id, self.session)
        
    def fields(self, *, app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]]=None, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None) -> AppCustomProductPageLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_custom_product_page_localization: the fields to include for returned resources of type appCustomProductPageLocalizations
        :type app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]] = None

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationEndpoint
        '''
        if app_custom_product_page_localization: self._set_fields('appCustomProductPageLocalizations',app_custom_product_page_localization if type(app_custom_product_page_localization) is list else [app_custom_product_page_localization])
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        return self
        
    class Include(StringEnum):
        APP_CUSTOM_PRODUCT_PAGE_VERSION = 'appCustomProductPageVersion'
        APP_SCREENSHOT_SETS = 'appScreenshotSets'
        APP_PREVIEW_SETS = 'appPreviewSets'
        SEARCH_KEYWORDS = 'searchKeywords'

    def include(self, relationship: Union[Include, list[Include]]) -> AppCustomProductPageLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_preview_sets: int=None, app_screenshot_sets: int=None, search_keywords: int=None) -> AppCustomProductPageLocalizationEndpoint:
        '''Number of included related resources to return.

        :param app_preview_sets: maximum number of related appPreviewSets returned (when they are included). The maximum limit is 50
        :type app_preview_sets: int = None

        :param app_screenshot_sets: maximum number of related appScreenshotSets returned (when they are included). The maximum limit is 50
        :type app_screenshot_sets: int = None

        :param search_keywords: maximum number of related searchKeywords returned (when they are included). The maximum limit is 50
        :type search_keywords: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationEndpoint
        '''
        if app_preview_sets and app_preview_sets > 50:
            raise ValueError(f'The maximum limit of app_preview_sets is 50')
        if app_preview_sets: self._set_limit(app_preview_sets, 'appPreviewSets')

        if app_screenshot_sets and app_screenshot_sets > 50:
            raise ValueError(f'The maximum limit of app_screenshot_sets is 50')
        if app_screenshot_sets: self._set_limit(app_screenshot_sets, 'appScreenshotSets')

        if search_keywords and search_keywords > 50:
            raise ValueError(f'The maximum limit of search_keywords is 50')
        if search_keywords: self._set_limit(search_keywords, 'searchKeywords')

        return self

    def get(self) -> AppCustomProductPageLocalizationResponse:
        '''Get the resource.

        :returns: Single AppCustomProductPageLocalization
        :rtype: AppCustomProductPageLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageLocalizationResponse.parse_obj(json)

    def update(self, request: AppCustomProductPageLocalizationUpdateRequest) -> AppCustomProductPageLocalizationResponse:
        '''Modify the resource.

        :param request: AppCustomProductPageLocalization representation
        :type request: AppCustomProductPageLocalizationUpdateRequest

        :returns: Single AppCustomProductPageLocalization
        :rtype: AppCustomProductPageLocalizationResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppCustomProductPageLocalizationResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppPreviewSetsLinkagesOfAppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}/relationships/appPreviewSets'

    def limit(self, number: int=None) -> AppPreviewSetsLinkagesOfAppCustomProductPageLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsLinkagesOfAppCustomProductPageLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCustomProductPageLocalizationAppPreviewSetsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppCustomProductPageLocalizationAppPreviewSetsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageLocalizationAppPreviewSetsLinkagesResponse.parse_obj(json)

class AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}/appPreviewSets'

    class PreviewType(StringEnum):
        IPHONE_67 = 'IPHONE_67'
        IPHONE_61 = 'IPHONE_61'
        IPHONE_65 = 'IPHONE_65'
        IPHONE_58 = 'IPHONE_58'
        IPHONE_55 = 'IPHONE_55'
        IPHONE_47 = 'IPHONE_47'
        IPHONE_40 = 'IPHONE_40'
        IPHONE_35 = 'IPHONE_35'
        IPAD_PRO_3GEN_129 = 'IPAD_PRO_3GEN_129'
        IPAD_PRO_3GEN_11 = 'IPAD_PRO_3GEN_11'
        IPAD_PRO_129 = 'IPAD_PRO_129'
        IPAD_105 = 'IPAD_105'
        IPAD_97 = 'IPAD_97'
        DESKTOP = 'DESKTOP'
        APPLE_TV = 'APPLE_TV'
        APPLE_VISION_PRO = 'APPLE_VISION_PRO'

    def fields(self, *, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]]=None, app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]]=None, app_preview: Union[AppPreviewField, list[AppPreviewField]]=None) -> AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :param app_custom_product_page_localization: the fields to include for returned resources of type appCustomProductPageLocalizations
        :type app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]] = None

        :param app_store_version_experiment_treatment_localization: the fields to include for returned resources of type appStoreVersionExperimentTreatmentLocalizations
        :type app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]] = None

        :param app_preview: the fields to include for returned resources of type appPreviews
        :type app_preview: Union[AppPreviewField, list[AppPreviewField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        if app_custom_product_page_localization: self._set_fields('appCustomProductPageLocalizations',app_custom_product_page_localization if type(app_custom_product_page_localization) is list else [app_custom_product_page_localization])
        if app_store_version_experiment_treatment_localization: self._set_fields('appStoreVersionExperimentTreatmentLocalizations',app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        if app_preview: self._set_fields('appPreviews',app_preview if type(app_preview) is list else [app_preview])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_LOCALIZATION = 'appStoreVersionLocalization'
        APP_CUSTOM_PRODUCT_PAGE_LOCALIZATION = 'appCustomProductPageLocalization'
        APP_STORE_VERSION_EXPERIMENT_TREATMENT_LOCALIZATION = 'appStoreVersionExperimentTreatmentLocalization'
        APP_PREVIEWS = 'appPreviews'

    def filter(self, *, preview_type: Union[PreviewType, list[PreviewType]]=None, app_store_version_localization: Union[str, list[str]]=None, app_store_version_experiment_treatment_localization: Union[str, list[str]]=None) -> AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param preview_type: filter by attribute 'previewType'
        :type preview_type: Union[PreviewType, list[PreviewType]] = None

        :param app_store_version_localization: filter by id(s) of related 'appStoreVersionLocalization'
        :type app_store_version_localization: Union[str, list[str]] = None

        :param app_store_version_experiment_treatment_localization: filter by id(s) of related 'appStoreVersionExperimentTreatmentLocalization'
        :type app_store_version_experiment_treatment_localization: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if preview_type: self._set_filter('previewType', preview_type if type(preview_type) is list else [preview_type])
        
        if app_store_version_localization: self._set_filter('appStoreVersionLocalization', app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        
        if app_store_version_experiment_treatment_localization: self._set_filter('appStoreVersionExperimentTreatmentLocalization', app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_previews: int=None) -> AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_previews: maximum number of related appPreviews returned (when they are included). The maximum limit is 50
        :type app_previews: int = None

        :returns: self
        :rtype: applaud.endpoints.AppPreviewSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_previews and app_previews > 50:
            raise ValueError(f'The maximum limit of app_previews is 50')
        if app_previews: self._set_limit(app_previews, 'appPreviews')

        return self

    def get(self) -> AppPreviewSetsResponse:
        '''Get one or more resources.

        :returns: List of AppPreviewSets
        :rtype: AppPreviewSetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppPreviewSetsResponse.parse_obj(json)

class AppScreenshotSetsLinkagesOfAppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}/relationships/appScreenshotSets'

    def limit(self, number: int=None) -> AppScreenshotSetsLinkagesOfAppCustomProductPageLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsLinkagesOfAppCustomProductPageLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCustomProductPageLocalizationAppScreenshotSetsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppCustomProductPageLocalizationAppScreenshotSetsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageLocalizationAppScreenshotSetsLinkagesResponse.parse_obj(json)

class AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}/appScreenshotSets'

    class ScreenshotDisplayType(StringEnum):
        APP_IPHONE_67 = 'APP_IPHONE_67'
        APP_IPHONE_61 = 'APP_IPHONE_61'
        APP_IPHONE_65 = 'APP_IPHONE_65'
        APP_IPHONE_58 = 'APP_IPHONE_58'
        APP_IPHONE_55 = 'APP_IPHONE_55'
        APP_IPHONE_47 = 'APP_IPHONE_47'
        APP_IPHONE_40 = 'APP_IPHONE_40'
        APP_IPHONE_35 = 'APP_IPHONE_35'
        APP_IPAD_PRO_3GEN_129 = 'APP_IPAD_PRO_3GEN_129'
        APP_IPAD_PRO_3GEN_11 = 'APP_IPAD_PRO_3GEN_11'
        APP_IPAD_PRO_129 = 'APP_IPAD_PRO_129'
        APP_IPAD_105 = 'APP_IPAD_105'
        APP_IPAD_97 = 'APP_IPAD_97'
        APP_DESKTOP = 'APP_DESKTOP'
        APP_WATCH_ULTRA = 'APP_WATCH_ULTRA'
        APP_WATCH_SERIES_10 = 'APP_WATCH_SERIES_10'
        APP_WATCH_SERIES_7 = 'APP_WATCH_SERIES_7'
        APP_WATCH_SERIES_4 = 'APP_WATCH_SERIES_4'
        APP_WATCH_SERIES_3 = 'APP_WATCH_SERIES_3'
        APP_APPLE_TV = 'APP_APPLE_TV'
        APP_APPLE_VISION_PRO = 'APP_APPLE_VISION_PRO'
        IMESSAGE_APP_IPHONE_67 = 'IMESSAGE_APP_IPHONE_67'
        IMESSAGE_APP_IPHONE_61 = 'IMESSAGE_APP_IPHONE_61'
        IMESSAGE_APP_IPHONE_65 = 'IMESSAGE_APP_IPHONE_65'
        IMESSAGE_APP_IPHONE_58 = 'IMESSAGE_APP_IPHONE_58'
        IMESSAGE_APP_IPHONE_55 = 'IMESSAGE_APP_IPHONE_55'
        IMESSAGE_APP_IPHONE_47 = 'IMESSAGE_APP_IPHONE_47'
        IMESSAGE_APP_IPHONE_40 = 'IMESSAGE_APP_IPHONE_40'
        IMESSAGE_APP_IPAD_PRO_3GEN_129 = 'IMESSAGE_APP_IPAD_PRO_3GEN_129'
        IMESSAGE_APP_IPAD_PRO_3GEN_11 = 'IMESSAGE_APP_IPAD_PRO_3GEN_11'
        IMESSAGE_APP_IPAD_PRO_129 = 'IMESSAGE_APP_IPAD_PRO_129'
        IMESSAGE_APP_IPAD_105 = 'IMESSAGE_APP_IPAD_105'
        IMESSAGE_APP_IPAD_97 = 'IMESSAGE_APP_IPAD_97'

    def fields(self, *, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]]=None, app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]]=None, app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]]=None, app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]]=None) -> AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_store_version_localization: the fields to include for returned resources of type appStoreVersionLocalizations
        :type app_store_version_localization: Union[AppStoreVersionLocalizationField, list[AppStoreVersionLocalizationField]] = None

        :param app_custom_product_page_localization: the fields to include for returned resources of type appCustomProductPageLocalizations
        :type app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]] = None

        :param app_store_version_experiment_treatment_localization: the fields to include for returned resources of type appStoreVersionExperimentTreatmentLocalizations
        :type app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]] = None

        :param app_screenshot: the fields to include for returned resources of type appScreenshots
        :type app_screenshot: Union[AppScreenshotField, list[AppScreenshotField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_store_version_localization: self._set_fields('appStoreVersionLocalizations',app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        if app_custom_product_page_localization: self._set_fields('appCustomProductPageLocalizations',app_custom_product_page_localization if type(app_custom_product_page_localization) is list else [app_custom_product_page_localization])
        if app_store_version_experiment_treatment_localization: self._set_fields('appStoreVersionExperimentTreatmentLocalizations',app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        if app_screenshot: self._set_fields('appScreenshots',app_screenshot if type(app_screenshot) is list else [app_screenshot])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_LOCALIZATION = 'appStoreVersionLocalization'
        APP_CUSTOM_PRODUCT_PAGE_LOCALIZATION = 'appCustomProductPageLocalization'
        APP_STORE_VERSION_EXPERIMENT_TREATMENT_LOCALIZATION = 'appStoreVersionExperimentTreatmentLocalization'
        APP_SCREENSHOTS = 'appScreenshots'

    def filter(self, *, screenshot_display_type: Union[ScreenshotDisplayType, list[ScreenshotDisplayType]]=None, app_store_version_localization: Union[str, list[str]]=None, app_store_version_experiment_treatment_localization: Union[str, list[str]]=None) -> AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param screenshot_display_type: filter by attribute 'screenshotDisplayType'
        :type screenshot_display_type: Union[ScreenshotDisplayType, list[ScreenshotDisplayType]] = None

        :param app_store_version_localization: filter by id(s) of related 'appStoreVersionLocalization'
        :type app_store_version_localization: Union[str, list[str]] = None

        :param app_store_version_experiment_treatment_localization: filter by id(s) of related 'appStoreVersionExperimentTreatmentLocalization'
        :type app_store_version_experiment_treatment_localization: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if screenshot_display_type: self._set_filter('screenshotDisplayType', screenshot_display_type if type(screenshot_display_type) is list else [screenshot_display_type])
        
        if app_store_version_localization: self._set_filter('appStoreVersionLocalization', app_store_version_localization if type(app_store_version_localization) is list else [app_store_version_localization])
        
        if app_store_version_experiment_treatment_localization: self._set_filter('appStoreVersionExperimentTreatmentLocalization', app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_screenshots: int=None) -> AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_screenshots: maximum number of related appScreenshots returned (when they are included). The maximum limit is 50
        :type app_screenshots: int = None

        :returns: self
        :rtype: applaud.endpoints.AppScreenshotSetsOfAppCustomProductPageLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_screenshots and app_screenshots > 50:
            raise ValueError(f'The maximum limit of app_screenshots is 50')
        if app_screenshots: self._set_limit(app_screenshots, 'appScreenshots')

        return self

    def get(self) -> AppScreenshotSetsResponse:
        '''Get one or more resources.

        :returns: List of AppScreenshotSets
        :rtype: AppScreenshotSetsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppScreenshotSetsResponse.parse_obj(json)

class SearchKeywordsLinkagesOfAppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}/relationships/searchKeywords'

    def limit(self, number: int=None) -> SearchKeywordsLinkagesOfAppCustomProductPageLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsLinkagesOfAppCustomProductPageLocalizationEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCustomProductPageLocalizationSearchKeywordsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppCustomProductPageLocalizationSearchKeywordsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageLocalizationSearchKeywordsLinkagesResponse.parse_obj(json)

    def create(self, request: AppCustomProductPageLocalizationSearchKeywordsLinkagesRequest):
        '''Create one or more related linkages.

        :param request: List of related linkages
        :type request: AppCustomProductPageLocalizationSearchKeywordsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_post(request)

    def delete(self, request: AppCustomProductPageLocalizationSearchKeywordsLinkagesRequest):
        '''Delete one or more related linkages.

        :param request: List of related linkages
        :type request: AppCustomProductPageLocalizationSearchKeywordsLinkagesRequest

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete(request)

class SearchKeywordsOfAppCustomProductPageLocalizationEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageLocalizations/{id}/searchKeywords'

    def fields(self, *, app_keyword: Union[AppKeywordField, list[AppKeywordField]]=None) -> SearchKeywordsOfAppCustomProductPageLocalizationEndpoint:
        '''Fields to return for included related types.

        :param app_keyword: the fields to include for returned resources of type appKeywords
        :type app_keyword: Union[AppKeywordField, list[AppKeywordField]] = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsOfAppCustomProductPageLocalizationEndpoint
        '''
        if app_keyword: self._set_fields('appKeywords',app_keyword if type(app_keyword) is list else [app_keyword])
        return self
        
    def filter(self, *, platform: Union[str, list[str]]=None, locale: Union[str, list[str]]=None) -> SearchKeywordsOfAppCustomProductPageLocalizationEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platform: filter by platform
        :type platform: Union[str, list[str]] = None

        :param locale: filter by locale
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsOfAppCustomProductPageLocalizationEndpoint
        '''
        if platform: self._set_filter('platform', platform if type(platform) is list else [platform])
        
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def limit(self, number: int=None) -> SearchKeywordsOfAppCustomProductPageLocalizationEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.SearchKeywordsOfAppCustomProductPageLocalizationEndpoint
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

