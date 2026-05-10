from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardReleasesEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardReleases'

    @deprecated
    def create(self, request: GameCenterLeaderboardReleaseCreateRequest) -> GameCenterLeaderboardReleaseResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardRelease representation
        :type request: GameCenterLeaderboardReleaseCreateRequest

        :returns: Single GameCenterLeaderboardRelease
        :rtype: GameCenterLeaderboardReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardReleaseResponse.parse_obj(json)

class GameCenterLeaderboardReleaseEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardReleases/{id}'

    def fields(self, *, game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]]=None) -> GameCenterLeaderboardReleaseEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_release: the fields to include for returned resources of type gameCenterLeaderboardReleases
        :type game_center_leaderboard_release: Union[GameCenterLeaderboardReleaseField, list[GameCenterLeaderboardReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardReleaseEndpoint
        '''
        if game_center_leaderboard_release: self._set_fields('gameCenterLeaderboardReleases',game_center_leaderboard_release if type(game_center_leaderboard_release) is list else [game_center_leaderboard_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_LEADERBOARD = 'gameCenterLeaderboard'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterLeaderboardReleaseResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardRelease
        :rtype: GameCenterLeaderboardReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardReleaseResponse.parse_obj(json)
    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

