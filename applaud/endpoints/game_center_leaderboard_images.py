from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterLeaderboardImagesEndpoint(Endpoint):
    path = '/v1/gameCenterLeaderboardImages'

    @deprecated
    def create(self, request: GameCenterLeaderboardImageCreateRequest) -> GameCenterLeaderboardImageResponse:
        '''Create the resource.

        :param request: GameCenterLeaderboardImage representation
        :type request: GameCenterLeaderboardImageCreateRequest

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardImageResponse.parse_obj(json)

class GameCenterLeaderboardImageEndpoint(IDEndpoint):
    path = '/v1/gameCenterLeaderboardImages/{id}'

    def fields(self, *, game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]]=None) -> GameCenterLeaderboardImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_image: the fields to include for returned resources of type gameCenterLeaderboardImages
        :type game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardImageEndpoint
        '''
        if game_center_leaderboard_image: self._set_fields('gameCenterLeaderboardImages',game_center_leaderboard_image if type(game_center_leaderboard_image) is list else [game_center_leaderboard_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_LEADERBOARD_LOCALIZATION = 'gameCenterLeaderboardLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterLeaderboardImageResponse:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardImageResponse.parse_obj(json)

    @deprecated
    def update(self, request: GameCenterLeaderboardImageUpdateRequest) -> GameCenterLeaderboardImageResponse:
        '''Modify the resource.

        :param request: GameCenterLeaderboardImage representation
        :type request: GameCenterLeaderboardImageUpdateRequest

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterLeaderboardImagesEndpoint(Endpoint):
    path = '/v2/gameCenterLeaderboardImages'

    def create(self, request: GameCenterLeaderboardImageV2CreateRequest) -> GameCenterLeaderboardImageV2Response:
        '''Create the resource.

        :param request: GameCenterLeaderboardImage representation
        :type request: GameCenterLeaderboardImageV2CreateRequest

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterLeaderboardImageV2Response.parse_obj(json)

class GameCenterLeaderboardImageEndpoint(IDEndpoint):
    path = '/v2/gameCenterLeaderboardImages/{id}'

    def fields(self, *, game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]]=None) -> GameCenterLeaderboardImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_leaderboard_image: the fields to include for returned resources of type gameCenterLeaderboardImages
        :type game_center_leaderboard_image: Union[GameCenterLeaderboardImageField, list[GameCenterLeaderboardImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardImageEndpoint
        '''
        if game_center_leaderboard_image: self._set_fields('gameCenterLeaderboardImages',game_center_leaderboard_image if type(game_center_leaderboard_image) is list else [game_center_leaderboard_image])
        return self
        
    class Include(StringEnum):
        LOCALIZATION = 'localization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterLeaderboardImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterLeaderboardImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterLeaderboardImageV2Response:
        '''Get the resource.

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterLeaderboardImageV2Response.parse_obj(json)

    def update(self, request: GameCenterLeaderboardImageV2UpdateRequest) -> GameCenterLeaderboardImageV2Response:
        '''Modify the resource.

        :param request: GameCenterLeaderboardImage representation
        :type request: GameCenterLeaderboardImageV2UpdateRequest

        :returns: Single GameCenterLeaderboardImage
        :rtype: GameCenterLeaderboardImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterLeaderboardImageV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

