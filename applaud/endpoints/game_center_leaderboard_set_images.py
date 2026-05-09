from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardSetImagesEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardSetImages'

    @deprecated
    def create(self, request: GameCenterLeaderboardSetImageCreateRequest) -> GameCenterLeaderboardSetImageResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetImage representation
        :type request: GameCenterLeaderboardSetImageCreateRequest

        :returns: Single GameCenterLeaderboardSetImage
        :rtype: GameCenterLeaderboardSetImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetImageResponse.parse_obj(json)

class GameCenterLeaderboardSetImageEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardSetImages/{id}'

    def fields(self, *, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None) -> GameCenterLeaderboardSetImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetImageEndpoint
        '''
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_SET_LOCALIZATION = 'gameCenterLeaderboardSetLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterLeaderboardSetImageResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSetImage
        :rtype: GameCenterLeaderboardSetImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetImageResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardSetImageUpdateRequest) -> GameCenterLeaderboardSetImageResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSetImage representation
        :type request: GameCenterLeaderboardSetImageUpdateRequest

        :returns: Single GameCenterLeaderboardSetImage
        :rtype: GameCenterLeaderboardSetImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardSetImagesEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboardSetImages'

    def create(self, request: GameCenterLeaderboardSetImageV2CreateRequest) -> GameCenterLeaderboardSetImageV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboardSetImage representation
        :type request: GameCenterLeaderboardSetImageV2CreateRequest

        :returns: Single GameCenterLeaderboardSetImage
        :rtype: GameCenterLeaderboardSetImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardSetImageV2Response.parse_obj(json)

class GameCenterLeaderboardSetImageEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardSetImages/{id}'

    def fields(self, *, game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]]=None) -> GameCenterLeaderboardSetImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_set_image: the fields to include for returned resources of type gameCenterLeaderboardSetImages
        :type game_center_leaderboard_set_image: Union[GameCenterLeaderboardSetImageField, list[GameCenterLeaderboardSetImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetImageEndpoint
        '''
        if game_center_leaderboard_set_image: self._set_fields('gameCenterLeaderboardSetImages',game_center_leaderboard_set_image if type(game_center_leaderboard_set_image) is list else [game_center_leaderboard_set_image])
        return self
        
    class Include(StringEnum):
        LOCALIZATION = 'localization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardSetImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardSetImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterLeaderboardSetImageV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardSetImage
        :rtype: GameCenterLeaderboardSetImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardSetImageV2Response.parse_obj(json)

    def update(self, request: GameCenterLeaderboardSetImageV2UpdateRequest) -> GameCenterLeaderboardSetImageV2Response:
        '''Modify the resource.

        :param request: GameCenterLeaderboardSetImage representation
        :type request: GameCenterLeaderboardSetImageV2UpdateRequest

        :returns: Single GameCenterLeaderboardSetImage
        :rtype: GameCenterLeaderboardSetImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardSetImageV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

