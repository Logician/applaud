from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AppStoreVersionExperimentsEndpoint(Endpoint):
    path = '/v2/appStoreVersionExperiments'

    def create(self, request: AppStoreVersionExperimentV2CreateRequest) -> AppStoreVersionExperimentV2Response:
        '''Create the resource.

        :param request: AppStoreVersionExperiment representation
        :type request: AppStoreVersionExperimentV2CreateRequest

        :returns: Single AppStoreVersionExperiment
        :rtype: AppStoreVersionExperimentV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionExperimentV2Response.parse_obj(json)

class AppStoreVersionExperimentEndpoint(IDEndpoint):
    path = '/v2/appStoreVersionExperiments/{id}'

    @endpoint('/v2/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments')
    def app_store_version_experiment_treatments(self) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        return AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint(self.id, self.session)
        
    @endpoint('/v2/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments')
    def app_store_version_experiment_treatments_linkages(self) -> AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint:
        return AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None) -> AppStoreVersionExperimentEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentEndpoint
        '''
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        LATEST_CONTROL_VERSION = 'latestControlVersion'
        CONTROL_VERSIONS = 'controlVersions'
        APP_STORE_VERSION_EXPERIMENT_TREATMENTS = 'appStoreVersionExperimentTreatments'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_experiment_treatments: int=None, control_versions: int=None) -> AppStoreVersionExperimentEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_experiment_treatments: maximum number of related appStoreVersionExperimentTreatments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatments: int = None

        :param control_versions: maximum number of related controlVersions returned (when they are included). The maximum limit is 50
        :type control_versions: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentEndpoint
        '''
        if app_store_version_experiment_treatments and app_store_version_experiment_treatments > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatments is 50')
        if app_store_version_experiment_treatments: self._set_limit(app_store_version_experiment_treatments, 'appStoreVersionExperimentTreatments')

        if control_versions and control_versions > 50:
            raise ValueError(f'The maximum limit of control_versions is 50')
        if control_versions: self._set_limit(control_versions, 'controlVersions')

        return self

    def get(self) -> AppStoreVersionExperimentV2Response:
        '''Get the resource.

        :returns: Single AppStoreVersionExperiment
        :rtype: AppStoreVersionExperimentV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentV2Response.parse_obj(json)

    def update(self, request: AppStoreVersionExperimentV2UpdateRequest) -> AppStoreVersionExperimentV2Response:
        '''Modify the resource.

        :param request: AppStoreVersionExperiment representation
        :type request: AppStoreVersionExperimentV2UpdateRequest

        :returns: Single AppStoreVersionExperiment
        :rtype: AppStoreVersionExperimentV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreVersionExperimentV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppStoreVersionExperimentsEndpoint(Endpoint):
    path = '/v1/appStoreVersionExperiments'

    @deprecated
    def create(self, request: AppStoreVersionExperimentCreateRequest) -> AppStoreVersionExperimentResponse:
        '''Create the resource.

        :param request: AppStoreVersionExperiment representation
        :type request: AppStoreVersionExperimentCreateRequest

        :returns: Single AppStoreVersionExperiment
        :rtype: AppStoreVersionExperimentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AppStoreVersionExperimentResponse.parse_obj(json)

class AppStoreVersionExperimentEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionExperiments/{id}'

    @endpoint('/v1/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments')
    def app_store_version_experiment_treatments(self) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        return AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint(self.id, self.session)
        
    @endpoint('/v1/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments')
    def app_store_version_experiment_treatments_linkages(self) -> AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint:
        return AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint(self.id, self.session)
        
    def fields(self, *, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None) -> AppStoreVersionExperimentEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentEndpoint
        '''
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION = 'appStoreVersion'
        APP_STORE_VERSION_EXPERIMENT_TREATMENTS = 'appStoreVersionExperimentTreatments'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, *, app_store_version_experiment_treatments: int=None) -> AppStoreVersionExperimentEndpoint:
        '''Number of included related resources to return.

        :param app_store_version_experiment_treatments: maximum number of related appStoreVersionExperimentTreatments returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatments: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentEndpoint
        '''
        if app_store_version_experiment_treatments and app_store_version_experiment_treatments > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatments is 50')
        if app_store_version_experiment_treatments: self._set_limit(app_store_version_experiment_treatments, 'appStoreVersionExperimentTreatments')

        return self

    @deprecated
    def get(self) -> AppStoreVersionExperimentResponse:
        '''Get the resource.

        :returns: Single AppStoreVersionExperiment
        :rtype: AppStoreVersionExperimentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentResponse.parse_obj(json)

    @deprecated
    def update(self, request: AppStoreVersionExperimentUpdateRequest) -> AppStoreVersionExperimentResponse:
        '''Modify the resource.

        :param request: AppStoreVersionExperiment representation
        :type request: AppStoreVersionExperimentUpdateRequest

        :returns: Single AppStoreVersionExperiment
        :rtype: AppStoreVersionExperimentResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AppStoreVersionExperimentResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint(IDEndpoint):
    path = '/v2/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments'

    def limit(self, number: int=None) -> AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> AppStoreVersionExperimentV2AppStoreVersionExperimentTreatmentsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionExperimentV2AppStoreVersionExperimentTreatmentsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentV2AppStoreVersionExperimentTreatmentsLinkagesResponse.parse_obj(json)

class AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint(IDEndpoint):
    path = '/v2/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments'

    def fields(self, *, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]]=None) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app_store_version_experiment_treatment_localization: the fields to include for returned resources of type appStoreVersionExperimentTreatmentLocalizations
        :type app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint
        '''
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app_store_version_experiment_treatment_localization: self._set_fields('appStoreVersionExperimentTreatmentLocalizations',app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_EXPERIMENT = 'appStoreVersionExperiment'
        APP_STORE_VERSION_EXPERIMENT_V2 = 'appStoreVersionExperimentV2'
        APP_STORE_VERSION_EXPERIMENT_TREATMENT_LOCALIZATIONS = 'appStoreVersionExperimentTreatmentLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_store_version_experiment_treatment_localizations: int=None) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_store_version_experiment_treatment_localizations: maximum number of related appStoreVersionExperimentTreatmentLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatment_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_store_version_experiment_treatment_localizations and app_store_version_experiment_treatment_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatment_localizations is 50')
        if app_store_version_experiment_treatment_localizations: self._set_limit(app_store_version_experiment_treatment_localizations, 'appStoreVersionExperimentTreatmentLocalizations')

        return self

    def get(self) -> AppStoreVersionExperimentTreatmentsResponse:
        '''Get one or more resources.

        :returns: List of AppStoreVersionExperimentTreatments
        :rtype: AppStoreVersionExperimentTreatmentsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentTreatmentsResponse.parse_obj(json)

class AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionExperiments/{id}/relationships/appStoreVersionExperimentTreatments'

    def limit(self, number: int=None) -> AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsLinkagesOfAppStoreVersionExperimentEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    @deprecated
    def get(self) -> AppStoreVersionExperimentAppStoreVersionExperimentTreatmentsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: AppStoreVersionExperimentAppStoreVersionExperimentTreatmentsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentAppStoreVersionExperimentTreatmentsLinkagesResponse.parse_obj(json)

class AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint(IDEndpoint):
    path = '/v1/appStoreVersionExperiments/{id}/appStoreVersionExperimentTreatments'

    def fields(self, *, app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]]=None, app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]]=None, app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]]=None) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        '''Fields to return for included related types.

        :param app_store_version_experiment_treatment: the fields to include for returned resources of type appStoreVersionExperimentTreatments
        :type app_store_version_experiment_treatment: Union[AppStoreVersionExperimentTreatmentField, list[AppStoreVersionExperimentTreatmentField]] = None

        :param app_store_version_experiment: the fields to include for returned resources of type appStoreVersionExperiments
        :type app_store_version_experiment: Union[AppStoreVersionExperimentField, list[AppStoreVersionExperimentField]] = None

        :param app_store_version_experiment_treatment_localization: the fields to include for returned resources of type appStoreVersionExperimentTreatmentLocalizations
        :type app_store_version_experiment_treatment_localization: Union[AppStoreVersionExperimentTreatmentLocalizationField, list[AppStoreVersionExperimentTreatmentLocalizationField]] = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint
        '''
        if app_store_version_experiment_treatment: self._set_fields('appStoreVersionExperimentTreatments',app_store_version_experiment_treatment if type(app_store_version_experiment_treatment) is list else [app_store_version_experiment_treatment])
        if app_store_version_experiment: self._set_fields('appStoreVersionExperiments',app_store_version_experiment if type(app_store_version_experiment) is list else [app_store_version_experiment])
        if app_store_version_experiment_treatment_localization: self._set_fields('appStoreVersionExperimentTreatmentLocalizations',app_store_version_experiment_treatment_localization if type(app_store_version_experiment_treatment_localization) is list else [app_store_version_experiment_treatment_localization])
        return self
        
    class Include(StringEnum):
        APP_STORE_VERSION_EXPERIMENT = 'appStoreVersionExperiment'
        APP_STORE_VERSION_EXPERIMENT_V2 = 'appStoreVersionExperimentV2'
        APP_STORE_VERSION_EXPERIMENT_TREATMENT_LOCALIZATIONS = 'appStoreVersionExperimentTreatmentLocalizations'

    def include(self, relationship: Union[Include, list[Include]]) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def limit(self, number: int=None, *, app_store_version_experiment_treatment_localizations: int=None) -> AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint:
        '''Number of resources or included related resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :param app_store_version_experiment_treatment_localizations: maximum number of related appStoreVersionExperimentTreatmentLocalizations returned (when they are included). The maximum limit is 50
        :type app_store_version_experiment_treatment_localizations: int = None

        :returns: self
        :rtype: applaud.endpoints.AppStoreVersionExperimentTreatmentsOfAppStoreVersionExperimentEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        if app_store_version_experiment_treatment_localizations and app_store_version_experiment_treatment_localizations > 50:
            raise ValueError(f'The maximum limit of app_store_version_experiment_treatment_localizations is 50')
        if app_store_version_experiment_treatment_localizations: self._set_limit(app_store_version_experiment_treatment_localizations, 'appStoreVersionExperimentTreatmentLocalizations')

        return self

    @deprecated
    def get(self) -> AppStoreVersionExperimentTreatmentsResponse:
        '''Get one or more resources.

        :returns: List of AppStoreVersionExperimentTreatments
        :rtype: AppStoreVersionExperimentTreatmentsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AppStoreVersionExperimentTreatmentsResponse.parse_obj(json)

