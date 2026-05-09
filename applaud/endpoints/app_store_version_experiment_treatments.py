from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionExperimentTreatmentsEndpoint(Endpoint):
    path = '/v1/appStoreVersionExperimentTreatments'

    def create(self, request: AppStoreVersionExperimentTreatmentCreateRequest) -> AppStoreVersionExperimentTreatmentResponse:
        '''Create the resource.

        :param request: AppStoreVersionExperimentTreatment representation
        :type request: AppStoreVersionExperimentTreatmentCreateRequest

        :returns: Single AppStoreVersionExperimentTreatment
        :rtype: AppStoreVersionExperimentTreatmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionExperimentTreatmentResponse.parse_obj(json)

class AppStoreVersionExperimentTreatmentEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionExperimentTreatments/{id}'

    @endpoint('/v1/appStoreVersionExperimentTreatments/{id}/appStoreVersionExperimentTreatmentLocalizations')
    def app_store_version_experiment_treatment_localizations(self) -> AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint:
        return AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersionExperimentTreatments/{id}/relationships/appStoreVersionExperimentTreatmentLocalizations')
    def app_store_version_experiment_treatment_localizations_linkages(self) -> AppStoreVersionExperimentTreatmentLocalizationsLinkagesOfAppStoreVersionExperimentTreatmentEndpoint:
        return AppStoreVersionExperimentTreatmentLocalizationsLinkagesOfAppStoreVersionExperimentTreatmentEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None, app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]]=None) -> AppStoreVersionExperimentTreatmentEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :param app_store_version_experiment_treatment_localization: the fields to include for returned resources of type appStoreVersionExperimentTreatmentLocalizations
        :type app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentEndpoint
        '''
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        if app_store_version_experiment_treatment_localization: self._set_fields('appStoreVersionExperimentTreatmentLocalizations',app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_EXPERIMENT = 'appStoreVersionExperiment'
        APP_STORE_VERSION_EXPERIMENT_V2 = 'appStoreVersionExperimentV2'
        APP_STORE_VERSION_EXPERIMENT_TREATMENT_LOCALIZATIONS = 'appStoreVersionExperimentTreatmentLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentTreatmentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_experiment_treatment_localizations: int=None) -> AppStoreVersionExperimentTreatmentEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_experiment_treatment_localizations: maximum number of related appStoreVersionExperimentTreatmentLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatment_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentEndpoint
        '''
        if app_store_version_experiment_treatment_localizations and app_store_version_experiment_treatment_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatment_localizations is 50')
        if app_store_version_experiment_treatment_localizations: self._set_limit(app_store_version_experiment_treatment_localizations, 'appStoreVersionExperimentTreatmentLocalizations')

        return self

    def get(self) -> AppStoreVersionExperimentTreatmentResponse:
        '''Get the resource.

        :returns: Single AppStoreVersionExperimentTreatment
        :rtype: AppStoreVersionExperimentTreatmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentTreatmentResponse.parse_obj(json)

    def update(self, request: AppStoreVersionExperimentTreatmentUpdateRequest) -> AppStoreVersionExperimentTreatmentResponse:
        '''Modify the resource.

        :param request: AppStoreVersionExperimentTreatment representation
        :type request: AppStoreVersionExperimentTreatmentUpdateRequest

        :returns: Single AppStoreVersionExperimentTreatment
        :rtype: AppStoreVersionExperimentTreatmentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreVersionExperimentTreatmentResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppStoreVersionExperimentTreatmentLocalizationsLinkagesOfAppStoreVersionExperimentTreatmentEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionExperimentTreatments/{id}/relationships/appStoreVersionExperimentTreatmentLocalizations'

    def limit(self, number: int=None) -> AppStoreVersionExperimentTreatmentLocalizationsLinkagesOfAppStoreVersionExperimentTreatmentEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentLocalizationsLinkagesOfAppStoreVersionExperimentTreatmentEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppStoreVersionExperimentTreatmentAppStoreVersionExperimentTreatmentLocalizationsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionExperimentTreatmentAppStoreVersionExperimentTreatmentLocalizationsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentTreatmentAppStoreVersionExperimentTreatmentLocalizationsLinkagesResponse.parse_obj(json)

class AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionExperimentTreatments/{id}/appStoreVersionExperimentTreatmentLocalizations'

    def fields(self, *, app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]]=None, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None, app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]]=None, app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]]=None) -> AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment_treatment_localization: the fields to include for returned resources of type appStoreVersionExperimentTreatmentLocalizations
        :type app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]] = None

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :param app_screenshot_set: the fields to include for returned resources of type appScreenshotSets
        :type app_screenshot_set: Union[AppScreenshotSetField, list[AppScreenshotSetField]] = None

        :param app_preview_set: the fields to include for returned resources of type appPreviewSets
        :type app_preview_set: Union[AppPreviewSetField, list[AppPreviewSetField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint
        '''
        if app_store_version_experiment_treatment_localization: self._set_fields('appStoreVersionExperimentTreatmentLocalizations',app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        if app_screenshot_set: self._set_fields('appScreenshotSets',app_screenshot_set if type(app_screenshot_set) is list else [app_screenshot_set])
        if app_preview_set: self._set_fields('appPreviewSets',app_preview_set if type(app_preview_set) is list else [app_preview_set])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_EXPERIMENT_TREATMENT = 'appStoreVersionExperimentTreatment'
        APP_SCREENSHOT_SETS = 'appScreenshotSets'
        APP_PREVIEW_SETS = 'appPreviewSets'

    def filter(self, *, locale: Union[str, list[str]]=None) -> AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param locale: filter by attribute 'locale'
        :type locale: Union[str, list[str]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint
        '''
        if locale: self._set_filter('locale', locale if type(locale) is list else [locale])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_screenshot_sets: int=None, app_preview_sets: int=None) -> AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_screenshot_sets: maximum number of related appScreenshotSets returned (when they are included). The maximum limit is 50
        :type app_screenshot_sets: int = None

        :param app_preview_sets: maximum number of related appPreviewSets returned (when they are included). The maximum limit is 50
        :type app_preview_sets: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentLocalizationsOfAppStoreVersionExperimentTreatmentEndpoint
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

        return self

    def get(self) -> AppStoreVersionExperimentTreatmentLocalizationsResponse:
        '''Get one or more resources.

        :returns: List of AppStoreVersionExperimentTreatmentLocalizations
        :rtype: AppStoreVersionExperimentTreatmentLocalizationsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentTreatmentLocalizationsResponse.parse_obj(json)

