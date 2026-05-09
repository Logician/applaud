from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildUploadFilesEndpoint(Endpoint):
    path = '/v1/buildUploadFiles'

    def create(self, request: BuildUploadFileCreateRequest) -> BuildUploadFileResponse:
        '''Create the resource.

        :param request: BuildUploadFile representation
        :type request: BuildUploadFileCreateRequest

        :returns: Single BuildUploadFile
        :rtype: BuildUploadFileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BuildUploadFileResponse.parse_obj(json)

class BuildUploadFileEndpoint(IDEndpoint):
    path = '/v1/buildUploadFiles/{id}'

    def fields(self, *, build_upload_file: Union[BuildUploadFileField, list[BuildUploadFileField]]=None) -> BuildUploadFileEndpoint:
        '''Fields to return for included related types.

        :param build_upload_file: the fields to include for returned resources of type buildUploadFiles
        :type build_upload_file: Union[BuildUploadFileField, list[BuildUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadFileEndpoint
        '''
        if build_upload_file: self._set_fields('buildUploadFiles',build_upload_file if type(build_upload_file) is list else [build_upload_file])
        return self
        
    def get(self) -> BuildUploadFileResponse:
        '''Get the resource.

        :returns: Single BuildUploadFile
        :rtype: BuildUploadFileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildUploadFileResponse.parse_obj(json)

    def update(self, request: BuildUploadFileUpdateRequest) -> BuildUploadFileResponse:
        '''Modify the resource.

        :param request: BuildUploadFile representation
        :type request: BuildUploadFileUpdateRequest

        :returns: Single BuildUploadFile
        :rtype: BuildUploadFileResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return BuildUploadFileResponse.parse_obj(json)

