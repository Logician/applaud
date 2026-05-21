from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BackgroundAssetsEndpoint(Endpoint):
    path = '/v1/backgroundAssets'

    def create(self, request: BackgroundAssetCreateRequest) -> BackgroundAssetResponse:
        '''Create the resource.

        :param request: BackgroundAsset representation
        :type request: BackgroundAssetCreateRequest

        :returns: Single BackgroundAsset
        :rtype: BackgroundAssetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BackgroundAssetResponse.parse_obj(json)

class BackgroundAssetEndpoint(IDEndpoint):
    path = '/v1/backgroundAssets/{id}'

    @endpoint('/v1/backgroundAssets/{id}/versions')
    def versions(self) -> VersionsOfBackgroundAssetEndpoint:
        return VersionsOfBackgroundAssetEndpoint(self.id, self.session)
        
    @endpoint('/v1/backgroundAssets/{id}/relationships/versions')
    def versions_linkages(self) -> VersionsLinkagesOfBackgroundAssetEndpoint:
        return VersionsLinkagesOfBackgroundAssetEndpoint(self.id, self.session)
        
    def fields(self, *, background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]]=None) -> BackgroundAssetEndpoint:
        '''Fields to return for included related types.

        :param background_asset: the fields to include for returned resources of type backgroundAssets
        :type background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetEndpoint
        '''
        if background_asset: self._set_fields('backgroundAssets',background_asset if type(background_asset) is list else [background_asset])
        return self
        
    class Include(StringEnum):
        APP = 'app'
        APP_STORE_VERSION = 'appStoreVersion'
        INTERNAL_BETA_VERSION = 'internalBetaVersion'
        EXTERNAL_BETA_VERSION = 'externalBetaVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> BackgroundAssetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BackgroundAssetResponse:
        '''Get the resource.

        :returns: Single BackgroundAsset
        :rtype: BackgroundAssetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetResponse.parse_obj(json)
    def update(self, request: BackgroundAssetUpdateRequest) -> BackgroundAssetResponse:
        '''Modify the resource.

        :param request: BackgroundAsset representation
        :type request: BackgroundAssetUpdateRequest

        :returns: Single BackgroundAsset
        :rtype: BackgroundAssetResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BackgroundAssetResponse.parse_obj(json)

class VersionsLinkagesOfBackgroundAssetEndpoint(IDEndpoint):
    path = '/v1/backgroundAssets/{id}/relationships/versions'

    def limit(self, number: int=None) -> VersionsLinkagesOfBackgroundAssetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsLinkagesOfBackgroundAssetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetVersionsLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BackgroundAssetVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionsLinkagesResponse.parse_obj(json)

    def get_all(self) -> BackgroundAssetVersionsLinkagesResponse:
        '''
        Get all resources.

        :returns: List of related linkages
        :rtype: BackgroundAssetVersionsLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BackgroundAssetVersionsLinkagesResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BackgroundAssetVersionsLinkagesResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

