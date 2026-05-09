from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BackgroundAssetVersionsEndpoint(Endpoint):
    path = '/v1/backgroundAssetVersions'

    def create(self, request: BackgroundAssetVersionCreateRequest) -> BackgroundAssetVersionResponse:
        '''Create the resource.

        :param request: BackgroundAssetVersion representation
        :type request: BackgroundAssetVersionCreateRequest

        :returns: Single BackgroundAssetVersion
        :rtype: BackgroundAssetVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BackgroundAssetVersionResponse.parse_obj(json)

class BackgroundAssetVersionEndpoint(IDEndpoint):
    path = '/v1/backgroundAssetVersions/{id}'

    @endpoint('/v1/backgroundAssetVersions/{id}/backgroundAssetUploadFiles')
    def background_asset_upload_files(self) -> BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint:
        return BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint(self.id, self.session)
        
    @endpoint('/v1/backgroundAssetVersions/{id}/relationships/backgroundAssetUploadFiles')
    def background_asset_upload_files_linkages(self) -> BackgroundAssetUploadFilesLinkagesOfBackgroundAssetVersionEndpoint:
        return BackgroundAssetUploadFilesLinkagesOfBackgroundAssetVersionEndpoint(self.id, self.session)
        
    def fields(self, *, background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]]=None) -> BackgroundAssetVersionEndpoint:
        '''Fields to return for included related types.

        :param background_asset_version: the fields to include for returned resources of type backgroundAssetVersions
        :type background_asset_version: Union[BackgroundAssetVersionField, list[BackgroundAssetVersionField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetVersionEndpoint
        '''
        if background_asset_version: self._set_fields('backgroundAssetVersions',background_asset_version if type(background_asset_version) is list else [background_asset_version])
        return self
        
    class Include(StringEnum):
        BACKGROUND_ASSET = 'backgroundAsset'
        INTERNAL_BETA_RELEASE = 'internalBetaRelease'
        EXTERNAL_BETA_RELEASE = 'externalBetaRelease'
        APP_STORE_RELEASE = 'appStoreRelease'
        ASSET_FILE = 'assetFile'
        MANIFEST_FILE = 'manifestFile'

    def include(self, relationship: Union[Include, list[Include]]) -> BackgroundAssetVersionEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetVersionEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BackgroundAssetVersionResponse:
        '''Get the resource.

        :returns: Single BackgroundAssetVersion
        :rtype: BackgroundAssetVersionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionResponse.parse_obj(json)

class BackgroundAssetUploadFilesLinkagesOfBackgroundAssetVersionEndpoint(IDEndpoint):
    path = '/v1/backgroundAssetVersions/{id}/relationships/backgroundAssetUploadFiles'

    def limit(self, number: int=None) -> BackgroundAssetUploadFilesLinkagesOfBackgroundAssetVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetUploadFilesLinkagesOfBackgroundAssetVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionBackgroundAssetUploadFilesLinkagesResponse.parse_obj(json)

class BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint(IDEndpoint):
    path = '/v1/backgroundAssetVersions/{id}/backgroundAssetUploadFiles'

    def fields(self, *, background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]]=None) -> BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint:
        '''Fields to return for included related types.

        :param background_asset_upload_file: the fields to include for returned resources of type backgroundAssetUploadFiles
        :type background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint
        '''
        if background_asset_upload_file: self._set_fields('backgroundAssetUploadFiles',background_asset_upload_file if type(background_asset_upload_file) is list else [background_asset_upload_file])
        return self
        
    def limit(self, number: int=None) -> BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetUploadFilesOfBackgroundAssetVersionEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BackgroundAssetUploadFilesResponse:
        '''Get one or more resources.

        :returns: List of BackgroundAssetUploadFiles
        :rtype: BackgroundAssetUploadFilesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetUploadFilesResponse.parse_obj(json)

