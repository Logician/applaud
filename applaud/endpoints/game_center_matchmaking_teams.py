from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterMatchmakingTeamsEndpoint(Endpoint):
    path = '/v1/gameCenterMatchmakingTeams'

    def create(self, request: GameCenterMatchmakingTeamCreateRequest) -> GameCenterMatchmakingTeamResponse:
        '''Create the resource.

        :param request: GameCenterMatchmakingTeam representation
        :type request: GameCenterMatchmakingTeamCreateRequest

        :returns: Single GameCenterMatchmakingTeam
        :rtype: GameCenterMatchmakingTeamResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterMatchmakingTeamResponse.parse_obj(json)

class GameCenterMatchmakingTeamEndpoint(IDEndpoint):
    path = '/v1/gameCenterMatchmakingTeams/{id}'

    def update(self, request: GameCenterMatchmakingTeamUpdateRequest) -> GameCenterMatchmakingTeamResponse:
        '''Modify the resource.

        :param request: GameCenterMatchmakingTeam representation
        :type request: GameCenterMatchmakingTeamUpdateRequest

        :returns: Single GameCenterMatchmakingTeam
        :rtype: GameCenterMatchmakingTeamResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterMatchmakingTeamResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

