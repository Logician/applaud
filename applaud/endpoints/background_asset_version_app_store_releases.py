from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BackgroundAssetVersionAppStoreReleaseEndpoint(IDEndpoint):
    path = '/v1/backgroundAssetVersionAppStoreReleases/{id}'

    def fields(self, *, background_asset_version_app_store_release: Union[BackgroundAssetVersionAppStoreReleaseField, list[BackgroundAssetVersionAppStoreReleaseField]]=None) -> BackgroundAssetVersionAppStoreReleaseEndpoint:
        '''Fields to return for included related types.

        :param background_asset_version_app_store_release: the fields to include for returned resources of type backgroundAssetVersionAppStoreReleases
        :type background_asset_version_app_store_release: Union[BackgroundAssetVersionAppStoreReleaseField, list[BackgroundAssetVersionAppStoreReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetVersionAppStoreReleaseEndpoint
        '''
        if background_asset_version_app_store_release: self._set_fields('backgroundAssetVersionAppStoreReleases',background_asset_version_app_store_release if type(background_asset_version_app_store_release) is list else [background_asset_version_app_store_release])
        return self
        
    class Include(StringEnum):
        BACKGROUND_ASSET_VERSION = 'backgroundAssetVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> BackgroundAssetVersionAppStoreReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetVersionAppStoreReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BackgroundAssetVersionAppStoreReleaseResponse:
        '''Get the resource.

        :returns: Single BackgroundAssetVersionAppStoreRelease
        :rtype: BackgroundAssetVersionAppStoreReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionAppStoreReleaseResponse.parse_obj(json)

