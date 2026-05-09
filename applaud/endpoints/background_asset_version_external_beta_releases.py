from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class BackgroundAssetVersionExternalBetaReleaseEndpoint(IDEndpoint):
    path = '/v1/backgroundAssetVersionExternalBetaReleases/{id}'

    def fields(self, *, background_asset_version_external_beta_release: Union[BackgroundAssetVersionExternalBetaReleaseField, list[BackgroundAssetVersionExternalBetaReleaseField]]=None) -> BackgroundAssetVersionExternalBetaReleaseEndpoint:
        '''Fields to return for included related types.

        :param background_asset_version_external_beta_release: the fields to include for returned resources of type backgroundAssetVersionExternalBetaReleases
        :type background_asset_version_external_beta_release: Union[BackgroundAssetVersionExternalBetaReleaseField, list[BackgroundAssetVersionExternalBetaReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetVersionExternalBetaReleaseEndpoint
        '''
        if background_asset_version_external_beta_release: self._set_fields('backgroundAssetVersionExternalBetaReleases',background_asset_version_external_beta_release if type(background_asset_version_external_beta_release) is list else [background_asset_version_external_beta_release])
        return self
        
    class Include(StringEnum):
        BACKGROUND_ASSET_VERSION = 'backgroundAssetVersion'

    def include(self, relationship: Union[Include, list[Include]]) -> BackgroundAssetVersionExternalBetaReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.BackgroundAssetVersionExternalBetaReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> BackgroundAssetVersionExternalBetaReleaseResponse:
        '''Get the resource.

        :returns: Single BackgroundAssetVersionExternalBetaRelease
        :rtype: BackgroundAssetVersionExternalBetaReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return BackgroundAssetVersionExternalBetaReleaseResponse.parse_obj(json)

