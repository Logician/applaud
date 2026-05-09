from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterPlayerAchievementSubmissionsEndpoint(Endpoint):
    path = '/v1/gameCenterPlayerAchievementSubmissions'

    def create(self, request: GameCenterPlayerAchievementSubmissionCreateRequest) -> GameCenterPlayerAchievementSubmissionResponse:
        '''Create the resource.

        :param request: GameCenterPlayerAchievementSubmission representation
        :type request: GameCenterPlayerAchievementSubmissionCreateRequest

        :returns: Single GameCenterPlayerAchievementSubmission
        :rtype: GameCenterPlayerAchievementSubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterPlayerAchievementSubmissionResponse.parse_obj(json)

