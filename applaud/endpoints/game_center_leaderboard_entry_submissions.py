from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardEntrySubmissionsEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardEntrySubmissions'

    def create(self, request: GameCenterLeaderboardEntrySubmissionCreateRequest) -> GameCenterLeaderboardEntrySubmissionResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardEntrySubmission representation
        :type request: GameCenterLeaderboardEntrySubmissionCreateRequest

        :returns: Single GameCenterLeaderboardEntrySubmission
        :rtype: GameCenterLeaderboardEntrySubmissionResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardEntrySubmissionResponse.parse_obj(json)