class VersionsOfBackgroundAssetEndpoint(IDEndpoint):
    path = '/v1/backgroundAssets/{id}/versions'

    class Platforms(StringEnum):
        IOS = 'IOS'
        MAC_OS = 'MAC_OS'
        TV_OS = 'TV_OS'
        VISION_OS = 'VISION_OS'

    class State(StringEnum):
        AWAITING_UPLOAD = 'AWAITING_UPLOAD'
        PROCESSING = 'PROCESSING'
        FAILED = 'FAILED'
        COMPLETE = 'COMPLETE'

    class InternalBetaRelease_state(StringEnum):
        READY_FOR_TESTING = 'READY_FOR_TESTING'
        SUPERSEDED = 'SUPERSEDED'

    class ExternalBetaRelease_state(StringEnum):
        READY_FOR_BETA_SUBMISSION = 'READY_FOR_BETA_SUBMISSION'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        REJECTED = 'REJECTED'
        PROCESSING_FOR_TESTING = 'PROCESSING_FOR_TESTING'
        READY_FOR_TESTING = 'READY_FOR_TESTING'
        SUPERSEDED = 'SUPERSEDED'

    class AppStoreRelease_state(StringEnum):
        PREPARE_FOR_SUBMISSION = 'PREPARE_FOR_SUBMISSION'
        READY_FOR_REVIEW = 'READY_FOR_REVIEW'
        WAITING_FOR_REVIEW = 'WAITING_FOR_REVIEW'
        IN_REVIEW = 'IN_REVIEW'
        ACCEPTED = 'ACCEPTED'
        REJECTED = 'REJECTED'
        PROCESSING_FOR_DISTRIBUTION = 'PROCESSING_FOR_DISTRIBUTION'
        READY_FOR_DISTRIBUTION = 'READY_FOR_DISTRIBUTION'
        SUPERSEDED = 'SUPERSEDED'

    def fields(self, *, background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]]=None, background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]]=None, background_asset_version_internal_beta_release: Union[BackgroundAssetVersionInternalBetaReleaseField, list[BackgroundAssetVersionInternalBetaReleaseField]]=None, background_asset_version_external_beta_release: Union[BackgroundAssetVersionExternalBetaReleaseField, list[BackgroundAssetVersionExternalBetaReleaseField]]=None, background_asset_version_app_store_release: Union[BackgroundAssetVersionAppStoreReleaseField, list[BackgroundAssetVersionAppStoreReleaseField]]=None, background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]]=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Fields to return for included related types.

        :param background_asset_version: the fields to include for returned resources of type backgroundAssetVersions
        :type background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]] = None

        :param background_asset: the fields to include for returned resources of type backgroundAssets
        :type background_asset: Union[BackgroundAssetField, list[BackgroundAssetField]] = None

        :param background_asset_version_internal_beta_release: the fields to include for returned resources of type backgroundAssetVersionInternalBetaReleases
        :type background_asset_version_internal_beta_release: Union[BackgroundAssetVersionInternalBetaReleaseField, list[BackgroundAssetVersionInternalBetaReleaseField]] = None

        :param background_asset_version_external_beta_release: the fields to include for returned resources of type backgroundAssetVersionExternalBetaReleases
        :type background_asset_version_external_beta_release: Union[BackgroundAssetVersionExternalBetaReleaseField, list[BackgroundAssetVersionExternalBetaReleaseField]] = None

        :param background_asset_version_app_store_release: the fields to include for returned resources of type backgroundAssetVersionAppStoreReleases
        :type background_asset_version_app_store_release: Union[BackgroundAssetVersionAppStoreReleaseField, list[BackgroundAssetVersionAppStoreReleaseField]] = None

        :param background_asset_upload_file: the fields to include for returned resources of type backgroundAssetUploadFiles
        :type background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if background_asset_version: self._set_fields('backgroundAssetVersions',background_asset_version if type(background_asset_version) is list else [background_asset_version])
        if background_asset: self._set_fields('backgroundAssets',background_asset if type(background_asset) is list else [background_asset])
        if background_asset_version_internal_beta_release: self._set_fields('backgroundAssetVersionInternalBetaReleases',background_asset_version_internal_beta_release if type(background_asset_version_internal_beta_release) is list else [background_asset_version_internal_beta_release])
        if background_asset_version_external_beta_release: self._set_fields('backgroundAssetVersionExternalBetaReleases',background_asset_version_external_beta_release if type(background_asset_version_external_beta_release) is list else [background_asset_version_external_beta_release])
        if background_asset_version_app_store_release: self._set_fields('backgroundAssetVersionAppStoreReleases',background_asset_version_app_store_release if type(background_asset_version_app_store_release) is list else [background_asset_version_app_store_release])
        if background_asset_upload_file: self._set_fields('backgroundAssetUploadFiles',background_asset_upload_file if type(background_asset_upload_file) is list else [background_asset_upload_file])
        return self
        
    class Include(StringEnum):
        BACKGROUND_ASSET = 'backgroundAsset'
        INTERNAL_BETA_RELEASE = 'internalBetaRelease'
        EXTERNAL_BETA_RELEASE = 'externalBetaRelease'
        APP_STORE_RELEASE = 'appStoreRelease'
        ASSET_FILE = 'assetFile'
        MANIFEST_FILE = 'manifestFile'

    def filter(self, *, platforms: Union[Platforms, list[Platforms]]=None, state: Union[State, list[State]]=None, version: Union[str, list[str]]=None, internal_beta_release_state: Union[InternalBetaRelease_state, list[InternalBetaRelease_state]]=None, external_beta_release_state: Union[ExternalBetaRelease_state, list[ExternalBetaRelease_state]]=None, app_store_release_state: Union[AppStoreRelease_state, list[AppStoreRelease_state]]=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Attributes, relationships, and IDs by which to filter.

        :param platforms: filter by attribute 'platforms'
        :type platforms: Union[Platforms, list[Platforms]] = None

        :param state: filter by attribute 'state'
        :type state: Union[State, list[State]] = None

        :param version: filter by attribute 'version'
        :type version: Union[str, list[str]] = None

        :param internal_beta_release_state: filter by attribute 'internalBetaRelease.state'
        :type internal_beta_release_state: Union[InternalBetaRelease_state, list[InternalBetaRelease_state]] = None

        :param external_beta_release_state: filter by attribute 'externalBetaRelease.state'
        :type external_beta_release_state: Union[ExternalBetaRelease_state, list[ExternalBetaRelease_state]] = None

        :param app_store_release_state: filter by attribute 'appStoreRelease.state'
        :type app_store_release_state: Union[AppStoreRelease_state, list[AppStoreRelease_state]] = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if platforms: self._set_filter('platforms', platforms if type(platforms) is list else [platforms])
        
        if state: self._set_filter('state', state if type(state) is list else [state])
        
        if version: self._set_filter('version', version if type(version) is list else [version])
        
        if internal_beta_release_state: self._set_filter('internalBetaRelease.state', internal_beta_release_state if type(internal_beta_release_state) is list else [internal_beta_release_state])
        
        if external_beta_release_state: self._set_filter('externalBetaRelease.state', external_beta_release_state if type(external_beta_release_state) is list else [external_beta_release_state])
        
        if app_store_release_state: self._set_filter('appStoreRelease.state', app_store_release_state if type(app_store_release_state) is list else [app_store_release_state])
        
        return self
        
    def include(self, relationship: Union[Include, list[Include]]) -> VersionsOfBackgroundAssetEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def sort(self, *, version: SortOrder=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Attributes by which to sort.

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        sort_expressions = []
        if version: sort_expressions.append('version' if version == SortOrder.ASC else '-version')
        if len(sort_expressions) > 0:
            self._set_sort(sort_expressions)
        return self
        
    def limit(self, number: int=None) -> VersionsOfBackgroundAssetEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.VersionsOfBackgroundAssetEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetVersionsResponse:
        '''Get one or more resources.

        :returns: List of BackgroundAssetVersions
        :rtype: BackgroundAssetVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionsResponse.parse_obj(json)

    def get_all(self) -> BackgroundAssetVersionsResponse:
        '''
        Get all resources.

        :returns: List of BackgroundAssetVersions
        :rtype: BackgroundAssetVersionsResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        response = BackgroundAssetVersionsResponse.parse_obj(json)
        while response.links.next != None:
            json = super()._perform_get_next(next = response.links.next)
            response2 = BackgroundAssetVersionsResponse.parse_obj(json)
            response.data.extend(response2.data)
            response.links = response2.links
        return response

