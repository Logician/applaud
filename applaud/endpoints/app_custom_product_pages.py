from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppCustomProductPagesEndpoint(Endpoint):
    path = '/v1/appCustomProductPages'

    def create(self, request: AppCustomProductPageCreateRequest) -> AppCustomProductPageResponse:
        '''Create the resource.

        :param request: AppCustomProductPage representation
        :type request: AppCustomProductPageCreateRequest

        :returns: Single AppCustomProductPage
        :rtype: AppCustomProductPageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppCustomProductPageResponse.parse_obj(json)

class AppCustomProductPageEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPages/{id}'

    @endpoint('/v1/appCustomProductPages/{id}/appCustomProductPageVersions')
    def app_custom_product_page_versions(self) -> AppCustomProductPageVersionsOfAppCustomProductPageEndpoint:
        return AppCustomProductPageVersionsOfAppCustomProductPageEndpoint(self.id, self.session)
        
    @endpoint('/v1/appCustomProductPages/{id}/relationships/appCustomProductPageVersions')
    def app_custom_product_page_versions_linkages(self) -> AppCustomProductPageVersionsLinkagesOfAppCustomProductPageEndpoint:
        return AppCustomProductPageVersionsLinkagesOfAppCustomProductPageEndpoint(self.id, self.session)
        
    def fields(self, *, app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]]=None, app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]]=None) -> AppCustomProductPageEndpoint:
        '''Fields to return for included related types.

        :param app_custom_product_page: the fields to include for returned resources of type appCustomProductPages
        :type app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]] = None

        :param app_custom_product_page_version: the fields to include for returned resources of type appCustomProductPageVersions
        :type app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageEndpoint
        '''
        if app_custom_product_page: self._set_fields('appCustomProductPages',app_custom_product_page if type(app_custom_product_page) is list else [app_custom_product_page])
        if app_custom_product_page_version: self._set_fields('appCustomProductPageVersions',app_custom_product_page_version if type(app_custom_product_page_version) is list else [app_custom_product_page_version])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_CUSTOM_PRODUCT_PAGE_VERSIONS = 'appCustomProductPageVersions'

    def include(self, relationship: Union[Include, list[Include]]) -> AppCustomProductPageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_custom_product_page_versions: int=None) -> AppCustomProductPageEndpoint:
        '''Number of included related resources to return.

        :param app_custom_product_page_versions: maximum number of related appCustomProductPageVersions returned (when they are included). The maximum limit is 50
        :type app_custom_product_page_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageEndpoint
        '''
        if app_custom_product_page_versions and app_custom_product_page_versions > 50:
            raise ValueError(f'The maximum limit of app_custom_product_page_versions is 50')
        if app_custom_product_page_versions: self._set_limit(app_custom_product_page_versions, 'appCustomProductPageVersions')

        return self

    def get(self) -> AppCustomProductPageResponse:
        '''Get the resource.

        :returns: Single AppCustomProductPage
        :rtype: AppCustomProductPageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageResponse.parse_obj(json)

    def update(self, request: AppCustomProductPageUpdateRequest) -> AppCustomProductPageResponse:
        '''Modify the resource.

        :param request: AppCustomProductPage representation
        :type request: AppCustomProductPageUpdateRequest

        :returns: Single AppCustomProductPage
        :rtype: AppCustomProductPageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppCustomProductPageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppCustomProductPageVersionsLinkagesOfAppCustomProductPageEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPages/{id}/relationships/appCustomProductPageVersions'

    def limit(self, number: int=None) -> AppCustomProductPageVersionsLinkagesOfAppCustomProductPageEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionsLinkagesOfAppCustomProductPageEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppCustomProductPageAppCustomProductPageVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppCustomProductPageAppCustomProductPageVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageAppCustomProductPageVersionsLinkagesResponse.parse_obj(json)

class AppCustomProductPageVersionsOfAppCustomProductPageEndpoint(IDEndpoint):
    path = '/v1/appCustomProductPages/{id}/appCustomProductPageVersions'

    class State(StringEnum):
        PREPARE_FOR_SUBMISSION = 'PREPARE_FOR_SUBMISSION'
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        ACCEPTED = 'ACCEPTED'
        APPROVED = 'APPROVED'
        REPLACED_WITH_NEW_VERSION = 'REPLACED_WITH_NEW_VERSION'
        REJECTED = 'REJECTED'

    def fields(self, *, app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]]=None, app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]]=None, app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]]=None) -> AppCustomProductPageVersionsOfAppCustomProductPageEndpoint:
        '''Fields to return for included related types.

        :param app_custom_product_page_version: the fields to include for returned resources of type appCustomProductPageVersions
        :type app_custom_product_page_version: Union[AppCustomProductPageVersionField, list[AppCustomProductPageVersionField]] = None

        :param app_custom_product_page: the fields to include for returned resources of type appCustomProductPages
        :type app_custom_product_page: Union[AppCustomProductPageField, list[AppCustomProductPageField]] = None

        :param app_custom_product_page_localization: the fields to include for returned resources of type appCustomProductPageLocalizations
        :type app_custom_product_page_localization: Union[AppCustomProductPageLocalizationField, list[AppCustomProductPageLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionsOfAppCustomProductPageEndpoint
        '''
        if app_custom_product_page_version: self._set_fields('appCustomProductPageVersions',app_custom_product_page_version if type(app_custom_product_page_version) is list else [app_custom_product_page_version])
        if app_custom_product_page: self._set_fields('appCustomProductPages',app_custom_product_page if type(app_custom_product_page) is list else [app_custom_product_page])
        if app_custom_product_page_localization: self._set_fields('appCustomProductPageLocalizations',app_custom_product_page_localization if type(app_custom_product_page_localization) is list else [app_custom_product_page_localization])
        return self
        
    class Include(StringEnum):
        APP_CUSTOM_PRODUCT_PAGE = 'appCustomProductPage'
        APP_CUSTOM_PRODUCT_PAGE_LOCALIZATIONS = 'appCustomProductPageLocalizations'

    def filter(self, *, state: Union[State, list[State]]=None) -> AppCustomProductPageVersionsOfAppCustomProductPageEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionsOfAppCustomProductPageEndpoint
        '''
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppCustomProductPageVersionsOfAppCustomProductPageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionsOfAppCustomProductPageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_custom_product_page_localizations: int=None) -> AppCustomProductPageVersionsOfAppCustomProductPageEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_custom_product_page_localizations: maximum number of related appCustomProductPageLocalizations returned (when they are included). The maximum limit is 50
        :type app_custom_product_page_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppCustomProductPageVersionsOfAppCustomProductPageEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_custom_product_page_localizations and app_custom_product_page_localizations > 50:
            raise ValueError(f'The maximum limit of app_custom_product_page_localizations is 50')
        if app_custom_product_page_localizations: self._set_limit(app_custom_product_page_localizations, 'appCustomProductPageLocalizations')

        return self

    def get(self) -> AppCustomProductPageVersionsResponse:
        '''Get one or more resources.

        :returns: List of AppCustomProductPageVersions
        :rtype: AppCustomProductPageVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppCustomProductPageVersionsResponse.parse_obj(json)

