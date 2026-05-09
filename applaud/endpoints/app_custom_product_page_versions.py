from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppCustomProductPageVersionsEndpoint(Endpoint):
    path = '/v1/appCustomProductPageVersions'

    def create(self, request: AppCustomProductPageVersionCreateRequest) -> AppCustomProductPageVersionResponse:
        '''Create the resource.

        :param request: AppCustomProductPageVersion representation
        :type request: AppCustomProductPageVersionCreateRequest

        :returns: Single AppCustomProductPageVersion
        :rtype: AppCustomProductPageVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppCustomProductPageVersionResponse.parse_obj(json)

class AppCustomProductPageVersionEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageVersions/{id}'

    @endpoint('/v1/appCustomProductPageVersions/{id}/appCustomProductPageLocalizations')
    def app_custom_product_page_localizations(self) -> AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint:
        return AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPageVersions/{id}/relationships/appCustomProductPageLocalizations')
    def app_custom_product_page_localizations_linkages(self) -> AppCustomProductPageLocalizationsLinkagesOfAppCustomProductPageVersionEndpoint:
        return AppCustomProductPageLocalizationsLinkagesOfAppCustomProductPageVersionEndpoint(self.id, self.session)
        
    def fields(self, *, app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]]=None, app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]]=None) -> AppCustomProductPageVersionEndpoint:
        '''Fields to return for included related types.

        :param app_custom_product_page_version: the fields to include for returned resources of type appCustomProductPageVersions
        :type app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]] = None

        :param app_custom_product_page_localization: the fields to include for returned resources of type appCustomProductPageLocalizations
        :type app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionEndpoint
        '''
        if app_custom_product_page_version: self._set_fields('appCustomProductPageVersions',app_custom_product_page_version if type(app_custom_product_page_version) is list else [app_custom_product_page_version])
        if app_custom_product_page_localization: self._set_fields('appCustomProductPageLocalizations',app_custom_product_page_localization if type(app_custom_product_page_localization) is list else [app_custom_product_page_localization])
        return self
        
    class Include(StringEnum):
        APP_CUSTOM_PRODUCT_PAGE = 'appCustomProductPage'
        APP_CUSTOM_PRODUCT_PAGE_LOCALIZATIONS = 'appCustomProductPageLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppCustomProductPageVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_custom_product_page_localizations: int=None) -> AppCustomProductPageVersionEndpoint:
        '''Number of included related resources to return.

        :param app_custom_product_page_localizations: maximum number of related appCustomProductPageLocalizations returned (when they are included). The maximum limit is 50
        :type app_custom_product_page_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionEndpoint
        '''
        if app_custom_product_page_localizations and app_custom_product_page_localizations > 50:
            raise ValueError(f'The maximum limit of app_custom_product_page_localizations is 50')
        if app_custom_product_page_localizations: self._set_limit(app_custom_product_page_localizations, 'appCustomProductPageLocalizations')

        return self

    def get(self) -> AppCustomProductPageVersionResponse:
        '''Get the resource.

        :returns: Single AppCustomProductPageVersion
        :rtype: AppCustomProductPageVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageVersionResponse.parse_obj(json)

    def update(self, request: AppCustomProductPageVersionUpdateRequest) -> AppCustomProductPageVersionResponse:
        '''Modify the resource.

        :param request: AppCustomProductPageVersion representation
        :type request: AppCustomProductPageVersionUpdateRequest

        :returns: Single AppCustomProductPageVersion
        :rtype: AppCustomProductPageVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppCustomProductPageVersionResponse.parse_obj(json)

class AppCustomProductPageLocalizationsLinkagesOfAppCustomProductPageVersionEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageVersions/{id}/relationships/appCustomProductPageLocalizations'

    def limit(self, number: int=None) -> AppCustomProductPageLocalizationsLinkagesOfAppCustomProductPageVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationsLinkagesOfAppCustomProductPageVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCustomProductPageVersionAppCustomProductPageLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppCustomProductPageVersionAppCustomProductPageLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageVersionAppCustomProductPageLocalizationsLinkagesResponse.parse_obj(json)

class AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPageVersions/{id}/appCustomProductPageLocalizations'

    def fields(self, *, app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]]=None, app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]]=None, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None, app_keyword: Union[AppKeywordField, list[AppKeywordField]]=None) -> AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint:
        '''Fields to return for included related types.

        :param app_custom_product_page_localization: the fields to include for returned resources of type appCustomProductPageLocalizations
        :type app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]] = None

        :param app_custom_product_page_version: the fields to include for returned resources of type appCustomProductPageVersions
        :type app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]] = None

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :param app_keyword: the fields to include for returned resources of type appKeywords
        :type app_keyword: Union[AppKeywordField, list[AppKeywordField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint
        '''
        if app_custom_product_page_localization: self._set_fields('appCustomProductPageLocalizations',app_custom_product_page_localization if type(app_custom_product_page_localization) is list else [app_custom_product_page_localization])
        if app_custom_product_page_version: self._set_fields('appCustomProductPageVersions',app_custom_product_page_version if type(app_custom_product_page_version) is list else [app_custom_product_page_version])
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        if app_keyword: self._set_fields('appKeywords',app_keyword if type(app_keyword) is list else [app_keyword])
        return self
        
    class Include(StringEnum):
        APP_CUSTOM_PRODUCT_PAGE_VERSION = 'appCustomProductPageVersion'
        APP_SCREENSHOT_SETS = 'appScreenshotSets'
        APP_PREVIEW_SETS = 'appPreviewSets'
        SEARCH_KEYWORDS = 'searchKeywords'

    def filter(self, *, locale: Union[str, list[str]]=None) -> AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_screenshot_sets: int=None, app_preview_sets: int=None, search_keywords: int=None) -> AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint:
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
        :rtype: applaud.endpoints.AppCustomProductPageLocalizationsOfAppCustomProductPageVersionEndpoint
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

    def get(self) -> AppCustomProductPageLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of AppCustomProductPageLocalizations
        :rtype: AppCustomProductPageLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageLocalizationsResponse.parse_obj(json)

