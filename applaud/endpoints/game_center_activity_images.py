from __future__ import annotations
from .base import Endpoint, IDEndpoint, SortOrder, endpoint
from ..fields import *
from typing import Union
from ..schemas.models import *
from ..schemas.responses import *
from ..schemas.requests import *
from ..schemas.enums import *

class GameCenterActivityImagesEndpoint(Endpoint):
    path = '/v1/gameCenterActivityImages'

    def create(self, request: GameCenterActivityImageCreateRequest) -> GameCenterActivityImageResponse:
        '''Create the resource.

        :param request: GameCenterActivityImage representation
        :type request: GameCenterActivityImageCreateRequest

        :returns: Single GameCenterActivityImage
        :rtype: GameCenterActivityImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_post(request)
        return GameCenterActivityImageResponse.parse_obj(json)

class GameCenterActivityImageEndpoint(IDEndpoint):
    path = '/v1/gameCenterActivityImages/{id}'

    def fields(self, *, game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]]=None) -> GameCenterActivityImageEndpoint:
        '''Fields to return for included related types.

        :param game_center_activity_image: the fields to include for returned resources of type gameCenterActivityImages
        :type game_center_activity_image: Union[GameCenterActivityImageField, list[GameCenterActivityImageField]] = None

        :returns: self
        :rtype: applaud.endpoints.GameCenterActivityImageEndpoint
        '''
        if game_center_activity_image: self._set_fields('gameCenterActivityImages',game_center_activity_image if type(game_center_activity_image) is list else [game_center_activity_image])
        return self
        
    def get(self) -> GameCenterActivityImageResponse:
        '''Get the resource.

        :returns: Single GameCenterActivityImage
        :rtype: GameCenterActivityImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a error reponse returned.
                 :py:class:`requests.RequestException`: if a connection or a HTTP error occurred.
        '''
        json = super()._perform_get()
        return GameCenterActivityImageResponse.parse_obj(json)

    def update(self, request: GameCenterActivityImageUpdateRequest) -> GameCenterActivityImageResponse:
        '''Modify the resource.

        :param request: GameCenterActivityImage representation
        :type request: GameCenterActivityImageUpdateRequest

        :returns: Single GameCenterActivityImage
        :rtype: GameCenterActivityImageResponse
        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        json = super()._perform_patch(request)
        return GameCenterActivityImageResponse.parse_obj(json)

    def delete(self):
        '''Delete the resource.

        :raises: :py:class:`applaud.schemas.responses.ErrorResponse`: if a request or a HTTP error occurred.
        '''
        super()._perform_delete()

