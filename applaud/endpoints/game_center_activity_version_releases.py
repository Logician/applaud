from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterActivityVersionReleasesEndpoint(Endpoint):
    path = '/v1/gameCenterActivityVersionReleases'

    @deprecated
    def create(self, request: GameCenterActivityVersionReleaseCreateRequest) -> GameCenterActivityVersionReleaseResponse:
        '''Create the resource.

        :param request: GameCenterActivityVersionRelease representation
        :type request: GameCenterActivityVersionReleaseCreateRequest

        :returns: Single GameCenterActivityVersionRelease
        :rtype: GameCenterActivityVersionReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterActivityVersionReleaseResponse.parse_obj(json)

class GameCenterActivityVersionReleaseEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityVersionReleases/{id}'

    def fields(self, *, game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]]=None) -> GameCenterActivityVersionReleaseEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_version_release: the fields to include for returned resources of type gameCenterActivityVersionReleases
        :type game_center_activity_version_release: Union[GameCenterActivityVersionReleaseField, list[GameCenterActivityVersionReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityVersionReleaseEndpoint
        '''
        if game_center_activity_version_release: self._set_fields('gameCenterActivityVersionReleases',game_center_activity_version_release if type(game_center_activity_version_release) is list else [game_center_activity_version_release])
        return self
        
    class Include(StringEnum):
        VERSION = 'version'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterActivityVersionReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityVersionReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterActivityVersionReleaseResponse:
        '''Get the resource.

        :returns: Single GameCenterActivityVersionRelease
        :rtype: GameCenterActivityVersionReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityVersionReleaseResponse.parse_obj(json)
    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

