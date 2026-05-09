from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterMatchmakingRuleSetTestsEndpoint(Endpoint):
    path = '/v1/gameCenterMatchmakingRuleSetTests'

    def create(self, request: GameCenterMatchmakingRuleSetTestCreateRequest) -> GameCenterMatchmakingRuleSetTestResponse:
        '''Create the resource.

        :param request: GameCenterMatchmakingRuleSetTest representation
        :type request: GameCenterMatchmakingRuleSetTestCreateRequest

        :returns: Single GameCenterMatchmakingRuleSetTest
        :rtype: GameCenterMatchmakingRuleSetTestResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterMatchmakingRuleSetTestResponse.parse_obj(json)

