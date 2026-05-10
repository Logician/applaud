from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterAchievementImagesEndpoint(Endpoint):
    path = '/v1/gameCenterAchievementImages'

    @deprecated
    def create(self, request: GameCenterAchievementImageCreateRequest) -> GameCenterAchievementImageResponse:
        '''Create the resource.

        :param request: GameCenterAchievementImage representation
        :type request: GameCenterAchievementImageCreateRequest

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementImageResponse.parse_obj(json)

class GameCenterAchievementImageEndpoint(IDEndpoint):
    path = '/v1/gameCenterAchievementImages/{id}'

    def fields(self, *, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None) -> GameCenterAchievementImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementImageEndpoint
        '''
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        return self
        
    class Include(StringEnum):
        GAME_CENTER_ACHIEVEMENT_LOCALIZATION = 'gameCenterAchievementLocalization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    @deprecated
    def get(self) -> GameCenterAchievementImageResponse:
        '''Get the resource.

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementImageResponse.parse_obj(json)
    @deprecated
    def update(self, request: GameCenterAchievementImageUpdateRequest) -> GameCenterAchievementImageResponse:
        '''Modify the resource.

        :param request: GameCenterAchievementImage representation
        :type request: GameCenterAchievementImageUpdateRequest

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAchievementImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

class GameCenterAchievementImagesEndpoint(Endpoint):
    path = '/v2/gameCenterAchievementImages'

    def create(self, request: GameCenterAchievementImageV2CreateRequest) -> GameCenterAchievementImageV2Response:
        '''Create the resource.

        :param request: GameCenterAchievementImage representation
        :type request: GameCenterAchievementImageV2CreateRequest

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterAchievementImageV2Response.parse_obj(json)

class GameCenterAchievementImageEndpoint(IDEndpoint):
    path = '/v2/gameCenterAchievementImages/{id}'

    def fields(self, *, game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]]=None) -> GameCenterAchievementImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_achievement_image: the fields to include for returned resources of type gameCenterAchievementImages
        :type game_center_achievement_image: Union[GameCenterAchievementImageField, list[GameCenterAchievementImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementImageEndpoint
        '''
        if game_center_achievement_image: self._set_fields('gameCenterAchievementImages',game_center_achievement_image if type(game_center_achievement_image) is list else [game_center_achievement_image])
        return self
        
    class Include(StringEnum):
        LOCALIZATION = 'localization'

    def include(self, relationship: Union[Include, list[Include]]) -> GameCenterAchievementImageEndpoint:
        '''Relationship data to include in the response.

        :returns: self
        :rtype: applaud.endpoints.GameCenterAchievementImageEndpoint
        '''
        if relationship: self._set_includes(relationship if type(relationship) is list else [relationship])
        return self
        
    def get(self) -> GameCenterAchievementImageV2Response:
        '''Get the resource.

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterAchievementImageV2Response.parse_obj(json)
    def update(self, request: GameCenterAchievementImageV2UpdateRequest) -> GameCenterAchievementImageV2Response:
        '''Modify the resource.

        :param request: GameCenterAchievementImage representation
        :type request: GameCenterAchievementImageV2UpdateRequest

        :returns: Single GameCenterAchievementImage
        :rtype: GameCenterAchievementImageV2Response
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterAchievementImageV2Response.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

