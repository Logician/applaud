from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterAchievementReleasesEndpoint(Endpoint):
    path = '/v1/gameCenterAchievementReleases'

    @deprecated
    def create(self, request: GameCenterAchievementReleaseCreateRequest) -> GameCenterAchievementReleaseResponse:
        '''Create the resource.

        :param request: GameCenterAchievementRelease representation
        :type request: GameCenterAchievementReleaseCreateRequest

        :returns: Single GameCenterAchievementRelease
        :rtype: GameCenterAchievementReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementReleaseResponse.parse_obj(json)

class GameCenterAchievementReleaseEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementReleases/{id}'

    def fields(self, *, game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]]=None) -> GameCenterAchievementReleaseEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_release: the fields to include for returned resources of type gameCenterAchievementReleases
        :type game_center_achievement_release: Union[GameCenterAchievementReleaseField, list[GameCenterAchievementReleaseField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementReleaseEndpoint
        '''
        if game_center_achievement_release: self._set_fields('gameCenterAchievementReleases',game_center_achievement_release if type(game_center_achievement_release) is list else [game_center_achievement_release])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_DETAIL = 'gameCenterDetail'
        GAME_CENTER_ACHIEVEMENT = 'gameCenterAchievement'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementReleaseEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementReleaseEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterAchievementReleaseResponse:
        '''Get the resource.

        :returns: Single GameCenterAchievementRelease
        :rtype: GameCenterAchievementReleaseResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementReleaseResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

