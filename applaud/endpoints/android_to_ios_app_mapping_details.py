from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class AndroidToIosAppMappingDetailsEndpoint(Endpoint):
    path = '/v1/androidToIosAppMappingDetails'

    def create(self, request: AndroidToIosAppMappingDetailCreateRequest) -> AndroidToIosAppMappingDetailResponse:
        '''Create the resource.

        :param request: AndroidToIosAppMappingDetail representation
        :type request: AndroidToIosAppMappingDetailCreateRequest

        :returns: Single AndroidToIosAppMappingDetail
        :rtype: AndroidToIosAppMappingDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return AndroidToIosAppMappingDetailResponse.parse_obj(json)

class AndroidToIosAppMappingDetailEndpoint(IDEndpoint):
    path = '/v1/androidToIosAppMappingDetails/{id}'

    def fields(self, *, android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]]=None) -> AndroidToIosAppMappingDetailEndpoint:
        '''Fields to return for included related types.

        :param android_to_ios_app_mapping_detail: the fields to include for returned resources of type androidToIosAppMappingDetails
        :type android_to_ios_app_mapping_detail: Union[AndroidToIosAppMappingDetailField, list[AndroidToIosAppMappingDetailField]] = None

        :returns: self
        :rtype: applaud.endpoints.AndroidToIosAppMappingDetailEndpoint
        '''
        if android_to_ios_app_mapping_detail: self._set_fields('androidToIosAppMappingDetails',android_to_ios_app_mapping_detail if type(android_to_ios_app_mapping_detail) is list else [android_to_ios_app_mapping_detail])
        return self
        
    def get(self) -> AndroidToIosAppMappingDetailResponse:
        '''Get the resource.

        :returns: Single AndroidToIosAppMappingDetail
        :rtype: AndroidToIosAppMappingDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return AndroidToIosAppMappingDetailResponse.parse_obj(json)

    def update(self, request: AndroidToIosAppMappingDetailUpdateRequest) -> AndroidToIosAppMappingDetailResponse:
        '''Modify the resource.

        :param request: AndroidToIosAppMappingDetail representation
        :type request: AndroidToIosAppMappingDetailUpdateRequest

        :returns: Single AndroidToIosAppMappingDetail
        :rtype: AndroidToIosAppMappingDetailResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return AndroidToIosAppMappingDetailResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

