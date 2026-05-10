from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardSetReleasesEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardSetReleases'

    @deprecated
    def create(self, request: GameCenterLeaderboardSetReleaseCreateRequest) -> GameCenterLeaderboardSetReleaseResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetRelease representation
        :type request: GameCenterLeaderboardSetReleaseCreateRequest

        :returns: Single GameCenterLeaderboardSetRelease
        :rtype: GameCenterLeaderboardSetReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetReleaseResponse.parse_obj(json)

class GameCenterLeaderboardSetReleaseEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetReleases/{id}'

    def fields(self, *, game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]]=None) -> GameCenterLeaderboardSetReleaseEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_release: the fields to include for returned resources of type gameCenterLeaderboardSetReleases
        :type game_center_leaderboard_set_release: Union[GameCenterLeaderboardSetReleaseField, list[GameCenterLeaderboardSetReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetReleaseEndpoint
        '''
        if game_center_leaderboard_set_release: self._set_fields('gameCenterLeaderboardSetReleases',game_center_leaderboard_set_release if type(game_center_leaderboard_set_release) is list else [game_center_leaderboard_set_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_LEADERBOARD_SET = 'gameCenterLeaderboardSet'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterLeaderboardSetReleaseResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSetRelease
        :rtype: GameCenterLeaderboardSetReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetReleaseResponse.parse_obj(json)
    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

