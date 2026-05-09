from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BuildUploadsEndpoint(Endpoint):
    path = '/v1/buildUploads'

    def create(self, request: BuildUploadCreateRequest) -> BuildUploadResponse:
        '''Create the resource.

        :param request: BuildUpload representation
        :type request: BuildUploadCreateRequest

        :returns: Single BuildUpload
        :rtype: BuildUploadResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return BuildUploadResponse.parse_obj(json)

class BuildUploadEndpoint(IDEndpoint):
    path = '/v1/buildUploads/{id}'

    @endpoint('/v1/buildUploads/{id}/buildUploadFiles')
    def build_upload_files(self) -> BuildUploadFilesOfBuildUploadEndpoint:
        return BuildUploadFilesOfBuildUploadEndpoint(self.id, self.session)
        
    @endpoint('/v1/buildUploads/{id}/relationships/buildUploadFiles')
    def build_upload_files_linkages(self) -> BuildUploadFilesLinkagesOfBuildUploadEndpoint:
        return BuildUploadFilesLinkagesOfBuildUploadEndpoint(self.id, self.session)
        
    def fields(self, *, build_upload: Union[BuildUploadField, list[BuildUploadField]]=None) -> BuildUploadEndpoint:
        '''Fields to return for included related types.

        :param build_upload: the fields to include for returned resources of type buildUploads
        :type build_upload: Union[BuildUploadField, list[BuildUploadField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadEndpoint
        '''
        if build_upload: self._set_fields('buildUploads',build_upload if type(build_upload) is list else [build_upload])
        return self
        
    class Include(StringEnum):
        BUILD = 'build'
        ASSET_FILE = 'assetFile'
        ASSET_DESCRIPTION_FILE = 'assetDescriptionFile'
        ASSET_SPI_FILE = 'assetSpiFile'

    def include(self, relationship: Union[Include, list[Include]]) -> BuildUploadEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BuildUploadEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BuildUploadResponse:
        '''Get the resource.

        :returns: Single BuildUpload
        :rtype: BuildUploadResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildUploadResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class BuildUploadFilesLinkagesOfBuildUploadEndpoint(IDEndpoint):
    path = '/v1/buildUploads/{id}/relationships/buildUploadFiles'

    def limit(self, number: int=None) -> BuildUploadFilesLinkagesOfBuildUploadEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadFilesLinkagesOfBuildUploadEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildUploadBuildUploadFilesLinkagesResponse:
        '''Get one or more resources.

        :returns: List of related linkages
        :rtype: BuildUploadBuildUploadFilesLinkagesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildUploadBuildUploadFilesLinkagesResponse.parse_obj(json)

class BuildUploadFilesOfBuildUploadEndpoint(IDEndpoint):
    path = '/v1/buildUploads/{id}/buildUploadFiles'

    def fields(self, *, build_upload_file: Union[BuildUploadFileField, list[BuildUploadFileField]]=None) -> BuildUploadFilesOfBuildUploadEndpoint:
        '''Fields to return for included related types.

        :param build_upload_file: the fields to include for returned resources of type buildUploadFiles
        :type build_upload_file: Union[BuildUploadFileField, list[BuildUploadFileField]] = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadFilesOfBuildUploadEndpoint
        '''
        if build_upload_file: self._set_fields('buildUploadFiles',build_upload_file if type(build_upload_file) is list else [build_upload_file])
        return self
        
    def limit(self, number: int=None) -> BuildUploadFilesOfBuildUploadEndpoint:
        '''Number of resources to return.

        :param number: maximum resources per page. The maximum limit is 200
        :type number: int = None

        :returns: self
        :rtype: applaud.endpoints.BuildUploadFilesOfBuildUploadEndpoint
        '''
        if number and number > 200:
            raise ValueError(f'The maximum limit of number is 200')
        if number: self._set_limit(number)
        
        return self

    def get(self) -> BuildUploadFilesResponse:
        '''Get one or more resources.

        :returns: List of BuildUploadFiles
        :rtype: BuildUploadFilesResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BuildUploadFilesResponse.parse_obj(json)

