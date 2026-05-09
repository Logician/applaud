from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BackgroundAssetUploadFilesEndpoint(Endpoint):
    path = '/v1/backgroundAssetUploadFiles'

    def create(self, request: BackgroundAssetUploadFileCreateRequest) -> BackgroundAssetUploadFileResponse:
        '''Create the resource.

        :param request: BackgroundAssetUploadFile representation
        :type request: BackgroundAssetUploadFileCreateRequest

        :returns: Single BackgroundAssetUploadFile
        :rtype: BackgroundAssetUploadFileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BackgroundAssetUploadFileResponse.parse_obj(json)

class BackgroundAssetUploadFileEndpoint(IDEndpoint):
    path = '/v1/backgroundAssetUploadFiles/{id}'

    def fields(self, *, background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]]=None) -> BackgroundAssetUploadFileEndpoint:
        '''Fields to return for included related types.

        :param background_asset_upload_file: the fields to include for returned resources of type backgroundAssetUploadFiles
        :type background_asset_upload_file: Union[BackgroundAssetUploadFileField, list[BackgroundAssetUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetUploadFileEndpoint
        '''
        if background_asset_upload_file: self._set_fields('backgroundAssetUploadFiles',background_asset_upload_file if type(background_asset_upload_file) is list else [background_asset_upload_file])
        return self
        
    def get(self) -> BackgroundAssetUploadFileResponse:
        '''Get the resource.

        :returns: Single BackgroundAssetUploadFile
        :rtype: BackgroundAssetUploadFileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetUploadFileResponse.parse_obj(json)

    def update(self, request: BackgroundAssetUploadFileUpdateRequest) -> BackgroundAssetUploadFileResponse:
        '''Modify the resource.

        :param request: BackgroundAssetUploadFile representation
        :type request: BackgroundAssetUploadFileUpdateRequest

        :returns: Single BackgroundAssetUploadFile
        :rtype: BackgroundAssetUploadFileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BackgroundAssetUploadFileResponse.parse_obj(json)

